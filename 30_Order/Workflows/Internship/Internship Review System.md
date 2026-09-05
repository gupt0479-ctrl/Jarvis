---
type: evergreen
status: sprout
created: 2026-09-04
updated: 2026-09-04
tags:
  - internship
  - workflow
  - review
notes:
  - "[[Internship Loop Review Standard]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
  - "[[Internship Loop Weekly Review Template]]"
  - "[[Internship Loop Monthly Review Template]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
next: "Wire a codebase-side loop-verifier run into the Weekly Discovery Review's Gate/Resource-Limit sections once that agent exists in internship-research-loop/.claude/agents/ — see #The Codebase Half below."
---
# Internship Review System
==The operational system that actually runs [[Internship Loop Review Standard]] — who triggers it, on what cadence, where the output lands, and what happens to what it finds.== That Standard states *what a review must contain, per heading*; this note states *how a review actually gets produced and closed out*, the same split [[Internship Tracking Workflow]] draws between a Standard's content rules and its own maintenance procedure.

## Trigger — Manual, Human-Initiated, Not A Cron Job
Per [[Internship Loop Review Standard]]'s own "Used By Workflow" line: no cron writes a review. A Weekly Discovery Review or Monthly Promotion Review starts when a person (or Claude, assisting one) opens the matching template and works it against real, current vault/repo state, in the same session or shortly after the period it covers. This is a deliberate choice, not a gap to eventually automate away — a review is exactly the kind of judgment-heavy synthesis [[20_Progress/Internship/Building System/Jarvis OS — North Star]]'s Part 5 governing principle assigns to "the agent owns content," not to unattended code.

## Cadence
- **Weekly Discovery Review** — every week, covering the prior 7 days of `List/Dossiers/` activity. Run it even in a week where nothing looks like it changed — per the general [[30_Order/Standards/Review Standard]]'s rule (which [[Internship Loop Review Standard]] inherits unchanged), "nothing to report" is a valid finding, not a reason to skip the review itself.
- **Monthly Promotion Review** — every calendar month, covering Steps 2-9 (`Programs/`, `Contacts/`, `Tracker/`, `Applying/`, `Preperation/`). Lower cadence is intentional: as of this writing only one real promotion trio (Appian) plus three manual-web-find Program notes exist, so a weekly cadence here would mostly produce padding.

## Where Output Lands
`60_Claude/30_Reviews/Internship Loop/Scheduled/{Weekly,Monthly}/`, one file per period, from [[Internship Loop Weekly Review Template]] / [[Internship Loop Monthly Review Template]]. [[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]] is the index — a new review file should always get linked there in the same sitting it's written, not left to be discovered later by a folder listing.

## Creating A New Period's File
Copy the matching template, filled per [[Internship Loop Review Standard]]'s per-heading spec — the template already carries the section skeleton; this workflow adds only the mechanical steps the Standard doesn't state:
1. Name the file consistently with the one real gold-standard example ([[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34]]'s own naming: `Internship Loop Weekly Review — YYYY-Www` / `Internship Loop Monthly Review — YYYY-MM`).
2. Link it into the Reviews MOC before writing the content, not after — a review that exists but isn't indexed is functionally unfindable the next time someone asks "when was this last checked."
3. Write the review per the Standard's per-heading spec, citing real files/counts throughout (per the Standard's own Gate/Standard Conformance warning: a fact answerable by one grep should be grepped, not sampled).

## Closing Out A Review's Findings
A review's own **Decided Fixes** section (only items at 100% clarity, per the general Review Standard) is not itself authorization to patch code or rewrite a note — it's a handoff:
- **A codebase-side finding** (a filter/classify/relevance bug, a schema-drift gap, a resource-limit-code gap) becomes a new dated entry or prompt in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]], the same handoff mechanism every prior codebase fix in this project has used — see [[20_Progress/Internship/Building System/System - Build Log]] for the pattern (a Build Log entry records what a review found; a Prompt entry is what actually gets run against the repo to fix it).
- **A vault-side finding** (a stale note, a broken cross-link, a template gap) gets fixed directly in the same session, same as any other vault-hygiene finding, and the fix gets a one-line mention in [[60_Claude/07_AI_Information/Session Logs/log.md]].
- **Open Questions** carry forward to the next period's review verbatim until actually resolved — don't let a question quietly disappear because nobody re-typed it into the next file.

## The Codebase Half — `loop-verifier`
`internship-research-loop/.claude/agents/loop-verifier.md` is, by its own description, "the automated equivalent of the manual audits run on 2026-07-19 and 2026-07-25" — it already checks the test suite, scheduled-run history (`run.yml`/`recheck.yml`/`test.yml`), vault-vs-log dossier counts, `seen_ids.json`/vault divergence, and auto-filed GitHub issues, producing a dated HEALTHY/DEGRADED/BROKEN verdict. This is real, existing overlap with the Weekly Discovery Review's **Gate Conformance** and **Resource-Limit Health** sections — both ask essentially the same question ("is discovery actually working, cited to real evidence") from two different sides of the same system.
**Not yet wired together.** Running `loop-verifier` is not currently a stated step of the Weekly Discovery Review, and the Review Standard's per-heading spec doesn't reference it. The two should not simply be merged — `loop-verifier` is read-only and code/infra-focused (tests, CI runs, state-file divergence); the Weekly Discovery Review also does content-quality sampling (priority classification accuracy, body-content spot checks) that no code-level check can do. The right integration is citing `loop-verifier`'s dated report as one input to the Weekly Discovery Review's Resource-Limit Health and Gate Conformance sections, not replacing either. Left as an open item here rather than decided unilaterally — see this note's own `next:` field.

## Done When
- Every calendar week and month has a review file, even a short one stating "nothing to report."
- Every review file is linked from [[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]] before it's considered filed.
- Every Decided Fix has a real, findable downstream artifact (a Claude Code Prompt entry, a direct vault fix with a session-log line) — a Decided Fix that never produced anything is itself a finding for the next review.
- Open Questions are either resolved or explicitly carried forward — none silently dropped between periods.
