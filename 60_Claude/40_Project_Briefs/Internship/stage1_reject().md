---
source_file: "core/relevance.py"
type: "code"
community: "test_write_dossier_different_uid_same_role_company_gets_collision_suffix"
location: "L78"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_write_dossier_different_uid_same_role_company_gets_collision_suffix
---

# stage1_reject()

## Connections
- [[True if this listing's titleraw_text is unambiguously non-software —     reject]] - `rationale_for` [EXTRACTED]
- [[check_dossier()]] - `calls` [EXTRACTED]
- [[fetch_and_filter()]] - `calls` [EXTRACTED]
- [[relevance.py]] - `contains` [EXTRACTED]
- [[revalidate.py]] - `imports` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_relevance.py]] - `imports` [EXTRACTED]
- [[test_stage1_does_not_reject_engineering_track_rotational_program()]] - `calls` [EXTRACTED]
- [[test_stage1_does_not_reject_plain_software_titles()]] - `calls` [EXTRACTED]
- [[test_stage1_does_not_reject_product_engineer_titles()]] - `calls` [EXTRACTED]
- [[test_stage1_does_not_reject_real_risk_technology_analyst_title()]] - `calls` [EXTRACTED]
- [[test_stage1_does_not_reject_real_tax_technology_intern()]] - `calls` [EXTRACTED]
- [[test_stage1_rejects_real_academy_performance_analyst_title()]] - `calls` [EXTRACTED]
- [[test_stage1_rejects_real_conagra_demand_science_rotational_title()]] - `calls` [EXTRACTED]
- [[test_stage1_rejects_real_databricks_product_management_title()]] - `calls` [EXTRACTED]
- [[test_stage1_rejects_real_investor_relations_title()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_write_dossier_different_uid_same_role_company_gets_collision_suffix