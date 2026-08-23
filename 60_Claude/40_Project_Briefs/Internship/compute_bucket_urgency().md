---
source_file: "core/debate.py"
type: "code"
community: "test_write_dossier_creates_missing_dossiers_dir"
location: "L73"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_write_dossier_creates_missing_dossiers_dir
---

# compute_bucket_urgency()

## Connections
- [[_prioritize_and_cap()]] - `calls` [EXTRACTED]
- [[classify()]] - `calls` [EXTRACTED]
- [[debate.py]] - `contains` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_debate.py]] - `imports` [EXTRACTED]
- [[test_debate_compare_prefers_bucket_at_risk_of_going_unfilled()]] - `calls` [EXTRACTED]
- [[{bucket max(0, budgetbucket - candidate_countbucket)} for every     bucket]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_write_dossier_creates_missing_dossiers_dir