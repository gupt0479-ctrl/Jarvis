---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-09-04
notes:
  - "[[Internship Pipeline]]"
  - "[[Applying Template]]"
  - "[[Now]]"
  - "[[_This Week]]"
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
tags:
  - internship
  - process
next: First real entry lands once a real Tailor pass actually starts for a real application — no Applying note exists yet, since Main Resume.md is still generic filler and Main Cover Letter.md doesn't exist (see [[20_Progress/Internship/Building System/Resume & Cover Letter - System Map]]'s Status section).
---
# Applying — How Notes Get Created Here
==One Applying note per internship, created at the **start** of real application preparation — the beginning of [[Internship Pipeline]] Step 5 (Tailor), not at submission and not just because a Program note exists.== Corrected 2026-09-04: this note previously said the Applying note is created at submission, in the same sitting as the Tracker/Program folder-moves. That was true of the *original* Pipeline Step 7 text but is now stale — [[30_Order/Workflows/Internship/Application Document Preparation]] (2026-08-28) moved the note's creation earlier specifically so a drafting step has something real to prepare against. Nothing has run through this sequence for real yet — zero Applying notes exist as of this writing — so everything below is the specified target process, not a proven one; treat the first real run as the thing to check this against, the same discipline [[30_Order/Standards/Internship/Internship Tracker Standard]] used for its own one-real-example caveat.
## The Trigger — Now `prepare`, Not `apply`
Per [[30_Order/Workflows/Internship/Application Document Preparation]]'s full sequence (`prepare → draft → plan → approve → humanize → write → link → apply`), reproduced here at the level this folder needs:
1. **`prepare`** — the Applying note is created now, from [[Applying Template]]. `status: Preparing`, `date_applied: null`. Links `program`/`contact`/the originating Tracker note, records the job URL, and one-line JD/networking/fit summaries. Neither the Tracker note nor the Program note moves yet — the Tracker note stays in `Current/`, the Program note stays in `Serious/` or `Considering/`.
2. **`draft` → `plan` → `approve` → `humanize` → `write` → `link`** — the resume/cover-letter drafting sequence runs against this note (full detail: [[30_Order/Workflows/Internship/Application Document Preparation]], [[Resume Alteration Standard]], [[Cover Letter Alteration Standard]]). This Applying note's JD/fit/networking fields and Documents section are what that sequence reads from and writes back to — nothing here duplicates those Standards' content rules, this folder only owns *when the note exists and what triggers each state change*.
3. **`apply`** — only *now*, at actual submission, do the three folder-moves that used to define "the Trigger" actually happen, all in the same sitting: `date_applied` set, `status` → `Applied`, the paired Tracker note moves `Current/` → `Applied/`, the paired Program note moves into its own `Ended/` subfolder, and an entry is added to [[Now]].
This means an Applying note can exist for a real, extended period in `status: Preparing` while its paired Tracker note is still sitting in `Current/` and its paired Program note is still in `Serious/`/`Considering/` — that's the expected mid-sequence state, not a sign something's out of sync. Only the *final* apply step syncs all three.
## What Belongs In The Note — Section By Section
- **Goal** — one real sentence on what winning looks like for *this specific* program, not a generic "get an offer."
- **Current State** — where this application actually stands: funnel stage, what's blocking it, what you're waiting on. Use the diagnostic split from [[System - Build Log]]'s research: a response rate under 10% signals a resume/targeting problem, responses without offers signal an interview-prep problem — write which one this looks like, not just the raw status.
- **Interlinks → Contact** — a short brief of the actual meeting/conversation with the person, pulled from the Contact note's Conversation Log, not restated in full.
- **Interlinks → Job Detail** — the handful of things you'd genuinely need to remember walking into a call about this role — pulled from the Job & Company note, not the whole thing copied over.
- **Next Action** — the single next physical move, mirroring the `next:` frontmatter field exactly.
- **Open Questions** — anything genuinely unresolved that would change how you'd act — not a checklist of routine steps.
- **Log** — dated, one line per real event (submitted, heard back, screen scheduled) — this is the audit trail, keep it factual and short.
## Now.md — The Single Source Of Truth
[[Now]] lists every internship currently mid-application — the one place to look for "what am I actually waiting on right now" across the whole pipeline, pulled from real Applying notes, not maintained separately by hand. Update it whenever an Applying note's status changes; don't let it drift into a second, stale copy of what the individual notes already say.
## Applied/ Folder
Once an Applying note's outcome is known either way (offer, rejection, withdrawal), it moves into `Applying/Applied/` — the archive of everything that ran its course, kept for reference (a rejection today can be a referral-worthy relationship next cycle) rather than deleted.
## Relationship To _This Week.md
[[_This Week]] is the weekly-curated subset — what's actually in motion this Friday, not the exhaustive list. `Now.md` is exhaustive; `_This Week.md` is the short list you actually touch each week. Don't duplicate content between them — `_This Week.md` links to the real Applying notes, it doesn't restate their content.
