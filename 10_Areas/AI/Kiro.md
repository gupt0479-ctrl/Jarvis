---
type: evergreen
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - ai
  - tool-guide
  - kiro
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
next: "Decide whether Jarvis needs Kiro at all beyond the two steering files — if yes, add a workspace agent JSON mounting the vault canon like resq.json does; if no, note it and stop maintaining the duplicate"
---
# Kiro
Kiro is the spec-driven surface: steering files that auto-load per project, formal specs with phases, JSON-defined hooks that fire on agent events, and workspace agents declared as JSON with explicit resource mounts. Where Claude Code is conversational and Cursor is editor-native, Kiro is contract-first — you write the product rules down before the agent moves, and hooks enforce them mid-flight. It earns its keep on projects with protected paths, deploy gates, and multi-tool coordination; it's overhead on exploratory work.
Setups are snapshotted in `20_Progress/AI/Kiro/` (Assisto, OpsPilot, Portfolio, Resq, SafeReach, TradingView, WSL Home).
## The Kiro building blocks, as actually used
- **Steering** (`.kiro/steering/*.md`, `inclusion: auto` frontmatter) — always-loaded project rules. Assisto's `project-rules.md` is the best example: repo layout, git conventions (primary remote, working branch `Anant`, never force-push), tech stack with explicit exclusions ("No Strapi, no external CMS, no Lovable code"), and protected paths the agent may not edit unless scoped.
- **Specs** (`.kiro/specs/`) — phase-gated build plans. Assisto's `assisto-spend-backend` spec pairs with steering that says all new product work goes in the spend module.
- **Hooks** — two flavors: `.kiro.hook` JSON descriptors (Assisto: backend-preflight, final-report-checklist, supabase-safety-check) and shell scripts wired through the agent JSON (Resq: `canon-gate.sh` on agentSpawn *and* userPromptSubmit — the agent literally cannot start or take a prompt without the canon check passing).
- **Workspace agents** (`agents/*.json`) — Resq's `resq.json` is the reference: `resources` mounts the `.claude/` canon files (`file://.claude/PRD.md`, playbooks, checklists) plus `skill://.kiro/skills/**/SKILL.md`, a `welcomeMessage` that orders the first read, and per-event hooks with matchers. This is the cross-tool pattern worth stealing: Kiro consumes the same canon Claude Code maintains.
## Per-project state
| Project | What's there | Notes |
| --- | --- | --- |
| Resq | agent JSON + 4 hook sets (canon-gate, demo-safety, secret-hygiene, finance-guard) + mcp.json | The hero Kiro project. "Protect deterministic finance truth" — finance math never moves into AI output. |
| Assisto | 5 steering files + 3 hooks + spend-backend spec + mcp.json | Enterprise spend module build; steering carries migration-recovery warnings for Supabase. |
| Portfolio | 2 steering (orby-system, portfolio-v1) + mcp.json + specs | Lighter — Cursor and Codex do most Portfolio work. |
| SafeReach | context + hooks + steering | Coordinates with Cursor via `kiro-cursor-contract.md` on the Cursor side. |
| TradingView | specs only | Kiro tasks 7.2–7.4 and 9–13 are open (see 2026-06-25 session log). |
| OpsPilot | supabase skills | Skill-only usage. |
## Jarvis's own `.kiro/`
Two steering files (`workspace-context.md`, `human-writing.md`) plus `settings/mcp.json`. Same drift problem as the Cursor rules: they restate what `AGENTS.md` and `HUMAN_WRITING.md` own. Security note: an exposed Obsidian API key was committed in `.kiro/settings/mcp.json` and removed in commit `b8604279` — keep credentials out of tool config that gets committed; the write guard now denies `.kiro/` writes entirely.
## When to use Kiro vs the others
- Product build with protected paths and phase gates → Kiro (steering + specs + hooks).
- The repo already has a `.claude/` canon → Kiro agent JSON mounting it, not a parallel context layer.
- Vault work, agentic multi-file changes, research → Claude Code. Kiro's event hooks add nothing to note-writing that the vault's own PreToolUse guard doesn't already do.
- In-editor refinement → Cursor.
## Gaps
1. Jarvis `.kiro/` duplicates vault authority files and has no workspace agent — it's a stub that costs maintenance without providing enforcement. Decide: build it out (agent JSON + canon mounts) or freeze it.
2. TradingView has open Kiro task numbers (7.2–7.4, 9–13) that nothing surfaces — they live in the spec, invisible to the dashboard.
3. Hook scripts are per-project copies; secret-hygiene and canon-gate patterns from Resq would apply to Assisto and SafeReach nearly verbatim but aren't shared.
