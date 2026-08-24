---
type: community
members: 21
---

# test_writer.py

**Members:** 21 nodes

## Members
- [[If the exact same uid were somehow matched twice in one run, it should     only]] - rationale - tests/test_run_pipeline.py
- [[Keys come from the dossier files actually in the checkout — a listing     whose]] - rationale - tests/test_run_pipeline.py
- [[Pre-seed stateexcluded_uids.json with a real candidate's uid already     at the]] - rationale - tests/test_debate_losses.py
- [[Same program via two sources (two distinct uids, one company+title) —     the se]] - rationale - tests/test_run_pipeline.py
- [[_fake_http_head_all_live()]] - code - tests/test_run_pipeline.py
- [[_page_with()]] - code - tests/test_run_pipeline.py
- [[_simplify_raw()]] - code - tests/test_run_pipeline.py
- [[compute_uid()]] - code - core/identity.py
- [[normalize_simplify()]] - code - ingestion/normalize.py
- [[test_dedup_new_dedupes_within_the_same_run()]] - code - tests/test_run_pipeline.py
- [[test_dedup_new_skips_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_eligible_posting_gets_content_section()]] - code - tests/test_run_pipeline.py
- [[test_fetch_and_filter_skips_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_fetch_failure_fails_open_to_thin_dossier()]] - code - tests/test_run_pipeline.py
- [[test_opt_cache_short_circuits_before_fetch()]] - code - tests/test_run_pipeline.py
- [[test_opt_exclusion_rejects_and_caches()]] - code - tests/test_run_pipeline.py
- [[test_run_once_never_fetches_an_already_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_validate_and_write_happy_path()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_rejects_dead_url()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - code - tests/test_run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_writerpy
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_plan_removals]]
- 11 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 11 edges to [[_COMMUNITY_test_filter.py]]
- 6 edges to [[_COMMUNITY_phd_only_exclusion]]
- 5 edges to [[_COMMUNITY_normalize.py]]
- 4 edges to [[_COMMUNITY_recheck.py]]
- 3 edges to [[_COMMUNITY_test_posting_page.py]]
- 2 edges to [[_COMMUNITY_render_dossier]]
- 2 edges to [[_COMMUNITY_build_frontmatter]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_matches]]

## Top bridge nodes
- [[normalize_simplify()]] - degree 36, connects to 11 communities
- [[compute_uid()]] - degree 26, connects to 6 communities
- [[_simplify_raw()]] - degree 18, connects to 3 communities
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - degree 7, connects to 2 communities
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - degree 7, connects to 2 communities