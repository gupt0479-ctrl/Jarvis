---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - safereach
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "none — external hackathon project dump, most complete reference architecture across all four platforms"
---
# SafeReach — Cursor Setup
A copy of the Cursor config for SafeReach, a disaster-response hackathon app (React + TypeScript + Vite, browser-only, no backend). This is the richest Cursor dump across all platform folders — 7 lifecycle hooks plus 8 skills, all locked to a shared PRD/deployment-guide context that Kiro also reads (see `integrations/kiro-cursor-contract.md`). Reference material, not part of this vault's own tooling.
## Files
### Skills
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-context-lock/SKILL|skills/safereach-context-lock/SKILL]] — loads the locked shared context; required first step before any other SafeReach skill
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-accessibility-reviewer/SKILL|skills/safereach-accessibility-reviewer/SKILL]] — crisis-accessibility review (48px targets, no color-only signals, SOS visibility)
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-agent-boundary-reviewer/SKILL|skills/safereach-agent-boundary-reviewer/SKILL]] — enforces the Cursor/Kiro division of labor
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-demo-guardian/SKILL|skills/safereach-demo-guardian/SKILL]] — protects the P0 hackathon demo flow
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-deploy-readiness/SKILL|skills/safereach-deploy-readiness/SKILL]] — local + live deployment verification gate
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-life-safety-guardrails/SKILL|skills/safereach-life-safety-guardrails/SKILL]] — guards non-negotiable safety invariants (backup-power hard rejection, SOS packet completeness)
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-refactor-agent/SKILL|skills/safereach-refactor-agent/SKILL]] — behavior-preserving React/TypeScript refactor scope and red flags
- [[20_Progress/AI/Cursor/SafeReach/skills/safereach-ui-specialist/SKILL|skills/safereach-ui-specialist/SKILL]] — UI requirements for the 4-tab app (Map/Shelter/S.O.S/Profile)
### Docs
- [[20_Progress/AI/Cursor/SafeReach/integrations/kiro-cursor-contract|integrations/kiro-cursor-contract]] — the one-time Cursor/Kiro collaboration contract: locked shared context, role split, routing rule, handoff payload shape
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/SafeReach"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `hooks.json` — hook registration wiring the 7 lifecycle hooks below.
- `hooks/safereach-context-bootstrap.js` — loads shared context at session start.
- `hooks/safereach-edit-review.js` — post-edit review hook.
- `hooks/safereach-prompt-context-gate.js` — gates prompts on context being loaded.
- `hooks/safereach-read-context-audit.js` — audits that context files were actually read.
- `hooks/safereach-shell-safety.js` — shell command safety guard.
- `hooks/safereach-stop-reminder.js` — session-stop reminder hook.
- `hooks/safereach-subagent-boundary.js` — enforces the Cursor/Kiro boundary at the hook level (code-level counterpart to `skills/safereach-agent-boundary-reviewer`).
- `integrations/agent-coordination.schema.json` — JSON schema for the `AgentCoordinationState`/`AgentHandoff` shapes described in `kiro-cursor-contract.md`.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every file marked `static`. Compare against [[20_Progress/AI/Kiro/SafeReach/Setup|SafeReach's Kiro dump]], which shares the same PRD/deployment-guide context per `kiro-cursor-contract.md` — the two platforms are designed to be read together, not independently. This is the most mature multi-agent handoff architecture across all Cursor/Kiro/Codex dumps in this vault; worth revisiting as a pattern if this vault ever needs Claude Code ↔ another tool coordination.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
