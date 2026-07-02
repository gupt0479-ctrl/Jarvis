# Memory Layer Design

The memory layer adds persistent cross-run awareness to CausalOps. Without it, every `run_causalops()` call starts from zero — past runs exist as JSON files in `data/` but nothing reads them. Implementation lives in `src/memory/`.

## What Is Being Built

Five components, each independently testable:

### 1. Vector Store (Supabase pgvector)
Every completed run gets embedded (Azure OpenAI `text-embedding-3-small`) and stored in Supabase. When a new incident arrives, `memory_retrieve_node` retrieves the 3 most similar past runs and passes them as prompt context to the orchestrator.

### 2. Knowledge Graph (Supabase)
Entities extracted from evidence records and causal graphs — assets, MITRE techniques, CVEs, causal variables — stored as nodes and edges in Supabase. Forms a persistent cross-run threat intelligence graph.

### 3. Temporal Indexing
Every stored fact carries a timestamp. Retrieval applies exponential decay:
```
weight = e^(-λ * age_in_days),  λ = 0.023,  half-life ≈ 30 days
```
Recent evidence weighs more than old evidence from the same run.

### 4. MCP Memory Server (src/memory/mcp_server.py)
Standalone FastMCP process on port 8001. Exposes 4 tools:
- `search_similar_incidents` — vector similarity search over past runs
- `get_entity_relationships` — graph traversal for a named entity
- `get_asset_timeline` — temporal index of events for a specific asset
- `write_run_to_memory` — embed + store a completed run

**Runs as a separate process**: `python -m memory.mcp_server`. NOT mounted inside FastAPI. NOT modifying `api.py`.

### 5. Agent Integration (LangGraph Nodes)
Two new nodes added to the workflow:
- `memory_retrieve_node` — runs before the orchestrator; fetches past context and writes it to `GraphState.memory_context`
- `memory_write_node` — runs after DoWhy estimation; embeds + stores the completed run

## Critical Constraints

- **Never pass memory retrieval results as `EvidenceRecord` objects.** Past context goes to `memory_context` (prompt text) only. It cannot enter the causal pipeline as evidence.
- **Never call `embed_text()` directly in async context.** Always: `await asyncio.to_thread(embed_text, text)`. The embedder is a sync function that calls Azure OpenAI.
- **Never use `SUPABASE_PUBLISHABLE_KEY` for Python backend writes.** RLS silently blocks writes. Use `SUPABASE_SERVICE_ROLE_KEY`.

## Module Structure

```
src/memory/
  __init__.py          empty
  embedder.py          embed_text() with 3-attempt backoff (sync, Azure OpenAI)
  extractor.py         extract_entities() + build_edges() (deterministic, no LLM)
  store.py             SupabaseMemoryStore with 4 methods
  nodes.py             memory_retrieve_node + memory_write_node (async)
  mcp_server.py        standalone FastMCP with 4 tools + __main__ block
```

## Supabase Schema

Two tables needed (run SQL in Supabase dashboard):

```sql
-- Run embeddings for vector similarity
create table memory_runs (
  id uuid primary key default gen_random_uuid(),
  run_id text not null,
  task_description text,
  embedding vector(1536),   -- text-embedding-3-small
  metadata jsonb,
  created_at timestamptz default now()
);

-- Entity knowledge graph
create table memory_entities (
  id uuid primary key default gen_random_uuid(),
  run_id text,
  entity_type text,         -- asset | technique | cve | variable
  entity_id text,
  label text,
  metadata jsonb,
  created_at timestamptz default now()
);

create table memory_entity_edges (
  id uuid primary key default gen_random_uuid(),
  run_id text,
  subject text,
  predicate text,
  object text,
  confidence float,
  created_at timestamptz default now()
);
```

## Docker (docker-compose.yml addition)

```yaml
mcp:
  build: .
  command: sh -c "cd src && python -m memory.mcp_server"
  ports:
    - "8001:8001"
  env_file:
    - .env
  environment:
    MCP_TRANSPORT: sse
  depends_on:
    api: {condition: service_healthy}
```

## Related Notes

- [[memory-layer/01-status|Status]] — what's blocked, what can be coded now
- [[agents/01-orchestrator|Orchestrator]] — where memory_context is injected
- [[pipeline/03-graphstate|GraphState]] — memory_context and run_id fields
- [[infrastructure/02-env-vars|Environment Variables]] — Supabase and Azure embedding vars
