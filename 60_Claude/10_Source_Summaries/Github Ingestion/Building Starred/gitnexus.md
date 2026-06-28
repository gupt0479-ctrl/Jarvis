---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - claude
  - mcp
  - tooling
source_url: https://github.com/abhigyanpatwari/GitNexus
notes:
  - "[[40_Resources/CS/Repos]]"
---
# GitNexus

**GitHub:** [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | **Stars:** 43.1k | **Updated:** June 26, 2026 (daily commits)

## What it is
Claude Code plugin that indexes a codebase into a graph database (KuzuDB) and exposes 15 MCP tools for deep code understanding. Builds a Program Dependency Graph (PDG) with CFG → reaching-defs → intra/inter-procedural taint → control dependence. Supports multi-branch indexing and private GitHub PAT + Azure DevOps.

Key MCP tools: `trace` (shortest call path between two symbols via BFS), `impact` (what does changing X affect), `context` (what does this symbol do), `api_impact` (which API routes are affected), plus 10 others.

## How Anant uses it
Install as a Claude Code plugin (`.claude-plugin` directory). Primary use case: navigating large codebases where "find where X is called from" or "what breaks if I change Y" takes minutes of manual search. For the trading project (TradingAgents + Kronos), `gitnexus trace analyst trader` finds how agent signals flow to the trader without reading thousands of lines. `gitnexus impact` before any refactor.

```bash
# Install
npm install -g gitnexus
gitnexus init          # indexes current project
gitnexus trace <from-symbol> <to-symbol>   # shortest call path
gitnexus impact <symbol>                   # what would break
```

In Claude Code, the MCP tools fire automatically after `gitnexus init`.

## How to install / run it (Windows)
`npm install -g gitnexus` then `gitnexus init` in project root. Multi-branch indexing: `gitnexus init --branches main,dev`. Private GitHub: set `GITNEXUS_PAT` env var.

## Caveats / current state
Actively maintained, v1.6.8 as of June 2026. PDG-backed impact analysis is opt-in (`--pdg` flag) — adds significant indexing time but makes impact analysis accurate vs. heuristic. The trace BFS caps at 30 depth and 1000 visited nodes to avoid infinite loops in highly connected graphs; `truncated: true` in response means the search was cut short. The `api_impact` tool had a shape instability bug fixed in v1.6.8 — update before using.

**Verdict: yes** — install on any project over a few hundred files where cross-file navigation is a bottleneck. The `trace` and `impact` tools alone pay for the setup time.

## Connects to
- [[40_Resources/CS/Repos]]
