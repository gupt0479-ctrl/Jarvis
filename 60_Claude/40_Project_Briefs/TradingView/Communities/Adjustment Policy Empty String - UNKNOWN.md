---
type: community
cohesion: 1.00
members: 1
---

# Adjustment Policy: Empty String -> UNKNOWN

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[An empty string maps to PriceAdjustment.UNKNOWN.]] - rationale - tests/test_property_adjustment_mapping.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Adjustment_Policy_Empty_String_-_UNKNOWN
SORT file.name ASC
```
