---
tags: [causalops, prompt, memory-layer, claude-code, testing, integration, supabase]
created: 2026-07-08
task: memory-layer-e2e-test-and-integration-gate
model: claude-sonnet-4-6
---

# Prompt 3 — Write the Missing End-to-End Memory Test, Then Run the Full Suite as the Acceptance Gate

> Copy the fenced prompt into a fresh Claude Code session. Run this **after** [[01 - Fix MCP Server Deployment and Housekeeping]] and [[02 - Close Documentation and Schema Drift]] are both done, so the report this prompt produces reflects a consistent state. See [[00 - Memory Layer Completion — Index]].

## Why This Exists

`Memory Layer Implementation Plan.md`, section 8 (Implementation Sequence), step 19:

> Full end-to-end test: POST `/run` with demo evidence, check Supabase dashboard for memory row, POST `/run` again and verify `memory_context` appears in orchestrator.

This step was **never done**. Confirmed this session: `grep -rl "execute_run\|run_causalops" tests/` finds only `tests/test_coordinator_runner.py` (mocked nodes, no Supabase, asserts nothing about memory) and `tests/test_api_async_run.py` (asserts HTTP status codes, not memory retrieval). Nothing in the repo proves that two sequential runs actually round-trip through memory via the real coordinator — every existing memory test calls `store.write_run()` / `memory_retrieve_node()` / `memory_write_node()` in isolation, never through `execute_run()`.

This is the single most important thing left. Everything else in this batch of prompts is cleanup; this is the actual proof that the memory layer does what it was built to do.

Separately, the [Independent Review](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1) couldn't get a conclusive result running `pytest tests/memory -m integration` — it hung with zero output for several minutes in a tool-sandboxed shell, while a direct MCP call to the live server succeeded immediately. Run the integration suite for real this time, in an unsandboxed terminal, and treat a clean pass as the gate.

## Ground Truth Going In (don't re-derive, just use this)

- `.env` already has real, working `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` / Azure embedding credentials — confirmed working this session via a live `search_similar_incidents` call.
- The live Supabase project currently has **0 rows in `memory_runs`** and 4 pre-existing rows in `memory_entities` (orphaned from an earlier test run whose cleanup correctly left entities in place — entities persist across runs by design, this is not something to fix). Don't assume a clean slate will still be true when you run this — query row counts first if it matters to your assertions, and always filter your own assertions by the specific `run_id`s and entity values you created, never by "the only row in the table."
- `tests/test_coordinator_runner.py` is the reference pattern for driving `execute_run()` with fake LLM nodes. Read it in full before writing anything. Key things it already tells you:
  - Fake `agents.grand_orchestrator_node`, `agents.parent_agent_node`, `agents.child_agent_node`, `evaluator.evaluate_memos_node`, `causal.causal_synthesis_node`, `causal.dowhy_engine_node` by installing fake modules into `sys.modules` before calling `execute_run` (see its `_install_fake_nodes` helper) — these are the only nodes that need faking.
  - `evolution.py`, `reasoning.py`, `policy_learning.py` are deterministic and run for real, unmocked, with no issues — do not fake these.
  - No Kafka mocking is needed — `execute_run` already has a working no-Kafka in-process path; the existing test relies on this with zero special setup, so don't add any.
  - Use an isolated `RunStore(db_path=tmp_path / "runs.db")` via `set_run_store` — this only isolates local SQLite state. **It does not isolate the Supabase writes** — `memory_write_node` always talks to the real project from `.env`, regardless of which local `RunStore` is in play. Plan cleanup accordingly.
  - `monkeypatch.setattr("coordinator.runner.publish_telemetry", lambda **_: None)` and the same for `bind_from_state` avoid needing a real telemetry bus.

## Hard Rules

- **Load real credentials into the shell before running anything integration-marked.** `.env` is never auto-loaded (confirmed: no dotenv loading anywhere in this repo's pytest/conftest setup) — a fresh shell has empty `SUPABASE_URL`/`SUPABASE_SERVICE_ROLE_KEY` even though `.env` has real values on disk. Every pytest invocation in this prompt that needs to actually run (not skip) the integration tests must be preceded, in the *same* shell call, by:
  ```bash
  set -a && source .env && set +a
  ```
  This is the exact trap the [Independent Review](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1) hit. Skipping this step doesn't make the gate fail loudly — it makes every integration test report as **skipped**, and `pytest`'s summary line still reads as a clean run with zero failures. A skip is not a pass. Before treating any pytest output as satisfying the gate in steps 3-5, check the summary line explicitly shows tests *run*, not skipped (e.g. `12 passed` vs `10 passed, 2 skipped`) — if your new integration test shows up in the skipped count, the credentials didn't make it into the process environment and the gate has not actually been met.
- This test writes to the **real, shared** Supabase project. There is no separate test project. Every row it creates must be identifiable by a unique, greppable tag and deleted in a `finally`/fixture teardown — including entities, which none of the existing tests bother cleaning up (that's why 4 orphaned rows already exist; don't add to the pile).
- Never assert on absolute table contents ("the only row is..."). Always filter by the specific `run_id`s / entity values this test itself created.
- Mark the new test `@pytest.mark.integration` and skip it with the same `_has_credentials()` pattern already used in `tests/memory/test_store.py` and `tests/memory/test_nodes.py` — copy that helper, don't reinvent it.
- Do not modify `dataset_compiler.py` or `estimators.py`. Not touched by this work; still off-limits.
- Do not weaken any existing test to make this one pass.

## Implementation Order

1. Read `tests/test_coordinator_runner.py` in full, and `tests/memory/test_store.py` + `tests/memory/test_nodes.py` for the credentials-skip pattern and cleanup convention.

2. Create `tests/memory/test_end_to_end.py`. Structure:
   - A fixture that generates two unique, related task descriptions and a shared unique tag for this test run, e.g. `tag = f"e2e-{uuid.uuid4().hex[:8]}"`, and asset/technique/CVE IDs prefixed with it (`f"{tag}-host-01"`, etc.) so cleanup can find everything by tag.
   - **Run 1**: fake the LLM nodes as in `test_coordinator_runner.py`, but give `fake_estimator` a *real-looking, non-withheld* result this time — e.g. `{"ate": -0.31, "method": "backdoor.linear_regression", "n_rows": 80}` — and give `fake_causal` a `causal_payload.graph` with real node/edge data using the tagged asset/technique IDs (mirror the shape in `tests/memory/test_store.py`'s `run_artifact` fixture). Also set `evidence_records` on the state to a list containing the tagged `asset_id`/`technique_id`/`cve_id`. Call `execute_run(task_description=<task 1>, run_id=<unique>, correlation_id=<same>, store=store)`.
   - Confirm the write landed: query `SupabaseMemoryStore().search_similar_runs(<task 1>, k=5)` and assert a row with this run's `run_id` is present.
   - **Run 2**: same fake-node setup, but a task description deliberately worded to closely resemble task 1 (same incident type, same key nouns) so real cosine similarity ranks it high. Call `execute_run(task_description=<task 2>, run_id=<different unique id>, ...)`.
   - **The actual assertion that matters**: inspect the `final_state` (or `store.get_run(run_id_2).memory_context`) from run 2 and assert:
     - `memory_context` is non-empty,
     - it contains an entry whose `run_id` equals run 1's `run_id`,
     - that entry's `ate`, `method`, and `n_rows` match what run 1's fake estimator produced.
     This proves the full loop: `memory_write_node` → Supabase → `memory_retrieve_node` → `GraphState.memory_context`, through the real coordinator, not just through isolated unit calls.
   - Also assert `agents._format_memory_context(...)`-shaped text would be non-empty for run 2's context (call the real function from `agents.py` directly with run 2's `memory_context` and assert it contains run 1's `run_id` string) — this closes the review's other observation that the non-null-ATE formatting branch had zero test coverage; the withheld-ATE branch is already implicitly covered elsewhere.
   - Teardown (`finally` or a fixture, not best-effort): delete `memory_entity_edges` where `source_run_id` is either run's `run_id`; delete `memory_runs` where `run_id` is either run's `run_id`; delete `memory_entities` where `entity_value LIKE '{tag}%'`. Run this even if assertions fail — use `try/finally` or a yielding pytest fixture, not code that only runs on the happy path.

3. Run the new test in isolation first, with credentials loaded:
   ```bash
   set -a && source .env && set +a && pytest tests/memory/test_end_to_end.py -v -m integration
   ```
   Confirm the test actually ran (not skipped) before iterating further. Iterate until it passes for real — don't move on with a skipped or xfailed result.

4. Now run the full memory suite as the acceptance gate, **from a real terminal, not a tool-sandboxed shell**, credentials loaded in the same command:
   ```bash
   set -a && source .env && set +a && pytest tests/memory/ -v
   ```
   Expect all tests to pass and none of the `integration`-marked ones to show as skipped (unit tests always run; integration tests now run for real since credentials are loaded). Paste the full summary line and confirm the skip count is 0 for anything under `tests/memory/`. If anything fails, fix it — this is the gate, not a status report on a known-broken state.

5. Run `pytest tests/ -m "not integration and not kafka"` (the full non-integration suite, no credentials needed) once more to confirm nothing outside `tests/memory/` regressed from anything touched in this session.

6. `ruff check tests/memory/test_end_to_end.py` and `pyright tests/memory/test_end_to_end.py` — both clean. (If bare `ruff`/`pyright`/`pytest` aren't found on `PATH`, this repo's tools live in `.venv/bin/` — use `.venv/bin/<tool>` instead.)

7. Query the live tables one more time after your teardown ran, with credentials still loaded (`SupabaseMemoryStore()._client.table("memory_runs").select("run_id").execute()` or equivalent) and confirm neither of this test's `run_id`s is still present — prove the cleanup actually worked, don't just trust the code path.

## Report Back

- Full pass/fail output from step 4, including the explicit skip count.
- Confirmation from step 7 that cleanup left no residue.
- If credentials were somehow missing when you started (they shouldn't be — verified present in `.env` this session, just not auto-loaded), say so explicitly and stop; do not report this phase done on the strength of unit tests — or a suite full of skips — alone.
