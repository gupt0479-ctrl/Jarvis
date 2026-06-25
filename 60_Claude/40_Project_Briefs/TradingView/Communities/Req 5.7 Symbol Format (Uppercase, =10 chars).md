---
type: community
cohesion: 1.00
members: 1
---

# Req 5.7: Symbol Format (Uppercase, <=10 chars)

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.7 symbol must be 1-10 uppercase ASCII letters only.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_57_Symbol_Format_Uppercase_10_chars
SORT file.name ASC
```
