---
type: concept
status: sprout
created: 2026-06-20
updated: 2026-08-26
course: Life
track:
  - laptop
  - ai-infrastructure
mastery_level: 4
prerequisites:
  - "[[New Laptop Setup]]"
used_in: []
evidence: []
tags:
  - concept
related:
  - "[[What MCPs]]"
  - "[[New Laptop Setup]]"
---
# Jarvis MCP and REST API Setup
## One-Line Answer
==Jarvis is reachable through two unrelated MCP paths — an HTTP path through Obsidian's Local REST API plugin that needs the app running, and a stdio filesystem/tooling path that doesn't need Obsidian open — and as of 2026-08-26 the home-level config already does the right thing (env-var-substituted tokens, correct port defaults); the earlier "three configs disagree" problem this note originally documented has been fixed in practice, just not previously updated here.==
## Mechanism
*The two paths, concretely:*
- HTTP path, server name `jarvis` — talks to the Local REST API plugin inside the running Obsidian app at `http://127.0.0.1:27123/mcp/`. Needs Obsidian open with the plugin enabled. Gives app-level operations: search, read/patch by heading, tags, run Obsidian commands, know the active file. This is the `mcp__jarvis__*` tool family.
- The Plan vault has the equivalent HTTP pair, `the-plan` (port `27124`).
- A separate project-local config (see below) additionally wires up filesystem, git, fetch, a custom memory server, and Excalidraw — none of which are Obsidian-app-aware.
*Why both a running-Obsidian path and a filesystem/tooling path matter:* the HTTP path can search by tag, trigger a command, and know what's open — the filesystem/tooling servers cannot do any of that, but keep working with Obsidian closed. Neither replaces the other.
*Verified current state of the configs (2026-08-26, corrects this note's earlier claims):*
1. `C:\Users\Anant Gupta\.mcp.json` — the global config Claude Code reads for any session. Defines `jarvis` and `the-plan` (HTTP) plus a `github` server. **Bearer tokens are already `${JARVIS_OBSIDIAN_API_KEY}` / `${THE_PLAN_OBSIDIAN_API_KEY}` env-var references, not hardcoded strings** — both env vars are confirmed set as Windows user variables. (This note previously claimed hardcoded literal tokens; that was already fixed by the time of this check and just never got reflected here.)
2. `D:\Users\_Anant\10_Areas\Documents\Jarvis\.mcp.json` — the project-local config, active only when Claude Code's working directory is inside the vault. Defines `obsidian` (via `uvx mcp-obsidian`), `filesystem`, `git`, `fetch`, `jarvis-memory` (custom Python server at `30_Order/System/jarvis-memory/server.py`), and `excalidraw`. **`OBSIDIAN_PORT` already defaults to `27123` correctly** (this note previously claimed a `27124`/The-Plan-port default bug; not present in the current file).
3. WSL `~/.mcp.json` — not checked this session (out of scope; see [[WSL Session Briefing]]). Still worth confirming from a WSL-side session, since a Windows-style backslash path handed to a Linux `npx` process would still fail there regardless of the Windows-side fixes above.
## Contrast / What It Is Not
This is not the same note as [[What MCPs]], the older Cursor-era brainstorm. That note explains MCP as a general concept — transports, security notes, generic server categories — and never once names Jarvis's actual ports, keys, or config files. This note documents what is wired up on this specific machine, not what MCP is in the abstract.
## Failure Modes / Misconceptions
> [!WARNING]
> Assuming `jarvis` (HTTP) and the project-local `filesystem`/`obsidian` servers are redundant. Close Obsidian and the HTTP path goes dark while filesystem-style access keeps working; ask for a tag search or a command run and the filesystem path simply can't do it.
> [!WARNING]
> Copying `~/.mcp.json` to the new laptop expecting it to work immediately. The Bearer tokens resolve from env vars now (good), but those env vars still hold *this* Obsidian install's API keys — a fresh Obsidian install generates new keys, and the old ones will be rejected until the env vars are updated.
> [!WARNING]
> Running Claude Code from inside the vault folder and assuming the home-level `.mcp.json` applies. The project-local config takes over instead — different server set entirely (adds git/fetch/memory/excalidraw, uses `uvx mcp-obsidian` instead of a direct HTTP call).
> [!WARNING]
> Expecting the Jarvis filesystem-style MCP tools to work unmodified from a WSL-side Claude Code session. The project-local config's paths are Windows-style (`D:\Users\_Anant\...`) — untested from WSL this session, flagged in [[WSL Session Briefing]].
## New Laptop Checklist
- [ ] Install Obsidian, open Jarvis and The Plan from `D:\Users\_Anant\10_Areas\Documents\`
- [ ] Install the Local REST API plugin in **both** vaults, enable it, and read the port each one actually claims — don't assume Jarvis is `27123` and The Plan is `27124`, confirm in the plugin settings
- [ ] Generate a new API key per vault in the plugin settings — old keys do not carry over
- [ ] Write the new keys into Windows user env vars `JARVIS_OBSIDIAN_API_KEY` and `THE_PLAN_OBSIDIAN_API_KEY` (confirmed the actual variable names in use, corrected from this note's earlier `OBSIDIAN_JARVIS_API_KEY`/`OBSIDIAN_PLAN_API_KEY`)
- [ ] `~/.mcp.json` already references `${VAR}` substitution correctly — just needs the vars repopulated with the new keys, no structural fix needed
- [ ] If a WSL-side Claude Code session needs vault access, write a WSL-native `~/.mcp.json` using `/mnt/d/...` paths — do not assume the Windows project-local config works there
- [ ] Before doing anything else in a fresh session, confirm `jarvis`, `the-plan`, and the project-local `filesystem`/`obsidian`/`git`/`fetch`/`jarvis-memory`/`excalidraw` servers all connect
## Evidence From This Vault
- the `mcp__jarvis__*`, `mcp__the-plan__*` tool families available in any Claude Code session — direct proof the HTTP path is real
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.mcp.json` — the project-local config, re-verified 2026-08-26
- [[What MCPs]] — the older, generic note this one supersedes for Jarvis-specific wiring
- [[WSL Session Briefing]] — where the WSL-side `~/.mcp.json` gap is tracked
## Flashcards
Why do the HTTP (`jarvis`) server and the project-local filesystem/tooling servers both matter for the same vault?::`jarvis` (HTTP) is Obsidian-app-aware — search, tags, commands — but needs Obsidian running. The project-local servers (filesystem, git, fetch, memory) always work but have no app awareness. Neither replaces the other.
#cards/laptop
As of 2026-08-26, are the Bearer tokens in `~/.mcp.json` hardcoded strings or env-var references?::Env-var references (`${JARVIS_OBSIDIAN_API_KEY}`, `${THE_PLAN_OBSIDIAN_API_KEY}`), both confirmed set. An earlier version of this note claimed they were hardcoded — that was already fixed by the time of the 2026-08-26 check.
#cards/laptop
Why would the Jarvis filesystem/tooling MCP servers fail if invoked from a WSL-side Claude Code session using the existing project-local config?::The config passes Windows-style paths (`D:\Users\_Anant\...`) as arguments. A Linux-side process can't resolve a backslash, drive-letter path. Not re-verified this session — flagged for a WSL session to check directly.
#cards/laptop
