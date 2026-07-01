# C25 — Coordinator State Machine + RunStore

**Community 25** — 7 nodes, cohesion 0.18

High-level coordinator description nodes and RunStore singleton.

## Key Nodes

`Run coordinator — bus-native scheduler replacing LangGraph in Phase 2.`, `SQLite-backed durable run state for the Phase 2 coordinator.`, `Load a run record by id.`, `set_run_store()`, `_record_from_json()`

## Source Files

`src/coordinator/runner.py`, `src/coordinator/store.py`

## Related Notes

- [[pipeline/02-coordinator|Coordinator]] — full execution model
- [[communities/C06-runstore-sqlite|C06]] — SQLite persistence methods
