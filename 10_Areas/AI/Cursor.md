---
type: evergreen
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - ai
  - tool-guide
  - cursor
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
next: "Port the SafeReach hook lifecycle pattern (context bootstrap → prompt gate → edit review → shell safety) to the Portfolio and CausalOps Cursor setups"
---
# Cursor
Cursor is the code-first surface: an IDE with LSP diagnostics, inline edits, and rules that load automatically per file glob. Use it when the work is *inside one repo and benefits from seeing squiggles* — type errors surfacing as you edit, jump-to-definition while reasoning about a change, tight edit-run loops. Use [[10_Areas/AI/Claude Code|Claude Code]] instead when the work is agentic — multi-file campaigns, skills, subagents, anything touching the vault. The practical split that has emerged across projects: Claude Code plans and builds, Cursor refines and verifies in-editor.
Setups are snapshotted in `20_Progress/AI/Cursor/` (CausalOps, DNA App, OpsPilot, Portfolio, SafeReach, Trading View, plus WSL/Windows home dumps). DNA App and Trading View dumps are empty — nothing catalogued there yet.
## Jarvis — the 5 rules files (`.cursor/rules/`)
| File | Scope | Job |
| --- | --- | --- |
| `workspace-context.mdc` | alwaysApply | Vault routing, folder structure, Write Contract |
| `human-writing.mdc` | alwaysApply | Voice standard — mirrors [[HUMAN_WRITING]] |
| `vault-behavior.mdc` | alwaysApply | Pre-flight reads, frontmatter schema, placement, quality gate |
| `note-creation.mdc` | `**/*.md` | Per-note formatting and plugin integration (SR markers, Tasks) |
| `plugin-rules.mdc` | alwaysApply | When to use each Obsidian plugin |
These duplicate content whose authority lives in the vault ([[Jarvis OS — North Star]] Part 4's one-fact-one-home rule): they should shrink to pointers at `AGENTS.md`/`HUMAN_WRITING.md` rather than restating them. Right now a rule change in the vault requires a second edit in `.cursor/rules/` or the two drift.
## CausalOps (HiveMind)
- `rules/hivemind-core.mdc` (alwaysApply) — the evidence guardrail: LLMs may propose hypotheses, memos, causal graphs, and measurement plans, but must not invent estimator rows or treat generated narrative as empirical evidence. This one rule is what keeps a causal-inference engine honest when an LLM is in the loop.
- `hooks.json` + `hooks/preflight.sh` — preflight check before work starts.
- Skills: `hivemind-project` (project onboarding) and `persistent-semantic-memory` (memory layer work).
- Working rules mirror the repo's `AGENTS.md`: smallest verification command, typed Pydantic contracts over loose dicts, never write generated data into git, don't touch `.kiro/` unless asked.
## Portfolio
- Agents: `portfolio-cms`, `portfolio-polish`, `portfolio-verify` — a build/refine/check trio.
- Command: `portfolio-guide`. Rules: `Portfolio-Main-Rules.mdc`.
- Skills: `portfolio-completion`, `portfolio-content-cms`, `portfolio-ui-polish`.
- Divides labor with Claude Code (WSL) which ran the R0–R8 refinement phases, and with Codex which carries the migrated `/deploy`-style gates.
## SafeReach — the reference hook architecture
SafeReach has the most complete Cursor hook lifecycle of any project; treat it as the template:
| Hook event | Script | Purpose |
| --- | --- | --- |
| sessionStart | `safereach-context-bootstrap.js` | Load project canon before anything runs |
| beforeSubmitPrompt | `safereach-prompt-context-gate.js` | Block prompts that skip required context |
| beforeReadFile | `safereach-read-context-audit.js` | Audit what the agent reads |
| postToolUse (Write/Edit/ApplyPatch) | `safereach-edit-review.js` | Review every edit after it lands |
| beforeShellExecution | `safereach-shell-safety.js` | Gate dangerous commands |
| stop | `safereach-stop-reminder.js` | End-of-turn checklist |
| subagent boundary | `safereach-subagent-boundary.js` | Keep subagents inside their lane |
All run with `failClosed: false` and 5s timeouts — advisory guardrails, not hard blocks. Skills (8): accessibility-reviewer, agent-boundary-reviewer, context-lock, demo-guardian, deploy-readiness, life-safety-guardrails, refactor-agent, ui-specialist. `integrations/kiro-cursor-contract.md` + `agent-coordination.schema.json` define how Cursor and Kiro hand off on the same repo — the only written cross-tool contract in any project so far.
## OpsPilot
Just a `settings.json`. The real OpsPilot setup lives in its `.claude/` canon (playbooks, checklists) and Kiro/Codex skills — Cursor is a thin client there.
## Gaps
1. Vault rules duplicate vault authority files instead of pointing at them — drift risk on every vault-rule change.
2. The SafeReach hook lifecycle exists in exactly one project; Portfolio and CausalOps have one hook or none. Porting the bootstrap → gate → review → safety chain is cheap and catches the same failure classes everywhere.
3. DNA App and Trading View Cursor dumps are empty — either the projects don't use Cursor (fine, note it) or the export was missed.
4. No Cursor setup reads the shared `AI_CONTEXT.md` manifest at session start the way Claude Code's SessionStart hook does — each repo bootstraps its own context or none.
