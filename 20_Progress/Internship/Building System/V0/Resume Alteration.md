---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - resume
  - system
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[30_Order/Workflows/Application Document Preparation]]"
  - "[[30_Order/Standards/Resume Alteration Standard]]"
  - "[[Cover Letter Alteration]]"
  - "[[Humanizer]]"
next: Rebuild Main Resume.md into the evidence-tagged structure this note assumes — gated on the human reviewing Resume Alteration Standard first (see 'Not Yet Built' below).
---
# Resume Alteration
==Was an empty stub until 2026-08-28. This is the design note for turning [[20_Progress/Internship/Resumes/Main Resume]] — currently a vague bullet bank behind a PDF — into a real per-application resume system.== Written after a discovery session that clarified the missing piece in [[30_Order/Workflows/Internship Pipeline]]: nothing defined what actually happens between "I found a program" and "a resume exists that's actually tailored to it." This note is that definition. The enforceable rules live in [[30_Order/Standards/Resume Alteration Standard]]; this note is the narrative — why the system is shaped this way and how it fits the rest of the pipeline.

## Scope
Governs the Main Resume master (`Resumes/Main Resume.md` / `.docx` / `.pdf`) and every per-application tailored resume DOCX. Cover letters have their own parallel note, [[Cover Letter Alteration]] — the two systems are siblings, not one system with two outputs, because a resume and a cover letter get evaluated by different readers (ATS + skim vs. a human reading start to finish) and can be revised independently. The style/tone review both pass through before either is written lives in [[Humanizer]], not here.

## Current State (2026-08-28) — What's Actually True Right Now
- `Resumes/Main Resume.md` is real and editable, but its content is generic ("seeking internships where I can build reliable AI-driven products...") rather than evidence-specific, and it has never been rewritten since 2026-07-16.
- `Resumes/Main Resume.pdf` exists as the current output format. No canonical `.docx` exists yet.
- No per-application resume has ever been created. `Resumes/Altered/` (per [[30_Order/Workflows/Internship Pipeline]]'s old Step 5 text) and `Tailored/<company>.md` (per Main Resume's own stale `next:` field) are two different names for a folder/file pattern that was never actually built — both are superseded by the convention below, not reconciled between each other.
- The Cheats note [[10_Areas/Career/Internships/Cheats/Resume Tailoring, LinkedIn Search & Outreach Discovery]] still describes the old `Resumes/Altered/<company>.md` Markdown-cut workflow. That note is left as-is (out of scope for this session) but should be read as historical once the system below is actually built — its five-prompt JD-keyword sequence is still useful *content*, just not the file convention.

## The Master Resume (Three Artifacts, One Source of Truth)
1. **`Resumes/Main Resume.md`** — the source of truth. Structured, evidence-tagged bullets (mirroring the existing `#skill/...` tag convention), each one traceable to real work. Rebuilding this into that shape is a separate, later task — not done by this note, and gated on a human reviewing [[30_Order/Standards/Resume Alteration Standard]] first, since that standard is what defines what counts as evidence.
2. **`Resumes/Main Resume.docx`** — the canonical export, generated from the Markdown, never hand-edited independently of it. If a discrepancy exists between the two, the Markdown wins and the DOCX is regenerated.
3. **`Resumes/Main Resume.pdf`** — the submission-format export, generated the same way.
`Main Resume.*` are reserved filenames at the root of `Resumes/` — no per-application file is ever named this.

## The Evidence Rule (Load-Bearing)
Every claim in the master resume and every tailored resume must trace to one of three sources, same fail-closed discipline `internship-research-loop`'s own dossier/contact rules apply to job postings, applied here to resume content instead:
1. An already-approved bullet in `Main Resume.md`.
2. A fact drawn from a linked Jarvis project note (e.g. [[20_Progress/Projects/Research/BOOM/BOOM Systems Engineering Bullet]], the Arc/OpsPilot/Resq project notes, the NSEdu internship) — cited by note path, not paraphrased into an unsourced claim.
3. Content the human explicitly supplies when asked.
A JD requirement with no matching evidence anywhere in those three sources is logged as a **gap** in the content plan (see below) — never guessed, never filled with a plausible-sounding invention. This is the same asymmetry `internship-research-loop`'s permissive-by-default filtering uses for the opposite reason: there, a false exclusion is worse than a false inclusion; here, a false (invented) inclusion is worse than an honestly-reported gap, because a lie on a resume costs more than a resume that's honestly short one keyword.

## The Tailoring Boundary
**Allowed:** selecting which existing bullets appear, reordering them to lead with what the JD emphasizes, and accurately rephrasing wording to mirror the JD's own terminology (e.g. "built REST APIs" → "designed RESTful services" if that's genuinely what happened).
**Not allowed:** inventing a bullet, changing a real number, claiming a tool/skill that wasn't actually used, or inflating scope ("contributed to" becoming "led" without that being true). Full enumeration in [[30_Order/Standards/Resume Alteration Standard]].

## Per-Application Flow
Full step-by-step sequencing (with the cover-letter side folded in) lives in [[30_Order/Workflows/Application Document Preparation]]; this is the resume-specific half of it:
1. **Program/Contact/Tracker exist. No resume work happens yet.** Promotion (Internship Pipeline Step 3) stays document-free, confirmed in this session — a Program note commits research time, not writing time.
2. **An Applying note is created at the start of real application preparation** — not at submission, which is where the pipeline used to place it. `status: Preparing`, `date_applied: null`. It links the Program, Tracker, and Contact notes, and records the job URL plus one-line JD/networking/fit summaries (see the revised [[30_Order/Templates/Career/Applying Template]]).
3. **Creating that note is meant to invoke a drafting step** (once the resume-alteration skill/agent below is actually built): read `Main Resume.md`, the Applying note's JD/fit fields, and any linked Jarvis project notes; ask the human for anything a JD needs that isn't already sourced, rather than inventing it.
4. **The agent proposes a short, traceable content plan** before writing anything — which bullets, in what order, what's rephrased and why, which JD keywords are covered, which are honest gaps. This plan is what gets approved, not the final document sight-unseen.
5. **On explicit approval, and only after the plan passes the Humanizer gate** ([[Humanizer]]), write or overwrite exactly one file: `Resumes/<Role> - <Company>.docx` — same naming convention as the Program/Contact/Tracker notes it's paired with.
6. **Overwrite in place** for any revision made before `date_applied` is set on the Applying note — no `v1`/`v2` files, per the explicit decision that applying should stay a quick step. Once `date_applied` is set, the file is historical; changing a submitted application's resume is a new, explicit human decision (e.g. a real resubmission), not a background rewrite.
7. **The Applying note's `resume_version` field links to the file**, and its short Documents section carries a one-line plain-language summary of what the resume leads with — the actual reasoning lives in the content plan and the file itself, not duplicated as prose on the Applying note.

## Not Yet Built (Read This Before Assuming Any Of This Runs)
- Main Resume.md's rebuild into the evidence-tagged structure this note assumes.
- The actual DOCX-generation mechanism (tool choice — e.g. `python-docx` or a template-fill approach — is an implementation detail for the Cursor skill, not decided here).
- The resume-alteration drafting skill/agent itself — scaffolded at `.cursor/skills/resume-alteration/SKILL.md`, but it depends on the rebuilt Main Resume to have anything real to draft from.
Nothing in this note is live automation. It's the contract the next build has to satisfy.

## Interfaces
- [[30_Order/Standards/Resume Alteration Standard]] — the enforceable evidence/source/naming/overwrite rules.
- [[30_Order/Workflows/Application Document Preparation]] — where this slots into [[30_Order/Workflows/Internship Pipeline]] Step 5, alongside the cover-letter half.
- [[Humanizer]] — the pre-write style gate every draft passes through.
- [[Cover Letter Alteration]] — the sibling system for the other half of an application packet.
