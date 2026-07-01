# C12 — Coordinator Barrier Waiting

**Community 12** — 17 nodes, cohesion 0.11

The async barrier polling logic and task enqueue functions that wait for parent/child completion.

## Key Nodes

`wait_for_barrier()`, `_dispatch_children()`, `_dispatch_parents()`, `enqueue_child_tasks()`, `enqueue_parent_tasks()`, `Poll run store until predicate is true or timeout.`

## What This Code Does

`wait_for_barrier(store, run_id, predicate)` polls SQLite every 0.5s until `predicate(record)` returns True. Used to block the coordinator until all parent agents or all child agents complete.

`enqueue_parent_tasks()` / `enqueue_child_tasks()` publish spawn envelopes then return immediately. The actual waiting happens in `wait_for_barrier`.

## Source File

`src/coordinator/runner.py` (barrier logic), `src/coordinator/spawn.py` (enqueue functions)

## Related Notes

- [[pipeline/02-coordinator|Coordinator]] — Kafka barriers and the dispatcher pattern
- [[event-bus/01-worker|Spawn Worker]] — increments the completion counters the barrier watches
