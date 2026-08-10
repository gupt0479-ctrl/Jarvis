---
type: evergreen
status: seed
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - use-case
  - not-yet-served
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/Github Skills]]"
next: Re-check once mattpocock-skills' engineering category or gstack individually clears Promotion-Criteria.md's bar
---
# Code Review
==Not yet served by anything promoted — this note exists so the gap is named instead of silently absent from the Toolkit.==
No agent, command, hook, or skill in either "Live in Jarvis" or "Promoted in claudekit" currently does automated code review. The two real candidates are stuck earlier in the pipeline: mattpocock-skills' `code-review` skill sits in `tested-tools/skills/mattpocock-engineering/`, one of 17 skills copied for review, not yet individually tested against [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map]]'s Promotion-Criteria; gstack's `/review` and `/plan-eng-review` are blocked entirely behind gstack's missing-Chromium-libs issue. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/Github Skills|Github Skills]] already has a narrative recommendation on both. Until one clears, the closest available Jarvis-native tools are `/simplify` and Claude Code's own `/code-review` skill, per [[20_Progress/Projects/AI Use/Builds & Resources/Code Review & Eval Gap|Code Review & Eval Gap]] — a built-in, not a claudekit-promoted tool.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] · [[20_Progress/Projects/AI Use/Builds & Resources/Code Review & Eval Gap]]
