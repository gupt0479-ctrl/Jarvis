---
type: community
cohesion: 1.00
members: 1
---

# Sessions Returned Chronologically

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Sessions should be returned in chronological order.]] - rationale - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Sessions_Returned_Chronologically
SORT file.name ASC
```
