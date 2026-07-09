---
tags: [causalops, prompt, memory-layer, claude-code, optional, efficiency]
created: 2026-07-08
task: memory-layer-batch-entity-upserts
model: claude-sonnet-4-6
---

# Prompt 4 (Optional) — Batch the Entity Upserts in SupabaseMemoryStore

> Copy the fenced prompt into a fresh Claude Code session, whenever — this has no dependency on the other three and isn't required to call the memory layer done. Skip it entirely if you're just trying to close out the roadmap item. See [[00 - Memory Layer Completion — Index]].

## Why This Exists

[Independent Review artifact](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1), minor finding: `SupabaseMemoryStore._upsert_entities()` in `src/memory/store.py` (lines 141-163) does one `.upsert().execute()` network round-trip per entity, in a Python loop. For a run with, say, 15 extracted entities, that's 15 sequential HTTP calls to Supabase where one batched upsert would do. Not a bug — correct today — just a latency cost that scales linearly with entity count per run, worth fixing before run volume makes it noticeable, not after.

## Hard Rules

- Scope is exactly `SupabaseMemoryStore._upsert_entities()` and its direct caller `write_run()`. Do not touch `search_similar_runs`, `get_entity_relationships`, or `get_asset_timeline`.
- The return type contract must not change: callers need `dict[(entity_type, entity_value), entity_id]` back, same as today, so `write_run()`'s edge-building step keeps working unmodified.
- Supabase's Python client supports batch upsert by passing a list of row dicts to a single `.upsert(...)` call with `on_conflict="entity_type,entity_value"` — confirm this returns all affected rows (including pre-existing ones matched by the conflict target) in one response before relying on it; if it silently only returns newly-inserted rows and drops conflict-updated ones, you'll need `returning="representation"` or an equivalent explicit flag — check the installed `supabase==2.31.0` / underlying `postgrest-py` client behavior directly rather than assuming.

## Implementation Order

1. Read `src/memory/store.py` in full, specifically `_upsert_entities` (lines 141-163) and its caller in `write_run` (lines 61-63).

2. Rewrite `_upsert_entities` to issue a single batched upsert:
   ```python
   def _upsert_entities(
       self, entity_pairs: list[tuple[str, str]]
   ) -> dict[tuple[str, str], str]:
       if not entity_pairs:
           return {}
       now = datetime.now(UTC).isoformat()
       rows = [
           {"entity_type": t, "entity_value": v, "last_seen": now}
           for t, v in entity_pairs
       ]
       response = (
           self._client.table("memory_entities")
           .upsert(rows, on_conflict="entity_type,entity_value")
           .execute()
       )
       result: dict[tuple[str, str], str] = {}
       for row in _as_rows(response.data):
           key = (row.get("entity_type"), row.get("entity_value"))
           entity_id = row.get("id")
           if key[0] and key[1] and entity_id:
               result[key] = str(entity_id)
       return result
   ```
   Verify this actually returns a row (with `id`) for every entity in `entity_pairs`, including ones that already existed (conflict-matched, not just newly inserted) — this is the exact behavior the existing per-entity loop gave you for free, and `write_run`'s edge-building step silently drops any edge whose endpoint is missing from this dict, so a regression here fails silently rather than loudly.

3. Existing unit tests (`tests/memory/test_extractor.py`, `tests/memory/test_mcp_tools.py`) don't touch `store.py`'s Supabase calls directly (they're mocked or extractor-only) and should be unaffected — run them to confirm: `pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v`.

4. This change can only be meaningfully verified against the real Supabase project. `.env` has working credentials, but a fresh shell does not auto-load them (no dotenv loading anywhere in this repo's test setup) — load them explicitly in the same command:
   ```bash
   set -a && source .env && set +a && pytest tests/memory/test_store.py::test_write_run_inserts_row_and_indexes_entities -v -m integration
   ```
   Confirm this actually ran rather than skipped (an unloaded-credentials run reports as skipped, not failed, and can look like a pass at a glance). It must still pass, and `result["entities_indexed"]` must still equal the number of entities extracted — that's the one thing a batching bug would most likely break silently (fewer indexed than extracted, with no exception).

5. `ruff check src/memory/store.py` and `pyright src/memory/store.py` — clean. (If bare `ruff`/`pyright` aren't found on `PATH`, use `.venv/bin/ruff` / `.venv/bin/pyright`.)

## Report Back

Confirm the integration test in step 4 passed with the batched implementation, and note the entity count it verified (should match the un-batched behavior exactly, just in fewer round-trips).
