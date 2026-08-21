---
source_file: "tests/test_validate.py"
type: "code"
community: "render_dossier"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/render_dossier
---

# test_validate.py

## Connections
- [[_ok_response()]] - `contains` [EXTRACTED]
- [[check_format_compliance()]] - `imports` [EXTRACTED]
- [[check_not_duplicate()]] - `imports` [EXTRACTED]
- [[check_required_fields()]] - `imports` [EXTRACTED]
- [[check_url_live()]] - `imports` [EXTRACTED]
- [[listing()]] - `contains` [EXTRACTED]
- [[normalize.py]] - `imports_from` [EXTRACTED]
- [[normalize_simplify()]] - `imports` [EXTRACTED]
- [[render_dossier()]] - `imports` [EXTRACTED]
- [[test_format_compliance_allows_blank_line_after_callout()]] - `contains` [EXTRACTED]
- [[test_format_compliance_passes_on_rendered_dossier()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_blank_line_after_frontmatter()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_dashes_in_body()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_duplicate_frontmatter_key()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_missing_frontmatter_field()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_missing_notes_field()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_missing_preference_tier_field()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_stray_blank_line_in_body()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_trailing_blank_line()]] - `contains` [EXTRACTED]
- [[test_format_compliance_rejects_trailing_blank_line_after_callout()]] - `contains` [EXTRACTED]
- [[test_not_duplicate_passes_when_uid_unseen()]] - `contains` [EXTRACTED]
- [[test_not_duplicate_rejects_seen_uid()]] - `contains` [EXTRACTED]
- [[test_required_fields_pass()]] - `contains` [EXTRACTED]
- [[test_required_fields_rejects_missing_company()]] - `contains` [EXTRACTED]
- [[test_required_fields_rejects_missing_uid()]] - `contains` [EXTRACTED]
- [[test_url_live_passes_on_2xx()]] - `contains` [EXTRACTED]
- [[test_url_live_passes_on_3xx()]] - `contains` [EXTRACTED]
- [[test_url_live_rejects_404()]] - `contains` [EXTRACTED]
- [[test_url_live_rejects_on_request_exception()]] - `contains` [EXTRACTED]
- [[test_validate_happy_path()]] - `contains` [EXTRACTED]
- [[test_validate_rejects_duplicate_uid()]] - `contains` [EXTRACTED]
- [[test_validate_stops_at_first_failing_check()]] - `contains` [EXTRACTED]
- [[uid()]] - `contains` [EXTRACTED]
- [[validate()]] - `imports` [EXTRACTED]
- [[validate.py]] - `imports_from` [EXTRACTED]
- [[writer.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/render_dossier