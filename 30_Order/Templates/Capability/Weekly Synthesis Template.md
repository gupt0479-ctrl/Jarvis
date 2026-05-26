---
type: evergreen
status: tree
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - evergreen
  - review
  - template
---
# Weekly Synthesis — <% tp.date.now("YYYY") %>-W<% tp.date.now("ww") %>

## Concepts Enriched This Week
Notes enriched or promoted since last review. Add manually or use the query below for recently updated concept notes.
```dataview
TABLE track, mastery_level, status, file.mtime AS "Updated"
FROM ""
WHERE type = "concept" AND track
AND file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```
## Overdue Drills
Concepts where `next_drill` has passed. Review these first.
```dataview
TABLE track, mastery_level, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND track AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```
## Unresolved Questions
Open questions across all tracks.
```dataview
TABLE track, question_kind, question_status
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND question_status != "resolved"
SORT track ASC
```
## Outputs Created
New outputs since last review.
```dataview
TABLE output_kind, track, source_concepts
FROM "60_Claude/45_Outputs"
WHERE type = "output"
AND file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```
## Synthesis Candidates
1-3 cross-track connections worth pursuing this week:
- [ ] _Candidate 1_: (describe the connection between two concepts from different tracks)
- [ ] _Candidate 2_: (describe another cross-track insight)
- [ ] _Candidate 3_: (optional third candidate)
## Notes
_Free-form observations, blockers, or adjustments to the capability system._