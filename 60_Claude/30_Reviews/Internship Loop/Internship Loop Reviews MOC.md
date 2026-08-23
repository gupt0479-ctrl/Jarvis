---
type: index
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - internship
  - moc
  - review
notes:
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
next: "Run the next Weekly Discovery Review around 2026-08-30; run the next Monthly Promotion Review in September once at least one more program has moved past Commit."
---
# Internship Loop Reviews — Map of Content
## Purpose
This folder holds the review layer for `gupta-builds/internship-research-loop` and everything downstream of it in [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]] — the thing that checks whether the loop's actual output matches what [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] and [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] say it should, instead of trusting the commit log or the dossier count alone.
## Map
[[30_Order/Standards/Internship Loop Review Standard|Internship Loop Review Standard]] is the content contract for everything under `Scheduled/` here — read it first, it explains why the folder splits into two review types rather than one. `Scheduled/Weekly/` holds the **Discovery Review**: a weekly check on Step 1 (Find) — the hourly, unattended GitHub Actions loop that writes into `List/Dossiers/`. This is the review that actually catches the loop's real, historical bug class — misclassification on an incidental keyword, cross-source duplicates that share an exact URL, postings that never should have cleared the CS/software-relevance gate — the same class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] records recurring even after being "fixed." `Scheduled/Monthly/` holds the **Promotion Review**: a monthly check on Steps 2-9 (Screen through Close) — Program, Contacts, and Tracker note hygiene, graded directly against [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s own `Done When` checklist. It runs monthly, not weekly, because this half of the pipeline is still lightly exercised (one real promotion, Appian, as of the first review below) and a weekly cadence on it would mostly report nothing new.
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|Internship Loop Weekly Review — 2026-W34]] is the first real review of either kind, run the same session the Standard was written. It found the loop's `notes:` interlink field — specified as shipped 2026-07-30 — present on only 11 of 392 live dossiers, plus a real gate-conformance miss (a pure quant-trading role that should have been rejected outright) and an exact-URL cross-source duplicate. [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08|Internship Loop Monthly Review — 2026-08]] is the first Promotion Review, checked against the one real program that exists (Appian) — its note trio cross-links correctly, but its Tracker note's stated "no rush" reasoning cites a review-start date that has since arrived.
> [!WARNING]
> The Monthly review's note-shape checks are provisional — see the Standard's own dependency warning. A separate session is still defining concrete field-level specs for Program/Contact/Tracker/Applying/Job & Company notes under `30_Order/`. Don't read a provisional finding here as a settled rule until that lands.
## Status
| Review | Period | Status |
|---|---|---|
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34\|Weekly — 2026-W34]] | 2026-08-17 to 2026-08-23 | First run — findings open |
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08\|Monthly — 2026-08]] | 2026-08-01 to 2026-08-23 | First run — findings open |
## Dataview
```dataview
TABLE created, status
FROM "60_Claude/30_Reviews/Internship Loop/Scheduled"
SORT file.name DESC
```
