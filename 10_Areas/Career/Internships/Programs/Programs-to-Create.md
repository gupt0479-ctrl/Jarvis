---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-09-04
tags:
  - internship
  - process
notes:
  - "[[Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Programs/Programs MOC]]"
  - "[[Claude Code Prompts]]"
  - "[[Internship Notes Standard]]"
next: Build the promote-dossier skill per [[20_Progress/Internship/Building System/Claude Code Prompts]] — nothing in this folder is hand-created until that exists.
---
# Programs — How Notes Get Created Here
==Nothing in `Programs/` gets typed from a hardcoded target list anymore.== This note replaces the old plan of that shape (13 hand-picked companies, written once at the start of a cycle) — that approach is retired, not archived under a different name; git history holds it if it's ever needed again. What replaced it: every Program note here is created the same way a dossier is — driven by code, from `gupta-builds/internship-research-loop` — except gated by explicit manual consent at every step. Nothing writes into this folder silently.
## The Actual Process
1. A dossier (or a hand-found lead that never went through the automated pipeline) passes the fit test — see [[Internship Pipeline]] Step 2. Goal-push, personal fit, contact-reachability noted-not-gated, pay never a factor. **The call itself gets recorded on the dossier**, not just made mentally — `screened_date`/`screened_decision`/`screened_reason` fields, per [[Internship Notes Standard]] §7. A dossier promoted into a Program note without those fields set is a real, checkable gap (the fields aren't retroactive, so a dossier that predates §7 won't have them — that's expected, not a violation).
2. You invoke the promotion skill (`gupta-builds/internship-research-loop`'s `.claude/skills/promote-dossier` once built — see [[Claude Code Prompts]] for the build spec). It asks two small things: which folder (`Serious/` or `Considering/`) and whether the dossier's auto-assigned priority/category still holds or needs a human override.
3. The skill runs contact research (`enrich.py`, promotion-triggered, same as always) and shows you what it found before writing anything.
4. On your explicit go-ahead, three notes get created together, cross-linked: the Program note (here), a Contacts/Each One note, and a Tracker/Each One note.
## What Belongs In The Note — Section By Section
- **Program Overview** — what the role actually is, who runs it, what makes it worth the hours to prepare for. Tie it explicitly to your resume and profile — how would this specific role actually help you, concretely, not "it's a good opportunity."
- **Eligibility** — who can apply, year/major requirements, anything that disqualifies you before you even start.
- **Company Information + Contact** — the key research points about the company: latest and most relatable real projects, what the company actually does, why it's related to you specifically. Write it so a conversation with this company would sound informed, not generic. The Contact sub-section is just interlinks to the real Contacts note — don't duplicate facts that already live there.
- **Traps & Gotchas** — the thing most applicants get wrong about this specific program, stated plainly.
- **Prep Checklist** — real, specific items drawn from what the actual posting asks for — never a bare empty checkbox left for later.
- **Related Resources** — links to the dossier origin, the Contacts note, and (once it exists) the Job & Company note.
## Serious vs. Considering
Identical template, identical research depth, in both folders. The only variable is preference/timing — pursuing this one now (`Serious/`) versus interested but not yet, or needs more thought first (`Considering/`). A thinner Considering note is a mistake, not a shortcut — fix it if you see one.
## Manual Finds
A lead you found yourself (career fair, a referral, LinkedIn) that never became a dossier enters at the same step 1 above — it just arrives without an originating dossier link. Everything downstream is identical.
## Ended — Applied, Awaiting The Next Step
Both `Serious/` and `Considering/` carry an `Ended/` subfolder. A Program note moves there once you've actually submitted an application for it — not when you've merely decided to, and not when it's still under consideration. `Ended` means the research-and-decide phase is over for this program; whatever happens next (screen, interview, offer, rejection) is tracked on the paired Applying note, not here.
> [!IMPORTANT]
> A note in `Ended/` with no matching note in `20_Progress/Internship/Applying/` gets discarded, not kept as a record. If there's no Applying note, no application was ever actually submitted — the program never left the research phase, and `Ended` would be a false claim otherwise.
## Job & Company — The Interview-Prep-Grade Deep Dive
`Programs/Job & Company/` is a separate, later step from the Program note — it exists for once you're actually ready to apply, not at commit time. Where a Program note is comp/eligibility/traps/prep-checklist scoped, a Job & Company note goes deeper: relevant company projects, the company's stated mission and how it actually maps to your own direction, research specific to the role (not generic company background), and what the verified contact has personally contributed to the company — everything that would make you sound genuinely informed in an interview, not just prepared.
- **Filename:** `[Company] - [Position].md`.
- **Trigger:** created when you're ready to move a program toward actually applying — not automatically at commit time, and not for every program in `Considering/`.
- **More than one real position at the same company (past 2):** stop using flat files — create a `[Company]/` subfolder and give each position its own note inside it. Do the same depth of research for each; a second posting at a company you've already researched still gets its own real pass, not a copy-paste.
- **The payoff question to answer in every one of these notes:** how exactly would this specific company move you toward the goal in [[Engineer Edge Roadmap]] — not "is this a good company" in the abstract, but "why this one, for me."
