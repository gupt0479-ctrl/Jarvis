---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - evergreen
  - ai
notes:
  - "[[Hermes Agent — Trading & Alert System (Distilled)]]"
  - "[[Internship Pipeline]]"
next:
---
# Hermes Agent Framework — Corrected Framing
## The Correction
"Hermes" isn't an installable app or product with a dashboard — [[00_Execution]] checked the actual source it was distilled from ([[4 Ways to Make Money with the Hermes Agent (web)]]) and found it's **zachdoesai's branding for a generic framework**: treat an agent as a junior operator, attach it to a function people already pay for, sell the outcome rather than the method. The framework spans four plays — Sales, Content, Research, Monitoring. Only Play 4 (Markets/monitoring) got distilled into [[Hermes Agent — Trading & Alert System (Distilled)]]; the other three generalize to any domain, not just trading.
## The Real Finding: Three of Four Plays Already Run Here, Unlabeled
| Play | What It Is | Where It Already Runs |
|---|---|---|
| **Play 1 — Sales (lead-gen)** | Attach an agent to outreach, applied to a paying function | The Contacts/Mimic.md draft-and-track system in [[Internship Pipeline#Step 4 — Reach Out (Contacts)]] — applied to recruiters instead of customers |
| **Play 2 — Content** | Attach an agent to content generation and reporting | **No equivalent anywhere in the vault** — see below |
| **Play 3 — Research** | Attach an agent to information-gathering | `internship-research-loop` (hourly GitHub Actions, per [[Internship Pipeline#Step 1 Is Automated — Steps 2+ Are Manual By Design]]) — applied to job postings instead of markets |
| **Play 4 — Monitoring** | Attach an agent to watching for signal | Same `internship-research-loop` — the monitoring half of the same system |
## The One Real Gap: Play 2 (Content)
No content-generation-and-reporting agent exists anywhere in this vault yet. The closest open slot, per [[00_Execution]]: the report-generation step of [[PDF's Ingestion Implementation#Knowledge Gathering & Intelligence Automation System (10% of Work Needed) - BUILD|Knowledge Gathering & Intelligence Automation]]'s aggregate → synthesize → auto-file reports design. If a fourth Hermes-style application ever gets picked, Content is the nameable gap — not a new build queued now, just the one slot that's actually empty.
## Direct Answer
No new "Hermes" build is needed. The pattern is already in daily use under different names (`internship-research-loop`, Contacts/Mimic.md) — this note exists so that fact is legible instead of scattered across two different pipeline notes that don't reference each other or the Hermes framing.
## Evidence
- [[Hermes Agent — Trading & Alert System (Distilled)]] — the Play 4 distillation
- [[60_Claude/10_Source_Summaries/Web Ingestion/4 Ways to Make Money with the Hermes Agent (web)]] — the source this corrects against
- [[Internship Pipeline]] — Steps 1 and 4, where Plays 1/3/4 already run
- [[PDF's Ingestion Implementation#Knowledge Gathering & Intelligence Automation System (10% of Work Needed) - BUILD|Knowledge Gathering & Intelligence Automation]] — the closest open slot for Play 2
- [[00_Execution]] — the resolved finding this note carries forward
