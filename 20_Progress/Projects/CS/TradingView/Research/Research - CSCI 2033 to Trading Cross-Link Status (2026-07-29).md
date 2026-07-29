---
type: research
status: sprout
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[Trading Resources Integration — TradingView Architecture Roadmap]]"
tags:
  - trading
  - research
  - csci-2033
track:
  - trading
---
# Research — CSCI 2033 to Trading Cross-Link Status (2026-07-29)
**Purpose:** [[00_Execution]]'s [[PDF's Ingestion Implementation#TRADING BOT TRACK: Integrated Analysis (All Trading Resources) - ACTION|TRADING BOT TRACK]] verdict confirmed a real gap — zero links from `20_Progress/Degree/CSCI 2033/Concepts_old/Least Squares and Feature Engineering.md`, `Least Squares Classifiers, Optimization, and Gradient Descent.md`, or `ML_Foundations.md` to trading anywhere in the vault — and instructed: cross-link the concept to [[AI Market Analyzer - Product Spec]] and the matching MIT Bible section in [[Trading Resources Integration — TradingView Architecture Roadmap]] once OVB, ridge/lasso, or gradient descent "actually gets covered in CSCI 2033 this term." That instruction assumed CSCI 2033 is still an active current-term course. It isn't.
---
## The Correction
`20_Progress/Degree/CSCI 2033/CSCI 2033 Board.md` has `status: archived`, `created: 2025-11-20`, `updated: 2025-12-26` — Fall 2025. Every concept file checked (`Week - 12.md`, `Concepts_new/Week_11_to_13.md`, `Concepts_old/ML_Foundations.md`) confirms the same: `status: archived` or `status: complete`, all dated Nov–Dec 2025. **CSCI 2033 already finished, eight months before this pass ran.** There is no "this term" left to wait on — the course notes sitting in `20_Progress/Degree/` are a completed course that never got moved to `50_Archive/`, not an in-progress one.
This means least squares, ridge/lasso, gradient descent, and the OVB-adjacent regression material named in [[Trading Resources Integration — TradingView Architecture Roadmap]] were **already taught, months ago** — confirmed present in `Concepts_old/Least Squares and Feature Engineering.md` and `Concepts_old/Least Squares Classifiers, Optimization, and Gradient Descent.md` by title alone. The gap isn't "not taught yet." It's that the cross-link was never added retroactively once the course ended.
## Why This Note Doesn't Retroactively Edit Those Files
Two reasons, not one:
1. **Maturity.** [[AGENTS]]'s Golden Rule 4 says respect maturity and propose changes before modifying settled notes — `status: archived`/`complete` concept notes from a finished course are exactly that class of note, even though they technically still sit in `20_Progress/` instead of `50_Archive/`.
2. **The instruction's own conditional never actually fires again.** [[00_Execution]] said link "when… actually covered this term" — that condition was satisfied in the past, not now, and CSCI 2033 won't have another "this term" to trigger on. Silently forcing the link now would look like this pass invented a coincidence ("just happened to get taught this week") when the real fact is the course ended in December.
## What To Do Instead
If a cross-link to trading is still wanted for this already-taught material, it should be a **deliberate, explicit decision** — not an automatic trigger inferred from a stale "this term" condition. The concrete options, left open rather than decided here:
- Add the cross-link now, directly, treating "already taught" as satisfying the original intent even though the timing assumption was wrong.
- Wait until an equivalent concept resurfaces in a currently-active course (e.g. if a future term revisits regression/optimization) and link it there instead, leaving the Fall 2025 notes untouched.
- Skip the retroactive link entirely — the trading side already has its own math coverage via [[Trading Resources Integration — TradingView Architecture Roadmap]]'s MIT Bible sections, so CSCI 2033 was always a supplementary reference, not the load-bearing source.
## Evidence
- `20_Progress/Degree/CSCI 2033/CSCI 2033 Board.md` — `status: archived`, Fall 2025
- `20_Progress/Degree/CSCI 2033/Concepts_old/ML_Foundations.md`, `Week_11_to_13.md`, `Week - 12.md` — all `archived`/`complete`, Nov–Dec 2025
- [[Trading Resources Integration — TradingView Architecture Roadmap]] — the MIT Bible sections this would have linked to
- [[AI Market Analyzer - Product Spec]] — the product side of the intended cross-link
- [[00_Execution]] — the verdict this note corrects the premise of, without overturning the underlying decision (still no forced link before a deliberate choice is made)
