# Coordinator Execution Model

`src/coordinator/runner.py` is the Phase 2b state machine that replaced `graph.ainvoke()`. It runs each pipeline phase sequentially, persisting state to SQLite between phases via `RunRecord`.

## Why Phase 2b Replaced LangGraph's graph.ainvoke

- LangGraph graph state is ephemeral — a crash loses the entire run
- Kafka-based worker dispatch requires durable state between publish and consume
- The api container cannot run both spawn publisher and spawn consumer (separation of concerns)
- Recovery after container restart requires SQLite persistence per phase

## Execution Sequence

```python
async def execute_run(task_description, evidence_records, run_id, correlation_id):
    record = run_store.create_run(...)          # SQLite row created

    await _run_memory_retrieve(record, store)   # memory_retrieve_node (PLANNED) — before orchestrator
    await _run_orchestrator(record, store)       # grand_orchestrator_node
    await _run_parent_evolution(record, store)   # evolve_parent_configs
    await _dispatch_parents(record, store)       # Kafka publish + barrier wait
    await _gather_children(record, store)        # barrier telemetry log
    await _run_child_evolution(record, store)    # evolve_child_configs
    await _dispatch_children(record, store)      # Kafka publish + barrier wait
    await _run_evaluator(record, store)          # evaluate_memos_node
    await _run_causal_loop(record, store)        # causal_synthesis + dowhy (loop)
    await _run_reasoner(record, store)           # reasoning_node
    if not kafka_enabled():
        _backfill_5d_graph(record)              # build KG from record state
    await _run_policy_learning(record, store)    # policy_learning_node
    await _run_memory_write(record, store)       # memory_write_node (PLANNED) — after policy_learning

    record.status = "completed"
    run_store.save(record)
    return record.to_graph_state()
```

**Memory phase rules (critical):**
- `_run_memory_retrieve` and `_run_memory_write` are **awaited directly** — no `asyncio.to_thread` wrapper (unlike every other phase)
- Both must be wrapped in `try/except` that logs the error and swallows it — memory failures must never crash a run

## asyncio.to_thread Pattern

All blocking node functions run in a thread pool to avoid blocking the async event loop:

```python
update = await asyncio.to_thread(grand_orchestrator_node, state)
record.apply_node_update(update)
store.save(record)
```

This lets the coordinator remain responsive to other requests while agents run.

## Kafka Barriers (Parent and Child Dispatch)

```python
await enqueue_parent_tasks(record)           # publish to hivemind.spawn
refreshed = await wait_for_barrier(
    store, record.run_id,
    lambda run: run.parents_barrier_met(),   # True when all parents complete
)
```

`wait_for_barrier` polls SQLite every 0.5s. Workers consume `hivemind.spawn`, run the agent node, write results back to SQLite, and increment `completed_parent_count`. The barrier lifts when count reaches `expected_parent_count`.

## Causal Loop

```python
while True:
    causal_synthesis_node(state)    # LLM: design DAG
    dowhy_engine_node(state)        # deterministic: compile + estimate
    if refutation_next_step(state) == "end":
        break
```

Breaks when: refuters passed, or ATE was withheld (`method == "withheld:data_quality_gates"`).

## Two-Container Architecture

| Container | `HIVEMIND_ENABLE_SPAWN_WORKER` | Behavior |
|-----------|-------------------------------|----------|
| `api` | `"0"` | Publishes spawn tasks, does NOT consume them |
| `worker` | `"1"` | Consumes spawn tasks, runs agents, writes results to SQLite |

For single-process local dev: set `HIVEMIND_ENABLE_SPAWN_WORKER=1` on the api service — lifespan creates an in-process spawn worker.

## RunRecord ↔ GraphState Bridge

```python
# Convert RunRecord to dict compatible with GraphState TypedDict:
state = record.to_graph_state()

# Apply a node's partial update back to RunRecord:
record.apply_node_update({"parent_configs": [...]})
```

This lets node functions (designed for LangGraph) work with the coordinator unchanged.

## RunRecord Changes for Memory Layer

When the memory layer is implemented, `src/coordinator/store.py` needs four changes to `RunRecord`:

1. Add field: `memory_context: list[dict[str, Any]] | None = None`
2. `to_graph_state()` — include `"memory_context": self.memory_context`
3. `apply_node_update(update)` — handle `memory_context` key in the update dict
4. `_record_to_json()` / `_record_from_json()` — serialize/deserialize the field (it's a plain JSON-serializable list, no `model_dump()` needed)

## SQLite Persistence

```python
DEFAULT_DB_PATH = data_dir() / "runs.db"
# PRAGMA journal_mode=DELETE   (not WAL — WAL shared-memory unreliable on Docker bind mounts)
# PRAGMA busy_timeout=30000
# PRAGMA synchronous=NORMAL
```

Both api and worker containers write to the same `./data/runs.db` via a bind mount. `DELETE` journal mode ensures single-writer safety without shared memory.

## DLQ and Retry

`HIVEMIND_SPAWN_MAX_RETRIES=2` (default). Failed agent tasks retry with `HIVEMIND_SPAWN_RETRY_BACKOFF_MS=1000` delay. After max retries → `hivemind.dlq`.

## Related Notes

- [[pipeline/01-langgraph-topology|LangGraph Topology]] — original graph (deprecated for execution)
- [[event-bus/00-topics|Kafka Topics]] — what gets published and where
- [[event-bus/01-worker|Spawn Worker]] — what the worker container does
- [[pipeline/03-graphstate|GraphState]] — RunRecord.to_graph_state() output shape
