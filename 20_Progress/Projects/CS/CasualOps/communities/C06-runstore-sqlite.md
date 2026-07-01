# C06 — RunStore SQLite Persistence

**Community 6** — 14 nodes, cohesion 0.11

The SQLite-backed run state methods: create, update phase, increment barrier counts, append child configs.

## Key Nodes

`Connection`, `Path`, `Persist coordinator run state in SQLite.`, `Update run lifecycle status.`, `Update run phase and persist.`, `Increment completed parent count; return new total.`, `Increment completed child count; return new total.`, `Append child configs from a parent agent.`

## Source Files

`src/coordinator/store.py`

## Related Notes

- [[pipeline/02-coordinator|Coordinator]] — uses RunStore for all phase state
- [[communities/C27-runrecord-json|C27]] — RunRecord JSON serialization
