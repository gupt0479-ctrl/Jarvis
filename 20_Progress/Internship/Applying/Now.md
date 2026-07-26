---
type: dashboard
status: active
created: 2026-07-26
notes:
  - "[[Applications-to-Create]]"
  - "[[_This Week]]"
  - "[[Applying Template]]"
tags:
  - internship
  - dashboard
next: "First real row lands once a Tracker note moves from Current/ to Applied/."
---
# Now — Every Internship Currently Being Applied To
==The single source of truth for what's actually in motion right now, across the whole pipeline — not curated, not weekly, exhaustive.== [[_This Week]] is the short Friday list; this is everything, live, pulled straight from real Applying notes.
## In Flight
```dataview
TABLE WITHOUT ID
  file.link as "Application",
  company as "Company",
  status as "Stage",
  date_applied as "Applied",
  next_deadline as "Next Deadline"
FROM "20_Progress/Internship/Applying"
WHERE status AND status != "Offer" AND status != "Rejected" AND status != "Withdrawn"
SORT next_deadline ASC
```
## Waiting Longest Without An Update
```dataview
TABLE WITHOUT ID
  file.link as "Application",
  date_applied as "Applied",
  date(today) - date_applied as "Days Waiting"
FROM "20_Progress/Internship/Applying"
WHERE status = "Applied" AND date_applied
SORT date_applied ASC
LIMIT 5
```
> [!NOTE]
> Respond to any recruiter reply within 24 hours — interview slots fill in batches. Follow up on anything applied to more than a month ago per the Friday ritual in [[_This Week]].
