---
source_file: "vault_writer/validate.py"
type: "code"
community: "_fake_http_get_only_interndock"
location: "L123"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_fake_http_get_only_interndock
---

# validate()

## Connections
- [[Runs all checks in the plan's order, fail-closed on the first failure.     Short]] - `rationale_for` [EXTRACTED]
- [[ValidationResult]] - `references` [EXTRACTED]
- [[check_cross_source_duplicate()]] - `calls` [EXTRACTED]
- [[check_format_compliance()]] - `calls` [EXTRACTED]
- [[check_not_duplicate()]] - `calls` [EXTRACTED]
- [[check_required_fields()]] - `calls` [EXTRACTED]
- [[check_url_live()]] - `calls` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_validate.py]] - `imports` [EXTRACTED]
- [[test_validate_happy_path()]] - `calls` [EXTRACTED]
- [[test_validate_rejects_duplicate_uid()]] - `calls` [EXTRACTED]
- [[test_validate_stops_at_first_failing_check()]] - `calls` [EXTRACTED]
- [[validate.py]] - `contains` [EXTRACTED]
- [[validate_and_write()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_fake_http_get_only_interndock