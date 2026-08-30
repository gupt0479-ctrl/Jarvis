---
type: community
members: 41
---

# commit_and_push_with_retry

**Members:** 41 nodes

## Members
- [[A dossier written before dossier_uids.json existed (or hand-edited into     the]] - rationale - tests/test_recheck.py
- [[A source missing from feeds_by_source means its fetch failed — its     dossiers]] - rationale - tests/test_recheck.py
- [[Frontmatter dicts of every dossier file actually present in the vault     checko]] - rationale - vault_writer/writer.py
- [[Real dossier Optiver 'FPGA Internship (2027 Start)' — Netherlands,     a _NON_U]] - rationale - tests/test_revalidate.py
- [[Real dossier Optiver 'Software Engineer Intern' style content —     genuine tec]] - rationale - tests/test_revalidate.py
- [[Real dossier UHY 'Data Operations Intern' — Excel-only audit     support, no si]] - rationale - tests/test_revalidate.py
- [[Real dossier Vertiv 'Product Management Intern' — matches     stage1_reject's e]] - rationale - tests/test_revalidate.py
- [[Real, reproducible bug found 2026-08-23 scan_dossiers() globs Viewed     along]] - rationale - tests/test_recheck.py
- [[The dossier's own already-fetched content (verbatim, as originally     written)]] - rationale - revalidate.py
- [[The first rule this dossier would now fail under current code, or     None if it]] - rationale - revalidate.py
- [[{path, company, title, reason} for every live dossier that would     now fail]] - rationale - revalidate.py
- [[{uid, path, reason} for dossiers whose posting closed. A source that     faile]] - rationale - recheck.py
- [[_commit_log()]] - code - recheck.py
- [[_fm()]] - code - tests/test_recheck.py
- [[check_dossier()]] - code - revalidate.py
- [[datetime_1]] - code
- [[extract_posting_content()]] - code - revalidate.py
- [[file_github_issue()]] - code - run_pipeline.py
- [[find_regressions()]] - code - revalidate.py
- [[main()_2]] - code - recheck.py
- [[main()_3]] - code - revalidate.py
- [[plan_removals is the recheck's whole decision surface — pure, tested offline.]] - rationale - tests/test_recheck.py
- [[plan_removals()]] - code - recheck.py
- [[revalidate.py]] - code - revalidate.py
- [[revalidate.py — re-checks live dossiers against current core code using their o]] - rationale - tests/test_revalidate.py
- [[scan_dossiers()]] - code - vault_writer/writer.py
- [[test_absent_from_feed_is_removed()]] - code - tests/test_recheck.py
- [[test_active_false_upstream_is_removed()]] - code - tests/test_recheck.py
- [[test_all_active_removes_nothing()]] - code - tests/test_recheck.py
- [[test_already_removed_dossier_is_not_re_swept()]] - code - tests/test_recheck.py
- [[test_check_dossier_flags_real_non_us_location()]] - code - tests/test_revalidate.py
- [[test_check_dossier_flags_real_stage1_reject_title()]] - code - tests/test_revalidate.py
- [[test_check_dossier_flags_real_stage2_non_technical_content()]] - code - tests/test_revalidate.py
- [[test_check_dossier_passes_real_genuine_posting()]] - code - tests/test_revalidate.py
- [[test_dossier_with_no_manifest_entry_is_skipped_not_removed()]] - code - tests/test_recheck.py
- [[test_extract_posting_content_from_enriched_dossier()]] - code - tests/test_revalidate.py
- [[test_extract_posting_content_from_thin_dossier()]] - code - tests/test_revalidate.py
- [[test_failed_fetch_skips_that_sources_dossiers_entirely()]] - code - tests/test_recheck.py
- [[test_find_regressions_scans_real_vault_layout()]] - code - tests/test_revalidate.py
- [[test_recheck.py]] - code - tests/test_recheck.py
- [[test_revalidate.py]] - code - tests/test_revalidate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/commit_and_push_with_retry
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_write_dossier]]
- 10 edges to [[_COMMUNITY_recheck.py]]
- 5 edges to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 2 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 2 edges to [[_COMMUNITY_build_frontmatter]]
- 2 edges to [[_COMMUNITY_writer.py_1]]
- 1 edge to [[_COMMUNITY__fake_http_get_only_interndock]]

## Top bridge nodes
- [[revalidate.py]] - degree 14, connects to 4 communities
- [[scan_dossiers()]] - degree 9, connects to 4 communities
- [[main()_2]] - degree 8, connects to 3 communities
- [[_commit_log()]] - degree 6, connects to 3 communities
- [[plan_removals()]] - degree 11, connects to 2 communities