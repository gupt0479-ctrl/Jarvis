---
type: evergreen
status: active
created: 2026-07-26
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Tracking Template]]"
  - "[[Application Tracker]]"
tags:
  - internship
  - process
next: "Point Application Tracker.md's Current/Applied/Rejected/Accepted sections at these folders once real Tracker notes exist to query."
---
# Tracker/Each One — How Notes Get Created Here
==One dated index note per internship that's made it to a Program note — the fast-scan source of truth for "where does this stand" until a real Applying note exists.== Created only after the Program note exists, per [[Tracking Template]]'s frontmatter contract. Not a duplicate of the Applying note — Tracker is the *timeline* (dates, links, deadline), Applying is the *narrative* (Current State, Next Action, Open Questions, meeting-prep content). Both stay live at once once an application starts; they don't replace each other.
## The Three Folders
- **`Current/`** — the internship is being actively researched or pursued, no application submitted yet. Default location for a newly-created Tracker note.
- **`Applied/`** — an application has actually been submitted (the paired Program note has moved to its own `Ended/` folder at the same time — see `Programs/Programs-to-Create.md`). Waiting on a response.
- **`Result/`** — an outcome has landed — offer, rejection, or withdrawal. The `result` and `date_result` frontmatter fields get set at the same time the note moves here.
Move the note as the real state changes; this mirrors the Program note's own `Ended/` transition and should happen in the same sitting, not drift out of sync.
## What Belongs In The Note
Per [[Tracking Template]]: `date_noted`, `date_researched`, `date_created`, `date_applied`, `date_result`, `result`, `deadline`, links to the Program note, the Contacts note, and the originating dossier — the whole timeline in frontmatter, so [[Application Tracker]]'s Dataview board can actually query it. The body stays short: a one-line Next Action, nothing that duplicates what the Applying note already carries once one exists.
## Why This Exists Separately From Application Tracker.md
[[Application Tracker]] is the aggregate board — every internship, one row each, grouped by stage. This folder is where the underlying per-internship detail actually lives; the board is a view over it, not a second source of truth. Never hand-edit the board's tables directly — fix the underlying Tracker note and let the Dataview query reflect it.
