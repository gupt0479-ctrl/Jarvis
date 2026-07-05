---
setup_status: current
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
---

# .claude — Jarvis tooling layer

This folder makes Claude Code the source of truth for operating the Jarvis vault. It wires the rules (the Write Contract and workflows), the tools (MCP servers), the automation (hooks), and the helpers (skills, agents) into one coherent system. The design goal is additive: every new MCP server, skill, agent, hook, or Python tool slots into a named place with a documented pattern, so adding more never forces a restructure.

If you are an agent, read `60_Claude/07_AI_Information/Vault Map.md` first. This README is for configuring the machinery, not for writing notes.

## How the pieces fit

```
Rules        AGENTS.md (Write Contract)  ·  30_Order/Workflows/  ·  HUMAN_WRITING.md
Orientation  60_Claude/07_AI_Information/Vault Map.md  ·  AI_CONTEXT.md
Tools        .mcp.json  ->  obsidian · filesystem · git · fetch · jarvis-memory
Automation   .claude/settings.json hooks  ->  30_Order/System/claude-workflow/hooks/*.ps1
Data         30_Order/System/jarvis-memory/  (SQLite registry + MCP server)
CLI          30_Order/System/jarvis-cli/     (read-only vault ops)
Helpers      .claude/skills/  ·  .claude/agents/
```

Single source of truth for *where notes go*: `40_Resources/Obsidian/Jarvis Vault Architecture.md`. Nothing in this folder should re-describe folder roles — it points there.

## Files in this folder

| Path | Role | Committed? |
|---|---|---|
| `settings.json` | Model, effort, and the hook registrations | No (gitignored — machine-local) |
| `settings.local.json` | Permission allow-list + `enableAllProjectMcpServers` | No (gitignored) |
| `agents/` | Subagent definitions (Markdown) | Yes |
| `skills/` | Slash-command skills (Markdown) | Yes |
| `rules/` | Steering wrappers (e.g. human-writing) | Yes |
| `context/` | Cross-tool steering context | Yes |

`.mcp.json` and the Python tooling live at the vault root and under `30_Order/System/`, not here, but are wired from here.

## MCP servers (`.mcp.json` at vault root)

Five servers, project-scoped. Secrets are referenced as `${ENV_VAR}` and never committed.

| Server | Command | Purpose | Needs |
|---|---|---|---|
| `obsidian` | `uvx mcp-obsidian` | Read/write the vault through the Local REST API plugin | `OBSIDIAN_API_KEY` env; the Obsidian "Local REST API" plugin enabled |
| `filesystem` | `npx @modelcontextprotocol/server-filesystem` | Direct file ops scoped to the vault | Node |
| `git` | `uvx mcp-server-git` | History, diffs, safe rollbacks | uv; git |
| `fetch` | `uvx mcp-server-fetch` | Pull web sources into the clipping workflow | uv |
| `jarvis-memory` | `python .../jarvis-memory/server.py` | The note registry: status, search, reindex | Python; `pip install mcp` |

### Prerequisites (one-time)

- **Python 3.10+**, **Node** (`npx`), and **uv** (`uvx`) on PATH.
- The Obsidian **Local REST API** plugin enabled; copy its API key.

### Secrets — env vars, never committed

Set these in your OS/user environment (PowerShell example):

```powershell
setx OBSIDIAN_API_KEY "paste-your-local-rest-api-key"
# optional overrides; defaults are 127.0.0.1 / 27124
setx OBSIDIAN_HOST "127.0.0.1"
setx OBSIDIAN_PORT "27124"
```

`.mcp.json` reads `${OBSIDIAN_API_KEY}`. Nothing sensitive is written to the repo. `.env`, `.env.local`, and `.claude/.env.local` are gitignored if you prefer a file.

### Adding an MCP server later

Add one object under `mcpServers` in `.mcp.json`. Use `${ENV_VAR}` for any secret and an absolute path for any local script. Restart Claude Code. That's the whole procedure — no other file changes required.

## Hooks (`.claude/settings.json` -> `30_Order/System/claude-workflow/hooks/`)

| Event | Script | What it does |
|---|---|---|
| `SessionStart` | `jarvis-session-continuity.ps1` | Injects the context-pack policy: read the Vault Map, AGENTS Write Contract, Architecture, and `30_Order` before writing |
| `PreToolUse` (Write/Edit/MultiEdit) | `jarvis-write-guard.ps1` | Enforces the Write Contract negatives: blocks new files at the vault root, and any write into `50_Archive/` or `.obsidian/`. Fails open on parse errors |
| `SessionEnd` | `jarvis-session-continuity.ps1` | Appends a session-activity line to `~/.claude/jarvis-session-activity.jsonl` |

The write-guard is the safety rail that makes "no conflicts tomorrow" real: even an agent that ignores the rules physically cannot pollute the root or the archive.

### Adding a hook later

Drop a `.ps1` in `30_Order/System/claude-workflow/hooks/`, register it under the event in `settings.json` with `powershell -NoProfile -ExecutionPolicy Bypass -File "<absolute path>"`. Hooks receive the event JSON on stdin; a `PreToolUse` hook can return `permissionDecision: deny` to block.

## Python tooling (`30_Order/System/`)

| Path | Role |
|---|---|
| `jarvis-cli/jarvis_ops.py` | Read-only vault ops: `status`, `health`, `context`, `projects`, `links`, `dates`, `encoding`, `enrich-candidates`, `report` |
| `jarvis-cli/jarvis.ps1` | PowerShell wrapper that finds Python and the vault root |
| `jarvis-memory/registry.py` | SQLite note index: `index`, `status`, `search` |
| `jarvis-memory/server.py` | MCP server exposing the registry |
| `jarvis-memory/schema.sql` | Registry tables for the full three-month plan |

```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 status
python .\30_Order\System\jarvis-memory\registry.py index
```

The CLI is read-only by design (only `report` writes, and only a new file). The registry is derived state — delete `registry.sqlite` and reindex any time.

## Agents and skills

Subagents live in `agents/` (research-distiller, vault-curator, career-operator, anti-slop-editor, learning-agent). Skills are slash commands in `skills/` (see `CLAUDE.md` for the table). The contract for both: **read the canonical docs, do not restate folder paths.** An agent or skill should reference `60_Claude/07_AI_Information/Vault Map.md`, the matching `30_Order/Workflows/` procedure, and the AGENTS Write Contract — never hard-code a routing table that can drift.

### Adding a skill or agent later

Create `skills/<name>.md` or `agents/<name>.md`. Open with: which canonical docs to read, which workflow it follows, and its specific job. Register skills in the `CLAUDE.md` table. Keep folder-routing out of the body — defer to the architecture note.

## Alignment backlog

**2026-06-24 reorg pass.** The vault moved again: `60_Claude/50_Reviews/` → `60_Claude/30_Reviews/` (rename, contents intact), `60_Claude/35_Outputs/` was deleted outright (not replaced — anything that used to route there now falls back to `60_Claude/00_Inbox/` per the Write Contract's "unsure → Inbox" rule), `40_Resources/CS/AI/` flattened files moved into `Toolkit/`, `Workflows/`, `Gen AI/`, `Prompts/`, `Token Optimization/` subfolders, UMN coursework split (`10_Areas/UMN/` now holds only the current-term board/syllabus; past course material moved to `40_Resources/UMN/Previous Classes/`), `30_Order/Standards/` and `30_Order/Workflows/` are now populated (previously documented as missing), and `Claude Pro Workflow.md` moved from `40_Resources/Obsidian/` to `40_Resources/CS/AI/Token Optimization/`. Every `agents/` and `skills/` file was re-read against the current tree and patched in this pass — paths above should now resolve.

**Known good, not touched:** `ingesting-clipping/` skill directory, `research-distiller.md`, `anti-slop-editor.md`, `connect-notes.md`, `remove-ai-slop.md`, `rules/human-writing.md`, `commands/*.md` (thin pointers, no embedded paths).

**Still open — out of scope for the 2026-06-24 pass, deliberately:**
- `40_Resources/Obsidian/Jarvis Vault Architecture.md` and `60_Claude/07_AI_Information/Vault Map.md` (the actual folder-role authorities) still describe the pre-reorg structure — `35_Outputs` as live, `50_Reviews` not `30_Reviews`, all UMN coursework under `10_Areas/UMN`. This file intentionally does not re-describe folder roles (see the "single source of truth" note above), so it was not the place to fix that — the architecture note itself needs the rewrite.
- `60_Claude/07_AI_Information/Jarvis OS — North Star.md` Part 3.3 cites the MGMT 3001 week notes as the template gold-standard. The vault owner says those notes were ungraded AI output dumped during the course, not a standard to build toward — this claim needs revisiting, not propagated further.
- `60_Claude/30_Reviews/50_Reviews Board.md` still carries its pre-rename filename (vault content, not `.claude/` — flagged here, not changed here).
- Where a removed `35_Outputs/`-routed artifact should actually land long-term is undecided. Current fallback is `00_Inbox/`; this is a stopgap, not a redesign.

These four are the explicit subject of the vault owner's planned follow-up conversation about redefining what each folder is for — don't pre-empt it by rewriting the architecture note from this backlog.
