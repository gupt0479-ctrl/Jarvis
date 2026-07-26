---
created: 2026-07-09
updated: 2026-07-26
type: evergreen
status: sprout
tags:
  - evergreen
  - career
notes:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
---
# README — Internships Folder
Start at [[Internships Hub]] for what this domain covers and why it's split from `20_Progress/Internship/`. This file is the mechanical folder guide — what goes where, not why.
## Folder Map
| Folder | Holds | Template |
| --- | --- | --- |
| `List/` | Monthly capture logs of manually-found postings, plus `Dossiers/` — auto-discovered by `internship-research-loop`, screened for eligibility and CS/software relevance, sorted into priority subfolders (`1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`); `Viewed/` is a human triage bin, not pipeline output | [[List Monthly Log Template]] |
| `Programs/Serious/` and `Programs/Considering/` | Static research, one note per program that passed the fit test — identical template and depth in both; the split is preference/timing only (pursuing now vs. later/undecided), never rigor | [[Program Template]] |
| `Contacts/` | `Each One/` — one contact note per internship (recruiter/HR/public info, researched by the loop's `enrich.py` on promotion); `Mimic.md` is the outreach-message template library | [[Contact Template]] |
| `Cheats/` | Proven tactics and methods | [[Cheat Template]] |
| `Tracker/` | Dashboard (detailed) and Kanban (glance); `Each One/` — one dated index note per committed internship, the fast-scan source of truth until an Applying note exists | — |
## Rewritten 2026-07-16
This README previously documented a one-time 2027-cycle setup guide (13 hardcoded programs, a single-tier tracker). That content is superseded by [[30_Order/Workflows/Internship Pipeline]], which splits static research (here) from live status (`20_Progress/Internship/Applying/`). The full session record of that redesign is in [[System - Build Log]].
## Updated 2026-07-26
Added the priority-folder dossier system, the `Programs/Serious` + `Programs/Considering` split, and `Tracker/Each One` + `Contacts/Each One` — see [[30_Order/Workflows/Internship Pipeline]] for the full sequence and [[20_Progress/Internship/Building System/Claude Code Prompts]] for the codebase side of this change.
