---
type: evergreen
status: sprout
created: 2026-09-04
updated: 2026-09-04
tags:
  - internship
  - workflow
  - tracking
notes:
  - "[[30_Order/Standards/Internship/Internship Tracker Standard]]"
  - "[[10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create]]"
  - "[[Internship Loop Review Standard]]"
  - "[[Internship Pipeline]]"
next: "First real cadence run happens once at least two Tracker notes exist to compare against each other, not just against the template."
---
# Internship Tracking Workflow
==The recurring maintenance procedure for a Tracker note, once it exists.== [[10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create]] covers *creation* (when and how a Tracker note comes into being); [[30_Order/Standards/Internship/Internship Tracker Standard]] covers *content rules* (what fields and sections mean); neither says what actually touches a Tracker note afterward, on an ongoing basis, until it reaches `Result/`. This note is that gap.

## Why This Is Its Own Workflow, Not Folded Into The Standard
A Standard states what must be true about a note; a Workflow states the recurring human procedure that keeps it true. [[30_Order/Standards/Internship/Internship Tracker Standard]] already states the mechanical invariant ("a Tracker note's folder and its date fields should never disagree") — this note is the answer to *how that invariant actually gets maintained* week to week, since nothing currently checks it automatically.

## The Touch Points — When A Tracker Note Actually Gets Opened Again
A Tracker note isn't rewritten on a cadence of its own; it's touched at four real trigger points, each borrowed from an event that's already happening elsewhere in [[Internship Pipeline]]:
1. **A deadline fact changes.** The paired Program note's `deadline_real`/`deadline_posted` gets a real update (a posting's own deadline moves, or an estimate becomes confirmed) — the Tracker note's `deadline` field is a direct mirror of that fact per the Tracker Standard, and a Program-note update that doesn't propagate here is a real, checkable drift, not a cosmetic gap.
2. **The Tailor sequence starts** ([[30_Order/Workflows/Internship/Application Document Preparation]]'s `prepare` step) — the Tracker note doesn't move folders yet at this point (it stays in `Current/` until actual submission — see [[Applying Standard]] §2), but its `## Next Action` should now point at the real next physical move in that sequence, not a stale pre-Tailor note.
3. **Actual submission** (Internship Pipeline Step 7) — the one hard, mechanical move: `Current/` → `Applied/`, `date_applied` set in the same sitting the Applying note's own `status` moves to `Applied`. This is the single most important sync point this workflow exists to protect — a Tracker note left in `Current/` after its paired Applying note already shows `Applied` is the exact drift [[30_Order/Standards/Internship/Internship Tracker Standard]] §3 calls "a real bug, not a stylistic issue."
4. **An outcome lands** (Internship Pipeline Step 9) — `Applied/` → `Result/`, `result`/`date_result` set, matching the Applying note's own outcome field verbatim (see [[Applying Standard]] §2).
Outside these four events, a Tracker note is not expected to change — don't open one "just to check on it" without a real trigger; that's what the review cadence below is for.

## The Weekly Check — Piggybacking On The Friday Ritual, Not A New Cadence
[[Internship Pipeline]]'s own cadence section already names a weekly Friday pass over `Applying/_This Week.md`. This workflow adds one concrete check to that same pass, rather than inventing a separate Tracker-specific ritual: for every Tracker note currently in `Current/` with a real `deadline` in the near term, confirm its `## Next Action` still names something that's actually still true — the same "a date cited in the reasoning has since passed" staleness pattern [[Internship Loop Review Standard]]'s Monthly Promotion Review already checks for at a coarser, monthly grain. Catching it weekly on the small `Current/` set is cheaper than waiting for the monthly review to find it after a month of drift.

## Relationship To The Monthly Promotion Review
[[Internship Loop Review Standard]]'s Monthly Promotion Review already does a **Per-Program Trace** — walking noted → researched → created → applied → result for every real trio and flagging anything stalled beyond what its own `Next Action` assumed. This workflow's weekly check and that monthly trace aren't redundant: the weekly check is a fast, narrow sanity pass on active `Current/` notes only; the monthly trace is the deeper, whole-corpus audit that also covers `Applied/`/`Result/` and cross-checks against the Dashboard/Kanban. A finding from either should cite the other rather than re-deriving it — if the monthly review finds a stalled Tracker note, that's a sign this workflow's weekly check missed it, worth naming as a review finding in its own right, not just fixing quietly.

## What This Workflow Does Not Cover
- **Frontmatter/section content rules** — see [[30_Order/Standards/Internship/Internship Tracker Standard]].
- **Note creation** — see [[10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create]].
- **`Tracker/Internship - Dashboard.md`'s own real gap** (it never queries `Tracker/Each One/`, per the Tracker Standard §4) — that's a Dashboard-note change, not something this workflow's manual touch-points can substitute for.

## Done When
- Every Tracker note in `Current/` was actually touched at one of the four trigger points above since its last real state change — not stale from a skipped sync.
- The weekly Friday pass over `_This Week.md` includes the Next-Action staleness check for every `Current/` Tracker note with a near-term deadline.
- No Tracker note's folder disagrees with its paired Applying note's `status` for more than the same working session in which the disagreement was created.
