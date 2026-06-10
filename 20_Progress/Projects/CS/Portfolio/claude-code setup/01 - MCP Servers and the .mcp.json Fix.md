---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - claude-setup
  - mcp
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
  - "[[02 - Deploy Security Checklist]]"
---
# MCP Servers and the .mcp.json Fix
This note owns the MCP setup for the WSL repo and fixes the "Sanity/Clerk don't render" problem. Claude Code's project MCPs come from `.mcp.json`, not from the Desktop connectors — so what works in Cowork does not automatically work in the repo.
## Why your config doesn't render (the likely causes, in order)
Your file is `.claude/mcp.json`. Two things commonly break it:
1. **Location.** Claude Code reads project-scoped MCP from **`.mcp.json` at the repo root** (a leading dot, at the top level — not inside `.claude/`). `.claude/mcp.json` is also accepted in some setups, but the reliable, documented location is repo-root `.mcp.json`. Move it there first.
2. **Missing credentials / env expansion.** Sanity and Clerk servers need tokens. If the `env` block references a variable that isn't set, the server fails silently on startup. Other silent killers: a trailing comma (JSON forbids them), an unescaped backslash, or a command binary that doesn't resolve. After any change you **must restart Claude Code** — config is read at launch.
Diagnose fast: run the server command manually in the WSL terminal to see stderr, run the file through `jq` to catch JSON errors, and check `claude mcp list` after restart.
## The working .mcp.json (repo root)
```json
{
  "mcpServers": {
    "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "sanity": {
      "command": "npx",
      "args": ["-y", "@sanity/mcp-server"],
      "env": {
        "SANITY_PROJECT_ID": "${SANITY_PROJECT_ID}",
        "SANITY_DATASET": "production",
        "SANITY_API_TOKEN": "${SANITY_API_TOKEN}"
      }
    },
    "clerk": {
      "command": "npx",
      "args": ["-y", "@clerk/agent-toolkit", "--mcp"],
      "env": { "CLERK_SECRET_KEY": "${CLERK_SECRET_KEY}" }
    },
    "upstash": {
      "command": "npx",
      "args": ["-y", "@upstash/mcp-server"],
      "env": {
        "UPSTASH_EMAIL": "${UPSTASH_EMAIL}",
        "UPSTASH_API_KEY": "${UPSTASH_API_KEY}"
      }
    }
  }
}
```
Confirm exact package names and required env with Context7 / the Vercel docs MCP before pasting — vendor package names drift, and this note is a starting point, not gospel. GitHub and Vercel MCPs you already have as Desktop connectors; add them here too only if you want Claude Code to use them headlessly in the repo.
## Env vars (never commit)
Put the real values in the repo's `.env.local` (gitignored) or export them in the WSL shell before launching `claude`. Same secrets discipline as [[02 - Deploy Security Checklist]]: server-only, never `NEXT_PUBLIC_`, scoped per environment in Vercel for deploy.
## jarvis MCP and the WSL→Windows gotcha
You want Claude Code to read the plan through jarvis. jarvis is the Obsidian Local REST API on **Windows `localhost:27123`**. From WSL2, `localhost` resolves to WSL, not Windows — so a jarvis MCP pointed at `localhost` will fail to connect from the repo. Two fixes:
- **Preferred: skip jarvis, read the files directly.** The vault is on D:, mounted in WSL at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/...`. Claude Code just `Read`s the phase note. No network, fewest tokens. This is what [[05 - Per-Phase Build Prompts]] use.
- **If you insist on jarvis MCP:** point it at the Windows host IP, not `localhost` — either enable WSL2 **mirrored networking** (`networkingMode=mirrored` in `.wslconfig`, then `localhost` works) or use the host IP from `/etc/resolv.conf`. Restart Claude Code after.
## What each server is for in this build
- **Direct `/mnt/d` reads** — pull the design notes (primary path).
- **sanity** — schema work, GROQ queries, fixing the slug fields the build needs (see [[06 - Tool System & Generative UI]]).
- **clerk** — version-correct auth SDK snippets; matters for the v2 memory path, light in v1.
- **upstash** — provision the Redis used for rate limiting (see [[05 - Model Layer, Rate Limiting & Abuse]]).
- **context7** — keep all library API calls (AI SDK, Next 16, Clerk, Sanity) version-correct.
