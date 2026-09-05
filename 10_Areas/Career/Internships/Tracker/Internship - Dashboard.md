---
created: 2026-07-09
updated: 2026-07-26
type: dashboard
status: active
tags:
  - internships
  - tracking
  - career
  - dashboard
notes:
  - "[[Internships Hub]]"
  - "[[Internship Pipeline]]"
  - "[[Source of Truth]]"
---
# 📊 Internship Dashboard — The Whole Process
==Not per-internship — this is the health of the entire loop, one screen.== For one specific internship's detail, go to its Tracker/Each One note. For the kanban glance, see [[Tracker]]. For the raw pipeline status doc, see [[Internships Hub]].
## 🔎 Discovery — Dossier Pipeline Health
```dataview
TABLE WITHOUT ID
  file.folder as "Priority Folder", length(rows) as "Count", "/ 50" as Limit
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE company AND file.folder != "10_Areas/Career/Internships/List/Dossiers"
GROUP BY file.folder
```
> [!IMPORTANT]
> Total cap is 201 across all four priority folders (50 each) — warning stages at 150, 170, 190, 200. If any single folder is closing in on 50, that's the one to screen down before the next push, not the others.
## 🧭 Screening Backlog — Found, Not Yet Screened
```dataview
TABLE company, title, file.folder as "Priority"
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE company AND length(file.inlinks) = 0
SORT date_found DESC
LIMIT 15
```
## 🌊 Programs — Committed Research
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
```dataview
TABLE company, deadline_real as "Real Deadline", pay_per_week as "Pay/Week"
FROM "10_Areas/Career/Internships/Programs/Serious" OR "10_Areas/Career/Internships/Programs/Considering"
WHERE deadline_real <= date(today) + dur(30 days)
SORT deadline_real ASC
```
## 🔄 Applying — Live Status
```dataview
TABLE WITHOUT ID
  file.link as "Application",
  company as "Company",
  status as "Stage",
  next_deadline as "Next Deadline"
FROM "20_Progress/Internship/Applying"
WHERE status AND status != "Offer" AND status != "Rejected" AND status != "Withdrawn"
SORT next_deadline ASC
```
### Funnel Counts
```dataview
TABLE WITHOUT ID
  rows.status as "Status",
  length(rows) as "Count"
FROM "20_Progress/Internship/Applying"
WHERE status
GROUP BY status
```
### Offer / Rejected / Withdrawn
```dataview
TABLE WITHOUT ID
  file.link as "Application",
  status as "Result",
  date_response as "Date"
FROM "20_Progress/Internship/Applying"
WHERE status IN ("Offer", "Rejected", "Withdrawn")
SORT date_response DESC
```
## 👥 Contacts — Relationship State
```dataview
TABLE WITHOUT ID
  "Ongoing" as Folder, length(rows) as Count
FROM "10_Areas/Career/Internships/Contacts/Each One/Ongoing"
GROUP BY true
```
```dataview
TABLE WITHOUT ID
  "Come Back" as Folder, length(rows) as Count
FROM "10_Areas/Career/Internships/Contacts/Each One/Come Back"
GROUP BY true
```
## 💰 Research — Sorted By Compensation
```dataview
TABLE
  company as "Company",
  program_type as "Type",
  pay_per_week as "Pay/Week"
FROM "10_Areas/Career/Internships/Programs/Serious" OR "10_Areas/Career/Internships/Programs/Considering"
WHERE pay_per_week
SORT pay_per_week DESC
```
## 🎯 This Week
Work this from [[_This Week]] and [[Now]], not from here — this dashboard is for scanning the whole system, those notes are for doing.
## 📚 External Resources
See [[Links & Interlinks]] for job boards and career-fair links, [[20_Progress/Internship/Building System/Research Loop - Resources]] for the loop's own data sources.
