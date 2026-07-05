---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - portfolio
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump from the AI portfolio repo, not synced to this vault"
---
# Portfolio — Claude Code Setup
A copy of the Claude Code config for Anant's AI portfolio site (Next.js 16 App Router, Tailwind v4, Sanity CMS, Three.js/R3F, an AI chatbot with a promptfoo eval suite). Previously an empty placeholder folder; re-exported with real content on 2026-07-05. Reference material only — not part of the Jarvis vault's own tooling.
## Files
### Agents
- [[20_Progress/AI/Claude Code/Portfolio/agents/ai-engineer|ai-engineer]] — chatbot server side: `/api/chat`, agent runtime loop, context engine, Gemini→Groq router
- [[20_Progress/AI/Claude Code/Portfolio/agents/eval-runner|eval-runner]] — promptfoo eval suite (grounding/refusal/tool-correctness/injection/fail-safe)
- [[20_Progress/AI/Claude Code/Portfolio/agents/frontend-builder|frontend-builder]] — Next.js/React UI, shadcn/Radix, Framer Motion, PortfolioLab panel
- [[20_Progress/AI/Claude Code/Portfolio/agents/sanity-schema|sanity-schema]] — GROQ query advisor + `localContent.ts` fallback (does not touch schema files)
- [[20_Progress/AI/Claude Code/Portfolio/agents/security-reviewer|security-reviewer]] — pre-deploy security gate, reports only
- [[20_Progress/AI/Claude Code/Portfolio/agents/test-runner|test-runner]] — Vitest specialist
- [[20_Progress/AI/Claude Code/Portfolio/agents/three-artist|three-artist]] — Three.js/R3F specialist (particle sphere, float physics, ObsidianBackground)
### Commands
- [[20_Progress/AI/Claude Code/Portfolio/commands/add-project|add-project]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/build-fix|build-fix]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/deploy|deploy]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/e2e|e2e]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/eval|eval]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/performance|performance]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/review|review]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/sanity-push|sanity-push]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/ship-check|ship-check]]
- [[20_Progress/AI/Claude Code/Portfolio/commands/typecheck|typecheck]]
### Docs
- [[20_Progress/AI/Claude Code/Portfolio/CLAUDE|CLAUDE]] — stack, visual identity, and hard rules primer for the repo root
- [[20_Progress/AI/Claude Code/Portfolio/docs/ecc-setup-guide|docs/ecc-setup-guide]] — Everything Claude Code setup notes for this project
- [[20_Progress/AI/Claude Code/Portfolio/docs/ORBY|docs/ORBY]] — "Orby" scroll-companion concept doc
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/Portfolio"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `cosmic-frontend.mdc` — a **Cursor** rule file (`.mdc`, not Claude Code), scoped to `src/components/**/*.tsx` and globals.css. Its presence here means this dump mixes both tools' configs in one folder.
- `scheduled_tasks.lock` — Claude Code scheduled-task lock file.
- `settings.local.json` — local Claude Code permission overrides.
## Status & Gaps
This folder was empty (dead) as of the first pass on 2026-07-05 and has since been re-exported with the project's actual `.claude/` contents. No live equivalent exists in this vault to diff against, so every markdown file is marked `static`. Worth noting: `cosmic-frontend.mdc` is a Cursor artifact sitting inside a Claude Code dump — likely copied because the two tools' config folders were merged during export, not a filing mistake worth fixing here.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
