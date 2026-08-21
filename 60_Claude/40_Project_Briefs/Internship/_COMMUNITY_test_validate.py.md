---
type: community
members: 48
---

# test_validate.py

**Members:** 48 nodes

## Members
- [[Confirms REQUIRED_FRONTMATTER_FIELDS actually enforces notes — adding     it to]] - rationale - tests/test_validate.py
- [[Layer 4 — the five-check write gate. Fail any check - item is rejected and neve]] - rationale - vault_writer/validate.py
- [[Like SafeLoader, but raises on duplicate mapping keys instead of     silently ke]] - rationale - vault_writer/validate.py
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
- [[listing()]] - code - tests/test_validate.py
- [[render_dossier()]] - code - vault_writer/writer.py
- [[required_fields runs before url_liveness — a missing field should reject     wit]] - rationale - tests/test_validate.py
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
TABLE source_file, type FROM #community/test_validatepy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_writer.py]]
- 8 edges to [[_COMMUNITY_run_pipeline.py]]
- 4 edges to [[_COMMUNITY_test_identity.py]]
- 3 edges to [[_COMMUNITY_test_posting_page.py]]
- 2 edges to [[_COMMUNITY_test_debate.py]]
- 2 edges to [[_COMMUNITY_test_run_pipeline.py]]
- 1 edge to [[_COMMUNITY_test_relevance.py]]
- 1 edge to [[_COMMUNITY_test_filter.py]]

## Top bridge nodes
- [[validate_and_write()]] - degree 16, connects to 6 communities
- [[test_validate.py]] - degree 36, connects to 3 communities
- [[render_dossier()]] - degree 32, connects to 2 communities
- [[validate.py]] - degree 14, connects to 2 communities
- [[check_format_compliance()]] - degree 18, connects to 1 community