---
type: community
cohesion: 1.00
members: 1
---

# OHLC Positivity Validation Rule

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Open, high, low, close must be strictly greater than zero.]] - rationale - src/research_data/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OHLC_Positivity_Validation_Rule
SORT file.name ASC
```
