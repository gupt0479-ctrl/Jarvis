# C13 — Coordinator Execution Phases

**Community 13** — 20 nodes, cohesion 0.16

The async coordinator state machine — `execute_run()` and its phase functions. The god node `execute_run` is the most cross-community bridge after `RunRecord` and `RunStore`.

## Key Nodes

`_backfill_5d_graph()`, `execute_run()`, `_gather_children()`, `_ingest_policy_optimization()`, `_load_kg_snapshot()`, `Coordinator state machine — replaces LangGraph graph.ainvoke in Phase 2a.`

## What This Code Does

`execute_run()` is the coordinator entry point called by `engine.run_hivemind()`. It runs each phase sequentially via `asyncio.to_thread`, persisting state to SQLite between phases via `RunRecord`.

`_backfill_5d_graph()` is the no-Kafka path: after the run completes, reconstructs the 5D KG from final `RunRecord` state.

`_gather_children()` is the barrier telemetry log between parent dispatch and child evolution.

`_load_kg_snapshot()` fetches the current 5D KG snapshot for policy_learning_node input.

## Source File

`src/coordinator/runner.py`

## Related Notes

- [[pipeline/02-coordinator|Coordinator]] — full phase sequence and asyncio.to_thread pattern
- [[communities/C06-runstore-sqlite|C06]] — RunStore used by every phase
- [[communities/C12-coordinator-barriers|C12]] — barrier waiting functions
