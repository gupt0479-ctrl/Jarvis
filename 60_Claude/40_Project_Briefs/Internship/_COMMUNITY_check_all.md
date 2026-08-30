---
type: community
members: 4
---

# check_all

**Members:** 4 nodes

## Members
- [[Runs every check in order; raises SchemaDriftError from whichever     fails firs]] - rationale - core/schema_drift.py
- [[check_all()]] - code - core/schema_drift.py
- [[test_check_all_passes_when_all_sources_are_healthy()]] - code - tests/test_schema_drift.py
- [[test_check_all_raises_on_first_failing_source()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_all
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_schema_drift.py]]
- 3 edges to [[_COMMUNITY_schema_drift.py]]
- 3 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY_check_greenhouse_schema]]
- 1 edge to [[_COMMUNITY_check_ashby_schema]]
- 1 edge to [[_COMMUNITY_check_lever_schema]]
- 1 edge to [[_COMMUNITY_check_freehire_schema]]
- 1 edge to [[_COMMUNITY_check_ai_jobs_schema]]
- 1 edge to [[_COMMUNITY_check_interndock_sitemap]]

## Top bridge nodes
- [[check_all()]] - degree 18, connects to 10 communities
- [[test_check_all_raises_on_first_failing_source()]] - degree 3, connects to 2 communities
- [[test_check_all_passes_when_all_sources_are_healthy()]] - degree 2, connects to 1 community