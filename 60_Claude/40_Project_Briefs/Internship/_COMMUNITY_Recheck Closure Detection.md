---
type: community
members: 12
---

# Recheck Closure Detection

**Members:** 12 nodes

## Members
- [[A dossier written before dossier_uids.json existed (or hand-edited into     the]] - rationale - tests/test_recheck.py
- [[A source missing from feeds_by_source means its fetch failed — its     dossiers]] - rationale - tests/test_recheck.py
- [[{uid, path, reason} for dossiers whose posting closed. A source that     faile]] - rationale - recheck.py
- [[_fm()]] - code - tests/test_recheck.py
- [[plan_removals is the recheck's whole decision surface — pure, tested offline.]] - rationale - tests/test_recheck.py
- [[plan_removals()]] - code - recheck.py
- [[test_absent_from_feed_is_removed()]] - code - tests/test_recheck.py
- [[test_active_false_upstream_is_removed()]] - code - tests/test_recheck.py
- [[test_all_active_removes_nothing()]] - code - tests/test_recheck.py
- [[test_dossier_with_no_manifest_entry_is_skipped_not_removed()]] - code - tests/test_recheck.py
- [[test_failed_fetch_skips_that_sources_dossiers_entirely()]] - code - tests/test_recheck.py
- [[test_recheck.py]] - code - tests/test_recheck.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Recheck_Closure_Detection
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]

## Top bridge nodes
- [[plan_removals()]] - degree 10, connects to 1 community
- [[test_recheck.py]] - degree 9, connects to 1 community
- [[_fm()]] - degree 3, connects to 1 community