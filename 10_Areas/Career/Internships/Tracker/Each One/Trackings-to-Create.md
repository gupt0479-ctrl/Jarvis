---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-09-04
notes:
  - "[[Internship Pipeline]]"
  - "[[Tracking Template]]"
  - "[[Application Tracker]]"
  - "[[30_Order/Standards/Internship/Internship Tracker Standard]]"
tags:
  - internship
  - process
next: Point Application Tracker.md's Current/Applied/Rejected/Accepted sections at these folders once real Tracker notes exist to query.
---
# Tracker/Each One — How Notes Get Created Here
==One dated index note per internship that's made it to a Program note — the fast-scan source of truth for "where does this stand" until a real Applying note exists.== Created only after the Program note exists, per [[Tracking Template]]'s frontmatter contract. Not a duplicate of the Applying note — Tracker is the *timeline* (dates, links, deadline), Applying is the *narrative* (Current State, Next Action, Open Questions, meeting-prep content). Both stay live at once once an application starts; they don't replace each other. Field-level rules and the `Current/`→`Applied/`→`Result/` lifecycle are fully specified in [[30_Order/Standards/Internship/Internship Tracker Standard]] — this note covers only *when and how* a Tracker note gets created, not its content rules in full.
> [!WARNING]
> **Real gap, confirmed 2026-09-04.** The rule below ("created only after the Program note exists") should mean every real Program note has a paired Tracker note. It doesn't: the three manual-web-find promotions ([[10_Areas/Career/Internships/Programs/Serious/2027-Uber-SWE-CareerPrep]], [[10_Areas/Career/Internships/Programs/Serious/2027-WesternDigital-SWE-EarlyCareer]], [[10_Areas/Career/Internships/Programs/Serious/2027-Deepgram-SWE-VoiceAI]], all 2026-07-29) have no paired Tracker note, confirmed by direct folder search — only Appian (the one `/promote-dossier`-driven promotion) got the full three-note trio. Same finding as [[10_Areas/Career/Internships/Contacts/Each One/Contacts-to-Create]]'s parallel gap — flagged, backfill optional, not resolved here.
## The Three Folders
- **`Current/`** — the internship is being actively researched or pursued, no application submitted yet. Default location for a newly-created Tracker note.
- **`Applied/`** — an application has actually been submitted (the paired Program note has moved to its own `Ended/` folder at the same time — see `Programs/Programs-to-Create.md`). Waiting on a response.
- **`Result/`** — an outcome has landed — offer, rejection, or withdrawal. The `result` and `date_result` frontmatter fields get set at the same time the note moves here.
Move the note as the real state changes; this mirrors the Program note's own `Ended/` transition and should happen in the same sitting, not drift out of sync.
## What Belongs In The Note — Field By Field
Per [[Tracking Template]]: `date_noted`, `date_researched`, `date_created`, `date_applied`, `date_result`, `result`, `deadline`, links to the Program note, the Contacts note, and the originating dossier — the whole timeline in frontmatter, so [[Application Tracker]]'s Dataview board can actually query it.
- **Timeline (including "Internship released"/"Internship Close")** — the internship's own real dates (when the portal opened, when it actually closes), not your dates. Fill these from the Program note's Traps/Eligibility research, not a guess.
- **Summary** — what is the internship actually about, and how does it specifically clear all four hard gates (timing, US, OPT, CS-relevance)? Why does this one matter — is it Considering or Serious, and why that call? How does it connect to what you're currently building or working on? This is the section that has to justify the internship's presence here, not just describe it.
- **Company Information** — a short summary plus the interlink to the deeper [[Job & Company]] note once one exists. Don't duplicate that note's depth here; point to it.
- **Conversation** — the real summary of what's actually been said with the recruiter/contact, plus concrete follow-up actions. Pulls from the Contacts note's Conversation Log, doesn't replace it.
- **Interview Steps** — left blank until you actually reach that stage; don't pre-fill speculative rounds.
- **Loop Process** — once this internship's outcome lands (or it's dropped), a short, visually clean note on how long the *entire* process took, start to finish. This is the number that eventually tells you whether the loop itself is fast enough to be worth running.
The body stays otherwise short: a one-line Next Action, nothing that duplicates what the Applying note already carries once one exists.
## Why This Exists Separately From Application Tracker.md
[[Application Tracker]] is the aggregate board — every internship, one row each, grouped by stage. This folder is where the underlying per-internship detail actually lives; the board is a view over it, not a second source of truth. Never hand-edit the board's tables directly — fix the underlying Tracker note and let the Dataview query reflect it.
