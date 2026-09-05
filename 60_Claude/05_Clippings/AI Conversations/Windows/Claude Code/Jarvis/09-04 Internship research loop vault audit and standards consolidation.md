---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Internship research loop vault audit and standards consolidation"
started_at: 2026-09-04T18:01:31
ended_at: 2026-09-04T20:40:13
exported_at: 2026-09-04T23:00:03
duration_minutes: 158.7
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: d924b0b1-5105-4f87-b8f4-6050f926a208
status: raw
turn_count: 2
tools_used:
  AskUserQuestion: 1
  Bash: 2
  Edit: 25
  Glob: 14
  Grep: 21
  Read: 28
  Write: 4
tokens:
  input: 268
  output: 199798
  cache_creation: 1044106
  cache_read: 23640873
  total: 24885045
cost_usd: 10.903115
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Contacts\\Each One\\Contacts-to-Create.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Contacts\\Each One\\Ongoing\\Software Engineering Intern - Appian.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\_Today\\New Internships Listings.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\_Today\\No Deadline.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Dossiers-to-Create.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\What was Viewed.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Programs\\Considering\\Software Engineering Intern - Appian.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Programs\\Programs-to-Create.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Tracker\\Deadline Tracker.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Tracker\\Each One\\Trackings-to-Create.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Applying\\Applications-to-Create.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\Resume & Cover Letter - System Map.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\System - Build Log.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\V0\\Cover Letter Alteration.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\V0\\Dossier Corrections.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\V0\\Humanizer.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\V0\\Resume Alteration.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Humanized Writing Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Cover Letter Alteration Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Deadline and Intake Triage Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Internship Loop Review Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Internship Notes Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Internship Tracker Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship\\Resume Alteration Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Tracking Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Career\\Internship\\Applying Template.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Application Document Preparation.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Internship\\Application Document Preparation.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Internship\\Internship Pipeline.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\05_Clippings\\AI Conversations\\Windows\\Claude Code\\Jarvis\\09-04 Internship research loop vault audit and standards consolidation.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\07_AI_Information\\Session Logs\\log.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Internship research loop vault audit and standards consolidation

## You

You're working inside the Jarvis vault directly (Windows, Claude Code, Sonnet 5, high/xhigh effort). This continues internship-research-loop — a zero-LLM internship-discovery pipeline paired with this vault's internship system — but you have no memory of any prior session. Everything you need is below or discoverable in the vault; where something is uncertain, investigate it yourself rather than guess, and where a real decision needs the human's input, stop and ask — this prompt has one mandatory pause built into it (Task 3), not a suggestion to skip if it feels slow.

This prompt covers three tasks only. Tasks that sound like natural next steps — building hooks, creating an agent, auditing the logging system, populating a master log — are explicitly out of scope here. A follow-up prompt covers those later, after the human reviews what this one produces. Do not start them even if Task 2's investigation makes them look like the obvious next move.

Context you need, pre-verified this session — re-check anything you're about to build on

A parallel codebase-side session just completed a "v0" audit of internship-research-loop (plan only, nothing shipped yet, pending human confirmation). Its real findings, which Task 1 needs to record accurately:

- The hourly discovery workflow (run.yml) has been in GitHub's disabled_manually state since 2026-08-29 — 6 days at zero new discovery when this was found. This was almost certainly an emergency stopgap during the write-starvation incident (see Discovery Step Postmortem — Write-Starvation Incident (2026-08-26), already in this vault). The actual fix (write_gate_failures.json, commit e856e05, 2026-08-30) shipped the next day and has real test coverage (18/18 passing) — but nobody re-enabled the workflow afterward. It's still off as of this writing.
- Week-over-week data from logs/runs.jsonl (real, not the vault's own Run Log.md rollup, which stops earlier): matched candidates grew ~30x (689/week → 34,499/week) as sources went from 2 to 11, while the write budget stayed fixed at ~10/run (~1,680/week ceiling) — meaning the 5-dossiers/hour target discussed is already below the existing design ceiling; the real blocker was the write-starvation bug (now fixed but unproven in production), not capacity.
- Test suite: 444 tests. Real redundancy found in exactly one place — tests/test_schema_drift.py (46 tests, a near-mechanical 4-5-tests-per-source pattern repeated across 11 sources) is a genuine parametrization candidate. test_filter.py/test_relevance.py are dense but NOT redundant — nearly every test guards one specific real-world incident (Mosaic, Databricks, AbbVie, Prophet Security, the NL/HK/PL/IL location gaps) per this repo's own "cite the real data" convention; consolidating those would delete real regression coverage.
- Vault housekeeping, counted fresh: 287 dossiers (134 AI/ML, 42 Fullstack, 50 CyS&Finance, 61 Other), 10 Programs/Serious + 4 Considering, 10 Contacts, 10 Tracker notes. A separate note, Dossier Corrections.md (2026-08-28 audit), already found real, cited defects in this exact set: ~10 duplicate pairs, systemic quant-firm bucket misclassification (Optiver/IMC/Chicago Trading Co. split inconsistently between AI/ML and CyS&Finance), a confirmed company-name typo (Montenson→Mortenson, 5 dossiers), and 6 Zipline dossiers still carrying the old broken content even after the extraction bug was fixed elsewhere — because nothing retroactively re-evaluates dossiers written before a fix lands.
- Proposed v0 README direction: generic (not personal-profile-hardcoded) eligibility config, setup instructions, and a verify.py concept letting a stranger check capture completeness against a live source feed. Not built — a proposal pending confirmation.

Also pre-verified this session, about the vault itself — this is new since whatever you might assume from an older mental model of this vault's structure:
- 30_Order/Standards/Internship/, 30_Order/Workflows/Internship/, and 30_Order/Templates/Career/Internship/ now exist as real subfolders. A reorganization has happened — but it looks partial, not complete:
  - 30_Order/Standards/Internship/ holds: Cover Letter Alteration Standard.md, Internship Loop Review Standard.md, Internship Notes Standard.md, Internship Tracker Standard.md, Resume Alteration Standard.md.
  - But Tracking Standard.md still sits at the top level of 30_Order/Standards/, separate from the new Internship Tracker Standard.md inside the subfolder. Are these the same content duplicated, two genuinely different scopes, or one stale leftover from before the move? Not known — investigate directly (read both, diff their actual content) before assuming either answer.
  - 30_Order/Workflows/Internship/ holds: Internship - Design Rationale.md, Internship Pipeline.md, Promotion.md. But Application Document Preparation.md (the resume/cover-letter workflow, per Resume & Cover Letter — System Map.md) is still at the top level of Workflows/, not moved in. Same question: intentional, or an incomplete migration?
  - 30_Order/Templates/Career/Internship/ holds 9 templates including two new ones — Internship Loop Weekly Review Template.md and Internship Loop Monthly Review Template.md. List Monthly Log Template.md and Plan Template.md stayed at the top level of Templates/Career/.
  - 10_Areas/Career/Internships/Tracker/Main Log.md already exists, but is a completely empty (0-byte) stub. Don't populate it — that's explicitly a later task (see below) — but don't assume it needs creating from scratch either.
  - 10_Areas/Career/Internships/List/Dossiers/_Today/ is a new folder (New Internships Listings.md, No Deadline.md) — appears connected to Tracker/Deadline Tracker.md and the 2026-08-28 "deadline sweep" mentioned in Dossier Corrections.md. Whether this triage view has any Standard/Workflow describing what it's for and how it's maintained is unknown — check.

Task 1 — Record this session's findings in the right place, not a guessed one

Before writing anything, determine where the last comparable session summary actually landed: check System - Build Log.md's most recent dated entry (the established pattern used by every prior prompt in this project's history) and 60_Claude/07_AI_Information/AI Conversation - Summaries/ (including its Claude Code/ subfolder, which you haven't been told the contents of — list it) for a more specific internship-loop summary pattern. Pick whichever is the real, current convention — don't split the write across both on a guess, and say which one you chose and why. Write a dated entry covering everything in the "Context" section above: the disabled-workflow finding, the root-cause numbers, the test-redundancy finding, the vault-housekeeping numbers and Dossier Corrections.md cross-reference, and the README proposal — stated as planned, not yet shipped, since the codebase session made zero code changes pending human confirmation.

Task 2 — Completeness and consistency audit of Standards/Workflows/Templates

For every real process this system actually performs — Find (dossier discovery/writing), Screen (the screened_* fields), Commit (Program+Contact+Tracker promotion), Reach Out (Contact note + Mimic.md), Tailor (the resume/cover-letter system), Deep Dive (Job & Company), Apply, Prep (interview), Close, plus the newer Internship Loop Review process and the _Today//Deadline Tracker triage view — confirm a Standard and/or Workflow and/or Template exists, is current, and doesn't conflict with a same-purpose note elsewhere. Concretely:

1. Resolve the Tracking Standard.md vs. Internship Tracker Standard.md question directly — read both in full, determine whether one is stale/superseded or whether they cover genuinely different scopes (e.g., general vault tracking-note convention vs. internship-specific), and consolidate or clearly cross-reference accordingly. Same treatment for Application Document Preparation.md's location relative to the new Workflows/Internship/ subfolder — move it in if it belongs there, leave it and note why if it doesn't, don't leave the question unresolved.
2. Confirm the _Today/ triage folder and Deadline Tracker.md have a real Standard or Workflow describing them — if not, write one, matching the citation/depth discipline Internship Notes Standard.md already established (real examples, real dates, not restated field lists).
3. Re-check whether Program/Contact/Applying still don't need their own dedicated Standards — two prior sessions (this project's history, both in Claude Code Prompts — Archive.md) checked this and said no, based on low volume and no observed defects. That was before the resume/cover-letter system and the Internship Loop Review process existed. Re-evaluate with that new context in mind rather than carrying the old answer forward unchanged — it may still hold, but say so because you checked, not because it's what the last note said.
4. Where a genuine gap exists (a real, recurring process with no note governing it), write the Standard/Workflow/Template. Where nothing is actually missing, say so plainly rather than inventing content to fill the task.

Task 3 — Update the five *-to-Create notes, with a mandatory pause for human input

The five notes: Contacts/Each One/Contacts-to-Create.md, List/Dossiers/Dossiers-to-Create.md, Programs/Programs-to-Create.md, Tracker/Each One/Trackings-to-Create.md, 20_Progress/Internship/Applying/Applications-to-Create.md.

Read each fully, and read the real history behind them — the actual Appian promotion (the one real end-to-end run of Commit/Reach Out that's ever happened), and the resume/cover-letter system's real state (per Resume & Cover Letter — System Map.md: Main Resume.md is still generic filler, Main Cover Letter.md doesn't exist yet — meaning the Tailor step has never actually run for real either). Then stop and ask the human directly, with specific questions grounded in what you just read — not generic ones. Examples of the right shape of question (don't just copy these verbatim, ground your actual questions in what you find):
- "The Appian Commit step created Program+Contact+Tracker together in one sitting per the Pipeline doc's instruction — did that actually happen in one sitting, or in what order, and does Programs-to-Create.md need to say anything about sequencing it didn't before?"
- "Applications-to-Create.md predates the resume/cover-letter system's prepare → draft → plan → approve → humanize → write → link → apply sequence — should applying now explicitly route through that, and where does a human's approval gate sit in Applications-to-Create.md's own process versus the Standard's own approval gate?"
- "Is there anything from real runs so far that these five notes describe incorrectly, not just incompletely?"

Only after getting real answers, update each note so it fully specifies a repeatable process — every step named, every interlink stated explicitly (Program list_origin → dossier, Program recruiter_contact ↔ Contact related_programs, Tracker → all three, per CLAUDE.md's existing cross-link contract — extend this explicitly to cover the resume/cover-letter and review-loop pieces where they now touch this chain) — such that a future session could execute the whole thing from these five notes alone, without re-deriving anything from memory.

Explicitly out of scope — do not start these

Auditing whether the logging system captures enough about skill invocations, building git/vault hooks, enhancing skills based on those hooks, creating a new agent, and populating Tracker/Main Log.md as a master interlinked log. These are real, already-scoped next steps (the human has described them in detail) — they come in a separate follow-up prompt after this one's output is reviewed. If Task 2's investigation surfaces something that looks like it belongs to this later work, name it in your report rather than building it now.

Report back

Task 1: which location you chose and why, confirmation the entry is written. Task 2: the Tracking Standard/Internship Tracker Standard resolution (with your reasoning), the Application Document Preparation.md placement decision, what you found for _Today/Deadline Tracker, the Program/Contact/Applying Standards re-evaluation outcome, and a list of what you wrote vs. what you found already adequate. Task 3: the human's actual answers to whatever you asked, and confirmation each of the five notes now fully specifies its process. State plainly anything in the "pre-verified" sections above that turned out wrong when you checked it yourself.

## Claude

I'll start by investigating the file locations and content needed for all three tasks. Let me gather the key files in parallel.

Now let me read the key files needed for Task 1 and Task 2 decisions.

I need to strip the duplicated body content, leaving only the redirect pointer.

Now replace it with a redirect stub and fix the path-qualified backlinks.

Now let me fix each of these with replace_all since the path string is consistent in each file.

Now let me add a second entry recording this session's Task 2 vault-side Standards work.

Right, em dashes not hyphens. Let me redo the edit with the correct characters.

This is coherent and consistent throughout. All three tasks are now complete. Let me give the final report.

All three tasks are done. Here's the report.

## Task 1 — Recorded

**Location chosen:** `20_Progress/Internship/Building System/System - Build Log.md`, not `AI Conversation - Summaries/`. This file is the established, unbroken convention for every prior session on this exact project (every dated entry since 2026-07-16 lives there) — the Summaries folder is for cross-project AI-conversation captures, a different genre. No split needed.

Added two new dated entries. The first records the v0 audit's granular findings (444 tests, the `test_schema_drift.py` parametrization case, `test_filter.py`/`test_relevance.py` confirmed *not* redundant, the Dossier Corrections cross-reference, the README-v0 proposal stated as pending). The second records this session's Task 2 work.

**A correction, not a guess:** the prompt's context said `run.yml`'s disable was "almost certainly an emergency stopgap" and dated the write-starvation fix commit to 2026-08-30. The vault's *own* Build Log entry from earlier the same day — independently verified via `gh api`/`gh run list` — already says otherwise: it was a **deliberate human pause** to focus on the promotion batch, and the fix commit shipped 2026-08-28, *before* the pause. I recorded the discrepancy explicitly rather than quietly picking one version.

## Task 2

- **Tracking Standard vs. Internship Tracker Standard:** stale duplicate, not two scopes. The top-level file's own scope line always read "internship-only" — it predates the `Internship/` subfolder and was never migrated. Moved the real content into `Internship Tracker Standard.md`, left a one-line redirect at the old path, fixed the one live backlink.
- **Application Document Preparation.md:** moved into `Workflows/Internship/` — its three siblings were already there; no reason found for it being the odd one out. Fixed 8 live path-qualified backlinks.
- **`_Today/`/Deadline Tracker:** genuinely ungoverned. Wrote `Deadline and Intake Triage Standard.md` from the two live files plus Dossier Corrections directly. Left one question explicitly open (fold into the Weekly Discovery Review or stay separate) rather than deciding it myself.
- **Program/Contact/Applying Standards:** re-checked against the new resume/cover-letter and review-loop context, not carried forward blindly — conclusion still holds (the `-to-Create` notes already carry standard-depth guidance, zero conformance defects observed), but the re-check surfaced the real Applications-to-Create staleness that Task 3 then fixed.
- **Wrote:** Internship Tracker Standard (migrated), Deadline and Intake Triage Standard (new). **Found already adequate:** Internship Notes Standard, Internship Loop Review Standard, all templates.

## Task 3 — human answers applied

1. **Applications-to-Create.md rewritten** to route through `prepare → draft → plan → approve → humanize → write → link → apply`, with the Tracker/Program folder-moves explicitly deferred to the final `apply` step (previously they were wrongly tied to Applying-note *creation*).
2. **Real gap flagged, not backfilled:** only Appian got the full Program+Contact+Tracker trio. Uber/Western Digital/Deepgram (manual-web-finds) have Program notes only — confirmed by direct folder search, no Contact or Tracker note exists for any of the three. Flagged in both Contacts-to-Create.md and Trackings-to-Create.md.
3. **Screen-field cross-ref added** to Dossiers-to-Create.md and Programs-to-Create.md, pointing at `screened_date`/`screened_decision`/`screened_reason`.

All five notes now state their process fully enough to run from cold, and each names what's still unexercised (zero Applying notes exist; the Tailor sequence has never run for real) rather than implying it's proven.

### Tool Calls

- `Bash` -- `cd "D:\Users\_Anant\10_Areas\Documents\Jarvis" && echo "=== Build Log tail ===" && tail -n 60 "System - Build Log.md" 2>/dev/null || find . -iname "System - Build Log.md"`
```
=== Build Log tail ===
./20_Progress/Internship/Building System/System - Build Log.md
```
- `Glob` -- pattern `**/System - Build Log.md` path ``
- `Glob` -- pattern `60_Claude/07_AI_Information/AI Conversation - Summaries/**` path ``
- `Glob` -- pattern `30_Order/Standards/**/*.md` path ``
- `Glob` -- pattern `30_Order/Workflows/**/*.md` path ``
- `Glob` -- pattern `30_Order/Templates/Career/**/*.md` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Tracking Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Tracker Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Application Document Preparation.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Internship Pipeline.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Notes Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Loop Review Standard.md`
- `Glob` -- pattern `10_Areas/Career/Internships/List/Dossiers/_Today/**` path ``
- `Glob` -- pattern `10_Areas/Career/Internships/Tracker/**` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Grep` -- pattern `Tracking Standard` path `D:\Users\_Anant\10_Areas\Documents\Jarvis`
- `Grep` -- pattern `Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis`
- `Grep` -- pattern `Program.{0,20}Standard|Contact.{0,20}Standard|Applying.{0,20}Standard` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Runs\Claude Code Prompts — Archive.md`
- `Glob` -- pattern `**/Dossier Corrections.md` path ``
- `Glob` -- pattern `**/Resume & Cover Letter*.md` path ``
- `Grep` -- pattern `Program/Contact/Applying|don't need|no Standard needed|Standard.{0,10}not needed|low volume` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Runs\Claude Code Prompts — Archive.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Dossier Corrections.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Resume & Cover Letter - System Map.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Contacts\Each One\Contacts-to-Create.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Programs-to-Create.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Trackings-to-Create.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Applying\Applications-to-Create.md`
- `Grep` -- pattern `created:|date_noted|date_researched|date_created` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Current\Software Engineering Intern - Appian.md`
- `Glob` -- pattern `10_Areas/Career/Internships/Programs/**/*Appian*` path ``
- `Glob` -- pattern `10_Areas/Career/Internships/Contacts/**/*Appian*` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Considering\Software Engineering Intern - Appian.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Contacts\Each One\Ongoing\Software Engineering Intern - Appian.md`
- `Grep` -- pattern `_Today|Deadline Tracker` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Deadline Tracker.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\_Today\New Internships Listings.md`
- `Grep` -- pattern `_Today|Deadline Tracker|deadline sweep` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards`
- `Grep` -- pattern `_Today|Deadline Tracker|deadline sweep` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\_Today\No Deadline.md`
- `Grep` -- pattern `\[\[.*Tracking Standard.*\]\]` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\What was Viewed.md`
- `Grep` -- pattern `\[\[.*Tracking Standard.*\]\]` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Internship - Dashboard.md`
- `Grep` -- pattern `Tracking Standard` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Trackings-to-Create.md`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Tracker Standard.md`
```
---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-09-04
tags:
  - internship
  - standard
  - tracking
notes:
  - "[[Internship Pipeline]]"
  - "[[Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/Tracker/Internship - Dashboard]]"
next:
---
# Internship Tracker Standard
==Was an empty stub. Written after checking the one real Tracker note this system has ever produced (Appian, created 2026-07-26) directly against `Tracking Template.md` and [[Internship Pipeline]]'s own description of Step 3 and Step 8.== One real example is thin evidence, but it's genuine evidence, not a guess - it's cited throughout below.

==Moved here 2026-09-04 from the top-level `30_Order/Standards/Tracking Standard.md`, content unchanged== — that file was never a general vault tracking convention despite its name; its own §1 scope line already read "Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`," internship-specific from the day it was written. It predates the `30_Order/Standards/Internship/` subfolder (created later the same reorg that produced this file as an empty stub) and was never migrated in. Confirmed via direct read of both files before consolidating: no second, genuinely-general-purpose tracking standard exists anywhere else in the vault, so this is a stale duplicate location being closed, not two real scopes being merged.

## Scope
Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`. Does not govern `Tracker/Tracker.md` (a separate, hand-maintained kanban board - see §4) or `Tracker/Internship - Dashboard.md` (a separate, generated whole-system view - see §4). Both of those share the word "Tracker" with this folder but are distinct artifacts with distinct purposes; don't conflate them.

## 1. Frontmatter - required fields
Every Tracker note carries `Tracking Template.md`'s fields: `type: tracker, program, contact, company, url, date_noted, date_researched, date_created, date_applied, date_result, result, deadline, related_notes, tags, next`. The real Appian note confirms the template is followed as written - `program` and `contact` are wikilinks to the paired Program and Contact notes (not plain text), `related_notes` links back to the originating dossier, and unset date fields (`date_applied`, `date_result`, `result`, `deadline`) stay genuinely empty rather than defaulted to a placeholder.

**Created only once the paired Program note exists** (Internship Pipeline Step 3) - a Tracker note with no matching Program note is out of sequence and shouldn't exist. `program` and `contact` should resolve to real notes, not broken links, from the moment the Tracker note is created, since both are created together in the same sitting per Step 3.

## 2. Timeline and body - what each section is actually for
`## Timeline` is the dated index itself: Noted → Researched → Created → Applied → Result, one line each, filled in as the real dates happen, not backfilled from memory. The real Appian note shows the intended shape - `Noted: 2026-07-25`, `Researched: 2026-07-26`, `Created: 2026-07-26`, `Applied: —`, `Result: —`, all real dates, unset fields left as an em dash placeholder rather than deleted.

**A real, current gap between the template and the one real example**: `Tracking Template.md` also defines `### Company Information`, `### Conversation`, `### Interview Steps`, and a `## Loop Process` section under `## Summary` - none of these appear in the real Appian note, which only has `## Timeline` and `## Next Action`. This isn't necessarily wrong - the Appian note is still in `Current/`, pre-application, so Interview Steps and a completed Loop Process genuinely don't apply yet - but `## Summary` and `### Company Information` (a pointer to the Job & Company note) are template sections that should exist regardless of funnel stage, and the real note skips them. Until a second real Tracker note exists to compare against, treat this as an open question rather than a confirmed pattern: either the template is heavier than what's actually needed at `Current/` stage (revise it down), or the Appian note is incomplete (fill it in). Don't resolve this by guessing - check against the next Tracker note actually created.

**`## Next Action`** is the one section every real note should carry regardless of stage - the single next physical move, mirrored from (or feeding into) the paired Program note's own Traps & Gotchas or the Applying note's Next Action once one exists. The real Appian note uses this correctly: a concrete decision ("move from Considering to actually applying") tied to a concrete reason (the review-start date named on the Program note).

## 3. The Current/ → Applied/ → Result/ lifecycle
Mirrors [[Internship Pipeline]] Steps 3, 7, and 9 exactly:
- **`Current/`** - from creation (Step 3, paired with the Program and Contact notes) until a real application goes out. This is where the Appian note sits as of 2026-08-23.
- **`Applied/`** - moves here the moment `Applying/Now.md` gets an entry and the Applying note is created (Step 7), in the same sitting. `date_applied` is set at the same time as the move, not after.
- **`Result/`** - moves here once an outcome lands (Step 9), with `date_result` and `result` (`Offer`/`Rejected`/`Withdrawn` - the same three values the Applying note's `status` field uses) set at the same time as the move.
A Tracker note's folder and its `date_applied`/`date_result` fields should never disagree - if the note is in `Applied/`, `date_applied` is filled; if it's still in `Current/`, it isn't. This is a mechanical consistency check, not a judgment call - a note found out of sync is a real bug, not a stylistic issue.

> [!WARNING]
> **Stale against the resume/cover-letter system, flagged 2026-09-04, not yet resolved here.** [[30_Order/Workflows/Application Document Preparation]] moved Applying-note creation earlier — to the *start* of Step 5 (Tailor), not Step 7 (Apply) as the line above still says. This section's Tracker-side claim (`Applied/` move happens "in the same sitting" as Applying-note creation) is now only true for the *folder move*, not the *note creation* — the Applying note already exists by the time a Tracker note reaches `Applied/`. See [[10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create]] for the corrected sequencing once Task 3 of the 2026-09-04 session updates it.

## 4. Interlinking - Dashboard, the kanban, and a real current gap
`Tracker/Internship - Dashboard.md` is the whole-system view (per [[Internship Pipeline]]'s Ongoing Views). Checked directly against its live queries (2026-08-23): it queries `List/Dossiers`, `Programs/Serious` + `Programs/Considering`, and `20_Progress/Internship/Applying` - **it does not query `Tracker/Each One/` at all, in any of its current sections.** This is a real, currently-live gap, not a hypothetical: the Dashboard's "Applying — Live Status" section reads funnel stage from the Applying note's `status` field, which only exists once Step 7 happens, so a program sitting in `Tracker/Each One/Current/` pre-application (like Appian, right now) is invisible to the Dashboard entirely. The only way to see "where does this stand" for a pre-application program today is opening its Tracker note directly. Whether this is worth fixing (a Dashboard section reading `Current/`/`Applied/`/`Result/` counts, mirroring the Discovery/Programs sections' pattern) is a real, concrete improvement to flag - not something this Standard resolves on its own, since it's a Dashboard-note change, not a Tracker-note-content change.

`Tracker/Tracker.md` is a separate, entirely manual Kanban board (Interesting / To Apply / Applying Today / Applied columns, currently empty on all four as of 2026-08-23) - it is not generated from `Tracker/Each One/` notes and carries no automatic relationship to them. Per Internship Pipeline: "the kanban glance, this week's cards" - a lightweight manual view for weekly triage, not a source of truth. Don't expect it to reflect Tracker note state automatically; nothing currently keeps the two in sync.

## Done When
- Every Tracker note in `Current/`, `Applied/`, or `Result/` has its folder and its date fields agree.
- `program` and `contact` resolve to real notes on every Tracker note, no broken links.
- A Tracker note's `## Next Action` names a real, current, single next move - not stale from an earlier stage.
- The Dashboard/Tracker-note gap in §4 has been either fixed (a Dashboard section added) or explicitly deferred with a reason, not silently ignored.

```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Tracking Standard.md`
```diff
- ---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - internship
  - standard
  - tracking
notes:
  - "[[Internship Pipeline]]"
  - "[[Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/Tracker/Internship - Dashboard]]"
next:
---
# Tracking Standard
==Was an empty stub. Written after checking the one real Tracker note this system has ever produced (Appian, created 2026-07-26) directly against `Tracking Template.md` and [[Internship Pipeline]]'s own description of Step 3 and Step 8.== One real example is thin evidence, but it's genuine evidence, not a guess - it's cited throughout below.
+ ---
type: evergreen
status: tree
created: 2026-08-23
updated: 2026-09-04
tags:
  - internship
  - standard
  - tracking
  - redirect
notes:
  - "[[30_Order/Standards/Internship/Internship Tracker Standard]]"
next:
---
# Tracking Standard — Moved
==Superseded 2026-09-04.== This note's real content (never a general vault convention — its own scope line always read "Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`") moved to [[30_Order/Standards/Internship/Internship Tracker Standard]], the correctly-located, correctly-named home inside the `30_Order/Standards/Internship/` subfolder created during the internship-system reorg. That subfolder's copy was an empty stub until this move; this file is kept only as a redirect so no existing link breaks. Do not add new content here — edit the Internship Tracker Standard instead.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\What was Viewed.md`
```diff
- per [[Internship Notes Standard]]'s sibling [[30_Order/Standards/Tracking Standard]], a Tracker note moves
+ per [[Internship Notes Standard]]'s sibling [[30_Order/Standards/Internship/Internship Tracker Standard]], a Tracker note moves
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Tracking Standard.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Tracking Standard.md`
```diff
- ## Scope
Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`. Does not govern `Tracker/Tracker.md` (a separate, hand-maintained kanban board - see §4) or `Tracker/Internship - Dashboard.md` (a separate, generated whole-system view - see §4). Both of those share the word "Tracker" with this folder but are distinct artifacts with distinct purposes; don't conflate them.

## 1. Frontmatter - required fields
Every Tracker note carries `Tracking Template.md`'s fields: `type: tracker, program, contact, company, url, date_noted, date_researched, date_created, date_applied, date_result, result, deadline, related_notes, tags, next`. The real Appian note confirms the template is followed as written - `program` and `contact` are wikilinks to the paired Program and Contact notes (not plain text), `related_notes` links back to the originating dossier, and unset date fields (`date_applied`, `date_result`, `result`, `deadline`) stay genuinely empty rather than defaulted to a placeholder.

**Created only once the paired Program note exists** (Internship Pipeline Step 3) - a Tracker note with no matching Program note is out of sequence and shouldn't exist. `program` and `contact` should resolve to real notes, not broken links, from the moment the Tracker note is created, since both are created together in the same sitting per Step 3.

## 2. Timeline and body - what each section is actually for
`## Timeline` is the dated index itself: Noted → Researched → Created → Applied → Result, one line each, filled in as the real dates happen, not backfilled from memory. The real Appian note shows the intended shape - `Noted: 2026-07-25`, `Researched: 2026-07-26`, `Created: 2026-07-26`, `Applied: —`, `Result: —`, all real dates, unset fields left as an em dash placeholder rather than deleted.

**A real, current gap between the template and the one real example**: `Tracking Template.md` also defines `### Company Information`, `### Conversation`, `### Interview Steps`, and a `## Loop Process` section under `## Summary` - none of these appear in the real Appian note, which only has `## Timeline` and `## Next Action`. This isn't necessarily wrong - the Appian note is still in `Current/`, pre-application, so Interview Steps and a completed Loop Process genuinely don't apply yet - but `## Summary` and `### Company Information` (a pointer to the Job & Company note) are template sections that should exist regardless of funnel stage, and the real note skips them. Until a second real Tracker note exists to compare against, treat this as an open question rather than a confirmed pattern: either the template is heavier than what's actually needed at `Current/` stage (revise it down), or the Appian note is incomplete (fill it in). Don't resolve this by guessing - check against the next Tracker note actually created.

**`## Next Action`** is the one section every real note should carry regardless of stage - the single next physical move, mirrored from (or feeding into) the paired Program note's own Traps & Gotchas or the Applying note's Next Action once one exists. The real Appian note uses this correctly: a concrete decision ("move from Considering to actually applying") tied to a concrete reason (the review-start date named on the Program note).

## 3. The Current/ → Applied/ → Result/ lifecycle
Mirrors [[Internship Pipeline]] Steps 3, 7, and 9 exactly:
- **`Current/`** - from creation (Step 3, paired with the Program and Contact notes) until a real application goes out. This is where the Appian note sits as of 2026-08-23.
- **`Applied/`** - moves here the moment `Applying/Now.md` gets an entry and the Applying note is created (Step 7), in the same sitting. `date_applied` is set at the same time as the move, not after.
- **`Result/`** - moves here once an outcome lands (Step 9), with `date_result` and `result` (`Offer`/`Rejected`/`Withdrawn` - the same three values the Applying note's `status` field uses) set at the same time as the move.
A Tracker note's folder and its `date_applied`/`date_result` fields should never disagree - if the note is in `Applied/`, `date_applied` is filled; if it's still in `Current/`, it isn't. This is a mechanical consistency check, not a judgment call - a note found out of sync is a real bug, not a stylistic issue.

## 4. Interlinking - Dashboard, the kanban, and a real current gap
`Tracker/Internship - Dashboard.md` is the whole-system view (per [[Internship Pipeline]]'s Ongoing Views). Checked directly against its live queries (2026-08-23): it queries `List/Dossiers`, `Programs/Serious` + `Programs/Considering`, and `20_Progress/Internship/Applying` - **it does not query `Tracker/Each One/` at all, in any of its current sections.** This is a real, currently-live gap, not a hypothetical: the Dashboard's "Applying — Live Status" section reads funnel stage from the Applying note's `status` field, which only exists once Step 7 happens, so a program sitting in `Tracker/Each One/Current/` pre-application (like Appian, right now) is invisible to the Dashboard entirely. The only way to see "where does this stand" for a pre-application program today is opening its Tracker note directly. Whether this is worth fixing (a Dashboard section reading `Current/`/`Applied/`/`Result/` counts, mirroring the Discovery/Programs sections' pattern) is a real, concrete improvement to flag - not something this Standard resolves on its own, since it's a Dashboard-note change, not a Tracker-note-content change.

`Tracker/Tracker.md` is a separate, entirely manual Kanban board (Interesting / To Apply / Applying Today / Applied columns, currently empty on all four as of 2026-08-23) - it is not generated from `Tracker/Each One/` notes and carries no automatic relationship to them. Per Internship Pipeline: "the kanban glance, this week's cards" - a lightweight manual view for weekly triage, not a source of truth. Don't expect it to reflect Tracker note state automatically; nothing currently keeps the two in sync.

## Done When
- Every Tracker note in `Current/`, `Applied/`, or `Result/` has its folder and its date fields agree.
- `program` and `contact` resolve to real notes on every Tracker note, no broken links.
- A Tracker note's `## Next Action` names a real, current, single next move - not stale from an earlier stage.
- The Dashboard/Tracker-note gap in §4 has been either fixed (a Dashboard section added) or explicitly deferred with a reason, not silently ignored.
+ ## Read Instead
[[30_Order/Standards/Internship/Internship Tracker Standard]] — same content, current, kept up to date. This file is not.
```
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Claude Code\Jarvis\09-04 Internship research loop vault audit and standards consolidation.md`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Application Document Preparation.md`
```
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

```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Application Document Preparation.md`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Application Document Preparation.md`
```
---
type: evergreen
status: tree
created: 2026-08-28
updated: 2026-09-04
tags:
  - internship
  - redirect
notes:
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
next:
---
# Application Document Preparation — Moved
==Superseded 2026-09-04.== Moved to [[30_Order/Workflows/Internship/Application Document Preparation]] alongside its siblings ([[Internship - Design Rationale]], [[Internship Pipeline]], [[Promotion]]), all already in `30_Order/Workflows/Internship/`. Content unchanged at the new location. Do not add new content here.

```
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Resume Alteration.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Cover Letter Alteration.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Resume & Cover Letter - System Map.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Cover Letter Alteration Standard.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Internship Pipeline.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Humanized Writing Standard.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Resume Alteration Standard.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Humanizer.md`
- `Grep` -- pattern `\[\[30_Order/Workflows/Application Document Preparation` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship\Applying Template.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Resume Alteration.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Cover Letter Alteration.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Resume & Cover Letter - System Map.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Cover Letter Alteration Standard.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Internship Pipeline.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Humanized Writing Standard.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Resume Alteration Standard.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Humanizer.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship\Applying Template.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Tracker Standard.md`
```diff
- [[30_Order/Workflows/Application Document Preparation]]
+ [[30_Order/Workflows/Internship/Application Document Preparation]]
```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Deadline and Intake Triage Standard.md`
```
---
type: evergreen
status: sprout
created: 2026-09-04
updated: 2026-09-04
tags:
  - internship
  - standard
  - triage
notes:
  - "[[Internship Pipeline]]"
  - "[[Internship Notes Standard]]"
  - "[[Internship Loop Review Standard]]"
  - "[[20_Progress/Internship/Building System/V0/Dossier Corrections]]"
next: "Decide whether this triage cadence should fold into the Weekly Discovery Review (Internship Loop Review Standard) or stay a separate ad hoc sweep — not decided as of this writing, see #Relationship To The Loop Review below."
---
# Deadline and Intake Triage Standard
==Was ungoverned.== `10_Areas/Career/Internships/List/Dossiers/_Today/` and `10_Areas/Career/Internships/Tracker/Deadline Tracker.md` both exist and are both populated with real content, but no Standard or Workflow described what they're for or how they get maintained before this note. Written 2026-09-04 by reading both live, plus the one real sweep session that produced them — [[20_Progress/Internship/Building System/V0/Dossier Corrections]] (2026-08-28, "the deadline sweep") — rather than guessing intent from the folder name.

## Scope
Two related but distinct artifacts, both maintained by the same kind of session (a manual "deadline sweep," not automated code, not a step in [[Internship Pipeline]]):
- **`List/Dossiers/_Today/`** — pre-dossier intake triage. Holds raw candidate postings pulled from sources the automated `internship-research-loop` doesn't poll (InternDock's manually-browsed guides, `speedyapply`'s raw list dumps, and similar one-off feeds) — logged here *before* a decision is made on whether any of them becomes a real dossier or a manual-find Program note.
- **`Tracker/Deadline Tracker.md`** — a deadline-sorted view over dossiers that already exist in `List/Dossiers/` (any priority bucket), re-bucketed by urgency relative to the sweep date.
Neither is a substitute for [[Internship Notes Standard]] (which governs dossier content once written) or [[Internship Loop Review Standard]]'s Weekly Discovery Review (which grades gate/Standard conformance on a sample). This Standard governs intake and deadline currency only.

## 1. `_Today/New Internships Listings.md` — raw intake log
One dated pass-header per sweep (e.g. `## InternDock Guide 1 ([REDACTED]) — 2026-08-28 pass, "Software Engineering" section, entries 1-125 of 136`), naming the exact source guide/list and exactly which slice of it was covered — never "some entries," always a real count (the real 2026-08-28/08-29 passes cite `1-125 of 136`, `126-136`, `5 previously-unchecked entries`, `full pass (259 rows scanned)`). Under each header, one line per candidate posting: a markdown link (title → URL), then a short clause naming location/work-authorization signal, deadline if stated, and any timing ambiguity worth flagging rather than silently resolving (the real Whiterabbit.ai entry is a confirmed example — its title says "(2026)" not "(2027)," flagged inline rather than dropped or guessed).
**This is intake, not a gate.** Nothing here has been screened against [[Internship Pipeline]] Step 2's fit test or the four hard gates a real dossier would need to clear — a line on this list is a candidate worth a human look, not a vetted match. A candidate that survives a look either becomes a real dossier (written by hand into the correct priority folder, same frontmatter contract as an automated one — see [[Internship Notes Standard]] §1) or a direct manual-find Program note (skipping the dossier stage entirely, per [[Internship Pipeline]] Step 1's manual-web-clip rule) or is discarded with the reason left implicit (this list doesn't currently record rejections — only what passed a first read as worth listing at all).

## 2. `_Today/No Deadline.md` — confirmed-absent deadlines
Real dossiers, already written, checked directly (stored posting text, or a live fetch of the posting URL where the stored text didn't say) and confirmed to state no deadline as of the sweep date. Grouped by the same priority-bucket headings the dossiers themselves live under (`1 - AI & ML`, `2 - Fullstack`, etc.) — a plain flat list, one wikilink per dossier, no annotation needed since "no deadline" is the entire finding. States explicitly what's *out of scope* for the pass (a real deadline that exists but falls outside the sweep's stated window is deliberately not listed here — see the sweep's own report for those) — carry that same explicit-scope discipline forward in any future sweep rather than letting "confirmed no deadline" quietly drift into "didn't check."

## 3. `Tracker/Deadline Tracker.md` — urgency-bucketed view
Five buckets, re-anchored to the sweep's own stated "today" each time it's re-run (the real 2026-08-28 pass defined *Soon* = within 7 days, *Next Week* = 8–14 days, *Next Month* = 15–45 days, *Later* = beyond 45 days, plus a standing *Already Over* bucket for confirmed-lapsed deadlines) — state the cutoff dates explicitly at the top of the note, as the real version does, since "Soon" is meaningless without the anchor date next to it. One line per dossier: wikilink, then the deadline itself, distinguishing a confirmed stated deadline from an inferred/anticipated one (the real Western Digital entries mark two as `(anticipated)` and one as `(anticipated, live-verified)` — keep that distinction, don't collapse it to a bare date). **Already Over is not the same claim as closed** — a lapsed posted deadline doesn't mean the posting stopped accepting applications; per the real note's own caveat, none of the Already Over entries were re-fetched live to confirm the posting is actually gone versus just past its stated date, and that check stays a human task, not an assumption either way.

## 4. Refresh cadence — not scheduled, real gaps acknowledged
No cron or scheduled review currently re-runs this triage — the one real instance (2026-08-28, with a same-window follow-up pass 2026-08-29) was triggered manually, not on a cycle. This means both files can silently go stale (a "Soon" entry ages past its own bucket with nothing re-sorting it, a `_Today/` intake candidate sits unconverted indefinitely with no expiry). Don't treat either file's contents as current without checking the sweep date in its own header against today's date first.

## Relationship To The Loop Review
[[Internship Loop Review Standard]]'s Weekly Discovery Review already reads `logs/runs.jsonl` and samples real dossiers on a real cadence — whether deadline re-bucketing and `_Today/` intake conversion should become a section of that same weekly review, or stay this separate ad hoc sweep, is a real open question, not resolved here. Recommend folding it in (one recurring cadence beats two, and the Weekly review already has a "Resource-Limit Health" section this would sit naturally beside) but this is a call for whoever runs the next Weekly Discovery Review to make explicitly, not decided unilaterally by this Standard.

## Done When
- Every `_Today/New Internships Listings.md` pass-header names its exact source and exact entry range covered — no "a sample of" phrasing.
- Every `No Deadline.md` entry was checked directly (stored text or live fetch), not inferred from the dossier's classification alone.
- `Deadline Tracker.md`'s bucket cutoff dates are stated in the note itself and match the date of the sweep that last touched it.
- A `_Today/` intake candidate that's been sitting more than one sweep cycle without converting to a dossier or being discarded is a flagged gap, not silently carried forward forever.

```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Internship Pipeline.md`
```diff
- - **`Tracker/Each One/<name>.md`** — the per-internship dated index created in Step 3, moving `Current/` → `Applied/` → `Result/` as the real state changes.
+ - **`Tracker/Each One/<name>.md`** — the per-internship dated index created in Step 3, moving `Current/` → `Applied/` → `Result/` as the real state changes.
- **`List/Dossiers/_Today/` + `Tracker/Deadline Tracker.md`** — manual intake/deadline triage, run as an ad hoc sweep rather than a scheduled step. See [[Deadline and Intake Triage Standard]].
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Loop Review Standard.md`
```diff
- notes:
  - "[[30_Order/Standards/Review Standard]]"
  - "[[Internship Notes Standard]]"
  - "[[Internship Pipeline]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
+ notes:
  - "[[30_Order/Standards/Review Standard]]"
  - "[[Internship Notes Standard]]"
  - "[[Internship Pipeline]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
  - "[[Deadline and Intake Triage Standard]]"
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- **Not done this session**: no code touched, `run.yml` not re-enabled, `10_Areas/Career/` not reviewed, `Claude Code Prompts.md` not archived/renumbered — all explicitly held for the human's answers to the open questions raised in this session, per direct instruction to ask before making sweeping changes.
+ **Not done this session**: no code touched, `run.yml` not re-enabled, `10_Areas/Career/` not reviewed, `Claude Code Prompts.md` not archived/renumbered — all explicitly held for the human's answers to the open questions raised in this session, per direct instruction to ask before making sweeping changes.
## 2026-09-04 — v0 Audit Detail: Test Suite and Dossier-Housekeeping Findings Recorded; README Still a Proposal
A separate codebase-side session ran a "v0" audit of `internship-research-loop` — plan only, nothing shipped, pending human confirmation. This entry records its specific findings that the same-day entry above didn't already capture in this level of detail; nothing here has been independently re-verified against the live repo by this vault session (no repo access from here) — treat the numbers below as reported, not re-confirmed.
- **Test suite: 444 tests.** Real redundancy found in exactly one place — `tests/test_schema_drift.py` (46 tests, a near-mechanical 4-5-tests-per-source pattern repeated across all 11 sources) is a genuine parametrization candidate, already named as the throughput-plan's test target in the entry above. `test_filter.py`/`test_relevance.py` are dense but **not** redundant — nearly every test guards one specific real-world incident (Mosaic, Databricks, AbbVie, Prophet Security, the NL/HK/PL/IL location-gate gaps), consistent with this codebase's own "cite the real data" convention; consolidating those would delete real regression coverage, not just tidy it.
- **The 5-dossiers/hour target is already below the existing design ceiling.** Week-over-week `logs/runs.jsonl` data (same log as the entry above): matched candidates grew ~30x (689/week → 34,499/week) as sources went from 2 to 11, while the write budget stayed fixed at ~10/run (~1,680/week ceiling) — the write-starvation bug (fixed, unproven in production per the entry above) explains the throughput gap, not a capacity shortfall against the stated target.
- **Vault housekeeping cross-referenced against [[20_Progress/Internship/Building System/V0/Dossier Corrections]]** (the real 2026-08-28 deadline-sweep audit, report-only, nothing moved/merged/edited by that pass): ~10 likely duplicate dossier pairs (mostly ByteDance/AbbVie/Humana/Amex/Vanguard title variants of the same posting), a systemic quant-trading-firm bucket split (Optiver, IMC, Chicago Trading Company all have sibling postings filed in both `1 - AI & ML` and `3 - CyS & Finance` depending on which keyword matched), a confirmed `company` frontmatter typo (Montenson→Mortenson, 5 dossiers — confirmed directly from posting body text reading "Mortenson," not just inferred from a name search), and 6 Zipline dossiers still carrying the pre-fix SPA-listing-page content (the same extraction bug [[20_Progress/Internship/Building System/System - Build Log|this file's]] 2026-08-23 entry named) even though the underlying fix shipped elsewhere — nothing currently re-evaluates a dossier written before a fix lands.
- **README v0 direction — proposed, not built**: a generic (not personal-profile-hardcoded) eligibility config, setup instructions, and a `verify.py` concept letting a stranger check capture completeness against a live source feed. Explicitly a proposal pending human confirmation, per the audit's own scope — no file in the repo currently matches this.
> [!WARNING]
> **A framing correction, not a new fact.** The prompt that requested this audit be recorded characterized `run.yml`'s 2026-08-29 disable as "almost certainly an emergency stopgap during the write-starvation incident" and dated the write-starvation fix commit (`e856e05`) to 2026-08-30. Both are contradicted by this same file's own entry directly above, written the same day from a direct `gh api`/`gh run list` check: the disable was a **deliberate human pause** (`gh workflow disable run`, confirmed against [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 25) to focus on the promotion batch, not an emergency reaction — and `e856e05` shipped 2026-08-28, *before* the pause, not after it. Recorded here as-is rather than silently reconciled, since the discrepancy itself is worth knowing about, not just the corrected fact.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- > **A framing correction, not a new fact.** The prompt that requested this audit be recorded characterized `run.yml`'s 2026-08-29 disable as "almost certainly an emergency stopgap during the write-starvation incident" and dated the write-starvation fix commit (`e856e05`) to 2026-08-30. Both are contradicted by this same file's own entry directly above, written the same day from a direct `gh api`/`gh run list` check: the disable was a **deliberate human pause** (`gh workflow disable run`, confirmed against [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 25) to focus on the promotion batch, not an emergency reaction — and `e856e05` shipped 2026-08-28, *before* the pause, not after it. Recorded here as-is rather than silently reconciled, since the discrepancy itself is worth knowing about, not just the corrected fact.
+ > **A framing correction, not a new fact.** The prompt that requested this audit be recorded characterized `run.yml`'s 2026-08-29 disable as "almost certainly an emergency stopgap during the write-starvation incident" and dated the write-starvation fix commit (`e856e05`) to 2026-08-30. Both are contradicted by this same file's own entry directly above, written the same day from a direct `gh api`/`gh run list` check: the disable was a **deliberate human pause** (`gh workflow disable run`, confirmed against [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 25) to focus on the promotion batch, not an emergency reaction — and `e856e05` shipped 2026-08-28, *before* the pause, not after it. Recorded here as-is rather than silently reconciled, since the discrepancy itself is worth knowing about, not just the corrected fact.
## 2026-09-04 — Standards Consolidation: Tracker Standard Migrated, Application Document Preparation Relocated, Deadline/Intake Triage Standard Written
Vault-side only, no code touched. Follow-up to the partial `30_Order/Standards/Internship/`, `Workflows/Internship/`, `Templates/Career/Internship/` reorganization that had already happened by the time this session started (not this session's own work — found already in place, left incomplete).
- **`Tracking Standard.md` (top-level) → `30_Order/Standards/Internship/Internship Tracker Standard.md`.** Read both files directly before touching either: the top-level file was the real, populated Standard (written 2026-08-23); the subfolder file was an empty stub from the same reorg, never filled in. Checked the top-level file's own scope line first — "Applies to every note in `10_Areas/Career/Internships/Tracker/Each One/`" — confirming it was always internship-specific, not a general vault tracking convention living in the wrong place. No second scope existed to preserve; this was a stale duplicate location, not two real standards. Content moved as-is (one addition: a warning flagging the Applied/-move-timing line as stale against [[30_Order/Workflows/Internship/Application Document Preparation]]'s later Applying-note-creation change, not yet reconciled). Old file left as a one-line redirect stub, not deleted — one real backlink ([[10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed]]) fixed to the new path directly.
- **`Application Document Preparation.md` (top-level `Workflows/`) → `Workflows/Internship/`.** Its siblings ([[Internship - Design Rationale]], [[Internship Pipeline]], [[Promotion]]) had already moved into `Workflows/Internship/` in the same reorg; this file hadn't, with no scope reason found for the difference. Moved, old file left as a redirect stub. Eight live backlinks (path-qualified, would have broken silently) fixed directly: both V0 design notes (Resume/Cover Letter Alteration), the System Map, both enforceable-layer Standards, Humanized Writing Standard, the Applying Template, and Internship Pipeline itself.
- **[[30_Order/Standards/Internship/Deadline and Intake Triage Standard]] written — was ungoverned.** `List/Dossiers/_Today/` (raw intake from sources the automated loop doesn't poll — InternDock guides, speedyapply dumps) and `Tracker/Deadline Tracker.md` (deadline-urgency-bucketed dossier view) both exist with real content from the 2026-08-28/08-29 deadline sweep but had no Standard or Workflow describing either before now. Written from the two live files plus [[20_Progress/Internship/Building System/V0/Dossier Corrections]] directly, not guessed from folder names. Left one real open question un-decided rather than resolving it unilaterally: whether this triage cadence should fold into [[Internship Loop Review Standard]]'s Weekly Discovery Review or stay a separate ad hoc sweep.
- **Program/Contact/Applying Standard question re-checked, not carried forward unchanged.** Two prior sessions ([[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]], Prompts 8 and 11) had already decided no dedicated 30_Order Standard was needed, on low volume and zero observed defects — both explicitly scoped to a dossier-focused audit that never touched Program/Contact/Applying notes. Re-evaluated this session against genuinely new context (the resume/cover-letter system and its evidence-chain/approval-gate machinery, both nonexistent at the time of Prompts 8/11): the existing `*-to-Create.md` directive notes in each folder already carry section-by-section content guidance at a depth comparable to a Standard, and zero conformance defects have been found in real Program/Contact notes (Appian, plus three manual-web-find Program-only promotions) — the recommendation still stands, same conclusion as before but re-derived, not assumed. The one real gap this re-check did surface — [[20_Progress/Internship/Applying/Applications-to-Create]]'s Trigger section describing the old submission-time Applying-note-creation model, contradicted by [[30_Order/Workflows/Internship/Application Document Preparation]]'s later change — is a content staleness issue in that specific note, not evidence a new Standard is needed; left for the five `-to-Create` notes' own update pass.
```
- `Glob` -- pattern `10_Areas/Career/Internships/Contacts/**/*{Uber,Western Digital,Deepgram}*` path ``
- `Glob` -- pattern `10_Areas/Career/Internships/Tracker/Each One/**/*{Uber,Western Digital,Deepgram}*` path ``
- `Glob` -- pattern `10_Areas/Career/Internships/Programs/Serious/*{Uber,Western,Deepgram}*` path ``
- `AskUserQuestion` -- `{"questions":[{"question":"Applications-to-Create.md\u0027s \"Trigger\" section says creating the Applying note is the same action as moving the Tracker note Current/→Applied/ and the Program note into Ended/, all in one sitting. That\u0027s the old model — Application Document Preparation.md (2026-08-28) moved Applying-note creation to the START of Tailor (Step 5), well before submission, with the Tracker/Program moves now only happening later at actual Apply (Step 7). Should I rewrite Applications-to-Create.md to route through the full prepare→draft→plan→approve→humanize→write→link→apply sequence, with the Tracker/Program folder-moves explicitly deferred to the final \"apply\" sub-step?","header":"Trigger fix","multiSelect":false,"options":[{"label":"Yes, rewrite to match Application Document Preparation (Recommended)","description":"Applications-to-Create.md becomes the authoritative version of the Trigger; old submission-time framing is corrected, not just cross-referenced."},{"label":"Cross-reference only, don\u0027t restate","description":"Applications-to-Create.md keeps a short pointer to Application Document Preparation for the full sequence and doesn\u0027t try to restate it in its own words."}]},{"question":"Real data: only Appian (the one loop-discovered, /promote-dossier promotion) got a paired Contact + Tracker note alongside its Program note. The other 3 real promotions — Uber, Western Digital, Deepgram, all manual-web-finds — only ever got a Program note; no Contact or Tracker note exists for any of them. Contacts-to-Create.md and Trackings-to-Create.md both currently assume every Program note gets a paired Contact/Tracker note. Is the 3-note-trio missing on those three a real gap to flag (and maybe backfill), or expected because manual finds skip the loop\u0027s enrich.py-triggered contact research?","header":"Manual-find gap","multiSelect":false,"options":[{"label":"Real gap — flag it, note backfill is optional","description":"The five notes should say explicitly that a manual-find Program note without a paired Contact/Tracker is a known incomplete state, not silently assumed-fine."},{"label":"Expected — manual finds legitimately skip Contact/Tracker","description":"Contacts-to-Create.md and Trackings-to-Create.md should be corrected to say the trio is only guaranteed for loop-discovered promotions."},{"label":"Not sure — go backfill Contact/Tracker notes for those three first","description":"Before writing the rule down, actually create the missing Contact/Tracker notes for Uber/Western Digital/Deepgram so there\u0027s a real second example to check the template against, same discipline Tracking Standard already used."}]},{"question":"None of the five -to-Create notes currently mention the Screen step\u0027s frontmatter fields (screened_date/screened_decision/screened_reason, added to Internship Notes Standard §7) or the Internship Loop Review\u0027s Monthly Promotion Review, even though both directly touch the same notes these five govern. Should I add explicit cross-references now?","header":"Cross-refs","multiSelect":true,"options":[{"label":"Add Screen-field cross-ref to Dossiers/Programs-to-Create (Recommended)","description":"Programs-to-Create.md\u0027s step 1 (\"a dossier passes the fit test\") should point at where that decision actually gets recorded (screened_* fields)."},{"label":"Add Monthly Promotion Review cross-ref to all five","description":"Each note gets a line noting it\u0027s graded by the Monthly Promotion Review\u0027s Pipeline Checklist / Note-Shape Conformance sections."},{"label":"Skip both — out of scope for these five notes","description":"Leave the five notes focused purely on note-creation mechanics; cross-references to Screen/Review live better in the Standards themselves, already done in Task 2."}]}]}`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Applying\Applications-to-Create.md`
```diff
- ---
type: evergreen
status: active
created: 2026-07-26
notes:
  - "[[Internship Pipeline]]"
  - "[[Applying Template]]"
  - "[[Now]]"
  - "[[_This Week]]"
tags:
  - internship
  - process
next: First real entry lands once a Tracker note actually moves from Current/ to Applied/.
---
# Applying — How Notes Get Created Here
==One Applying note per internship, created only once real application activity actually starts — not at commit time, and not just because a Program note exists.== Per [[Applying Template]] and [[Internship Pipeline]] Step 4: this is where source-of-truth responsibility for "what's going on with this application" transfers from the Tracker note's dated index to a live narrative — Current State, Next Action, Open Questions, whatever's useful to have on hand in a meeting.
## The Trigger
Creating an Applying note is the same action as moving the paired Tracker note from `Tracker/Each One/Current/` to `Applied/`, and the paired Program note from `Programs/Serious/` (or `Considering/`) into its own `Ended/` subfolder — all three happen in the same sitting, not staggered across sessions.
## What Belongs In The Note — Section By Section
+ ---
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
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Contacts\Each One\Contacts-to-Create.md`
```diff
- ---
type: evergreen
status: active
created: 2026-07-26
notes:
  - "[[Internship Pipeline]]"
  - "[[Mimic]]"
  - "[[Networking Strategies]]"
tags:
  - internship
  - process
next: Fill in a real Networking Strategies note — currently empty despite being linked from here.
---
# Contacts/Each One — How Notes Get Created Here
==One contact-research note per internship, created at the same time as the Program note, never before.== Company-level, not person-level — a single note can (and usually will) list several real people found for that one internship, per [[Mimic]]'s scenario templates for the actual outreach drafts.
## How It Gets Created
Written by the `contact-researcher` agent, invoked from the `/promote-dossier` skill at commit time (Step 3 of [[Internship Pipeline]]) — public sources only (GitHub org members, engineering-blog bylines, MX-validated pattern-inferred email, scoped recruiter/university-recruiting search, LinkedIn search-snippets — never a fetch of the actual LinkedIn page). Every fact carries its source inline; "nothing found" is a valid, honest outcome, never papered over with a plausible-sounding guess.
+ ---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-09-04
notes:
  - "[[Internship Pipeline]]"
  - "[[Mimic]]"
  - "[[Networking Strategies]]"
tags:
  - internship
  - process
next: Fill in a real Networking Strategies note — currently empty despite being linked from here.
---
# Contacts/Each One — How Notes Get Created Here
==One contact-research note per internship, created at the same time as the Program note, never before.== Company-level, not person-level — a single note can (and usually will) list several real people found for that one internship, per [[Mimic]]'s scenario templates for the actual outreach drafts.
## How It Gets Created
Written by the `contact-researcher` agent, invoked from the `/promote-dossier` skill at commit time (Step 3 of [[Internship Pipeline]]) — public sources only (GitHub org members, engineering-blog bylines, MX-validated pattern-inferred email, scoped recruiter/university-recruiting search, LinkedIn search-snippets — never a fetch of the actual LinkedIn page). Every fact carries its source inline; "nothing found" is a valid, honest outcome, never papered over with a plausible-sounding guess.
> [!WARNING]
> **Real gap, confirmed 2026-09-04, not yet resolved.** `/promote-dossier`'s `contact-researcher` step only runs for a loop-discovered dossier going through the actual skill — the one time this has happened for real (Appian, 2026-07-26), the Program+Contact+Tracker trio landed together as designed. The three *manual-web-find* promotions ([[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], [[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], [[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], all 2026-07-29) never went through `/promote-dossier` at all — they have Program notes and **no paired Contact note exists for any of the three**, confirmed by direct folder search, not assumed. This is a real incomplete state, not a silent design choice: [[Internship Pipeline]] Step 1's manual-web-clip rule says a manual find "runs through the same Step 2 fit test" and enters at the same Step 3 commit point as a loop-discovered one, which per Step 3 means a Contact note should exist too. Backfilling the three missing Contact notes is optional, not required by this note alone — flagged here so it isn't mistaken for "nothing missing" the next time someone checks this folder against `Programs/Serious/`.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Trackings-to-Create.md`
```diff
- ---
type: evergreen
status: active
created: 2026-07-26
notes:
  - "[[Internship Pipeline]]"
  - "[[Tracking Template]]"
  - "[[Application Tracker]]"
tags:
  - internship
  - process
next: Point Application Tracker.md's Current/Applied/Rejected/Accepted sections at these folders once real Tracker notes exist to query.
---
# Tracker/Each One — How Notes Get Created Here
==One dated index note per internship that's made it to a Program note — the fast-scan source of truth for "where does this stand" until a real Applying note exists.== Created only after the Program note exists, per [[Tracking Template]]'s frontmatter contract. Not a duplicate of the Applying note — Tracker is the *timeline* (dates, links, deadline), Applying is the *narrative* (Current State, Next Action, Open Questions, meeting-prep content). Both stay live at once once an application starts; they don't replace each other.
+ ---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-09-04
notes:
  - "[[Internship Pipeline]]"
  - "[[Tracking Template]]"
  - "[[Application Tracker]]"
  - "[[30_Order/Standards/Internship/Internship Tracker Standard]]"
tags:
  - internship
  - process
next: Point Application Tracker.md's Current/Applied/Rejected/Accepted sections at these folders once real Tracker notes exist to query.
---
# Tracker/Each One — How Notes Get Created Here
==One dated index note per internship that's made it to a Program note — the fast-scan source of truth for "where does this stand" until a real Applying note exists.== Created only after the Program note exists, per [[Tracking Template]]'s frontmatter contract. Not a duplicate of the Applying note — Tracker is the *timeline* (dates, links, deadline), Applying is the *narrative* (Current State, Next Action, Open Questions, meeting-prep content). Both stay live at once once an application starts; they don't replace each other. Field-level rules and the `Current/`→`Applied/`→`Result/` lifecycle are fully specified in [[30_Order/Standards/Internship/Internship Tracker Standard]] — this note covers only *when and how* a Tracker note gets created, not its content rules in full.
> [!WARNING]
> **Real gap, confirmed 2026-09-04.** The rule below ("created only after the Program note exists") should mean every real Program note has a paired Tracker note. It doesn't: the three manual-web-find promotions ([[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], [[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], [[10_Areas/Career/Internships/Programs/Serious/[REDACTED]]], all 2026-07-29) have no paired Tracker note, confirmed by direct folder search — only Appian (the one `/promote-dossier`-driven promotion) got the full three-note trio. Same finding as [[10_Areas/Career/Internships/Contacts/Each One/Contacts-to-Create]]'s parallel gap — flagged, backfill optional, not resolved here.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Programs-to-Create.md`
```diff
- ## The Actual Process
1. A dossier (or a hand-found lead that never went through the automated pipeline) passes the fit test — see [[Internship Pipeline]] Step 2. Goal-push, personal fit, contact-reachability noted-not-gated, pay never a factor.
+ ## The Actual Process
1. A dossier (or a hand-found lead that never went through the automated pipeline) passes the fit test — see [[Internship Pipeline]] Step 2. Goal-push, personal fit, contact-reachability noted-not-gated, pay never a factor. **The call itself gets recorded on the dossier**, not just made mentally — `screened_date`/`screened_decision`/`screened_reason` fields, per [[Internship Notes Standard]] §7. A dossier promoted into a Program note without those fields set is a real, checkable gap (the fields aren't retroactive, so a dossier that predates §7 won't have them — that's expected, not a violation).
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
```diff
- ## What Does Not Belong Here
A lead you found yourself - career fair, LinkedIn, a referral - never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[Internship Pipeline]] Step 1, skipping this folder entirely.
+ ## What Does Not Belong Here
A lead you found yourself - career fair, LinkedIn, a referral - never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[Internship Pipeline]] Step 1, skipping this folder entirely.
## After The Gate — Screen Gets Recorded Here Too
Once a dossier clears the eligibility/relevance/classification gates above, [[Internship Pipeline]] Step 2's fit test (goal-push, personal fit, contact-reachability noted-not-gated) still has to happen before promotion — and per [[Internship Notes Standard]] §7, that decision is written back onto the dossier itself (`screened_date`/`screened_decision`/`screened_reason`), not left as an unrecorded mental check. This isn't automated by the loop — it's a human (or Claude, assisting one) recording a real Screen call at the moment it happens, same footing as the gate fields above even though a different party writes them.
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
```diff
- ## What Does Not Belong Here
A lead you found yourself — career fair, LinkedIn, a referral — never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[Internship Pipeline]] Step 1, skipping this folder entirely.
+ ## What Does Not Belong Here
A lead you found yourself — career fair, LinkedIn, a referral — never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[Internship Pipeline]] Step 1, skipping this folder entirely.
## After The Gate — Screen Gets Recorded Here Too
Once a dossier clears the eligibility/relevance/classification gates above, [[Internship Pipeline]] Step 2's fit test (goal-push, personal fit, contact-reachability noted-not-gated) still has to happen before promotion — and per [[Internship Notes Standard]] §7, that decision is written back onto the dossier itself (`screened_date`/`screened_decision`/`screened_reason`), not left as an unrecorded mental check. This isn't automated by the loop — it's a human (or Claude, assisting one) recording a real Screen call at the moment it happens, same footing as the gate fields above even though a different party writes them.
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Programs-to-Create.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
```diff
- created: 2026-07-26
tags:
  - internship
  - process
  - automation
notes:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[Dossiers MOC]]"
+ created: 2026-07-26
updated: 2026-09-04
tags:
  - internship
  - process
  - automation
notes:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[Dossiers MOC]]"
  - "[[Internship Notes Standard]]"
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Programs-to-Create.md`
```diff
- created: 2026-07-26
tags:
  - internship
  - process
notes:
  - "[[Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Programs/Programs MOC]]"
  - "[[Claude Code Prompts]]"
+ created: 2026-07-26
updated: 2026-09-04
tags:
  - internship
  - process
notes:
  - "[[Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Programs/Programs MOC]]"
  - "[[Claude Code Prompts]]"
  - "[[Internship Notes Standard]]"
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Applying\Applications-to-Create.md`
- `Bash` -- `cd "D:\Users\_Anant\10_Areas\Documents\Jarvis" && git status --short | head -30`
```
 M .obsidian/plugins/recent-files-obsidian/data.json
 M 10_Areas/Career/Internships/Contacts/Mimic.md
 M "10_Areas/Career/Internships/Internships Hub.md"
 M "10_Areas/Career/Internships/List/2026-07 Found.md"
 M "10_Areas/Career/Internships/List/Dossiers MOC.md"
 M 10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md
 M "10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md"
 M "10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed.md"
 M "10_Areas/Career/Internships/Programs/Programs MOC.md"
 M 10_Areas/Career/Internships/Programs/Programs-to-Create.md
 M 10_Areas/Career/Internships/README.md
 M "10_Areas/Career/Internships/Tracker/Each One/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md"
 M "10_Areas/Career/Internships/Tracker/Each One/AI and Data Engineering Summer Scholar Intern - Government & Public Services - Deloitte.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Current/Software Engineering Intern - Appian.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Data Analytics Intern - Global Servicing - Financial Crimes Risk & Controls - American Express.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Data Engineer Intern - Data - LPL Financial Holdings.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Data Intern - Key Technology & Services - Data Track - KeyBank.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Data Science Machine Learning Intern - Castleton Commodities International.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Full-Stack Software Engineer Intern - Castleton Commodities International.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Software Engineer Co-Op - Enterprise Finance Applications - Summer 2027 - Fifth Third Bank.md"
 M "10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create.md"
 M "10_Areas/Career/Internships/Tracker/Habit Tracker.md"
 M "10_Areas/Career/Internships/Tracker/Internship - Dashboard.md"
 M "20_Progress/AI/Claude Code/CausalOps/Sync-Log.md"
 M "20_Progress/AI/Claude Code/Jarvis/Sync-Log.md"
 M "20_Progress/AI/Claude Code/OpsPilot/Sync-Log.md"
 M "20_Progress/AI/Claude Code/Portfolio/Sync-Log.md"
 M "20_Progress/AI/Claude Code/Resq/Sync-Log.md"
 M "20_Progress/AI/Claude Code/The Plan/Sync-Log.md"
 M "20_Progress/AI/Claude Code/Trading View/Sync-Log.md"
```

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Deadline and Intake Triage Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Tracker Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Application Document Preparation.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Application Document Preparation.md`

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Contacts\Each One\Contacts-to-Create.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Dossiers-to-Create.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\What was Viewed.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Programs-to-Create.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Trackings-to-Create.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Applying\Applications-to-Create.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Resume & Cover Letter - System Map.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Cover Letter Alteration.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Humanizer.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\V0\Resume Alteration.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Humanized Writing Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Cover Letter Alteration Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Internship Loop Review Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship\Resume Alteration Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Tracking Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship\Applying Template.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship\Internship Pipeline.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `cd "D:\Users\_Anant\10_Areas\Documents\Jarvis" && echo "=== Build Log tail ===" && tail -n 60 "System - Build Log.md" 2>/dev/null || find . -iname "System - Build Log.md"`
- `cd "D:\Users\_Anant\10_Areas\Documents\Jarvis" && git status --short | head -30`


