---
type: community
cohesion: 1.00
members: 1
---

# Req 5.3: Low <= Close

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.3 low must be = close.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_53_Low__Close
SORT file.name ASC
```
