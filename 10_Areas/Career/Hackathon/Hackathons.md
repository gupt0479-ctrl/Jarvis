---
type: evergreen
status: tree
created: 2026-01-14
updated: 2026-07-29
tags:
  - evergreen
  - hackathon
  - career
notes:
  - "[[Ultimate Guide to Winning Hackathons (PDF)]]"
  - "[[Hall of Hacks — Winning Hackathon Patterns Analysis]]"
  - "[[Engineer Edge Roadmap]]"
next: "Register for the next Lablab.ai AI hackathon (2-4 weeks out) and scope 3 ideas against it"
---
# Hackathons
Guide: ![[Ultimate Guide to Winning Hackathons.pdf]]
==Winning a hackathon is 70% planning and presentation, 30% code — a judge-validated project beats three months of solo building, and this note is the actual playbook, not a stub pointing at the PDF.== Distilled from [[Ultimate Guide to Winning Hackathons (PDF)]] plus [[Hall of Hacks — Winning Hackathon Patterns Analysis]] (50+ winning projects from 2024-2025 analyzed), per [[PDF's Ingestion Implementation#HACKATHON TRACK: Ultimate Guide to Winning Hackathons + Web Research Integration|the HACKATHON TRACK synthesis]] and [[00_Execution]]. Portfolio value is real: a hackathon win carries 25% interview weight vs. 20% for a solo project, per [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — judge-validated credibility instead of self-reported.
## Judge-Credibility Ranking (Pick Your Hackathon By This)
Hackathon selection is 20% of winning probability — a B-tier project at a prestigious hackathon beats an A-tier project at a low-prestige one, because judges' own credibility becomes part of the portfolio signal.
1. **Lablab.ai AI Hackathons** (monthly, online) — **recommended first.** Judge credibility: A (growing pool of industry AI engineers). 50-150 teams, no travel, AI-focused — matches the career pivot direction and is the easiest real win to validate the whole approach before spending on a premium event.
2. **HackHarvard / Hack the North / YCombinator Startup School** — Tier-1 prestige. Judge credibility: S (YC partners, top VCs). 300-400+ teams, very hard to win, but a win here carries investor interest and job inquiries. Travel cost (~$250-300 for HackHarvard).
3. **Specialized (Hugging Face, MLOps.community)** — mid-tier credibility, narrower judge pool, good for a second win once the format is proven.
4. **Local university / online-only** — lowest credibility signal; fine for practice reps, not for the portfolio bullet.
**Sequencing:** Lablab.ai first (build confidence, validate the workflow), then HackHarvard or YC once the 24-hour build muscle is proven.
## The Meta-Pattern (From 50+ Winning Projects)
1. **Problem clarity beats complexity** — "Debugging LLM prompts takes 2h; we cut it to 5 min" beats a vague "AI tool" pitch.
2. **Demo beats slides** — a working live demo is a 30-50% score bump over slides alone.
3. **Team size 2-4 is the sweet spot** — each person owns a clear feature; judges see professional division of labor.
4. **Boring tech wins; trendy tech loses** — React + Python + FastAPI + Supabase (judges recognize it instantly) beats Rust/Elixir/a custom stack judges have to parse cold.
5. **AI/LLM projects are 40-50% of winners** right now — lowest barrier to entry, judges are primed to reward it.
## Pre-Hackathon Checklist (48 Hours Before — Highest ROI, 4-5 Hours Total)
1. **Track selection (1h)** — list every sponsor + track + prize + rubric; rank by (your skill match) × (rubric weight fit); research the *previous winner* in that track and calibrate 3 ideas against that pattern.
2. **Judge booth validation (30min, ~18h before)** — pitch all 3 ideas to the judge scoring your track in 30 seconds each; build whichever gets "oh that's cool," not "we see that every year." This gives the judge stakes in your project before you've built anything.
3. **API pre-prep (2h)** — for every API you'll touch, read the docs, write 3 test calls, build minimal boilerplate. This is 90 minutes of debugging you don't do at 2am during the hack.
4. **Rubric-to-slides pre-mapping (1h)** — if judging is Innovation 30% / Impact 30% / Tech 20% / Execution 20%, pre-write one slide bullet per criterion now, while you're not exhausted.
5. **Team role clarity (30min, before kickoff)** — assign explicit owners (backend/API, frontend/UI, demo/presentation); document the integration point and who's primary for debugging each piece.
## The 24-Hour Build Workflow
| Hour | Frontend | Backend | Product | AI |
|---|---|---|---|---|
| 0-2 | v0 scaffold test | API test | Confirm scope | Test 5 prompt variants |
| 2-6 | Build real UI | Build API routes | Demo narration | Prompt iteration |
| 6-10 | Polish demo flow | Deploy + connect | Cut scope if behind | Fine-tune behavior |
| 10-12 | Rehearsal x5 | Stress test | Rehearsal x5 | Rehearsal |
| 12-18 | Sleep (6h) | Sleep | Sleep | Sleep |
| 18-24 | Final rehearsal x2 | Final check | Final rehearsal x2 | Final check |
**Ruthless scoping rule:** two features done perfectly beats five features half-baked — judges score execution, not feature count. Deploy MVP by hour 6; if a feature is behind schedule at hour 10, cut it rather than ship it broken.
## The Four-Slide Rubric-Aligned Deck
- **Slide 1 — Problem + Vision** → demonstrates Innovation
- **Slide 2 — Live demo, ≤90 seconds** → demonstrates Execution + Impact
- **Slide 3 — Tech & Architecture** → demonstrates Technical Quality
- **Slide 4 — Call-to-Action** → demonstrates Pitch Skills
**Demo script (90 sec, timed, rehearse 10+ times):** 0-10s hook (one-sentence problem statement) → 10-30s live demo (3 clicks max: login, core feature, result) → 30-70s explain (how it works, why it matters, what's different) → 70-85s quantified value ("saves X hours/week" — numbers stick) → 85-90s specific ask ("mentorship on [specific problem]" or "interested in production"). Always have a Loom video backup — a crash hurts, a backup plus confidence recovers it.
> [!WARNING]
> Anti-patterns confirmed across 50+ projects: over-scoped MVP (30% of 5 features reads as "incomplete," not ambitious), no live demo (judges imagine the worst), a vague problem statement ("we made an AI tool" loses to a quantified one), wrong tech for the judge pool, and a tired presenter from last-minute coding instead of rehearsal.
## Post-Hackathon (Win or Lose — Document Within a Week)
- Case study: problem → solution → quantified results
- Loom walkthrough (2-3 min): live demo + why it won or lost
- Clean GitHub repo: README, deployment instructions, boilerplate comments removed
- Social proof: LinkedIn post (tag the hackathon/judges if they engaged), thank-you email to judges with the deployed link
- Resume bullet via [[Resume Tailoring, LinkedIn Search & Outreach Discovery|the MavGPT prompt sequence]] — lead with "Won [Hackathon]" and the judge credential, not "built X over a weekend." **The judge credibility is 50% of the portfolio signal.**
## Postmortem Template (Apply To Every Project Going Forward)
Each hackathon project note under `20_Progress/Projects/CS/Hackathons/` should carry two sections once the event ends — added by heading to the existing project file, not a separate folder structure:
- **`## Case Study`** — problem, solution, result, one quantified number.
- **`## Lessons Learned`** — what worked, what didn't, judged against the meta-pattern above.
See [[Vibe Coding Hackathon]] for the first project this postmortem structure was applied to.
## Evidence
- [[Ultimate Guide to Winning Hackathons (PDF)]]
- [[Hall of Hacks — Winning Hackathon Patterns Analysis]]
- [[60_Claude/05_Clippings/Web/the permanent archive of winning hackathon projects]]
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — the 20%/25% interview-weight comparison
- [[00_Execution]] — the resolved verdict this note executes
