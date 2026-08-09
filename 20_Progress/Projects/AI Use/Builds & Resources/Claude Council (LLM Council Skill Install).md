---
type: project
status: complete
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Maverick Skills Mode-to-Repo Mapping]]"
tags:
  - "#progress"
  - "#ai"
next: "Use /llm-council on the first genuinely high-stakes, ambiguous decision that comes up (architecture choice, risk call, hard debug)"
---
# Claude Council (LLM Council Skill Install)
## What Got Built
`.claude/skills/llm-council.md` + `.claude/commands/llm-council.md` — installed for real this pass, not just recorded as a plan, per [[00_Execution]]'s "BUILD today" verdict on [[Claude Council — Path A Prompt (web)]]. Registered in `CLAUDE.md`'s skill table as `/llm-council "question"`.
## Source and Correction Carried Forward
Adapted from [[LLM Council skills]] (aiwithremy/claude-skills-llm-council, itself adapting Karpathy's original `llm-council`). **One correction preserved from the source ingestion, not dropped:** the discovery landing page ([[Claude Council — Path A Prompt (web)]]) claims Path B "saves an HTML report to your workspace" — false. The real `SKILL.md` explicitly forbids file output; verdicts present in chat only. The built skill enforces this as a hard rule (Step 5), with optional transcript saving to `60_Claude/00_Inbox/` only on explicit request.
## What The Skill Does
Runs a genuinely uncertain, high-stakes question through 5 parallel advisor personas (domain-customized for this vault: Trading Analyst, CS Theorist, Systems Engineer, ML Practitioner, Pragmatic Builder — not Karpathy's generic five), has them peer-review each other's anonymized answers, then synthesizes a chairman verdict across five fixed sections (Where the Council Agrees, Where the Council Clashes, Blind Spots, Recommendation, First Action). Explicitly scoped to hard-to-reverse decisions — architecture choices, risk assessments, ambiguous debugging calls — not routine tasks.
## Evidence
- `.claude/skills/llm-council.md` — the built skill
- [[LLM Council skills]] — the source repo analysis, including the live `SKILL.md` fetch that surfaced the HTML-report discrepancy
- [[Claude Council — Path A Prompt (web)]] — the discovery page with the corrected claim
- [[00_Execution]] — the "BUILD today" verdict this note confirms was executed
