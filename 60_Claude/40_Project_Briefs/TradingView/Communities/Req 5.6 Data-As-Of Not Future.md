---
type: community
cohesion: 1.00
members: 1
---

# Req 5.6: Data-As-Of Not Future

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.6 data_as_of cannot be in the future.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_56_Data-As-Of_Not_Future
SORT file.name ASC
```
