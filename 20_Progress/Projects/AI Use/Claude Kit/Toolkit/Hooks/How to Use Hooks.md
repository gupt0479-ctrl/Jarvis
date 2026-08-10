---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - hooks
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks]]"
next:
---
# How to Use Hooks
==A hook is for anything that must happen without being asked — every other layer in this Toolkit (agents, commands, skills) requires an explicit invocation.==
# Claude Kit
Both of second-brain-claudekit's promoted hooks fire automatically inside that repo only — nothing to invoke, nothing to type. Use `after-edit-log.ps1`'s output (`60_Claude/Sessions/_today-edits.md`) to reconstruct what happened in a session without re-reading the whole transcript. Treat `session-wrapup.ps1`'s reminder as a real gate — running `/compress` is a manual step it only nudges, never forces.
# Particular Use
No `# Particular Use` entries yet — Jarvis currently has exactly one live hook (`jarvis-write-guard.ps1`, a permission gate, not a task-specific automation) and one unregistered one. Nothing here maps onto a named use case like the other four categories do until the session-continuity hook is actually wired, or a new hook is promoted from claudekit's own pipeline.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks]] for exactly what is and is not currently active.
