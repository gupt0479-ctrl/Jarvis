---
type: community
members: 18
---

# test_schema_drift.py

**Members:** 18 nodes

## Members
- [[Fixtures carry a test-only _case label; real upstream entries don't.]] - rationale - tests/test_schema_drift.py
- [[_strip_case_keys()_1]] - code - tests/test_schema_drift.py
- [[ai_jobs_raw()]] - code - tests/test_schema_drift.py
- [[applyguy_raw()]] - code - tests/test_schema_drift.py
- [[ashby_raw()]] - code - tests/test_schema_drift.py
- [[check_josegael_schema()]] - code - core/schema_drift.py
- [[freehire_raw()]] - code - tests/test_schema_drift.py
- [[greenhouse_raw()]] - code - tests/test_schema_drift.py
- [[interndock_sitemap_text()]] - code - tests/test_schema_drift.py
- [[josegael_raw()]] - code - tests/test_schema_drift.py
- [[lever_raw()]] - code - tests/test_schema_drift.py
- [[simplify_raw()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_detects_dropped_permissive_field()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_detects_renamed_key()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_schema_drift.py]] - code - tests/test_schema_drift.py
- [[vanshb03_raw()]] - code - tests/test_schema_drift.py
- [[zshah101_raw()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_schema_driftpy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_vault_root]]
- 11 edges to [[_COMMUNITY_schema_drift.py]]
- 6 edges to [[_COMMUNITY_check_freehire_schema]]
- 6 edges to [[_COMMUNITY_check_interndock_sitemap]]
- 5 edges to [[_COMMUNITY_check_greenhouse_schema]]
- 5 edges to [[_COMMUNITY_check_ashby_schema]]
- 5 edges to [[_COMMUNITY_check_lever_schema]]
- 5 edges to [[_COMMUNITY_check_ai_jobs_schema]]
- 4 edges to [[_COMMUNITY_check_all]]
- 1 edge to [[_COMMUNITY_test_freehire.py]]
- 1 edge to [[_COMMUNITY_interndock.py]]
- 1 edge to [[_COMMUNITY_write_dossier]]

## Top bridge nodes
- [[test_schema_drift.py]] - degree 77, connects to 12 communities
- [[check_josegael_schema()]] - degree 7, connects to 2 communities
- [[test_josegael_schema_passes_on_real_shape()]] - degree 3, connects to 1 community
- [[test_josegael_schema_detects_renamed_key()]] - degree 3, connects to 1 community
- [[test_josegael_schema_detects_dropped_permissive_field()]] - degree 3, connects to 1 community