---
type: input
input_kind: listing
status: active
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
tags:
  - internship
  - list
next:
---
# <% tp.file.title %>
Generated view, not hand-typed — every row is a dossier file in `List/Dossiers/`, written either by you (manual quick-add) or the research loop (automated find). This file just queries them for this month. See [[Internship Pipeline]].
## Postings
```dataview
TABLE company, title as "Role", url as "Link", category, matched_reason as "Why It Matched", status
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE date_found >= date(this.month + "-01") AND date_found < date(this.month + "-01") + dur(1 month)
SORT date_found DESC
```
## Promotion Rule
A dossier's `status` moves from `unreviewed` to a link (`promoted: "[[Programs/Company - Role]]"`) only when you decide to seriously pursue it — see [[Internship Pipeline]]. Promotion creates a Programs note (static research) and an Applying note (live status) together.
