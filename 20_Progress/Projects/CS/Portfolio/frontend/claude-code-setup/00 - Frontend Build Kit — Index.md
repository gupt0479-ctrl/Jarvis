---
type: project
status: active
created: 2026-06-12
updated: 2026-06-12
tags:
  - progress
  - portfolio
  - claude-setup
  - frontend
related_progress:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[00 - Claude Code Build Kit — Index]]"
notes:
  - "[[01 - Subagents & Existing .claude]]"
  - "[[02 - Commands, Hooks & CSP Fix]]"
  - "[[03 - Per-Phase Build Prompts]]"
  - "[[04 - Refinement Prerequisites & Deploy Checklist]]"
next: "Final refinement pass — read [[04 - Refinement Prerequisites & Deploy Checklist]], then run R0 from [[03 - Per-Phase Build Prompts]]. Ship after R8 green."
---
# Frontend Build Kit — Index
> **REFINEMENT PASS 2026-06-13.** The original build ran; the prompts are now the **R-phases (R0–R8)** in [[03 - Per-Phase Build Prompts]] — targeted fixes from `[[BUILD-STATUS]]` `## UI Fixes`, not a rebuild. Read note 10 + the graphify map (`../INDEX`, `../components`, `../data`) for exact paths. Key corrections: Projects & Education are **R3F** (drei `Float` / `MeshDistortMaterial`); **`skill.color` is added**; CSP stays last (R8, report-only first).

The operating kit that lets Claude Code (Sonnet 4.8) build the frontend overhaul from the design notes in `frontend/`, one phase per prompt, at minimum tokens. The design is the source of truth; this folder is *how the executor uses it*. Direct sibling of the chatbot's [[00 - Claude Code Build Kit — Index]] — same model, same discipline. Reuse what that kit already set up; this kit only adds what the visual rebuild needs.

## The model: design in the vault, build in WSL
The portfolio repo is in WSL; build it there (`cd repo` → `claude`). The plan is in this Windows vault. Claude Code reaches it two ways, preferring the first:
1. **Direct file read (preferred, zero network).** D: is mounted in WSL at `/mnt/d/`, so the notes are at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend/`. Read the one phase note you need.
2. **jarvis MCP (fallback).** Works, but mind the WSL→Windows localhost gotcha documented in the chatbot kit's [[01 - MCP Servers and the .mcp.json Fix]].

## How the build runs: refinement R-phases (R0–R8), one prompt each
One phase per session, clean context. The copy-paste prompts are in [[03 - Per-Phase Build Prompts]]. The loop every phase:
1. `/clear` for a clean context window.
2. Paste the phase prompt. It names note 10 + the *one or two* design notes to read — never all of them.
3. Claude Code reads only those, delegates to the right subagent, implements, runs `pnpm typecheck` + visual check.
4. **Anant commits** (Cowork/Claude Code must not commit or deploy). Next.

## Token strategy (same as the chatbot kit)
- **One phase, one clean context.** `/clear` between phases.
- **Read the leaf, not the tree.** Each prompt names the exact note path(s).
- **Delegate to subagents** so the main thread stays lean — see [[01 - Subagents & Existing .claude]].
- **Keep AGENTS.md thin** — stack conventions only; the plan is pulled per phase.
- **Commit per phase** so a bad phase rolls back cheaply.

## What to add to the existing `.claude` folder
The repo already has agents `frontend-builder, sanity-schema, security-reviewer, test-runner, three-artist` and commands `add-project, build-fix, deploy, e2e, performance, review, sanity-push, typecheck`. For this visual rebuild:
- **Subagents:** lean on `three-artist` (motion/three.js primitives), `frontend-builder` (section assembly), `sanity-schema` (the `skill`/`skillCategory` refactor). One optional new agent `motion-systems` if you want the comet/float primitives owned separately. Details in [[01 - Subagents & Existing .claude]].
- **Commands:** reuse `/sanity-push`, `/typecheck`, `/performance`, `/deploy`. Add nothing mandatory.
- **Hooks + the CSP fix:** keep Biome-on-edit and the typecheck Stop hook; **add the CSP header in `next.config.ts`** — the one open item flagged from the chatbot build that never shipped. Full config in [[02 - Commands, Hooks & CSP Fix]]. This is non-optional this round.
- **MCP servers:** `sanity` (for the content push) and the github MCP (to resolve real `githubUrl`s) must be live at the repo root `.mcp.json`. Reuse the chatbot kit's fix.

## Kit contents
- [[01 - Subagents & Existing .claude]] — which agent builds what; the one optional new agent.
- [[02 - Commands, Hooks & CSP Fix]] — reused commands, hook config, and the flagged CSP header for `next.config.ts`.
- [[03 - Per-Phase Build Prompts]] — the R0–R8 refinement prompts (ship-today pass).
- [[04 - Refinement Prerequisites & Deploy Checklist]] — packages, typegen, per-phase verification, and the final pre-deploy checklist.

## Current State
Kit drafted alongside the design notes. Needs user: confirm `.claude` agents exist, confirm `sanity` + `github` MCPs render at repo root, decide which certifications are real ([[09 - Sanity Content Spec]] §6), then run Phase 0.

## Next Action
Phase 0 — Sanity as source of truth (schema refactor + real content) from [[03 - Per-Phase Build Prompts]].

## Log
- **2026-06-12:** Built the frontend build kit mirroring the chatbot kit. Reused existing agents/commands; the only mandatory addition is the CSP header in `next.config.ts` (the flagged open item). Phased the build so Sanity-as-SoT and the motion primitives land before any section.
