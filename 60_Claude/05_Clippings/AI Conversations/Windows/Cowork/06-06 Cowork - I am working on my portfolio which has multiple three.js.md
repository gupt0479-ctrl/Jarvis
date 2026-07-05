---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "I am working on my portfolio which has multiple three.js"
started_at: 2026-06-06T03:18:10
ended_at: 2026-06-06T03:22:59
project: Cowork
status: raw
session_id: a4609a00-003c-46f6-b7fe-5cb872bf100b
tags:
  - input
  - ai-conversation
  - claude-code
---

# I am working on my portfolio which has multiple three.js

## You

I am working on my portfolio which has multiple three.js components and cards that appear to be floating. Multiple things that need to work out but my ai agent's just can't seem to give me the result I desire. I want to add a crazy front end developer kit to claude or maybe cursor. Search the resources in my vault for this. I want to focus on front end development for producing three dimensional background and multiple cards that appear to be in space

## Claude

Your vault has everything I need. You have a Next.js 16 App Router + Three.js/R3F + Tailwind v4 + shadcn + Framer Motion stack, with a full cosmic UI refactor spec already documented. The problem is clear: agents don't know your component contracts, design tokens, or R3F patterns, so they guess wrong every time.

The fix is a three-file kit — a `CLAUDE.md` for Claude Code, a `.mdc` for Cursor rules, and a specialized `three-artist` agent. Let me build them.

Three files built from your vault's own spec. Here's where each one goes:

**`CLAUDE.md`** → drop at `ai-portfolio/CLAUDE.md` (repo root). Claude Code reads this automatically on every session. It encodes your full stack, the component contracts for `cosmic-card` and `float-btn`, all the R3F rules, forbidden actions, and the real Sanity content so the agent never hardcodes "Alex Morgan" again.

**`cosmic-frontend.mdc`** → goes at `ai-portfolio/.cursor/rules/cosmic-frontend.mdc`. Cursor picks this up via glob — it activates when you're in `three/`, `comet-card.tsx`, or `globals.css`. Has copy-paste recipes for float physics, particle sphere, elastic tether, the card CSS, and organic education blobs.

**`three-artist.md`** → goes at `ai-portfolio/.claude/agents/three-artist.md`. Invoke it in Claude Code with `@three-artist` when you need a focused 3D session. It has its own verification checklist so it doesn't hand you back untested Three.js.

The root cause of your agent failures is that they were working from zero context every time — guessing at your color tokens, card opacity rules, and whether to use raw Three.js or R3F. These files fix that permanently. The `CLAUDE.md` alone will eliminate most of the drift.

*Tools used: ToolSearch, TaskCreate, TaskUpdate, mcp__jarvis__search_simple, mcp__jarvis__vault_read, mcp__workspace__bash, Write, mcp__cowork__present_files*


