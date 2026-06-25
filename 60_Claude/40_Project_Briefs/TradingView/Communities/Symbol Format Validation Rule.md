---
type: community
cohesion: 1.00
members: 1
---

# Symbol Format Validation Rule

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Symbol must be uppercase ASCII letters only, max 10 chars.]] - rationale - src/research_data/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Symbol_Format_Validation_Rule
SORT file.name ASC
```
