---
source_file: "revalidate.py"
type: "code"
community: "commit_and_push_with_retry"
location: "L64"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/commit_and_push_with_retry
---

# find_regressions()

## Connections
- [[Path]] - `calls` [INFERRED]
- [[{path, company, title, reason} for every live dossier that would     now fail]] - `rationale_for` [EXTRACTED]
- [[check_dossier()]] - `calls` [EXTRACTED]
- [[extract_posting_content()]] - `calls` [EXTRACTED]
- [[main()_3]] - `calls` [EXTRACTED]
- [[revalidate.py]] - `contains` [EXTRACTED]
- [[scan_dossiers()]] - `calls` [EXTRACTED]
- [[test_find_regressions_scans_real_vault_layout()]] - `calls` [EXTRACTED]
- [[test_revalidate.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/commit_and_push_with_retry