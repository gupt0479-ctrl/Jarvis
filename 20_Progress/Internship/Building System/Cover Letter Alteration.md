---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - cover-letter
  - system
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[30_Order/Workflows/Application Document Preparation]]"
  - "[[30_Order/Standards/Cover Letter Alteration Standard]]"
  - "[[20_Progress/Internship/Building System/Resume Alteration]]"
  - "[[20_Progress/Internship/Building System/Humanizer]]"
next: "Build Cover Letters/Main Cover Letter.md — the paragraph-bank equivalent of Main Resume.md — once the resume rebuild's evidence structure is proven out."
---
# Cover Letter Alteration
==The sibling system to [[20_Progress/Internship/Building System/Resume Alteration]].== A cover letter and a resume get read differently — one gets skimmed and keyword-matched, the other gets read start to finish by an actual human — so they're two systems with the same evidence discipline, not one system with two outputs. Enforceable rules live in [[30_Order/Standards/Cover Letter Alteration Standard]]; this note is the narrative.

## Scope
Governs a new master, `Cover Letters/Main Cover Letter.md`, and every per-application cover letter DOCX in `20_Progress/Internship/Cover Letters/`. That folder doesn't exist yet — nothing has been written to it. Does not govern the resume side (see [[20_Progress/Internship/Building System/Resume Alteration]]) or the style/tone pass itself (see [[20_Progress/Internship/Building System/Humanizer]]).

## The Master Cover Letter (Mirrors The Resume's Three-Artifact Contract)
1. **`Cover Letters/Main Cover Letter.md`** — not yet built. The intended shape is a paragraph/story bank, not a single fixed letter: reusable, evidence-backed narrative fragments (an opening hook per company-type, 2–3 experience paragraphs each tied to a specific real project or role, a closing) that a per-application letter selects from and recombines — the cover-letter equivalent of Main Resume's tagged bullet bank. This is genuinely new content to write, not an extraction from something that already exists in the vault.
2. **`Cover Letters/Main Cover Letter.docx`** — canonical export, regenerated from the Markdown, never edited independently.
3. **`Cover Letters/Main Cover Letter.pdf`** — submission-format export.
`Main Cover Letter.*` are reserved filenames at the root of `Cover Letters/`, same reservation rule as `Main Resume.*`.

## Evidence Rule — Same As The Resume Side
Every paragraph traces to an approved fragment in `Main Cover Letter.md`, a linked Jarvis project note, or an explicit human-supplied fact — identical three-source rule to [[20_Progress/Internship/Building System/Resume Alteration#The Evidence Rule (Load-Bearing)]]. A cover letter is exactly the kind of document where invented enthusiasm ("I've always dreamed of working at X") or an invented specific fact about the company is the most tempting failure mode — the rule exists precisely to block that, not just generic false-metric risk.

## What Tailoring Means Here
Select 2–3 real, evidence-backed experiences that best map to the JD's top requirements — not more; a letter that tries to cover everything reads as generic by trying to be complete. Open with something specific to the company (a real product, a real problem, something from the Program note's Company Information section — never a generic "I am passionate about your mission" line). Default length: 250–350 words, per [[30_Order/Standards/Cover Letter Alteration Standard]] — short enough to read start to finish, long enough to make a real case. Deviating from that range needs a stated reason (a company that explicitly asks for a specific format), not a default drift.

## Per-Application Flow
Runs in the same sitting as the resume side, sharing one Applying note and one approval gate — full sequencing in [[30_Order/Workflows/Application Document Preparation]]:
1. Applying note exists (`status: Preparing`), created at the start of preparation, same as the resume flow.
2. Drafting step (once built) reads `Main Cover Letter.md`, the Applying note's JD/fit/networking fields, and linked Jarvis project/Program notes; asks the human for anything missing rather than inventing a company-specific detail.
3. Proposes a short content plan — which 2–3 experiences, why they map to this JD, the opening hook, an honest note on anything the JD asks for that isn't covered.
4. On approval, and only after the draft passes the Humanizer gate, write or overwrite exactly one file: `Cover Letters/<Role> - <Company>.docx` — same naming convention as the resume file and the Program/Contact/Tracker notes.
5. Overwrite in place until `date_applied` is set on the Applying note; frozen as historical after that, same rule as the resume side.
6. The Applying note's `cover_letter` field links to the file; its Documents section carries a one-line summary of what the letter opens with.

## Not Yet Built
- `Main Cover Letter.md` itself — has to be written from scratch, not extracted.
- The DOCX-generation mechanism (shared tooling with the resume side, most likely).
- The cover-letter-alteration drafting skill/agent — scaffolded at `.cursor/skills/cover-letter-alteration/SKILL.md`, blocked on `Main Cover Letter.md` existing.

## Interfaces
- [[30_Order/Standards/Cover Letter Alteration Standard]] — enforceable length/evidence/naming/overwrite rules.
- [[30_Order/Workflows/Application Document Preparation]] — shared sequencing with the resume side.
- [[20_Progress/Internship/Building System/Humanizer]] — shared pre-write style gate.
- [[20_Progress/Internship/Building System/Resume Alteration]] — the sibling system this mirrors.
