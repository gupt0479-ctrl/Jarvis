# C01 — 5D Knowledge Graph Ingestion

**Community 1** — 49 nodes, cohesion 0.11

Functions that write structured events from run artifacts into the 5D spatiotemporal knowledge graph. This is the real-time streaming path (Kafka consumer in `graph_5d_stream.py`) and the batch backfill path.

## Key Nodes

`_derive_location()`, `get_5d_graph()`, `ingest_causal()`, `ingest_child()`, `ingest_evidence_record()`, `ingest_evolution_report()`, `ingest_findings()`

## What This Code Does

For each artifact type arriving on `hivemind.artifacts`, a type-specific `ingest_*` function parses the payload and writes nodes/edges to `graph_5d.db`. The 5D dimensions: Subject, Predicate, Object, Time, Location.

`_derive_location()` extracts the spatial coordinate (network zone or host group) from evidence or agent metadata.

## Source Files

`src/graph_5d.py`, `src/graph_5d_stream.py`

## Related Notes

- [[event-bus/01-worker|Spawn Worker]] — runs the graph_5d_stream.py consumer
- [[pipeline/02-coordinator|Coordinator]] — `_backfill_5d_graph` (no-Kafka path)
