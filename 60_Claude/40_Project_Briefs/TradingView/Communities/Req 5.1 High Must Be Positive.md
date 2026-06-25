---
type: community
cohesion: 1.00
members: 1
---

# Req 5.1: High Must Be Positive

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.1 high must be strictly greater than zero.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_51_High_Must_Be_Positive
SORT file.name ASC
```
