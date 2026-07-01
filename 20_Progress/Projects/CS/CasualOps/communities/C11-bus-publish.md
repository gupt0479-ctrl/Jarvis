# C11 — Bus Publish Functions

**Community 11** — 21 nodes, cohesion 0.17

The Kafka publish functions used throughout the codebase. Every node that produces an artifact calls these.

## Key Nodes

`get_run_context()`, `_emit()`, `publish_artifact()`, `publish_run_event()`, `publish_spawn()`, `publish_telemetry()`

## What This Code Does

`publish_telemetry()` creates an `EXECUTION_PHASE` envelope → `hivemind.telemetry`. Called by every agent node at start and end.

`publish_artifact()` creates a typed artifact envelope → correct topic via `topic_for_artifact()`.

`publish_spawn()` creates `AGENT_CONFIG` or `CHILD_CONFIG` envelope → `hivemind.spawn`.

`publish_run_event()` publishes `RUN_STARTED` / `RUN_COMPLETED` / `RUN_FAILED` → `hivemind.runs`.

All functions call the internal `_emit()` which handles the actual Kafka send.

## Source File

`src/bus/publish.py`

## Related Notes

- [[event-bus/00-topics|Kafka Topics]] — routing table
