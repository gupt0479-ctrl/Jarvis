---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
source_url: 60_Claude/05_Clippings/PDFs/Nexus Setup Resource.pdf
source_note: "[[Nexus Setup Resource.pdf]]"
input_kind: pdf
track: ai
---
# GitNexus — Give Your AI Agent a Codebase Map — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Nexus Setup Resource.pdf`
**Ingested:** 2026-07-04
**Pages:** 1
## Source
A setup resource for **GitNexus** (abhigyanpatwari/GitNexus), a tool that indexes a repo into a **local knowledge graph** so AI coding agents can inspect structure before editing — "stop your agent from changing code blind."
## Key Claims
- ==GitNexus lets an agent inspect connected files, dependencies, call chains, execution flows, impacted symbols, and likely blast radius before a change==
- Best setup is **CLI + MCP**: `npx gitnexus analyze` then `npx gitnexus setup`, restart the agent to load the MCP server
- Works with Claude Code, Cursor, Codex, Windsurf, OpenCode, Antigravity — **Claude Code has the deepest integration** (MCP tools + skills + hooks)
- It's a **map, not a guarantee** — still run tests, review diffs, check risky changes manually; storage is local
## Full Content
**Setup (from project root):** `npx gitnexus analyze` → `npx gitnexus setup` → restart the editor/agent.
**Manual MCP (Claude Code):** macOS/Linux `claude mcp add gitnexus -- npx -y gitnexus@latest mcp`; Windows `claude mcp add gitnexus -- cmd /c npx -y gitnexus@latest mcp`. Codex: `codex mcp add gitnexus -- npx -y gitnexus@latest mcp`. Faster startup: `npm install -g gitnexus` then `gitnexus setup`.
**Agent instruction:** "Before you modify this codebase, use GitNexus to inspect the relevant symbols, dependencies, execution flows, and blast radius. If the index is stale, ask before re-indexing. Do not make broad changes until you understand what the touched code connects to."
**Safety:** a map, not a guarantee; run tests and review diffs; local storage; web UI can run in-browser or connect to a local backend.
## Why It Matters
This is the same idea as the vault's own `jarvis-memory` server but for *code* rather than notes — a graph the agent queries before acting. Genuinely useful for the **code projects** in [[Claude OS]] (CausalOps, Portfolio) where "changing code blind" is a real risk and the codebases are large; less relevant to vault work, which is prose. The "inspect blast radius before editing" instruction pairs with the karpathy-style surgical-edits discipline the North Star already endorses. Worth trialing on CausalOps specifically, where the coordinator/graph code is exactly the kind of tightly-coupled system where blast-radius matters. Anti-drift note: tool trial goes in the weekly slot.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Nexus Setup Resource.pdf`
- [[Claude OS]] — where the code-project agent setups live
- Repo: `github.com/abhigyanpatwari/GitNexus`
## Open Questions
- [ ] Trial GitNexus on CausalOps (large, tightly-coupled) to see if blast-radius inspection catches breakages Claude misses?
- [ ] Does it overlap with the existing preflight/canon-gate hooks, or add a distinct capability?
## Flashcards
#cards/ai
What problem does GitNexus solve for AI coding agents?::It indexes a repo into a **local knowledge graph** so the agent can inspect dependencies, call chains, execution flows, and **blast radius before editing** — stopping it from changing code blind.
Why is GitNexus more relevant to CausalOps/Portfolio than to the Jarvis vault?::It maps **code** structure, not prose — its value is in large, tightly-coupled codebases where blast radius matters, whereas vault work is notes (already covered by jarvis-memory).
