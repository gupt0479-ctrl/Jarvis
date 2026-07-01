# C28 — 5D Graph Database Connection

**Community 28** — 6 nodes, cohesion 0.33

SQLite connection management for the 5D KG database (`graph_5d.db`).

## Key Nodes

`connect_graph_db()`, `graph_db_path()`, `Fetch the compiled 5D spatiotemporal graph nodes and edges.`, `Open (and lazily initialise) a connection to the dedicated graph DB.`, `Resolve the 5D graph database path (overridable via env for tests).`

## What This Code Does

`connect_graph_db()` opens `graph_5d.db`, creates tables if not exist (`st_nodes`, `st_edges`), sets journal_mode=DELETE and busy_timeout. Uses `HIVEMIND_GRAPH_DB_PATH` env var for test overrides.

`graph_db_path()` resolves the DB path: `HIVEMIND_GRAPH_DB_PATH` env → `data_dir() / "graph_5d.db"`.

## Source File

`src/graph_5d.py`

## Related Notes

- [[infrastructure/00-docker|Docker Setup]] — separate graph_5d.db volume
