---
type: plan
status: active
created: 2026-07-27
updated: 2026-07-27
deadline: 2026-09-01
review_cadence: "daily via Daily Operating System; full rewrite Sunday via Weekly Operating System; full review 2026-08-31"
tags:
  - plan
  - summer
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[Daily Operating System]]"
  - "[[Weekly Operating System]]"
  - "[[LeetCode & CSCI 4041]]"
  - "[[ML Fundamentals (2033 + 2230)]]"
  - "[[Anti-Drift Rules]]"
  - "[[Engineer Edge Roadmap]]"
  - "[[Internships Hub]]"
next: "[[Daily Operating System]]"
---
# Final Month Plan (Jul 28 – Sep 1)
==This is the one source of truth for the rest of the summer — goal, timeframe, systems, real status, and the rule for keeping it current. Replaces the separate July recap, close-out, and August-plan notes; they were three fragments of one thing.==
## Goal
Turn the daily floor that never ran in Dubai or Bangalore — LeetCode, system design, trading knowledge, AI knowledge — into an actual habit, and ship the project work already in flight (TradingView's UI, CausalOps' two remaining steps, Arc, internship-loop, Portfolio's Orby upgrade) before the 2026-09-01 flight to the US. **One metric:** daily floor checked ≥90% of days in `10_Areas/Life/Enumerate/Daily/` from 2026-07-28 through 2026-08-31.
## Timeframe
2026-07-28 → 2026-09-01, 36 days. Real capacity is closer to 31 focused days — the BLR→Dubai move sits inside the week of Aug 15–21 and stays deliberately light, not zero. Location: Bangalore through Aug 17, Dubai Aug 24 through the Sept 1 flight.
| Week | Dates | Location | Flagship | Certification |
|---|---|---|---|---|
| W0 | Jul 28–31 | Bangalore | Close-out — see §Implementation Status below | — |
| W1 | Aug 1–7 | Bangalore | TradingView UI review + CausalOps close (SQL migration, integration tests) | Git & GitHub exam → AWS Cloud Practitioner starts |
| W2 | Aug 8–14 | Bangalore | Arc — real scope (one sentence problem, one user, one hero flow, one metric), then build | AWS Cloud Practitioner finishes → Azure AI-900 starts |
| W3 | Aug 15–21 | Bangalore → Dubai (light) | Arc continues, review-only on travel days | Azure AI-900 finishes; Google AI Essentials + NVIDIA credential |
| W4 | Aug 22–28 | Dubai | internship-loop Steps 2–9 buildout + Portfolio Orby upgrade | Anthropic/Claude certification |
| W5 | Aug 29–31 | Dubai | Buffer — close what slipped, write the Aug 31 review | Catch-up slot |
## Systems
### Daily floor
Four tracks, every day, mechanism lives in [[Daily Operating System]] — this section states them, doesn't duplicate the checklist:
1. **LeetCode + CSCI 4041 + company problems** — ≥5/day, full system in [[LeetCode & CSCI 4041]].
2. **System design** — 20–30 min/day, following [[Engineer Edge Roadmap]]'s 8-step order (API design → schema/indexes → queues → caching → auth → observability → reliability → scale), applied against TradingView or CausalOps since both are real systems you actually have.
3. **Trading knowledge** — one note-line/day minimum: personal mechanics (market-making math from the MIT Quant Bible, already scoped at 6–8 hours total in `PDF's Ingestion Implementation.md`) or one TradingView project note read.
4. **AI knowledge** — one item/day, informal: an NVIDIA course beyond the one counted certification, a DataTalksClub zoomcamp lesson, a HuggingFace agents-course unit, or a paper relevant to CausalOps or TradingView's AI hub.
### Weekly flagship rotation
One project gets the week's hours beyond the daily floor — see the Timeframe table. Arc's kickoff at W2 requires a real scoping pass first; the existing `20_Progress/Projects/CS/Arc/` docs (a 5-sprint roadmap, a data-model sketch) don't count as that scope — they were written before any build discipline was applied to this project and stay as raw material, not the plan.
### Certifications — the 5
Chosen from `40_Resources/CS/Links` (Courses → Certifications), [[Summer Grind]]'s NVIDIA course list, and `PDF's Ingestion Implementation.md`'s researched stack, aimed at the three dossier categories (AI & ML, Fullstack, CyS & Finance). **Git & GitHub is not one of the 5** — exam scheduled for W1, next cert starts the day it's passed.
1. **AWS Certified Cloud Practitioner** — 10–15 hours. Reads across all three dossier categories.
2. **Microsoft Azure AI Fundamentals (AI-900)** — 10–15 hours. Named in the researched stack as appearing on most high-paying AI postings.
3. **Google AI Essentials** — 5 hours. Fastest of the 5; placed in the light travel week.
4. **NVIDIA "Introduction to NVIDIA NIM Microservices"** — 2 hours, free, per [[Summer Grind]]'s own course list. Ties to the LLM work already live in TradingView's AI Brain Hub and CausalOps.
5. **Anthropic / Claude certification** — hour count unconfirmed as of 2026-07-27. **W1 action item:** look up the exact guide linked in `40_Resources/CS/Links` and lock the real hour figure before W4 starts, so it doesn't become the thing that silently slips.
### Jarvis — commands and scheduled routines
| Cadence | Command | Protects |
|---|---|---|
| Daily, morning | `/startday` | Populates the day's floor + flagship into the daily note |
| Daily, evening | `/closeday` | Writes the scorecard, catches a red day before two in a row |
| Weekly, Sunday | `/weekly-review` | The 7 questions + this note's Current Progress update |
| Weekly | `/ops health-check` | Vault maintenance |
> [!WARNING]
> Five scheduled `CronCreate` routines are designed — morning `/startday`, midday internship-dossier check against the 201-cap, evening `/closeday`, a daily check that no `Applying/` note has gone a week without a log entry, and Sunday `/weekly-review` — but **not provisioned**. Turning on unattended agents that consume recurring Pro-plan usage needs an explicit go-ahead, separate from writing this plan.
## Implementation Status
Verified against live vault files and `git log` on 2026-07-27, corrected once by direct instruction mid-session. Not a self-report.
| Track | Status |
|---|---|
| Daily floor (LeetCode, ML spine, friction log) | Never ran — [[LeetCode & CSCI 4041]]'s tracker has zero rows all summer; the CSCI 2033 progress table sits at 0/14 |
| **TradingView** | Backend is real: ingestion pipeline, a landed strategy pack through a four-gate harness, an AI Analyst/Critic loop merged to `main` (PR #4, 497 tests passing). UI spec locked 2026-07-26, zero UI code yet. Not demo-eligible — the OOS gate correctly failed closed on thin history |
| **Portfolio** | Deployed. `BUILD-STATUS.md`'s 14-item UI-fix list is the live backlog; Orby upgrade is next after it closes |
| **CausalOps** | Most finished project — memory layer implementation complete, two steps from done: run the Supabase SQL migration, run the integration tests |
| **internship-research-loop** | Step 1 (Find) live and independently re-verified twice. Steps 2–9 exercised exactly once (the Appian promotion, 2026-07-26). Count-limit throttle designed, not shipped (`run_pipeline.py:66`) |
| **Arc** | Planning docs exist but don't count as a real scope — no code |
| **Jarvis** | Skills/agents/dashboards built, not run daily this past month |
| MATH 2230 + HIST 1103 | Complete |
| Certifications, system design, trading knowledge, Git exam | All at zero going into W0 |
## Current Progress
Living section — append a dated line here after each Sunday `/weekly-review`, don't rewrite the table above. Do not let this section go silent; a missing week here is the same signal as a missing daily-floor checkbox.
- 2026-07-27: baseline set. Table above is the starting state.
## Update Protocol
This note's `updated:` field bumps every Sunday during `/weekly-review`, and immediately whenever a flagship in the Timeframe table closes or changes. If two Sundays pass with no edit to Current Progress, that's a Never Miss Twice trigger per [[Anti-Drift Rules]] — treat the plan itself as a missed rep, not just the daily floor. Full review against the Goal's metric on 2026-08-31, written as a new dated entry in `60_Claude/50_Reviews/`, not by rewriting this file's history.
