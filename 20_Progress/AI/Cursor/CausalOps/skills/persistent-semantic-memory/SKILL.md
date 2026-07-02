---
name: persistent-semantic-memory
description: Use when researching, designing, or implementing HiveMind's persistent semantic memory and retrieval layer, including vector retrieval, graph traversal, temporal indexing, run memory, provenance, and future MCP memory tools.
---

# Persistent Semantic Memory Skill

## Purpose

Design memory as a trusted context layer, not as empirical evidence. Retrieved
memory can inform agents and architecture, but causal estimates must still be
backed by current normalized evidence records and compiler gates.

## Design Checklist

- Define memory record types before adding storage.
- Track provenance for every stored and retrieved item.
- Separate current evidence from historical context.
- Preserve timestamps for temporal queries.
- Model entities and relationships for graph traversal.
- Support semantic search only with explicit source attribution.
- Keep storage swappable until requirements are stable.

## Candidate Memory Objects

- Run artifact summaries from `src/engine.py`.
- Decision memos from `src/schema.py`.
- Causal graph definitions and measurement plans.
- Evidence dataset profiles and estimator reports.
- User decisions and accepted architecture plans.
- Entity mentions: assets, users, CVEs, MITRE techniques, incidents, controls.

## Future MCP Bridge Shape

Start with a narrow tool surface:

- `memory.write`: store a typed memory record with provenance.
- `memory.search`: semantic search with filters and source metadata.
- `memory.get`: fetch a stored record by ID.
- `memory.timeline`: query records by time window and entity.
- `memory.traverse`: follow graph relationships from an entity or run.

Do not expose mutation-heavy or destructive tools until storage, auth, and audit
rules are reviewed.

## First Implementation Preference

For an initial local implementation, prefer a small typed abstraction around the
existing run artifacts before introducing a database. Add a real store only after
the memory schema, provenance model, and retrieval API are clear.
