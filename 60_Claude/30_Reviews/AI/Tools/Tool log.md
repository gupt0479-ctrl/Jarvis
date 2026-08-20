---
type: dashboard
status: active
created: 2026-08-11
updated: 2026-08-20
tags:
  - claude-code
  - tool-log
  - skill-use
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code]]"
next: Add a row every time /export-ai-session reviews a session — the ad-hoc/multiple convention (added 2026-08-20) covers sessions without one clean slash-command name; watch whether that convention holds up once more rows land
---
# Tool log
==Every row is one skill or command's use in one session — one skill invoked twice in a session earns two rows — appended by /export-ai-session, never hand-edited into a different shape.==
## Purpose
This is the per-use record of Claude Code skills, commands, and agents across both Windows and WSL sessions — Claude Code only for now, per the same scope [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code|Toolkit/Claude Code.md]] tracks. It answers "when was this skill last used, on what, and what happened" without opening every raw session note in `60_Claude/05_Clippings/AI Conversations/`. A future review pass (weekly/monthly, or a claudekit session deciding what to improve) reads this file first, the raw notes only when a specific row needs more depth.
Filed under `60_Claude/30_Reviews/AI/Tools/`, not `05_Clippings/`, on purpose — this is a derived, continuously-updated index built from raw captures, not a raw capture itself, and `05_Clippings` is read-only after capture per the vault's Write Contract (`AGENTS.md`). An empty placeholder was originally created at `60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Tool log.md`; this file is the real one, and that placeholder should be deleted rather than mistaken for it.
## Row shape
| Date | Project | Skill/Command | What It Did | Outcome | Source |
|---|---|---|---|---|---|
| YYYY-MM-DD | project name from the raw note's frontmatter | `/skill-name` or agent name | one clause, concrete | clean / partial / failed, one clause why if not clean | `[[raw session note]]` |
`Outcome` is never left blank — "clean" still gets written, not omitted. `Source` links the raw session note (`Windows/Claude Code/<project>/...` or `WSL/Claude Code/<project>/...`), not the distilled summary — the summary may not exist for every session that gets a Tool log row, since `/export-ai-session` logs every reviewed session here regardless of whether it was distilled.
**`Skill/Command` when there is no single clean value (added 2026-08-20, found necessary the first time this log got a real row):** a real session frequently doesn't route through one nameable slash command. Two explicit values cover this rather than leaving the column blank or forcing a fake name:
- **`ad-hoc`** — the session invoked no registered skill/command at all (a freeform task worked directly in the main thread). Name what it actually did in `What It Did` instead — that column carries the specificity this one can't.
- **`multiple`** — the session invoked more than one registered skill/command. Name every one actually used in `What It Did` (e.g. "ran `/startday` then `/note-to-actions`"); do not pick just one to represent the row.
One row is still written per session in either case — `ad-hoc`/`multiple` describes the session's shape, it doesn't multiply into several rows the way one skill used twice in a session does.
## Log
| Date | Project | Skill/Command | What It Did | Outcome | Source |
|---|---|---|---|---|---|
| 2026-08-19 | Jarvis | ad-hoc | Re-verified second-brain-claudekit's real repo state via direct WSL access (not the Windows mirror) and patched 7 Jarvis tracking notes (Tool Map, Log, What Agents/Commands/Hooks, Folder Map, Notes Map, Claude Code.md) to match — no registered skill/command invoked | partial — verification was thorough for prompt-flagged leads but missed one unflagged claim (a fake `docs/<Project>/` staging folder) baked into the task prompt's own framing, caught by the next day's adversarial review | `[[60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-19 Second-brain-claudekit Jarvis notes sync]]` |
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code]] for the wider Toolkit this log feeds. `C:\Users\Anant Gupta\.claude\skills\export-ai-session\SKILL.md` for the skill that writes rows here.
