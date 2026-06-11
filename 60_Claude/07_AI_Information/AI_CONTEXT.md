---
type: evergreen
status: sprout
created: 2026-05-31
updated: 2026-06-11
tags:
  - system
  - ai-agents
---
# AI Context Manifest

Shared context manifest for Jarvis. Keeps Claude, Cursor, Kiro, Codex, and other tools aligned without copying instructions into multiple files.

**Cold-start read order:** [[Jarvis OS — North Star]] → [[AGENTS.md]] → [[40_Resources/Obsidian/Jarvis Vault Architecture]] → [[HUMAN_WRITING]] → this file → live state below.

Do not duplicate the contents of this file into tool-specific docs. Tool-specific docs point here.

## Live State Sources

These tell you what is happening right now. Read them instead of relying on stale summaries.

- `00_Dashboard.md` — current control panel; active projects, open tasks, inbox and cleanup queues
- `60_Claude/07_AI_Information/Session Logs/log.md` — recent AI-assisted work, system changes, previous sessions
- `60_Claude/44_Indexes/Vault Health Dashboard.md` — metadata drift, orphan notes, stale inbox items, projects missing next actions
- `60_Claude/44_Indexes/Claude Layer Index.md` — current Claude-layer outputs

## Domain Entry Points

Read these when the task is domain-specific.

### Vault root / note routing

- `AGENTS.md` → authoritative routing table for where any note type should be written

### System and vault work

- `40_Resources/Obsidian/Vault Operating System.md` — canonical property/field schema
- `AGENTS.md`, `CLAUDE.md`

### UROP / systems / backend

- `20_Progress/UROP/BOOM Board.md`
- `20_Progress/UROP/index.md`

### Active projects and career work

- `20_Progress/Projects/Projects Board.md`
- relevant notes under `20_Progress/Career/`
- relevant notes under `20_Progress/Mentorship Program/`

### AI / agents / workflows

- `40_Resources/Obsidian/Claude Pro Workflow.md`
- notes under `40_Resources/CS/AI/`
- relevant `60_Claude/10_Source_Summaries/` and `20_Distilled_Notes/`

### Coursework as feeder layer

- relevant notes under `10_Areas/UMN/`
- enrich only flagship notes or create durable mirror notes elsewhere

## Shared Rules

- Do not modify raw clippings under `60_Claude/05_Clippings/` unless explicitly asked.
- Prefer enriching existing notes over creating duplicates.
- Prefer backlinks and canonical notes over repeated summaries.
- Preserve frontmatter.
- Use `HUMAN_WRITING.md` to avoid AI slop.

## Continuity Protocol

1. After meaningful vault work, append a concise entry to `60_Claude/07_AI_Information/Session Logs/log.md`.
2. If work changes focus, structure, or priorities, update the relevant dashboard or board.
3. Do not store transient status in this file.
4. Treat `00_Dashboard.md` and the session log as the live continuity layer.

## Tool-Specific Notes

- `CLAUDE.md` — Claude-specific workflow details, skills, and agents.
- `40_Resources/Obsidian/Claude Pro Workflow.md` — Claude Pro usage, context-pack, MCP, Desktop, and mobile rules.
- `.kiro/steering/` — Kiro loading rules.
- `.cursor/rules/` — Cursor rule wrappers.
- `.claude/agents/` and `.claude/skills/` — Claude-specific operational helpers.
