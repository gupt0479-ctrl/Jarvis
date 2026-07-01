# C26 — Run Enqueue Logic

**Community 26** — 11 nodes, cohesion 0.18

API-level run enqueue: the background task launcher and the blocking sync endpoint.

## Key Nodes

`enqueue_run()`, `_execute_run_background()`, `Request body for the full agentic workflow.`, `Run HiveMind in the background for async POST /run.`, `Blocking run endpoint retained for scripts and integration tests.`, `run_engine_sync()`

## What This Code Does

`POST /run` calls `enqueue_run()` which creates a `RunRecord` in SQLite with `status="queued"` and fires `_execute_run_background()` as a FastAPI `BackgroundTask`. Returns immediately with `{"run_id": ..., "status": "queued"}`.

`run_engine_sync()` wraps `run_hivemind()` in a `asyncio.run()` call for the blocking sync endpoint.

## Source File

`src/api.py`

## Related Notes

- [[infrastructure/01-api|API Reference]] — POST /run and POST /run/sync
