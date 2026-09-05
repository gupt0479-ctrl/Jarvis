---
type: index
status: seed
created: 2026-08-24
updated: 2026-08-24
tags:
  - internship
  - moc
  - automation
notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed]]"
  - "[[Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
next: Re-check this MOC after recheck.py's next removal batch — currently only the single 2026-08-23 batch exists.
---
# Removed Dossiers — Map of Content
## Purpose
Every dossier `recheck.py` finds closed upstream moves here instead of being deleted, per [[Internship Notes Standard]] §4 — this is the map every such dossier's `notes:` field points back to, so a removed dossier stays reachable rather than becoming an orphan. See [[10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed]] for why this folder exists at all and what it's deliberately not (an applied-internships tracker).
## Map
As of 2026-08-24, four real dossiers have gone through the move-not-delete path, all in a single batch on 2026-08-23, all for the same reason (`removed_reason: "active: false upstream"` — the posting was live when found and gone by the next recheck, not a bad match caught late):
- **Capital One closed two postings the same day** — [[10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security Intern - Capital One (2)|Cyber Security Intern]] and [[10_Areas/Career/Internships/List/Dossiers/Viewed/Software Engineer Intern - Capital One (2)|Software Engineer Intern]], both found 2026-08-03 via vanshb03, both removed 2026-08-23. Two independent postings from the same company closing on the same recheck is exactly the hiring-cadence signal [[10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed|What was Viewed]] says this folder should be read for, not re-screened by hand.
- **[[10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security IT Intern - CNO Financial Group (2)|Cyber Security IT Intern - CNO Financial Group]]** — found 2026-08-06 via vanshb03, removed 2026-08-23. A three-week-old remote posting, gone by the next check.
- **[[10_Areas/Career/Internships/List/Dossiers/Viewed/Data Internship - Data & AI Program - JP Morgan Chase (2)|Data Internship - Data & AI Program - JP Morgan Chase]]** — found 2026-08-03 via SimplifyJobs, removed 2026-08-23. The only removed dossier so far that didn't come through vanshb03.
No removal has recurred as a later duplicate yet — nothing here is currently evidence for the dedup/exclusion logic [[20_Progress/Internship/Building System/Source of Truth]] tracks; that's a real future use of this folder, not yet observed.
## Status
| Metric | Value |
| --- | --- |
| Total removed dossiers | 4 |
| Removal batches | 1 (2026-08-23) |
| Removal reasons seen | `active: false upstream` only — `absent from live feed` not yet observed |
| Sources represented | vanshb03 (3), SimplifyJobs (1) |
## Dataview
```dataview
TABLE company, title as "Role", source, removed_reason as "Why It Closed", removed_date as "Closed"
FROM "10_Areas/Career/Internships/List/Dossiers/Viewed"
WHERE company
SORT removed_date DESC
```
