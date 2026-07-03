---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, coordinator, runner, async, phases]
aliases: [coordinator/runner.py]
---

# Coordinator Runner

`src/coordinator/runner.py` is the Phase 2b state machine that replaced `graph.ainvoke()`. It executes each pipeline phase sequentially, persisting state to SQLite between phases.

## execute_run() — Top-Level Async Entry Point

Called from `engine.run_CausalOps()`:
```python
final_state = await execute_run(
    task_description=...,
    evidence_records=...,
    run_id=...,
    correlation_id=...,
)
```

Creates or retrieves `RunRecord`, runs all phases in order, returns `record.to_graph_state()` on success.

## Phases (in order)

```
orchestrator        → grand_orchestrator_node (asyncio.to_thread)
parent_evolution    → evolve_parent_configs (asyncio.to_thread)
parents             → enqueue_parent_tasks + wait_for_barrier
children_gather     → telemetry barrier log (sync)
child_evolution     → evolve_child_configs (asyncio.to_thread)
children            → enqueue_child_tasks + wait_for_barrier
evaluator           → evaluate_memos_node (asyncio.to_thread)
causal_synthesis    → causal_synthesis_node (loop start)
estimator           → dowhy_engine_node (loop)
  └── refutation_next_step == "end" → break from loop
reasoning           → reasoning_node (asyncio.to_thread)
[no-Kafka only]     → _backfill_5d_graph (sync thread)
policy_learning     → policy_learning_node (asyncio.to_thread, with kg_snapshot)
[no-Kafka only]     → _ingest_policy_optimization (sync thread)
```

## asyncio.to_thread Pattern

All blocking node calls use `asyncio.to_thread()` to avoid blocking the event loop:
```python
update = await asyncio.to_thread(grand_orchestrator_node, state)
record.apply_node_update(update)
store.save(record)
```

## Kafka Barriers

For parent and child dispatch:
```python
await enqueue_parent_tasks(record)           # publish to hivemind.spawn
refreshed = await wait_for_barrier(
    store, record.run_id,
    lambda run: run.parents_barrier_met(),   # True when all parents complete
)
```

`wait_for_barrier` polls SQLite every 0.5s until the barrier predicate returns True or timeout.

Workers consume `hivemind.spawn`, run the agent node, write results back to SQLite (updating child_configs, memos, etc.), and mark completion. The barrier then lifts.

## Error Handling

If any phase raises an exception:
```python
record.status = "failed"
run_store.save(record)
raise
```

The run is marked failed in SQLite and the exception propagates to `engine.run_CausalOps()`, which publishes a `RUN_FAILED` event.

## RunStore.set_phase()

Before each phase:
```python
store.set_phase(record, "orchestrator")  # updates record.phase and saves
```

This allows monitoring tools to see which phase the run is currently in.

## Related Notes

- [[Coordinator Execution Model]] — Architecture description with full phase list
- [[Run Store]] — SQLite RunRecord and RunStore implementation
- [[Kafka Bus Overview]] — enqueue tasks and barrier waiting
- [[agents]] — Node functions called by coordinator phases
