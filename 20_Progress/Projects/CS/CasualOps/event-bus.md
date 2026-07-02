---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - kafka
  - event-bus
next: "[[infrastructure]]"
---

# Event Bus

Kafka (Redpanda) is the coordination layer between the api container and worker container. Six topics, one producer side (api), one consumer side (worker).

## Topics

| Topic | Producer | Consumer | Schema |
|-------|----------|----------|--------|
| `hivemind.runs` | api (run enqueue) | worker (coordinator start) | `RunEnqueueEvent` |
| `hivemind.spawn` | coordinator (dispatch phases) | worker (parent/child execution) | `SpawnTask` |
| `hivemind.artifacts` | worker (run complete) | api (streaming endpoint) | `RunArtifactEvent` |
| `hivemind.telemetry` | every agent node | api/frontend (SSE progress) | `TelemetryEvent` |
| `hivemind.evidence` | evidence ingestion | coordinator (realtime evidence) | `EvidenceRecord` |
| `hivemind.dlq` | worker (failed tasks) | monitoring | `DLQEvent` |

**Note:** Topic names are code-level identifiers in the CausalOps codebase. They are not branding -- `hivemind.*` stays as-is in the actual topic names.

## EventEnvelope

All events use a common wrapper:
```python
class EventEnvelope(BaseModel):
    event_type: str            # e.g., "EXECUTION_PHASE", "RUN_ENQUEUE", "SPAWN_TASK"
    correlation_id: str        # links events across a single investigation
    run_id: str
    timestamp: str             # ISO 8601
    payload: dict[str, Any]
```

`correlation_id` links all Kafka events for a single run together. This is separate from `run_id` -- a run can have multiple correlation IDs if retried.

## SpawnTask (hivemind.spawn)

The spawn topic is the critical fan-out mechanism. When the coordinator dispatches parent or child agents:

```python
class SpawnTask(BaseModel):
    task_type: str             # "RUN_PARENT" | "RUN_CHILD"
    run_id: str
    correlation_id: str
    agent_config: AgentConfig | ChildConfig
    retry_count: int           # 0 on first dispatch
```

Worker picks up the task, runs the agent node (`parent_agent_node` or `child_agent_node`), writes result to SQLite RunRecord, and increments the barrier counter.

**Retry policy:**
```env
CAUSALOPS_SPAWN_MAX_RETRIES=2
CAUSALOPS_SPAWN_RETRY_BACKOFF_MS=1000
```

Failed tasks after max retries are sent to `hivemind.dlq`.

## Telemetry (hivemind.telemetry)

Every LangGraph node (agents, evaluator, causal synthesis) publishes at start and end:
```python
class TelemetryEvent(BaseModel):
    event_type: Literal["EXECUTION_PHASE"]
    phase: str        # e.g., "orchestrator", "parent_agent", "dowhy_engine"
    status: str       # "started" | "completed" | "failed"
    run_id: str
    correlation_id: str
    agent_id: str | None
    metadata: dict[str, Any] | None
```

Frontend subscribes via `GET /run/{run_id}/events` (SSE). The api container streams `hivemind.telemetry` events to the browser.

## Worker (spawn_worker.py)

The worker container (`CAUSALOPS_ENABLE_SPAWN_WORKER=1`) runs `spawn_worker.py`:
- Consumes `hivemind.spawn` with `group_id: "causalops-spawn-worker"`
- Calls `parent_agent_node` or `child_agent_node` depending on `task_type`
- Writes result to SQLite via RunStore
- On failure: retries up to `CAUSALOPS_SPAWN_MAX_RETRIES`, then DLQ

**Critical:** The api container must NOT consume `hivemind.spawn`. That's what `CAUSALOPS_ENABLE_SPAWN_WORKER=0` enforces in the api service.

## No-Kafka Mode

When Kafka is not available (e.g., local dev without Docker), `kafka_enabled()` returns False and:
- Parent/child dispatch is done in-process via `asyncio.gather`
- `_backfill_5d_graph()` is called after reasoning (replaces the stream consumer)
- SSE telemetry events are lost (no subscribers)

## Kafka Config (Redpanda)

```yaml
# docker-compose.yml
redpanda:
  image: redpandadata/redpanda:v23.3.6
  ports:
    - "19092:19092"   # external (localhost)
  command:
    - redpanda start
    - --kafka-addr PLAINTEXT://0.0.0.0:9092,OUTSIDE://0.0.0.0:19092
    - --advertise-kafka-addr PLAINTEXT://redpanda:9092,OUTSIDE://localhost:19092
```

`KAFKA_BOOTSTRAP=redpanda:9092` in compose services (not 19092 -- that's for external access only).

## Related Notes

- [[CausalOps — Index]] -- project index
- [[pipeline-coordinator]] -- Kafka barriers in execute_run
- [[agents]] -- what gets published when agents complete
- [[infrastructure]] -- Docker compose services and env vars
