---
description: "Ingest a clipping file from 60_Claude/05_Clippings/ into the vault. Usage: /ingest-clipping \"filename.md\""
setup_status: current
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
---
The target clipping is: $ARGUMENTS

Invoke the `ingesting-clipping` skill by reading `.claude/skills/ingesting-clipping/SKILL.md` and executing every step for the file specified above. The skill is a directory — always start from SKILL.md, and load `reference.md` / `examples.md` only when a step points you there. Do not explain the skill or ask for confirmation — just run it.
