# C10 — API Endpoints

**Community 10** — 22 nodes, cohesion 0.10

FastAPI endpoint handlers for the HiveMind HTTP interface.

## Key Nodes

`_allowed_origins()`, `get_run_5d_graph()`, `get_run_reasoning()`, `health_check()`, `Ingest5DRequest`, `ingest_run_5d_graph()`, `lifespan()`

## What This Code Does

The FastAPI app definition with all endpoint handlers. `lifespan()` manages startup/shutdown: starts Kafka producer, optionally starts in-process spawn worker. `_allowed_origins()` parses `HIVEMIND_ALLOWED_ORIGINS` for CORS.

`get_run_5d_graph()` and `get_run_reasoning()` are the two graph/reasoning endpoints.

## Source File

`src/api.py`

## Related Notes

- [[infrastructure/01-api|API Reference]] — all endpoints with curl examples
