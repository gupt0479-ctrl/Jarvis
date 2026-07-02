---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - docker
  - infra
  - api
next: "[[pipeline-coordinator]]"
---

# Infrastructure

## Docker Compose Services

| Service | Port | Image | Role |
|---------|------|-------|------|
| `api` | 8000 | `./Dockerfile` | FastAPI, coordinator runner, SSE |
| `worker` | -- | `./Dockerfile` | Kafka spawn consumer, agent runner |
| `redpanda` | 19092 (external), 9092 (internal) | `redpandadata/redpanda:v23.3.6` | Kafka-compatible event bus |
| `frontend` | 8080 | `./frontend/Dockerfile` | React/TanStack UI |
| `mcp` | 8001 | `./Dockerfile` | Standalone FastMCP memory server |

The api and worker containers share a bind-mounted `./data/` directory for SQLite (`runs.db`).

```yaml
# api and worker in docker-compose.yml
volumes:
  - ./data:/app/data
```

## Container Separation

| Env var | api | worker |
|---------|-----|--------|
| `CAUSALOPS_ENABLE_SPAWN_WORKER` | `"0"` | `"1"` |

`"0"` = api publishes `hivemind.spawn` tasks, does NOT consume them.
`"1"` = worker consumes spawn tasks, runs agent nodes, writes to SQLite.

If you set `CAUSALOPS_ENABLE_SPAWN_WORKER=1` in the api container, both api and worker will try to consume the same spawn topic and agents will run twice.

## SQLite (runs.db)

```python
DEFAULT_DB_PATH = data_dir() / "runs.db"
# PRAGMA journal_mode=DELETE   # NOT WAL -- WAL breaks on Docker bind mounts
# PRAGMA busy_timeout=30000
```

Do not switch to WAL mode. Docker bind-mounted SQLite + WAL = file corruption on concurrent writers. `busy_timeout=30000` gives 30 seconds for lock contention before giving up.

## API Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/health` | Health check |
| `POST` | `/run` | Enqueue investigation run |
| `GET` | `/run/{run_id}` | Get run status + artifact |
| `GET` | `/run/{run_id}/events` | SSE stream of telemetry events |
| `GET` | `/run/{run_id}/reasoning` | Get reasoning report |
| `GET` | `/run/{run_id}/graph` | Get 5D KG for run |
| `GET` | `/runs` | List all runs (paginated) |

`POST /run` accepts:
```json
{
  "task_description": "...",
  "evidence_records": [...],
  "run_id": "...",        // optional, generated if omitted
  "correlation_id": "..."  // optional
}
```

Returns immediately with `{"run_id": "..."}`. Run executes async in background. Poll `GET /run/{run_id}` or subscribe to SSE.

**api.py is NOT modified for the MCP server.** The MCP server runs as a separate container.

## Environment Variables

Full env var reference in `60_Claude/40_Project_Briefs/CausalOps/Infrastructure/Environment Variables.md`. Key vars by category:

**LLM (Required):**
```env
GEMINI_API_KEY=
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_MODEL=gemini-2.5-flash
```

**Kafka:**
```env
KAFKA_BOOTSTRAP=redpanda:9092   # inside compose
# KAFKA_BOOTSTRAP=localhost:19092  # outside compose
```

**CausalOps Runtime:**
```env
CAUSALOPS_ENABLE_SPAWN_WORKER=0
CAUSALOPS_SPAWN_MAX_RETRIES=2
CAUSALOPS_SPAWN_RETRY_BACKOFF_MS=1000
CAUSALOPS_DATA_DIR=
CAUSALOPS_ALLOWED_ORIGINS=http://localhost:8080
```

**Memory Layer:**
```env
SUPABASE_URL=https://glbmdbwqmuttykhicasq.supabase.co
SUPABASE_SERVICE_ROLE_KEY=    # Required for backend writes -- NOT the anon key
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Supabase frontend vars (VITE_ prefix):**
```env
VITE_SUPABASE_URL=https://glbmdbwqmuttykhicasq.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=   # anon/public key -- safe in browser
VITE_SUPABASE_PROJECT_ID=glbmdbwqmuttykhicasq
```

## Files Never Committed

```
.env
settings.local.json
data/*.json
data/*.db
```

## Related Notes

- [[CausalOps — Index]] -- project index
- [[event-bus]] -- Kafka topics and Redpanda config
- [[pipeline-coordinator]] -- two-container architecture details
- [[memory-layer]] -- Supabase connection details
