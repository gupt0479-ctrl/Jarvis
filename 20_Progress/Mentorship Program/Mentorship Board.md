---
type: index
status: sprout
created: 2025-12-25
updated: 2026-08-08
tags:
  - moc
  - mentorship
notes:
  - "[[Mentor Details]]"
  - "[[Plan]]"
  - "[[Mentor Meeting Playbook]]"
  - "[[Fall 2026 — Detailed Expectations]]"
  - "[[adx]]"
next: Hold the first fall meeting under the confirmed alternate-week cadence
---
# Mentorship Board
## Purpose
This is the control surface for the Ahnaf mentorship program — every meeting, plan, and open thread lives under this folder. Read this before opening any individual note inside it.
## Map
[[Mentor Details]] holds who Ahnaf is — Senior Engineering Manager at Best Buy, matched through the CSE Mentor Program — and how to reach him. [[Plan]] is the standing goals document: its `## Summer` section carries the live 4-Goals framework (Relationship, Project + build review, Startup fundamentals, Professional image), the 5-month roadmap, and the standing meeting format; `## Fall 2026` stays intentionally short, pointing at [[Fall 2026 — Detailed Expectations]] rather than pre-deciding fall content before real meetings generate it.
[[Mentor Meeting Playbook]] is the format every meeting follows — Demo → Shipped/Blocked/Deciding → Ask — and its Session Log is the append-only record of what was actually said. The most recent entry, 2026-07-14, is where **adx** — [[adx|Ahnaf's own Agent Development Kit]] — became the real center of gravity of the relationship, ahead of the original four goals.
Each meeting now moves through three folders under `Meetings/`: the raw call lands untouched in `Transcripts/`, `/transcript-to-brief` turns it into a dated brief in `Briefs/` — [[Project Briefings - 2026-07-13]] is the current real example — and `/note-to-actions` turns that brief into a link-dense action note in `Action/` once one exists for a given meeting. [[Mentor Meeting - One-Pager]] and [[Mentor Meeting - Hackathons, Summer, and Networking]] are both superseded, kept for history rather than as live references.
[[Fall 2026 — Detailed Expectations]] is where fall actually gets planned — not by guessing now, but by accumulating what Ahnaf raises meeting by meeting, checked against the program's original [Detailed Goals doc](https://docs.google.com/document/d/1xu8pmUATj1jrVf_2csw1lUbGaV-3YZnP202AI1CzYKw/edit?usp=sharing) for how far the relationship has actually moved since it started.
## Status
| Thread | State |
|---|---|
| Cadence | Alternate weeks, confirmed for fall — unchanged from summer |
| Fall 2026 content | Not yet written — accumulates from real meetings via [[Fall 2026 — Detailed Expectations]] |
| adx contribution | Contingent on what Ahnaf raises; primary currency of the relationship through fall per the 2026-07-14 Session Log entry |
| Second mentor | Idea for fall enrollment, different purpose — not yet built out |
## Dataview
```dataview
TABLE status, deadline, related_progress, next
FROM "20_Progress/Mentorship Program"
WHERE (type = "project" OR type = "brainstorm")
SORT deadline ASC
```
## Links
[[adx]] — Ahnaf's Agent Development Kit, [ahnafyy/adx](https://github.com/ahnafyy/adx); the codebase-review notes live under `20_Progress/Mentorship Program/adx/`.
