---
type: project
status: active
created: 2026-07-26
updated: 2026-08-30
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts —
    Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompts 24/25 archived 2026-08-30 (both fully complete — external sweep
  and dossier reconciliation genuinely closed, with one factual correction
  logged: ApplyGuy is not a new source, it's been live since Prompt 17). Hourly
  run.yml is paused (human's deliberate call, 2026-08-30, gh workflow disable —
  re-enable with gh workflow enable run when discovery should resume). Prompts
  26/27 pivot to actual promotion: two parallel Codebase sessions, each invoking
  /promote-dossier on a real, deadline-ordered half of the 15 dossiers in
  Tracker/Deadline Tracker.md's Soon/Next Week/Next Month buckets. This is
  deliberately NOT a 300-application mass-apply — that was the human's opening
  framing but the actual ask (confirmed in the request itself) was building real
  Program/Contact/Tracker notes, which only exist for 15 dossiers with a
  genuinely known near-term deadline right now. /promote-dossier's own consent
  gate is preserved, not bypassed. Reach Out and Apply remain explicit human
  steps after these notes exist — not attempted by these prompts."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **A hypothesis this file itself wrote can turn out wrong — say so plainly when it does, don't quietly drop it.** Prompt 14 v2's own JGCL hypothesis (a `SOURCES`-tuple tie-break bug) was checked and found wrong; the real cause was three specific already-deleted scholarship postings. That's now the record, not the guess that preceded it — every doc touched below corrects to the real finding, not a hedge between the two.
- **An alarming-sounding fact ("46 deletions") is worth one direct check before treating it as a problem.** It resolved in one search — a real, already-tracked session (auto-captured, per this vault's own conversation-export layer), not an untracked gap. Cheap to verify, expensive to leave as a nagging unresolved worry across future prompts.
- **When a real source count changes, every doc that states a specific number becomes a small, precise lie until corrected.** Lever going live makes "eight sources" wrong wherever it's written — treat this the same as any other now-stale claim, not a footnote.

---

- **A local git checkout goes stale fast on this project — the pipeline auto-commits hourly.** Read state files via `git show origin/master:<path>`, or `git fetch` + confirm local `HEAD` matches `origin/master` (pull/rebase if not) before trusting any local working-tree read of anything `run_pipeline.py`/`recheck.py` touches. Caught live 2026-08-27: a local `git show`-free read of `state/debate_losses.json` showed 6 entries where `origin/master`'s real, current file had 271 — a local clone can sit dozens of commits behind within a single day.

- **A session sharing a file with a parallel session must only ever append or fix its own entries — never remove something it didn't write because it looks unfamiliar or out of scope.** Real incident, 2026-08-28: Prompt 21's session found 6 legitimate links Prompt 20's session had added to a shared `No Deadline.md` (companies with no existing dossier, correctly out of Prompt 21's own 320-dossier scope) and deleted them as presumed noise during its own cleanup pass. Caught and restored by the coordinating session, not by either prompt session itself. If something in a shared file looks wrong, say so in the report — don't unilaterally remove it.
- **When a follow-up genuinely needs the same deep context a session just built (e.g., re-checking its own just-completed work), tell the human to continue in the SAME session, not paste into a fresh one.** Re-deriving 320 already-read dossiers from scratch in a new session would re-burn the exact token cost being complained about — this project's usual "fresh session per prompt" default is a good default, not an absolute rule, when continuity itself is the point.

# Codebase
### Prompt 26: Batch Program + Contact + Tracker Notes — Deadline-Priority Batch A (8 dossiers)
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first, then invoke the `/promote-dossier` skill for each dossier below in order — don't build these notes freehand, the skill already encodes the real template contract, the contact-researcher agent invocation, and (deliberately, by this project's own design) a human consent gate before each write. Confirm the Jarvis vault is reachable (sibling checkout or `jarvis` MCP tools) before starting, per the skill's own prerequisite.

```
**Context — real, verified 2026-08-30, don't re-derive:** These 8 dossiers are drawn directly from `Tracker/Deadline Tracker.md`'s real, already-confirmed deadlines (built across Prompts 21/23/25's deadline sweep) — every date below is a real deadline read from the dossier's own posting text or a live confirmation, not estimated. Ordered by deadline, most urgent first:

1. `List/Dossiers/1 - AI & ML/Data Science Machine Learning Intern - Castleton Commodities International.md` — deadline 2026-09-01
2. `List/Dossiers/2 - Fullstack/Full-Stack Software Engineer Intern - Castleton Commodities International.md` — deadline 2026-09-01
3. `List/Dossiers/3 - CyS & Finance/Data Intern - Key Technology & Services - Data Track - KeyBank.md` — deadline 2026-09-04
4. `List/Dossiers/1 - AI & ML/Data Engineer Intern - Data - LPL Financial Holdings.md` — priority deadline 2026-09-21
5. `List/Dossiers/1 - AI & ML/AI and Data Engineering Summer Scholar Intern - Government & Public Services - Deloitte.md` — deadline 2026-09-24
6. `List/Dossiers/1 - AI & ML/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md` — deadline 2026-09-30
7. `List/Dossiers/Other/Data Analytics Intern - Global Servicing - Financial Crimes Risk & Controls - American Express.md` — deadline 2026-10-01
8. `List/Dossiers/1 - AI & ML/Software Engineer Co-Op - Enterprise Finance Applications - Summer 2027 - Fifth Third Bank.md` — deadline 2026-10-09

**Efficiency note, real: two of these (#1/#2) share a company (Castleton Commodities International).** Do the real contact-research pass once per company where possible and reuse it across that company's dossiers — don't pay for duplicate research on the same employer's recruiting org.

**Scope — this builds Program + Contact + Tracker notes only (Internship Pipeline.md's Screen→Commit step), not further.** Reach Out and Apply are the human's own next actions once these notes exist — don't attempt to draft outreach messages or submit anything on an external site as part of this prompt.

**Discipline:** real research only, no fabricated fields (the contact-researcher agent already refuses to fabricate — trust that, don't override it under time pressure). The skill's consent gate is deliberate — go through it for each dossier, don't look for a way around it.

### Report back
Per dossier: Program note created (Serious/ or Considering/, with your reasoning), Contact note created (or "genuinely nothing found," which is a valid, honest outcome), Tracker note created. Anything that hit a real blocker (dead posting, no reachable contact signal at all) — say so plainly, don't force a fabricated note through.
```

### Prompt 27: Batch Program + Contact + Tracker Notes — Deadline-Priority Batch B (7 dossiers)
**Fresh session**, `gupta-builds/internship-research-loop`. Runs in parallel with Prompt 26 in a separate terminal. Same setup: read `CLAUDE.md`, confirm vault reachability, invoke `/promote-dossier` per dossier, same consent-gate discipline as Prompt 26 — don't duplicate that context here, it applies identically.

```
**The other half of the same real, deadline-ordered list** (round-robin split with Prompt 26 so both sessions cover the full urgency range, not front-loaded/back-loaded):

1. `List/Dossiers/2 - Fullstack/Data Engineering Intern - Castleton Commodities International.md` — deadline 2026-09-01
2. `List/Dossiers/1 - AI & ML/Analytics and Quantitative Modeling Intern - Analytics & Quantitative Modeling - KeyBank.md` — deadline 2026-09-04
3. `List/Dossiers/1 - AI & ML/Machine Learning Intern - OpRegen Machine Learning - Genentech.md` — deadline 2026-09-08
4. `List/Dossiers/1 - AI & ML/Software Engineer Intern - LPL Financial Holdings.md` — priority deadline 2026-09-21
5. `List/Dossiers/Other/Technology, Operations, Digital, and Data Analytics Intern - Regions Bank.md` — deadline 2026-09-25
6. `List/Dossiers/3 - CyS & Finance/Infrastructure Engineer Intern [2027 Intern Program] - DTCC.md` — deadline 2026-10-01
7. `List/Dossiers/Other/Application Engineer Co-opIntern - PCS - GE Vernova.md` — deadline 2026-10-02

**Efficiency note, real: two of these (#1 here, plus #3 in Prompt 26's list) share Castleton Commodities International, and #4 here shares LPL Financial with #4 in Prompt 26's list.** These are running in two different sessions, so you can't literally reuse the other session's research — but check whether either company's contact/program info is already sitting in a `Considering/`/`Serious/` note or a Contact note from prior work before re-researching from zero.

Same scope boundary, same discipline, same report-back shape as Prompt 26 — see that prompt's text for the full detail, it applies identically here.
```

