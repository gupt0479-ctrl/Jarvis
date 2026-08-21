---
type: index
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - moc
  - claude-kit
  - toolkit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/How to Use Commands]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/How to Use Hooks]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/What MCPs]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/How to Use Global]]"
next: Build out 60_Claude/30_Reviews/AI/ as the review-system counterpart to this catalog
---
# Claude Kit Toolkit
==This folder answers one question in real time: mid-session, which promoted agent, command, hook, MCP, or skill actually closes the task in front of you, and where is the concrete "how" for it?==
## Purpose
The Toolkit is the reference layer between [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map.md]] (which tracks pipeline *stage* — sandbox, tested-tools, promoted) and an actual working session. Tool Map answers "is this tool trustworthy yet"; the Toolkit answers "given a real task right now, what do I actually type." Read this before starting any non-trivial Claude Code session that touches agents, commands, hooks, MCPs, or skills.
## Map
Six categories, each with two notes and a fixed job split. `What {Category}.md` is a ground-truth inventory — split into what second-brain-claudekit itself has promoted into its own `.claude/` ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents|example]]) and what is actually live in Jarvis's real vault-root `.claude/` right now, verified against the files on disk, not against a stale snapshot. `How to Use {Category}.md` is the dispatch note — a `# Claude Kit` section giving project-agnostic usage guidance per promoted claudekit tool, and a `# Particular Use` section of named-use-case anchors ("code review," "vault curation," "learning drills") that the use-case notes below link straight into.
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents|What Agents]] and [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents|How to Use Agents]] cover sub-agents — long-running, focused personas invoked via the Agent/Task tool. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands|What Commands]] and its pair cover `/slash-commands` — the trigger layer, one command per skill in most cases. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks|What Hooks]] and its pair cover lifecycle automation (PreToolUse/PostToolUse/SessionStart/SessionEnd/Stop) — the layer that runs without being asked. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/What MCPs|What MCPs]] and its pair cover Model Context Protocol servers — external tool access beyond the filesystem. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills|What Skills]] and its pair cover the actual logic behind each command — `SKILL.md` files and directory skills, plus [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/Github Skills|Github Skills]], the one pre-existing note in this folder that was already real and stays as-is. **[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global|What Global]]** and its pair (added 2026-08-20) cover the sixth, orthogonal scope: the two Claude Code **home directories** (`~/.claude` on WSL, `C:\Users\Anant Gupta\.claude` on Windows), available in every session regardless of which project is open — a different axis from the other five, which are all project-scoped (either second-brain-claudekit's own `.claude/` or Jarvis's vault-root `.claude/`).
Below the category pairs, this folder holds one shared set of use-case notes — [[Research & Distillation]], [[Vault Curation]], [[Writing Quality]], [[Decision & Planning]], [[Learning & Mastery]], [[Career Ops]], [[Daily Operations]] — each a short summary that cross-links into whichever category notes' `# Particular Use` anchors actually serve that task. [[Code Review]] and [[Frontend]] exist too, honestly flagged as **not yet served** — the tools that would close them (mattpocock-skills' `code-review`, gstack's design-review workflow) are still at `sandbox`/`tested-tools` stage per Tool Map, not promoted.
## Status
| Category | Promoted in claudekit | Live in Jarvis | Use cases served |
|---|---|---|---|
| Agents | 3 (vault-curator, research-distiller, weekly-reviewer) | 5 (adds anti-slop-editor, learning-agent, career-operator) | Vault Curation, Research & Distillation, Writing Quality, Learning & Mastery, Career Ops |
| Commands | 11 | 19 | Daily Operations, Decision & Planning |
| Hooks | 2, both wired | 2 registered, 1 actually active — session-continuity hook exists on disk, unregistered in `settings.json` | — |
| MCPs | 0 promoted (GBrain is the closest, still sandbox stage) | 6 (`obsidian`, `filesystem`, `git`, `fetch`, `jarvis-memory`, `excalidraw`) | Vault Curation, Daily Operations |
| Skills | 0 (claudekit's own `skills/` is empty) | ~19 directory/file skills | most of the above |
| Global | n/a — this axis is machine-scoped, not project-scoped | WSL home: 3 agents, 7 commands, 3 hooks, 28 skills, all real, some stale-path. Windows home: 0 agents, 0 commands, 0 hooks, 1 real skill (`export-ai-session`) | Daily Operations, Vault Curation (both as documented fallbacks, not primary) |
## Dataview
```dataview
TABLE type, status, updated
FROM "20_Progress/Projects/AI Use/Claude Kit/Toolkit"
SORT file.folder ASC, file.name ASC
```
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] for pipeline stage. [[10_Areas/AI/Setup/Review System]] for how usage of everything catalogued here gets reviewed on a cadence. [[10_Areas/AI/Setup/Folder Map]] for where this folder sits in the wider AI-tooling layer.
