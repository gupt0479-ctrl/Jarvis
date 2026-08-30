---
type: community
members: 17
---

# vault_root

**Members:** 17 nodes

## Members
- [[Not a bare list (SimplifyJobsJGCLvanshb03) or a dict keyed by posting     id (]] - rationale - tests/test_schema_drift.py
- [[_json_response()]] - code - tests/test_schema_drift.py
- [[category is read via .get() so a rename wouldn't crash the normalizer —     it w]] - rationale - tests/test_schema_drift.py
- [[check_applyguy_schema()]] - code - core/schema_drift.py
- [[check_simplify_schema()]] - code - core/schema_drift.py
- [[season is read via .get() so a rename wouldn't crash the normalizer —     every]] - rationale - tests/test_schema_drift.py
- [[test_applyguy_schema_detects_dropped_listing_url_field()]] - code - tests/test_schema_drift.py
- [[test_applyguy_schema_detects_dropped_season_field()]] - code - tests/test_schema_drift.py
- [[test_applyguy_schema_detects_empty_jobs_list()]] - code - tests/test_schema_drift.py
- [[test_applyguy_schema_detects_wrong_shape()]] - code - tests/test_schema_drift.py
- [[test_applyguy_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_dropped_optional_field()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_dropped_permissive_field()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_empty_list()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_renamed_key()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_wrong_shape()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/vault_root
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_schema_drift.py]]
- 9 edges to [[_COMMUNITY_schema_drift.py]]
- 5 edges to [[_COMMUNITY_check_freehire_schema]]
- 4 edges to [[_COMMUNITY_check_ai_jobs_schema]]
- 4 edges to [[_COMMUNITY_check_ashby_schema]]
- 4 edges to [[_COMMUNITY_check_greenhouse_schema]]
- 4 edges to [[_COMMUNITY_check_lever_schema]]
- 3 edges to [[_COMMUNITY_check_all]]

## Top bridge nodes
- [[_json_response()]] - degree 42, connects to 8 communities
- [[check_simplify_schema()]] - degree 10, connects to 3 communities
- [[check_applyguy_schema()]] - degree 9, connects to 3 communities
- [[test_simplify_schema_detects_dropped_optional_field()]] - degree 4, connects to 1 community
- [[test_applyguy_schema_detects_dropped_season_field()]] - degree 4, connects to 1 community