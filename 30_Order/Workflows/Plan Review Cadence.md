---
type: evergreen
status: sprout
created: 2026-07-27
updated: 2026-07-27
tags:
  - system
  - workflow
notes:
  - "[[00_Workflows Index]]"
  - "[[30_Order/Standards/Daily Workflow Standard|Daily Workflow Standard]]"
  - "[[30_Order/Templates/Career/Plan Template|Plan Template]]"
  - "[[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]]"
---
# Plan Review Cadence
Keep a `type: plan` note wired into daily and weekly execution instead of becoming a write-once wish list. **Use when:** any daily or weekly skill (`/startday`, `/closeday`, `/weekly-review`) runs in a folder that contains `type: plan` notes, or when creating a new plan per [[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]].
## Why This Exists
The original Summer Plans folder had no version of this workflow. Eleven files accumulated over two months; most were never re-opened after creation, two plan/tracker pairs quietly duplicated the same tracking data in separate files, and three different notes tried to be "the current status" at once. Nothing ever checked whether a plan note's own `review_cadence` was being honored — so none of them were. This workflow is the fix: a plan note is only as good as the mechanism that keeps rereading it.
## Steps
1. **On `/startday`:** if today's date matches or follows a plan note's stated cadence trigger (e.g. "daily," "Sunday"), read that plan's Current Progress and Implementation Status sections before writing today's plan — don't invent today's priorities independent of what the plan already says is true.
2. **On `/closeday`:** if today closed with a missed daily-floor item that traces to a `type: plan` note's Systems section, note it — this is the raw material `/weekly-review` uses to judge whether the plan itself needs a scope cut, not just the day.
3. **On `/weekly-review`:** for every active `type: plan` note whose `review_cadence` includes "weekly," append one dated line to its Current Progress section. Do not rewrite the section — append. If Implementation Status has drifted (a tracked item shipped, a flagship changed), patch that section by heading in the same pass.
4. **Staleness check, every `/weekly-review`:** if a plan note's Current Progress has gone two review cycles with no new entry, treat it the same as a missed daily rep under [[Anti-Drift Rules]]'s Never Miss Twice — flag it explicitly in the weekly synthesis note rather than letting it pass silently.
5. **On plan creation:** follow [[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]] end to end, using [[30_Order/Templates/Career/Plan Template|Plan Template]] and checking the note against [[30_Order/Standards/Daily Workflow Standard|Daily Workflow Standard]]'s Done Conditions before it's considered finished, not after.
6. **On merge or cleanup:** if a plan and its tracker have split into two files, or two notes both claim to be "the current status," merge them per [[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]]'s one-source-of-truth rule before adding more content to either.
## Done When
- Every active `type: plan` note has a Current Progress entry no older than its own stated `review_cadence`.
- No folder holds two notes tracking the same thing.
- A staleness flag, once raised in a weekly synthesis, gets resolved (updated or explicitly archived) before the next weekly review, not carried silently for a third cycle.
