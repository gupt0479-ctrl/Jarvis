# Docker Setup

HiveMind runs as a 4-service compose stack (5 with the planned mcp service). All Python services share a single `./data/` bind-mount volume for SQLite and run artifacts.

## Services

```yaml
services:
  redpanda:    # Kafka-compatible event bus
  api:         # FastAPI coordinator + SSE (port 8000)
  worker:      # Spawn consumer, no exposed port
  frontend:    # React/TanStack UI (port 8080)
  # mcp:       # Memory MCP server (port 8001) — planned
```

## Service Details

### redpanda
```yaml
image: redpandadata/redpanda:v24.2.4
ports: "19092:19092"             # external (localhost)
internal: redpanda:9092          # used by api + worker containers
healthcheck: rpk cluster health
```

### api
```yaml
command: sh -c "cd src && uvicorn api:app --host 0.0.0.0 --port 8000"
ports: "8000:8000"
env_file: .env
environment:
  KAFKA_BOOTSTRAP: redpanda:9092
  HIVEMIND_ENABLE_SPAWN_WORKER: "0"   # coordinator only
  HIVEMIND_ALLOWED_ORIGINS: http://localhost:8080,http://127.0.0.1:8080
volumes: ./data:/app/data
depends_on: redpanda (healthy)
healthcheck: curl -f http://localhost:8000/health
```

### worker
```yaml
command: sh -c "cd src && python -m worker"
environment:
  KAFKA_BOOTSTRAP: redpanda:9092
  HIVEMIND_ENABLE_SPAWN_WORKER: "1"
  HIVEMIND_SPAWN_MAX_RETRIES: "2"
  HIVEMIND_SPAWN_RETRY_BACKOFF_MS: "1000"
volumes: ./data:/app/data
depends_on: redpanda (healthy) + api (healthy)
restart: unless-stopped
```

### frontend
```yaml
build: ./app
ports: "8080:8080"
depends_on: api (healthy)
```

### mcp (planned addition)
```yaml
mcp:
  build: .
  command: sh -c "cd src && python -m memory.mcp_server"
  ports:
    - "8001:8001"
  env_file: .env
  environment:
    MCP_TRANSPORT: sse
  depends_on:
    api: {condition: service_healthy}
```

## Data Volume

`./data/` mounted into `api` and `worker`:
- `data/runs.db` — SQLite run state (both read/write)
- `data/graph_5d.db` — 5D KG (worker writes via stream; api writes via backfill)
- `data/run-*.json` — run artifact JSON files (api writes)

## SQLite Journal Mode

```sql
PRAGMA journal_mode=DELETE   -- NOT WAL
PRAGMA busy_timeout=30000
PRAGMA synchronous=NORMAL
```

WAL (Write-Ahead Log) mode is excluded because WAL uses shared memory files that are unreliable on Docker bind-mounted volumes. DELETE (rollback journal) mode ensures single-writer safety.

## Access Points

| URL | Service |
|-----|---------|
| `http://localhost:8080` | Frontend UI |
| `http://localhost:8000/docs` | FastAPI interactive docs |
| `http://localhost:8000/health` | Health check |
| `http://localhost:8000/demo/estimate` | Smoke test (no LLM, no credentials) |
| `localhost:19092` | Redpanda external Kafka port |
| `http://localhost:8001` | MCP server (planned) |

## Common Commands

```bash
docker-compose up --build    # full stack
docker-compose down          # teardown
./scripts/smoke_kafka_bus.sh # bus unit tests + health check

# Single-process local dev (no Kafka, no worker):
cd src
uvicorn api:app --reload --host 0.0.0.0 --port 8000

# With in-process worker:
HIVEMIND_ENABLE_SPAWN_WORKER=1 uvicorn api:app --reload
```

## Related Notes

- [[event-bus/01-worker|Spawn Worker]] — what the worker container does
- [[event-bus/00-topics|Kafka Topics]] — Redpanda topic structure
- [[infrastructure/02-env-vars|Environment Variables]] — full env var reference
- [[infrastructure/01-api|API]] — endpoints exposed by the api container
