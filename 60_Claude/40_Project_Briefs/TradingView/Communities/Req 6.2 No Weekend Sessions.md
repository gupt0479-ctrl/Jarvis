---
type: community
cohesion: 1.00
members: 1
---

# Req 6.2: No Weekend Sessions

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 6.2 No Saturday or Sunday in returned sessions.]] - rationale - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_62_No_Weekend_Sessions
SORT file.name ASC
```
