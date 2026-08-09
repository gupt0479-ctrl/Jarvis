---
type: evergreen
status: sprout
created: 2026-07-27
updated: 2026-07-27
tags:
  - system
  - standards
notes:
  - "[[30_Order/Templates/Career/Plan Template|Plan Template]]"
  - "[[Plan Review Cadence]]"
  - "[[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]]"
  - "[[HUMAN_WRITING]]"
---
# Daily Workflow Standard
==A plan note that no daily or weekly skill ever reads is a wish list with frontmatter — this standard exists so a `type: plan` note stays wired into `/startday`, `/closeday`, and `/weekly-review` instead of going stale the way the July 2026 Summer Plans notes did.== That failure is the reason this standard exists: eleven files, most never checked, two plan/tracker pairs duplicating the same data, three fragments of one status note, and a folder index whose "standing assumptions" were seven weeks out of date. This is the content standard for `type: plan` notes anywhere in the vault, and the rule for how daily/weekly automation must treat them.
## Maps To
- Template: [[30_Order/Templates/Career/Plan Template|Plan Template]]
## Used By Workflow
- [[Plan Review Cadence]] — the step-by-step for how `/startday`, `/closeday`, and `/weekly-review` read and update `type: plan` notes.
## Per-Heading Standard
### Frontmatter
`type: plan`, `status:` one of `seed | active | complete | paused | archived`, `created`/`updated`, `deadline:` if a real external date exists, `review_cadence:` in plain words (e.g. "weekly via /weekly-review"), `next:`.
> [!WARNING]
> `review_cadence:` left empty. A plan with no stated cadence cannot be checked for staleness by any skill — it silently drops out of daily/weekly automation, exactly what happened to the original Summer Plans folder.
### Goal
One or two sentences, one metric.
*Density:* a single outcome sentence with a number or a done-condition in it, not a theme.
> [!WARNING]
> A goal stated as an identity or a feeling ("be a builder who ships"). That belongs in [[Summer Grind]]-style strategic notes, not in a plan note's Goal section — a plan's Goal must be checkable.
### Timeframe
Start date, end date, and why the end date is real. Add a phase or week table for anything longer than two weeks.
*Density:* dates, not seasons. "The rest of summer" is not a timeframe; "2026-07-28 → 2026-09-01" is.
> [!WARNING]
> An end date with no external reason behind it. If nothing forces the deadline, say so explicitly rather than implying urgency that isn't real.
### Systems
The goal broken into concrete, checkable tracks, each with a cadence and a done-definition.
*Density:* every track answers "how would I know today whether this happened." A track without a done-definition is a category, not a system.
> [!WARNING]
> A list of project names with no mechanism attached. "Ship TradingView" is a category; "review Cursor's Streamlit build against the locked UI spec" is a system.
### Implementation Status
What's actually built, verified against a real file, commit, or tracker — never against memory of intent.
*Density:* one row or line per track, each traceable to something a second person could go check.
> [!WARNING]
> Self-report language ("should be mostly done," "probably on track"). If it can't be verified against a live file right now, write "unverified" and say what would verify it — do not round up.
### Current Progress
Living section, append-only. One dated line per review.
*Density:* short, dated, factual — this section is a log, not a rewrite target.
> [!WARNING]
> Rewriting this section instead of appending to it. Deleting old entries erases the exact history a plan needs to prove whether it's drifting.
### Update Protocol
States which skill touches this note and on what cadence, and what happens on two consecutive misses.
*Density:* names a real command (`/closeday`, `/weekly-review`) and a real trigger, not "review periodically."
> [!WARNING]
> No update protocol at all. This is the single field the July 2026 failure traces back to — every deleted or merged note in that cleanup either had no update protocol or had one nobody enforced.
## Done Conditions
- Every section in [[30_Order/Templates/Career/Plan Template|Plan Template]] is filled with real content, not a placeholder sentence.
- `review_cadence:` is set and matches a real skill or review cycle.
- Implementation Status is verified against live files/commits, not self-reported.
- Current Progress has at least one dated entry and is append-only from here.
- The note is linked from its folder's index (e.g. [[00 - Summer Plans Index]]) so it's discoverable, not just linked from other plan notes.
- No two notes in the same folder duplicate the same tracking data — a plan and its tracker are one file, per [[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]].
## Gold Standard Example
- [[Final Month Plan (Jul 28 - Sep 1)|Final Month Plan (Jul 28 - Sep 1)]] — Goal with one metric, a dated Timeframe table, Systems broken into checkable tracks, Implementation Status verified against real files and `git log`, a Current Progress log seeded with its baseline entry, and an Update Protocol naming the exact Sunday trigger and the two-miss consequence.
