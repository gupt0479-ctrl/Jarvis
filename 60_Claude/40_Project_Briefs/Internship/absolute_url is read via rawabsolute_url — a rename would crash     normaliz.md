---
source_file: "tests/test_schema_drift.py"
type: "rationale"
community: "check_greenhouse_schema"
location: "L345"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/check_greenhouse_schema
---

# absolute_url is read via raw["absolute_url"] — a rename would crash     normaliz

## Connections
- [[test_greenhouse_schema_detects_renamed_absolute_url()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/check_greenhouse_schema