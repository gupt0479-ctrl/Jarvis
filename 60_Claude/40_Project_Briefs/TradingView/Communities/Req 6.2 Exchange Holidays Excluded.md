---
type: community
cohesion: 1.00
members: 1
---

# Req 6.2: Exchange Holidays Excluded

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 6.2 Known exchange holidays are excluded from sessions.]] - rationale - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_62_Exchange_Holidays_Excluded
SORT file.name ASC
```
