---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - process
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Programs/Programs MOC]]"
  - "[[20_Progress/Internship/Building System/Claude Code Prompts]]"
next: "Build the promote-dossier skill per [[20_Progress/Internship/Building System/Claude Code Prompts]] — nothing in this folder is hand-created until that exists."
---
# Programs — How Notes Get Created Here
==Nothing in `Programs/` gets typed from a hardcoded target list anymore.== This note replaces the old plan of that shape (13 hand-picked companies, written once at the start of a cycle) — that approach is retired, not archived under a different name; git history holds it if it's ever needed again. What replaced it: every Program note here is created the same way a dossier is — driven by code, from `gupta-builds/internship-research-loop` — except gated by explicit manual consent at every step. Nothing writes into this folder silently.
## The Actual Process
1. A dossier (or a hand-found lead that never went through the automated pipeline) passes the fit test — see [[30_Order/Workflows/Internship Pipeline]] Step 2. Goal-push, personal fit, contact-reachability noted-not-gated, pay never a factor.
2. You invoke the promotion skill (`gupta-builds/internship-research-loop`'s `.claude/skills/promote-dossier` once built — see [[20_Progress/Internship/Building System/Claude Code Prompts]] for the build spec). It asks two small things: which folder (`Serious/` or `Considering/`) and whether the dossier's auto-assigned priority/category still holds or needs a human override.
3. The skill runs contact research (`enrich.py`, promotion-triggered, same as always) and shows you what it found before writing anything.
4. On your explicit go-ahead, three notes get created together, cross-linked: the Program note (here), a Contacts/Each One note, and a Tracker/Each One note.
## Serious vs. Considering
Identical template, identical research depth, in both folders. The only variable is preference/timing — pursuing this one now (`Serious/`) versus interested but not yet, or needs more thought first (`Considering/`). A thinner Considering note is a mistake, not a shortcut — fix it if you see one.
## Manual Finds
A lead you found yourself (career fair, a referral, LinkedIn) that never became a dossier enters at the same step 1 above — it just arrives without an originating dossier link. Everything downstream is identical.
