---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - cover-letter
  - standard
notes:
  - "[[20_Progress/Internship/Building System/Cover Letter Alteration]]"
  - "[[30_Order/Workflows/Application Document Preparation]]"
  - "[[30_Order/Standards/Resume Alteration Standard]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
next: null
---
# Cover Letter Alteration Standard
==The enforceable rules behind [[20_Progress/Internship/Building System/Cover Letter Alteration]].== Mirrors [[30_Order/Standards/Resume Alteration Standard]]'s structure; only the content-specific rules differ (a cover letter is read start to finish by a human, not skimmed and keyword-matched, so its rules are about narrative selection and length, not bullet ordering).

## Scope
Governs `20_Progress/Internship/Cover Letters/Main Cover Letter.md` / `.docx` / `.pdf` (not yet built) and every per-application cover letter DOCX in that folder. Does not govern the resume side or the tone/style checklist itself (see [[30_Order/Standards/Humanized Writing Standard]]).

## 1. Source-of-Truth Hierarchy
`Main Cover Letter.md` is authoritative once built — a paragraph/story bank of reusable, evidence-backed narrative fragments (opening hooks, experience paragraphs, closings). `.docx`/`.pdf` are generated exports, never hand-edited independently. A per-application letter selects and recombines fragments from the master plus anything explicitly approved as a one-off addition during that application's content-plan review.

## 2. Evidence-Only Claims (Fail-Closed)
Same three-source rule as [[30_Order/Standards/Resume Alteration Standard#2. Evidence-Only Claims (Fail-Closed)]]: every paragraph traces to an approved fragment in `Main Cover Letter.md`, a linked Jarvis project note, or an explicit human-supplied fact. A cover letter is the format most tempting to fabricate in — invented enthusiasm ("I've always dreamed of working at X") and invented specific company facts are both violations of this rule, not exempt from it because they read as "just tone."
- Flag: any company-specific fact, personal claim, or connection stated with no traceable source.
- Pass: a real fact about the company (from the Program note's Company Information section, or real contact-research findings) cited to where it came from.

## 3. Selection and Length
- Select **2–3 real, evidence-backed experiences** that map most directly to the JD's top requirements — not more. A letter that tries to cover everything reads as generic by trying to be complete.
- Open with something specific to the company — a real product, problem, or initiative, never a generic "I am passionate about your mission" line.
- Default length: **250–350 words**. Deviating needs a stated reason (the company explicitly asks for a different format) — not a default drift toward longer or shorter.

## 4. File and Naming Convention
- `Main Cover Letter.md`, `.docx`, `.pdf` are reserved names at the root of `20_Progress/Internship/Cover Letters/`.
- Every per-application letter is `<Role> - <Company>.docx` in that same folder — identical convention to the resume side and to Program/Contact/Tracker notes.

## 5. Overwrite Policy
One cover letter file per application, overwritten in place until `date_applied` is set on the paired Applying note, then treated as historical — identical rule to [[30_Order/Standards/Resume Alteration Standard#6. Overwrite Policy]].

## 6. Approval Gate
Same two-gate sequence as the resume side: explicit human approval of the content plan, then a pass through the Humanizer gate (see [[30_Order/Standards/Humanized Writing Standard]]), in that order, before any file is written or overwritten.

## Done When
- `Main Cover Letter.md` exists with real, evidence-backed, reusable fragments — not a single fixed letter copy-pasted per application.
- Every per-application letter names 2–3 real experiences, each traceable to §2's sources.
- No letter exceeds the 250–350 word default without a stated reason on the content plan.
