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
  - "[[Cover Letter Alteration]]"
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
  - "[[Resume Alteration Standard]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
  - "[[30_Order/Templates/Career/Internship/Cover Letter Template]]"
next:
---
# Cover Letter Alteration Standard
==The enforceable rules behind [[Cover Letter Alteration]].== Mirrors [[Resume Alteration Standard]]'s structure; only the content-specific rules differ (a cover letter is read start to finish by a human, not skimmed and keyword-matched, so its rules are about narrative selection and length, not bullet ordering).

## Scope
Governs `20_Progress/Internship/Cover Letters/Main Cover Letter.md` / `.docx` / `.pdf` (not yet built) and every per-application cover letter DOCX in that folder. Does not govern the resume side or the tone/style checklist itself (see [[30_Order/Standards/Humanized Writing Standard]]).

## 1. Source-of-Truth Hierarchy
`Main Cover Letter.md` is authoritative once built — a paragraph/story bank of reusable, evidence-backed narrative fragments (opening hooks, experience paragraphs, closings). `.docx`/`.pdf` are generated exports, never hand-edited independently. A per-application letter selects and recombines fragments from the master plus anything explicitly approved as a one-off addition during that application's content-plan review.

## 2. Evidence-Only Claims (Fail-Closed)
Same three-source rule as [[Resume Alteration Standard#2. Evidence-Only Claims (Fail-Closed)]]: every paragraph traces to an approved fragment in `Main Cover Letter.md`, a linked Jarvis project note, or an explicit human-supplied fact. A cover letter is the format most tempting to fabricate in — invented enthusiasm ("I've always dreamed of working at X") and invented specific company facts are both violations of this rule, not exempt from it because they read as "just tone."
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
One cover letter file per application, overwritten in place until `date_applied` is set on the paired Applying note, then treated as historical — identical rule to [[Resume Alteration Standard#6. Overwrite Policy]].

## 6. Approval Gate
Same two-gate sequence as the resume side: explicit human approval of the content plan, then a pass through the Humanizer gate (see [[30_Order/Standards/Humanized Writing Standard]]), in that order, before any file is written or overwritten.

## 7. Source Register — External Cover-Letter Guidance
Same tier definitions as [[Resume Alteration Standard#4. Source Register — External Resume-Writing Guidance]]. Full findings live in [[Resume & Cover Letter - ATS Research Log]] §C/§F/Session 2; this section holds only what's load-bearing here.

**(b) sources verified 2026-08-29**, all independently converging on §3's 250–350 word default and one-page limit: University of Michigan Career Center's [Cover Letter Resources](https://careercenter.umich.edu/content/cover-letter-resources) (3–4 paragraphs, font matches the resume, margins 0.5–1in), UT Dallas Career Center's [Creating a Cover Letter](https://career.utdallas.edu/career-resource-library/resume-and-cover-letter/creating-a-cover-letter/) (explicit ATS framing — no templates, text boxes, images, QR codes, color, or shading; a true text-only version, not a designed document), Penn State Engineering Career Services' [Cover Letters](https://career.engr.psu.edu/students/basics/cover-letter.aspx) (block business-letter format, same typeface as the resume).

**(a) sources verified 2026-08-29:**
- Google Careers' [Human Resources Apprenticeship, September 2025 Start](https://www.google.com/about/careers/applications/jobs/results/77547348728652486-human-resources-apprenticeship-september-2025-start) requires one PDF containing an English CV and an English cover letter explaining the applicant's interest, intended degree/curriculum, and apprenticeship rhythm. This is a posting- and jurisdiction-specific instruction, **not** a universal Google or Google-internship requirement.
- Capital One's [How to Write a Cover Letter for a Job](https://www.capitalone.com/learn-grow/life-events/how-to-write-a-cover-letter/) recommends a tailored letter that introduces role/strengths, connects qualifications to the organization, and adds depth rather than repeating the resume. It is company-published general career advice, **not** Capital One recruiting policy or proof that Capital One roles require a cover letter.

**Format rule this adds to §3/§4**: no text boxes, images, QR codes, color, or shading — a cover letter is read as plain text by the same ATS pipeline as the resume (see [[Resume Alteration Standard#8. ATS Format & Keyword Baseline (Sourced)]]), and a designed letter risks the identical parse failures.

**Limit:** no target-company cover-letter-specific guidance was found for Lever, Workday, Jane Street, Citadel, HRT, Two Sigma, Microsoft Explore, Google ASDI, LinkedIn First Play, Bloomberg, MLH Fellowship, or NASA OSTEM. Never presume a cover letter is required; follow the live posting/application.
## Done When
- `Main Cover Letter.md` exists with real, evidence-backed, reusable fragments — not a single fixed letter copy-pasted per application.
- Every per-application letter names 2–3 real experiences, each traceable to §2's sources.
- No letter exceeds the 250–350 word default without a stated reason on the content plan.
