---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - mcp
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/What MCPs]]"
next:
---
# How to Use MCPs
==Reach for an MCP server when a task needs reliable access to something outside plain repo files — a database, a live API, a browser, another vault — not for anything a direct file read already covers.==
# Claude Kit
No promoted MCP exists in claudekit yet, so there is no claudekit-specific usage guidance to give here. Once GBrain clears its embedding-provider decision and promotes, this section gets its first real entry — a personal-knowledge layer with synthesis and gap-analysis, not just retrieval, useful project-agnostically per [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map]]'s global-candidate note.
# Particular Use
## Vault Curation
`obsidian` and `filesystem` — use `obsidian` for anything that should respect Obsidian's own indexing (patch-by-heading, backlinks); use `filesystem` only when a raw file operation is needed that the Obsidian API does not expose — see [[Vault Curation]].
## Daily Operations
`git` for anything touching commit history or diffs during `/closeday`; `jarvis-memory` for a keyword search across the vault before assuming a note does not exist — see [[Daily Operations]].
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/What MCPs]] for the underlying inventory.
