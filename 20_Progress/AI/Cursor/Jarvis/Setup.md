---
type: project
status: stale
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - jarvis
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "Re-export plans/vault_os_upgrade_08f568c7.plan.md — corrupted Templater placeholder in the dump"
---
# Jarvis — Cursor Setup
This is a copy of this vault's own `.cursor/` layer — global MCP config and the five always-on/file-scoped rules that make Cursor operate *this* vault, mirroring what `.claude/` does for Claude Code. Unlike the Claude Code Jarvis dump, this one is mostly current: the rules and MCP config are byte-identical to the live `.cursor/`.
## Files
### Docs
- [[20_Progress/AI/Cursor/Jarvis/plans/standards_layer_extraction_7dda639e|plans/standards_layer_extraction_7dda639e]] — completed plan: extracted per-heading template guidance into 30_Order/Standards/
- [[20_Progress/AI/Cursor/Jarvis/plans/vault_os_upgrade_08f568c7|plans/vault_os_upgrade_08f568c7]] — in-progress plan: four-phase plugin-docs + templates rewrite
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/Jarvis"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `mcp.json` — global Cursor MCP server config (obsidian, context7, playwright, openaiDeveloperDocs). Current, byte-identical to live `.cursor/mcp.json`.
- `rules/human-writing.mdc` — current, byte-identical to live.
- `rules/note-creation.mdc` — current, byte-identical to live.
- `rules/plugin-rules.mdc` — current, byte-identical to live.
- `rules/vault-behavior.mdc` — current, byte-identical to live.
- `rules/workspace-context.mdc` — current, byte-identical to live.
## Status & Gaps
Diffed directly against the live `D:\Users\_Anant\10_Areas\Documents\Jarvis\.cursor\` on 2026-07-05:
- **`mcp.json` and all 5 `rules/*.mdc` files are byte-identical to live** — no drift.
- **`plans/standards_layer_extraction_7dda639e.plan.md` is current** — byte-identical to live, and all its todos are marked `completed`.
- **`plans/vault_os_upgrade_08f568c7.plan.md` is stale** — in the Locked Decisions section, the live file's Templater file-title placeholder in the "Research steps" line got replaced in this dump with the literal string `vault_os_upgrade_08f568c7.plan` (looks like an export tool ran Templater and substituted its own filename token where the live tag should be). Content is otherwise identical; re-export to fix. (Caution for future edits to this Setup.md: writing the literal Templater tag syntax as prose — even inside backticks — gets auto-executed by this vault's Templater on new-file creation, as happened once while drafting this note.)
- Cursor's plan file format uses native `name:`/`overview:`/`todos:` keys (not `type:`/`tags:`) — this is tool-native shape, left untouched; only `setup_status`/`updated`/`notes` were added.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
