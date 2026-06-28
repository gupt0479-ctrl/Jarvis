---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - claude
  - second-brain
  - knowledge-management
  - mcp
source_url: https://github.com/garrytan/gbrain
notes:
  - "[[40_Resources/CS/Repos]]"
---
# GBrain

**GitHub:** [garrytan/gbrain](https://github.com/garrytan/gbrain) | **Stars:** large (Garry Tan, YC CEO) | **Updated:** Active

## What it is
Personal knowledge MCP server with synthesis (not just RAG), self-wiring knowledge graph, and 43 skills for autonomous ingestion. Built and used by Garry Tan (YC CEO) to manage 146K pages, 24K people, 5K companies across meetings, emails, tweets, calls.

The key differentiator: `gbrain think "question"` returns a **synthesized answer with citations + explicit gap analysis** — what it knows, what it doesn't, what's stale. Not "here are 10 chunks"; an actual prose answer. Benchmarked: P@5 49.1%, R@5 97.9% on rich-prose corpus, +31.4 pts over vector-only RAG.

Also supports team/company brain with per-user access control.

## How Anant uses it
**Verdict: Potentially worth integrating as Claude Code MCP, not a Jarvis replacement.**

GBrain is an MCP server — it connects to Claude Code as a tool layer, not a competing system. The fastest integration path:
```bash
npm install -g github:garrytan/gbrain  # or: bun install -g github:garrytan/gbrain
gbrain init --pglite           # 2-second local DB, no Docker
claude mcp add gbrain -- gbrain serve
```
Then Claude Code has 30+ brain tools available in any session.

The synthesis + gap analysis layer is genuinely stronger than Obsidian's backlink browsing for complex questions ("what do I know about X, and what's missing?"). The knowledge graph edge extraction (person-company-investment relationships) would be useful for trading research (tracking who's building what).

**However:** the 43-skill "dream cycle" autonomous enrichment requires an always-on agent platform (OpenClaw or Hermes). For just the MCP layer + local brain, the lightweight path above works without that.

## How to install / run it (Windows)
```bash
bun install -g github:garrytan/gbrain
gbrain init --pglite     # no server, no Docker needed
gbrain doctor            # verify
gbrain import ~/path/to/notes/  # index existing markdown
claude mcp add gbrain -- gbrain serve
```
Bun works on Windows. PGLite runs entirely in-process — no PostgreSQL server needed.

## Caveats / current state
- Designed by Garry Tan for his own production use at 146K pages — not vaporware
- PGLite path makes local setup genuinely easy; Postgres/Supabase paths for scale
- 43 skills + overnight enrichment requires separate agent platform (optional)
- **Research and implement a better form for second brain?** GBrain's synthesis layer is worth studying for what it does beyond Jarvis. The knowledge graph extraction and gap analysis are the parts Jarvis doesn't have. Consider adding gbrain as MCP to the Jarvis Claude Code config for a trial.
- License: likely MIT (follows Garry Tan's open-source pattern — check repo)

## Connects to
[[40_Resources/CS/Repos]]
