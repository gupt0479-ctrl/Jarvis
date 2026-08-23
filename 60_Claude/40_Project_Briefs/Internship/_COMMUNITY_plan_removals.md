---
type: community
members: 14
---

# plan_removals

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
TABLE source_file, type FROM #community/plan_removals
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[plan_removals()]] - degree 11, connects to 1 community
- [[test_recheck.py]] - degree 10, connects to 1 community
- [[_fm()]] - degree 4, connects to 1 community