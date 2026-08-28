---
source_file: "core/identity.py"
type: "code"
community: "test_write_dossier_creates_missing_dossiers_dir"
location: "L108"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_write_dossier_creates_missing_dossiers_dir
---

# company_matches_preference()

## Connections
- [[The matched preference tier (e.g. 'high'), or None if company isn't in     prefe]] - `rationale_for` [EXTRACTED]
- [[_norm_company()]] - `calls` [EXTRACTED]
- [[_preference_rank()]] - `calls` [EXTRACTED]
- [[_prioritize_and_cap()]] - `calls` [EXTRACTED]
- [[build_frontmatter()]] - `calls` [EXTRACTED]
- [[debate.py]] - `imports` [EXTRACTED]
- [[identity.py]] - `contains` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_company_matches_preference_case_insensitive()]] - `calls` [EXTRACTED]
- [[test_company_matches_preference_none_for_empty_preferred_dict()]] - `calls` [EXTRACTED]
- [[test_company_matches_preference_none_for_unlisted_company()]] - `calls` [EXTRACTED]
- [[test_company_matches_preference_punctuation_insensitive_real_de_shaw_case()]] - `calls` [EXTRACTED]
- [[test_identity.py]] - `imports` [EXTRACTED]
- [[writer.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_write_dossier_creates_missing_dossiers_dir