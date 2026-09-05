---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - resume
  - standard
notes:
  - "[[Resume Alteration]]"
  - "[[30_Order/Workflows/Application Document Preparation]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
next:
---
# Resume Alteration Standard
==The enforceable rules behind [[Resume Alteration]].== That note is the narrative — why the system looks this way. This is the contract: what a future resume-alteration skill/agent, or a human doing the same work by hand, must actually do.

## Scope
Governs `20_Progress/Internship/Resumes/Main Resume.md` / `.docx` / `.pdf` and every per-application tailored resume DOCX in that same folder. Does not govern cover letters (see [[30_Order/Standards/Cover Letter Alteration Standard]]) or the tone/style checklist itself (see [[30_Order/Standards/Humanized Writing Standard]]) — a resume can pass every rule below and still fail the Humanizer gate for how it reads.

## 1. Source-of-Truth Hierarchy
`Main Resume.md` is authoritative. `Main Resume.docx` and `Main Resume.pdf` are generated exports — never hand-edited independently of the Markdown. If the exports and the Markdown ever disagree, the Markdown wins and the exports get regenerated, not patched individually. A per-application resume derives its content only from `Main Resume.md`'s approved bullets plus anything explicitly approved as a one-off addition during that application's content-plan review (see §2) — it never introduces a claim that doesn't also belong, in principle, on the master.

## 2. Evidence-Only Claims (Fail-Closed)
Every bullet, skill, and metric on any resume this standard governs must trace to exactly one of:
- An already-approved bullet in `Main Resume.md`.
- A fact drawn from a linked Jarvis project note, cited by note path.
- Content the human explicitly supplied when asked during that application's drafting pass.
A JD requirement with no matching evidence in any of those three is recorded as a **gap** in the content plan — never guessed, never filled with a plausible-sounding invention, no matter how minor. This is fail-closed the same direction `vault_writer/validate.py`'s required-fields check is in the internship-research-loop repo: a missing field is a bug to surface, not something to default past silently. Applied to resume content, an unsupported claim is a bug to surface, not something to write past silently.
- Flag: any bullet, number, tool name, or outcome that doesn't trace to one of the three sources above.
- Pass: a bullet whose wording changed but whose underlying fact is identical to an approved source.

## 3. The Tailoring Boundary
**Allowed:**
- Selecting which existing bullets appear on a given application's resume.
- Reordering bullets and the Skills list to lead with what the JD emphasizes.
- Accurately rephrasing wording to mirror the JD's own terminology, as long as the underlying fact is unchanged ("built REST APIs" → "designed RESTful services" is fine if that's genuinely what happened; → "led API architecture" is not, if "led" wasn't true).
**Not allowed:**
- Inventing a bullet, metric, tool, employer, or outcome.
- Changing a real number.
- Claiming a skill/tool that wasn't actually used, even if the JD asks for it.
- Inflating scope or seniority beyond what actually happened.

## 4. Source Register — External Resume-Writing Guidance
Every piece of external resume-writing guidance this system relies on (a named methodology, a company-specific format claim, a "best practice") must be classified as one of:
- **(a) Primary/official** — a direct citation to the company's or organization's own published source.
- **(b) University career-service guidance** — cited to the specific office/publication.
- **(c) Third-party advisory** — a guide, course, or clipped resource (e.g. this vault's [[60_Claude/10_Source_Summaries/PDF Ingestion/MavGPT AI Resume & Job Search Guide (PDF)]]) — useful, but never presented as an official employer standard.
Full findings, dates, and every source not listed here live in [[Resume & Cover Letter - ATS Research Log]] (Session 1 2026-08-29, Session 2 2026-08-29) — this section holds only the citations actually load-bearing for §8 below.

### ATS Vendor Documentation (a) — the four platforms named-program dossiers pass through
- **Greenhouse Support** — [Supported formats for resumes, cover letters and other candidate uploads](https://support.greenhouse.io/hc/en-us/articles/360052218132), [Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175).
- **Ashby** — [Bulk Import: Email Import — file requirements](https://docs.ashbyhq.com/bulk-import-email-import), [Reviewing 1500 resumes with AI-Assisted Application Review](https://www.ashbyhq.com/blog/recruiting/ai-assisted-application-review-in-practice).
- **Lever Help Center** — [Understanding resume parsing](https://help.lever.co/hc/en-us/articles/20087345054749-Understanding-resume-parsing), [Adding and deleting resumes](https://help.lever.co/hc/en-us/articles/20087357076253): parses readable text from common file types; cannot parse image files (JPG/PNG); uploads accepted up to 10MB.
- **Workday** — [HiredScore Grades](https://doc.workday.com/hiredscore/en-us/workday-hiredscore/recruiter-productivity-/concept--hiredscore-grades.html), [Candidate Profiles](https://doc.workday.com/hiredscore/en-us/workday-hiredscore/recruiter-productivity-/concept--candidate-profiles.html): public product/recruiter documentation confirms JD skills-and-qualifications matching and DOC/DOCX/PDF/RTF/TXT support. It is **not candidate-facing**, and HiredScore grades expressly exclude campus/graduate requisitions — don't infer that a Workday-hosted internship is automatically ranked.

### Company & Named-Program Guidance (a)
- **Google** — [Create Your Resume for Google: Tips and Advice](https://www.google.com/about/careers/applications/videos/google-resume-tips-and-advice/), hosted on `google.com/about/careers` — the real citation for "Google's XYZ method" ("Accomplished [X] as measured by [Y] by doing [Z]"), genuinely Google's own stated framework, not a third-party myth.
- **Amazon** — [Amazon job application: Resume writing tips](https://www.aboutamazon.com/news/workplace/amazon-job-application-resume-writing-tips), on `aboutamazon.com`, quoting named Amazon recruiting staff. This is official *guidance*, not a downloadable "Amazon resume template" — no such template exists at (a) tier; don't describe it as one.
- **NASA OSTEM** — [Intern FAQ](https://www.nasa.gov/learning-resources/internship-programs/intern-frequently-asked-questions/), [5 Tips to Craft a Standout NASA Internship Application](https://www.nasa.gov/learning-resources/tips-to-craft-standout-internship-application/): OSTEM uses application fields rather than a resume upload; the project-aligned personal statement, academics, extracurriculars, and skills are the relevant application evidence.
- **MLH Fellowship** — [official application](https://fellowship.mlh.io/apply): at least one of resume/GitHub/LinkedIn/portfolio is required; DOC/DOCX/PDF resume uploads are accepted; the named program evaluates original essay responses.
- **Bloomberg** — [Engineering: Student Application Process](https://www.bloomberg.com/company/careers/application-process/engineering-student/): Bloomberg reviews students' resumes and discusses technical-project contributions and impact.

### University & Association Guidance (b / a-assoc)
University of Florida Career Connections Center, University of Michigan Career Center, UT Dallas Career Center, Penn State Engineering Career Services — see the research log for what each says. NACE (National Association of Colleges and Employers) is the professional association several of these build on; treat it as authoritative but one tier below a named employer's own statement.

**Limit:** no (a)/(b) resume-format, LaTeX, one-page, or GPA-threshold rule was found for Jane Street, Citadel, HRT, or Two Sigma. No official source validates a keyword-mention-count heuristic; see §8. The uConnect-hosted "CARS-669" handout (research log §C) could not be attributed to a specific university and is **not** registered here as (b) — don't cite it by name until its origin is confirmed.

## 5. File and Naming Convention
- `Main Resume.md`, `Main Resume.docx`, `Main Resume.pdf` are reserved names at the root of `20_Progress/Internship/Resumes/`.
- Every per-application resume is `<Role> - <Company>.docx` in that same folder — same sanitization rule as Program/Contact/Tracker notes (strip `\/:*?"<>|`, since the vault lives on a Windows-mounted drive).
- No subfolder (no `Altered/`, no `Tailored/`) — both names appear elsewhere in the vault from before this standard existed and are superseded by the flat convention above.

## 6. Overwrite Policy
One resume file per application. Any revision made **before** `date_applied` is set on the paired Applying note overwrites that file in place — no `v1`/`v2` files; applying should stay a quick step, and multiple live versions would slow it down for no real benefit. Once `date_applied` is set, the file is historical — a genuine need to change a submitted application's resume (e.g. an actual resubmission request) is a new, explicit human decision, never a background rewrite of a file that's already out the door.

## 7. Approval Gate
No per-application DOCX is written or overwritten until:
1. A human has explicitly approved the traceable content plan (which bullets, why, what's rephrased, what's an honest gap), and
2. The draft has passed the Humanizer gate (see [[30_Order/Standards/Humanized Writing Standard]]).
Both gates are required, in that order — evidence/selection correctness first, tone correctness second. Neither substitutes for the other.

## 8. ATS Format & Keyword Baseline (Sourced)
Distilled from the §4 (a) sources plus the convergent (c) findings logged in [[Resume & Cover Letter - ATS Research Log]] — applies to every resume this Standard governs, on top of §2's evidence rule and §3's tailoring boundary:
- **Layout**: single-column, top to bottom — no tables, text boxes, columns, sidebars, or graphics/icons/skill-bar images. This is Greenhouse's own documented parse-failure list, not a style preference.
- **Section headings**: familiar labels only — Experience, Education, Skills (Summary optional). Greenhouse names unclear/inconsistent sections as a parse risk; no vendor source in §4 requires an exact heading beyond that.
- **Contact info**: in the document body, first page, never in a header/footer.
- **Dates**: one consistent, readable format throughout the document. No vendor source in §4 requires a specific date syntax (e.g. "MM/YYYY" is not a documented Workday/Greenhouse/Lever/Ashby requirement) — consistency is the actual rule, not a particular format.
- **Fonts**: standard system fonts (Arial, Calibri, Times New Roman, Garamond, Helvetica) at 10–12pt.
- **File**: PDF preferred, text-based/selectable (never a scanned image); DOCX acceptable. Keep under 2.5MB for Greenhouse; Lever accepts common resume types up to 10MB. Default to the stricter 2.5MB ceiling whenever the target ATS is unknown.
- **Length**: one page by default for an internship/entry-level resume; two pages only where the target company's own guidance explicitly allows it for technical/engineering roles (Google's own video does — see §4).
- **Keywords**: use the JD's exact terminology where it truthfully describes demonstrated work, each mention paired with real context and a result. No (a) source in §4 gives a repetition count or density threshold — Workday HiredScore documents JD-to-resume matching but not a frequency rule, and Lever's parsing docs don't address keyword matching at all. There is **no verified universal percentage or mention-count rule**; treat any specific count as (c)-tier advisory only, never a requirement. The one thing every source agrees on: never duplicate the identical phrase back-to-back with no new information attached — that pattern, not a raw count, is what reads as stuffing.
- **GPA**: include only where the application form or JD explicitly asks for it, or where the target program conventionally expects one (quant/finance roles, per research log §G). The ~3.5 general / ~3.7 quant thresholds circulating in third-party guidance are unverified convention — usable as a rule of thumb, never stated as a named company's actual policy.
## Done When
- `Main Resume.md` carries evidence-tagged bullets a human actually approved, not generic filler.
- A spot-check of any per-application resume can trace every line back to §2's three sources or an explicitly logged gap.
- No per-application resume file exists outside `Resumes/`, and none collides with the `Main Resume.*` reserved names.
- §4 and §8 cite a real (a)/(b) source for every format/keyword rule this system enforces — "Google's XYZ method" and Amazon's guidance are now sourced (2026-08-29); don't let a new claim about a company or ATS platform enter this Standard without the same treatment.
