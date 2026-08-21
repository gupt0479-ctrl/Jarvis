---
type: community
members: 37
---

# test_identity.py

**Members:** 37 nodes

## Members
- [[A sourceATS with no recognizable job id in its URL shape (e.g.     Freehire's T]] - rationale - tests/test_identity.py
- [[Both remaining sources guarantee an id; a listing without one is a bug     (the]] - rationale - tests/test_identity.py
- [[Fix 1, Prompt 5 review (2026-07-30) the Google pattern used to have no     doma]] - rationale - tests/test_identity.py
- [[Layer 3 — stable dedup keys for a Listing.  Both remaining sources carry a stabl]] - rationale - core/identity.py
- [[Real Aquatic vs Aquatic Capital Management same Greenhouse posting,     same UR]] - rationale - tests/test_identity.py
- [[Real Google BS vs MS title-string variant, same numeric job id.]] - rationale - tests/test_identity.py
- [[Real Google BSMS Summer 2027 SWE intern duplicate vanshb03 and     Freehire bo]] - rationale - tests/test_identity.py
- [[Real Palantir 'Intel' FDSE duplicate across two different buckets     (SimplifyJ]] - rationale - tests/test_identity.py
- [[Real Palantir 'Intel' FDSE duplicate SimplifyJobs' URL carries a     trailing]] - rationale - tests/test_identity.py
- [[Real dup from the 2026-07-18 audit same Workday req via two routes,     titled]] - rationale - tests/test_run_pipeline.py
- [[Real profile.yaml entry 'D.E. Shaw' must match the real vault dossier     compan]] - rationale - tests/test_identity.py
- [[Real, confirmed 2026-07-29 — a genuine TRIPLE duplicate three     different tit]] - rationale - tests/test_identity.py
- [[The ATS-native job id embedded in url, or None if url is from a     sourceATS w]] - rationale - core/identity.py
- [[The matched preference tier (e.g. 'high'), or None if company isn't in     prefe]] - rationale - core/identity.py
- [[_norm_company()]] - code - core/identity.py
- [[company_matches_preference()]] - code - core/identity.py
- [[cross_source_key()]] - code - core/identity.py
- [[extract_ats_job_id()]] - code - core/identity.py
- [[identity.py]] - code - core/identity.py
- [[test_company_matches_preference_case_insensitive()]] - code - tests/test_identity.py
- [[test_company_matches_preference_none_for_empty_preferred_dict()]] - code - tests/test_identity.py
- [[test_company_matches_preference_none_for_unlisted_company()]] - code - tests/test_identity.py
- [[test_company_matches_preference_punctuation_insensitive_real_de_shaw_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_falls_back_to_normalized_text_when_no_job_id()]] - code - tests/test_identity.py
- [[test_cross_source_key_falls_back_to_text_for_company_name_variant_real_aquatic_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_normalizes_case_and_whitespace()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_google_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_palantir_cross_bucket_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_virtu_triple()]] - code - tests/test_identity.py
- [[test_cross_source_key_punctuation_insensitive_marmon_case()]] - code - tests/test_run_pipeline.py
- [[test_extract_ats_job_id_google_careers_results_url()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_google_pattern_is_domain_anchored()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_greenhouse()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_lever_ignores_apply_suffix()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_none_when_no_recognizable_id()]] - code - tests/test_identity.py
- [[test_identity.py]] - code - tests/test_identity.py
- [[test_missing_raw_id_raises()]] - code - tests/test_identity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_identitypy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_test_run_pipeline.py]]
- 5 edges to [[_COMMUNITY_test_filter.py]]
- 4 edges to [[_COMMUNITY_test_validate.py]]
- 3 edges to [[_COMMUNITY_test_debate.py]]
- 3 edges to [[_COMMUNITY_run_pipeline.py]]
- 3 edges to [[_COMMUNITY_test_writer.py]]

## Top bridge nodes
- [[identity.py]] - degree 13, connects to 5 communities
- [[test_identity.py]] - degree 32, connects to 3 communities
- [[cross_source_key()]] - degree 15, connects to 3 communities
- [[company_matches_preference()]] - degree 12, connects to 2 communities
- [[test_missing_raw_id_raises()]] - degree 4, connects to 2 communities