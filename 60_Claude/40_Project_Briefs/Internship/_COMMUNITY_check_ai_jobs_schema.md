---
type: community
members: 6
---

# check_ai_jobs_schema

**Members:** 6 nodes

## Members
- [[check_ai_jobs_schema()]] - code - core/schema_drift.py
- [[level is what fetch_ai_jobs' own role-type triage reads     (raw.get(level) ==]] - rationale - tests/test_schema_drift.py
- [[test_ai_jobs_schema_detects_dropped_level_field()]] - code - tests/test_schema_drift.py
- [[test_ai_jobs_schema_detects_empty_jobs_list()]] - code - tests/test_schema_drift.py
- [[test_ai_jobs_schema_hits_the_real_url()]] - code - tests/test_schema_drift.py
- [[test_ai_jobs_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_ai_jobs_schema
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_schema_drift.py]]
- 4 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_schema_drift.py]]
- 1 edge to [[_COMMUNITY_check_all]]

## Top bridge nodes
- [[check_ai_jobs_schema()]] - degree 8, connects to 3 communities
- [[test_ai_jobs_schema_detects_dropped_level_field()]] - degree 4, connects to 2 communities
- [[test_ai_jobs_schema_passes_on_real_shape()]] - degree 3, connects to 2 communities
- [[test_ai_jobs_schema_hits_the_real_url()]] - degree 3, connects to 2 communities
- [[test_ai_jobs_schema_detects_empty_jobs_list()]] - degree 3, connects to 2 communities