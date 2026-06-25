---
type: community
cohesion: 1.00
members: 1
---

# Req 5.3: Low <= Open

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.3 low must be = open.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_53_Low__Open
SORT file.name ASC
```
