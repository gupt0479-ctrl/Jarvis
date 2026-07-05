---
type: project
status: stale
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - jarvis
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "Refresh agents/*.md (missing tools:/model: fields), commands+skills/closeday.md and startday.md (still point at flat skill files instead of SKILL.md directories), and add the missing excalidraw-diagram command+skill"
---
# Jarvis — Claude Code Setup
This is a copy of this vault's own `.claude/` tooling layer — the agents, commands, skills, hooks, and rules that make Claude Code operate *this* vault. It's the most actively maintained of the four platform dumps under `20_Progress/AI`, and the reference for how the other project folders should eventually look, but the copy itself has drifted behind the live `.claude/` at the vault root.
## Files
### Agents
- [[20_Progress/AI/Claude Code/Jarvis/agents/anti-slop-editor|anti-slop-editor]]
- [[20_Progress/AI/Claude Code/Jarvis/agents/career-operator|career-operator]]
- [[20_Progress/AI/Claude Code/Jarvis/agents/learning-agent|learning-agent]]
- [[20_Progress/AI/Claude Code/Jarvis/agents/research-distiller|research-distiller]]
- [[20_Progress/AI/Claude Code/Jarvis/agents/vault-curator|vault-curator]]
### Commands
- [[20_Progress/AI/Claude Code/Jarvis/commands/closeday|closeday]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/connect-notes|connect-notes]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/context|context]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/distill-note|distill-note]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/ingest-clipping|ingest-clipping]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/lint-claude-layer|lint-claude-layer]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/ops|ops]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/organize-csci2033|organize-csci2033]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/remove-ai-slop|remove-ai-slop]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/startday|startday]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/tag-month|tag-month]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/trace-topic|trace-topic]]
- [[20_Progress/AI/Claude Code/Jarvis/commands/weekly-review|weekly-review]]
### Skills
- [[20_Progress/AI/Claude Code/Jarvis/skills/closeday|closeday]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/connect-notes|connect-notes]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/context|context]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/distill-note|distill-note]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/ingesting-clipping/SKILL|ingesting-clipping/SKILL]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/ingesting-clipping/examples|ingesting-clipping/examples]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/ingesting-clipping/reference|ingesting-clipping/reference]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/lint-claude-layer|lint-claude-layer]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/mcp-hub|mcp-hub]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/ops|ops]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/ops-reference|ops-reference]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/organize-csci2033|organize-csci2033]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/remove-ai-slop|remove-ai-slop]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/startday|startday]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/tag-month|tag-month]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/trace-topic|trace-topic]]
- [[20_Progress/AI/Claude Code/Jarvis/skills/weekly-review|weekly-review]]
### Docs
- [[20_Progress/AI/Claude Code/Jarvis/README|README]]
- [[20_Progress/AI/Claude Code/Jarvis/GITHUB_WORKFLOW|GITHUB_WORKFLOW]]
- [[20_Progress/AI/Claude Code/Jarvis/context/workspace-context|context/workspace-context]]
- [[20_Progress/AI/Claude Code/Jarvis/rules/human-writing|rules/human-writing]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/Jarvis"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings.json` — Claude Code project settings (model pin). **Stale**: pins `claude-sonnet-4-6`; live `.claude/settings.json` pins `claude-sonnet-5`.
- `settings.local.json` — local permission overrides. Current, matches live file byte-for-byte.
- `skills/ingesting-clipping/scripts/extract_pdf.py` — PDF text extraction helper used by the ingestion skill. Current, matches live file.
## Status & Gaps
Diffed directly against the live `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\` on 2026-07-05:
- **All 5 agent files are stale.** The live versions carry `tools:` and `model:` frontmatter fields and longer, more specific `description:` text; this dump still has the older, thinner frontmatter shape (no `tools:`/`model:`, shorter descriptions).
- **`commands/closeday.md` and `commands/startday.md` are stale** — both still tell the agent to read `.claude/skills/closeday.md` / `.claude/skills/startday.md` as flat files. Live `.claude/skills/closeday/` and `.claude/skills/startday/` are now directories (`SKILL.md` inside), and `startday.md` live also references an additional "Step 3b" this dump doesn't mention.
- **`skills/closeday.md` and `skills/startday.md` are stale** for the same reason — they exist here as flat files; live has them as `closeday/` and `startday/` directories.
- **Missing entirely**: `commands/excalidraw-diagram.md` and `skills/excalidraw-diagram.md` — both exist live but were never captured in this dump.
- Everything else (11 commands, 14 flat/nested skill files, `README.md`, `GITHUB_WORKFLOW.md`, `context/workspace-context.md`, `rules/human-writing.md`, `settings.local.json`, the ingestion script) is byte-identical to the live vault-root `.claude/`.
- **Note on this pass**: `commands/ingest-clipping.md`, `commands/ops.md`, and `commands/trace-topic.md` had a pre-existing `description:` value with an unquoted colon (e.g. `Usage: /ops [operation]`), which is invalid YAML and would have made this file's frontmatter — including the new `setup_status` field — unparseable by Dataview. Quoted the value to fix it; no wording changed, so these 3 files now differ from live by quoting only.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
