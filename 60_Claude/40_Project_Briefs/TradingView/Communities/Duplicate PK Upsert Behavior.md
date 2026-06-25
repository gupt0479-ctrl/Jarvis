---
type: community
cohesion: 1.00
members: 1
---

# Duplicate PK Upsert Behavior

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Inserting two records with the same PK results in one row with second record's v]] - rationale - tests/test_property_duplicate_pk.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Duplicate_PK_Upsert_Behavior
SORT file.name ASC
```
