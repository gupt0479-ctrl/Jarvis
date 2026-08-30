---
type: community
members: 15
---

# schema_drift.py

**Members:** 15 nodes

## Members
- [[Exception]] - code
- [[GreenhouseAshbyAIJobs' shared shape a dict wrapping a jobs list —     same]] - rationale - core/schema_drift.py
- [[Schema-drift check. Runs before the scheduled pipeline touches feeds for real f]] - rationale - core/schema_drift.py
- [[SchemaDriftError]] - code - core/schema_drift.py
- [[The one source shaped as a dict, not a list — a schema check that     assumed li]] - rationale - tests/test_schema_drift.py
- [[_check_json_source()]] - code - core/schema_drift.py
- [[_check_wrapped_jobs_source()]] - code - core/schema_drift.py
- [[check_vanshb03_schema()]] - code - core/schema_drift.py
- [[check_zshah101_schema()]] - code - core/schema_drift.py
- [[schema_drift.py]] - code - core/schema_drift.py
- [[test_vanshb03_schema_detects_dropped_sponsorship_field()]] - code - tests/test_schema_drift.py
- [[test_vanshb03_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_detects_dropped_is_open_field()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_detects_wrong_shape()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/schema_driftpy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_schema_drift.py]]
- 9 edges to [[_COMMUNITY_vault_root]]
- 3 edges to [[_COMMUNITY_check_all]]
- 3 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_check_ai_jobs_schema]]
- 2 edges to [[_COMMUNITY_check_ashby_schema]]
- 2 edges to [[_COMMUNITY_check_freehire_schema]]
- 2 edges to [[_COMMUNITY_check_greenhouse_schema]]
- 2 edges to [[_COMMUNITY_check_interndock_sitemap]]
- 2 edges to [[_COMMUNITY_check_lever_schema]]
- 2 edges to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry]]
- 1 edge to [[_COMMUNITY_test_freehire.py]]
- 1 edge to [[_COMMUNITY_interndock.py]]
- 1 edge to [[_COMMUNITY_write_dossier]]

## Top bridge nodes
- [[schema_drift.py]] - degree 22, connects to 14 communities
- [[SchemaDriftError]] - degree 11, connects to 6 communities
- [[_check_json_source()]] - degree 7, connects to 3 communities
- [[_check_wrapped_jobs_source()]] - degree 6, connects to 3 communities
- [[check_zshah101_schema()]] - degree 7, connects to 2 communities