---
tags: [hivemind, project, active, memory-layer, implementation]
created: 2026-05-30
status: awaiting-credentials
---

# HiveMind — Persistent Semantic Memory and Retrieval Layer

> **Task:** Implement the "Persistent Semantic Memory and Retrieval Layer" from the HiveMind roadmap: a hybrid long-term memory architecture combining vector retrieval, graph traversal, and temporal indexing so agents maintain persistent contextual awareness across runs.

---

## 1. What We Are Building (Plain English)

Right now every `run_hivemind()` call starts from zero. Past runs are saved as JSON files in `data/` but nothing reads them. There is no way for the orchestrator to say "this looks like the FIN7 campaign from three weeks ago." There is no entity memory. There is no timeline.

We are adding:

1. **Vector store** — every completed run gets embedded and stored in Supabase pgvector. When a new incident arrives, the orchestrator retrieves the 3 most similar past runs and uses them as context before decomposing the incident.
2. **Knowledge graph** — entities extracted from evidence records and causal graphs (assets, MITRE techniques, CVEs, graph nodes) are stored as nodes and edges in Supabase, forming a persistent cross-run threat intelligence graph.
3. **Temporal indexing** — every stored fact carries a timestamp and queries apply exponential decay (`e^(-λ * age_in_days)`, λ = 0.023, half-life 30 days) so recent evidence weighs more than old.
4. **MCP memory server** — a FastMCP instance mounted inside the existing FastAPI app at `/mcp`, exposing four tools: `search_similar_incidents`, `get_entity_relationships`, `get_asset_timeline`, `write_run_to_memory`.
5. **Agent integration** — two new LangGraph nodes: `memory_retrieve` (before the orchestrator) and `memory_write` (after DoWhy finishes). The orchestrator prompt is extended to accept past context.

---

## 2. What YOU Need to Do Before Any Code Is Written

These are hard blockers. Nothing can proceed without them.

### 2.1 Create an Azure OpenAI Embedding Deployment

**Where:** Azure Portal → your OpenAI resource → Model deployments → Deploy model

**Steps:**
1. Open [Azure Portal](https://portal.azure.com)
2. Navigate to your Azure OpenAI resource (the same one `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` point to)
3. Click **Model deployments** → **Manage deployments**
4. Click **Create new deployment**
5. Model: `text-embedding-3-small`
6. Deployment name: `text-embedding-3-small` (use this exact name, it goes in `AZURE_OPENAI_EMBEDDING_DEPLOYMENT`)
7. Click Deploy. This takes ~1 minute.

**Why `text-embedding-3-small`:** 1536 dimensions, best cost-to-performance ratio for semantic similarity on short text. Consistent with what the rest of the Azure stack uses.

### 2.2 Get the Supabase Service Role Key

**Where:** [https://supabase.com/dashboard/project/lejmpbxchamaqjfclfyz/settings/api](https://supabase.com/dashboard/project/lejmpbxchamaqjfclfyz/settings/api)

**Steps:**
1. Log in to Supabase dashboard
2. Select project `lejmpbxchamaqjfclfyz`
3. Go to **Project Settings** → **API**
4. Copy the `service_role` key (NOT the `anon` / `public` key — that one has RLS restrictions and can't write)
5. Keep it secret — this key bypasses Row Level Security

**Why not the anon key:** The Python backend needs to write to `memory_runs`, `memory_entities`, and `memory_entity_edges`. The anon key will be blocked by Supabase's default RLS. The service role key bypasses RLS entirely, which is correct for a backend process.

### 2.3 Build Your .env File

Once you have both credentials, create a `.env` file at the repo root (already gitignored via `.dockerignore`):

```dotenv
# Existing (already have these)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-chat-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-08-01-preview

# New — add after getting credentials
SUPABASE_URL=https://lejmpbxchamaqjfclfyz.supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJ...your-service-role-key...
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

---

## 3. Database Schema (Run This in Supabase SQL Editor)

**Location:** Supabase dashboard → SQL Editor → New query

This is a single migration. Run it once. Do not run it twice (uses `CREATE TABLE IF NOT EXISTS` / `CREATE EXTENSION IF NOT EXISTS`).

### Step 1: Enable the pgvector Extension

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### Step 2: Create memory_runs Table

```sql
CREATE TABLE IF NOT EXISTS memory_runs (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id              TEXT NOT NULL UNIQUE,
  task_description    TEXT NOT NULL,
  task_embedding      extensions.vector(1536) NOT NULL,
  memos               JSONB NOT NULL DEFAULT '[]'::jsonb,
  causal_graph        JSONB NOT NULL DEFAULT '{}'::jsonb,
  estimate_report     JSONB NOT NULL DEFAULT '{}'::jsonb,
  agent_tier_metrics  JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

### Step 3: Create HNSW Index on Embedding Column

```sql
CREATE INDEX IF NOT EXISTS memory_runs_embedding_idx
  ON memory_runs
  USING hnsw (task_embedding extensions.vector_cosine_ops);
```

**Why HNSW over IVFFlat:** HNSW has no training phase, performs better on changing datasets, and is the Supabase recommendation for 2025+. IVFFlat needs to be retrained as data grows; HNSW does not.

### Step 4: Create memory_entities Table

```sql
CREATE TABLE IF NOT EXISTS memory_entities (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_type   TEXT NOT NULL,
  entity_value  TEXT NOT NULL,
  first_seen    TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_seen     TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (entity_type, entity_value)
);
```

Valid `entity_type` values: `asset`, `technique`, `cve`, `graph_node`.

### Step 5: Create memory_entity_edges Table

```sql
CREATE TABLE IF NOT EXISTS memory_entity_edges (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_entity_id  UUID NOT NULL REFERENCES memory_entities(id) ON DELETE CASCADE,
  target_entity_id  UUID NOT NULL REFERENCES memory_entities(id) ON DELETE CASCADE,
  relationship      TEXT NOT NULL,
  source_run_id     TEXT NOT NULL REFERENCES memory_runs(run_id) ON DELETE CASCADE,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS memory_entity_edges_source_idx
  ON memory_entity_edges (source_entity_id);

CREATE INDEX IF NOT EXISTS memory_entity_edges_run_idx
  ON memory_entity_edges (source_run_id);
```

### Step 6: Create the Vector Search Function

```sql
CREATE OR REPLACE FUNCTION search_similar_runs(
  query_embedding   extensions.vector(1536),
  match_count       INT DEFAULT 5,
  decay_lambda      FLOAT DEFAULT 0.023
)
RETURNS TABLE (
  run_id            TEXT,
  task_description  TEXT,
  similarity        FLOAT,
  temporal_weight   FLOAT,
  weighted_score    FLOAT,
  created_at        TIMESTAMPTZ,
  causal_graph      JSONB,
  estimate_report   JSONB,
  memos             JSONB
)
LANGUAGE sql STABLE
AS $$
  SELECT
    r.run_id,
    r.task_description,
    1 - (r.task_embedding <=> query_embedding)                       AS similarity,
    EXP(-decay_lambda * EXTRACT(EPOCH FROM (now() - r.created_at)) / 86400.0) AS temporal_weight,
    (1 - (r.task_embedding <=> query_embedding))
      * EXP(-decay_lambda * EXTRACT(EPOCH FROM (now() - r.created_at)) / 86400.0) AS weighted_score,
    r.created_at,
    r.causal_graph,
    r.estimate_report,
    r.memos
  FROM memory_runs r
  ORDER BY weighted_score DESC
  LIMIT match_count;
$$;
```

**Temporal decay explained:** `decay_lambda = 0.023` means a run 30 days old gets 50% weight, 60 days old gets 25%, 90 days old gets ~12.5%. A fresh run from today gets full weight. This prevents the SOC from being anchored to old incidents.

### Step 7: Create the Entity Graph Traversal Function

```sql
CREATE OR REPLACE FUNCTION get_entity_neighborhood(
  p_entity_value  TEXT,
  p_entity_type   TEXT
)
RETURNS TABLE (
  source_type   TEXT,
  source_value  TEXT,
  relationship  TEXT,
  target_type   TEXT,
  target_value  TEXT,
  run_id        TEXT,
  created_at    TIMESTAMPTZ
)
LANGUAGE sql STABLE
AS $$
  SELECT
    s.entity_type   AS source_type,
    s.entity_value  AS source_value,
    e.relationship,
    t.entity_type   AS target_type,
    t.entity_value  AS target_value,
    e.source_run_id AS run_id,
    e.created_at
  FROM memory_entity_edges e
  JOIN memory_entities s ON e.source_entity_id = s.id
  JOIN memory_entities t ON e.target_entity_id = t.id
  WHERE s.entity_value = p_entity_value
    AND s.entity_type  = p_entity_type
  ORDER BY e.created_at DESC;
$$;
```

### Step 8: Regenerate Supabase TypeScript Types

After running the SQL above, regenerate the TypeScript types so the frontend stays in sync:

```bash
npx supabase gen types typescript \
  --project-id lejmpbxchamaqjfclfyz \
  --schema public \
  > app/src/integrations/supabase/types.ts
```

---

## 4. Python Packages to Add to requirements.txt

Add these four lines. Pin exact versions for reproducible Docker builds.

```
supabase==2.15.2
openai==1.91.0
fastmcp==3.2.4
httpx==0.28.1
```

**Why `openai` instead of `langchain-openai`:** The `langchain-openai` package wraps chat completions. For embeddings we need the raw `AzureOpenAI` client — `openai>=1.0` has a clean `client.embeddings.create()` API. This is the documented Azure approach per Microsoft Learn.

**Why `fastmcp==3.2.4`:** Latest stable version. The `@mcp.tool` decorator pattern is unchanged from 2.0, and 3.x adds the ASGI mounting we need.

**Why `httpx`:** FastMCP's HTTP client depends on it. Pinning avoids a transitive version conflict with `httpx` pulled in by FastAPI/starlette.

---

## 5. New Files to Create

All new files live under `src/memory/`. Create the directory and an `__init__.py`.

### 5.1 `src/memory/__init__.py`
Empty. Just marks the directory as a Python package.

### 5.2 `src/memory/embedder.py`

**Responsibility:** One function: embed a text string into a 1536-dimensional float list using Azure OpenAI.

**Public API:**
```python
def embed_text(text: str) -> list[float]:
    """Embed text using Azure OpenAI text-embedding-3-small. Returns 1536-dim vector."""
```

**Implementation notes:**
- Instantiate `openai.AzureOpenAI` with `azure_endpoint`, `api_key`, `api_version` from env.
- Call `client.embeddings.create(model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT, input=text)`.
- Return `response.data[0].embedding`.
- Wrap with 3-attempt exponential backoff: 1s, 2s, 4s. Raise on final failure.
- Truncate input to 8191 tokens max (model limit) — truncate by character count at ~32000 chars as a safe proxy.
- This function is synchronous. Callers use `asyncio.to_thread(embed_text, text)` for async contexts.

### 5.3 `src/memory/extractor.py`

**Responsibility:** Deterministic entity extraction from a completed run artifact. No LLM.

**Public API:**
```python
def extract_entities(run_artifact: dict) -> list[tuple[str, str]]:
    """Return (entity_type, entity_value) pairs from a run artifact."""

def build_edges(
    run_artifact: dict,
    entity_pairs: list[tuple[str, str]],
) -> list[tuple[str, str, str, str, str]]:
    """Return (src_type, src_val, relationship, tgt_type, tgt_val) tuples."""
```

**Implementation notes for `extract_entities`:**
- From `run_artifact["evidence_records"]` (list of EvidenceRecord dicts):
  - `asset_id` if not None → `("asset", asset_id)`
  - `technique_id` if matches regex `T\d{4}(?:\.\d{3})?` → `("technique", technique_id)`
  - `cve_id` if matches regex `CVE-\d{4}-\d+` → `("cve", cve_id)`
- From `run_artifact["causal_graph"]["nodes"]` (list of node dicts):
  - Each `node["id"]` → `("graph_node", node["id"])`
- Deduplicate. Return sorted list for stability.

**Implementation notes for `build_edges`:**
- From `run_artifact["causal_graph"]["edges"]` (list of edge dicts):
  - Each edge has `source` and `target` (graph node IDs) and `relationship`
  - Build `("graph_node", source, relationship, "graph_node", target)`
- Cross-link: for each `technique` entity, check if any `asset` co-appeared in the same evidence record and build `("asset", asset_id, "observed_with", "technique", technique_id)` edges
- Return list of 5-tuples.

### 5.4 `src/memory/store.py`

**Responsibility:** The Supabase read/write interface. Pure Python. No HTTP framework here.

**Public API:**
```python
class SupabaseMemoryStore:
    def __init__(self) -> None: ...

    def write_run(self, run_artifact: dict) -> dict:
        """Embed task_description, insert memory_run, upsert entities and edges.
        Returns {"run_id": str, "entities_indexed": int}."""

    def search_similar_runs(self, task_description: str, k: int = 5) -> list[dict]:
        """Embed query, call search_similar_runs RPC. Returns list of run summaries."""

    def get_entity_relationships(
        self,
        entity_value: str,
        entity_type: str,
    ) -> list[dict]:
        """Call get_entity_neighborhood RPC. Returns list of edge dicts."""

    def get_asset_timeline(
        self,
        asset_id: str,
        since_days: int = 90,
    ) -> list[dict]:
        """Query edges for asset entities ordered chronologically."""
```

**Implementation notes:**

`__init__`: Create `supabase.create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)`. Store as `self._client`.

`write_run`:
1. Embed `run_artifact["task_description"]` via `embedder.embed_text()`
2. Upsert to `memory_runs` via `self._client.table("memory_runs").upsert({...}, on_conflict="run_id").execute()`
3. Call `extract_entities(run_artifact)` → list of `(type, value)` pairs
4. For each entity: upsert to `memory_entities` with `on_conflict="entity_type,entity_value"`, also update `last_seen = now()` — use Supabase's `upsert` with `ignoreDuplicates=False`
5. Query back to get UUIDs for each upserted entity (needed for edge inserts)
6. Call `build_edges(run_artifact, entities)`
7. Insert edges to `memory_entity_edges` (do not upsert — duplicate edges are fine for timeline)
8. Return `{"run_id": run_id, "entities_indexed": len(entities)}`

`search_similar_runs`:
1. Embed `task_description`
2. Call `self._client.rpc("search_similar_runs", {"query_embedding": embedding, "match_count": k}).execute()`
3. Return `response.data` (list of dicts with run_id, task_description, similarity, temporal_weight, weighted_score, created_at, causal_graph, estimate_report)

`get_entity_relationships`:
1. Call `self._client.rpc("get_entity_neighborhood", {"p_entity_value": entity_value, "p_entity_type": entity_type}).execute()`
2. Return `response.data`

`get_asset_timeline`:
1. Compute cutoff = `now() - timedelta(days=since_days)` as ISO string
2. Query: `self._client.table("memory_entity_edges").select("*, source_entity:source_entity_id(*), target_entity:target_entity_id(*)").gte("created_at", cutoff).order("created_at").execute()`
3. Filter results where either entity has `entity_type="asset"` and `entity_value=asset_id`
4. Return sorted list of edge dicts

**Error handling:** Wrap all Supabase calls in try/except. Log errors. Return empty list / raise depending on whether it is a read (return empty) or write (raise so caller knows).

### 5.5 `src/memory/nodes.py`

**Responsibility:** The two new LangGraph nodes.

**Public API:**
```python
async def memory_retrieve_node(state: GraphState) -> dict:
    """Retrieve similar past runs before orchestrator. Returns {"memory_context": list[dict]}."""

async def memory_write_node(state: GraphState) -> dict:
    """Persist completed run to memory after estimation. Returns {}."""
```

**Implementation notes:**

`memory_retrieve_node`:
1. Check `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` env vars exist. If either is missing, log warning and return `{"memory_context": []}` (graceful degradation — memory is additive, not required for the pipeline to function).
2. Instantiate `SupabaseMemoryStore()`
3. Call `await asyncio.to_thread(store.search_similar_runs, state["task_description"], 3)`
4. Format: for each result, keep only `run_id`, `task_description`, `similarity`, `weighted_score`, `created_at`, and a summary of `estimate_report` (just `ate`, `method`, `n_rows`). Drop full `memos` (too large for prompt context).
5. Return `{"memory_context": formatted_results}`

`memory_write_node`:
1. If missing credentials, log and return `{}` gracefully.
2. Assemble `run_artifact` from state fields: `run_id`, `task_description`, `memos` (serialized), `causal_payload.graph`, `causal_estimate_report`, `evidence_records`, `agent_tier_metrics`
3. Serialize Pydantic objects using the same `serialize_pydantic` helper already in `engine.py`
4. Call `await asyncio.to_thread(store.write_run, run_artifact)`
5. Log result: entities indexed, run ID
6. Return `{}`

### 5.6 `src/memory/mcp_server.py`

**Responsibility:** FastMCP instance exposing 4 tools. Mounted into the FastAPI app at `/mcp`.

**Implementation:**
```python
from fastmcp import FastMCP
from memory.store import SupabaseMemoryStore

mcp = FastMCP("hivemind-memory")

@mcp.tool
def search_similar_incidents(description: str, k: int = 5) -> list[dict]:
    """Search for past HiveMind runs similar to the given incident description.
    Returns ranked results with similarity score, temporal weight, causal graph summary."""
    store = SupabaseMemoryStore()
    return store.search_similar_runs(description, k=k)

@mcp.tool
def get_entity_relationships(entity_value: str, entity_type: str) -> list[dict]:
    """Get all known relationships for an entity (asset, technique, cve, graph_node).
    Returns edges with source, relationship type, target, and source run ID."""
    store = SupabaseMemoryStore()
    return store.get_entity_relationships(entity_value, entity_type)

@mcp.tool
def get_asset_timeline(asset_id: str, since_days: int = 90) -> list[dict]:
    """Get chronological event timeline for an asset over the past N days.
    Returns edges ordered by observed_at."""
    store = SupabaseMemoryStore()
    return store.get_asset_timeline(asset_id, since_days=since_days)

@mcp.tool
def write_run_to_memory(run_artifact: dict) -> dict:
    """Store a completed HiveMind run in the memory layer.
    Embeds task description, indexes entities, and builds knowledge graph edges.
    Returns {"run_id": str, "entities_indexed": int}."""
    store = SupabaseMemoryStore()
    return store.write_run(run_artifact)
```

---

## 6. Existing Files to Modify

### 6.1 `src/schema.py`

Add two fields to `GraphState`:

```python
class GraphState(TypedDict):
    # ... existing fields unchanged ...

    # NEW: set before graph.ainvoke() in engine.py
    run_id: str

    # NEW: populated by memory_retrieve_node, consumed by grand_orchestrator_node
    memory_context: list[dict[str, Any]] | None
```

### 6.2 `src/graph.py`

Changes:
1. Import `memory_retrieve_node` and `memory_write_node` from `memory.nodes`
2. Add both nodes to the builder
3. Change `START → orchestrator` to `START → memory_retrieve → orchestrator`
4. Change `"end": END` in `conditional_refutation_check` routing to `"end": "memory_write"`
5. Add `memory_write → END`

Full graph topology after change:
```
START → memory_retrieve → orchestrator → [parallel parent_agents] → gather_children
      → [parallel child_agents] → evaluate_memos → causal_synthesis
      → dowhy_engine → (retry: causal_synthesis | end: memory_write) → END
```

### 6.3 `src/agents.py`

Changes to `grand_orchestrator_prompt` and `grand_orchestrator_node`:

The prompt gets a new optional section. When `memory_context` is non-empty, prepend this block to the user message:

```
RELEVANT PAST INCIDENTS (ranked by recency-weighted similarity):
{formatted_memory}

---
```

Where `formatted_memory` is a formatted list like:
```
1. [run_id: run-20260510-143022] similarity=0.87, weight=0.94
   "Suspected FIN7 lateral movement via RDP in finance segment"
   ATE={ate}, method={method}, n_rows={n_rows}

2. [run_id: run-20260418-091500] similarity=0.72, weight=0.61
   "Privilege escalation via CVE-2025-XXXX on domain controller"
   ATE=null (withheld: data_quality_gates)
```

In `grand_orchestrator_node`: check `state.get("memory_context")`, format if non-empty, inject into invoke call. The orchestrator prompt chain will need a second input variable (`memory_context_text`). When empty, pass an empty string.

### 6.4 `src/engine.py`

Change `initial_state` to include `run_id` and `memory_context`:

```python
run_id = f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
initial_state = {
    "run_id": run_id,
    "memory_context": None,
    # ... all existing fields unchanged ...
}
```

Move `run_id` generation to the top of `run_hivemind()` (before the `graph` call). The rest of `engine.py` is unchanged.

### 6.5 `src/api.py`

Three changes:
1. Import `mcp` and `mcp_app` from `memory.mcp_server`
2. Change the `app = FastAPI(...)` constructor to pass `lifespan=mcp_app.lifespan` (required by FastMCP for session manager initialization)
3. Add `app.mount("/mcp", mcp_app)` after middleware setup

Specific code change for lifespan (since the existing app has no lifespan):
```python
mcp_app = mcp.http_app(path="/")
app = FastAPI(
    title="HiveMind API",
    version="0.2.0",
    description="...",
    lifespan=mcp_app.lifespan,   # <- new
)
app.add_middleware(CORSMiddleware, ...)
app.mount("/mcp", mcp_app)
```

**Note on CORS:** FastMCP's docs warn against top-level `CORSMiddleware` with OAuth-protected MCP servers. We are NOT using OAuth on the MCP server (it is internal), so this is safe.

### 6.6 `docker-compose.yml`

Add three env vars to the `api` service under `environment`:
```yaml
SUPABASE_URL: ${SUPABASE_URL}
SUPABASE_SERVICE_ROLE_KEY: ${SUPABASE_SERVICE_ROLE_KEY}
AZURE_OPENAI_EMBEDDING_DEPLOYMENT: ${AZURE_OPENAI_EMBEDDING_DEPLOYMENT}
```

### 6.7 `app/src/integrations/supabase/types.ts`

After running the SQL migration, regenerate this file via the Supabase CLI. Do not hand-edit.

---

## 7. New `.env.example` File (Create at Repo Root)

```dotenv
# HiveMind environment variables — copy to .env and fill in values
# Never commit .env to git

# Azure OpenAI (chat)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-08-01-preview

# Azure OpenAI (embeddings)
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

# Supabase (backend only — never expose service_role key to frontend)
SUPABASE_URL=https://lejmpbxchamaqjfclfyz.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# CORS
HIVEMIND_ALLOWED_ORIGINS=http://localhost:8080,http://127.0.0.1:8080
```

---

## 8. Implementation Sequence

Execute in this order. Each step is independently testable before moving forward.

| Step | Action | Test |
|------|--------|------|
| 1 | Create Azure embedding deployment | `curl POST /embeddings` directly in Azure Portal playground |
| 2 | Get Supabase service role key | Log in and copy |
| 3 | Build `.env` file | `python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('SUPABASE_SERVICE_ROLE_KEY'))"` |
| 4 | Run SQL migration in Supabase SQL Editor | Check Tables tab — 3 tables, 2 functions appear |
| 5 | Add packages to `requirements.txt` | `pip install -r requirements.txt` |
| 6 | Create `src/memory/__init__.py` | `python -c "from memory import embedder"` |
| 7 | Create `src/memory/embedder.py` | `python -c "from memory.embedder import embed_text; v = embed_text('test'); print(len(v))"` — expect 1536 |
| 8 | Create `src/memory/extractor.py` | Unit test with a fixture run artifact |
| 9 | Create `src/memory/store.py` | `store.write_run(demo_artifact)` — check Supabase dashboard for row |
| 10 | Create `src/memory/nodes.py` | Standalone async test |
| 11 | Modify `src/schema.py` | `python -c "from schema import GraphState"` — no import error |
| 12 | Modify `src/engine.py` | `run_id` added to initial_state |
| 13 | Modify `src/graph.py` | Build graph — no errors |
| 14 | Modify `src/agents.py` | Grand orchestrator accepts memory_context |
| 15 | Create `src/memory/mcp_server.py` | Import without error |
| 16 | Modify `src/api.py` | `uvicorn api:app --reload` — check `/mcp` responds |
| 17 | Full integration test | POST `/run` with demo evidence, check Supabase for memory row, POST `/run` again and verify memory_context appears in orchestrator |
| 18 | Regenerate Supabase TypeScript types | `npx supabase gen types...` |
| 19 | Docker build | `docker-compose up --build` |

---

## 9. Architecture Decision Log

### Why not LangChain's built-in memory?
LangChain's memory stores (e.g. `ConversationBufferMemory`) are in-session only and don't persist across process restarts. LangGraph's built-in `Store` API is cross-thread but in-memory by default and requires a custom persistence backend. Building directly on Supabase + pgvector gives us: the same infra already connected to the frontend, proper vector search with the `<=>` operator, a real Postgres knowledge graph with FK constraints, and no additional managed services.

### Why Supabase over Pinecone/Weaviate?
The Supabase project ID `lejmpbxchamaqjfclfyz` is already in the repo. The frontend is already wired to it. Adding pgvector to an existing Postgres database is a one-line extension enable. Pinecone/Weaviate would add a new managed service, new credentials, and new operational overhead with no benefit at our scale.

### Why HNSW over IVFFlat?
IVFFlat requires a training phase on existing data and degrades in recall as the dataset grows past the training distribution. HNSW builds a navigable graph at insert time, has no training phase, and performs comparably or better at small-to-medium scale. For a SOC memory store that grows incrementally with each run, HNSW is the correct choice.

### Why exponential temporal decay?
Cyber adversaries change TTPs. A FIN7 campaign from 6 months ago may use completely different infrastructure today. Using raw cosine similarity without decay would anchor the orchestrator to old incidents even when their operational details are outdated. The 30-day half-life is a tunable parameter (`decay_lambda` in the SQL function) — adjust it based on observed adversary dwell time in your environment.

### Why mount MCP in FastAPI rather than standalone?
The user chose "Embedded in FastAPI." This keeps the deployment to a single Docker service. The MCP server is available at `http://localhost:8000/mcp` via HTTP/SSE. Any MCP-compatible client (including Claude Code) can connect to it. The tradeoff is that it shares the same process as the API; a high-traffic MCP query could add latency to `/run` calls. At the expected usage volume for a SOC tool, this is acceptable.

### Why `source_type: "memory"` not needed?
Memory retrieval results are injected into the orchestrator prompt as text context, not as `EvidenceRecord` objects. This keeps the memory layer cleanly separate from the evidence pipeline. Evidence records are factual observations; memory context is inference guidance. Mixing them would corrupt the evidence gates.

---

## 10. What to Never Do

These are hard project rules derived directly from the codebase design:

1. **Never pass memory retrieval results as `EvidenceRecord` objects into `evidence_records`.** Memory context goes into the orchestrator prompt only. The evidence pipeline is guarded by the empirical-data gate.
2. **Never let the LLM generate embedding text.** Embeddings are always computed from the literal `task_description` string. No LLM paraphrase.
3. **Never commit `.env` or `settings.local.json`.** The `.dockerignore` excludes `.env`; verify `.gitignore` also excludes it.
4. **Never use the Supabase anon key in the Python backend.** It will fail silently on writes due to RLS.
5. **Never modify `dataset_compiler.py` or `estimators.py` as part of this work.** The evidence pipeline is completely independent of memory.
6. **Never call `embed_text()` inside a synchronous context without `asyncio.to_thread`.** It makes a network call and will block the event loop.

---

## 11. Open Questions (Not Blocking)

- **Memory context prompt formatting:** Exact wording of the "RELEVANT PAST INCIDENTS" block will need iteration based on observed orchestrator behavior.
- **Entity co-occurrence edges:** Whether to extract cross-record edges (asset + technique co-occurrence) adds complexity. Start without them, add in a follow-up.
- **Row Level Security on memory tables:** Currently bypassed via service role key. Add RLS policies when multi-tenancy is needed.
- **Memory pruning:** No deletion strategy yet. Old runs accumulate. Future: add a `memory_runs_retention_days` config and a scheduled Supabase Edge Function to prune.
- **Supabase TypeScript regeneration in CI:** Add to the GitHub Actions workflow once the schema is stable.

---

*Note created: 2026-05-30. Status: awaiting Azure embedding deployment + Supabase service role key before implementation begins.*
