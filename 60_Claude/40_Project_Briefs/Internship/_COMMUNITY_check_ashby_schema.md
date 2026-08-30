---
type: community
members: 7
---

# check_ashby_schema

**Members:** 7 nodes

## Members
- [[One company (elevenlabs) legitimately having zero open reqs right     now is mun]] - rationale - tests/test_schema_drift.py
- [[check_ashby_schema()]] - code - core/schema_drift.py
- [[employmentType is what fetch_ashby's own role-type triage reads     (job.get(em]] - rationale - tests/test_schema_drift.py
- [[test_ashby_schema_detects_dropped_employment_type()]] - code - tests/test_schema_drift.py
- [[test_ashby_schema_hits_the_schema_check_token()]] - code - tests/test_schema_drift.py
- [[test_ashby_schema_passes_on_empty_jobs_list()]] - code - tests/test_schema_drift.py
- [[test_ashby_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_ashby_schema
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_schema_drift.py]]
- 4 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_schema_drift.py]]
- 1 edge to [[_COMMUNITY_check_all]]

## Top bridge nodes
- [[check_ashby_schema()]] - degree 8, connects to 3 communities
- [[test_ashby_schema_detects_dropped_employment_type()]] - degree 4, connects to 2 communities
- [[test_ashby_schema_passes_on_empty_jobs_list()]] - degree 4, connects to 2 communities
- [[test_ashby_schema_passes_on_real_shape()]] - degree 3, connects to 2 communities
- [[test_ashby_schema_hits_the_schema_check_token()]] - degree 3, connects to 2 communities