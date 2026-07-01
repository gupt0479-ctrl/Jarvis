# API Reference

`src/api.py` — FastAPI HTTP surface for HiveMind, version `0.2.0`. Base URL: `http://localhost:8000`.

## Health & Meta

```
GET /          → orientation links (docs_url, health_check, endpoints)
GET /health    → {"status": "ok"}
```

## Full Agentic Run

### POST /run (async, 202)
Enqueue the full agentic workflow. Returns immediately.
```json
Request:  { "task_description": "...", "run_id": "...", "evidence_records": [...] }
Response: { "run_id": "run-...", "status": "queued" }
```
Idempotency: if run_id already exists with status "queued" or "running" → 409.

### POST /run/sync (blocking)
Same as `/run` but blocks until complete. For scripts and integration tests.

### GET /run/{run_id}
Return run lifecycle status and artifact when complete.
```json
{ "run_id": "...", "status": "running" | "completed" | "failed", "artifact": {...} }
```
Race condition guard: if status is "completed" but artifact file not yet written → `effective_status: "running"`.

### GET /run/{run_id}/events (SSE)
Stream execution telemetry. Frontend generates a run_id, opens this stream first, then calls `POST /run`.
```
data: {"phase": "ORCHESTRATOR", "message": "...", "status": "running", "ts": 1234567890}
data: {"phase": "COMPLETE", "message": "Causal loop complete", "status": "done"}
```
Stream closes on COMPLETE or ERROR phase.

## Deterministic Estimation (No LLM)

### POST /estimate
Compile caller evidence and return a causal estimate. No LLM tokens spent.
```json
Request:  { "graph": {...}, "evidence_records": [...] }
Response: { "causal_estimate_report": {...}, "causal_dataset_profile": {...}, "provenance": [...] }
```

### GET /demo/estimate
Smoke test using bundled SIEM fixture (Patch_Applied → Lateral_Movement, confounder: Asset_Criticality). Always returns a result or explicit gate refusal.

## Evidence Normalizers

```
POST /normalize/sentinel   → SIEM/Sentinel export rows → evidence_records
POST /normalize/cve        → NVD/CVE feed rows → evidence_records
POST /normalize/incidents  → incident report export → evidence_records
```

Accepts exported records without live tenant credentials.

## 5D Knowledge Graph

```
GET  /run/{run_id}/graph/5d           → nodes + edges from graph_5d.db
POST /run/{run_id}/graph/5d/ingest    → manually ingest nodes/edges
GET  /run/{run_id}/reasoning          → reasoning_report (anomalies + recommendations)
```

## Startup / Lifespan

On startup: starts Kafka producer; if `HIVEMIND_ENABLE_SPAWN_WORKER=1`, starts in-process spawn worker.
On shutdown: stops spawn worker, stops Kafka producer.

## CORS

```python
HIVEMIND_ALLOWED_ORIGINS  # comma-separated; default: localhost:8080
```

## Request Models

```python
class RunRequest(BaseModel):
    task_description: str  # min_length=20
    run_id: str | None
    evidence_records: list[dict] | None

class EstimateRequest(BaseModel):
    graph: dict[str, Any]
    evidence_records: list[dict[str, Any]]

class NormalizeRequest(BaseModel):
    records: list[dict[str, Any]]
    source_name: str | None
```

## Recommended Run Flow (Async)

```bash
# 1. Generate run_id client-side
run_id="run-$(date +%Y%m%d-%H%M%S)-$(head -c4 /dev/urandom | xxd -p)"

# 2. Open SSE stream first
curl -N "http://localhost:8000/run/${run_id}/events"

# 3. In another terminal, POST the run
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d "{\"task_description\": \"Suspicious lateral movement across 3 hosts\", \"run_id\": \"${run_id}\"}"

# 4. Poll for completion
curl "http://localhost:8000/run/${run_id}"
```

## Related Notes

- [[infrastructure/00-docker|Docker Setup]] — how to start the stack
- [[causal-engine/02-evidence|Evidence]] — what the normalizers produce
- [[event-bus/00-topics|Kafka Topics]] — SSE stream backed by hivemind.telemetry
