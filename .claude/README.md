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

The infrastructure above is current. These existing helper docs still carry pre-reorg folder paths and should be aligned to the new structure and workflows (low risk, high tidiness). Tracked so it isn't forgotten:

- `agents/`: `research-distiller.md`, `career-operator.md`, `anti-slop-editor.md`, `learning-agent.md` (vault-curator is already aligned).
- `skills/`: `distill-note.md`, `context.md`, `today.md`, `closeday.md`, `weekly-review.md`, `lint-claude-layer.md`, `trace-topic.md`, `connect-notes.md`, `ops.md`, `organize-csci2033.md`, `mcp-hub.md` (ingest-clipping is already aligned).

Each just needs dead paths updated (`10_UMN`→`10_Areas/UMN`, `30_Source_Summaries`→`10_Source_Summaries`, `45_Outputs`→`35_Outputs`, `60_Indexes`→`44_Indexes`, `10_Session_Logs`→`07_AI_Information/Session Logs`, `7_AI_Information`→`07_AI_Information`) and a pointer to the matching workflow.
