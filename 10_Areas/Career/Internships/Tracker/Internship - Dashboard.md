---
created: 2026-07-09
updated: 2026-07-16
type: evergreen
status: active
tags:
  - internships
  - tracking
  - career
  - dashboard
notes:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
---
# 📊 Internship Tracker Dashboard
Two kinds of query below, and they don't mix: **research** tables pull static facts from `Programs/` (comp, deadlines, eligibility — these don't change once written). **Pipeline** tables pull live status from `20_Progress/Internship/Applying/` (funnel stage, dates — these change every time you hear back). See [[30_Order/Workflows/Internship Pipeline]] for why they're split. The kanban glance view is [[Tracker]].
## ⏰ Research — Upcoming Deadlines (Next 30 Days)
```dataview
TABLE
  company,
  opens_date,
  deadline_real as "Real Deadline",
  pay_per_week as "Pay/Week",
  eligible_classes as "Eligible"
FROM "10_Areas/Career/Internships/Programs"
WHERE deadline_real <= date(today) + dur(30 days)
SORT deadline_real ASC
```
> [!WARNING]
> Real deadlines run ahead of posted deadlines on most programs — apply in the first two weeks a portal opens, don't wait for the posted date.
## 🔄 Pipeline — Live Status
```dataview
TABLE WITHOUT ID
  file.link as "Application",
  company as "Company",
  status as "Stage",
  date_applied as "Applied",
  next_deadline as "Next Deadline"
FROM "20_Progress/Internship/Applying"
WHERE status != "Rejected" AND status != "Withdrawn"
SORT next_deadline ASC
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
### Funnel Counts
```dataview
TABLE WITHOUT ID
  rows.status as "Status",
  length(rows) as "Count"
FROM "20_Progress/Internship/Applying"
GROUP BY status
```
## 💰 Research — Sorted By Compensation
```dataview
TABLE
  company as "Company",
  program_type as "Type",
  pay_per_week as "Pay/Week",
  deadline_real as "Deadline"
FROM "10_Areas/Career/Internships/Programs"
WHERE pay_per_week
SORT pay_per_week DESC
```
## 🌊 Research — By Wave
```dataview
TABLE
  company,
  eligible_classes,
  opens_date,
  deadline_real,
  pay_per_week
FROM "10_Areas/Career/Internships/Programs"
WHERE wave
SORT wave ASC, deadline_real ASC
```
## ✅ Research — Total Programs Tracked
```dataview
LIST
FROM "10_Areas/Career/Internships/Programs"
WHERE name
```
## 🎯 This Week
Work this from `20_Progress/Internship/Applying/_This Week.md`, not from here — this dashboard is for scanning, that note is for doing.
## 📚 External Resources
See [[Links & Interlinks]] for job boards, career fair links, and mock-interview resources.
