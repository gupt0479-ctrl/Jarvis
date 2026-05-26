# Claude Workflow System

This folder holds local helpers for the Jarvis Claude Pro workflow.

## Files

- `hooks/jarvis-session-continuity.ps1`: lightweight Claude Code hook script.
- `claude_desktop_config.read-first.example.json`: Desktop MCP reference config. Use it as a guide, not as a secret store.
- `.mcp.json` at the vault root is the Claude Code project MCP file used by current Claude Code builds.
- `.claude/.mcp.json` is kept for compatibility with the earlier Jarvis setup.

## Contract

- Claude Code is the main implementation surface.
- Desktop is read-first planning and review.
- Mobile is capture only.
- MCP should retrieve small context packs, not dump the whole vault.
