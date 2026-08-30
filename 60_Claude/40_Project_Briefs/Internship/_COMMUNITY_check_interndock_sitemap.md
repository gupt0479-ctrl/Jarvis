---
type: community
members: 8
---

# check_interndock_sitemap

**Members:** 8 nodes

## Members
- [[Every real URL is still there, but none look drop-shaped anymore —     e.g. inte]] - rationale - tests/test_schema_drift.py
- [[Not a field-schema check (InternDock has no JSON API — see the block     comment]] - rationale - core/schema_drift.py
- [[_text_response()]] - code - tests/test_schema_drift.py
- [[check_interndock_sitemap()]] - code - core/schema_drift.py
- [[test_interndock_sitemap_detects_no_drop_shaped_candidates()]] - code - tests/test_schema_drift.py
- [[test_interndock_sitemap_detects_no_loc_entries()]] - code - tests/test_schema_drift.py
- [[test_interndock_sitemap_hits_the_real_url()]] - code - tests/test_schema_drift.py
- [[test_interndock_sitemap_passes_on_real_shape()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_interndock_sitemap
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_schema_drift.py]]
- 2 edges to [[_COMMUNITY_schema_drift.py]]
- 1 edge to [[_COMMUNITY_check_all]]

## Top bridge nodes
- [[check_interndock_sitemap()]] - degree 9, connects to 3 communities
- [[_text_response()]] - degree 5, connects to 1 community
- [[test_interndock_sitemap_detects_no_drop_shaped_candidates()]] - degree 4, connects to 1 community
- [[test_interndock_sitemap_passes_on_real_shape()]] - degree 3, connects to 1 community
- [[test_interndock_sitemap_hits_the_real_url()]] - degree 3, connects to 1 community