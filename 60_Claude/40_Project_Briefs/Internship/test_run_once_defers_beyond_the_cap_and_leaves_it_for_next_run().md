---
source_file: "tests/test_run_pipeline.py"
type: "code"
community: "test_writer.py"
location: "L268"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_writerpy
---

# test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()

## Connections
- [[The core guarantee a deferred item is not marked seen, so it's neither     lost]] - `rationale_for` [EXTRACTED]
- [[_fake_http_get()]] - `indirect_call` [INFERRED]
- [[_run_once_kwargs()]] - `calls` [EXTRACTED]
- [[test_run_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_writerpy