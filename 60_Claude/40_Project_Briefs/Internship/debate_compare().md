---
source_file: "core/debate.py"
type: "code"
community: "test_write_dossier_creates_missing_dossiers_dir"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_write_dossier_creates_missing_dossiers_dir
---

# debate_compare()

## Connections
- [[Standard cmp semantics negative if a should rank first, positive if     b shoul]] - `rationale_for` [EXTRACTED]
- [[_preference_rank()]] - `calls` [EXTRACTED]
- [[_prioritize_and_cap()]] - `calls` [EXTRACTED]
- [[classify()]] - `calls` [EXTRACTED]
- [[debate.py]] - `contains` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_debate.py]] - `imports` [EXTRACTED]
- [[test_debate_compare_missing_date_posted_sorts_last()]] - `calls` [EXTRACTED]
- [[test_debate_compare_prefers_bucket_at_risk_of_going_unfilled()]] - `calls` [EXTRACTED]
- [[test_debate_compare_prefers_preferred_company_with_identical_dates()]] - `calls` [EXTRACTED]
- [[test_debate_compare_recency_is_final_tiebreak()]] - `calls` [EXTRACTED]
- [[test_debate_compare_skips_bucket_fill_need_for_same_bucket_pair()]] - `calls` [EXTRACTED]
- [[test_debate_compare_ties_between_two_preferred_companies_falls_through()]] - `calls` [EXTRACTED]
- [[test_debate_compare_without_bucket_urgency_skips_stage_2()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_write_dossier_creates_missing_dossiers_dir