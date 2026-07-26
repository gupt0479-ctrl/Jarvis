---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - moc
notes:
  - "[[10_Areas/Career/Internships/Programs/Programs-to-Create]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Tracker/Internship - Dashboard]]"
---
# Programs — Map of Content
==Everything currently in `Programs/`, live.== This is a folder-scoped visualization, not a replacement for [[10_Areas/Career/Internships/Tracker/Internship - Dashboard]] — that dashboard also joins in live Applying status; this note only shows what's actually sitting in `Programs/` right now, split by folder. See [[10_Areas/Career/Internships/Programs/Programs-to-Create]] for how a note gets here at all.
## Serious — Pursuing Now
```dataview
TABLE
  company,
  wave,
  deadline_real as "Real Deadline",
  pay_per_week as "Pay/Week",
  eligible_classes as "Eligible",
  applying_note as "Applying Note"
FROM "10_Areas/Career/Internships/Programs/Serious"
SORT deadline_real ASC
```
## Considering — Interested, Not Yet Committed
```dataview
TABLE
  company,
  wave,
  deadline_real as "Real Deadline",
  pay_per_week as "Pay/Week",
  eligible_classes as "Eligible"
FROM "10_Areas/Career/Internships/Programs/Considering"
SORT deadline_real ASC
```
## Counts
```dataview
TABLE WITHOUT ID
  "Serious" as Folder, length(rows) as Count
FROM "10_Areas/Career/Internships/Programs/Serious"
WHERE company
GROUP BY true
```
```dataview
TABLE WITHOUT ID
  "Considering" as Folder, length(rows) as Count
FROM "10_Areas/Career/Internships/Programs/Considering"
WHERE company
GROUP BY true
```
