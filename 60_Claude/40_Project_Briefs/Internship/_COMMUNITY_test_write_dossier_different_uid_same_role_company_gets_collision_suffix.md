---
type: community
members: 32
---

# test_write_dossier_different_uid_same_role_company_gets_collision_suffix

**Members:** 32 nodes

## Members
- [[A genuinely technical Vertiv posting must still pass even though the     company]] - rationale - tests/test_relevance.py
- [[A hardware-adjacent titlecompany with content that never mentions     any real]] - rationale - tests/test_relevance.py
- [[Called only when posting_content is non-empty. True = passes (either     not adj]] - rationale - core/relevance.py
- [[Hardware is not auto-excluded — Jane Street's FPGAASIC internship is     a real]] - rationale - tests/test_relevance.py
- [[No adjacent-field hint at all — already cleared stage 1, content     (even empty]] - rationale - tests/test_relevance.py
- [[Not company-gated (see module note above) and no signal-word match     in its ow]] - rationale - tests/test_relevance.py
- [[Real, documented limitation adding 'truist' to the hint list doesn't     flip t]] - rationale - tests/test_relevance.py
- [[Same documented limitation as Truist above KeyBank's real content     (from 'Da]] - rationale - tests/test_relevance.py
- [[corerelevance.py's two-stage gate — real examples throughout, no synthetic non-]] - rationale - tests/test_relevance.py
- [[stage2_confirm()]] - code - core/relevance.py
- [[test_relevance.py]] - code - tests/test_relevance.py
- [[test_stage2_confirms_appian_infosec_from_real_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_bosch_ml_internship_from_real_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_jane_street_cybersecurity_from_real_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_jane_street_hardware_role_from_real_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_magna_computer_vision_from_real_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_real_continental_resources_data_analyst_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_real_dimensional_fund_operations_insights_content()]] - code - tests/test_relevance.py
- [[test_stage2_confirms_real_vertiv_operations_intern_content()]] - code - tests/test_relevance.py
- [[test_stage2_passes_through_non_adjacent_titles_without_content_check()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_adjacent_field_with_no_software_signal()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_cno_financial_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_continental_resources_geoscience_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_dimensional_fund_data_and_tools_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_fti_consulting_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_mosaic_chemical_engineering_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_uhy_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_vertiv_planning_analytics_content()]] - code - tests/test_relevance.py
- [[test_stage2_rejects_real_walleye_finance_and_accounting_content()]] - code - tests/test_relevance.py
- [[test_stage2_still_confirms_real_truist_content_on_coincidental_team_name_mention()]] - code - tests/test_relevance.py
- [[test_stage2_still_confirms_real_walleye_investment_data_science_content()]] - code - tests/test_relevance.py
- [[test_stage2_still_rejects_real_keybank_content_on_coincidental_tool_list_mention()]] - code - tests/test_relevance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_write_dossier_different_uid_same_role_company_gets_collision_suffix
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_matches]]
- 2 edges to [[_COMMUNITY_relevance.py]]
- 2 edges to [[_COMMUNITY_revalidate.py]]
- 1 edge to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY_writer.py]]
- 1 edge to [[_COMMUNITY_test_filter.py]]
- 1 edge to [[_COMMUNITY_test_writer.py]]

## Top bridge nodes
- [[test_relevance.py]] - degree 37, connects to 4 communities
- [[stage2_confirm()]] - degree 28, connects to 4 communities