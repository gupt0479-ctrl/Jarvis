# C27 — RunRecord JSON Serialization

**Community 27** — 5 nodes, cohesion 0.25

The RunRecord insert and JSON serialization functions.

## Key Nodes

`Insert a new run record.`, `Create a queued run awaiting background execution.`, `Merge a node return dict into this record.`, `_record_to_json()`

## What This Code Does

`_record_to_json()` serializes a `RunRecord` dataclass to the JSON blob stored in SQLite. Handles all nested Pydantic models (AgentConfig, DecisionMemo, etc.) via `model_dump()`. The inverse `_record_from_json()` deserializes on read.

## Source File

`src/coordinator/store.py`

## Related Notes

- [[communities/C06-runstore-sqlite|C06]] — uses these serialization functions
