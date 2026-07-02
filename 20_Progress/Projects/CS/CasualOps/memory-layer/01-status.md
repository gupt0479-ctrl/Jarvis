# Memory Layer Status

Current implementation state as of 2026-07-01. The memory layer is being implemented in a separate Claude Code session running inside the CausalOps repo.

## What's Blocked (Requires Live Credentials)

Integration tests cannot run until these are in `.env`:

```env
SUPABASE_URL=https://<new-project-ref>.supabase.co   # project must be provisioned via Supabase MCP first
SUPABASE_SERVICE_ROLE_KEY=...    # required for backend writes (RLS)
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

> **Note:** The old project ID `glbmdbwqmuttykhicasq` does not exist under the account. A new Supabase project must be created first (via Supabase MCP or dashboard) before any URL or keys are known.

The Supabase tables (`memory_runs`, `memory_entities`, `memory_entity_edges`) also need to be provisioned via migration (see [[memory-layer/00-design|Memory Layer Design]]) before `store.py` can write.

Also blocked: running the MCP server against Supabase, and executing `memory_write_node` in a real run.

## What Can Be Coded Now (No Credentials)

All pure-logic modules are credential-free and can be implemented and unit-tested immediately:

**`embedder.py`** — calls Azure OpenAI. Testable with mock responses. The 3-attempt retry backoff is pure logic.

**`extractor.py`** — `extract_entities()` + `build_edges()`. Takes evidence records and causal graph dicts. Returns entity lists. Pure Python, no external calls. Has unit tests in `tests/memory/test_extractor.py`.

**`mcp_server.py`** — FastMCP setup, tool definitions, `__main__` block. Import-testable without credentials. `python -c "from memory.mcp_server import mcp"` should work immediately.

**`store.py`** — SupabaseMemoryStore class with 4 methods. Can be coded and mock-tested without live Supabase.

**`nodes.py`** — `memory_retrieve_node` + `memory_write_node`. Pure async orchestration logic. Unit-testable with mock store.

## Test Plan

```
tests/memory/
  test_extractor.py   unit tests (no credentials) — fixture artifact, entity extraction
  test_mcp_tools.py   unit tests (mock store) — each of the 4 MCP tools
  test_store.py       integration (needs .env) — marked @pytest.mark.integration
  test_nodes.py       integration (needs .env) — marked @pytest.mark.integration
```

Run unit tests only:
```bash
cd /home/anant_gupta/projects/hub/CausalOps
pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v
```

Run integration tests (after credentials are in .env):
```bash
pytest tests/memory/ -m integration -v
```

## Implementation Order

Defined in the first session prompt. Key sequence:
1. `src/memory/__init__.py` (empty)
2. `src/memory/embedder.py`
3. `src/memory/extractor.py`
4. `tests/memory/test_extractor.py`
5. `src/memory/store.py`
6. `src/memory/nodes.py`
7. `src/memory/mcp_server.py`
8. `.mcp.json` at repo root
9. Modify `src/schema.py` — add `memory_context: list[dict[str, Any]] | None` to GraphState
10. Modify `src/engine.py` — add `"memory_context": None` to `initial_state` (`run_id` is already present at line 61)
11. Modify `src/graph.py` — insert memory nodes (**cosmetic only** — graph.py is deprecated for execution in Phase 2b; real wiring is in step 12)
12. Modify `src/coordinator/runner.py` — add `_run_memory_retrieve` (before `_run_orchestrator`) and `_run_memory_write` (after `_run_policy_learning`). See [[pipeline/02-coordinator|Coordinator]] for exact placement and error-handling requirements.
13. Modify `src/agents.py` — inject memory_context into orchestrator prompt using `_format_memory_context()`
14. Modify `docker-compose.yml` — add mcp service
15. Add to requirements.txt: supabase==2.15.2, openai==1.91.0, fastmcp==3.2.4, httpx==0.28.1
16. `tests/memory/test_mcp_tools.py`

Files that must NOT be modified: `src/dataset_compiler.py`, `src/estimators.py`.

## Related Notes

- [[memory-layer/00-design|Memory Layer Design]] — full component description
- [[infrastructure/02-env-vars|Environment Variables]] — which vars are needed and where
