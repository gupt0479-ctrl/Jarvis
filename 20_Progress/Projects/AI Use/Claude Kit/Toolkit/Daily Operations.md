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
next:
---
# Daily Operations
==Opening and closing a working day, and the maintenance tasks that ride along — the one use case where a hook was supposed to remove the need to type a command at all, and currently does not.==
Run `/startday` to open — reads plans and session history, fills the daily note. Work the day. Run `/closeday` to close — verifies completions, writes the scorecard. Run `/ops` for vault health operations outside the daily cadence, and `/tag-month` when a completed month is missing its checkpoint git tag. `/context` loads the manifest, dashboard, and session-log tail before any of the above, if picking up cold. See [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/What Hooks]] for why this is currently manual every time rather than triggered by `SessionStart`/`SessionEnd`.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]]
