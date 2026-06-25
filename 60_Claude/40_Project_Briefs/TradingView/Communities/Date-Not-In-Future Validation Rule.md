---
type: community
cohesion: 1.00
members: 1
---

# Date-Not-In-Future Validation Rule

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[trading_date and data_as_of cannot be in the future (UTC).]] - rationale - src/research_data/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Date-Not-In-Future_Validation_Rule
SORT file.name ASC
```
