---
source_file: "ingestion/freehire.py"
type: "rationale"
community: "write_dossier"
location: "L104"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/write_dossier
---

# Checks freehire's own company mapping before ever guessing a token     ourselves

## Connections
- [[lookup_company_on_freehire()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/write_dossier