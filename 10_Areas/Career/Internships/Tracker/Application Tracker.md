---
type: dashboard
status: active
created: 2026-07-26
notes:
  - "[[Tracking Template]]"
  - "[[Trackings-to-Create]]"
  - "[[Internship - Dashboard]]"
tags:
  - internship
  - dashboard
next: "First real rows land once a Tracker/Each One note actually exists."
---
# Application Tracker
## Overview
==Tracks the research, contact, and application state into one board for every internship in this loop.== Every row here is a real note in `Tracker/Each One/`, per [[Tracking Template]]. As soon as an application is actually sent, its Tracker note moves folders (`Current/` → `Applied/`) and this board reflects it automatically — nothing here is hand-maintained.
## Current
```dataview
TABLE company, deadline, date_researched as "Researched"
FROM "10_Areas/Career/Internships/Tracker/Each One/Current"
SORT deadline ASC
```
## Applied
```dataview
TABLE company, date_applied as "Applied", date(today) - date_applied as "Days Waiting"
FROM "10_Areas/Career/Internships/Tracker/Each One/Applied"
SORT date_applied ASC
```
## Rejected
```dataview
TABLE company, date_result as "Date"
FROM "10_Areas/Career/Internships/Tracker/Each One/Result"
WHERE result = "Rejected"
SORT date_result DESC
```
## Accepted
```dataview
TABLE company, date_result as "Date"
FROM "10_Areas/Career/Internships/Tracker/Each One/Result"
WHERE result = "Offer"
SORT date_result DESC
```
## All Outcomes
```dataview
TABLE company, result, date_result as "Date"
FROM "10_Areas/Career/Internships/Tracker/Each One/Result"
SORT date_result DESC
```
