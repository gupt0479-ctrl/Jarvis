---
tags: [causalops, docker, infrastructure, deployment, redpanda]
---

# Docker Setup

## Services

```yaml
services:
  redpanda:   # Kafka-compatible event bus
  api:        # FastAPI coordinator + SSE (port 8000)
  worker:     # Spawn consumer (no port)
  frontend:   # React/TanStack UI (port 8080)
```

## Startup / Access

```bash
docker-compose up --build    # full stack
docker-compose down          # teardown

# Access:
# Frontend:    http://localhost:8080
# API docs:    http://localhost:8000/docs
# Health:      http://localhost:8000/health
# Demo smoke:  curl http://localhost:8000/demo/estimate
```

## Service Details

### redpanda
```yaml
image: redpandadata/redpanda:v24.2.4
ports: "19092:19092"             # external Kafka port
internal: redpanda:9092          # used by api + worker
healthcheck: rpk cluster health  # api and worker depend on this
```

### api
```yaml
command: uvicorn api:app --host 0.0.0.0 --port 8000
env:
  KAFKA_BOOTSTRAP: redpanda:9092
  CAUSALOPS_ENABLE_SPAWN_WORKER: "0"   # coordinator only, no spawn consumer
  CAUSALOPS_ALLOWED_ORIGINS: http://localhost:8080
volumes: ./data:/app/data            # shared SQLite + artifacts
depends_on: redpanda (healthy)
healthcheck: curl -f http://localhost:8000/health
```

### worker
```yaml
command: python -m worker
env:
  KAFKA_BOOTSTRAP: redpanda:9092
  CAUSALOPS_ENABLE_SPAWN_WORKER: "1"   # runs spawn consumer
  CAUSALOPS_SPAWN_MAX_RETRIES: "2"
  CAUSALOPS_SPAWN_RETRY_BACKOFF_MS: "1000"
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

## Data Volume

`./data/` is mounted into both `api` and `worker` containers:
- `data/runs.db` — SQLite run state (both api and worker read/write)
- `data/graph_5d.db` — 5D KG (worker writes via stream consumer; api writes via backfill)
- `data/run-*.json` — Run artifact JSON files (api writes)

SQLite journal mode is set to `DELETE` (not WAL) because WAL shared-memory is unreliable on Docker bind-mounted volumes.

## Single-Process Local Dev (No Compose)

```bash
# Backend only — spawns in-process worker
cd src
CAUSALOPS_ENABLE_SPAWN_WORKER=1 uvicorn api:app --reload --host 0.0.0.0 --port 8000

# Without Kafka (no spawn worker either, no SSE):
cd src
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

## Smoke Test

```bash
chmod +x scripts/smoke_kafka_bus.sh
./scripts/smoke_kafka_bus.sh
# Runs bus unit tests, hits /health, lists Redpanda topics (when compose is up)
```

## Dockerfile (Backend)

```dockerfile
# Root Dockerfile — installs Python deps from requirements.txt
# Source: src/ directory
# Working dir: /app
```

## Frontend Dockerfile

```dockerfile
# app/Dockerfile — builds React app via Vite
```

## Related Notes

- [[Environment Variables]] — All env vars for each service
- [[Kafka Bus Overview]] — Redpanda topics and message flow
- [[API Reference]] — All endpoints to test after startup
