# C31 — Run Status + Artifact Loading

**Community 31** — 4 nodes, cohesion 0.50

The run status endpoint and artifact file loader.

## Key Nodes

`get_run_status()`, `Return run lifecycle status and artifact when complete.`, `load_run_artifact()`

## What This Code Does

`get_run_status()` handles `GET /run/{run_id}`. Checks SQLite `RunRecord.status`, loads artifact JSON from disk if completed. Race condition guard: if SQLite shows "completed" but artifact file isn't written yet → returns `effective_status: "running"`.

`load_run_artifact(run_id)` reads `data/{run_id}.json` from disk.

## Source File

`src/api.py`, `src/engine.py`

## Related Notes

- [[infrastructure/01-api|API Reference]] — GET /run/{run_id}
