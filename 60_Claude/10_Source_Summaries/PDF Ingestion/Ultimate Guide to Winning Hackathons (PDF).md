---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[07 - Projects & Hackathons Queue]]"
  - "[[Hall of Hacks — Winning Hackathon Archive (web)]]"
source_url: 60_Claude/05_Clippings/PDFs/Ultimate Guide to Winning Hackathons.pdf
source_note: "[[Ultimate Guide to Winning Hackathons.pdf]]"
input_kind: pdf
track: career
---
# Ultimate Guide to Winning Hackathons — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Ultimate Guide to Winning Hackathons.pdf`
**Ingested:** 2026-07-04
**Pages:** 4
## Source
A tactical how-to for winning college hackathons (author claims never having lost one) — prep, team, build workflow, AI use, presentation, and judge-proofing. Complements [[Hall of Hacks — Winning Hackathon Archive (web)]] (which is the *what won*; this is the *how to win*).
## Key Claims
- ==Validate the idea with the judge-in-the-booth *before* building — pitch your shortlist to the sponsor booth and build whichever concept excites the person who'll be scoring you== (instant validation from the dude giving the prize)
- **Map slides directly to the rubric** — if scoring is Innovation 30% / Impact 30% / Tech 20% / Demo 20%, make one slide or spoken beat per criterion
- **Live demo > slide deck**, with a click path Login → key feature → wow moment ≤90 sec, and a pre-recorded Loom backup in case the live demo breaks
- **Quantify impact** ("saves SMBs 5 hrs/week and $12k/yr — numbers stick") and **close with the ask** (mentorship + the specific prize to pilot with N beta users)
- Solo strategy: prioritize **pitch + backend scaffolding**, lean on v0 for UI — a polished presentation is impressive when solo
## Full Content
1. **Pre-prep (48–24h before):** pick a track early (rank by interest × sponsor prize × judging-criteria weight); brainstorm 2–3 ideas/track with ChatGPT/Perplexity then converge on top 3 with clear problem→solution→impact; **validate at sponsor booths**; read every API doc you'll touch and prep sample Postman calls so integration doesn't eat build time.
2. **Balanced team:** Product lead/pitcher (Docs/Keynote/Loom), Frontend (Next.js + Tailwind + v0), Backend/DevOps (Express + Supabase + Vercel), ML/AI wrapper (OpenAI + Perplexity/Gemini). No blockers, no overlap.
3. **Lightning build (0–12h):** scaffold UI with v0 from the fleshed-out idea → open the repo in Cursor and let it index 5 min before natural-language queries → backend in one shot (Supabase SQL schema → paste types → ask Cursor for Express routes) → **one flagship sponsor integration** that demos well. Target: MVP deployed in ≤5h so you can polish and rehearse.
4. **AI smarter than everyone:** prompt engineering 101 — assign a clear role, state the goal, define the output format ("valid code, no commentary"), use few-shot / chain-of-thought for complex tasks.
5. **Presentation (last 2h):** map slides to rubric bullets; hook the room (15-sec story or live poll); live demo with Loom backup; quantify impact; close with the ask.
6. **Judge-proofing:** explain the tech simply (simplicity signals real understanding), articulate the value clearly, name-drop the sponsor API in the first minute, leave 30 sec for Q&A and repeat each question before answering.
## Why It Matters
Directly operational for the Saturday hackathon slot and the AWS+Vercel hackathon in [[07 - Projects & Hackathons Queue]]. The highest-leverage, least-obvious move is **booth-validating with the actual judge before building** — it turns a guess into a near-guaranteed rubric fit. The rubric-mapping + quantified-impact + close-with-the-ask presentation structure is reusable well beyond hackathons (it's the same "lead with a number" discipline as the BASWE portfolio-project case studies). Pairs with the archive note: study what won there, execute how here.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Ultimate Guide to Winning Hackathons.pdf`
- [[07 - Projects & Hackathons Queue]] — the hackathon lane
- [[Hall of Hacks — Winning Hackathon Archive (web)]] — the "what won" companion
## Open Questions
- [ ] For the next hackathon, pre-write the rubric→slide map and the ≤90-sec demo click-path before the event?
## Flashcards
#cards/career
What's the single highest-leverage pre-hackathon move in this guide?::**Validate your shortlist at the sponsor booth before building** — pitch the judge-in-the-booth and build whatever excites the person who'll score you (instant rubric-fit validation).
How should a hackathon presentation be structured?::**Map slides directly to the rubric** (one beat per weighted criterion), lead with a **live demo** (Login → key feature → wow ≤90 sec, Loom backup), **quantify impact** with numbers, and **close with the ask**.
