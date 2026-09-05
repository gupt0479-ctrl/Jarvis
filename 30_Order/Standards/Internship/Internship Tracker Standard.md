---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-09-04
tags:
  - internship
  - standard
  - tracking
notes:
  - "[[Internship Pipeline]]"
  - "[[Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/Tracker/Internship - Dashboard]]"
next:
---
# Internship Tracker Standard
==Was an empty stub. Written after checking the one real Tracker note this system has ever produced (Appian, created 2026-07-26) directly against `Tracking Template.md` and [[Internship Pipeline]]'s own description of Step 3 and Step 8.== One real example is thin evidence, but it's genuine evidence, not a guess - it's cited throughout below.

==Moved here 2026-09-04 from the top-level `30_Order/Standards/Tracking Standard.md`, content unchanged== — that file was never a general vault tracking convention despite its name; its own §1 scope line already read "Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`," internship-specific from the day it was written. It predates the `30_Order/Standards/Internship/` subfolder (created later the same reorg that produced this file as an empty stub) and was never migrated in. Confirmed via direct read of both files before consolidating: no second, genuinely-general-purpose tracking standard exists anywhere else in the vault, so this is a stale duplicate location being closed, not two real scopes being merged.

## Scope
Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`. Does not govern `Tracker/Tracker.md` (a separate, hand-maintained kanban board - see §4) or `Tracker/Internship - Dashboard.md` (a separate, generated whole-system view - see §4). Both of those share the word "Tracker" with this folder but are distinct artifacts with distinct purposes; don't conflate them.

## 1. Frontmatter - required fields
Every Tracker note carries `Tracking Template.md`'s fields: `type: tracker, program, contact, company, url, date_noted, date_researched, date_created, date_applied, date_result, result, deadline, related_notes, tags, next`. The real Appian note confirms the template is followed as written - `program` and `contact` are wikilinks to the paired Program and Contact notes (not plain text), `related_notes` links back to the originating dossier, and unset date fields (`date_applied`, `date_result`, `result`, `deadline`) stay genuinely empty rather than defaulted to a placeholder.

**Created only once the paired Program note exists** (Internship Pipeline Step 3) - a Tracker note with no matching Program note is out of sequence and shouldn't exist. `program` and `contact` should resolve to real notes, not broken links, from the moment the Tracker note is created, since both are created together in the same sitting per Step 3.

## 2. Timeline and body - what each section is actually for
`## Timeline` is the dated index itself: Noted → Researched → Created → Applied → Result, one line each, filled in as the real dates happen, not backfilled from memory. The real Appian note shows the intended shape - `Noted: 2026-07-25`, `Researched: 2026-07-26`, `Created: 2026-07-26`, `Applied: —`, `Result: —`, all real dates, unset fields left as an em dash placeholder rather than deleted.

**A real, current gap between the template and the one real example**: `Tracking Template.md` also defines `### Company Information`, `### Conversation`, `### Interview Steps`, and a `## Loop Process` section under `## Summary` - none of these appear in the real Appian note, which only has `## Timeline` and `## Next Action`. This isn't necessarily wrong - the Appian note is still in `Current/`, pre-application, so Interview Steps and a completed Loop Process genuinely don't apply yet - but `## Summary` and `### Company Information` (a pointer to the Job & Company note) are template sections that should exist regardless of funnel stage, and the real note skips them. Until a second real Tracker note exists to compare against, treat this as an open question rather than a confirmed pattern: either the template is heavier than what's actually needed at `Current/` stage (revise it down), or the Appian note is incomplete (fill it in). Don't resolve this by guessing - check against the next Tracker note actually created.

**`## Next Action`** is the one section every real note should carry regardless of stage - the single next physical move, mirrored from (or feeding into) the paired Program note's own Traps & Gotchas or the Applying note's Next Action once one exists. The real Appian note uses this correctly: a concrete decision ("move from Considering to actually applying") tied to a concrete reason (the review-start date named on the Program note).

## 3. The Current/ → Applied/ → Result/ lifecycle
Mirrors [[Internship Pipeline]] Steps 3, 7, and 9 exactly:
- **`Current/`** - from creation (Step 3, paired with the Program and Contact notes) until a real application goes out. This is where the Appian note sits as of 2026-08-23.
- **`Applied/`** - moves here the moment `Applying/Now.md` gets an entry and the Applying note is created (Step 7), in the same sitting. `date_applied` is set at the same time as the move, not after.
- **`Result/`** - moves here once an outcome lands (Step 9), with `date_result` and `result` (`Offer`/`Rejected`/`Withdrawn` - the same three values the Applying note's `status` field uses) set at the same time as the move.
A Tracker note's folder and its `date_applied`/`date_result` fields should never disagree - if the note is in `Applied/`, `date_applied` is filled; if it's still in `Current/`, it isn't. This is a mechanical consistency check, not a judgment call - a note found out of sync is a real bug, not a stylistic issue.

> [!WARNING]
> **Stale against the resume/cover-letter system, flagged 2026-09-04, not yet resolved here.** [[30_Order/Workflows/Internship/Application Document Preparation]] moved Applying-note creation earlier — to the *start* of Step 5 (Tailor), not Step 7 (Apply) as the line above still says. This section's Tracker-side claim (`Applied/` move happens "in the same sitting" as Applying-note creation) is now only true for the *folder move*, not the *note creation* — the Applying note already exists by the time a Tracker note reaches `Applied/`. See [[10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create]] for the corrected sequencing once Task 3 of the 2026-09-04 session updates it.

## 4. Interlinking - Dashboard, the kanban, and a real current gap
`Tracker/Internship - Dashboard.md` is the whole-system view (per [[Internship Pipeline]]'s Ongoing Views). Checked directly against its live queries (2026-08-23): it queries `List/Dossiers`, `Programs/Serious` + `Programs/Considering`, and `20_Progress/Internship/Applying` - **it does not query `Tracker/Each One/` at all, in any of its current sections.** This is a real, currently-live gap, not a hypothetical: the Dashboard's "Applying — Live Status" section reads funnel stage from the Applying note's `status` field, which only exists once Step 7 happens, so a program sitting in `Tracker/Each One/Current/` pre-application (like Appian, right now) is invisible to the Dashboard entirely. The only way to see "where does this stand" for a pre-application program today is opening its Tracker note directly. Whether this is worth fixing (a Dashboard section reading `Current/`/`Applied/`/`Result/` counts, mirroring the Discovery/Programs sections' pattern) is a real, concrete improvement to flag - not something this Standard resolves on its own, since it's a Dashboard-note change, not a Tracker-note-content change.

`Tracker/Tracker.md` is a separate, entirely manual Kanban board (Interesting / To Apply / Applying Today / Applied columns, currently empty on all four as of 2026-08-23) - it is not generated from `Tracker/Each One/` notes and carries no automatic relationship to them. Per Internship Pipeline: "the kanban glance, this week's cards" - a lightweight manual view for weekly triage, not a source of truth. Don't expect it to reflect Tracker note state automatically; nothing currently keeps the two in sync.

## Done When
- Every Tracker note in `Current/`, `Applied/`, or `Result/` has its folder and its date fields agree.
- `program` and `contact` resolve to real notes on every Tracker note, no broken links.
- A Tracker note's `## Next Action` names a real, current, single next move - not stale from an earlier stage.
- The Dashboard/Tracker-note gap in §4 has been either fixed (a Dashboard section added) or explicitly deferred with a reason, not silently ignored.
