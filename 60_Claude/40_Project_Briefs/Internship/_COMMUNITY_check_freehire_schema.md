---
type: community
members: 8
---

# check_freehire_schema

**Members:** 8 nodes

## Members
- [[The one company (google) legitimately having zero intern-tagged     postings rig]] - rationale - tests/test_schema_drift.py
- [[check_freehire_schema()]] - code - core/schema_drift.py
- [[seniority lives nested under enrichment — what fetch_freehire's own     role-typ]] - rationale - tests/test_schema_drift.py
- [[test_freehire_schema_detects_dropped_nested_seniority()]] - code - tests/test_schema_drift.py
- [[test_freehire_schema_detects_dropped_public_slug()]] - code - tests/test_schema_drift.py
- [[test_freehire_schema_hits_the_schema_check_slug()]] - code - tests/test_schema_drift.py
- [[test_freehire_schema_passes_on_empty_data_list()]] - code - tests/test_schema_drift.py
- [[test_freehire_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_freehire_schema
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_schema_drift.py]]
- 5 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_schema_drift.py]]
- 1 edge to [[_COMMUNITY_check_all]]

## Top bridge nodes
- [[check_freehire_schema()]] - degree 9, connects to 3 communities
- [[test_freehire_schema_detects_dropped_nested_seniority()]] - degree 4, connects to 2 communities
- [[test_freehire_schema_passes_on_empty_data_list()]] - degree 4, connects to 2 communities
- [[test_freehire_schema_passes_on_real_shape()]] - degree 3, connects to 2 communities
- [[test_freehire_schema_hits_the_schema_check_slug()]] - degree 3, connects to 2 communities