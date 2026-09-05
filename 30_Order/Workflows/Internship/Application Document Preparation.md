---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-09-04
tags:
  - system
  - workflow
  - internship
  - career
notes:
  - "[[Internship Pipeline]]"
  - "[[Resume Alteration]]"
  - "[[Cover Letter Alteration]]"
  - "[[Humanizer]]"
  - "[[Resume Alteration Standard]]"
  - "[[Cover Letter Alteration Standard]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
next: Build the resume-alteration and cover-letter-alteration Cursor skills for real, once Main Resume.md and Main Cover Letter.md exist in their evidence-tagged shape.
---
# Application Document Preparation
==Moved here 2026-09-04 from the top-level `30_Order/Workflows/` folder, content unchanged== — it's internship-specific end to end (reads/writes the Applying note, gates on internship-loop-specific Standards), and its sibling docs ([[Internship - Design Rationale]], [[Internship Pipeline]], [[Promotion]]) already moved into `30_Order/Workflows/Internship/` during the same reorg. This file wasn't migrated with them; no scope reason found for leaving it behind, so it moves now.

==The sub-workflow [[Internship Pipeline]] Step 5 (Tailor) now runs, folding resume and cover-letter drafting into one sequence sharing a single Applying note and a single approval gate.== Written 2026-08-28 alongside [[Resume Alteration]] and [[Cover Letter Alteration]] — read those two for *why* the rules below exist; this note is only the *sequence*.

## Relationship To Internship Pipeline
This changes when the Applying note gets created. Previously (per the Pipeline's old Step 7 text), the Applying note was created **at submission**, in the same sitting as actually applying. That's too late for a note-created drafting step to have anything to prepare — the application would already be out the door. As of this note:
- **Program note creation (Step 3) stays document-free.** No resume or cover-letter work happens at promotion — confirmed explicitly in the discovery session for this note. Promotion commits research time, not writing time.
- **The Applying note is created at the start of real application preparation** — i.e., at the beginning of what used to be Step 5 (Tailor) — not at submission. `status: Preparing`, `date_applied: null`.
- **Step 7 (Apply) narrows** to: submit, set `date_applied`, move status to `Applied`, move the Tracker note `Current/` → `Applied/`, move the Program note to its own `Ended/` subfolder. The Applying note itself already exists by this point.

## The Sequence
```
prepare        Applying/<name>.md (30_Order/Templates/Career/Applying Template) created — before any
               document exists. status: Preparing, date_applied null. Links program/tracker/contact,
               records the job URL, and one-line JD/networking/fit summaries.
   ↓ note creation is meant to invoke the drafting step, once built
draft          resume-alteration + cover-letter-alteration skills/agent read Main Resume.md /
               Main Cover Letter.md, the Applying note's JD/fit/networking fields, and linked Jarvis
               project notes. Anything a JD needs that isn't already sourced → ask the human, never invent.
   ↓
plan           agent proposes a short, traceable content plan for each document — which bullets/
               paragraphs, in what order, what's rephrased and why, which JD keywords are covered,
               which are honest gaps. Nothing is written yet.
   ↓
approve        human reviews the plan(s) — explicit yes/no, same consent discipline as /promote-dossier.
               Changes route back to the plan step, not a partial write.
   ↓ on yes
humanize       each approved plan passes the Humanizer gate (Humanized Writing Standard) before
               anything is written. A fail routes back to draft/plan with specific flags, never a
               silent rewrite.
   ↓ pass
write          write or overwrite exactly one Resumes/<Role> - <Company>.docx and exactly one
               Cover Letters/<Role> - <Company>.docx. Overwrite in place on any revision made before
               date_applied is set — no v1/v2 files.
   ↓
link           Applying note's resume_version / cover_letter fields point at the two files; its short
               Documents section gets a one-line summary of what each leads with — not the full content.
   ↓ actually ready to apply (Pipeline Step 6 — Deep Dive — may happen here too)
apply          submit. Applying note: date_applied set, status → Applied. Tracker Current/ → Applied/.
               Program → its own Ended/ subfolder. (Internship Pipeline Step 7.)
```

## Approval Is One Gate, Not Two Separate Sign-Offs Per Document
The resume and cover letter share one Applying note and are drafted, planned, and approved together in one sitting — the point of "applying should stay a quick step," stated explicitly in the discovery session for this note. Building two entirely separate approval conversations for one application would work against that.

## Overwrite, Not Version
Both documents follow the same rule (full reasoning in [[Resume Alteration Standard#6. Overwrite Policy]] and its cover-letter mirror): one file per application, overwritten in place pre-submission, frozen post-submission. This is a deliberate choice against versioning (`v1`/`v2`) specifically to keep this workflow fast.

## What Actually Runs Today (2026-09-04)
None of the `draft` / `plan` / `humanize` / `write` steps are live — there is no drafting skill/agent yet, `Main Resume.md` isn't in evidence-tagged shape, and `Main Cover Letter.md` doesn't exist. The `prepare` step (creating the Applying note early, with the revised template fields) is the only part of this sequence that's actually actionable today, by hand. See each design note's own "Not Yet Built" section for what has to exist first. Confirmed still true as of 2026-09-04 (re-checked against [[20_Progress/Internship/Building System/Resume & Cover Letter - System Map]]'s own Status section, not assumed carried-forward).

## Interfaces
- [[Internship Pipeline]] — the parent pipeline this slots into (Steps 5–7).
- [[Resume Alteration]] / [[Resume Alteration Standard]] — resume-side rules.
- [[Cover Letter Alteration]] / [[Cover Letter Alteration Standard]] — cover-letter-side rules.
- [[Humanizer]] / [[30_Order/Standards/Humanized Writing Standard]] — the shared tone gate.
- [[Applying Template]] — the note this sequence starts from.
