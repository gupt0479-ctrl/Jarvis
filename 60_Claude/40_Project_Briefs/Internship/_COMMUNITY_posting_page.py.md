---
type: community
members: 75
---

# posting_page.py

**Members:** 75 nodes

## Members
- [[.increase_indent()]] - code - vault_writer/writer.py
- [[Copy of the committed throwaway_vault skeleton in a scratch dir per test,     so]] - rationale - tests/test_writer.py
- [[Dumps None as a blank scalar (matching the plan's `field` empty style     inste]] - rationale - vault_writer/writer.py
- [[Layer 4 — the five-check write gate. Fail any check - item is rejected and neve]] - rationale - vault_writer/validate.py
- [[Like SafeLoader, but raises on duplicate mapping keys instead of     silently ke]] - rationale - vault_writer/validate.py
- [[Renders the fixed dossier template and writes it into a vault checkout.  Renderi]] - rationale - vault_writer/writer.py
- [[Runs all checks in the plan's order, fail-closed on the first failure.     Short]] - rationale - vault_writer/validate.py
- [[Same program via two sources = two different uids but one normalized     company]] - rationale - vault_writer/validate.py
- [[Same role+company but a genuinely different uid must not overwrite —     only a]] - rationale - tests/test_writer.py
- [[The mid-body loop explicitly allows a blank line after a callout — but not     w]] - rationale - tests/test_validate.py
- [[ValidationResult]] - code - vault_writer/validate.py
- [[Writes an already-rendered, already-validated dossier into its     priority-buck]] - rationale - vault_writer/writer.py
- [[Role - Company.md', Windows-unsafe chars stripped (the vault lives     on a]] - rationale - vault_writer/writer.py
- [[_DupeKeyLoader]] - code - vault_writer/validate.py
- [[_FrontmatterDumper]] - code - vault_writer/writer.py
- [[_construct_mapping_no_dupes()]] - code - vault_writer/validate.py
- [[_iso_date()]] - code - vault_writer/writer.py
- [[_ok_response()]] - code - tests/test_validate.py
- [[_represent_none()]] - code - vault_writer/writer.py
- [[_yaml_list()]] - code - vault_writer/writer.py
- [[build_frontmatter()]] - code - vault_writer/writer.py
- [[check_cross_source_duplicate()]] - code - vault_writer/validate.py
- [[check_format_compliance()]] - code - vault_writer/validate.py
- [[check_not_duplicate()]] - code - vault_writer/validate.py
- [[check_required_fields()]] - code - vault_writer/validate.py
- [[check_url_live()]] - code - vault_writer/validate.py
- [[dossier_filename()]] - code - vault_writer/writer.py
- [[listing()]] - code - tests/test_validate.py
- [[listing()_1]] - code - tests/test_writer.py
- [[load_dossier_uids()]] - code - vault_writer/writer.py
- [[render_dossier()]] - code - vault_writer/writer.py
- [[required_fields runs before url_liveness — a missing field should reject     wit]] - rationale - tests/test_validate.py
- [[save_dossier_uids()]] - code - vault_writer/writer.py
- [[state_dir()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_appends_number()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_increments_past_multiple()]] - code - tests/test_writer.py
- [[test_dossier_filename_sanitizes_illegal_chars()]] - code - tests/test_writer.py
- [[test_format_compliance_allows_blank_line_after_callout()]] - code - tests/test_validate.py
- [[test_format_compliance_passes_on_rendered_dossier()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_blank_line_after_frontmatter()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_dashes_in_body()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_duplicate_frontmatter_key()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_frontmatter_field()]] - code - tests/test_validate.py
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
- [[test_write_dossier_creates_missing_dossiers_dir()]] - code - tests/test_writer.py
- [[test_write_dossier_different_uid_same_role_company_gets_collision_suffix()]] - code - tests/test_writer.py
- [[test_write_dossier_is_idempotent_on_uid()]] - code - tests/test_writer.py
- [[test_write_dossier_records_uid_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_routes_into_bucket_subfolder()]] - code - tests/test_writer.py
- [[test_write_dossier_without_state_dir_records_no_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_writes_expected_file()]] - code - tests/test_writer.py
- [[test_writer.py]] - code - tests/test_writer.py
- [[uid and category are deliberately not rendered — uid stays available     interna]] - rationale - vault_writer/writer.py
- [[uid()]] - code - tests/test_validate.py
- [[validate()]] - code - vault_writer/validate.py
- [[validate.py]] - code - vault_writer/validate.py
- [[vault_root with no pre-existing Dossiers folder at all still works.]] - rationale - tests/test_writer.py
- [[vault_root()]] - code - tests/test_writer.py
- [[write_dossier()]] - code - vault_writer/writer.py
- [[writer.py]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/posting_pagepy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_extract_content]]
- 7 edges to [[_COMMUNITY_phd_only_exclusion]]
- 2 edges to [[_COMMUNITY__content_fetch_url]]

## Top bridge nodes
- [[test_validate.py]] - degree 34, connects to 2 communities
- [[test_writer.py]] - degree 20, connects to 2 communities
- [[validate.py]] - degree 14, connects to 2 communities
- [[render_dossier()]] - degree 26, connects to 1 community
- [[check_format_compliance()]] - degree 16, connects to 1 community