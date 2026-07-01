---
tags: [causalops, kafka, redpanda, event-bus, messaging]
---

# Kafka Bus Overview

HiveMind uses Redpanda (Kafka-compatible) as its event bus. The bus decouples the coordinator (api container) from the spawn workers, enables live SSE telemetry streaming, and provides the event log that feeds the 5D spatiotemporal KG.

## Topics

| Topic | Purpose |
|-------|---------|
| `hivemind.runs` | Run lifecycle events: started, completed, failed |
| `hivemind.spawn` | Parent and child task dispatch (coordinator → worker) |
| `hivemind.artifacts` | Agent artifacts: memos, configs, causal payloads, reports |
| `hivemind.telemetry` | Phase-level execution events (for SSE streaming) |
| `hivemind.evidence` | Evidence record events |
| `hivemind.dlq` | Dead-letter queue for failed spawn tasks after max retries |

## Artifact → Topic Routing

```python
# bus/topics.py
RUN_STARTED / RUN_COMPLETED / RUN_FAILED → hivemind.runs
AGENT_CONFIG / CHILD_CONFIG / RUN_PARENT / RUN_CHILD → hivemind.spawn
EXECUTION_PHASE → hivemind.telemetry
Everything else (memos, causal payloads, reports) → hivemind.artifacts
```

## Event Envelope

All messages use `EventEnvelope`:
```python
class EventEnvelope(BaseModel):
    run_id: str
    correlation_id: str    # equals run_id
    agent_id: str          # e.g. "orchestrator", "child:Network Forensics Analyst"
    tier: Tier             # orchestrator | parent | child | evaluator | causal | estimator | reasoning | optimizer | control
    artifact_type: ArtifactType
    payload: dict[str, Any]
    sequence: int = 0
    timestamp: datetime    # UTC
```

## No-Kafka Fallback

When `KAFKA_BOOTSTRAP` is unset, the producer module detects this and no-ops all publish calls. The coordinator still runs, but:
- SSE telemetry stream is empty (frontend shows no live updates)
- 5D KG is built via backfill at run end instead of streaming
- DLQ and retry logic are not activated

```python
from bus.producer import kafka_enabled
if kafka_enabled():
    # Kafka path
else:
    # In-memory / backfill path
```

## Redpanda Configuration (docker-compose)

```yaml
image: redpandadata/redpanda:v24.2.4
ports: "19092:19092"    # external (localhost access)
internal: redpanda:9092  # used by api and worker containers
```

## SSE Telemetry Flow

1. Frontend opens `GET /run/{run_id}/events`
2. API's `stream_telemetry(run_id, stop_event)` subscribes to `hivemind.telemetry` filtered by `run_id`
3. Each `EXECUTION_PHASE` envelope is converted to SSE JSON event
4. Stream closes on COMPLETE or ERROR phase

## Related Notes

- [[Event Schema]] — EventEnvelope, ArtifactType, Tier definitions
- [[Coordinator Execution Model]] — How coordinator publishes to bus
- [[Run Store]] — SQLite state that persists independently of bus
- [[graph_5d]] — 5D KG populated from hivemind.artifacts via graph_5d_stream.py
