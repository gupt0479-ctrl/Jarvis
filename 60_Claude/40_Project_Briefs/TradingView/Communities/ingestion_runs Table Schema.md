---
type: community
cohesion: 1.00
members: 1
---

# ingestion_runs Table Schema

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[ingestion_runs Table Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingestion_runs_Table_Schema
SORT file.name ASC
```
