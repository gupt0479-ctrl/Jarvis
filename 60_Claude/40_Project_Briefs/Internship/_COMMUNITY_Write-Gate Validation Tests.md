---
type: community
members: 62
---

# Write-Gate Validation Tests

**Members:** 62 nodes

## Members
- [[A sourceATS with no recognizable job id in its URL shape (e.g.     Freehire's T]] - rationale - tests/test_identity.py
- [[Confirms REQUIRED_FRONTMATTER_FIELDS actually enforces notes — adding     it to]] - rationale - tests/test_validate.py
- [[Layer 4 — the five-check write gate. Fail any check - item is rejected and neve]] - rationale - vault_writer/validate.py
- [[Like SafeLoader, but raises on duplicate mapping keys instead of     silently ke]] - rationale - vault_writer/validate.py
- [[Real Aquatic vs Aquatic Capital Management same Greenhouse posting,     same UR]] - rationale - tests/test_identity.py
- [[Real Google BS vs MS title-string variant, same numeric job id.]] - rationale - tests/test_identity.py
- [[Real Palantir 'Intel' FDSE duplicate across two different buckets     (SimplifyJ]] - rationale - tests/test_identity.py
- [[Real dup from the 2026-07-18 audit same Workday req via two routes,     titled]] - rationale - tests/test_run_pipeline.py
- [[Real, confirmed 2026-07-29 — a genuine TRIPLE duplicate three     different tit]] - rationale - tests/test_identity.py
- [[Renders + validates each new listing; writes the ones that pass into     the Jar]] - rationale - run_pipeline.py
- [[Runs all checks in the plan's order, fail-closed on the first failure.     Short]] - rationale - vault_writer/validate.py
- [[Same program via two sources = two different uids but one normalized     company]] - rationale - vault_writer/validate.py
- [[The mid-body loop explicitly allows a blank line after a callout — but not     w]] - rationale - tests/test_validate.py
- [[ValidationResult]] - code - vault_writer/validate.py
- [[_DupeKeyLoader]] - code - vault_writer/validate.py
- [[_construct_mapping_no_dupes()]] - code - vault_writer/validate.py
- [[_ok_response()]] - code - tests/test_validate.py
- [[build_matched_reason()]] - code - run_pipeline.py
- [[check_cross_source_duplicate()]] - code - vault_writer/validate.py
- [[check_format_compliance()]] - code - vault_writer/validate.py
- [[check_not_duplicate()]] - code - vault_writer/validate.py
- [[check_required_fields()]] - code - vault_writer/validate.py
- [[check_url_live()]] - code - vault_writer/validate.py
- [[cross_source_key()]] - code - core/identity.py
- [[listing()]] - code - tests/test_validate.py
- [[render_dossier()]] - code - vault_writer/writer.py
- [[required_fields runs before url_liveness — a missing field should reject     wit]] - rationale - tests/test_validate.py
- [[test_cross_source_key_falls_back_to_normalized_text_when_no_job_id()]] - code - tests/test_identity.py
- [[test_cross_source_key_falls_back_to_text_for_company_name_variant_real_aquatic_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_normalizes_case_and_whitespace()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_google_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_palantir_cross_bucket_case()]] - code - tests/test_identity.py
- [[test_cross_source_key_prefers_job_id_over_text_real_virtu_triple()]] - code - tests/test_identity.py
- [[test_cross_source_key_punctuation_insensitive_marmon_case()]] - code - tests/test_run_pipeline.py
- [[test_format_compliance_allows_blank_line_after_callout()]] - code - tests/test_validate.py
- [[test_format_compliance_passes_on_rendered_dossier()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_blank_line_after_frontmatter()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_dashes_in_body()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_duplicate_frontmatter_key()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_frontmatter_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_notes_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_preference_tier_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_stray_blank_line_in_body()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_trailing_blank_line()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_trailing_blank_line_after_callout()]] - code - tests/test_validate.py
- [[test_not_duplicate_passes_when_uid_unseen()]] - code - tests/test_validate.py
- [[test_not_duplicate_rejects_seen_uid()]] - code - tests/test_validate.py
- [[test_required_fields_pass()]] - code - tests/test_validate.py
- [[test_required_fields_rejects_missing_company()]] - code - tests/test_validate.py
- [[test_required_fields_rejects_missing_uid()]] - code - tests/test_validate.py
- [[test_url_live_passes_on_2xx()]] - code - tests/test_validate.py
- [[test_url_live_passes_on_3xx()]] - code - tests/test_validate.py
- [[test_url_live_rejects_404()]] - code - tests/test_validate.py
- [[test_url_live_rejects_on_request_exception()]] - code - tests/test_validate.py
- [[test_validate.py]] - code - tests/test_validate.py
- [[test_validate_happy_path()]] - code - tests/test_validate.py
- [[test_validate_rejects_duplicate_uid()]] - code - tests/test_validate.py
- [[test_validate_stops_at_first_failing_check()]] - code - tests/test_validate.py
- [[uid()]] - code - tests/test_validate.py
- [[validate()]] - code - vault_writer/validate.py
- [[validate.py]] - code - vault_writer/validate.py
- [[validate_and_write()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Write-Gate_Validation_Tests
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Dossier Writer (Vault Output)]]
- 10 edges to [[_COMMUNITY_Cross-Source Identity Keys]]
- 9 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]
- 3 edges to [[_COMMUNITY_Posting Page Fetch & OPTPhD Screen]]
- 2 edges to [[_COMMUNITY_Priority-Bucket Classification]]
- 2 edges to [[_COMMUNITY_Fetch, Dedup & Identity]]
- 2 edges to [[_COMMUNITY_normalize_simplify]]
- 1 edge to [[_COMMUNITY_CSSoftware Relevance Gate]]
- 1 edge to [[_COMMUNITY_Layer 1 Eligibility Filter]]

## Top bridge nodes
- [[validate_and_write()]] - degree 16, connects to 5 communities
- [[test_validate.py]] - degree 36, connects to 3 communities
- [[cross_source_key()]] - degree 15, connects to 3 communities
- [[render_dossier()]] - degree 32, connects to 2 communities
- [[validate.py]] - degree 14, connects to 2 communities