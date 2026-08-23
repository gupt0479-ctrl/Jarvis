---
source_file: "tests/test_debate_losses.py"
type: "code"
community: "test_writer.py"
location: "L102"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_writerpy
---

# test_run_once_never_fetches_an_already_excluded_uid()

## Connections
- [[Pre-seed stateexcluded_uids.json with a real candidate's uid already     at the]] - `rationale_for` [EXTRACTED]
- [[_run_once_kwargs()]] - `calls` [INFERRED]
- [[_simplify_raw()]] - `calls` [INFERRED]
- [[compute_uid()]] - `calls` [EXTRACTED]
- [[normalize_simplify()]] - `calls` [EXTRACTED]
- [[test_debate_losses.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_writerpy