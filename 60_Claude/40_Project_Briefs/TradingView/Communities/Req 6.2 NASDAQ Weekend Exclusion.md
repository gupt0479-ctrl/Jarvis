---
type: community
cohesion: 1.00
members: 1
---

# Req 6.2: NASDAQ Weekend Exclusion

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 6.2 NASDAQ sessions also exclude weekends.]] - rationale - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_62_NASDAQ_Weekend_Exclusion
SORT file.name ASC
```
