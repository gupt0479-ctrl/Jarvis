---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - use-case
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/How to Use Commands]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/How to Use Global]]"
next:
---
# Daily Operations
==Opening and closing a working day, and the maintenance tasks that ride along — the one use case where a hook was supposed to remove the need to type a command at all, and currently does not.==
Run `/startday` to open — reads plans and session history, fills the daily note. Work the day. Run `/closeday` to close — verifies completions, writes the scorecard. Run `/ops` for vault health operations outside the daily cadence, and `/tag-month` when a completed month is missing its checkpoint git tag. `/context` loads the manifest, dashboard, and session-log tail before any of the above, if picking up cold. See [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks]] for why this is currently manual every time rather than triggered by `SessionStart`/`SessionEnd`.
**A WSL-global alternative exists and is currently not preferred:** the WSL home directory's own `/obsidian-daily-review`, `/obsidian-session-review`, and `/second-brain-*` command lifecycle ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global|What Global]]) predates `/startday`/`/closeday` and covers similar ground, but its instructions still point at pre-reorg paths (`10_UMN/`, `00_Inbox/Headway/`) that no longer exist in this vault, while `/startday`/`/closeday`/`/context` are written against the vault's current structure and read the live dashboard and session log directly. Reach for the global commands only in a different WSL project that has no vault-specific skills of its own.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global]]
