---
type: community
cohesion: 1.00
members: 1
---

# Property: Empty Response -> Zero Records

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[For any empty provider response, normalization SHALL produce zero valid records.]] - rationale - tests/test_property_no_fabrication.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Property_Empty_Response_-_Zero_Records
SORT file.name ASC
```
