---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - memory
  - supabase
  - pgvector
next: "[[CausalOps — Index]]"
---

# Memory Layer

## Status

**Implementation: Complete**

All `src/memory/` files written. Coordinator phases wired. RunRecord serialization updated. Agent integration (nodes.py) done. 10 unit tests passing.

Supabase project provisioned: `glbmdbwqmuttykhicasq`

Pending:
1. Run SQL migration on Supabase project glbmdbwqmuttykhicasq
2. Add credentials to `.env` (SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, AZURE_OPENAI_EMBEDDING_DEPLOYMENT)
3. Run `pytest tests/memory/ -m integration -v`

## What It Does

Every completed CausalOps run starts from zero. Past runs exist as JSON files in `data/` but nothing reads them. The memory layer fixes this.

Five components:

1. **Vector store** (Supabase pgvector) — every completed run is embedded (Azure OpenAI `text-embedding-3-small`, 1536-dim) and stored in `memory_runs`. New incidents retrieve 3 most similar past runs.
2. **Knowledge graph** (Supabase, `memory_entities` + `memory_entity_edges`) — entities extracted from evidence records and causal graphs (assets, MITRE techniques, CVEs, graph nodes) persist across runs.
3. **Temporal indexing** — exponential decay (`e^(-λ * age_in_days)`, λ = 0.023, half-life 30 days) applied at query time. Recent evidence weighs more.
4. **MCP server** — standalone FastMCP on port 8001, NOT mounted in FastAPI. Exposes: `search_similar_incidents`, `get_entity_relationships`, `get_asset_timeline`, `write_run_to_memory`.
5. **Agent integration** — two coordinator phases: `memory_retrieve` (before orchestrator) and `memory_write` (after policy_learning).

## Supabase Schema

Tables: `memory_runs`, `memory_entities`, `memory_entity_edges`.

Key columns:
- `memory_runs.task_embedding` — `extensions.vector(1536)` — HNSW index
- `memory_entities.entity_type` — one of: `asset`, `technique`, `cve`, `graph_node`
- `memory_entity_edges.relationship` — text label, e.g., "exploits", "lateral_move_to"

RPCs: `search_similar_runs(query_embedding, match_count, decay_lambda)`, `get_entity_neighborhood(entity_id, depth)`.

Full SQL migration is in `60_Claude/40_Project_Briefs/CausalOps/Memory Layer Implementation Plan.md`.

## Azure OpenAI (Embeddings Only)

The memory layer uses Azure OpenAI ONLY for embeddings. The chat LLM is Gemini.

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

Never call `embed_text()` directly in an async context -- it is synchronous and must be wrapped:
```python
embedding = await asyncio.to_thread(embed_text, text)
```

## MCP Server

Standalone FastMCP app, not mounted in FastAPI. Starts separately:
```bash
docker-compose up mcp   # port 8001
```

`api.py` is NOT modified for the MCP server. The `mcp` service is a separate container with its own entrypoint.

## Coordinator Integration

Both memory phases are called directly (not via `asyncio.to_thread`) because they are already async:

```python
await _run_memory_retrieve(record, store)   # before orchestrator
# ... all coordinator phases ...
await _run_memory_write(record, store)       # after policy_learning
```

Both wrapped in `try/except Exception` that logs and swallows. A Supabase outage must not fail a run.

## memory_context in GraphState

`GraphState.memory_context` is `list[dict[str, Any]] | None` -- a list of serialized past run summaries. NOT a string.

The orchestrator formats it with `_format_memory_context()`:
```python
ctx = state.get("memory_context") or []
if ctx:
    prompt += "\n\n## Relevant Past Incidents\n" + _format_memory_context(ctx)
```

Memory context goes into the orchestrator prompt only. Never inject it as `EvidenceRecord` objects.

## Source Files

| File | Purpose |
|------|---------|
| `src/memory/__init__.py` | Package init |
| `src/memory/embedder.py` | `embed_text(str) -> list[float]` — Azure text-embedding-3-small |
| `src/memory/extractor.py` | Deterministic entity extraction from run artifacts (no LLM) |
| `src/memory/store.py` | `SupabaseMemoryStore` — 4 methods: write_run, search_similar_runs, get_entity_relationships, get_asset_timeline |
| `src/memory/nodes.py` | `memory_retrieve_node`, `memory_write_node` — async coordinator phases |
| `src/memory/mcp_server.py` | FastMCP instance + 4 tools, standalone process |
| `tests/memory/` | 10 unit tests (test_extractor.py, test_mcp_tools.py) + integration tests (test_store.py, test_nodes.py) |

## Related Notes

- [[CausalOps — Index]] -- project index and pending steps
- [[pipeline-coordinator]] -- how memory phases fit in execute_run
- [[agents]] -- memory_context injection in orchestrator node
- [[infrastructure]] -- env vars for Supabase and Azure embeddings
- `60_Claude/40_Project_Briefs/CausalOps/Memory Layer Implementation Plan.md` -- full SQL migration
