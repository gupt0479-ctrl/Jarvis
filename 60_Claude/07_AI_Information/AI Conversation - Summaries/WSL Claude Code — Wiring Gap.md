---
type: input
status: sprout
created: 2026-07-29
tags:
  - ai-conversations
  - wsl
  - infrastructure
notes:
  - "[[60_Claude/05_Clippings/AI Conversations/README]]"
  - "[[export-ai-session]]"
---
# WSL Claude Code — Wiring Gap
**This mostly already exists — the ask this session was answered by finding the real gap, not by designing something new.** `60_Claude/05_Clippings/AI Conversations/README.md` already documents the exact pipeline asked for: a `SessionEnd` hook (`jarvis-session-continuity.ps1`, registered in Windows' `~/.claude/settings.json`) automatically mirrors every Claude Code session's raw JSONL (zero token cost, NTFS junction to `~/.claude/projects`) and writes a cleaned per-session archive note, and the global `/export-ai-session` skill already does exactly the "crucial/important sessions only, ask before distilling" job into `60_Claude/07_AI_Information/AI Conversation - Summaries/` — the folder named in the original ask. This is not a proposal; it runs today, for Windows Claude Code and Cowork.
## The actual gap, confirmed by direct inspection
Two folders already exist as scaffolds, confirmed empty, both documented in the README as "not wired":
- `60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/` — WSL runs a completely separate Claude Code instance with its own `~/.claude/projects` session storage and its own `~/.claude/settings.json`. That settings file has its own `SessionEnd`/hook wiring (`after-edit-log.ps1`, `session-wrapup.ps1` via `pwsh`) but **not** `jarvis-session-continuity.ps1` — WSL sessions currently vanish with no vault trace at all.
- `60_Claude/05_Clippings/AI Conversations/Claude App/` — the Claude.ai desktop/web app, cloud-based. There's no official local session-export mechanism for this the way Claude Code writes JSONL to disk — this is very likely not buildable at zero cost right now, not a wiring gap like the other two. Leave it as a manual-paste folder until Anthropic ships something exportable; don't promise automation here that doesn't exist.
## The real fix (scoped to Claude Code only, per this session's instruction)
WSL's `settings.json` already calls `pwsh` for its existing hooks, which confirms the mechanism works cross-boundary — this is a real, buildable addition, not a redesign:
1. Adapt `jarvis-session-continuity.ps1` for WSL: read from WSL's own `~/.claude/projects` (Linux paths, not `~/.claude/projects` under Windows profile — they're two separate trees), write into `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/` (WSL can reach the Windows filesystem directly via `/mnt/d/...`, confirmed).
2. Register it as a **third** `SessionEnd` hook entry in WSL's `~/.claude/settings.json`, alongside the two already there — don't replace `after-edit-log.ps1` or `session-wrapup.ps1`.
3. Reuse `/export-ai-session` unmodified for the distillation step (Step 2 onward in that skill already just reads whatever raw notes exist in `AI Conversations/Windows/Claude Code/` and `.../Cowork/` — extend its candidate search to also scan `.../WSL/Claude Code/`).
**Not done this session** — this is the concrete next build, not yet executed. The script adaptation and the settings.json edit are real work, correctly scoped as its own task rather than rushed here.
