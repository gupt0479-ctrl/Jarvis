---
type: prompt
task: mcp-bridge-protocol-test-and-final-housekeeping
status: pending
created: 2026-07-09
tags: [causalops, memory-layer, mcp, testing, claude-code, prompt]
---

# 05 — MCP Protocol Bridge Integration Test and Final Housekeeping

> Prompts 1-4 (now in `claude code/ran/`) closed the coordinator-level memory round trip and doc/schema drift. This prompt closes the one real gap they left: nothing in the repo actually drives the MCP server through the MCP protocol itself. It also cleans up two small nits caught while re-verifying prompts 1-4 against the live repo this session.

## Why This Exists

`tests/memory/test_mcp_tools.py` mocks `SupabaseMemoryStore` and calls the tool
*functions* directly (`mcp_server.search_similar_incidents("...", k=2)`). That
proves the functions delegate correctly. It does **not** prove the MCP server
works as an MCP server — no test ever opens a real client session, lists tools
through the protocol, or calls a tool the way Claude Code/Claude Desktop
actually would (JSON-RPC-style tool invocation, argument validation against
the tool's schema, structured content serialized back). That is the literal
meaning of "integration test for the MCP bridge," and it's currently zero.

This was verified directly this session, live, before writing this prompt —
not assumed:

```python
import asyncio
from fastmcp import Client
from memory import mcp_server

async def main():
    async with Client(mcp_server.mcp) as client:
        tools = await client.list_tools()
        print([t.name for t in tools])
        # -> ['search_similar_incidents', 'get_entity_relationships',
        #     'get_asset_timeline', 'write_run_to_memory']
        result = await client.call_tool("search_similar_incidents", {...})
        result.data  # -> the tool's return value, already deserialized

asyncio.run(main())
```

`Client(mcp_server.mcp)` — passing the live `FastMCP` object directly, not a
URL — makes `fastmcp` infer an in-memory `FastMCPTransport`. No Docker, no
network hop, no subprocess. It still goes through the real protocol layer
(tool discovery, schema validation, request/response serialization); it just
skips the SSE wire transport, which prompt 1 already proved works separately
(`curl http://localhost:8001/sse` → `200 OK`, verified live this session).

A second, live version of the same pattern was also run this session against
the real Supabase project (write_run_to_memory → search_similar_incidents
through the real `Client`, then cleaned up) and worked end to end. This
prompt's acceptance criteria reuse that exact, already-proven shape — there is
no unverified design decision left in this prompt.

## Hard Rules

- The project disables the pytest-asyncio plugin (`pyproject.toml`:
  `addopts = "... -p no:asyncio"`). Every test that awaits the `Client` must be
  a plain `def test_...()` that wraps an inner `async def` and calls it with
  `asyncio.run(...)` — the same pattern already used in
  `tests/memory/test_end_to_end.py`. Do NOT write `async def test_...` — it
  will silently not run as a coroutine under this config.
- Do not touch `dataset_compiler.py` or `estimators.py`.
- Do not modify `tests/memory/test_end_to_end.py`, `test_store.py`,
  `test_nodes.py`, or `test_extractor.py` — this prompt is additive only.
- Do not add temporal-decay math verification or a memory-row retention/
  deletion strategy. Both are real, already-identified gaps (see
  `claude code/ran/00 - Memory Layer Completion — Index.md`, "Caught While
  Verifying" section, and `Memory Layer Implementation Plan.md` section 11,
  "Open Questions — Not Blocking") but neither is in scope here. Flag them
  back if you think they need their own prompt; do not implement them now.
- Do not touch the pre-existing `tsc --noEmit` errors in
  `SpatiotemporalKGPanel.client.tsx` or `causalops-api.ts` — confirmed this
  session to be unrelated to the memory layer's `types.ts` regeneration
  (they don't reference `memory_runs`/`memory_entities`/`memory_entity_edges`
  at all). Out of scope.

## Task 1 — Protocol-level unit tests (no credentials)

Add to `tests/memory/test_mcp_tools.py` (do not create a new file for this
part — it belongs with the existing mocked-store tool tests):

```python
import asyncio

from fastmcp import Client


def test_list_tools_exposes_all_four_tools() -> None:
    async def _list() -> list[str]:
        async with Client(mcp_server.mcp) as client:
            tools = await client.list_tools()
            return [tool.name for tool in tools]

    names = asyncio.run(_list())
    assert set(names) == {
        "search_similar_incidents",
        "get_entity_relationships",
        "get_asset_timeline",
        "write_run_to_memory",
    }


def test_search_similar_incidents_round_trips_through_mcp_protocol() -> None:
    mock_store = MagicMock()
    mock_store.search_similar_runs.return_value = [
        {"run_id": "run-1", "similarity": 0.9}
    ]

    async def _call() -> list[dict]:
        with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
            async with Client(mcp_server.mcp) as client:
                result = await client.call_tool(
                    "search_similar_incidents",
                    {"description": "lateral movement", "k": 2},
                )
                return result.data

    data = asyncio.run(_call())
    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
    assert data == [{"run_id": "run-1", "similarity": 0.9}]
```

`MagicMock`, `patch`, and `mcp_server` are already imported at the top of this
file — only the `asyncio` import and `from fastmcp import Client` need adding.
This deliberately reuses the mocked-store pattern already in the file; the
new part is going through `Client(...)`/`call_tool(...)` instead of calling
`mcp_server.search_similar_incidents(...)` directly, so it actually exercises
tool registration and the protocol's argument/response marshaling.

## Task 2 — Live MCP bridge round trip (integration)

Create `tests/memory/test_mcp_bridge.py`:

```python
"""Live round-trip test through the actual MCP protocol layer.

`tests/memory/test_mcp_tools.py` mocks ``SupabaseMemoryStore`` and never opens
a real client session — it proves the tool wrappers delegate correctly, not
that the MCP bridge itself works end to end. This test opens a real
``fastmcp.Client`` session against the live ``mcp`` server object (in-memory
transport — no Docker, no network hop, but the same protocol layer prompt 1's
``curl http://localhost:8001/sse`` check exercises over SSE) and calls
``write_run_to_memory`` then ``search_similar_incidents`` exactly as an MCP
client (Claude Code, Claude Desktop) would, against the real Supabase
project. Skipped automatically unless real Supabase credentials are
configured — see ``tests/memory/test_store.py`` for the same pattern. Run
with:

    pytest tests/memory/test_mcp_bridge.py -v -m integration
"""

from __future__ import annotations

import asyncio
import os
import uuid

import pytest
from fastmcp import Client

from memory import mcp_server
from memory.store import SupabaseMemoryStore

pytestmark = pytest.mark.integration

_SKIP_REASON = "Real Supabase credentials not configured in .env"


def _has_credentials() -> bool:
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key


requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)


@pytest.fixture
def tagged_run():
    tag = f"mcp-bridge-{uuid.uuid4().hex[:8]}"
    run_id = f"{tag}-run-1"
    yield {"tag": tag, "run_id": run_id}
    store = SupabaseMemoryStore()
    store._client.table("memory_entity_edges").delete().eq(
        "source_run_id", run_id
    ).execute()
    store._client.table("memory_runs").delete().eq("run_id", run_id).execute()
    store._client.table("memory_entities").delete().like(
        "entity_value", f"{tag}%"
    ).execute()


@requires_credentials
def test_write_then_search_round_trips_through_real_mcp_client(tagged_run) -> None:
    tag = tagged_run["tag"]
    run_id = tagged_run["run_id"]
    task_description = f"Incident {tag}: MCP bridge protocol round trip"

    async def _round_trip() -> tuple[dict, list[dict]]:
        async with Client(mcp_server.mcp) as client:
            write_result = await client.call_tool(
                "write_run_to_memory",
                {
                    "run_artifact": {
                        "run_id": run_id,
                        "task_description": task_description,
                        "memos": [],
                        "causal_graph": {},
                        "causal_estimate_report": {},
                    }
                },
            )
            search_result = await client.call_tool(
                "search_similar_incidents",
                {"description": task_description, "k": 3},
            )
            return write_result.data, search_result.data

    write_data, search_data = asyncio.run(_round_trip())

    assert write_data["run_id"] == run_id
    assert any(row.get("run_id") == run_id for row in search_data)
```

This exact shape (fixture, tagging, teardown, assertions) was run live this
session against the real Supabase project and passed — you are implementing a
proven design, not inventing one. Do not simplify away the tagging/cleanup —
it is what keeps repeated runs of this test from polluting the live
`memory_runs`/`memory_entities` tables.

## Task 3 — Two small housekeeping fixes

1. **`CLAUDE.md`** — the "Status" paragraph currently ends with a bare
   Obsidian wikilink that means nothing outside the Jarvis vault:
   ```
   Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].
   ```
   Replace it with plain text. Run the full memory suite first
   (`set -a && source .env && set +a && pytest tests/memory/ -v`), then write
   a sentence that states the *actual* result of that run (e.g. which files
   pass, whether the MCP bridge round trip passes) — do not hardcode a
   "PASSING" claim without having just run it in this same session.

2. **`.gitignore`** — add a `supabase/` entry. Running
   `npx supabase gen types typescript --project-id ...` (as prompt 2 did)
   creates `supabase/.temp/` (CLI link-cache — a project ref and org ID, no
   secrets) as an untracked, un-ignored directory. Add it near the existing
   `.env`/`data/` entries so it doesn't get committed by accident later.

## What NOT to Do

- Don't re-run the SQL migration or re-verify RLS policy decisions — already
  settled (see `claude code/ran/00 - Memory Layer Completion — Index.md`).
- Don't re-litigate whether the MCP server should be Docker/SSE vs
  stdio-only — prompt 1 already fixed and live-verified the Docker/SSE path
  (`causalops-mcp-1` container, confirmed running, `curl` returns
  `200 OK` + `text/event-stream`, clean logs).
- Don't touch `src/memory/mcp_server.py`'s tool implementations, `store.py`,
  `embedder.py`, or `extractor.py` — this prompt is test coverage and
  documentation only.
- Don't run `pytest tests/memory -m integration` from a tool-sandboxed shell
  and trust a hang as a pass or fail — run it from a real terminal, and
  always `set -a && source .env && set +a` first in the same shell
  invocation, or the test will silently **skip** rather than run, and a skip
  is not a pass.

## Acceptance Criteria

1. `pytest tests/memory/test_mcp_tools.py -v` — all pass, zero credentials
   needed, includes the two new protocol-level tests.
2. `set -a && source .env && set +a && pytest tests/memory/test_mcp_bridge.py -v -m integration`
   — must show `1 passed`, not skipped. If it skips, credentials didn't reach
   the process — stop and say so, don't report this done.
3. `set -a && source .env && set +a && pytest tests/memory/ -v` — full memory
   suite, all pass, zero skips anywhere under `tests/memory/`. Paste the
   final summary line.
4. `pytest tests/ -m "not integration and not kafka"` — confirm no
   regression in the rest of the suite (was 88 passed before this prompt).
5. `ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py`
   and `pyright tests/memory/test_mcp_bridge.py` — both clean.
6. Post-teardown check: after the integration test runs, directly query
   `memory_runs`/`memory_entity_edges`/`memory_entities` (via
   `SupabaseMemoryStore()._client...`) for the tagged run/entity values and
   confirm nothing remains — prove cleanup actually worked, don't just trust
   the fixture code path.
7. `git diff CLAUDE.md` shows only the wikilink line replaced, nothing else
   changed. `git diff .gitignore` shows only the added `supabase/` line.

## Related Notes

- `claude code/ran/00 - Memory Layer Completion — Index.md` — prompts 1-4,
  now archived, that this prompt follows on from.
- `claude code/ran/03 - End-to-End Memory Verification and Integration Gate.md`
  — the coordinator-level round trip this prompt's Task 2 complements (that
  one proves the coordinator ↔ Supabase loop; this one proves the MCP client
  ↔ server protocol loop — together they cover the whole memory layer's
  external surface).
- `Memory Layer Implementation Plan.md` section 11 ("Open Questions — Not
  Blocking") — where the deferred temporal-decay-verification and
  retention-strategy items are tracked for whenever they get picked up.
