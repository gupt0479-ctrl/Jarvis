---
type: community
cohesion: 1.00
members: 1
---

# Req 6.4: Sessions Within Requested Range

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 6.4 All returned sessions fall within start, end.]] - rationale - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_64_Sessions_Within_Requested_Range
SORT file.name ASC
```
