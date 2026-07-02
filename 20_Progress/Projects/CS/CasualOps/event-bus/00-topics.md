# Kafka Topics

CausalOps uses Redpanda (Kafka-compatible) as its event bus. The bus decouples coordinator from spawn workers, enables live SSE telemetry, and provides the event log that feeds the 5D spatiotemporal KG.

## 6 Topics

| Topic | Purpose |
|-------|---------|
| `hivemind.runs` | Run lifecycle: started, completed, failed |
| `hivemind.spawn` | Parent and child task dispatch (coordinator → worker) |
| `hivemind.artifacts` | Agent artifacts: memos, configs, causal payloads, reports |
| `hivemind.telemetry` | Phase-level execution events for SSE streaming |
| `hivemind.evidence` | Evidence record events |
| `hivemind.dlq` | Dead-letter queue: failed spawn tasks after max retries |

## Artifact → Topic Routing

```python
# bus/topics.py: topic_for_artifact()
RUN_STARTED / RUN_COMPLETED / RUN_FAILED → hivemind.runs
AGENT_CONFIG / CHILD_CONFIG / RUN_PARENT / RUN_CHILD → hivemind.spawn
EXECUTION_PHASE → hivemind.telemetry
# Everything else (memos, causal payloads, reports) → hivemind.artifacts
```

## EventEnvelope

All messages use this schema:

```python
class EventEnvelope(BaseModel):
    run_id: str
    correlation_id: str       # equals run_id
    agent_id: str             # e.g. "orchestrator", "child:Network Forensics Analyst"
    tier: Tier                # orchestrator | parent | child | evaluator | causal | ...
    artifact_type: ArtifactType
    payload: dict[str, Any]
    sequence: int = 0
    timestamp: datetime       # UTC, timezone-aware
```

## ArtifactType Enum (bus/events.py)

Full set:
```python
AGENT_CONFIG, CHILD_CONFIG, RUN_PARENT, RUN_CHILD, TASK_COMPLETED
DECISION_MEMO, RANKED_STRATEGIES
CAUSAL_PAYLOAD, CAUSAL_ESTIMATE_REPORT, REASONING_REPORT
AGENT_EVOLUTION_REPORT, POLICY_OPTIMIZATION_REPORT
RUN_STARTED, RUN_COMPLETED, RUN_FAILED
EXECUTION_PHASE
```

## Bus Context

`bus/context.py` binds `run_id` and `correlation_id` for the current thread:
```python
bind_run_context(run_id, correlation_id)   # at run start
get_run_summary()    # returns publish counters: parent_config_count, memo_count, etc.
```

`bus/helpers.py`'s `bind_from_state(state)` extracts run_id/correlation_id from any state dict and calls bind_run_context — used in every agent node.

## No-Kafka Fallback

When `KAFKA_BOOTSTRAP` is unset, all publish calls no-op. The coordinator still runs, but:
- SSE telemetry stream is empty (frontend shows no live updates)
- 5D KG is built via backfill at run end instead of real-time streaming
- DLQ and retry logic are not activated

```python
from bus.producer import kafka_enabled
if kafka_enabled():
    publish_artifact(...)
```

## SSE Telemetry Flow

1. Frontend opens `GET /run/{run_id}/events`
2. `stream_telemetry(run_id, stop_event)` subscribes to `hivemind.telemetry` filtered by `run_id`
3. Each `EXECUTION_PHASE` envelope → SSE JSON event to frontend
4. Stream closes on COMPLETE or ERROR phase

## Related Notes

- [[event-bus/01-worker|Spawn Worker]] — consumes hivemind.spawn
- [[pipeline/02-coordinator|Coordinator]] — publishes to hivemind.spawn and hivemind.telemetry
- [[infrastructure/00-docker|Docker Setup]] — Redpanda configuration
- [[infrastructure/02-env-vars|Environment Variables]] — KAFKA_BOOTSTRAP, DLQ settings
