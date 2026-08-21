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
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/How to Use Global]]"
next:
---
# Vault Curation
==Keeping the vault's links, frontmatter, and structure honest — broken links, orphan notes, duplicates, stale frontmatter — without silently rewriting anything.==
Use the `vault-curator` agent ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents#Vault Curation|Agents]]) for a full sweep after a large ingestion session; it reports first and applies fixes only incrementally with explicit approval, never deletes without permission, and never reads `50_Archive/`. Use `/lint-claude-layer` ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills#Vault Curation|Skills]]) for a narrower, faster check scoped to `60_Claude/` specifically. Use `/connect-notes` when the goal is additive — surfacing missing wikilinks — rather than corrective. The `obsidian` MCP server ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs#Vault Curation|MCPs]]) is what any of these actually calls to patch a note by heading rather than overwriting the whole file.
**The WSL home directory also carries two global agents in this same territory** ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global|What Global]]): `obsidian-architect` (structure/MOC/frontmatter audits) and `obsidian-researcher` (open-ended vault search). Both predate and duplicate ground Jarvis's own `vault-curator`/`research-distiller` agents already cover, and both carry the same stale-path problem flagged in `What Global` — prefer the Jarvis-native pair for this vault specifically; the global pair is there for a WSL project that has no vault-specific agents of its own.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global]]
