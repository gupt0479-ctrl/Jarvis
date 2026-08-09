---
type: evergreen
status: tree
created: 2026-07-27
updated: 2026-07-27
tags:
  - system
  - plans
  - standards
notes:
  - "[[30_Order/Templates/Career/Plan Template|Plan Template]]"
  - "[[30_Order/Standards/Daily Workflow Standard|Daily Workflow Standard]]"
  - "[[Plan Review Cadence]]"
  - "[[Plans Board]]"
  - "[[Final Month Plan (Jul 28 - Sep 1)|Final Month Plan (Jul 28 - Sep 1)]]"
next: "[[30_Order/Templates/Career/Plan Template|Plan Template]]"
---
# Plans-to-Create
==One source of truth for how a plan note gets created in this vault — every future plan follows the steps below, in order, before it counts as finished.== Written 2026-07-27 after a full cleanup of `10_Areas/Life/Plans/Summer/`, which is the case study this file keeps referring back to.
## Why This File Exists
The Summer Plans folder grew to 11 files over two months without ever being checked against a standard, because no standard existed — [[30_Order/Templates/Career/Plan Template|Plan Template]] and this file both sat empty the whole time. The concrete damage: two plan/tracker pairs (LeetCode plan + LeetCode tracker, ML Fundamentals plan + ML Fundamentals progress) duplicated the same tracking data in separate files; a status recap, a near-term close-out, and a forward plan were written as three separate notes that each partly repeated the others; and the folder's own index carried "standing assumptions" that were seven weeks stale with no mechanism to catch it. Fixing that meant merging 11 files down to 6 in one pass. This file exists so the next plan is built right the first time instead of needing that pass.
## Before Creating Any Plan
Three checks, before opening the template:
1. **Search first.** Does a plan already exist for this domain, even a rough one? Extend it by heading — do not create a second note that will end up competing with the first for "current status."
2. **Can the Goal sentence be written right now, with a real metric?** If the answer requires a paragraph, the plan isn't scoped yet. Scope it in conversation before creating the file.
3. **Does a tracker-shaped file already exist for this same thing** (a log, a progress table, a daily-count sheet)? If yes, the new plan absorbs it as a numbered section inside the same file — it never sits beside it as a second file.
## The Creation Steps
1. Copy [[30_Order/Templates/Career/Plan Template|Plan Template]] in full. Every section in it is required, not optional scaffolding.
2. **Goal** — one or two sentences, one metric that proves it happened.
3. **Timeframe** — real calendar dates, not seasons. Add a phase or week table for anything spanning more than two weeks.
4. **Systems** — break the goal into tracks, each with a cadence and a done-definition checkable on any given day.
5. **Implementation Status** — verified only. Check a real file, a real commit, a real `git log` before writing a line here. Where verification isn't possible yet, write "unverified" and name what would verify it — never round up to "probably done."
6. **Current Progress** — seed it with one dated baseline entry the day the plan is created.
7. **Update Protocol** — name the exact skill (`/closeday`, `/weekly-review`, a monthly review) and cadence that will touch this note, and what happens on two consecutive misses.
8. Set the frontmatter `review_cadence:` field to match what Update Protocol says in prose — the two must agree.
9. **Link the plan from its folder's index or MOC** (e.g. a `00 -` index note) so it's discoverable without already knowing it exists.
10. **Check it against [[30_Order/Standards/Daily Workflow Standard|Daily Workflow Standard]]'s Done Conditions**, line by line, before calling it finished.
11. **Wire it into [[Plan Review Cadence]]** — confirm which skill will actually read and update this note, and on what trigger.
12. Log the creation in `60_Claude/07_AI_Information/Session Logs/log.md`.
## The One-Source-of-Truth Rule
Two failure shapes caused nearly all of the Summer Plans cleanup, and both are now explicit rules:
- **No plan/tracker splits.** A plan's own tracking data — a log table, a progress table, a mastery table — lives inside the plan note as a numbered section (see [[LeetCode & CSCI 4041|LeetCode & CSCI 4041]] §8 and [[ML Fundamentals (2033 + 2230)|ML Fundamentals (2033 + 2230)]] §8 for the corrected shape). A separate "Tracker" file next to a "Plan" file is always wrong.
- **No status fragments.** A plan has exactly one "what's true right now" section — Current Progress, inside the plan itself. It does not get a separate recap note, a separate close-out note, and a separate forward-plan note that each claim to be current. [[Final Month Plan (Jul 28 - Sep 1)|Final Month Plan (Jul 28 - Sep 1)]] replaced exactly three such fragments with one file.
## Anti-Patterns Found In The 2026-07-27 Cleanup
Concrete, not hypothetical — these are what actually had to be fixed:
- **Hedges standing in for decisions.** Phrases like "estimated hours" or "not yet known" repeated across a note without ever getting resolved. A real plan states an unknown as a dated action item ("W1 task: confirm the exact hour count before W4") — not a permanent shrug that reappears every time the note is read.
- **A folder index frozen in time.** The original index's "Standing assumptions" section still said "Today is 2026-06-03" seven weeks later, because nothing ever re-checked it. [[Plan Review Cadence]]'s staleness check exists specifically to catch this.
- **Skills hardcoding file paths that outlive the files.** `/startday` and `/weekly-review` both referenced the old numbered filenames (`01 - Daily Operating System.md`, `05a - LeetCode Tracker.md`) directly — when the files were renamed and merged, both skills silently pointed at nothing. Any skill that reads a plan folder's files by name must be re-checked whenever that folder's file set changes; this is now stated in both skill files directly.
- **Two tables tracking the same thing in two files.** The LeetCode mastery table and the LeetCode daily-log table lived in separate notes, so neither one was ever the single place to look. Merged per the One-Source-of-Truth rule above.
## Review Cadence For This File
When the process above still produces a weak plan, patch this file, not just the one plan that failed — that keeps the fix durable instead of one-off. Re-check this file whenever a plan-note cleanup happens again, or when the same mistake shows up in two different plans in a row.
