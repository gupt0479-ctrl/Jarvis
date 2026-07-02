---
tags: [causalops, environment, config, secrets, env]
---

# Environment Variables

## LLM Configuration (Required)

```env
GEMINI_API_KEY="..."          # Required. Get from https://aistudio.google.com/u/1/api-keys
GEMINI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL="gemini-2.5-flash"   # or "gemini-2.5-pro" for high-reasoning
```

## Kafka / Redpanda

```env
# Only needed when running api/worker OUTSIDE compose
# In compose, services use: KAFKA_BOOTSTRAP=redpanda:9092
KAFKA_BOOTSTRAP=localhost:19092
```

## CausalOps Runtime

```env
CAUSALOPS_ENABLE_SPAWN_WORKER=0   # "1" to run in-process spawn consumer (api container)
                                  # "0" to expect separate worker container (compose default)
CAUSALOPS_SPAWN_MAX_RETRIES=2     # Spawn task retry count before DLQ
CAUSALOPS_SPAWN_RETRY_BACKOFF_MS=1000  # Delay between spawn retries (ms)
CAUSALOPS_DATA_DIR=               # Override data/ directory (default: repo-root/data/)
CAUSALOPS_ALLOWED_ORIGINS=http://localhost:8080  # CORS origins (comma-separated)
```

## Reasoning Layer Tuning

```env
CAUSALOPS_ANOMALY_THRESHOLD=0.15     # p(outcome | treatment_group) deviation threshold
CAUSALOPS_REASONING_MAX_TARGETS=10   # max assets listed in recommendations
```

## Causal Discovery Tuning

```env
CAUSALOPS_DISCOVERY_ALPHA=0.1        # p-value threshold for independence tests
CAUSALOPS_DISCOVERY_MIN_ROWS=30      # min rows required to run discovery (else all "compatible")
```

## Graph DB Override (Testing)

```env
CAUSALOPS_GRAPH_DB_PATH=             # Override path to graph_5d.db (used in tests)
```

## Supabase (Memory Layer -- Active)

```env
# Client (VITE_ prefix = safe in browser)
VITE_SUPABASE_URL=https://glbmdbwqmuttykhicasq.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=      # anon/public key
VITE_SUPABASE_PROJECT_ID=glbmdbwqmuttykhicasq

# Server (secrets -- never put anon key here)
SUPABASE_URL=https://glbmdbwqmuttykhicasq.supabase.co
SUPABASE_PUBLISHABLE_KEY=           # same anon key (auth middleware)
SUPABASE_SERVICE_ROLE_KEY=          # service_role key -- REQUIRED for backend writes (RLS)
```

> **Critical:** Never use the Supabase anon key in the Python backend. RLS silently blocks writes. Always use `SUPABASE_SERVICE_ROLE_KEY`.

## Azure OpenAI (Embeddings Only -- NOT Chat LLM)

The chat LLM is Gemini. Azure OpenAI is used only for the memory layer embeddings.

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

## Never Commit

```
.env
settings.local.json
data/*.json   (run artifacts)
data/*.db     (SQLite databases)
```

## Related Notes

- [[Docker Setup]] -- How env vars are passed to each compose service
- [[Memory Layer]] -- Supabase and Azure embedding vars
