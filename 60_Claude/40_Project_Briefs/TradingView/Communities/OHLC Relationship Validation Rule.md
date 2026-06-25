---
type: community
cohesion: 1.00
members: 1
---

# OHLC Relationship Validation Rule

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Validate OHLC price relationships high = opencloselow, low = openclose.]] - rationale - src/research_data/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OHLC_Relationship_Validation_Rule
SORT file.name ASC
```
