---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - use-case
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs]]"
next:
---
# Vault Curation
==Keeping the vault's links, frontmatter, and structure honest — broken links, orphan notes, duplicates, stale frontmatter — without silently rewriting anything.==
Use the `vault-curator` agent ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents#Vault Curation|Agents]]) for a full sweep after a large ingestion session; it reports first and applies fixes only incrementally with explicit approval, never deletes without permission, and never reads `50_Archive/`. Use `/lint-claude-layer` ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills#Vault Curation|Skills]]) for a narrower, faster check scoped to `60_Claude/` specifically. Use `/connect-notes` when the goal is additive — surfacing missing wikilinks — rather than corrective. The `obsidian` MCP server ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs#Vault Curation|MCPs]]) is what any of these actually calls to patch a note by heading rather than overwriting the whole file.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]]
