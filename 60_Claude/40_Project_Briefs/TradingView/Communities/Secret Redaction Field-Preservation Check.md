---
type: community
cohesion: 1.00
members: 1
---

# Secret Redaction Field-Preservation Check

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Verify secret fields are redacted and non-secret fields preserved in stored reco]] - rationale - tests/test_property_no_secrets.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Secret_Redaction_Field-Preservation_Check
SORT file.name ASC
```
