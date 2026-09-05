---
type: index
status: sprout
created: 2026-08-23
updated: 2026-09-04
tags:
  - internship
  - moc
  - review
notes:
  - "[[Internship Loop Review Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
  - "[[Internship Pipeline]]"
next: "2026-W36/2026-09 reviews found two real deadlines (Castleton, KeyBank) already reached or passed with zero Applying-note activity, a confirmed stage1_reject false-positive regression on 6 Microsoft dossiers, and Prompt 27's Batch B never landing despite being recorded as run. Run the next Weekly Discovery Review once run.yml is re-enabled and has a few days of data; run the next Monthly once the urgent deadline findings above are resolved one way or another."
---
# Internship Loop Reviews — Map of Content
## Purpose
This folder holds the review layer for `gupta-builds/internship-research-loop` and everything downstream of it in [[Internship Pipeline|Internship Pipeline]] — the thing that checks whether the loop's actual output matches what [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] and [[Internship Notes Standard|Internship Notes Standard]] say it should, instead of trusting the commit log or the dossier count alone.
## Map
[[Internship Loop Review Standard|Internship Loop Review Standard]] is the content contract for everything under `Scheduled/` here — read it first, it explains why the folder splits into two review types rather than one. `Scheduled/Weekly/` holds the **Discovery Review**: a weekly check on Step 1 (Find) — the hourly, unattended GitHub Actions loop that writes into `List/Dossiers/`. This is the review that actually catches the loop's real, historical bug class — misclassification on an incidental keyword, cross-source duplicates that share an exact URL, postings that never should have cleared the CS/software-relevance gate — the same class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] records recurring even after being "fixed." `Scheduled/Monthly/` holds the **Promotion Review**: a monthly check on Steps 2-9 (Screen through Close) — Program, Contacts, and Tracker note hygiene, graded directly against [[Internship Pipeline|Internship Pipeline]]'s own `Done When` checklist. It runs monthly, not weekly, because this half of the pipeline is still lightly exercised (one real promotion, Appian, as of the first review below) and a weekly cadence on it would mostly report nothing new.
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|Internship Loop Weekly Review — 2026-W34]] is the first real review of either kind, run the same session the Standard was written. It found the loop's `notes:` interlink field — specified as shipped 2026-07-30 — present on only 11 of 392 live dossiers, plus a real gate-conformance miss (a pure quant-trading role that should have been rejected outright) and an exact-URL cross-source duplicate. [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08|Internship Loop Monthly Review — 2026-08]] is the first Promotion Review, checked against the one real program that exists (Appian) — its note trio cross-links correctly, but its Tracker note's stated "no rush" reasoning cites a review-start date that has since arrived.
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W36|Internship Loop Weekly Review — 2026-W36]] and [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-09|Internship Loop Monthly Review — 2026-09]] (2026-09-04, both run with real `gh`/repo access this time — the exact gap 2026-W34 itself flagged) found: a confirmed `stage1_reject` false-positive regression on 6 genuine Microsoft dossiers (a sidebar-link content bleed, same bug class as the known Google careers-listing-shell issue); the Virtu gate-conformance miss still unaddressed 12 days later; a real alert-fatigue pattern (6 of 9 GitHub issues permanently open and informational); Prompt 27's entire 7-dossier promotion batch never landing in the vault despite being recorded as run; and — the most concrete finding either review has produced — two real application deadlines (Castleton Commodities International, KeyBank) already reached or passed with zero downstream Applying-note activity.
> [!WARNING]
> The Monthly review's note-shape checks are provisional — see the Standard's own dependency warning. A separate session is still defining concrete field-level specs for Program/Contact/Tracker/Applying/Job & Company notes under `30_Order/`. Don't read a provisional finding here as a settled rule until that lands.
## Status
| Review | Period | Status |
|---|---|---|
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34\|Weekly — 2026-W34]] | 2026-08-17 to 2026-08-23 | Findings still open (see 2026-W36) |
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08\|Monthly — 2026-08]] | 2026-08-01 to 2026-08-23 | Findings still open (see 2026-09) |
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W36\|Weekly — 2026-W36]] | 2026-08-24 to 2026-09-04 | New — findings open |
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-09\|Monthly — 2026-09]] | 2026-08-24 to 2026-09-04 | New — 2 urgent deadline findings, act today |
## Dataview
```dataview
TABLE created, status
FROM "60_Claude/30_Reviews/Internship Loop/Scheduled"
SORT file.name DESC
```
