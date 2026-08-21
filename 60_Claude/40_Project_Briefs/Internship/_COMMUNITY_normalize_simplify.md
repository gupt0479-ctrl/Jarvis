---
type: community
members: 21
---

# normalize_simplify

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
TABLE source_file, type FROM #community/normalize_simplify
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Fetch, Dedup & Identity]]
- 11 edges to [[_COMMUNITY_Cross-Source Identity Keys]]
- 10 edges to [[_COMMUNITY_Layer 1 Eligibility Filter]]
- 5 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]
- 5 edges to [[_COMMUNITY_test_debate_losses.py]]
- 3 edges to [[_COMMUNITY__listing_with_date]]
- 2 edges to [[_COMMUNITY_CSSoftware Relevance Gate]]
- 2 edges to [[_COMMUNITY_Write-Gate Validation Tests]]
- 2 edges to [[_COMMUNITY_Dossier Writer (Vault Output)]]

## Top bridge nodes
- [[normalize_simplify()]] - degree 36, connects to 9 communities
- [[compute_uid()]] - degree 25, connects to 5 communities
- [[_simplify_raw()]] - degree 18, connects to 2 communities
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - degree 7, connects to 2 communities
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - degree 7, connects to 2 communities