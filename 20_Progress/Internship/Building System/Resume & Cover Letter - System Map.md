---
type: evergreen
status: sprout
created: 2026-08-29
updated: 2026-08-29
tags:
  - internship
  - resume
  - cover-letter
  - map
notes:
  - "[[Resume Alteration]]"
  - "[[Cover Letter Alteration]]"
  - "[[Humanizer]]"
  - "[[Resume Alteration Standard]]"
  - "[[Cover Letter Alteration Standard]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
  - "[[Resume & Cover Letter - ATS Research Log]]"
next: "Rebuild Resumes/Main Resume.md into evidence-tagged bullets — the one blocker every downstream note (Standards §2, both Cursor skills' Prerequisite section) is waiting on. See #Status below."
---
# Resume & Cover Letter — System Map
==One entry point for every note that governs how this loop writes, tailors, and validates a resume or cover letter — narrative design, enforceable rules, workflow sequencing, external research, and the human role that makes the whole evidence chain real.== Start here before touching any piece of this system; each linked note below states its own scope precisely so this map stays a pointer, not a duplicate.

## Why This Exists
The resume/cover-letter system now spans nine vault notes plus two repo-side Cursor skills, written across three sessions. No single note lists all of them together, and the evidence chain that makes every Standard's "fail-closed" rule actually enforceable — a real human fact source — was never written down anywhere. This note is both: a map, and the place that states the fact-source rule explicitly (see [[#Where The Facts Actually Come From]]).

## The Design Layer — why the system looks this way
- [[Resume Alteration]] — the master-resume contract, the evidence rule, the tailoring boundary, and the per-application flow, narrated.
- [[Cover Letter Alteration]] — the parallel contract for cover letters; describes the not-yet-built `Main Cover Letter.md` as a paragraph/story bank.
- [[Humanizer]] — the pre-write style gate both documents pass through before a file is ever written; defines the minimal input/output interface, not the full checklist (that's the Standard below).

## The Enforceable Layer — what a skill/agent/human must actually do
- [[Resume Alteration Standard]] — the resume contract: source-of-truth hierarchy, evidence-only claims (fail-closed), the tailoring boundary, the external-source register (§4, reorganized 2026-08-29 into ATS-vendor / company-and-program / university-and-association groups), file/naming/overwrite rules, the approval gate, and the sourced ATS format & keyword baseline (§8).
- [[Cover Letter Alteration Standard]] — the mirrored cover-letter contract: same evidence rule, narrative selection and length instead of bullet ordering, its own §7 source register.
- [[30_Order/Standards/Humanized Writing Standard]] — the tone/style checklist both Standards defer to; a document can pass every rule above and still fail this gate for how it reads.

## The Workflow Layer — when each of the above actually runs
- [[30_Order/Workflows/Internship/Application Document Preparation]] — the `prepare → draft → plan → approve → humanize → write → link → apply` sequence that ties the Design and Enforceable layers to a real Applying note.
- [[Internship Pipeline]] — Step 5 (Tailor) triggers this whole system; Step 7 (Apply) is where it hands back off to a human submitting the application. Read those two steps specifically, not the whole pipeline, if you're only touching this system.
- [[Applying Template]] — the note this system reads from and writes back to (`job_url`, `resume_version`, `cover_letter` fields, Documents section).

## The Research Layer — what's actually sourced, and what still isn't
- [[Resume & Cover Letter - ATS Research Log]] — the running, cross-session log of every external resume/cover-letter/ATS resource found (Session 1 + Session 2, both 2026-08-29), classified (a)/(a-assoc)/(b)/(c-1)/(c-2). This is where a *new* claim about a company or ATS platform gets checked and logged before it's allowed into either Standard — see the Standards' own §4/§7/§8 for what's already been promoted from this log into an enforceable rule.
- [[10_Areas/Career/Internships/Cheats/Resume Tailoring, LinkedIn Search & Outreach Discovery]] — the pre-existing (c)-tier cheat sheet (MavGPT's five-prompt tailoring sequence, LinkedIn search operators, the Outreach-tool verdict). Still valid as advisory content; superseded as an *authority* by the (a)/(b) sources the research log now carries for anything it overlaps with.
- [[60_Claude/10_Source_Summaries/PDF Ingestion/MavGPT AI Resume & Job Search Guide (PDF)]] — the original (c)-tier PDF ingestion behind that cheat sheet.

## The Repo Layer — where this becomes an invokable skill
Lives in `internship-research-loop`, not the vault — linked here by path since it's outside Jarvis:
- `.cursor/skills/resume-alteration/SKILL.md` — drafts and writes the tailored resume for one application, gated on Main Resume being evidence-tagged (it isn't yet — see [[#Status]]).
- `.cursor/skills/cover-letter-alteration/SKILL.md` — the cover-letter half; gated on `Main Cover Letter.md` existing (it doesn't yet).
Both skills read the same Standards linked above at the start of every run — they don't duplicate the rules, they enforce them.

## Where The Facts Actually Come From
Every Standard above enforces the same three-source evidence rule (Resume Standard §2, Cover Letter Standard §2): a claim traces to an approved `Main Resume.md`/`Main Cover Letter.md` fragment, a linked Jarvis project note, **or a fact the human explicitly supplies when asked**. That third source isn't a fallback — for anything not already written up as a project note, it's the primary source, and it depends on a real person being reachable and willing to do it.

**Anant is that source.** Confirmed directly (2026-08-29): available to supply and confirm the real fact inventory behind every resume bullet and cover-letter claim — specific projects, roles, metrics, and tools — whenever a content-plan draft (§3 of either Standard) surfaces a gap or needs a number/detail no existing note captures. This means:
- A drafting pass should **ask**, not guess, the moment a JD requirement has no matching bullet or fragment — per both Standards' "never guessed, never filled with a plausible-sounding invention" rule, an unasked question is the same failure as an invented fact.
- The three-source rule works because this fourth path is real, not theoretical — don't treat "the human wasn't available" as a reason to invent something plausible instead of logging an honest gap and moving on.
- This is distinct from the Program note's Company Information section or contact-research findings (which supply *company*-side facts for cover letters) — this is specifically the *candidate*-side fact inventory: what Anant actually built, did, measured, and used.

## Status — what's real, what's still a gap
- **Blocking everything downstream**: `20_Progress/Internship/Resumes/Main Resume.md` is still generic filler, not the evidence-tagged bullet bank the Resume Standard's §1/§2 assume. Per [[Resume Alteration]]'s own "Not Yet Built" section, this rebuild is separate, gated work — it hasn't started.
- **Not yet built at all**: `20_Progress/Internship/Cover Letters/Main Cover Letter.md` — no paragraph/story bank exists yet.
- **No DOCX-generation mechanism confirmed** in this environment — both Cursor skills' §5 ("Write the file") stop short and fall back to a Markdown content-plan file rather than fabricating a tool call that doesn't exist, until this is set up.
- **Sourced and current** as of 2026-08-29: both Standards' external-guidance registers (§4/§7) and the ATS format baseline (§8) — see the research log for exactly what's (a)/(b) vs. still (c)-tier advisory.
