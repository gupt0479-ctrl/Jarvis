---
source_file: "ingestion/freehire.py"
type: "code"
community: "write_dossier"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/write_dossier
---

# lookup_company_on_freehire()

## Connections
- [[Checks freehire's own company mapping before ever guessing a token     ourselves]] - `rationale_for` [EXTRACTED]
- [[freehire.py]] - `contains` [EXTRACTED]
- [[test_freehire.py]] - `imports` [EXTRACTED]
- [[test_lookup_company_on_freehire_found()]] - `calls` [EXTRACTED]
- [[test_lookup_company_on_freehire_not_found_returns_empty_dict()]] - `calls` [EXTRACTED]
- [[test_lookup_company_on_freehire_slugifies_the_company_name()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/write_dossier