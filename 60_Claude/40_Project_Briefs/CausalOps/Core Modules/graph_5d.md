---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, knowledge-graph, spatiotemporal, sqlite, 5d]
aliases: [graph_5d.py, graph_5d_stream.py]
---

# graph_5d.py — 5D Spatiotemporal Knowledge Graph

`src/graph_5d.py` implements a 5-dimensional spatiotemporal knowledge graph that captures `(Subject, Predicate, Object, Time, Location)` tuples from each run. It uses a dedicated SQLite database (`data/graph_5d.db`).

## The 5 Dimensions

1. **Subject** — who/what initiated the event (agent, asset, threat actor)
2. **Predicate** — the action or relationship (called, detected, escalated, spawned)
3. **Object** — the target (asset, artifact, causal variable)
4. **Time** — `observed_at` ISO timestamp
5. **Location** — network zone, host group, or spatial coordinates

## Node Types

```python
STNode types: "agent" | "asset" | "threat" | "artifact" | "causal_variable"
```

## Database Architecture

Stored in `data/graph_5d.db` — **separate file from `runs.db`** to avoid SQLite write contention between api and worker containers on shared bind mount.

```
# PRAGMA journal_mode=DELETE (not WAL — WAL shared-memory unreliable on Docker bind mounts)
# PRAGMA busy_timeout=30000
```

Tables: `st_nodes`, `st_edges` (with `run_id` foreign key for per-run isolation).

## Two Population Paths

### With Kafka: graph_5d_stream.py
Worker's `graph_5d_stream.py` consumer listens to `hivemind.artifacts` and streams every artifact event into the 5D graph in real-time as agents produce them. Edges get actual agent-emission timestamps.

### Without Kafka: Backfill
Coordinator calls `_backfill_5d_graph(record)` after the run completes:
```python
from graph_5d import connect_graph_db, reconstruct_5d_graph
conn = connect_graph_db()
reconstruct_5d_graph(conn, record.run_id, record)
```
`reconstruct_5d_graph` builds the graph from final `RunRecord` state — synthetic timestamps, but structurally complete.

## Key Functions

```python
log_st_node(conn, run_id, node_id, node_type, label, description, location)
log_st_edge(conn, run_id, subject_id, predicate, object_id, observed_at, location, confidence, edge_metadata)
get_5d_graph(conn, run_id) → {"run_id": ..., "nodes": [...], "edges": [...]}
```

## Manual Ingest API

`POST /run/{run_id}/graph/5d/ingest` allows external systems to push additional nodes/edges directly.

## Policy Optimization Integration

After policy learning completes, the RL report is also ingested into the KG:
```python
ingest_policy_optimization(conn, run_id, policy_optimization_report)
```

This adds policy shards, Q-values, and Stackelberg responses as graph nodes/edges for future traversal.

## env: CAUSALOPS_GRAPH_DB_PATH
Override the graph DB path (used in tests to point at an in-memory or temp DB).

## Related Notes

- [[Coordinator Execution Model]] — Where backfill and policy ingestion are called
- [[Kafka Bus Overview]] — graph_5d_stream.py consumer details
- [[reasoning]] — Produces anomalies that get ingested into the KG
- [[policy_learning]] — RL report ingested into KG after run completion
- [[api]] — `GET /run/{run_id}/graph/5d` and `/graph/5d/ingest` endpoints
