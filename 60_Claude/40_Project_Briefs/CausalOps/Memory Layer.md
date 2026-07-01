---
tags: [causalops, memory, supabase, vector-store, mcp, planned]
---

# Memory Layer (Planned — Not Yet Implemented)

> **Status:** Awaiting Azure embedding deployment + Supabase service role key. Do NOT write implementation code until credentials are confirmed in `.env`.

The Persistent Semantic Memory and Retrieval Layer is the next major architecture initiative. It adds durable cross-run memory without weakening evidence provenance.

## Five Components

### 1. Vector Store (src/memory/embedder.py + store.py)
- Every completed run is embedded using `text-embedding-3-small` via Azure OpenAI
- Stored in Supabase pgvector (`memory_runs` table)
- New incidents retrieve the 3 most similar past runs before orchestrator runs

### 2. Knowledge Graph (src/memory/extractor.py + store.py)
- Entities (assets, MITRE techniques, CVEs, graph nodes) extracted from evidence records and causal graphs
- Persisted as nodes and edges across runs in `memory_entities` + `memory_entity_edges` tables

### 3. Temporal Indexing
Cosine similarity is decay-weighted:
```python
score = cosine_similarity * exp(-0.023 * age_in_days)
# 30-day half-life decay
```

### 4. MCP Server (src/memory/mcp_server.py)
FastMCP instance mounted at `/mcp` on the FastAPI app.
Four tools:
- `search_similar_incidents` — vector similarity search over past runs
- `get_entity_relationships` — graph traversal for entity connections
- `get_asset_timeline` — temporal index query for an asset's history
- `write_run_to_memory` — persist a completed run into the memory layer

### 5. Agent Integration (src/memory/nodes.py)
Two new LangGraph nodes:
- `memory_retrieve_node` — before orchestrator: retrieves 3 most similar past runs, injects context into orchestrator prompt
- `memory_write_node` — after DoWhy: embeds run and writes to Supabase

**Critical rule:** Memory retrieval results go into the orchestrator **prompt only** — never as `EvidenceRecord` objects.

## Planned Graph Topology (Post-Implementation)

```
START → memory_retrieve → orchestrator → [parallel parents]
      → gather_children → [parallel children] → evaluate_memos
      → causal_synthesis → dowhy_engine
      → (retry → causal_synthesis | end → memory_write) → END
```

## Supabase Schema

**Project:** `lejmpbxchamaqjfclfyz`

**Tables:**
- `memory_runs` — run embeddings + metadata (pgvector column)
- `memory_entities` — extracted entities (assets, techniques, CVEs, graph nodes)
- `memory_entity_edges` — entity relationships across runs

**RPC functions:**
- `search_similar_runs(query_embedding, match_count, decay_lambda)`
- `get_entity_neighborhood(p_entity_value, p_entity_type)`

## New Packages Required

```
supabase==2.15.2
openai==1.91.0
fastmcp==3.2.4
httpx==0.28.1
```

## Key Implementation Rules

1. `embed_text()` must never be called directly in async context — wrap with `await asyncio.to_thread(embed_text, text)`
2. Use `SUPABASE_SERVICE_ROLE_KEY` (never anon key) for all Python backend writes
3. Memory context → orchestrator prompt only. Never `EvidenceRecord`.
4. Do not modify `dataset_compiler.py` or `estimators.py` as part of this work

## TypeScript Types Regeneration

After schema changes:
```bash
npx supabase gen types typescript \
  --project-id lejmpbxchamaqjfclfyz \
  --schema public \
  > app/src/integrations/supabase/types.ts
```

## Related Notes

- [[Environment Variables]] — Supabase + Azure embedding credentials needed
- [[System Overview]] — Where memory layer fits in the pipeline
- [[Design Philosophy]] — Invariant: memory context never as EvidenceRecord
- [[_Index]] — Back to master index
