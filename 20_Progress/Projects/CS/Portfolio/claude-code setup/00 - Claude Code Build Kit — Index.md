---
type: project
status: active
created: 2026-06-10
updated: 2026-06-10
tags:
  - progress
  - portfolio
  - claude-setup
related_progress:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
  - "[[00 - AI Setup — Index & Integration Guide]]"
notes:
  - "[[01 - MCP Servers and the .mcp.json Fix]]"
  - "[[02 - Subagents]]"
  - "[[03 - Commands and Hooks]]"
  - "[[04 - Eval Harness — promptfoo]]"
  - "[[05 - Per-Phase Build Prompts]]"
next: "Fix .mcp.json (Sanity + Clerk + jarvis) per [[01 - MCP Servers and the .mcp.json Fix]], then run Phase 0 prompt from [[05 - Per-Phase Build Prompts]]."
---
# Claude Code Build Kit — Index
This folder is the operating kit that lets Claude Code (Sonnet 4.8) build the nextgen chatbot from the design notes, one phase per prompt, with minimum tokens. The design lives in `nextgen-chatbot/`; this folder is *how the executor uses it*. The design notes are the source of truth — Claude Code reads them, it does not re-derive them.
## The model: design in the vault, build in WSL
The portfolio repo is in WSL; build it there with Claude Code in the terminal (`cd repo` → `claude`). The plan is in this Windows vault. Claude Code reaches the plan two ways, in order of preference:
1. **Direct file read (preferred, zero network, fewest tokens).** The D: drive is mounted in WSL at `/mnt/d/`, so the notes are readable at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot/`. Claude Code `Read`s the one phase note it needs. No MCP round-trip.
2. **jarvis MCP (fallback).** If you'd rather query by note, the jarvis MCP works — but note the WSL→Windows localhost gotcha in [[01 - MCP Servers and the .mcp.json Fix]].
Prefer the direct read: it is faster, cheaper, and has no networking failure mode.
## How the build runs: 8 prompts, 8 phases
One phase per session, mapped to [[08 - Build Phases & Milestones]]. The eight copy-paste prompts are in [[05 - Per-Phase Build Prompts]]. The loop for every phase is the same:
1. `/clear` to start the phase with a clean context window.
2. Paste the phase prompt. It points Claude Code at the *one* phase note path and its 1–2 dependency notes — never the whole note set.
3. Claude Code reads only those notes, implements, then runs `/eval` and `/typecheck`.
4. Commit the phase. Move to the next.
## Token strategy (Sonnet 4.8 at max efficiency)
The waste in agentic builds is context bloat. This kit fights it:
- **One phase, one clean context.** `/clear` between phases so phase 6 is not dragging phase 1's tokens.
- **Read the leaf, not the tree.** Each prompt names the exact note path(s). Claude Code reads that note, not the index, not all nine.
- **Delegate to subagents.** Heavy implementation (UI, Sanity schema, security pass, eval run) goes to subagents in [[02 - Subagents]] — each has its own context window, so the main thread stays lean.
- **Keep AGENTS.md thin.** The repo's `AGENTS.md` holds stack conventions only; the detailed plan stays in the vault and is pulled per phase. A fat AGENTS.md is paid on every turn.
- **Commit per phase** so a bad phase rolls back cheaply without re-running good ones.
## What to add to the existing .claude folder
Your current `.claude/` (from the screenshot) has agents `frontend-builder, sanity-schema, security-reviewer, test-runner, three-artist` and commands `add-project, build-fix, deploy, e2e, performance, review, sanity-push, typecheck`. For this build, add:
- **2 subagents:** `ai-engineer` (the API route, agent runtime loop, context engine, grounding, tools, model router) and `eval-runner` (promptfoo). Full definitions in [[02 - Subagents]].
- **1 command:** `/eval` (run the promptfoo suite). Optional `/ship-check` (pre-deploy gate). See [[03 - Commands and Hooks]].
- **Hooks:** keep Biome-on-edit and a typecheck Stop hook; add a deploy-time promptfoo gate. Do **not** tie the AI evals to a Vitest Stop hook — they cost tokens and time; run them via `/eval` and CI instead. See [[03 - Commands and Hooks]].
- **MCP servers:** add `jarvis` (or use direct reads), `sanity`, `clerk`, and `upstash` to a correct `.mcp.json` at the **repo root**. The current `mcp.json` not rendering is almost certainly location + missing env credentials — fixed in [[01 - MCP Servers and the .mcp.json Fix]].
- **Plugins:** the "everything-claude-code" plugin you already installed covers the rest; nothing else required for v1.
## Kit contents
- [[01 - MCP Servers and the .mcp.json Fix]] — the working `.mcp.json`, the Sanity/Clerk/jarvis fix, env vars, WSL gotcha.
- [[02 - Subagents]] — the two new agents, full definitions, and how the existing five are used.
- [[03 - Commands and Hooks]] — `/eval`, the hook config, what to gate where.
- [[04 - Eval Harness — promptfoo]] — config, test file, judge rubric, CI gate.
- [[05 - Per-Phase Build Prompts]] — the eight copy-paste prompts.
## Current State
Kit drafted. Needs user: fix `.mcp.json` (Sanity + Clerk render), confirm direct-read path resolves in WSL, then run Phase 0.
## Next Action
Fix `.mcp.json` per [[01 - MCP Servers and the .mcp.json Fix]], then run the Phase 0 prompt from [[05 - Per-Phase Build Prompts]].
## Log
- **2026-06-10:** Built the Claude Code operating kit alongside the locked design notes. Chose direct `/mnt/d` reads over jarvis MCP for token efficiency, promptfoo over Vitest for AI evals, two new subagents, one new command.
