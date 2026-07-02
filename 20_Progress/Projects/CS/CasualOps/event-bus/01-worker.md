# Spawn Worker

The worker container (`src/worker/`) is a Kafka consumer that runs agent tasks dispatched by the coordinator. It provides horizontal separation: the api container never executes agent LLM calls directly in Phase 2b.

## Two-Container Split

| Container | `KAFKA_BOOTSTRAP` | `CAUSALOPS_ENABLE_SPAWN_WORKER` | Role |
|-----------|------------------|-------------------------------|------|
| `api` | `redpanda:9092` | `"0"` | Publishes spawn tasks, runs coordinator phases, exposes HTTP |
| `worker` | `redpanda:9092` | `"1"` | Consumes spawn tasks, runs parent/child agent nodes |

For single-process local dev: set `CAUSALOPS_ENABLE_SPAWN_WORKER=1` on the api service — the FastAPI lifespan starts an in-process worker as an asyncio background task.

## What the Worker Does

1. Subscribes to `hivemind.spawn`
2. Receives `RUN_PARENT` or `RUN_CHILD` envelopes
3. Loads `RunRecord` from SQLite by `run_id`
4. Calls `parent_agent_node(state)` or `child_agent_node(state)` (wrapped in `asyncio.to_thread`)
5. Writes the node's partial update back to SQLite via `record.apply_node_update(update)`
6. Increments `completed_parent_count` or `completed_child_count` on the record
7. Publishes `TASK_COMPLETED` event to `hivemind.artifacts`
8. The barrier in the coordinator lifts once the count reaches `expected_*_count`

## Retry Backoff

```python
CAUSALOPS_SPAWN_MAX_RETRIES = 2      # default retry count
CAUSALOPS_SPAWN_RETRY_BACKOFF_MS = 1000  # delay between retries
```

After max retries, the task is published to `hivemind.dlq`. The run continues with whatever completions it has — a single failed child doesn't block the barrier if `_fallback_memo()` was used.

## Barrier Pattern

The coordinator calls `wait_for_barrier(store, run_id, predicate)` which polls SQLite every 0.5s:

```python
def parents_barrier_met(self) -> bool:
    return self.completed_parent_count >= self.expected_parent_count
```

Workers write to the shared SQLite `runs.db` (mounted as a Docker bind volume). Both api and worker see the same database file. The barrier lifts when the count matches.

## 5D Graph Stream Consumer (graph_5d_stream.py)

The worker also runs a second consumer subscribed to `hivemind.artifacts`. For each incoming artifact:
- Parses the `ArtifactType`
- Calls the appropriate `ingest_*` function in `graph_5d.py`
- Ingests nodes and edges into `graph_5d.db` in real-time

This means the 5D KG is populated incrementally as agents produce artifacts, not just at run end.

## Docker Configuration

```yaml
worker:
  command: sh -c "cd src && python -m worker"
  environment:
    KAFKA_BOOTSTRAP: redpanda:9092
    CAUSALOPS_ENABLE_SPAWN_WORKER: "1"
    CAUSALOPS_SPAWN_MAX_RETRIES: "2"
    CAUSALOPS_SPAWN_RETRY_BACKOFF_MS: "1000"
  volumes:
    - ./data:/app/data    # shared with api — same runs.db and graph_5d.db
  depends_on:
    redpanda: {condition: service_healthy}
    api: {condition: service_healthy}
  restart: unless-stopped
```

## Related Notes

- [[event-bus/00-topics|Kafka Topics]] — hivemind.spawn and hivemind.artifacts
- [[pipeline/02-coordinator|Coordinator]] — enqueue_parent_tasks + wait_for_barrier
- [[infrastructure/00-docker|Docker Setup]] — compose file structure
