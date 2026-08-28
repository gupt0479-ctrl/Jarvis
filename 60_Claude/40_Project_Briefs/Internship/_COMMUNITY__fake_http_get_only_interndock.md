---
type: community
members: 14
---

# _fake_http_get_only_interndock

**Members:** 14 nodes

## Members
- [[A dossier written before dossier_uids.json existed (or hand-edited into     the]] - rationale - tests/test_recheck.py
- [[A source missing from feeds_by_source means its fetch failed — its     dossiers]] - rationale - tests/test_recheck.py
- [[Real, reproducible bug found 2026-08-23 scan_dossiers() globs Viewed     along]] - rationale - tests/test_recheck.py
- [[{uid, path, reason} for dossiers whose posting closed. A source that     faile]] - rationale - recheck.py
- [[_fm()]] - code - tests/test_recheck.py
- [[plan_removals is the recheck's whole decision surface — pure, tested offline.]] - rationale - tests/test_recheck.py
- [[plan_removals()]] - code - recheck.py
- [[test_absent_from_feed_is_removed()]] - code - tests/test_recheck.py
- [[test_active_false_upstream_is_removed()]] - code - tests/test_recheck.py
- [[test_all_active_removes_nothing()]] - code - tests/test_recheck.py
- [[test_already_removed_dossier_is_not_re_swept()]] - code - tests/test_recheck.py
- [[test_dossier_with_no_manifest_entry_is_skipped_not_removed()]] - code - tests/test_recheck.py
- [[test_failed_fetch_skips_that_sources_dossiers_entirely()]] - code - tests/test_recheck.py
- [[test_recheck.py]] - code - tests/test_recheck.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_fake_http_get_only_interndock
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_write_dossier]]
- 2 edges to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry]]

## Top bridge nodes
- [[plan_removals()]] - degree 11, connects to 3 communities
- [[test_recheck.py]] - degree 10, connects to 1 community
- [[_fm()]] - degree 4, connects to 1 community