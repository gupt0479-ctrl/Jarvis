---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
source_url: 60_Claude/05_Clippings/Web/Naive - Quickstart.md
source_note: "[[Naive - Quickstart.md]]"
input_kind: web
track: ai
---
# Naive — Agent Primitives API (Quickstart) — Summary
**Source:** `60_Claude/05_Clippings/Web/Naive - Quickstart.md` (usenaive.ai)
**Ingested:** 2026-07-04
**Pages:** quickstart doc
## Source
The quickstart for **Naive**, a CLI/API that gives AI agents ready-made "primitives" (search, etc.) via a skill manifest an agent can self-install.
## Key Claims
- ==The whole setup is a self-installing skill manifest: paste **"follow https://api.usenaive.ai/skill.md and setup naive"** into any agent (Claude/ChatGPT/Cursor) and it registers an account and starts using primitives autonomously==
- CLI: `npm install -g @usenaive-sdk/cli` → `naive register` → `naive search "..."` (the key auto-saves)
- The pitch is agents-calling-agents: give an agent a set of callable primitives rather than hand-building each integration
## Why It Matters
Low-signal but conceptually adjacent to the Jarvis MCP work ([[Claude OS]]) — Naive's "skill.md manifest an agent reads to install itself" is the same self-describing-capability idea as MCP, and the Agent-Ready Roadmap's "give an agent buttons it can push." Worth knowing the pattern exists; not worth adopting over the existing MCP servers, which already give Jarvis agents their primitives (obsidian, filesystem, git, jarvis-memory). Recorded as a discovery note. Anti-drift: any trial is weekly-slot work.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/Web/Naive - Quickstart.md`
- [[Claude OS]] — the MCP servers that already provide Jarvis's agent primitives
## Flashcards
#cards/ai
What is Naive's self-install mechanism?::Paste **"follow https://api.usenaive.ai/skill.md and setup naive"** into any agent — it reads the **skill manifest**, registers an account, and starts calling primitives (like `search`) autonomously.
