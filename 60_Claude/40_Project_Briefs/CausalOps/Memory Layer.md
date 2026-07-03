---
type: project
status: sprout
created: 2026-07-02
tags: [causalops, memory, supabase, vector-store, mcp, complete]
---

# Memory Layer

> **Status:** Complete. All src/memory/ files written, coordinator phases wired, 10 unit tests passing. Supabase project provisioned (glbmdbwqmuttykhicasq). Pending: SQL migration + integration tests.

The Persistent Semantic Memory and Retrieval Layer adds durable cross-run memory to CausalOps. Every completed run is embedded and stored; new incidents retrieve past context before the orchestrator runs. Implementation lives in `src/memory/`.

## Five Components

### 1. Vector Store (embedder.py + store.py)
Every completed run is embedded using `text-embedding-3-small` via Azure OpenAI and stored in Supabase pgvector (`memory_runs` table). New incidents retrieve the 3 most similar past runs before the orchestrator decomposes the incident.

### 2. Knowledge Graph (extractor.py + store.py)
Entities extracted from evidence records and causal graphs (assets, MITRE techniques, CVEs, causal variables) are persisted as nodes and edges across runs in `memory_entities` and `memory_entity_edges` tables.

### 3. Temporal Indexing
Retrieval applies exponential decay to cosine similarity:
```python
score = cosine_similarity * exp(-0.023 * age_in_days)
# 30-day half-life -- recent runs weigh more than old ones
```

### 4. MCP Server (mcp_server.py)
Standalone FastMCP process. Runs as `python -m memory.mcp_server` on port 8001. NOT mounted inside FastAPI -- `api.py` is not modified. See docker-compose.yml `mcp` service.

Four tools:
- `search_similar_incidents` -- vector similarity search over past runs
- `get_entity_relationships` -- graph traversal for a named entity
- `get_asset_timeline` -- temporal index for a specific asset
- `write_run_to_memory` -- embed + store a completed run

### 5. Agent Integration (nodes.py)
Two coordinator phases added to `runner.py::execute_run()`:
- `memory_retrieve_node` -- before orchestrator: retrieves 3 similar past runs, writes result to `GraphState.memory_context`
- `memory_write_node` -- after policy_learning: embeds + stores the completed run

Both phases are awaited directly (no `asyncio.to_thread`). Both are wrapped in `try/except` -- a Supabase outage must never fail a run.

**Critical rule:** Memory retrieval results go into the orchestrator prompt only -- never as `EvidenceRecord` objects.

## Implementation Files

```
src/memory/
  __init__.py      empty package marker
  embedder.py      embed_text(str) -> list[float]  Azure text-embedding-3-small
  extractor.py     extract_entities() + build_edges() -- deterministic, no LLM
  store.py         SupabaseMemoryStore (4 methods: write_run, search_similar_runs,
                   get_entity_relationships, get_asset_timeline)
  nodes.py         memory_retrieve_node, memory_write_node (async)
  mcp_server.py    FastMCP instance + 4 tools, standalone process
```

## Coordinator Phase Sequence (after memory integration)

```
memory_retrieve -> orchestrator -> parent_evolution -> parents (Kafka barrier)
  -> gather_children -> child_evolution -> children (Kafka barrier) -> evaluator
  -> causal_loop (synthesis + dowhy, retries) -> reasoner -> policy_learning
  -> memory_write -> completed
```

## Supabase Schema

**Project:** `glbmdbwqmuttykhicasq`

**Tables:**
- `memory_runs` -- run embeddings + metadata (pgvector column, 1536-dim)
- `memory_entities` -- extracted entities (assets, techniques, CVEs, graph nodes)
- `memory_entity_edges` -- entity relationships across runs

**RPC functions:**
- `search_similar_runs(query_embedding, match_count, decay_lambda)`
- `get_entity_neighborhood(p_entity_value, p_entity_type)`

## Tests

```
tests/memory/
  test_extractor.py   unit tests, no credentials -- extract_entities() + build_edges()
  test_mcp_tools.py   unit tests, mock store -- each MCP tool function
  test_store.py       integration (@pytest.mark.integration) -- needs SUPABASE_SERVICE_ROLE_KEY
  test_nodes.py       integration (@pytest.mark.integration) -- needs real .env
```

Run unit tests only:
```bash
pytest tests/ -m "not integration and not kafka"
pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v
```

## Pending (remaining ops steps)

1. Run SQL migration on Supabase project `glbmdbwqmuttykhicasq` -- enables pgvector, creates tables + RPC functions. SQL is in [[Memory Layer Implementation Plan]].
2. Run integration tests: `pytest tests/memory/ -m integration -v` -- requires SUPABASE_SERVICE_ROLE_KEY + Azure embedding credentials in `.env`.

## Key Invariants

1. `embed_text()` is synchronous -- always wrap: `await asyncio.to_thread(embed_text, text)`
2. Use `SUPABASE_SERVICE_ROLE_KEY` (never anon key) for all Python backend writes
3. Memory context -> orchestrator prompt only. Never `EvidenceRecord`.
4. Do not modify `dataset_compiler.py` or `estimators.py`

## Related Notes

- [[Memory Layer Implementation Plan]] -- full schema SQL, implementation history, ADRs
- [[Environment Variables]] -- Supabase + Azure embedding credentials
- [[Coordinator Execution Model]] -- where memory_retrieve and memory_write fit
- [[_Index]] -- back to master index
