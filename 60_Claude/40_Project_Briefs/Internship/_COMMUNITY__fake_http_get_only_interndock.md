---
type: community
members: 8
---

# _fake_http_get_only_interndock

**Members:** 8 nodes

## Members
- [[End-to-end InternDock flows through matches()stage1_reject() and the     norma]] - rationale - tests/test_run_pipeline.py
- [[Every other source returns empty (in its own real response shape) —     isolates]] - rationale - tests/test_run_pipeline.py
- [[Same 'absence means off' convention as fetch_page_fn.]] - rationale - tests/test_run_pipeline.py
- [[_fake_http_get_only_interndock()]] - code - tests/test_run_pipeline.py
- [[_fake_interndock_sitemap_get()]] - code - tests/test_run_pipeline.py
- [[test_discover_interndock_fetches_only_new_candidates_and_persists_state()]] - code - tests/test_run_pipeline.py
- [[test_discover_interndock_returns_empty_when_fetch_fn_is_none()]] - code - tests/test_run_pipeline.py
- [[test_run_once_writes_interndock_listings_when_wired()]] - code - tests/test_run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_fake_http_get_only_interndock
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_writer.py]]

## Top bridge nodes
- [[_fake_interndock_sitemap_get()]] - degree 4, connects to 1 community
- [[_fake_http_get_only_interndock()]] - degree 4, connects to 1 community
- [[test_run_once_writes_interndock_listings_when_wired()]] - degree 4, connects to 1 community
- [[test_discover_interndock_returns_empty_when_fetch_fn_is_none()]] - degree 3, connects to 1 community
- [[test_discover_interndock_fetches_only_new_candidates_and_persists_state()]] - degree 2, connects to 1 community