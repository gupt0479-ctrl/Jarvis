---
tags: [causalops, coordinator, phase2, async, architecture]
---

# Coordinator Execution Model

## Why Phase 2b Replaced LangGraph's `graph.ainvoke`

The original LangGraph graph ran everything in a single async call. Phase 2b replaced this with a coordinator state machine because:
- LangGraph graph state is ephemeral — a crash loses everything
- Kafka-based worker dispatch requires durable state between publish and consume
- The api container cannot run both the spawn publisher and spawn consumer (separation of concerns)
- Recovery after container restart requires SQLite persistence per phase

## Execution Sequence (coordinator/runner.py)

```python
async def execute_run(task_description, evidence_records, run_id, correlation_id):
    record = run_store.create_run(...)          # SQLite row created
    
    await _run_orchestrator(record, store)       # Phase: orchestrator
    await _run_parent_evolution(record, store)   # Phase: parent_evolution
    await _dispatch_parents(record, store)       # Phase: parents (Kafka + barrier)
    await _gather_children(record, store)        # Phase: children_gather (barrier telemetry)
    await _run_child_evolution(record, store)    # Phase: child_evolution
    await _dispatch_children(record, store)      # Phase: children (Kafka + barrier)
    await _run_evaluator(record, store)          # Phase: evaluator
    await _run_causal_loop(record, store)        # Phase: causal_synthesis + estimator (loop)
    await _run_reasoner(record, store)           # Phase: reasoning
    
    if not kafka_enabled():
        _backfill_5d_graph(record)              # Build KG from record state (no-Kafka path)
    
    await _run_policy_learning(record, store)    # Phase: policy_learning
    
    if not kafka_enabled():
        _ingest_policy_optimization(record)     # Push RL report into KG
    
    record.status = "completed"
    run_store.save(record)
    return record.to_graph_state()
```

## Phase Details

### Orchestrator Phase
- Calls `grand_orchestrator_node(state)` synchronously via `asyncio.to_thread`
- Writes `parent_configs` to `RunRecord` via `record.apply_node_update(update)`
- Saves to SQLite

### Parent Evolution Phase
- Calls `evolve_parent_configs(state, configs)` — deterministic island EA
- Attaches `AgentPolicy` to each `AgentConfig`
- Publishes evolution report to Kafka (`hivemind.artifacts`)

### Parent Dispatch Phase (Kafka barrier)
- Calls `enqueue_parent_tasks(record)` → publishes one `RUN_PARENT` spawn event per parent config to `hivemind.spawn`
- Calls `wait_for_barrier(store, run_id, lambda run: run.parents_barrier_met())`
- Barrier polls SQLite every 0.5s until all parent completions are recorded
- Worker consumes `hivemind.spawn`, runs `parent_agent_node`, writes results back to SQLite

### Child Evolution Phase
Same pattern as parent evolution but over `child_configs`.

### Child Dispatch Phase (Kafka barrier)
Same pattern as parent dispatch but over `child_configs`. Barrier waits for all child memos.

### Causal Loop
```python
while True:
    causal_synthesis_node(state)    # LLM: design DAG
    dowhy_engine_node(state)        # deterministic: estimate
    if refutation_next_step(state) == "end":
        break
```
Retries when refuters fail. Stops when they pass or ATE is withheld.

### 5D Graph (Kafka vs no-Kafka)
- **With Kafka:** worker's `graph_5d_stream.py` consumer ingests artifact events in real-time as they arrive on `hivemind.artifacts`. No batch rebuild needed.
- **Without Kafka:** coordinator calls `_backfill_5d_graph(record)` at the end to reconstruct the KG from final `RunRecord` state.

## RunRecord ↔ GraphState Bridge

```python
# Convert RunRecord to dict compatible with GraphState TypedDict
state = record.to_graph_state()

# Apply a node's partial update back to RunRecord
record.apply_node_update(update)  # e.g. {"parent_configs": [...]}
```

This bridge lets the same node functions (originally designed for LangGraph) work with the coordinator without modification.

## Two-Container Architecture

| Container | Env | Behavior |
|-----------|-----|----------|
| `api` | `HIVEMIND_ENABLE_SPAWN_WORKER=0` | Publishes spawn tasks, does NOT consume them |
| `worker` | `HIVEMIND_ENABLE_SPAWN_WORKER=1` | Consumes spawn tasks, runs agents |

For single-process local dev: set `HIVEMIND_ENABLE_SPAWN_WORKER=1` on the api service — the lifespan creates an in-process spawn worker task.

## DLQ and Retry

`HIVEMIND_SPAWN_MAX_RETRIES=2` (default). Failed agent tasks are retried with `HIVEMIND_SPAWN_RETRY_BACKOFF_MS=1000` delay. After max retries, the task goes to `hivemind.dlq`.

## Related Notes

- [[LangGraph Pipeline]] — Original graph topology (deprecated for execution)
- [[Run Store]] — SQLite-backed RunRecord and RunStore
- [[Kafka Bus Overview]] — Topics and event flow
- [[GraphState Contract]] — The state shared across all phases
