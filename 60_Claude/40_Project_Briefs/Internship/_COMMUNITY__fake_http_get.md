---
type: community
members: 8
---

# _fake_http_get

**Members:** 8 nodes

## Members
- [[_applyguy_raw()]] - code - tests/test_run_pipeline.py
- [[_fake_http_get()]] - code - tests/test_run_pipeline.py
- [[_josegael_raw()]] - code - tests/test_run_pipeline.py
- [[_strip_case_keys()]] - code - tests/test_run_pipeline.py
- [[_vanshb03_raw()]] - code - tests/test_run_pipeline.py
- [[_zshah101_raw()]] - code - tests/test_run_pipeline.py
- [[test_dedup_new_splits_new_vs_already_seen()]] - code - tests/test_run_pipeline.py
- [[test_fetch_and_filter_counts_and_matches()]] - code - tests/test_run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_fake_http_get
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_writer.py]]
- 5 edges to [[_COMMUNITY_normalize_simplify]]

## Top bridge nodes
- [[_fake_http_get()]] - degree 10, connects to 2 communities
- [[_strip_case_keys()]] - degree 6, connects to 2 communities
- [[_josegael_raw()]] - degree 5, connects to 2 communities
- [[test_fetch_and_filter_counts_and_matches()]] - degree 4, connects to 2 communities
- [[test_dedup_new_splits_new_vs_already_seen()]] - degree 3, connects to 2 communities