---
tags: [causalops, api, fastapi, endpoints, http]
aliases: [api.py]
---

# api.py — FastAPI HTTP Interface

`src/api.py` is the HTTP surface for HiveMind. Version: `0.2.0`. It exposes two execution paths (agentic and deterministic), an SSE telemetry stream, normalizer endpoints, and a 5D graph ingestion endpoint.

## Startup / Lifespan

On startup: starts Kafka producer, optionally starts in-process spawn worker.
On shutdown: stops spawn worker task, stops Kafka producer.

```python
HIVEMIND_ENABLE_SPAWN_WORKER  # "1" → in-process worker; "0" → expect separate worker container
```

## CORS

```python
HIVEMIND_ALLOWED_ORIGINS  # comma-separated origins; default: localhost:8080
```

## Endpoints

### GET /
Returns orientation links (docs_url, health_check, endpoints).

### GET /health
Returns `{"status": "ok"}`. Used by Docker healthcheck.

### POST /run (async, 202)
**Enqueue the full agentic workflow.** Returns immediately with run_id.
```json
Request:  { "task_description": "...", "run_id": "...", "evidence_records": [...] }
Response: { "run_id": "run-...", "status": "queued" }
```
Runs `run_hivemind()` as a background task. Client should poll `GET /run/{run_id}` or stream `GET /run/{run_id}/events`.

**Idempotency:** If the run_id already exists with status "queued" or "running", returns 409.

### POST /run/sync (blocking)
Same as `/run` but blocks until complete. Used by scripts and integration tests.

### GET /run/{run_id}
Return run lifecycle status and artifact when complete.
```json
{ "run_id": "...", "status": "running" | "completed" | "failed", "artifact": {...} }
```
Note: if status is "completed" but artifact file not yet written, returns `effective_status: "running"` to avoid race condition.

### GET /run/{run_id}/events (SSE)
Stream execution telemetry as Server-Sent Events.
```
data: {"id": "...", "phase": "ORCHESTRATOR", "message": "...", "status": "running", "ts": 1234567890}
data: {"id": "...", "phase": "COMPLETE", "message": "Causal loop complete", "status": "done"}
```
The frontend generates a `run_id`, opens this SSE stream, then calls `POST /run` with the same id. The stream closes on COMPLETE or ERROR phase.

### GET /run/{run_id}/graph/5d
Retrieve the 5D Spatiotemporal Knowledge Graph for a run.
Returns nodes and edges from the graph_5d.db SQLite database.

### POST /run/{run_id}/graph/5d/ingest
Manually ingest node/edge tuples into the 5D graph.
```json
{
  "nodes": [{"id": "...", "node_type": "agent|asset|threat|artifact|causal_variable", "label": "...", "description": "..."}],
  "edges": [{"subject": "...", "predicate": "...", "object": "...", "observed_at": "...", "confidence": 1.0}]
}
```

### GET /run/{run_id}/reasoning
Return the reasoning layer's anomalies and recommendations.

### POST /estimate (deterministic, fast)
Compile caller evidence and return a causal estimate report. No LLM tokens spent.
```json
Request:  { "graph": {...}, "evidence_records": [...] }
Response: { "causal_estimate_report": {...}, "causal_dataset_profile": {...}, "provenance": [...] }
```

### GET /demo/estimate
Deterministic smoke test with bundled SIEM fixture:
- treatment: `Patch_Applied`, outcome: `Lateral_Movement`, confounder: `Asset_Criticality`
- Always returns a result (or explicit gate refusal if fixture is broken)

### POST /normalize/sentinel
Normalize Microsoft Sentinel or SIEM-like export rows → `{"evidence_records": [...]}`

### POST /normalize/cve
Normalize NVD/CVE feed rows → `{"evidence_records": [...]}`

### POST /normalize/incidents
Normalize incident report export rows → `{"evidence_records": [...]}`

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

## Related Notes

- [[engine]] — run_hivemind() called by /run and /run/sync
- [[estimators]] — estimate_causal_effect() called by /estimate
- [[dataset_compiler]] — compile_evidence_dataset() called by /estimate
- [[evidence_adapters]] — normalize_* functions called by /normalize/*
- [[demo_fixtures]] — patch_lateral_movement_* called by /demo/estimate
- [[Kafka Bus Overview]] — SSE streams from Kafka consumer
- [[graph_5d]] — 5D KG endpoints read/write to graph_5d.db
