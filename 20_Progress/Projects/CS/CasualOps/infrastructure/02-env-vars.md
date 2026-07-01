# Environment Variables

All env vars for the HiveMind stack. Secrets are marked. Never-commit list at the bottom.

## LLM (Required)

```env
GEMINI_API_KEY=...              # Required. aistudio.google.com/u/1/api-keys
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_MODEL=gemini-2.5-flash   # or gemini-2.5-pro for high-reasoning tasks
```

Used by: `src/llm.py` → all agent nodes (orchestrator, parents, children, evaluator, causal architect).

## Kafka / Redpanda

```env
# Only needed when running api/worker OUTSIDE compose
# Inside compose, services use: KAFKA_BOOTSTRAP=redpanda:9092
KAFKA_BOOTSTRAP=localhost:19092
```

## HiveMind Runtime

```env
HIVEMIND_ENABLE_SPAWN_WORKER=0  # "1" → in-process spawn worker (api container)
HIVEMIND_SPAWN_MAX_RETRIES=2    # retry count before DLQ
HIVEMIND_SPAWN_RETRY_BACKOFF_MS=1000
HIVEMIND_DATA_DIR=              # override data/ directory (default: repo-root/data/)
HIVEMIND_ALLOWED_ORIGINS=http://localhost:8080  # CORS origins (comma-separated)
```

## Causal Pipeline Tuning

```env
HIVEMIND_ANOMALY_THRESHOLD=0.15     # reasoning: p(outcome | treatment_group) deviation threshold
HIVEMIND_REASONING_MAX_TARGETS=10   # max assets listed in recommendations
HIVEMIND_DISCOVERY_ALPHA=0.1        # causal discovery: p-value threshold for independence tests
HIVEMIND_DISCOVERY_MIN_ROWS=30      # skip discovery if fewer rows (all edges marked "compatible")
```

## Supabase (Memory Layer)

```env
# Client-side (VITE_ prefix = safe in browser)
VITE_SUPABASE_URL=https://lejmpbxchamaqjfclfyz.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=...       # anon/public key
VITE_SUPABASE_PROJECT_ID=lejmpbxchamaqjfclfyz

# Server-side (secrets)
SUPABASE_URL=https://lejmpbxchamaqjfclfyz.supabase.co
SUPABASE_PUBLISHABLE_KEY=...            # anon key (auth middleware only)
SUPABASE_SERVICE_ROLE_KEY=...           # REQUIRED for Python backend writes (RLS)
```

> **Critical**: Never use the anon/publishable key in Python backend code. RLS silently blocks writes with the anon key. Always use `SUPABASE_SERVICE_ROLE_KEY` in `store.py`.

## Azure OpenAI (Embeddings Only)

```env
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
# Note: Azure chat deployment (AZURE_OPENAI_DEPLOYMENT) is replaced by Gemini
# These vars are for embedder.py only
```

## Graph DB Override (Tests)

```env
HIVEMIND_GRAPH_DB_PATH=     # override path to graph_5d.db (used in tests)
```

## MCP Server

```env
MCP_TRANSPORT=sse     # transport mode for the MCP memory server
```

## Never Commit

```
.env
data/*.json     (run artifacts)
data/*.db       (SQLite databases — runs.db, graph_5d.db)
```

## Related Notes

- [[infrastructure/00-docker|Docker Setup]] — how vars are passed to each compose service
- [[memory-layer/00-design|Memory Layer Design]] — Supabase and Azure vars context
- [[memory-layer/01-status|Status]] — which vars are needed before integration tests can run
