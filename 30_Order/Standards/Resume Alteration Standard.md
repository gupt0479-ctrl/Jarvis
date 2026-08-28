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
  - "[[20_Progress/Internship/Building System/Resume Alteration]]"
  - "[[30_Order/Workflows/Application Document Preparation]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
next: null
---
# Resume Alteration Standard
==The enforceable rules behind [[20_Progress/Internship/Building System/Resume Alteration]].== That note is the narrative — why the system looks this way. This is the contract: what a future resume-alteration skill/agent, or a human doing the same work by hand, must actually do.

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
**As of 2026-08-28**, this vault holds only category (c) material for anything resembling "Google's XYZ method," and holds no source at all for an "Amazon resume template." Both stay advisory — usable as guidance, not citable as an official standard — until a real (a) or (b) source is captured and logged in this section with its actual citation. Don't upgrade a (c) source to (a)/(b) by repetition; upgrade it only when a real primary source is found and recorded here.

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

## Done When
- `Main Resume.md` carries evidence-tagged bullets a human actually approved, not generic filler.
- A spot-check of any per-application resume can trace every line back to §2's three sources or an explicitly logged gap.
- No per-application resume file exists outside `Resumes/`, and none collides with the `Main Resume.*` reserved names.
- No resume in this system cites "Google's XYZ method" or an "Amazon template" as official without a real (a)/(b) source logged in §4.
