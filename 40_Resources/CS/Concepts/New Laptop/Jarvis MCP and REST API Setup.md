---
type: concept
status: sprout
created: 2026-06-20
updated: 2026-06-20
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
  - "[[MCPs]]"
  - "[[New Laptop Setup]]"
---
# Jarvis MCP and REST API Setup
## One-Line Answer
==Jarvis is reachable through two unrelated MCP paths — an HTTP path through Obsidian's Local REST API plugin that needs the app running, and a stdio filesystem path that reads the vault folder directly with no Obsidian awareness — and right now three different config files wire this up and disagree with each other.==
## Mechanism
*The two paths, concretely:*
- HTTP path, server name `jarvis` — talks to the Local REST API plugin inside the running Obsidian app at `http://127.0.0.1:27123/mcp/`. Needs Obsidian open with the plugin enabled. Gives app-level operations: search, read/patch by heading, tags, run Obsidian commands, know the active file. This is the `mcp__jarvis__*` tool family.
- Filesystem path, server name `jarvis-fs` — a plain `@modelcontextprotocol/server-filesystem` process pointed straight at `D:\Users\_Anant\10_Areas\Documents\Jarvis` on disk. Works even with Obsidian closed. No tag, command, or active-file awareness — just file read/write/move. This is the `mcp__jarvis-fs__*` tool family.
- The Plan vault has the identical pair, `the-plan` (HTTP, port `27124`) and `the-plan-fs` (filesystem).
*Why both exist instead of one:* the HTTP path can search by tag, trigger a command, and know what's open — a filesystem server cannot do any of that. The filesystem path is the one that still works when Obsidian isn't running. Neither replaces the other; losing track of this is most of "wasting time on the REST API."
*The three configs that exist today, and where they disagree:*
1. `C:\Users\Anant Gupta\.mcp.json` — the global config Claude Code reads for any session. Defines `jarvis`/`the-plan` (HTTP) and `jarvis-fs`/`the-plan-fs` (filesystem). Its Bearer tokens are hardcoded as literal strings, even though `OBSIDIAN_JARVIS_API_KEY` and `OBSIDIAN_PLAN_API_KEY` already exist as Windows user env vars for this exact purpose and currently do nothing.
2. `D:\Users\_Anant\10_Areas\Documents\Jarvis\.mcp.json` — a second, project-local config that only applies when Claude Code's working directory is inside the vault. It uses a different package (`uvx mcp-obsidian`) instead of a direct HTTP call, and defaults `OBSIDIAN_PORT` to `27124` — that is The Plan's port, not Jarvis's `27123`. It also defines `git`, `fetch`, and a custom `jarvis-memory` Python server (`30_Order/System/jarvis-memory/server.py`) that the other two configs never mention.
3. WSL `~/.mcp.json` — does not exist. A Claude Code session started from WSL has none of this wired up. Even if it inherited the project-local config above, that config's filesystem path is a Windows-style string (`D:\Users\_Anant\...`, backslashes) handed to a Linux-side `npx` process, which cannot resolve it.
## Contrast / What It Is Not
This is not the same note as [[MCPs]], the older Cursor-era brainstorm. That note explains MCP as a general concept — transports, security notes, generic server categories — and never once names Jarvis's actual ports, keys, or config files. This note documents what is wired up on this specific machine, not what MCP is in the abstract.
## Failure Modes / Misconceptions
> [!WARNING]
> Assuming `jarvis` and `jarvis-fs` are redundant and only one is needed. Close Obsidian and the HTTP path goes dark while the filesystem path keeps working; ask for a tag search or a command run and the filesystem path simply can't do it.
> [!WARNING]
> Copying `~/.mcp.json` to the new laptop expecting it to work immediately. The Bearer tokens are tied to keys the Local REST API plugin generated on this install — a fresh Obsidian install generates new keys, and the old tokens will be rejected.
> [!WARNING]
> Running Claude Code from inside the vault folder and assuming the home-level `.mcp.json` applies. The project-local config takes over instead, and it is the one with the `27124` default-port mismatch.
> [!WARNING]
> Expecting the Jarvis filesystem MCP to work from a WSL-side Claude Code session through the existing project-local config. The path is Windows-style and a Linux `npx` process cannot resolve a backslash path with a drive letter.
## New Laptop Checklist
- [ ] Install Obsidian, open Jarvis and The Plan from `D:\Users\_Anant\10_Areas\Documents\`
- [ ] Install the Local REST API plugin in **both** vaults, enable it, and read the port each one actually claims — don't assume Jarvis is `27123` and The Plan is `27124`, confirm in the plugin settings
- [ ] Generate a new API key per vault in the plugin settings — old keys do not carry over
- [ ] Write the new keys into Windows user env vars `OBSIDIAN_JARVIS_API_KEY` and `OBSIDIAN_PLAN_API_KEY` — the variable names already exist as a pattern from the old machine
- [ ] Write `~/.mcp.json` so the `jarvis`/`the-plan` headers reference `${OBSIDIAN_JARVIS_API_KEY}`/`${OBSIDIAN_PLAN_API_KEY}` instead of hardcoded strings — the project-local config already proves `${VAR}` substitution works here
- [ ] Fix the project-local `D:\...\Jarvis\.mcp.json` port default while touching this — it should not silently default to `27124`
- [ ] If a WSL-side Claude Code session needs vault access, write a WSL-native `~/.mcp.json` using `/mnt/d/...` paths — do not assume the Windows project-local config works there
- [ ] Before doing anything else in a fresh session, confirm `jarvis`, `jarvis-fs`, `the-plan`, and `the-plan-fs` all connect
## Evidence From This Vault
- the `mcp__jarvis__*`, `mcp__jarvis-fs__*`, `mcp__the-plan__*`, `mcp__the-plan-fs__*` tool families available in any Claude Code session — direct proof the dual-path setup is real
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.mcp.json` — the project-local config with the port mismatch
- [[MCPs]] — the older, generic note this one supersedes for Jarvis-specific wiring
## Flashcards
Why do `jarvis` and `jarvis-fs` both exist for the same vault?::`jarvis` (HTTP) is Obsidian-app-aware — search, tags, commands — but needs Obsidian running. `jarvis-fs` (filesystem) always works but is just file read/write with no app awareness. Neither replaces the other.
#cards/laptop
The project-local `.mcp.json` inside the Jarvis vault defaults `OBSIDIAN_PORT` to which value, and why is that wrong?::`27124` — that's The Plan's port. Jarvis's own Local REST API plugin runs on `27123`. It's a copy-paste mismatch, not an intended default.
#cards/laptop
A Bearer token for the Jarvis MCP server is hardcoded as a literal string in `~/.mcp.json` instead of referencing an env var — what's the fix, and where's the proof it would work?::Replace the literal string with `${OBSIDIAN_JARVIS_API_KEY}`. The project-local `.mcp.json`'s `obsidian` entry already does this successfully with `${OBSIDIAN_API_KEY}`.
#cards/laptop
Why would the Jarvis filesystem MCP fail if invoked from a WSL-side Claude Code session using the existing project-local config?::The config passes a Windows-style path (`D:\Users\_Anant\...`) as an argument to the filesystem server. A Linux-side `npx` process can't resolve a backslash, drive-letter path.
#cards/laptop
