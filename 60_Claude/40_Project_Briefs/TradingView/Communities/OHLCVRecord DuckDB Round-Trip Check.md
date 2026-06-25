---
type: community
cohesion: 1.00
members: 1
---

# OHLCVRecord DuckDB Round-Trip Check

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Store a valid OHLCVRecord in DuckDB and verify all fields survive the round trip]] - rationale - tests/test_property_roundtrip.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OHLCVRecord_DuckDB_Round-Trip_Check
SORT file.name ASC
```
