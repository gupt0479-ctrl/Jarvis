# C08 — Spawn Command Builders

**Community 8** — 23 nodes, cohesion 0.12

Functions that build and publish spawn work commands to `hivemind.spawn` for Phase 2b workers.

## Key Nodes

`build_child_command()`, `build_parent_command()`, `_child_idempotency_key()`, `_parent_idempotency_key()`, `Publish executable spawn work commands for Phase 2b workers.`, `Build a RUN_PARENT spawn envelope.`, `Build a RUN_CHILD spawn envelope.`

## What This Code Does

`enqueue_parent_tasks()` and `enqueue_child_tasks()` publish `RUN_PARENT` / `RUN_CHILD` envelopes to `hivemind.spawn`. Each envelope carries a complete sub-state dict (persona, objective, policy, run_id) so workers can execute the agent node without reading from SQLite.

Idempotency keys prevent duplicate dispatch if the coordinator restarts mid-phase.

## Source File

`src/coordinator/spawn.py` (or similar spawn dispatcher)

## Related Notes

- [[event-bus/01-worker|Spawn Worker]] — consumes these envelopes
- [[pipeline/02-coordinator|Coordinator]] — `_dispatch_parents` and `_dispatch_children` phases
