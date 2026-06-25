---
type: community
cohesion: 1.00
members: 1
---

# Req 5.4: Volume Non-Negative

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.4 volume must be non-negative.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_54_Volume_Non-Negative
SORT file.name ASC
```
