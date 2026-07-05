---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Cursor/CausalOps/Setup]]"
---
# Cursor workflow for HiveMind

Project-level agent configuration lives under `.cursor/`. Global MCP servers
(Obsidian, GitHub, filesystem vaults) live in `~/.cursor/mcp.json`.

## Layout

- `rules/` — always-on and file-scoped guidance
- `skills/` — task-specific workflows (hivemind-project, persistent-semantic-memory)
- `hooks/` — session preflight and guardrails
- `agents/` — optional project subagents (use `~/.cursor/agents/` for personal agents)

## Global MCP (all projects)

Configured in `~/.cursor/mcp.json` to mirror Windows Claude Desktop:

| Server | Transport | Purpose |
|--------|-----------|---------|
| `jarvis` | HTTP → `127.0.0.1:27123/mcp/` | Jarvis vault REST API |
| `the-plan` | HTTP → `127.0.0.1:27124/mcp/` | The Plan vault REST API |
| `jarvis-fs` | stdio filesystem | Jarvis vault files |
| `the-plan-fs` | stdio filesystem | The Plan vault files |
| `github` | stdio | GitHub API |

Secrets: copy `~/.cursor/mcp.env.example` to `~/.cursor/mcp.env` and source it
from your shell profile so `${env:...}` placeholders resolve at Cursor startup.

Requirements:

1. Obsidian running on Windows with Local REST API plugin enabled (HTTP + MCP endpoint)
2. WSL can reach `127.0.0.1:27123` and `27124` (WSL2 localhost forwarding)
3. Vault paths mounted at `/mnt/d/Users/_Anant/10_Areas/Documents/...`

## Verification

After changing MCP config, restart Cursor and check **Settings → MCP** for green status on `jarvis` and `the-plan`.
