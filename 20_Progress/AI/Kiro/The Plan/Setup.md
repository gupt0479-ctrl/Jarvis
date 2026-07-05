---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - the-plan
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external vault dump, not synced to this vault"
---
# The Plan — Kiro Setup
A copy of the Kiro workspace for "The Plan," a separate Obsidian vault the user also operates (see the `the-plan`/`the-plan-fs` MCP servers referenced in [[20_Progress/AI/Cursor/CausalOps/Setup|CausalOps' Cursor README]]). Its two specs share names with [[20_Progress/AI/Kiro/Jarvis/Setup|Jarvis's own Kiro specs]] (`claude-code-ops-layer`, `pkm-capability-engine`) but are not byte-identical — The Plan's `requirements.md` copies are shorter, missing the Jarvis-specific "Requirement 12: Jarvis Ops CLI Integration" section, since that requirement only makes sense in this vault. Reference material, not part of this vault's own tooling.
## Files
### Specs (claude-code-ops-layer)
- [[20_Progress/AI/Kiro/The Plan/specs/claude-code-ops-layer/design|specs/claude-code-ops-layer/design]]
- [[20_Progress/AI/Kiro/The Plan/specs/claude-code-ops-layer/requirements|specs/claude-code-ops-layer/requirements]] — shorter than Jarvis's copy, no vault-specific CLI requirement
- [[20_Progress/AI/Kiro/The Plan/specs/claude-code-ops-layer/tasks|specs/claude-code-ops-layer/tasks]]
### Specs (pkm-capability-engine)
- [[20_Progress/AI/Kiro/The Plan/specs/pkm-capability-engine/design|specs/pkm-capability-engine/design]]
- [[20_Progress/AI/Kiro/The Plan/specs/pkm-capability-engine/requirements|specs/pkm-capability-engine/requirements]]
- [[20_Progress/AI/Kiro/The Plan/specs/pkm-capability-engine/tasks|specs/pkm-capability-engine/tasks]]
### Steering
- [[20_Progress/AI/Kiro/The Plan/steering/human-writing|steering/human-writing]] — always-on writing standard steering
- [[20_Progress/AI/Kiro/The Plan/steering/workspace-context|steering/workspace-context]] — always-on workspace context steering
- [[20_Progress/AI/Kiro/The Plan/steering/styling|steering/styling]] — always-on styling steering (no equivalent in the Jarvis Kiro dump)
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/The Plan"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings/mcp.json` — Kiro MCP server config for The Plan vault.
- `specs/claude-code-ops-layer/.config.kiro`, `specs/pkm-capability-engine/.config.kiro` — Kiro spec metadata.
## Status & Gaps
External vault dump, no live equivalent inside *this* vault to diff against — marked `static`. The interesting comparison isn't against a live source but against [[20_Progress/AI/Kiro/Jarvis/Setup|Jarvis's own Kiro dump]]: the two vaults share spec designs (same authoring pass, adapted per-vault), so divergence here is expected rather than drift. `steering/styling.md` has no counterpart in Jarvis's Kiro dump — The Plan apparently needed a dedicated styling steering doc that Jarvis doesn't.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
