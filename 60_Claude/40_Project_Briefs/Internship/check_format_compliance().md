---
source_file: "vault_writer/validate.py"
type: "code"
community: "render_dossier"
location: "L81"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/render_dossier
---

# check_format_compliance()

## Connections
- [[ValidationResult]] - `references` [EXTRACTED]
- [[_DupeKeyLoader]] - `indirect_call` [INFERRED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_format_compliance_allows_blank_line_after_callout()]] - `calls` [EXTRACTED]
- [[test_format_compliance_passes_on_rendered_dossier()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_blank_line_after_frontmatter()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_dashes_in_body()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_duplicate_frontmatter_key()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_missing_frontmatter_field()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_missing_notes_field()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_missing_preference_tier_field()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_stray_blank_line_in_body()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_trailing_blank_line()]] - `calls` [EXTRACTED]
- [[test_format_compliance_rejects_trailing_blank_line_after_callout()]] - `calls` [EXTRACTED]
- [[test_validate.py]] - `imports` [EXTRACTED]
- [[validate()]] - `calls` [EXTRACTED]
- [[validate.py]] - `contains` [EXTRACTED]
- [[validate_and_write()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/render_dossier