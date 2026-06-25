---
type: community
cohesion: 1.00
members: 1
---

# Req 5.1: Close Must Be Positive

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.1 close must be strictly greater than zero.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_51_Close_Must_Be_Positive
SORT file.name ASC
```
