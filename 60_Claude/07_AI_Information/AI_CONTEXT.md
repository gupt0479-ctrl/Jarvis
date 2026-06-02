# AI Context Manifest
This is the shared context manifest for Jarvis.
Its purpose is to keep Codex, Claude, Kiro, Cursor, and other AI tools aligned without copying the same instructions into multiple files.
Do not duplicate the contents of this file into tool-specific docs.
Tool-specific docs should point here.
## How To Use This File
If you are an AI tool working in this vault:
1. Read `60_Claude/07_AI_Information/Vault Map.md` first — the five-minute orientation.
2. Read `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` — the governing specification for all AI behavior. Read before writing a single character.
3. Read `AGENTS.md` for root behavioral rules and the Write Contract.
4. Read `40_Resources/Obsidian/Jarvis Vault Architecture.md` for where every note goes.
5. Read `30_Order/` (Templates + Workflows) before writing, and `HUMAN_WRITING.md` for writing quality.
6. Read this file to discover the live context sources.
7. Read the live context sources relevant to the current task.
This file is the manifest.
The files it points to are the source of truth.
## Canonical Shared Sources

These are the main cross-tool context files:

- `60_Claude/07_AI_Information/Vault Map.md` → read-me-first orientation for any agent.
- `AGENTS.md` → root behavioral rules + the Write Contract (golden rules, routing table, negative write constraints). Read before creating any file.
- `40_Resources/Obsidian/Jarvis Vault Architecture.md` → the folder-placement source of truth.
- `30_Order/` → templates and per-folder writing workflows. Mandatory pre-write reading.
- `CLAUDE.md`
- `HUMAN_WRITING.md`
- `60_Claude/07_AI_Information/AI_CONTEXT.md` (this file — full path; the wikilink `[[AI_CONTEXT]]` resolves here)
- `40_Resources/Obsidian/Vault Operating System.md`
- `40_Resources/Obsidian/Claude Pro Workflow.md`
- `00_Dashboard.md`

## Live State Sources

These are the files that tell you what is going on right now.
Prefer reading them instead of relying on stale summaries.

- `00_Dashboard.md`
  - current control panel
  - active projects
  - open tasks
  - inbox and cleanup queues

- `60_Claude/07_AI_Information/Session Logs/log.md`
  - recent AI-assisted work
  - system changes
  - previous sessions

- `60_Claude/44_Indexes/Vault Health Dashboard.md`
  - metadata drift
  - orphan notes
  - stale inbox items
  - projects missing next actions

- `60_Claude/44_Indexes/Claude Layer Index.md`
  - current Claude-layer outputs

## Domain Entry Points

Read these when the task is domain-specific.

### Vault root / note routing

- `AGENTS.md` ## Note Routing — authoritative table for where any note type should be written

### System and vault work

- `40_Resources/Obsidian/Vault Operating System.md`
- `AGENTS.md`
- `CLAUDE.md`

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
- selectively enrich only flagship notes or create durable mirror notes elsewhere

## Shared Rules

- Do not modify raw clippings under `60_Claude/05_Clippings/` unless explicitly asked.
- Prefer enriching existing notes over creating duplicates.
- Prefer backlinks and canonical notes over repeated summaries.
- Preserve frontmatter.
- Use `HUMAN_WRITING.md` to avoid AI slop.

## Continuity Protocol

To keep all tools up to date when the user returns:

1. After meaningful vault work, append a concise entry to `60_Claude/07_AI_Information/Session Logs/log.md`.
2. If the work changes focus, structure, or priorities, update the relevant dashboard or board.
3. Do not store transient status in this file.
4. Treat `00_Dashboard.md` and the session log as the live continuity layer.

## Tool-Specific Notes

- `CLAUDE.md` contains Claude-specific workflow details and commands.
- `40_Resources/Obsidian/Claude Pro Workflow.md` contains the Claude Pro usage, context-pack, MCP, Desktop, and mobile operating rules.
- `.kiro/steering/` contains Kiro loading rules and references.
- `.cursor/rules/` contains Cursor rule wrappers.
- `.claude/agents/` and `.claude/skills/` contain Claude-specific operational helpers.

Those files should reference this manifest instead of re-describing the whole workspace.
