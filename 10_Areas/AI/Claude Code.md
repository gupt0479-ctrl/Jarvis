---
type: evergreen
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - ai
  - tool-guide
  - claude-code
notes:
  - "[[Claude OS]]"
  - "[[Jarvis OS — North Star]]"
next: "Wire the scheduled daily loop (morning context assembly + evening close) so Jarvis moves without being driven by hand"
---
# Claude Code
Claude Code is the primary implementation surface. Everything that changes files — vault notes, project code, system config — runs through it. Cursor is for surgical in-editor edits with live LSP feedback; Kiro is for spec-gated product builds; Codex is a second opinion with repo-local skills. Claude Code is where the agentic work happens: multi-file changes, skills, subagents, hooks, MCP.
It runs in two homes on this machine. The Windows home (`C:\Users\Anant Gupta\.claude\`) drives the Jarvis vault. The WSL home drives code projects (CausalOps, Portfolio) and carries the plugin marketplaces. Snapshots of both live in `20_Progress/AI/Claude Code/` — that dump is the source material for this note and for [[Claude OS]].
## What each project uses it for
| Project | Role of Claude Code | Where the setup lives |
| --- | --- | --- |
| Jarvis (this vault) | PKM/vault OS: skills, agents, hooks, MCP — the whole daily loop | `.claude/` in the vault; snapshot at `20_Progress/AI/Claude Code/Jarvis/` |
| CausalOps (HiveMind) | Multi-agent CI: 3 specialist subagents, 4 test commands, 3 guard hooks | `20_Progress/AI/Claude Code/CausalOps/` |
| Portfolio | Web dev in WSL (Next.js + Sanity); deploy gates migrated to Codex skills too | WSL home projects; `20_Progress/AI/Claude Code/Portfolio/` is currently an empty dump — re-export needed |
| Resq / OpsPilot | `.claude/` as the canon layer: PRD, context, playbooks, checklists that Kiro agents also read | `20_Progress/AI/Claude Code/Resq/`, `.../OpsPilot/` |
| TradingView | Research + strategy engine work (see 2026-06-25 session log) | dump folder empty — setup lives in the project repo |
The Resq pattern is worth copying: its `.claude/` holds the project canon (PRD, current-state, architecture, playbooks) and the Kiro agent (`resq.json`) mounts those same files as `file://` resources. One context layer, two tools reading it — no duplication.
## Jarvis setup
### Skills (14 commands via `.claude/commands/`)
| Command | What it does |
| --- | --- |
| `/startday` | Fills today's daily note from the Summer OS plans + session history, patches the dashboard focus fields (directory skill: `startday/SKILL.md` + `reference.md`) |
| `/closeday` | Auto-gathers the day, asks one 5-question block, writes `lc_count`/`study_today`/`wins_done`/`habits_done` to the daily note, resets the dashboard (directory skill) |
| `/ingest-clipping` | Routes any source (PDF/image/web/repo) into `60_Claude/10_Source_Summaries/` (directory skill with `scripts/extract_pdf.py`) |
| `/distill-note` | Distills a note into a durable evergreen |
| `/remove-ai-slop` | Rewrites AI-sounding prose per [[HUMAN_WRITING]] |
| `/context` | Loads the context pack: manifest, dashboard, session log tail |
| `/trace-topic` | Traces a topic across the vault |
| `/connect-notes` | Surfaces missing wikilinks |
| `/weekly-review` | Answers the 7 weekly questions, writes the weekly note |
| `/lint-claude-layer` | Lints 60_Claude for broken links and orphans |
| `/ops` | Vault health operations (see `ops-reference.md`) |
| `/organize-csci2033` | Course-note merge workflow |
| `/tag-month` | Creates missing monthly checkpoint git tags |
| `/mcp-hub` | MCP server reference (skill file only, no command) |
Only `startday`, `closeday`, and `ingesting-clipping` follow the directory standard from [[Jarvis OS — North Star]] Part 5.1 (SKILL.md ≤500 lines + reference.md + scripts/). The other eleven are still flat prose files — convert them as they get used, most-used first.
### Agents (5, in `.claude/agents/`)
All five now carry proper frontmatter (`name`, `description` in the "Use proactively… MUST BE USED…" pattern, `tools` allowlist, `model: claude-sonnet-4-6`):
- `research-distiller` — deep source ingestion; the only agent with Bash + WebFetch (needs `extract_pdf.py` and `gh api`)
- `anti-slop-editor` — rewrites per [[HUMAN_WRITING]]
- `vault-curator` — link/duplicate/frontmatter health, report-first
- `learning-agent` — spaced-repetition drills over Capability Engine fields
- `career-operator` — internship/resume/mentorship briefs
### Hooks (2 scripts, wired in `.claude/settings.json`)
| Hook | Event | What it enforces |
| --- | --- | --- |
| `jarvis-session-continuity.ps1` | SessionStart + SessionEnd | Injects the context-pack read order at start; continuity at end |
| `jarvis-write-guard.ps1` | PreToolUse (Write\|Edit\|MultiEdit) | Write Contract: denies vault-root files, `50_Archive/`, `.obsidian/`, `05_Clippings/`, `.cursor/`, `.kiro/`, `.git/`; allowlists the daily-ops paths (Daily/, Plans/, Templates/, skills, agents, dashboard, session log, Claude OS) so the daily loop can never be blocked |
Both scripts live in `30_Order/System/claude-workflow/hooks/` — the vault owns the code, `.claude/settings.json` just points at it. Fail-open by design: a JSON parse error exits 0 rather than blocking real work.
### MCP servers (5, in `.mcp.json`)
| Server | Command | Provides |
| --- | --- | --- |
| obsidian | `uvx mcp-obsidian` | Vault read/write through the Obsidian Local REST API (patch-by-heading, periodic notes) |
| filesystem | `npx @modelcontextprotocol/server-filesystem` | Direct file access scoped to the vault |
| git | `uvx mcp-server-git` | Git operations on the vault repo |
| fetch | `uvx mcp-server-fetch` | Web fetch |
| jarvis-memory | `python 30_Order/System/jarvis-memory/server.py` | Custom: `jarvis_status`, `jarvis_search`, `jarvis_reindex` over a SQLite registry — the seed of the semantic index in North Star Part 5.4 |
The obsidian server needs the Local REST API plugin running (it is, `startupType: instant` in lazy-plugins). jarvis-memory verification status: see [[Claude OS]] MCP table.
## WSL home — what's installed there
- `graphify` skill (any input → knowledge graph, `/graphify`)
- second-brain-claudekit commands (7): `second-brain-capture/compress/graduate/resume/review`, `obsidian-daily-review`, `obsidian-session-review` — overlap analysis against Jarvis skills is in [[Claude OS]]
- Obsidian agents (3): `obsidian-architect`, `obsidian-researcher`, `obsidian-session-archivist`
- `everything-claude-code` marketplace: ~240 skills installed, almost none adopted — the High/Medium/Low relevance triage lives in [[Claude OS]]
- Windows home additionally carries `addy-agent-skills` and `claude-plugins-official` marketplaces plus ~30 firecrawl skills
The failure mode here is width: three marketplaces installed, near-zero adopted into actual workflows. Installing a skill is capture; adopting it means a command you actually type in a real session. Evaluate before enabling more.
## Connections
- Obsidian: Local REST API plugin + obsidian MCP; homepage plugin auto-opens [[10_Areas/AI/Jarvis OS Dashboard|Jarvis OS Dashboard]] canvas on vault start
- GitHub: `gh` CLI 2.89 + GitHub MCP tools; used live for repo ingestion (92 starred repos ingested via `gh api`, see 2026-06-28 log)
- Python: 3.13.5 with `pypdf` for PDF extraction; `30_Order/System/jarvis-cli` (8 read-only health commands) and `jarvis-memory` (SQLite registry)
- Excalidraw: `excalidraw` MCP (`30_Order/System/excalidraw-mcp/`) drives the live diagram canvas; this setup is mapped below

![[Claude OS Map.excalidraw]]
## Gaps
1. Nothing runs on a schedule. Hooks fire on events, but the morning context assembly and evening close (North Star Move 4) still require a human to type `/startday` and `/closeday`. This is the single biggest gap between "PKM" and "OS".
2. jarvis-memory is a skeleton — keyword search over a registry, no `chunks` populated, no semantic search. The whole token-economy design (North Star Part 6) waits on this.
3. Eleven skills are still flat files; the deterministic steps inside them (link checks, frontmatter validation) are prose an agent re-derives instead of scripts it runs.
4. The Portfolio and TradingView dump folders in `20_Progress/AI/Claude Code/` are empty — those setups exist only in their repos and aren't catalogued.
5. Marketplace skills: ~240 installed, adoption near zero. Triage table in [[Claude OS]]; act on the High rows, uninstall the noise.
