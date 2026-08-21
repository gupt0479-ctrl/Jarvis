---
source_file: "core/relevance.py"
type: "code"
community: "test_write_dossier_different_uid_same_role_company_gets_collision_suffix"
location: "L123"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_write_dossier_different_uid_same_role_company_gets_collision_suffix
---

# stage2_confirm()

## Connections
- [[Called only when posting_content is non-empty. True = passes (either     not adj]] - `rationale_for` [EXTRACTED]
- [[relevance.py]] - `contains` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_relevance.py]] - `imports` [EXTRACTED]
- [[test_stage2_confirms_bosch_ml_internship_from_real_content()]] - `calls` [EXTRACTED]
- [[test_stage2_confirms_jane_street_hardware_role_from_real_content()]] - `calls` [EXTRACTED]
- [[test_stage2_confirms_magna_computer_vision_from_real_content()]] - `calls` [EXTRACTED]
- [[test_stage2_passes_through_non_adjacent_titles_without_content_check()]] - `calls` [EXTRACTED]
- [[test_stage2_rejects_adjacent_field_with_no_software_signal()]] - `calls` [EXTRACTED]
- [[test_stage2_rejects_real_mosaic_chemical_engineering_content()]] - `calls` [EXTRACTED]
- [[validate_and_write()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_write_dossier_different_uid_same_role_company_gets_collision_suffix