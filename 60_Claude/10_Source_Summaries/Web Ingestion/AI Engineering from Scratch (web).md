---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]"
source_url: https://aiengineeringfromscratch.com/
source_note: "[[AI Engineering from Scratch.md]]"
input_kind: web
track: ai
---
# AI Engineering from Scratch — Summary
**Source:** `60_Claude/05_Clippings/Web/AI Engineering from Scratch.md` (aiengineeringfromscratch.com)
**Ingested:** 2026-07-04
**Pages:** landing page (thin — see note)
> [!NOTE] This is a discovery record, not a full ingestion. The clip is the site's landing page — the actual 503 lessons live in the GitHub repo, not the clip. Captured: what the resource is and why it's worth the repo link.
## Source
A **free, open-source AI-engineering curriculum** by rohitg00 that builds every core algorithm by hand — **503 lessons, 20 phases, four languages (Python, TypeScript, Rust, Julia)**, from linear algebra to autonomous swarms. Repo: `github.com/rohitg00/ai-engineering-from-scratch`.
## Key Claims
- ==Most AI material teaches in scattered pieces that never line up — "you ship a chatbot but can't explain its loss curve"; this curriculum is the spine==
- Every algorithm is **built from raw math first** (backprop, tokenizer, attention, agent loop) — "by the time PyTorch shows up, you already know what it's doing under the hood"
- Each lesson runs the same loop: **read the problem → derive the math → write the code → run the test → keep the artifact** — no videos, no copy-paste deploys, runs on your own laptop
- Free, open source, no paywall or signup; language chosen per concept
## Why It Matters
This is a from-scratch complement to the course/resource stack in [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] (which lists Karpathy's Zero-to-Hero for the same "build the transformer by hand" purpose). The "derive → code → test → keep the artifact" loop matches the vault's own learning-agent proof-artifact philosophy and the [[ML Fundamentals (2033 + 2230)]] "output per session" rule. Worth bookmarking as a self-paced backbone, but 503 lessons is a multi-year commitment — pick phases that fill a specific gap (attention, agent loop) rather than treating it as a linear must-finish.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/Web/AI Engineering from Scratch.md`
- Repo: `github.com/rohitg00/ai-engineering-from-scratch`
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — the broader roadmap this fits into
- [[ML Fundamentals (2033 + 2230)]] — the vault's own from-fundamentals ML track
## Open Questions
- [ ] Which specific phases (attention? agent loop?) fill a real gap vs what CSCI 2033/coursework already covers?
- [ ] Is the repo active/maintained, or a one-time drop?
## Flashcards
#cards/ai
What is the pedagogical bet of "AI Engineering from Scratch"?::Build every algorithm **from raw math first** (backprop, tokenizer, attention, agent loop) so that when frameworks like PyTorch appear you already understand what they do underneath — 503 lessons across Python/TS/Rust/Julia.
