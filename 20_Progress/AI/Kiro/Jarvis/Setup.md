---
type: project
status: current
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - jarvis
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — fully current, nothing to reconcile"
---
# Jarvis — Kiro Setup
This is a copy of this vault's own `.kiro/` layer — two specs (Claude Code Operations Layer, PKM Capability Engine) and two always-on steering docs (human-writing, workspace-context) that mirror what `.cursor/rules` and `.claude/` do for the other tools. Unlike the Claude Code and Cursor Jarvis dumps, this one has zero drift.
## Files
### Specs (claude-code-ops-layer)
- [[20_Progress/AI/Kiro/Jarvis/specs/claude-code-ops-layer/design|specs/claude-code-ops-layer/design]] — `/ops` dispatcher architecture: jarvis-cli for deterministic scans + Obsidian MCP for semantic queries
- [[20_Progress/AI/Kiro/Jarvis/specs/claude-code-ops-layer/requirements|specs/claude-code-ops-layer/requirements]] — requirements for turning existing skills/agents into a daily operations cadence
- [[20_Progress/AI/Kiro/Jarvis/specs/claude-code-ops-layer/tasks|specs/claude-code-ops-layer/tasks]] — implementation plan: health check engine, capability audit, triage queue, report generator
### Specs (pkm-capability-engine)
- [[20_Progress/AI/Kiro/Jarvis/specs/pkm-capability-engine/design|specs/pkm-capability-engine/design]] — Capability Engine architecture for the vault
- [[20_Progress/AI/Kiro/Jarvis/specs/pkm-capability-engine/requirements|specs/pkm-capability-engine/requirements]] — capability-tracking schema, templates, per-track dashboards, evidence-first output
- [[20_Progress/AI/Kiro/Jarvis/specs/pkm-capability-engine/tasks|specs/pkm-capability-engine/tasks]] — four-phase implementation plan, Phase 0 (schema hardening) already complete
### Steering
- [[20_Progress/AI/Kiro/Jarvis/steering/human-writing|steering/human-writing]] — always-on: read HUMAN_WRITING.md before drafting/rewriting
- [[20_Progress/AI/Kiro/Jarvis/steering/workspace-context|steering/workspace-context]] — always-on workspace context steering
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/Jarvis"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings/mcp.json` — Kiro MCP server config. Current, byte-identical to live `.kiro/settings/mcp.json`.
## Status & Gaps
Diffed directly against the live `D:\Users\_Anant\10_Areas\Documents\Jarvis\.kiro\` on 2026-07-05: **every file is byte-identical to live** — all 6 spec files, both steering docs, and `settings/mcp.json`. No drift found. Both steering docs use Kiro's native `inclusion: always` frontmatter key (tool-native, left untouched); the 6 spec files had no frontmatter at all and got a fresh minimal block.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
