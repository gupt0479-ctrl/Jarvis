---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Internship-research-loop postmortem and gaps"
started_at: 2026-08-26T17:09:28
ended_at: 2026-08-26T19:47:02
exported_at: 2026-08-28T13:00:02
duration_minutes: 157.6
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: 48087f6f-1442-42d9-9cca-fcafbf8038ef
status: raw
turn_count: 2
tools_used:
  Bash: 17
  Edit: 4
  Read: 35
  Write: 1
tokens:
  input: 186
  output: 162962
  cache_creation: 811334
  cache_read: 16543748
  total: 17518230
cost_usd: 8.184078
model:
  - "claude-sonnet-5"
files_touched:
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/loop-verifier.md"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change/SKILL.md"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/CLAUDE.md"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/classify.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/debate.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/filter.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/git_ops.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/identity.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/freehire.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/interndock.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/sources.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/PRD.md"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/recheck.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/revalidate.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py"
  - "//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\Runs\\Discovery Step Postmortem — Write-Starvation Incident (2026-08-26).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\Source of Truth.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\System - Build Log.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship Loop Review Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship Notes Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Internship Pipeline.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Internship Loop Reviews MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Scheduled\\Monthly\\Internship Loop Monthly Review — 2026-08.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Scheduled\\Weekly\\Internship Loop Weekly Review — 2026-W34.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Internship-research-loop postmortem and gaps

## You

Dive deep inside the internship-research-loop that we have established so far. I am lost on what to build next. Except promoting dossiers into program notes and programs to applying notes. What do we need to establish? The review system is not in depth and stale, we need to tighten that gap based on the review that has already been run. Except this, i am extremely lost on the next courses of actions required. Help me identify the gaps in the internship search/discovery. Postmortem the existing disvoery step in detail. I want to to fix these things in detail (already in execution unfortunately). After finding a detailed postmortem, make a list of adversaries on the entire internship loop established. Look at the system build in extreme detail before you do any of these things. Look through each and every single note, each and every single execution, skills, commands, setup entirely. I want everything to be looked at before the postmortem or adversary lands.

## Claude

I'll start by mapping the actual scope of the internship system before touching anything else - folders, skills, commands, and logs involved.

Found the actual code repo in WSL. Let me get its structure before deciding how to split the deep-dive work.

I now have a complete, verified picture of the entire system: every module in the discovery pipeline's code, four-plus days of real production logs, current live state files, the full review system and both reviews that have run, and the complete build history back to 2026-07-16. One finding dominates everything else — a live, currently-active, previously-undocumented failure. Let me write this up properly.

I need to fix the ordering — I inserted the new entry before the 08-24 entry, breaking this file's chronological order. Let me move it to the end where it belongs.

I read the entire discovery pipeline end to end (every module in `core/`, `ingestion/`, `vault_writer/`, plus `run_pipeline.py`, `recheck.py`, `revalidate.py`, `git_ops.py`), 82 real hourly production run records, current live state files, the full review system (Standard + both reviews that have actually run + the MOC), the downstream pipeline workflow, and six weeks of build history in `System - Build Log.md`. Found a live, currently-active, previously-undocumented bug that outranks everything else. Wrote it up as a proper postmortem note in the vault and logged it in the Build Log. Here's the full picture.

## The headline finding: the write gate has no failure memory

A candidate that fails at the write gate (`vault_writer/validate.py` — dead URL, cross-source duplicate, cached OPT exclusion, degree exclusion) is **never recorded anywhere**. Only a confirmed push adds a uid to `seen_ids.json`. Only the debate comparator's *deferred* list (candidates cut by the per-run budget) feeds the 48-loss exclusion counter. A candidate that gets *selected* into the write budget and then rejected by the gate falls into neither bucket. If it keeps winning its bucket's ranking, it gets re-offered and re-selected every single hour, forever, with nothing to ever stop it.

This isn't theoretical. `SimplifyJobs:[REDACTED]` (a 403 dead link) appears identically in the rejection list of every run I sampled across four straight days, permanently squatting one of the ~10 write-budget slots every hour.

**The evidence, from `logs/runs.jsonl` directly:**
- 2026-08-22 15:11 → 2026-08-25 17:23 (72 hourly runs): `written_count` was 0 in **68 of 72** runs, despite matching 10-51 new eligible candidates every single hour. In every one of those 68 runs, the number of rejections exactly equaled the size of the selected write budget — not partial failure, total failure.
- 2026-08-26 05:24 → 14:35 (the 10 most recent runs): `written_count` was 0 in **all 10**, while `new_count` jumped to 219-233/run — ApplyGuy just went live as a source and is contributing 168 matches/run on its first exposure.
- The vault's own git log shows the stall isn't a hard freeze — a burst of 11 real writes landed in the gap between those two windows. It's bursty: the doomed-candidate queue occasionally clears, a few real dossiers get through, then it refills with new persistent losers and stalls again. As of the last 10 straight hours, it's stalled again.

**The compounding, time-bound risk — this is the part to act on first, not the whole postmortem:**

`state/debate_losses.json` right now has 233 entries, of which **156 sit at exactly 20 losses** out of the 48 that trigger permanent exclusion — nearly all real ApplyGuy candidates. `excluded_uids.json` is still 388, unchanged across every check this session, so none have crossed yet. At roughly 1 loss/hour, that cluster reaches 48 in **roughly 24-30 hours from 2026-08-26 14:35 UTC** — sometime around tomorrow midday-to-evening. The two bugs compound: the write budget is permanently squatted by candidates that can never be written, so the real new ApplyGuy candidates never get an actual turn at the gate — they only ever land in "deferred," silently climbing toward exclusion for a reason that has nothing to do with their quality. Left alone, a large batch of real, never-actually-evaluated postings gets swept into `Excluded — Losing The Debate.md` within about a day.

I did **not** fix any of this — you asked for postmortem and adversaries first, and this is a public repo with a live hourly cron, so a code change deserves your explicit go-ahead, not a unilateral push. But given the clock, I'd treat "raise `MAX_DEBATE_LOSSES` again as a stopgap" as a decision worth making today, not after a full root-cause fix.

## What's genuinely fixed since the last review (so I'm not just reporting new problems)
- The `notes:`/`company/<slug>` tag write-time gap the 2026-08-23 weekly review found at 11/392 and 69/392 — fixed. Verified directly against today's freshest dossier.
- Location denylist gaps (Netherlands/Hong Kong/Poland/Israel/bare "London"), adjacent-field company hints, the Zipline SPA extraction bug, Workday/Oracle job-id dedup — all live in code with real citations.
- `revalidate.py` exists and runs on its own schedule — the retroactive re-sweep the 2026-08-23 audit asked for.
- The Virtu "Quantitative Trading Intern" gate-conformance miss that same review flagged is **still live in the vault**, unaddressed 3 days later — a real carryover.

## Secondary findings from the same pass
1. **Schema-drift coverage covers less than half the sources.** Only SimplifyJobs/JGCL/vanshb03/zshah101/ApplyGuy get a pre-flight check. Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock (6 of 11 sources) degrade silently to zero on a schema change, no halt, no issue. Ashby is at 0 matches in every run I sampled — I don't know if that's real or drift, and neither does the current system.
2. **`Source of Truth.md` and `System - Build Log.md` are stale relative to already-shipped code**, not just runtime state. Both describe Phase 4's fixes and the Lever/InternDock/ApplyGuy launches as "queued, not yet run" — they're live. Anyone deciding what to build next by reading those notes instead of the live repo is working from a false picture. I flagged this in both notes' `next` fields rather than silently rewriting them.
3. **The classification incidental-keyword bug is now a confirmed pattern, not an edge case.** Today's freshest dossier (Prophet Security, a security company) classified AI/ML on an incidental "machine learning" mention for a plain backend role — the same bug class as Databricks (2026-07-26), Mosaic (2026-07-26), and AbbVie (flagged as one data point on 2026-08-23). Four independent instances now.

## Adversaries — what's actually working against this system

**1. The write-starvation bug above** — the most acute, time-bound threat right now.

**2. Every new source launch is a starvation multiplier, not just a slow ramp-up.** ApplyGuy just proved this: one source going live added 168 matches/run against a fixed ~10/run budget. InternDock's confirmed drops run 257-720 postings each. Adding sources faster than the write-starvation bug is fixed makes the compounding risk above worse with every launch, not better.

**3. Stale documentation is systemic, not a one-off.** This has happened repeatedly in the Build Log's own history (Prompt 4 "confirmed still never run" three weeks after being written; Source of Truth's "queued for Prompt 10" framing now false). Anyone — you, me, a future session — who plans the next build off `Source of Truth.md` instead of the live repo will build against a fiction.

**4. The review system can't see the thing that just happened.** The one Weekly Discovery Review that's run (2026-08-23) explicitly had no `gh` auth and no repo clone — it sampled 12 dossiers already *in* the vault. A bug whose entire signature is "what never got written" is invisible to a method that only ever reads what did get written. This is a design gap in the Review Standard, not a one-time miss.

**5. Alert fatigue is already building.** 5+ open, permanent, informational capacity-notification GitHub issues, never closed. The exclusion-spike alert (fires above 20 exclusions/run) already fired repeatedly during the legitimate ApplyGuy onboarding surge — it can't distinguish a real problem from healthy new-source growth, and its own text says "review before treating this as a quality signal," but nothing in the current review cadence actually reads GitHub issues promptly. A real anomaly risks getting lost in noise the system generates about itself.

**6. Classification is whack-a-mole by design.** Every fix so far (Mosaic, Databricks, AbbVie-class patterns) has patched the *specific* keyword combination a real failure exposed. The underlying mechanism — "does any of these keywords appear anywhere in the fetched content" — will keep producing new incidental-match false positives indefinitely; there's no structural defense, only a growing denylist reacting to whatever broke last.

**7. The downstream funnel is the real bottleneck, and discovery is optimizing the wrong thing.** `Source of Truth.md` says it plainly: "the success metric is applications submitted per week, not dossiers written." Six weeks in: 319 dossiers, exactly 5 promotions ever (1 skill-assisted + 4 manual), 4 of those 5 missing their Contacts/Tracker notes, **zero** Applying notes, **zero** submitted applications. Every hour of engineering on discovery (debate comparators, priority buckets, ninth and tenth sources) makes the supply side more sophisticated while the demonstrated human-processing throughput sits at 5 promotions in 6 weeks. More sources without more promotion throughput just grows an already-unprocessed backlog faster.

**8. Public repo, unmonitored secrets, no expiry tracking.** Already flagged in the repo's own PRD as "the biggest silent-failure risk" — `JARVIS_PUSH_TOKEN` and `FIRECRAWL_API_KEY` expiry dates aren't checkable via any API, and GitHub Actions minutes usage can't be queried with the current token scope. Not new, but real and still true.

**9. Two independent writers on one branch, one retry.** The vault's own auto-commit cycle and this pipeline's hourly push both write to the same branch; `git_ops.py` handles this with rebase + retry-once. That's reasonable, but it's one retry — a genuine conflict (e.g., you hand-editing a dossier at the wrong moment) fails closed (nothing marked seen, retried next hour) rather than losing data, but it's a real single point of fragility worth knowing about.

**10. Cleanup debt never gets retroactively applied.** The ~53 pre-fix cross-source duplicates and the 49 Zipline/AIJobs shared-content dossiers found in the 2026-08-23 audit were never swept once the code fix landed — `revalidate.py` only catches *new* regressions going forward, nothing has gone back and cleaned the backlog those specific fixes were meant to address.

## Tightening the review system, concretely

The Weekly review's own design can't catch what just happened. Three specific process gaps, not code changes:
1. **Give the review real repo access before it runs**, every time, not "if reachable this session." It needs `logs/runs.jsonl` and `gh issue list` to do the one thing a vault-side dossier sample structurally cannot: detect zero-output runs.
2. **Add a mandatory Write-Throughput section** to the Weekly Discovery Review: sum of `written_count` vs `new_count` over the period, plus a check for the same uid appearing in `rejections` across more than N consecutive runs. That single check would have caught this four days ago instead of me finding it today.
3. **The review cadence is entirely manual and memory-triggered** — nothing reminds you it's due. The Reviews MOC says "run around 2026-08-30," but nothing enforces that. Worth a recurring `/loop` or scheduled nudge if you want this to actually happen on a cadence rather than whenever someone remembers.

## What I did in the vault
- New note: [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]] — the full evidence trail, numbers, and recommendations.
- Added a dated entry to `System - Build Log.md` and updated its `next` field to flag the urgent item and the documentation-staleness gap.

I didn't touch the pipeline's code or open any GitHub issue — say the word if you want me to (a) raise `MAX_DEBATE_LOSSES` as the stopgap, (b) build the write-gate failure-memory fix, or (c) go after the review-system changes first.

### Tool Calls

- `Bash` -- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis" && echo "=== Career-related dirs ===" && find . -ipath "*career*" -not -path "*/node_modules/*" -not -path "*/.git/*" -type d 2>/dev/null && echo "=== Internship-related files ===" && find . -iname "*internship*" -not -path "*/.git/*" 2>/dev/null && echo "=== dossier files ===" && find . -iname "*dossier*" -not -path "*/.git/*" 2>/dev/null`
```
=== Career-related dirs ===
./.claude/skills/obsidian-project-career
./10_Areas/Career
./10_Areas/Career/Certifications
./10_Areas/Career/Finance
./10_Areas/Career/Hackathon
./10_Areas/Career/Internships
./10_Areas/Career/Internships/Cheats
./10_Areas/Career/Internships/Contacts
./10_Areas/Career/Internships/Contacts/Each One
./10_Areas/Career/Internships/Contacts/Each One/Come Back
./10_Areas/Career/Internships/Contacts/Each One/Ended
./10_Areas/Career/Internships/Contacts/Each One/Ongoing
./10_Areas/Career/Internships/List
./10_Areas/Career/Internships/List/Dossiers
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance
./10_Areas/Career/Internships/List/Dossiers/Other
./10_Areas/Career/Internships/List/Dossiers/Viewed
./10_Areas/Career/Internships/Programs
./10_Areas/Career/Internships/Programs/Considering
./10_Areas/Career/Internships/Programs/Considering/Ended
./10_Areas/Career/Internships/Programs/Job & Company
./10_Areas/Career/Internships/Programs/Serious
./10_Areas/Career/Internships/Programs/Serious/Ended
./10_Areas/Career/Internships/Tracker
./10_Areas/Career/Internships/Tracker/Each One
./10_Areas/Career/Internships/Tracker/Each One/Applied
./10_Areas/Career/Internships/Tracker/Each One/Current
./10_Areas/Career/Internships/Tracker/Each One/Result
./10_Areas/Career/Mentors
./20_Progress/AI/Claude Code/Jarvis/.claude/skills/obsidian-project-career
./30_Order/Templates/Career
=== Internship-related files ===
./10_Areas/Career/Internships
./10_Areas/Career/Internships/Internships Hub.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Autonomous Driving – Internship in Machine Learning - Robert Bosch Venture Capital.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 AI Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Atlanta, GA - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- New York, NY - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 Software Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Charlotte, NC - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- New York, NY - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 AI Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Atlanta, GA - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- New York, NY - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 Software Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Charlotte, NC - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Technology - New York, NY - American Express.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/College to Corporate IT Internship - Data Science (NC) - Vanguard.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/College to Corporate IT Internship - Data Science (PA) - Vanguard.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantic - PhD Quantitative Researcher Intern (Summer 2027) - Walleye Capital Internships.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantic – Quantitative Developer Intern (Summer 2027) - Walleye Capital Internships.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantitative Research, Markets, Summer Internship - Analyst - JPMorgan Chase.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineering Internship - Deepgram.md
./10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineering- Internship (Fall 2026-Summer 2027) - Deepgram.md
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/2027 North America Software Engineering Internship - The Trade Desk.md
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/2027 Software Engineering Internship - Uber.md
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Enterprise Operations Software Internship - Hewlett Packard (HP).md
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Development Internship - SimonComputing.md
./10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Summer 2027 Software Engineering Internship - Western Digital.md
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Quant Research (Undergrad) - Virtu Financial.md
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship- FPGA - Virtu Financial.md
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend Developer Internship - Virtu Financial.md
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Research Analyst Internship - Stevens Capital Management.md
./10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Technology Intern - New York - 2027 - Marshall Wace Internship Programmes.md
./10_Areas/Career/Internships/List/Dossiers/Other/College to Corporate IT Internship - Data Analyst (NC) - Vanguard.md
./10_Areas/Career/Internships/List/Dossiers/Other/IT Infrastructure Internship - Summer 2027 - Conagra Brands.md
./10_Areas/Career/Internships/List/Dossiers/Other/Software Development Internship - Summer 2027 - Conagra Brands.md
./10_Areas/Career/Internships/List/Dossiers/Other/Software Engineer Internship (2027 Start) - Optiver.md
./10_Areas/Career/Internships/List/Dossiers/Other/Summer 2027 Internship - Tech (Infrastructure) - ING.md
./10_Areas/Career/Internships/List/Dossiers/Viewed/Corporate Summer Internship - Technology, Software Engineering and Cyber - Hilton Worldwide.md
./10_Areas/Career/Internships/List/Dossiers/Viewed/Data Internship - Data & AI Program - JP Morgan Chase (2) (2) (2).md
./10_Areas/Career/Internships/List/Dossiers/Viewed/RenderATL - 2027 US Software Engineering Internship - Axon.md
./10_Areas/Career/Internships/Tracker/Internship - Dashboard.md
./20_Progress/Internship
./20_Progress/Internship/Building System/Internship Research Loop — Full Pipeline.excalidraw
./30_Order/Standards/Internship Loop Review Standard.md
./30_Order/Standards/Internship Notes Standard.md
./30_Order/Templates/Career/Internship Loop Monthly Review Template.md
./30_Order/Templates/Career/Internship Loop Weekly Review Template.md
./30_Order/Workflows/Internship - Design Rationale.md
./30_Order/Workflows/Internship Pipeline.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/07-16 Build comprehensive AI-powered internship application system.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/07-25 Define internship search profile and dossier rules.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/07-25 Design internship tracking and research loop system.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-23 Internship documentation standards and system hygiene.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-23 Internship loop review system.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-24 Internship resources and dossier coverage refresh.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/_archive-pre-fix/07-16 Claude Code - Let's do a very deep dive into our internship workflow..md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-16 Build 247 internship discovery automation system.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-19 Improve internship sourcing and company career page scraping.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-19 Independent audit of internship research loop.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-25 internship-pipeline-classification.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-25 Set up Claude Code tooling for internship research loop.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-25 Update internship filter for systems-minded AI engineer persona.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-30 Fix bugs in internship pipeline and implement dossier standards.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-03 Analyze internship application process and review recent additions.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-21 internship-research-loop git hygiene and CI health.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-21 Jarvis internship pipeline audit and setup.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship dossier audit and filter-rule reconciliation.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship sources audit and verification.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-25 Internship-research-loop handoff and verification.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-16 Build 247 internship discovery automation system.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-19 Improve internship sourcing and company career page scraping.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-19 Independent audit of internship research loop.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-25 internship-pipeline-classification.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-25 Set up Claude Code tooling for internship research loop.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-25 Update internship filter for systems-minded AI engineer persona.md
./60_Claude/05_Clippings/Web/fintech early programs that actually pay, not sm bs unpaid internship lmao.md
./60_Claude/05_Clippings/Web/Internships
./60_Claude/05_Clippings/Web/The 2027 Internship Calendar (Prediction) when everything actually drops.md
./60_Claude/05_Clippings/Web/the underclassmen internship list, before u age out.md
./60_Claude/10_Source_Summaries/Github Ingestion/Jobs Starred/summer2026-internships.md
./60_Claude/10_Source_Summaries/Github Ingestion/Jobs Starred/underclassmen-internships.md
./60_Claude/10_Source_Summaries/Web Ingestion/2027 Internship Calendar (web).md
./60_Claude/10_Source_Summaries/Web Ingestion/Underclassmen Internship List (web).md
./60_Claude/20_Distilled_Notes/Sources - Plan/Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline.md
./60_Claude/30_Reviews/Internship Loop
./60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC.md
./60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08.md
./60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34.md
./60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation.md
./60_Claude/40_Project_Briefs/Internship
./60_Claude/40_Project_Briefs/Internship/650+ Summer 2027 Internships Open Now (Apply Links).md
./60_Claude/40_Project_Briefs/Internship/Hardware is not auto-excluded — Jane Street's FPGAASIC internship is     a real.md
./60_Claude/40_Project_Briefs/Internship/Internship Research Loop — PRD.md
./60_Claude/40_Project_Briefs/Internship/internship-research-loop — Claude Code guidance.md
./60_Claude/40_Project_Briefs/Internship/internship-research-loop.md
./60_Claude/40_Project_Briefs/Internship/Real case, confirmed live 2026-08-24 '[REDACTED]'.md
./60_Claude/40_Project_Briefs/Internship/Real dossier Optiver 'FPGA Internship (2027 Start)' — Netherlands,     a _NON_U.md
./60_Claude/40_Project_Briefs/Internship/[REDACTED]().md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_650+ Summer 2027 Internships Open Now (Apply Links).md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_Internship Research Loop — PRD.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_internship-research-loop — Claude Code guidance.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_internship-research-loop.md
=== dossier files ===
./10_Areas/Career/Internships/List/Dossiers
./10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md
./10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md
./10_Areas/Career/Internships/List/Dossiers MOC.md
./10_Areas/Life/Plans/Zero-Cost AI Stack/Research Dossier — Internal LLM Inference at Near-Zero Cost.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/07-25 Define internship search profile and dossier rules.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-21 Promote-dossier note templates file recovery.md
./60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-24 Internship resources and dossier coverage refresh.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-30 Fix bugs in internship pipeline and implement dossier standards.md
./60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship dossier audit and filter-rule reconciliation.md
./60_Claude/40_Project_Briefs/Internship/150170 stay informational-only (logged via dossier_total, no issue);     19020.md
./60_Claude/40_Project_Briefs/Internship/3. Vault dossier counts vs. what run logs claim was written.md
./60_Claude/40_Project_Briefs/Internship/A dossier written before dossier_uids.json existed (or hand-edited into     the.md
./60_Claude/40_Project_Briefs/Internship/A source missing from feeds_by_source means its fetch failed — its     dossiers.md
./60_Claude/40_Project_Briefs/Internship/check_dossier().md
./60_Claude/40_Project_Briefs/Internship/count_dossiers_by_bucket().md
./60_Claude/40_Project_Briefs/Internship/dossier_filename().md
./60_Claude/40_Project_Briefs/Internship/Fix 2, Prompt 5 review (2026-07-30) two dossiers with the identical     filenam.md
./60_Claude/40_Project_Briefs/Internship/Frontmatter dicts of every dossier file actually present in the vault     checko.md
./60_Claude/40_Project_Briefs/Internship/Keys come from the dossier files actually in the checkout — a listing     whose.md
./60_Claude/40_Project_Briefs/Internship/load_dossier_uids().md
./60_Claude/40_Project_Briefs/Internship/Moves a closed-posting dossier into Viewed instead of deleting it     (Internsh.md
./60_Claude/40_Project_Briefs/Internship/move_dossier_to_viewed().md
./60_Claude/40_Project_Briefs/Internship/Not a Dossier (doesn't go through validate.validate()'s dossier-specific     fro.md
./60_Claude/40_Project_Briefs/Internship/Note-template contracts (for `promote-dossier` and any future vault-writing code).md
./60_Claude/40_Project_Briefs/Internship/promote-dossier note templates.md
./60_Claude/40_Project_Briefs/Internship/promote-dossier.md
./60_Claude/40_Project_Briefs/Internship/read_dossier().md
./60_Claude/40_Project_Briefs/Internship/Real bug, confirmed 2026-07-26 on both Google dossiers sourced via     Freehire.md
./60_Claude/40_Project_Briefs/Internship/Real dossier Optiver 'FPGA Internship (2027 Start)' — Netherlands,     a _NON_U.md
./60_Claude/40_Project_Briefs/Internship/Real dossier Optiver 'Software Engineer Intern' style content —     genuine tec.md
./60_Claude/40_Project_Briefs/Internship/Real dossier UHY 'Data Operations Intern' — Excel-only audit     support, no si.md
./60_Claude/40_Project_Briefs/Internship/Real dossier Vertiv 'Product Management Intern' — matches     stage1_reject's e.md
./60_Claude/40_Project_Briefs/Internship/Real fetched content, verbatim from three separate live Zipline     dossiers ('A.md
./60_Claude/40_Project_Briefs/Internship/Real listing.url shape stored on every AIJobs-sourced Zipline dossier     ('Aero.md
./60_Claude/40_Project_Briefs/Internship/Real profile.yaml entry 'D.E. Shaw' must match the real vault dossier     compan.md
./60_Claude/40_Project_Briefs/Internship/Real, reproducible bug found 2026-08-23 scan_dossiers() globs Viewed     along.md
./60_Claude/40_Project_Briefs/Internship/Renders the fixed dossier template and writes it into a vault checkout.  Renderi.md
./60_Claude/40_Project_Briefs/Internship/render_dossier().md
./60_Claude/40_Project_Briefs/Internship/revalidate.py — re-checks live dossiers against current core code using their o.md
./60_Claude/40_Project_Briefs/Internship/Same slugification as dossier_filename() lowercase, spaces to     hyphens, ille.md
./60_Claude/40_Project_Briefs/Internship/save_dossier_uids().md
./60_Claude/40_Project_Briefs/Internship/scan_dossiers().md
./60_Claude/40_Project_Briefs/Internship/test_already_removed_dossier_is_not_re_swept().md
./60_Claude/40_Project_Briefs/Internship/test_check_dossier_flags_real_non_us_location().md
./60_Claude/40_Project_Briefs/Internship/[REDACTED]().md
./60_Claude/40_Project_Briefs/Internship/[REDACTED]().md
./60_Claude/40_Project_Briefs/Internship/test_check_dossier_passes_real_genuine_posting().md
./60_Claude/40_Project_Briefs/Internship/test_count_dossiers_by_bucket_counts_real_files().md
./60_Claude/40_Project_Briefs/Internship/test_dossier_filename_collision_appends_number().md
./60_Claude/40_Project_Briefs/Internship/test_dossier_filename_collision_increments_past_multiple().md
./60_Claude/40_Project_Briefs/Internship/test_dossier_filename_sanitizes_illegal_chars().md
./60_Claude/40_Project_Briefs/Internship/test_dossier_with_no_manifest_entry_is_skipped_not_removed().md
./60_Claude/40_Project_Briefs/Internship/test_extract_posting_content_from_enriched_dossier().md
./60_Claude/40_Project_Briefs/Internship/test_extract_posting_content_from_thin_dossier().md
./60_Claude/40_Project_Briefs/Internship/test_failed_fetch_skips_that_sources_dossiers_entirely().md
./60_Claude/40_Project_Briefs/Internship/test_fetch_failure_fails_open_to_thin_dossier().md
./60_Claude/40_Project_Briefs/Internship/test_format_compliance_passes_on_rendered_dossier().md
./60_Claude/40_Project_Briefs/Internship/test_move_dossier_to_viewed_does_not_overwrite_filename_collision().md
./60_Claude/40_Project_Briefs/Internship/test_move_dossier_to_viewed_moves_file_and_updates_frontmatter().md
./60_Claude/40_Project_Briefs/Internship/test_move_dossier_to_viewed_updates_uid_manifest().md
./60_Claude/40_Project_Briefs/Internship/test_read_dossier_parses_frontmatter().md
./60_Claude/40_Project_Briefs/Internship/test_read_dossier_rejects_non_dossier().md
./60_Claude/40_Project_Briefs/Internship/test_render_dossier_frontmatter_contains_moc_link_and_company_tag().md
./60_Claude/40_Project_Briefs/Internship/test_render_dossier_shows_real_rendered_frontmatter_with_preference_match().md
./60_Claude/40_Project_Briefs/Internship/test_run_once_happy_path_marks_seen_and_writes_dossiers().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_creates_missing_dossiers_dir().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_different_uid_same_role_company_gets_collision_suffix().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_is_idempotent_on_uid().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_records_uid_manifest().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_routes_into_bucket_subfolder().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_without_state_dir_records_no_manifest().md
./60_Claude/40_Project_Briefs/Internship/test_write_dossier_writes_expected_file().md
./60_Claude/40_Project_Briefs/Internship/The critical ordering guarantee a validated, written dossier whose     push fai.md
./60_Claude/40_Project_Briefs/Internship/The dossier's own already-fetched content (verbatim, as originally     written).md
./60_Claude/40_Project_Briefs/Internship/The first rule this dossier would now fail under current code, or     None if it.md
./60_Claude/40_Project_Briefs/Internship/Two dossiers for the same company (varying casingwhitespace) must     produce t.md
./60_Claude/40_Project_Briefs/Internship/vault_root with no pre-existing Dossiers folder at all still works..md
./60_Claude/40_Project_Briefs/Internship/Writes an already-rendered, already-validated dossier into its     priority-buck.md
./60_Claude/40_Project_Briefs/Internship/write_dossier().md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_promote-dossier note templates.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_promote-dossier.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_render_dossier.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix.md
./60_Claude/40_Project_Briefs/Internship/_COMMUNITY_write_dossier.md
./60_Claude/40_Project_Briefs/Internship/{path, company, title, reason} for every live dossier that would     now fail.md
./60_Claude/40_Project_Briefs/Internship/{uid, path, reason} for dossiers whose posting closed. A source that     faile.md
```
- `Bash` -- `echo "=== search common locations for internship-research-loop repo ===" 
for p in "$HOME" "/c/Users/Anant Gupta" "/d/Users/_Anant" "/d/Users/_Anant/10_Areas/Documents" "/d" "/c"; do
  echo "--- $p ---"
  find "$p" -maxdepth 4 -iname "internship-research-loop*" -not -path "*Jarvis/60_Claude*" 2>/dev/null
done`
```
Exit code 1
=== search common locations for internship-research-loop repo ===
--- /c/Users/Anant Gupta ---
--- /c/Users/Anant Gupta ---
--- /d/Users/_Anant ---
--- /d/Users/_Anant/10_Areas/Documents ---
--- /d ---
--- /c ---
```
- `Bash` -- `ls "/c/Users/Anant Gupta" 2>/dev/null; echo "---wsl check---"; ls "//wsl$" 2>/dev/null; ls "/mnt/c" 2>/dev/null | head; wsl.exe -l -v 2>/dev/null`
```
0K7YY.exe
AppData
Application Data
battery-report.html
bin
Claude
Cookies
Documents
Downloads
echo
Favorites
fix-workspace-after-download.ps1
global.yml
i-need-a-deep-dreamy-bumblebee.md
install-claude-correctly.md
Local Settings
miniconda3
mongosh-2.5.9-win32-x64
mongosh-2.5.9-x64.msi
My Documents
nc6a9.exe
NetHood
new-laptop-setup.md
NTUSER.DAT
ntuser.dat.LOG1
ntuser.dat.LOG2
NTUSER.DAT{[REDACTED]}.TM.blf
NTUSER.DAT{[REDACTED]}.[REDACTED].regtrans-ms
NTUSER.DAT{[REDACTED]}.[REDACTED].regtrans-ms
ntuser.ini
OneDrive
Postman
PrintHood
Recent
Saved Games
scikit_learn_data
Searches
SendTo
settings.json
Start Menu
Templates
vscode-remote-wsl
WPS Cloud Files
---wsl check---
docker-desktop
Ubuntu
    N A M E                             S T A T E                       V E R S I O N  
 *   U b u n t u                         R u n n i n g                   2  
     d o c k e r - d e s k t o p         R u n n i n g                   2  
 
```
- `Bash` -- `find "//wsl\$/Ubuntu/home" -maxdepth 5 -iname "*internship*" 2>/dev/null
echo "---try root---"
find "//wsl\$/Ubuntu/root" -maxdepth 5 -iname "*internship*" 2>/dev/null`
```
//wsl$/Ubuntu/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-work-internship-research-loop
//wsl$/Ubuntu/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop
//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop
//wsl$/Ubuntu/home/anant_gupta/.cache/claude-cli-nodejs/-home-anant-gupta-projects-work-internship-research-loop
---try root---
```
- `Bash` -- `REPO="//wsl\$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop"
echo "=== top level ==="
ls -la "$REPO"
echo "=== git log (last 40) ==="
git -C "$REPO" log --oneline -40 2>/dev/null
echo "=== git status ==="
git -C "$REPO" status 2>/dev/null`
```
Exit code 128
=== top level ===
total 112
drwxr-xr-x 17 Anant Gupta 197121     0 Aug 25 22:05 .
drwxr-xr-x  4 Anant Gupta 197121     0 Jul 16 20:52 ..
drwxr-xr-x  4 Anant Gupta 197121     0 Aug 23 16:19 .claude
-rw-r--r--  1 Anant Gupta 197121    25 Aug 25 22:04 .claudeignore
drwxr-xr-x 10 Anant Gupta 197121     0 Aug 25 22:06 .git
-rw-r--r--  1 Anant Gupta 197121    39 Aug 25 22:04 .gitattributes
drwxr-xr-x  3 Anant Gupta 197121     0 Jul 16 23:46 .github
-rw-r--r--  1 Anant Gupta 197121   468 Jul 17 15:24 .gitignore
drwxr-xr-x  3 Anant Gupta 197121     0 Jul 17 15:31 .pytest_cache
drwxr-xr-x  5 Anant Gupta 197121     0 Jul 16 21:52 .venv
drwxr-xr-x  2 Anant Gupta 197121     0 Aug 25 22:03 __pycache__
-rw-r--r--  1 Anant Gupta 197121 10535 Aug 25 22:05 CLAUDE.md
drwxr-xr-x  3 Anant Gupta 197121     0 Aug 25 22:03 core
-rwxr-xr-x  1 Anant Gupta 197121  8464 Jul 26 11:32 enrich.py
-rwxr-xr-x  1 Anant Gupta 197121  3390 Jul 18 10:55 grade_resume.py
drwxr-xr-x  8 Anant Gupta 197121     0 Aug 25 22:03 graphify-out
drwxr-xr-x  3 Anant Gupta 197121     0 Aug 25 22:03 ingestion
drwxr-xr-x  2 Anant Gupta 197121     0 Jul 17 15:24 jarvis-checkout
drwxr-xr-x  2 Anant Gupta 197121     0 Aug 25 22:03 logs
-rw-r--r--  1 Anant Gupta 197121 11679 Aug 22 14:06 PRD.md
-rw-r--r--  1 Anant Gupta 197121  1515 Aug 22 13:56 README.md
-rwxr-xr-x  1 Anant Gupta 197121  7944 Aug 25 22:03 recheck.py
-rw-r--r--  1 Anant Gupta 197121    59 Jul 17 10:51 requirements.txt
-rwxr-xr-x  1 Anant Gupta 197121  4580 Aug 25 22:03 revalidate.py
-rw-r--r--  1 Anant Gupta 197121 34747 Aug 25 22:03 run_pipeline.py
drwxr-xr-x  3 Anant Gupta 197121     0 Aug 22 13:55 scripts
drwxr-xr-x  2 Anant Gupta 197121     0 Aug 25 22:03 state
drwxr-xr-x  4 Anant Gupta 197121     0 Aug 25 22:03 tests
drwxr-xr-x  4 Anant Gupta 197121     0 Aug 21 21:42 vault_writer
=== git log (last 40) ===
=== git status ===
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc 'cd ~/projects/work/internship-research-loop && git log --oneline -50 && echo "===STATUS===" && git status && echo "===STRUCTURE===" && find . -maxdepth 3 -not -path "./.git*" -not -path "./.venv*" -not -path "*__pycache__*" -not -path "./.pytest_cache*" | sort'`
```
cbbb2a1 Wire InternDock into SOURCES (Task 1) + add ApplyGuy as a source (Task 2)
dc135e3 Add InternDock drop-detection primitives (Task 3): sitemap index + posting parser
8a132a2 Add Lever as a source (Task 5): fetch_lever/normalize_lever, second real company beyond Palantir
93972d0 identity.py: add Oracle Cloud HCM job-id pattern for cross-source dedup
6d54628 run_pipeline.py: raise MAX_DEBATE_LOSSES from 5 to 48
b5a2a5f _prioritize_and_cap: reserve one additive preferred-company slot per bucket
fd7b22e run_pipeline.py: alert when debate-loss exclusions spike in one run
b0f9000 Add periodic dossier revalidation against current core/ rules
2b47d55 identity.py: add Workday requisition-id ATS pattern for cross-source dedup
aa99f46 relevance.py: tighten space/defense false positives, extend adjacent-field hints to non-technical business/finance/BI companies
fd1d662 filter.py: close _NON_US denylist gaps (Netherlands, Hong Kong, Poland, Israel, bare "London")
561ac14 recheck.py: stop re-sweeping already-removed dossiers in Viewed/
7988058 Fix Zipline SPA board-index content-extraction bug
dd0c888 Update state + logs — 2026-08-25
66e144a Update state + logs — 2026-08-25
93699ff Update state + logs — 2026-08-25
25beaa6 Update state + logs — 2026-08-25
5495075 Update state + logs — 2026-08-25
eb00de4 Update state + logs — 2026-08-25
422e7be Update state + logs — 2026-08-25
126cf1d Update state + logs — 2026-08-25
64e5348 Update state + logs — 2026-08-25
c57e49a Update state + logs — 2026-08-25
f382e24 Update state + logs — 2026-08-25
0fefbfa Recheck log — 2026-08-25
783cb9a Update state + logs — 2026-08-25
f271032 Update state + logs — 2026-08-25
57f8131 Update state + logs — 2026-08-25
1c3f737 Update state + logs — 2026-08-25
33a33f1 Update state + logs — 2026-08-25
e16d62c Update state + logs — 2026-08-25
1c00aff Update state + logs — 2026-08-24
a82ffd5 Update state + logs — 2026-08-24
9bcb1f5 Update state + logs — 2026-08-24
9629942 Update state + logs — 2026-08-24
430d904 Update state + logs — 2026-08-24
b84a1ce Update state + logs — 2026-08-24
132798c Update state + logs — 2026-08-24
ce95f45 Update state + logs — 2026-08-24
07a2bc5 Update state + logs — 2026-08-24
3df66c0 Update state + logs — 2026-08-24
c299344 Update state + logs — 2026-08-24
50d604e Update state + logs — 2026-08-24
ac04b1b Update state + logs — 2026-08-24
7cc417a Update state + logs — 2026-08-24
0c3975f Update state + logs — 2026-08-24
515fb3e Update state + logs — 2026-08-24
63e7f4d Update state + logs — 2026-08-24
643a959 Recheck log — 2026-08-24
bcc1a37 Update state + logs — 2026-08-24
===STATUS===
On branch master
Your branch is behind 'origin/master' by 21 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CLAUDE.md
	modified:   graphify-out/.graphify_labels.json
	modified:   graphify-out/GRAPH_REPORT.md
	modified:   graphify-out/graph.html
	modified:   graphify-out/graph.json
	modified:   graphify-out/manifest.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claudeignore
	.gitattributes

no changes added to commit (use "git add" and/or "git commit -a")
===STRUCTURE===
.
./.claude
./.claude/agents
./.claude/agents/contact-researcher.md
./.claude/agents/loop-verifier.md
./.claude/scheduled_tasks.lock
./.claude/settings.json
./.claude/settings.local.json
./.claude/skills
./.claude/skills/promote-dossier
./.claude/skills/review-loop-change
./.claudeignore
./CLAUDE.md
./PRD.md
./README.md
./core
./core/classify.py
./core/debate.py
./core/filter.py
./core/git_ops.py
./core/identity.py
./core/profile.yaml
./core/relevance.py
./core/run_log.py
./core/schema_drift.py
./enrich.py
./grade_resume.py
./graphify-out
./graphify-out/.gitignore
./graphify-out/.graphify_labels.json
./graphify-out/.graphify_root
./graphify-out/2026-08-21
./graphify-out/2026-08-21/.graphify_labels.json
./graphify-out/2026-08-21/GRAPH_REPORT.md
./graphify-out/2026-08-21/graph.json
./graphify-out/2026-08-21/manifest.json
./graphify-out/2026-08-22
./graphify-out/2026-08-22/.graphify_labels.json
./graphify-out/2026-08-22/GRAPH_REPORT.md
./graphify-out/2026-08-22/graph.json
./graphify-out/2026-08-22/manifest.json
./graphify-out/2026-08-23
./graphify-out/2026-08-23/.graphify_labels.json
./graphify-out/2026-08-23/GRAPH_REPORT.md
./graphify-out/2026-08-23/graph.json
./graphify-out/2026-08-23/manifest.json
./graphify-out/2026-08-24
./graphify-out/2026-08-24/.graphify_labels.json
./graphify-out/2026-08-24/GRAPH_REPORT.md
./graphify-out/2026-08-24/graph.json
./graphify-out/2026-08-24/manifest.json
./graphify-out/2026-08-25
./graphify-out/2026-08-25/.graphify_labels.json
./graphify-out/2026-08-25/GRAPH_REPORT.md
./graphify-out/2026-08-25/graph.json
./graphify-out/2026-08-25/manifest.json
./graphify-out/GRAPH_REPORT.md
./graphify-out/cache
./graphify-out/cache/ast
./graphify-out/cache/stat-index.json
./graphify-out/graph.html
./graphify-out/graph.json
./graphify-out/manifest.json
./ingestion
./ingestion/freehire.py
./ingestion/interndock.py
./ingestion/normalize.py
./ingestion/posting_page.py
./ingestion/sources.py
./jarvis-checkout
./logs
./logs/rechecks.jsonl
./logs/runs.jsonl
./recheck.py
./requirements.txt
./revalidate.py
./run_pipeline.py
./scripts
./scripts/hooks
./scripts/hooks/pre-push
./state
./state/capacity_notified.json
./state/debate_losses.json
./state/dossier_uids.json
./state/excluded_uids.json
./state/opt_cache.json
./state/seen_ids.json
./tests
./tests/fixtures
./tests/fixtures/applyguy.json
./tests/fixtures/freehire.json
./tests/fixtures/interndock_drop.md
./tests/fixtures/josegael.json
./tests/fixtures/posting_ashby_ctgt.md
./tests/fixtures/posting_fiverings.md
./tests/fixtures/posting_google_careers.md
./tests/fixtures/posting_zipline_open_roles.md
./tests/fixtures/simplifyjobs.json
./tests/fixtures/throwaway_vault
./tests/fixtures/vanshb03.json
./tests/fixtures/zshah101.json
./tests/test_classify.py
./tests/test_debate.py
./tests/test_debate_losses.py
./tests/test_enrich.py
./tests/test_filter.py
./tests/test_freehire.py
./tests/test_git_ops.py
./tests/test_grade_resume.py
./tests/test_identity.py
./tests/test_interndock.py
./tests/test_posting_page.py
./tests/test_recheck.py
./tests/test_relevance.py
./tests/test_revalidate.py
./tests/test_run_log.py
./tests/test_run_pipeline.py
./tests/test_schema_drift.py
./tests/test_sources.py
./tests/test_validate.py
./tests/test_writer.py
./vault_writer
./vault_writer/templates
./vault_writer/templates/dossier.md.j2
./vault_writer/validate.py
./vault_writer/writer.py
```
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/PRD.md`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/CLAUDE.md`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/sources.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/filter.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/classify.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/debate.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/freehire.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/interndock.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/revalidate.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== state file sizes/counts ==="
for f in state/*.json; do echo "--$f--"; python3 -c "import json,sys; d=json.load(open(\"$f\")); print(type(d), len(d))" 2>/dev/null || wc -c "$f"; done
echo "=== logs/runs.jsonl last 5 lines ==="
tail -n 5 logs/runs.jsonl
echo "=== logs/rechecks.jsonl last 5 lines ==="
tail -n 5 logs/rechecks.jsonl
echo "=== workflows ==="
ls .github/workflows
echo "=== README ==="
cat README.md
'
`
```
wc: invalid zero-length file name
wc: inva----
----
----
----
=== logs/runs.jsonl last 5 lines ===
{"timestamp": "2026-08-25T13:40:53.094215+00:00", "fetch_counts": {"SimplifyJobs": 14715, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 471, "zshah101": 543, "Greenhouse": 56, "Ashby": 4, "Freehire": 7, "AIJobs": 244}, "filter_match_counts": {"SimplifyJobs": 169, "Jose-Gael-Cruz-Lopez": 3, "vanshb03": 87, "zshah101": 57, "Greenhouse": 30, "Ashby": 0, "Freehire": 2, "AIJobs": 48}, "new_count": 16, "already_seen_count": 380, "deferred_count": 6, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "zshah101:greenhouse:advancedspace:4324875009", "check": "opt_eligibility", "reason": "export controlled information. Under U.S. law, this requires that you be a \u2018U.S. Person (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|ai engineer intern enterprise technology services"}, {"uid": "zshah101:greenhouse:advancedspace:4333179009", "check": "opt_eligibility", "reason": "must be a U.S. person (cached 2026-08-24)"}, {"uid": "zshah101:greenhouse:sage49:6131185004", "check": "cross_source_duplicate", "reason": "company+title already in vault: jobid:6131185004"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "Must be a US Citizen (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|cybersecurity intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "export-controlled items. Because our employees are provided access to export-controlled items, our policy is to only hire \u201cU.S. person (cached 2026-08-07)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null, "bucket_at_capacity": ["AI/ML", "Other"], "dossier_total": 311, "newly_excluded_count": 2}
{"timestamp": "2026-08-25T14:37:09.905579+00:00", "fetch_counts": {"SimplifyJobs": 14717, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 471, "zshah101": 543, "Greenhouse": 56, "Ashby": 4, "Freehire": 7, "AIJobs": 244}, "filter_match_counts": {"SimplifyJobs": 167, "Jose-Gael-Cruz-Lopez": 3, "vanshb03": 87, "zshah101": 57, "Greenhouse": 30, "Ashby": 0, "Freehire": 2, "AIJobs": 48}, "new_count": 14, "already_seen_count": 380, "deferred_count": 4, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "zshah101:greenhouse:advancedspace:4324875009", "check": "opt_eligibility", "reason": "export controlled information. Under U.S. law, this requires that you be a \u2018U.S. Person (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|ai engineer intern enterprise technology services"}, {"uid": "zshah101:greenhouse:advancedspace:4333179009", "check": "opt_eligibility", "reason": "must be a U.S. person (cached 2026-08-24)"}, {"uid": "zshah101:greenhouse:sage49:6131185004", "check": "cross_source_duplicate", "reason": "company+title already in vault: jobid:6131185004"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "Must be a US Citizen (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|cybersecurity intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "export-controlled items. Because our employees are provided access to export-controlled items, our policy is to only hire \u201cU.S. person (cached 2026-08-07)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null, "bucket_at_capacity": ["AI/ML", "Other"], "dossier_total": 311, "newly_excluded_count": 2}
{"timestamp": "2026-08-25T15:33:22.836048+00:00", "fetch_counts": {"SimplifyJobs": 14719, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 471, "zshah101": 546, "Greenhouse": 56, "Ashby": 4, "Freehire": 7, "AIJobs": 244}, "filter_match_counts": {"SimplifyJobs": 168, "Jose-Gael-Cruz-Lopez": 3, "vanshb03": 87, "zshah101": 56, "Greenhouse": 30, "Ashby": 0, "Freehire": 2, "AIJobs": 48}, "new_count": 14, "already_seen_count": 380, "deferred_count": 4, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "zshah101:greenhouse:advancedspace:4324875009", "check": "opt_eligibility", "reason": "export controlled information. Under U.S. law, this requires that you be a \u2018U.S. Person (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|ai engineer intern enterprise technology services"}, {"uid": "zshah101:greenhouse:advancedspace:4333179009", "check": "opt_eligibility", "reason": "must be a U.S. person (cached 2026-08-24)"}, {"uid": "zshah101:greenhouse:sage49:6131185004", "check": "cross_source_duplicate", "reason": "company+title already in vault: jobid:6131185004"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "Must be a US Citizen (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|cybersecurity intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "export-controlled items. Because our employees are provided access to export-controlled items, our policy is to only hire \u201cU.S. person (cached 2026-08-07)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null, "bucket_at_capacity": ["AI/ML", "Other"], "dossier_total": 311, "newly_excluded_count": 2}
{"timestamp": "2026-08-25T16:24:46.813259+00:00", "fetch_counts": {"SimplifyJobs": 14720, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 471, "zshah101": 546, "Greenhouse": 56, "Ashby": 4, "Freehire": 7, "AIJobs": 244}, "filter_match_counts": {"SimplifyJobs": 165, "Jose-Gael-Cruz-Lopez": 3, "vanshb03": 87, "zshah101": 56, "Greenhouse": 30, "Ashby": 0, "Freehire": 2, "AIJobs": 48}, "new_count": 12, "already_seen_count": 379, "deferred_count": 2, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "zshah101:greenhouse:advancedspace:4324875009", "check": "opt_eligibility", "reason": "export controlled information. Under U.S. law, this requires that you be a \u2018U.S. Person (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|ai engineer intern enterprise technology services"}, {"uid": "zshah101:greenhouse:advancedspace:4333179009", "check": "opt_eligibility", "reason": "must be a U.S. person (cached 2026-08-24)"}, {"uid": "zshah101:greenhouse:sage49:6131185004", "check": "cross_source_duplicate", "reason": "company+title already in vault: jobid:6131185004"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "Must be a US Citizen (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|cybersecurity intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "export-controlled items. Because our employees are provided access to export-controlled items, our policy is to only hire \u201cU.S. person (cached 2026-08-07)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null, "bucket_at_capacity": ["AI/ML", "Other"], "dossier_total": 311, "newly_excluded_count": 0}
{"timestamp": "2026-08-25T17:23:08.398585+00:00", "fetch_counts": {"SimplifyJobs": 14725, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 471, "zshah101": 546, "Greenhouse": 56, "Ashby": 4, "Freehire": 7, "AIJobs": 244}, "filter_match_counts": {"SimplifyJobs": 165, "Jose-Gael-Cruz-Lopez": 3, "vanshb03": 87, "zshah101": 55, "Greenhouse": 30, "Ashby": 0, "Freehire": 2, "AIJobs": 48}, "new_count": 13, "already_seen_count": 377, "deferred_count": 3, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "zshah101:greenhouse:advancedspace:4324875009", "check": "opt_eligibility", "reason": "export controlled information. Under U.S. law, this requires that you be a \u2018U.S. Person (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|ai engineer intern enterprise technology services"}, {"uid": "zshah101:greenhouse:advancedspace:4333179009", "check": "opt_eligibility", "reason": "must be a U.S. person (cached 2026-08-24)"}, {"uid": "zshah101:greenhouse:sage49:6131185004", "check": "cross_source_duplicate", "reason": "company+title already in vault: jobid:6131185004"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "Must be a US Citizen (cached 2026-08-24)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: american express|cybersecurity intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "export-controlled items. Because our employees are provided access to export-controlled items, our policy is to only hire \u201cU.S. person (cached 2026-08-07)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null, "bucket_at_capacity": ["AI/ML", "Other"], "dossier_total": 311, "newly_excluded_count": 0}
=== logs/rechecks.jsonl last 5 lines ===
{"timestamp": "2026-08-21T07:25:22.016769+00:00", "type": "recheck", "scanned": 359, "removals": [{"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "AIJobs:[REDACTED]", "reason": "absent from live feed"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-08-22T07:10:29.669697+00:00", "type": "recheck", "scanned": 395, "removals": [{"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-08-23T07:11:43.733917+00:00", "type": "recheck", "scanned": 395, "removals": [{"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-08-24T07:39:48.916088+00:00", "type": "recheck", "scanned": 316, "removals": [{"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-08-25T07:26:40.869933+00:00", "type": "recheck", "scanned": 320, "removals": [{"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "zshah101:workday:philips:/job/Plymouth-Minnesota-United-States/[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
=== workflows ===
recheck.yml
revalidate.yml
run.yml
test.yml
=== README ===
# internship-research-loop

24/7 internship discovery automation — polls SimplifyJobs and Jose-Gael-Cruz-Lopez,
filters against a profile, dedups (per-source uid + cross-source company+title), and
writes dossiers into an Obsidian vault through a validated template + five-check
write gate. A daily recheck (`recheck.yml`) removes dossiers whose postings close
upstream. (zapplyjobs was dropped as a source 2026-07-18 — its entries are program
landing pages, not deadline-bearing postings.)

Full spec lives in the Jarvis vault: `Internship/Building System/Research Loop —
Implementation Plan.md`.

## Status

Phases 1–3 are live. `.github/workflows/run.yml` runs hourly against the real
`gupta-builds/Jarvis` repo — schema-drift check, fetch, filter, dedup,
validate, write, push (retry-safe against the vault's own independent
auto-commit cycle), with `state/seen_ids.json` only updated after a confirmed
push. First live run (2026-07-17) wrote 137 real dossiers into
`10_Areas/Career/Internships/List/Dossiers/`; a follow-up run correctly
recognized all 137 as already-seen and wrote zero duplicates. Per the plan's
build order: watch the Run Log rollup for a full week before tightening the
cadence past hourly.

## Local dev

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests/ -v
```

One-time: `cp scripts/hooks/pre-push .git/hooks/pre-push` — this repo has no PR gate, so this local hook is what blocks a `git push` with a failing test suite.
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== count of runs and written_count distribution over last 72 entries ==="
tail -n 72 logs/runs.jsonl | python3 -c "
import json,sys
for line in sys.stdin:
    d=json.loads(line)
    print(d[\"timestamp\"], \"new=\",d[\"new_count\"], \"deferred=\",d[\"deferred_count\"], \"written=\",d[\"written_count\"], \"total=\",d[\"dossier_total\"], \"excl=\",d[\"newly_excluded_count\"], \"halted=\",d[\"halted\"])
"
'
`
```
=== count of runs and written_count distribution over last 72 entries ===
2026-08-22T15:11:14.591187+00:00 new= 17 deferred= 7 written= 0 total= 391 excl= 2 halted= False
2026-08-22T16:12:29.499624+00:00 new= 15 deferred= 5 written= 0 total= 391 excl= 0 halted= False
2026-08-22T17:11:52.600958+00:00 new= 15 deferred= 5 written= 0 total= 391 excl= 0 halted= False
2026-08-22T18:15:12.054052+00:00 new= 15 deferred= 5 written= 0 total= 391 excl= 0 halted= False
2026-08-22T19:15:48.238491+00:00 new= 15 deferred= 5 written= 0 total= 391 excl= 5 halted= False
2026-08-22T20:12:13.179694+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-22T21:12:14.423461+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-22T22:11:55.674954+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-22T23:11:21.529416+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T00:42:50.169831+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T02:18:56.668471+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T03:41:44.736312+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T04:27:29.228662+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T05:20:46.756365+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T06:23:52.021189+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T07:25:27.285477+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T08:18:14.758903+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T09:18:18.779519+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T10:13:35.443099+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T11:12:46.309286+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T12:19:30.115262+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T13:25:29.750472+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T14:13:53.093154+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T15:13:07.127854+00:00 new= 10 deferred= 0 written= 0 total= 391 excl= 0 halted= False
2026-08-23T16:13:31.036930+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T17:12:20.601770+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T18:15:08.285552+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T19:15:37.197390+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T20:11:43.654867+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T21:12:17.326083+00:00 new= 10 deferred= 0 written= 0 total= 349 excl= 0 halted= False
2026-08-23T22:11:58.067951+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-23T23:11:44.874952+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T00:41:54.968584+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T02:17:32.544550+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T03:44:51.692005+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T04:35:28.157708+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T05:29:53.261425+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T06:36:51.039457+00:00 new= 10 deferred= 0 written= 0 total= 312 excl= 0 halted= False
2026-08-24T07:50:07.552042+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T08:36:43.280884+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T09:36:48.723707+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T10:33:41.112356+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T11:18:15.900989+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T12:27:44.166243+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-24T13:42:10.840115+00:00 new= 18 deferred= 8 written= 0 total= 311 excl= 0 halted= False
2026-08-24T14:32:25.192275+00:00 new= 18 deferred= 8 written= 0 total= 311 excl= 0 halted= False
2026-08-24T15:29:56.591005+00:00 new= 46 deferred= 36 written= 0 total= 311 excl= 0 halted= False
2026-08-24T16:24:27.932752+00:00 new= 51 deferred= 41 written= 1 total= 312 excl= 0 halted= False
2026-08-24T17:23:06.062677+00:00 new= 51 deferred= 41 written= 0 total= 312 excl= 8 halted= False
2026-08-24T18:25:23.864500+00:00 new= 45 deferred= 35 written= 0 total= 312 excl= 0 halted= False
2026-08-24T19:22:06.431336+00:00 new= 46 deferred= 36 written= 0 total= 312 excl= 29 halted= False
2026-08-24T20:18:48.478629+00:00 new= 20 deferred= 10 written= 0 total= 312 excl= 3 halted= False
2026-08-24T21:19:31.440302+00:00 new= 40 deferred= 30 written= 2 total= 314 excl= 1 halted= False
2026-08-24T22:15:44.052576+00:00 new= 37 deferred= 27 written= 0 total= 314 excl= 2 halted= False
2026-08-24T23:14:07.775981+00:00 new= 41 deferred= 31 written= 0 total= 314 excl= 2 halted= False
2026-08-25T00:40:49.785098+00:00 new= 43 deferred= 33 written= 0 total= 314 excl= 4 halted= False
2026-08-25T02:12:42.206455+00:00 new= 39 deferred= 29 written= 0 total= 314 excl= 19 halted= False
2026-08-25T03:40:09.989230+00:00 new= 20 deferred= 10 written= 0 total= 314 excl= 0 halted= False
2026-08-25T04:29:42.814742+00:00 new= 20 deferred= 10 written= 0 total= 314 excl= 6 halted= False
2026-08-25T05:23:28.121592+00:00 new= 14 deferred= 4 written= 0 total= 314 excl= 4 halted= False
2026-08-25T06:28:24.942371+00:00 new= 11 deferred= 1 written= 1 total= 315 excl= 0 halted= False
2026-08-25T07:36:05.194038+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-25T08:30:26.534657+00:00 new= 10 deferred= 0 written= 0 total= 311 excl= 0 halted= False
2026-08-25T09:25:15.751538+00:00 new= 11 deferred= 1 written= 0 total= 311 excl= 0 halted= False
2026-08-25T10:21:54.107089+00:00 new= 14 deferred= 4 written= 0 total= 311 excl= 0 halted= False
2026-08-25T11:17:55.845677+00:00 new= 16 deferred= 6 written= 0 total= 311 excl= 0 halted= False
2026-08-25T12:28:06.609616+00:00 new= 16 deferred= 6 written= 0 total= 311 excl= 0 halted= False
2026-08-25T13:40:53.094215+00:00 new= 16 deferred= 6 written= 0 total= 311 excl= 2 halted= False
2026-08-25T14:37:09.905579+00:00 new= 14 deferred= 4 written= 0 total= 311 excl= 2 halted= False
2026-08-25T15:33:22.836048+00:00 new= 14 deferred= 4 written= 0 total= 311 excl= 2 halted= False
2026-08-25T16:24:46.813259+00:00 new= 12 deferred= 2 written= 0 total= 311 excl= 0 halted= False
2026-08-25T17:23:08.398585+00:00 new= 13 deferred= 3 written= 0 total= 311 excl= 0 halted= False
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
python3 -c "
import json
for f in [\"state/seen_ids.json\",\"state/dossier_uids.json\",\"state/excluded_uids.json\",\"state/debate_losses.json\",\"state/opt_cache.json\",\"state/capacity_notified.json\"]:
    d=json.load(open(f))
    print(f, type(d).__name__, len(d))
"
echo "=== opt_cache excluded count ==="
python3 -c "
import json
d=json.load(open(\"state/opt_cache.json\"))
excl=[k for k,v in d.items() if v.get(\"verdict\")==\"excluded\"]
print(\"total\",len(d),\"excluded\",len(excl))
print(excl[:10])
"
echo "=== debate_losses top values ==="
python3 -c "
import json
d=json.load(open(\"state/debate_losses.json\"))
print(\"count\",len(d))
top=sorted(d.items(), key=lambda x:-x[1])[:10]
print(top)
"
'
`
```
state/seen_ids.json list 610
state/dossier_uids.json dict 361
state/excluded_uids.json list 388
state/debate_losses.json dict 6
state/opt_cache.json dict 545
state/capacity_notified.json dict 2
=== opt_cache excluded count ===
total 545 excluded 76
['AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]', 'AIJobs:[REDACTED]']
=== debate_losses top values ===
count 6
[('SimplifyJobs:[REDACTED]', 3), ('vanshb03:[REDACTED]', 3), ('zshah101:ashby:voleon:[REDACTED]', 3), ('vanshb03:[REDACTED]', 2), ('SimplifyJobs:[REDACTED]', 1), ('SimplifyJobs:[REDACTED]', 1)]
```
- `Bash` -- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
echo "=== counts per bucket (actual vault, Windows checkout) ==="
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" "Viewed"; do
  n=$(find "$d" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)
  echo "$d : $n"
done
echo "=== total excluding Viewed ==="
find "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l
echo "=== git log for this Windows Jarvis checkout, last internship-related commits ==="
cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
git log --oneline -10 -- "10_Areas/Career/Internships/List/Dossiers" 2>/dev/null
echo "=== last commit touching this path, date ==="
git log -1 --format="%ci %s" -- "10_Areas/Career/Internships/List/Dossiers" 2>/dev/null`
```
=== counts per bucket (actual vault, Windows checkout) ===
1 - AI & ML : 141
2 - Fullstack : 43
3 - CyS & Finance : 51
Other : 84
Viewed : 15
=== total excluding Viewed ===
319
=== git log for this Windows Jarvis checkout, last internship-related commits ===
112c5a58 Move 4 closed posting(s) to Viewed/ — recheck 2026-08-26
8e4b3be0 Auto-discovered 1 internship(s) — 2026-08-26
be25551f Auto-discovered 1 internship(s) — 2026-08-26
896a5c78 Auto-discovered 1 internship(s) — 2026-08-25
95f0f977 Auto-discovered 2 internship(s) — 2026-08-25
6b6dcb09 Auto-discovered 7 internship(s) — 2026-08-25
9de40346 Move 9 closed posting(s) to Viewed/ — recheck 2026-08-25
58ae6b62 Auto-discovered 1 internship(s) — 2026-08-25
d6d27a49 Auto-discovered 2 internship(s) — 2026-08-24
25b5d8ab Auto-discovered 1 internship(s) — 2026-08-24
=== last commit touching this path, date ===
2026-08-26 07:28:02 +0000 Move 4 closed posting(s) to Viewed/ — recheck 2026-08-26
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
git fetch origin 2>&1 | tail -5
echo "=== commits between local HEAD and origin/master ==="
git log --oneline HEAD..origin/master
echo "=== files changed in those commits ==="
git diff --stat HEAD origin/master -- run_pipeline.py core/ ingestion/ vault_writer/ recheck.py revalidate.py
echo "=== latest runs.jsonl on origin/master (last 10) ==="
git show origin/master:logs/runs.jsonl | tail -10 | python3 -c "
import json,sys
for line in sys.stdin:
    d=json.loads(line)
    print(d[\"timestamp\"], \"new=\",d[\"new_count\"], \"deferred=\",d[\"deferred_count\"], \"written=\",d[\"written_count\"], \"total=\",d[\"dossier_total\"], \"excl=\",d[\"newly_excluded_count\"], \"halted=\",d[\"halted\"], d.get(\"halt_reason\"))
"
'
`
```
=== commits between local HEAD and origin/master ===
ec77221 Update state + logs — 2026-08-26
3a9fb09 Update state + logs — 2026-08-26
95d95e6 Update state + logs — 2026-08-26
9629979 Update state + logs — 2026-08-26
f91fd43 Update state + logs — 2026-08-26
3973ef8 Update state + logs — 2026-08-26
e5c9389 Update state + logs — 2026-08-26
d665a9e Update state + logs — 2026-08-26
496fbb6 Recheck log — 2026-08-26
01e93af Update state + logs — 2026-08-26
d41da21 Update state + logs — 2026-08-26
72c8d39 Update state + logs — 2026-08-26
ab78c53 Update state + logs — 2026-08-26
2d87dfa Update state + logs — 2026-08-26
4937aa9 Update state + logs — 2026-08-26
572490f Update state + logs — 2026-08-25
b20dc4d Update state + logs — 2026-08-25
7bab3f7 Update state + logs — 2026-08-25
a234200 Update state + logs — 2026-08-25
72495a0 Update state + logs — 2026-08-25
bd82f96 Update state + logs — 2026-08-25
=== files changed in those commits ===
=== latest runs.jsonl on origin/master (last 10) ===
2026-08-26T05:24:18.037085+00:00 new= 219 deferred= 208 written= 0 total= 323 excl= 0 halted= False None
2026-08-26T06:30:55.994592+00:00 new= 226 deferred= 215 written= 0 total= 323 excl= 0 halted= False None
2026-08-26T07:37:53.266482+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T08:31:35.613448+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T09:31:17.521762+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T10:24:59.748577+00:00 new= 227 deferred= 216 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T11:20:19.841110+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T12:31:07.540420+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T13:45:24.397829+00:00 new= 226 deferred= 215 written= 0 total= 319 excl= 0 halted= False None
2026-08-26T14:35:00.140290+00:00 new= 233 deferred= 222 written= 0 total= 319 excl= 0 halted= False None
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== full breakdown of latest run rejections (checks histogram) ==="
git show origin/master:logs/runs.jsonl | tail -1 | python3 -c "
import json,sys,collections
d=json.loads(sys.stdin.read())
print(\"timestamp\", d[\"timestamp\"])
print(\"fetch_counts\", d[\"fetch_counts\"])
print(\"filter_match_counts\", d[\"filter_match_counts\"])
print(\"new_count\", d[\"new_count\"], \"deferred\", d[\"deferred_count\"], \"written\", d[\"written_count\"])
c = collections.Counter(r[\"check\"] for r in d[\"rejections\"])
print(\"rejection check histogram:\", dict(c))
print(\"num rejections total:\", len(d[\"rejections\"]))
for r in d[\"rejections\"][:15]:
    print(\" -\", r[\"uid\"], r[\"check\"], r[\"reason\"][:100])
"
echo "=== interndock_seen_guides.json on origin/master ==="
git show origin/master:state/interndock_seen_guides.json 2>&1 | head -20
echo "=== how many InternDock-sourced entries appear in rejections/uid namespace ==="
git show origin/master:logs/runs.jsonl | tail -1 | python3 -c "
import json,sys
d=json.loads(sys.stdin.read())
print(\"InternDock fetch/match in this record present?\", \"InternDock\" in d[\"fetch_counts\"], d[\"fetch_counts\"].get(\"InternDock\"), d[\"filter_match_counts\"].get(\"InternDock\"))
"
'
`
```
=== full breakdown of latest run rejections (checks histogram) ===
timestamp 2026-08-26T14:35:00.140290+00:00
fetch_counts {'SimplifyJobs': 14777, 'Jose-Gael-Cruz-Lopez': 112, 'vanshb03': 471, 'zshah101': 575, 'ApplyGuy': 248, 'Greenhouse': 58, 'Ashby': 4, 'Lever': 61, 'Freehire': 7, 'AIJobs': 252, 'InternDock': 0}
filter_match_counts {'SimplifyJobs': 198, 'Jose-Gael-Cruz-Lopez': 3, 'vanshb03': 87, 'zshah101': 69, 'ApplyGuy': 168, 'Greenhouse': 24, 'Ashby': 0, 'Lever': 3, 'Freehire': 0, 'AIJobs': 55, 'InternDock': 0}
new_count 233 deferred 222 written 0
rejection check histogram: {'url_liveness': 5, 'cross_source_duplicate': 4, 'degree_eligibility': 1, 'opt_eligibility': 1}
num rejections total: 11
 - SimplifyJobs:[REDACTED] url_liveness HTTP 403
 - SimplifyJobs:[REDACTED] url_liveness HTTP 405
 - SimplifyJobs:[REDACTED] cross_source_duplicate company+title already in vault: jobid:155522
 - ApplyGuy:custom:google:91436104816698054 degree_eligibility currently pursuing a PhD degree
 - vanshb03:[REDACTED] url_liveness HTTP 404
 - SimplifyJobs:[REDACTED] cross_source_duplicate company+title already in vault: jobid:5210942007
 - SimplifyJobs:[REDACTED] cross_source_duplicate company+title already in vault: jobid:5210813007
 - ApplyGuy:[REDACTED] url_liveness HTTP 404
 - AIJobs:[REDACTED] opt_eligibility export-controlled items. Because our employees are provided access to export-controlled items, our p
 - Lever:[REDACTED] cross_source_duplicate company+title already in vault: jobid:[REDACTED]
 - vanshb03:[REDACTED] url_liveness HTTP 404
=== interndock_seen_guides.json on origin/master ===
[
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/campus-ambassador-programs-open-now",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]",
  "https://www.interndock.com/tracker/guides/[REDACTED]"
]
=== how many InternDock-sourced entries appear in rejections/uid namespace ===
InternDock fetch/match in this record present? True 0 0
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== .claude/skills structure ==="
find .claude -type f | sort
'`
```
=== .claude/skills structure ===
.claude/agents/contact-researcher.md
.claude/agents/loop-verifier.md
.claude/scheduled_tasks.lock
.claude/settings.json
.claude/settings.local.json
.claude/skills/promote-dossier/SKILL.md
.claude/skills/promote-dossier/reference/note-templates.md
.claude/skills/review-loop-change/SKILL.md
```
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/git_ops.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/loop-verifier.md`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change/SKILL.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Loop Review Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Notes Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship Pipeline.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Weekly\Internship Loop Weekly Review — 2026-W34.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Monthly\Internship Loop Monthly Review — 2026-08.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Internship Loop Reviews MOC.md`
- `Bash` -- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== recently added dossiers (git show for latest Auto-discovered commit) ==="
git show --stat 8e4b3be0 2>/dev/null | head -10
echo "=== frontmatter of that file ==="
git show 8e4b3be0 2>/dev/null | head -40
echo "=== search for Virtu duplicate pair still present? ==="
find "10_Areas/Career/Internships/List/Dossiers" -iname "*Virtu*" 2>/dev/null`
```
=== recently added dossiers (git show for latest Auto-discovered commit) ===
commit [REDACTED]
Author: internship-research-loop bot <actions@users.noreply.github.com>
Date:   Wed Aug 26 02:19:37 2026 +0000

    Auto-discovered 1 internship(s) — 2026-08-26

 ... Engineer, Backend Intern - Prophet Security.md | 72 ++++++++++++++++++++++
 1 file changed, 72 insertions(+)
=== frontmatter of that file ===
commit [REDACTED]
Author: internship-research-loop bot <actions@users.noreply.github.com>
Date:   Wed Aug 26 02:19:37 2026 +0000

    Auto-discovered 1 internship(s) — 2026-08-26

diff --git a/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer, Backend Intern - Prophet Security.md b/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer, Backend Intern - Prophet Security.md
new file mode 100644
index 00000000..45b4ec15
--- /dev/null
+++ b/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer, Backend Intern - Prophet Security.md	
@@ -0,0 +1,72 @@
+---
+company: Prophet Security
+title: Software Engineer, Backend Intern
+url: https://jobs.ashbyhq.com/prophet-security/[REDACTED]
+source: ApplyGuy
+terms: []
+locations:
+  - Palo Alto, CA
+target_year: []
+date_posted: '2026-08-25'
+date_found: '2026-08-26'
+matched_reason: matched
+status: unreviewed
+next:
+notes:
+  - '[[10_Areas/Career/Internships/List/Dossiers MOC]]'
+preference_tier:
+tags:
+  - internship
+  - auto-discovered
+  - company/prophet-security
+---
+# Software Engineer, Backend Intern
+Found 2026-08-26 via ApplyGuy.
+> [!NOTE] AI/ML: matched on "machine learning".
+## Posting (fetched 2026-08-26)
+# Software Engineer, Backend Intern
+## Location
=== search for Virtu duplicate pair still present? ===
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Quant Research (Undergrad) - Virtu Financial.md
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship- FPGA - Virtu Financial.md
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend Developer Internship - Virtu Financial.md
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Software Engineer Intern - Virtu Financial.md
```
- `Bash` -- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== find Source of Truth / Build Log / Design Rationale files ==="
find "20_Progress/Internship/Building System" -iname "*.md" 2>/dev/null
echo "--- sizes ---"
find "20_Progress/Internship/Building System" -iname "*.md" -exec wc -l {} \; 2>/dev/null`
```
=== find Source of Truth / Build Log / Design Rationale files ===
20_Progress/Internship/Building System/Research Loop - Implementation Plan.md
20_Progress/Internship/Building System/Research Loop - Improvement Plan.md
20_Progress/Internship/Building System/Research Loop - Resources.md
20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive.md
20_Progress/Internship/Building System/Runs/Claude Code Prompts.md
20_Progress/Internship/Building System/Runs/Phases Run.md
20_Progress/Internship/Building System/Runs/Research Loop - Phase 7 Coverage Expansion.md
20_Progress/Internship/Building System/Source of Truth.md
20_Progress/Internship/Building System/System - Build Log.md
--- sizes ---
151 20_Progress/Internship/Building System/Research Loop - Implementation Plan.md
80 20_Progress/Internship/Building System/Research Loop - Improvement Plan.md
66 20_Progress/Internship/Building System/Research Loop - Resources.md
412 20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive.md
81 20_Progress/Internship/Building System/Runs/Claude Code Prompts.md
205 20_Progress/Internship/Building System/Runs/Phases Run.md
74 20_Progress/Internship/Building System/Runs/Research Loop - Phase 7 Coverage Expansion.md
59 20_Progress/Internship/Building System/Source of Truth.md
123 20_Progress/Internship/Building System/System - Build Log.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Source of Truth.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers MOC.md`
- `Bash` -- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== current origin/master debate_losses.json ==="
git show origin/master:state/debate_losses.json | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(\"count\",len(d))
top=sorted(d.items(), key=lambda x:-x[1])[:15]
print(top)
import collections
c=collections.Counter(d.values())
print(\"loss-count histogram:\", dict(sorted(c.items())))
"
echo "=== current origin/master excluded_uids.json count ==="
git show origin/master:state/excluded_uids.json | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(\"excluded total\", len(d))
"
echo "=== how much did excluded_uids grow this week? check Excluded log recent lines from vault ==="
'
echo "=== vault Excluded log tail ==="
cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
tail -c 3000 "10_Areas/Career/Internships/List/Excluded — Losing The Debate.md" 2>/dev/null | tail -30
wc -l "10_Areas/Career/Internships/List/Excluded — Losing The Debate.md" 2>/dev/null`
```
=== current origin/master debate_losses.json ===
count 233
[('SimplifyJobs:[REDACTED]', 23), ('zshah101:ashby:voleon:[REDACTED]', 23), ('SimplifyJobs:[REDACTED]', 21), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20), ('ApplyGuy:[REDACTED]', 20)]
loss-count histogram: {1: 10, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1, 9: 8, 10: 1, 11: 1, 13: 9, 14: 11, 15: 2, 16: 12, 17: 4, 18: 1, 19: 8, 20: 156, 21: 1, 23: 2}
=== current origin/master excluded_uids.json count ===
excluded total 388
=== how much did excluded_uids grow this week? check Excluded log recent lines from vault ===
=== vault Excluded log tail ===
dale-CA-USA/[REDACTED]](https://disney.wd5.myworkdayjobs.com/disneycareer/job/Glendale-CA-USA/[REDACTED]) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **The Walt Disney Company** — Menu Planning Intern — [https://disney.wd5.myworkdayjobs.com/disneycareerdc/job/Glendale-CA-USA/[REDACTED]](https://disney.wd5.myworkdayjobs.com/disneycareerdc/job/Glendale-CA-USA/[REDACTED]) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Rystad Energy** — Analyst Intern - Summer 2027 — [https://apply.workable.com/rystad-energy/j/74A4CBBC6B/apply](https://apply.workable.com/rystad-energy/j/74A4CBBC6B/apply) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **TikTok** — Client Solutions Intern — [https://lifeattiktok.com/search/7677467052537776437](https://lifeattiktok.com/search/7677467052537776437) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **TikTok** — Client Solutions Intern - Global Business Solutions — [https://lifeattiktok.com/search/7677467375487486213](https://lifeattiktok.com/search/7677467375487486213) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **TikTok** — Client Solutions Intern - Global Business Solutions — [https://lifeattiktok.com/search/7677467375486765317](https://lifeattiktok.com/search/7677467375486765317) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Tesla** — Internship - Fullstack Engineer - Applications Engineering - Winter/Spring 2027 — [https://www.tesla.com/careers/search/job/280820](https://www.tesla.com/careers/search/job/280820) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Kodiak Robotics** — Behavior Planning Intern - Motion Planning — [https://job-boards.greenhouse.io/kodiak/jobs/4377721009](https://job-boards.greenhouse.io/kodiak/jobs/4377721009) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **BTI360** — Software Engineering Intern — [https://job-boards.greenhouse.io/bti36021/jobs/8155152](https://job-boards.greenhouse.io/bti36021/jobs/8155152) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Sage** — Software Engineering Intern (Edge) – Summer 2027 — [https://job-boards.greenhouse.io/sage49/jobs/6131191004](https://job-boards.greenhouse.io/sage49/jobs/6131191004) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Kodiak Robotics** — Simulation Intern — [https://job-boards.greenhouse.io/kodiak/jobs/4378662009](https://job-boards.greenhouse.io/kodiak/jobs/4378662009) — excluded 2026-08-25 — lost the debate 5 consecutive runs
- **Kodiak Robotics** — Controls Intern — [https://job-boards.greenhouse.io/kodiak/jobs/4378402009](https://job-boards.greenhouse.io/kodiak/jobs/4378402009) — excluded 2026-08-25 — lost the debate 5 consecutive runs
399 10_Areas/Career/Internships/List/Excluded — Losing The Debate.md
```
- `Bash` -- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
ls "20_Progress/Internship/Building System/Runs" 2>/dev/null`
```
Claude Code Prompts — Archive.md
Claude Code Prompts.md
Phases Run.md
Research Loop - Phase 7 Coverage Expansion.md
```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Runs\Discovery Step Postmortem — Write-Starvation Incident (2026-08-26).md`
```
---
type: project
status: active
created: 2026-08-26
related_progress:
  - "[[Source of Truth]]"
  - "[[System - Build Log]]"
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
tags:
  - internship
  - automation
  - postmortem
  - incident
next: "URGENT, time-bound: ~156 real ApplyGuy candidates are sitting at 20/48 debate losses as of 2026-08-26 ~14:35 UTC and will start permanently excluding within roughly 24-30 hours unless the write-budget-squatting bug below is fixed or MAX_DEBATE_LOSSES/budget is raised as a stopgap first. Decide before that window closes."
---
# Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)
==A live, currently-active bug, found by reading `logs/runs.jsonl` directly rather than trusting `Source of Truth`/`System - Build Log`, which are both stale relative to what's actually shipped and actually happening as of this writing.== Full method: every module in `core/`, `ingestion/`, `vault_writer/`, `run_pipeline.py`, `recheck.py`, `revalidate.py`, `git_ops.py`, `run_log.py` read directly from the live repo (`~/projects/work/internship-research-loop`, both local HEAD `cbbb2a1` and `origin/master`, 21 commits ahead, diffed to confirm zero code drift between them); `logs/runs.jsonl` read across 82 real hourly run records spanning 2026-08-22 15:11 through 2026-08-26 14:35; `state/*.json` read directly; vault dossier counts cross-checked by direct folder count against the pipeline's own self-reported total (both agree: 319). Not sampled, not summarized from memory.

## The Headline Finding
**The write gate has no failure memory.** A candidate that fails at `vault_writer/validate.py` (`url_liveness`, `cross_source_duplicate`, `opt_eligibility`, `degree_eligibility`, `cs_relevance`) is never added to `seen_ids.json` (only a confirmed *push* adds a uid there) and never added to `excluded_uids.json` (only `_prioritize_and_cap`'s **deferred** list feeds the debate-loss counter — a candidate that gets *selected* into `this_run` and then rejected by the write gate never enters `deferred` at all). If such a candidate keeps winning its bucket's ranking in `_prioritize_and_cap` (`core/debate.py`'s `debate_compare`, stable-sorted on preference tier → bucket urgency → recency), it is re-offered and re-selected every single hour, forever, with zero mechanism to ever stop.

This is not hypothetical. `SimplifyJobs:[REDACTED]` (HTTP 403) appears **identically** in the rejection list of every run sampled from 2026-08-22 through 2026-08-26 — at minimum 4 straight days, permanently occupying one of the ~10-11 write-budget slots every single hour.

## The Evidence
82 hourly run records read directly, in two windows:
- **2026-08-22T15:11 → 2026-08-25T17:23 (72 runs, ~3 days):** `written_count` was 0 in 68 of 72 runs. The 4 exceptions: 1 at 08-24T16:24, 2 at 08-24T21:19, 1 at 08-25T06:28. Every one of these 72 runs matched 10-51 new eligible candidates (`new_count`); the write budget (`MAX_NEW_WRITES_PER_RUN` = 3 AI/ML + 3 Fullstack + 3 CyS&Finance + 1 Other = 10/run) was always full, and rejections consistently totaled exactly the size of `this_run` — meaning **100% of the selected write-budget was rejected, not partially.**
- **2026-08-26T05:24 → 2026-08-26T14:35 (10 runs, most recent):** `written_count` = 0 in all 10, while `new_count` jumped to 219-233/run (`ApplyGuy` alone contributing 168 matches/run — it just went live, Task 2 of the local HEAD commit `cbbb2a1`). `deferred_count` climbed to 215-222/run.
- The vault's own git log (direct source of truth, not the pipeline's log) shows a partial-recovery burst of 11 real writes in the ~12-hour gap between these two sampled windows (commits `6b6dcb09` "7", `95f0f977` "2", `896a5c78` "1" on 08-25, plus 2 more since) — so the stall is **bursty, not a hard freeze**: the doomed-candidate queue occasionally empties or gets briefly outranked, a few real writes get through, then it refills with new persistent losers and stalls again. Reporting it as a constant zero would overstate the finding; reporting it as fixed would understate it — as of the most recent 10 straight runs (10 hours), it is fully stalled again.
- Cross-checked directly: today's freshest dossier (`Software Engineer, Backend Intern - Prophet Security.md`, written 2026-08-26 via one of the rare successful writes) still carries `matched_reason: matched` (the bare literal string §6 of the [[30_Order/Standards/Internship Notes Standard]] already flagged as a gap on 2026-07-30) and a `> [!NOTE] AI/ML: matched on "machine learning"` callout on a **backend engineering role at a security company** — the same incidental-keyword classification bug class as AbbVie (flagged, one data point, in the 2026-08-23 weekly review) and Databricks/Mosaic (flagged 2026-07-26, still unfixed as a systemic pattern). This is now a *third* independently-observed instance — no longer reasonable to treat as an edge case.

## The Compounding, Time-Bound Risk (act on this first)
`state/debate_losses.json` on `origin/master` right now: **233 entries**, of which **156 sit at exactly 20 losses** (`MAX_DEBATE_LOSSES` = 48), nearly all `ApplyGuy:*` uids — real candidates from ApplyGuy's very first exposure to this pipeline, genuinely new and (per `sources.py`'s own citation) confirmed to carry a real employer ATS link 100% of the time. `excluded_uids.json` is still 388 — unchanged across every check this session, meaning **none of these have crossed the line yet.** At the current ~1 loss/hour rate, the leading edge of that cluster reaches 48 in **roughly 24-30 hours from 2026-08-26 14:35 UTC** — i.e., sometime around 2026-08-27 midday-to-evening.

The two bugs compound: the write budget is being permanently squatted by candidates that can never be written (dead links, cached OPT exclusions, cross-source dupes), which means genuinely-new ApplyGuy candidates never get a real turn at the write gate — they only ever appear in `deferred`, where they silently accrue toward permanent exclusion. **Unless this is addressed, a large batch of real, eligible, never-actually-evaluated postings will move to `Excluded — Losing The Debate.md` within about a day**, not because they lost on merit but because the budget was never actually available to them.

This is worth a stopgap even before a real fix: temporarily raising `MAX_DEBATE_LOSSES` again (it was already raised 5→48 on 2026-08-23 for exactly this shape of problem) or the per-run budget buys time without needing the harder root-cause fix done under pressure.

## Why This Specific Class Of Candidate Keeps Winning (hypothesis, not confirmed)
`debate_compare`'s only real tiebreaker within a bucket is recency (`date_posted or 0`, most-recent-first). Most sources do carry a real `date_posted`, so a genuinely-stale dead candidate should eventually lose that tiebreak to fresher arrivals — *unless* the specific bucket it sits in (especially `Other`, budget 1/run, or `AI/ML` when the item is preference-tier `high`) simply doesn't receive many competing candidates with a *newer* date in the same hour, letting an old-but-still-locally-freshest item keep winning by default. This is plausible from the code but **not verified** — nothing in this pass directly logged which uids actually won `this_run`'s selection each hour versus merely appearing in `rejections`. **Recommended before fixing:** add one line of logging (the selected `this_run` uids, not just the final rejections) for a day, to confirm the exact mechanism before changing `debate_compare` or the write-then-remember ordering.

## Secondary Findings, Same Pass
1. **Schema-drift coverage covers less than half the sources.** `core/schema_drift.py`'s `check_all()` only pre-flights SimplifyJobs, JGCL, vanshb03, zshah101, ApplyGuy — the five single-feed JSON sources. Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock (6 of 11 sources now) have no pre-flight check at all; a renamed field on any of them degrades silently to zero matches per company/feed, with no halt and no issue, and nothing in the current review process would catch it except a human noticing a source's `filter_match_counts` unexpectedly at 0 in the raw log (Ashby is already at 0 in every run sampled this pass — worth a direct check of whether that's a real drift or genuinely zero current Ashby-hosted intern postings; not resolved this pass).
2. **`Source of Truth.md` and `System - Build Log.md` are stale relative to shipped code**, not just relative to runtime state. Both describe the Phase 4 fixes (NL/HK/PL/IL denylist entries, the widened `_ADJACENT_FIELD_COMPANY_HINT_RE`, `MAX_DEBATE_LOSSES` 5→48, the debate-loss spike alert, `revalidate.py`, the Zipline SPA fix, Workday/Oracle job-id dedup) as **"queued for Prompt 10, not yet run"** — every one of them is already live in the code read this session. Same for Lever/InternDock/ApplyGuy: `Source of Truth` (updated 2026-08-24) says "InternDock... explicitly not wired into `SOURCES` yet"; it is wired, live, and fetching in production as of this session. Anyone making a decision by reading these notes instead of the live repo is working from a false picture of what's already shipped.
3. **The review system had no visibility into any of this**, and by its own design could not have. The one Weekly Discovery Review that has run ([[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34]], 2026-08-23) explicitly notes `logs/runs.jsonl` / GitHub issues were "not reachable this session (no local clone... no `gh` auth)" — its entire method is a 12-dossier sample of what's already *in* the vault, which cannot detect a bug whose entire signature is *what never got written*. See the Review-system section below.

## What's Genuinely Fixed Since The Last Review (say this too, not just new problems)
- The `notes:`/`company/<slug>` tag write-time gap the 2026-08-23 weekly review found at 11/392 and 69/392 respectively is fixed — confirmed directly against today's freshest dossier, both fields present and correctly formed.
- The location denylist gaps (Netherlands/Hong Kong/Poland/Israel/bare "London"), the adjacent-field company hints (FTI/Truist/Vertiv/UHY/CNO/Dimensional/KeyBank/Continental), the Zipline SPA content-extraction bug, and Workday/Oracle-HCM job-id cross-source dedup are all live in code, all with real-data citations in their comments.
- `revalidate.py` (periodic re-check of live dossiers against current rules) exists and is wired into `.github/workflows/revalidate.yml` — the exact "retroactive re-sweep" the 2026-08-23 audit recommended.
- The `Quantitative Trading Intern - Virtu.md` gate-conformance miss the weekly review flagged is **still live in the vault**, unaddressed 3 days later — a real carryover, not a false alarm.

## Recommendations (not implemented this pass — this is a postmortem, not a fix)
1. **Stopgap now:** raise `MAX_DEBATE_LOSSES` or pause the clock on the current ApplyGuy cohort before ~2026-08-27 midday, given the quantified risk above.
2. **Root-cause fix:** give `validate_and_write` rejections a real memory. Simplest shape consistent with this codebase's existing patterns: a `write_gate_failures.json` (uid → {check, count, first_seen}) checked before re-offering a uid as new, with its own reviewable-log/exclusion threshold — same "notify, don't silently drop" discipline as `excluded_uids.json` already uses, just triggered by a different failure class (structurally-doomed, not merely out-ranked).
3. **Confirm the win-mechanism hypothesis** (log `this_run` selections for a day) before changing `debate_compare`.
4. **Extend schema-drift coverage**, or at minimum add a per-source zero-match-rate alert to the run record, to close the blind spot on the 6 unchecked sources.
5. **Update `Source of Truth.md` and `System - Build Log.md`** to match what's actually shipped — the "queued, not yet run" framing is actively misleading now.

```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- ## 2026-08-24 — Prompt 14 v2: Lever Shipped, InternDock Partial, JGCL Resolved, LinkedIn/7-Company Dead End Confirmed
+ ## 2026-08-26 — Discovery Postmortem: Write-Starvation Bug Found Live, Documentation Confirmed Stale
Deep vault-and-repo audit (Claude, requested as a full-system postmortem before any new build work), reading every module in the live repo, 82 real hourly run records (2026-08-22 through 2026-08-26), and current `state/*.json` directly rather than trusting this file or [[Source of Truth]]. Full report: [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]].
**Real, currently-active bug found, not previously documented anywhere in this file or Source of Truth**: `validate_and_write` rejections (dead URL, cross-source duplicate, cached OPT exclusion) are never added to `seen_ids.json` or `excluded_uids.json`, so a structurally-doomed candidate that keeps winning `_prioritize_and_cap`'s ranking gets re-offered and re-selected every hour forever, permanently occupying write-budget slots. Confirmed via `logs/runs.jsonl`: `written_count` was 0 in 68 of 72 sampled hourly runs (2026-08-22 to 2026-08-25), and 0 in the 10 most recent runs (2026-08-26), despite 10-233 new eligible candidates matching every single hour. **Time-bound compounding risk**: `state/debate_losses.json` shows 156 real ApplyGuy-sourced candidates sitting at 20/48 debate losses as of 2026-08-26 14:35 UTC — on track to permanently exclude within roughly a day unless the budget-squatting bug is fixed or `MAX_DEBATE_LOSSES` is raised again first.
**Also found**: this file and [[Source of Truth]] are stale relative to already-shipped code — Phase 4's fixes (location-denylist entries, adjacent-field hints, `MAX_DEBATE_LOSSES` 5→48, `revalidate.py`, Zipline SPA fix, Workday/Oracle dedup) and Lever/InternDock/ApplyGuy going live are all real and live in the repo as of this session, but both notes still frame them as "queued for Prompt 10, not yet run." The `notes:`/`company/<slug>` tag gap the 2026-08-23 weekly review found is confirmed fixed; the Virtu quant-trading gate-conformance miss that review also found is confirmed still unfixed 3 days later. Nothing fixed this session — postmortem and adversary-analysis only, per explicit instruction; fixes are queued, not yet run.
## 2026-08-24 — Prompt 14 v2: Lever Shipped, InternDock Partial, JGCL Resolved, LinkedIn/7-Company Dead End Confirmed
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- ## 2026-08-26 — Discovery Postmortem: Write-Starvation Bug Found Live, Documentation Confirmed Stale
Deep vault-and-repo audit (Claude, requested as a full-system postmortem before any new build work), reading every module in the live repo, 82 real hourly run records (2026-08-22 through 2026-08-26), and current `state/*.json` directly rather than trusting this file or [[Source of Truth]]. Full report: [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]].
**Real, currently-active bug found, not previously documented anywhere in this file or Source of Truth**: `validate_and_write` rejections (dead URL, cross-source duplicate, cached OPT exclusion) are never added to `seen_ids.json` or `excluded_uids.json`, so a structurally-doomed candidate that keeps winning `_prioritize_and_cap`'s ranking gets re-offered and re-selected every hour forever, permanently occupying write-budget slots. Confirmed via `logs/runs.jsonl`: `written_count` was 0 in 68 of 72 sampled hourly runs (2026-08-22 to 2026-08-25), and 0 in the 10 most recent runs (2026-08-26), despite 10-233 new eligible candidates matching every single hour. **Time-bound compounding risk**: `state/debate_losses.json` shows 156 real ApplyGuy-sourced candidates sitting at 20/48 debate losses as of 2026-08-26 14:35 UTC — on track to permanently exclude within roughly a day unless the budget-squatting bug is fixed or `MAX_DEBATE_LOSSES` is raised again first.
**Also found**: this file and [[Source of Truth]] are stale relative to already-shipped code — Phase 4's fixes (location-denylist entries, adjacent-field hints, `MAX_DEBATE_LOSSES` 5→48, `revalidate.py`, Zipline SPA fix, Workday/Oracle dedup) and Lever/InternDock/ApplyGuy going live are all real and live in the repo as of this session, but both notes still frame them as "queued for Prompt 10, not yet run." The `notes:`/`company/<slug>` tag gap the 2026-08-23 weekly review found is confirmed fixed; the Virtu quant-trading gate-conformance miss that review also found is confirmed still unfixed 3 days later. Nothing fixed this session — postmortem and adversary-analysis only, per explicit instruction; fixes are queued, not yet run.
## 2026-08-24 — Prompt 14 v2: Lever Shipped, InternDock Partial, JGCL Resolved, LinkedIn/7-Company Dead End Confirmed
+ ## 2026-08-24 — Prompt 14 v2: Lever Shipped, InternDock Partial, JGCL Resolved, LinkedIn/7-Company Dead End Confirmed
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- - **The 2026-08-23 "46 `vault_delete` calls" is accounted for, confirmed directly this session**, not re-investigated as a new concern: the auto-captured conversation note [[60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship dossier audit and filter-rule reconciliation]] records exactly `mcp__jarvis__vault_delete: 46` in its own tool-use tally — a real, already-tracked 241-minute audit/reconciliation session (2026-08-23, 11:53-15:54), not an untracked deletion event.
+ - **The 2026-08-23 "46 `vault_delete` calls" is accounted for, confirmed directly this session**, not re-investigated as a new concern: the auto-captured conversation note [[60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship dossier audit and filter-rule reconciliation]] records exactly `mcp__jarvis__vault_delete: 46` in its own tool-use tally — a real, already-tracked 241-minute audit/reconciliation session (2026-08-23, 11:53-15:54), not an untracked deletion event.
## 2026-08-26 — Discovery Postmortem: Write-Starvation Bug Found Live, Documentation Confirmed Stale
Deep vault-and-repo audit (Claude, requested as a full-system postmortem before any new build work), reading every module in the live repo, 82 real hourly run records (2026-08-22 through 2026-08-26), and current `state/*.json` directly rather than trusting this file or [[Source of Truth]]. Full report: [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]].
**Real, currently-active bug found, not previously documented anywhere in this file or Source of Truth**: `validate_and_write` rejections (dead URL, cross-source duplicate, cached OPT exclusion) are never added to `seen_ids.json` or `excluded_uids.json`, so a structurally-doomed candidate that keeps winning `_prioritize_and_cap`'s ranking gets re-offered and re-selected every hour forever, permanently occupying write-budget slots. Confirmed via `logs/runs.jsonl`: `written_count` was 0 in 68 of 72 sampled hourly runs (2026-08-22 to 2026-08-25), and 0 in the 10 most recent runs (2026-08-26), despite 10-233 new eligible candidates matching every single hour. **Time-bound compounding risk**: `state/debate_losses.json` shows 156 real ApplyGuy-sourced candidates sitting at 20/48 debate losses as of 2026-08-26 14:35 UTC — on track to permanently exclude within roughly a day unless the budget-squatting bug is fixed or `MAX_DEBATE_LOSSES` is raised again first.
**Also found**: this file and [[Source of Truth]] are stale relative to already-shipped code — Phase 4's fixes (location-denylist entries, adjacent-field hints, `MAX_DEBATE_LOSSES` 5→48, `revalidate.py`, Zipline SPA fix, Workday/Oracle dedup) and Lever/InternDock/ApplyGuy going live are all real and live in the repo as of this session, but both notes still frame them as "queued for Prompt 10, not yet run." The `notes:`/`company/<slug>` tag gap the 2026-08-23 weekly review found is confirmed fixed; the Virtu quant-trading gate-conformance miss that review also found is confirmed still unfixed 3 days later. Nothing fixed this session — postmortem and adversary-analysis only, per explicit instruction; fixes are queued, not yet run.
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
```diff
- updated: 2026-08-24
related_progress:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
tags:
  - internship
  - career
  - system-design
next: "2026-08-24: Prompt 14 v2 shipped Lever live (nine sources now, not eight), built InternDock's detection+parsing but explicitly left it unwired, and closed the JGCL and LinkedIn/7-company open questions for real. Prompt 17 (InternDock's SOURCES wiring, evaluating ApplyGuy/dreamworkhq) is next, not yet run. Full detail: this file's 2026-08-24 entry and [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 14 v2."
+ updated: 2026-08-26
related_progress:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]]"
tags:
  - internship
  - career
  - system-design
next: "URGENT (2026-08-26): a live write-starvation bug is squatting the entire write budget on structurally-doomed candidates while ~156 real ApplyGuy candidates climb toward permanent debate-loss exclusion (48 losses) within roughly a day — see [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]] before touching anything else in this repo. Prompt 17 (InternDock/ApplyGuy evaluation) has since shipped for real — both are live sources as of this postmortem — but that entry below is now stale on that point; the postmortem note is the current source of truth until this file is updated to match."
```

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Runs\Discovery Step Postmortem — Write-Starvation Incident (2026-08-26).md`

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis" && echo "=== Career-related dirs ===" && find . -ipath "*career*" -not -path "*/node_modules/*" -not -path "*/.git/*" -type d 2>/dev/null && echo "=== Internship-related files ===" && find . -iname "*internship*" -not -path "*/.git/*" 2>/dev/null && echo "=== dossier files ===" && find . -iname "*dossier*" -not -path "*/.git/*" 2>/dev/null`
- `echo "=== search common locations for internship-research-loop repo ===" 
for p in "$HOME" "/c/Users/Anant Gupta" "/d/Users/_Anant" "/d/Users/_Anant/10_Areas/Documents" "/d" "/c"; do
  echo "--- $p ---"
  find "$p" -maxdepth 4 -iname "internship-research-loop*" -not -path "*Jarvis/60_Claude*" 2>/dev/null
done`
- `ls "/c/Users/Anant Gupta" 2>/dev/null; echo "---wsl check---"; ls "//wsl$" 2>/dev/null; ls "/mnt/c" 2>/dev/null | head; wsl.exe -l -v 2>/dev/null`
- `find "//wsl\$/Ubuntu/home" -maxdepth 5 -iname "*internship*" 2>/dev/null
echo "---try root---"
find "//wsl\$/Ubuntu/root" -maxdepth 5 -iname "*internship*" 2>/dev/null`
- `REPO="//wsl\$/Ubuntu/home/anant_gupta/projects/work/internship-research-loop"
echo "=== top level ==="
ls -la "$REPO"
echo "=== git log (last 40) ==="
git -C "$REPO" log --oneline -40 2>/dev/null
echo "=== git status ==="
git -C "$REPO" status 2>/dev/null`
- `wsl.exe -d Ubuntu -- bash -lc 'cd ~/projects/work/internship-research-loop && git log --oneline -50 && echo "===STATUS===" && git status && echo "===STRUCTURE===" && find . -maxdepth 3 -not -path "./.git*" -not -path "./.venv*" -not -path "*__pycache__*" -not -path "./.pytest_cache*" | sort'`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== state file sizes/counts ==="
for f in state/*.json; do echo "--$f--"; python3 -c "import json,sys; d=json.load(open(\"$f\")); print(type(d), len(d))" 2>/dev/null || wc -c "$f"; done
echo "=== logs/runs.jsonl last 5 lines ==="
tail -n 5 logs/runs.jsonl
echo "=== logs/rechecks.jsonl last 5 lines ==="
tail -n 5 logs/rechecks.jsonl
echo "=== workflows ==="
ls .github/workflows
echo "=== README ==="
cat README.md
'
`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== count of runs and written_count distribution over last 72 entries ==="
tail -n 72 logs/runs.jsonl | python3 -c "
import json,sys
for line in sys.stdin:
    d=json.loads(line)
    print(d[\"timestamp\"], \"new=\",d[\"new_count\"], \"deferred=\",d[\"deferred_count\"], \"written=\",d[\"written_count\"], \"total=\",d[\"dossier_total\"], \"excl=\",d[\"newly_excluded_count\"], \"halted=\",d[\"halted\"])
"
'
`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
python3 -c "
import json
for f in [\"state/seen_ids.json\",\"state/dossier_uids.json\",\"state/excluded_uids.json\",\"state/debate_losses.json\",\"state/opt_cache.json\",\"state/capacity_notified.json\"]:
    d=json.load(open(f))
    print(f, type(d).__name__, len(d))
"
echo "=== opt_cache excluded count ==="
python3 -c "
import json
d=json.load(open(\"state/opt_cache.json\"))
excl=[k for k,v in d.items() if v.get(\"verdict\")==\"excluded\"]
print(\"total\",len(d),\"excluded\",len(excl))
print(excl[:10])
"
echo "=== debate_losses top values ==="
python3 -c "
import json
d=json.load(open(\"state/debate_losses.json\"))
print(\"count\",len(d))
top=sorted(d.items(), key=lambda x:-x[1])[:10]
print(top)
"
'
`
- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
echo "=== counts per bucket (actual vault, Windows checkout) ==="
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" "Viewed"; do
  n=$(find "$d" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)
  echo "$d : $n"
done
echo "=== total excluding Viewed ==="
find "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l
echo "=== git log for this Windows Jarvis checkout, last internship-related commits ==="
cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
git log --oneline -10 -- "10_Areas/Career/Internships/List/Dossiers" 2>/dev/null
echo "=== last commit touching this path, date ==="
git log -1 --format="%ci %s" -- "10_Areas/Career/Internships/List/Dossiers" 2>/dev/null`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
git fetch origin 2>&1 | tail -5
echo "=== commits between local HEAD and origin/master ==="
git log --oneline HEAD..origin/master
echo "=== files changed in those commits ==="
git diff --stat HEAD origin/master -- run_pipeline.py core/ ingestion/ vault_writer/ recheck.py revalidate.py
echo "=== latest runs.jsonl on origin/master (last 10) ==="
git show origin/master:logs/runs.jsonl | tail -10 | python3 -c "
import json,sys
for line in sys.stdin:
    d=json.loads(line)
    print(d[\"timestamp\"], \"new=\",d[\"new_count\"], \"deferred=\",d[\"deferred_count\"], \"written=\",d[\"written_count\"], \"total=\",d[\"dossier_total\"], \"excl=\",d[\"newly_excluded_count\"], \"halted=\",d[\"halted\"], d.get(\"halt_reason\"))
"
'
`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== full breakdown of latest run rejections (checks histogram) ==="
git show origin/master:logs/runs.jsonl | tail -1 | python3 -c "
import json,sys,collections
d=json.loads(sys.stdin.read())
print(\"timestamp\", d[\"timestamp\"])
print(\"fetch_counts\", d[\"fetch_counts\"])
print(\"filter_match_counts\", d[\"filter_match_counts\"])
print(\"new_count\", d[\"new_count\"], \"deferred\", d[\"deferred_count\"], \"written\", d[\"written_count\"])
c = collections.Counter(r[\"check\"] for r in d[\"rejections\"])
print(\"rejection check histogram:\", dict(c))
print(\"num rejections total:\", len(d[\"rejections\"]))
for r in d[\"rejections\"][:15]:
    print(\" -\", r[\"uid\"], r[\"check\"], r[\"reason\"][:100])
"
echo "=== interndock_seen_guides.json on origin/master ==="
git show origin/master:state/interndock_seen_guides.json 2>&1 | head -20
echo "=== how many InternDock-sourced entries appear in rejections/uid namespace ==="
git show origin/master:logs/runs.jsonl | tail -1 | python3 -c "
import json,sys
d=json.loads(sys.stdin.read())
print(\"InternDock fetch/match in this record present?\", \"InternDock\" in d[\"fetch_counts\"], d[\"fetch_counts\"].get(\"InternDock\"), d[\"filter_match_counts\"].get(\"InternDock\"))
"
'
`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== .claude/skills structure ==="
find .claude -type f | sort
'`
- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== recently added dossiers (git show for latest Auto-discovered commit) ==="
git show --stat 8e4b3be0 2>/dev/null | head -10
echo "=== frontmatter of that file ==="
git show 8e4b3be0 2>/dev/null | head -40
echo "=== search for Virtu duplicate pair still present? ==="
find "10_Areas/Career/Internships/List/Dossiers" -iname "*Virtu*" 2>/dev/null`
- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== find Source of Truth / Build Log / Design Rationale files ==="
find "20_Progress/Internship/Building System" -iname "*.md" 2>/dev/null
echo "--- sizes ---"
find "20_Progress/Internship/Building System" -iname "*.md" -exec wc -l {} \; 2>/dev/null`
- `wsl.exe -d Ubuntu -- bash -lc '
cd ~/projects/work/internship-research-loop
echo "=== current origin/master debate_losses.json ==="
git show origin/master:state/debate_losses.json | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(\"count\",len(d))
top=sorted(d.items(), key=lambda x:-x[1])[:15]
print(top)
import collections
c=collections.Counter(d.values())
print(\"loss-count histogram:\", dict(sorted(c.items())))
"
echo "=== current origin/master excluded_uids.json count ==="
git show origin/master:state/excluded_uids.json | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(\"excluded total\", len(d))
"
echo "=== how much did excluded_uids grow this week? check Excluded log recent lines from vault ==="
'
echo "=== vault Excluded log tail ==="
cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
tail -c 3000 "10_Areas/Career/Internships/List/Excluded — Losing The Debate.md" 2>/dev/null | tail -30
wc -l "10_Areas/Career/Internships/List/Excluded — Losing The Debate.md" 2>/dev/null`
- `cd "D:/Users/_Anant/10_Areas/Documents/Jarvis"
ls "20_Progress/Internship/Building System/Runs" 2>/dev/null`


