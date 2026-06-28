---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - ai-agent
  - context-engineering
  - claude-code
source_url: https://github.com/open-gsd/gsd-core
notes:
  - "[[40_Resources/CS/Repos]]"
---
# GSD Core

**GitHub:** [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | **Stars:** 5.3k | **Updated:** Jun 24, 2026 (v1.6.0)

## What it is
Context engineering and spec-driven development framework for Claude Code (and OpenCode, Gemini CLI, Cursor, etc.). Solves "context rot" — the quality degradation from a bloated context window — by running all heavy research, planning, and execution work in fresh-context subagents while keeping the main session lean.

The five-step phase loop: **Discuss → Plan → Execute → Verify → Ship.** Each phase writes structured artifacts (`STATE.md`, `CONTEXT.md`) that survive session boundaries.

## How Anant uses it
For Jarvis development phases (e.g., building a new ingestion pipeline, overhauling the trading project architecture): gsd-core adds discipline to multi-session Claude Code work. Instead of one long bloated session, each milestone repeats the phase loop with fresh subagents for the heavy work.

**The "other installations" question:** gsd-core is a workflow/prompting layer, not a competing runtime. It installs via `npx` and adds slash commands + CLAUDE.md files to your project. It sits alongside the existing Jarvis `.claude/` setup without conflict — you'd merge or configure it to complement existing skills. Most practically useful for new projects or major Jarvis rebuilds.

## How to install / run it (Windows)
Requires Node.js:
```bash
npx @opengsd/gsd-core@latest
# Prompts for: which runtime (select Claude Code), global vs local
```
Then in any project:
```
/gsd-new-project
```
MIT license. 161 contributors, actively maintained.

## Caveats / current state
- v1.6.0 released Jun 24, 2026 — very active development (28 releases total)
- npm package: `@opengsd/gsd-core`
- **Very useful?** Yes, for complex multi-phase projects. The context-rot problem is real in long Claude Code sessions. The answer to "how does it work with other installations": it adds its own `.claude/commands/` and `CLAUDE.md` entries — you merge these with existing Jarvis skills manually, or keep them project-scoped. Not a global system conflict.
- Works with Claude Code, OpenCode, Gemini CLI, Cursor, Windsurf, Copilot — multi-runtime is a key feature

## Connects to
[[40_Resources/CS/Repos]]
