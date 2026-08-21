---
type: community
members: 28
---

# Cross-Source Identity Keys

**Members:** 28 nodes

## Members
- [[Both remaining sources guarantee an id; a listing without one is a bug     (the]] - rationale - tests/test_identity.py
- [[Fix 1, Prompt 5 review (2026-07-30) the Google pattern used to have no     doma]] - rationale - tests/test_identity.py
- [[Layer 3 — stable dedup keys for a Listing.  Both remaining sources carry a stabl]] - rationale - core/identity.py
- [[Real Google BSMS Summer 2027 SWE intern duplicate vanshb03 and     Freehire bo]] - rationale - tests/test_identity.py
- [[Real Palantir 'Intel' FDSE duplicate SimplifyJobs' URL carries a     trailing]] - rationale - tests/test_identity.py
- [[Real profile.yaml entry 'D.E. Shaw' must match the real vault dossier     compan]] - rationale - tests/test_identity.py
- [[The ATS-native job id embedded in url, or None if url is from a     sourceATS w]] - rationale - core/identity.py
- [[The matched preference tier (e.g. 'high'), or None if company isn't in     prefe]] - rationale - core/identity.py
- [[_load()_2]] - code - tests/test_identity.py
- [[_norm_company()]] - code - core/identity.py
- [[company_matches_preference()]] - code - core/identity.py
- [[extract_ats_job_id()]] - code - core/identity.py
- [[identity.py]] - code - core/identity.py
- [[test_company_matches_preference_case_insensitive()]] - code - tests/test_identity.py
- [[test_company_matches_preference_none_for_empty_preferred_dict()]] - code - tests/test_identity.py
- [[test_company_matches_preference_none_for_unlisted_company()]] - code - tests/test_identity.py
- [[test_company_matches_preference_punctuation_insensitive_real_de_shaw_case()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_google_careers_results_url()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_google_pattern_is_domain_anchored()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_greenhouse()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_lever_ignores_apply_suffix()]] - code - tests/test_identity.py
- [[test_extract_ats_job_id_none_when_no_recognizable_id()]] - code - tests/test_identity.py
- [[test_identity.py]] - code - tests/test_identity.py
- [[test_josegael_uid_uses_upstream_id()]] - code - tests/test_identity.py
- [[test_missing_raw_id_raises()]] - code - tests/test_identity.py
- [[test_simplify_uid_uses_upstream_id()]] - code - tests/test_identity.py
- [[test_uids_stable_across_recomputation()]] - code - tests/test_identity.py
- [[test_uids_unique_across_distinct_listings()]] - code - tests/test_identity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Cross-Source_Identity_Keys
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_normalize_simplify]]
- 10 edges to [[_COMMUNITY_Write-Gate Validation Tests]]
- 6 edges to [[_COMMUNITY_Layer 1 Eligibility Filter]]
- 3 edges to [[_COMMUNITY_Priority-Bucket Classification]]
- 3 edges to [[_COMMUNITY_Dossier Writer (Vault Output)]]
- 2 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]
- 1 edge to [[_COMMUNITY_test_debate_losses.py]]
- 1 edge to [[_COMMUNITY_Fetch, Dedup & Identity]]

## Top bridge nodes
- [[identity.py]] - degree 13, connects to 7 communities
- [[test_identity.py]] - degree 32, connects to 4 communities
- [[company_matches_preference()]] - degree 12, connects to 2 communities
- [[test_josegael_uid_uses_upstream_id()]] - degree 4, connects to 2 communities
- [[test_missing_raw_id_raises()]] - degree 4, connects to 2 communities