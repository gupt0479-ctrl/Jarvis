---
type: project
status: active
created: 2026-08-07
updated: 2026-08-07
deadline:
related_progress:
  - "[[Codebase Deep Read]]"
  - "[[adx]]"
  - "[[Distribution and Adoption Gaps]]"
tags:
  - "#progress"
next: Decide whether to update adx.md's Competitive Read section with this, and scope the single Factory-comparison GitHub issue.
---
# adx — Competitive Positioning
==Factory AI's "Agent Readiness" is a sharper, more granular measurement tool than adx's four vitals — but it doesn't compete with adx's Agency Ladder at all, because it doesn't attempt the accountability problem. And its own published methodology has the same undisclosed-validation gap this review found in adx's abstraction.ts.==
## What This Note Corrects From Its Own Prior Version
The earlier version of this note recorded a scoping decision without research behind it, by design — flagged honestly at the time. This version replaces that with real, independently sourced findings. Two things from the original framing didn't survive contact with actual research, and are corrected below rather than quietly dropped.
## Key Claims
- **Factory's Agent Readiness measures codebase quality across 9 pillars and 5 maturity levels** (Style & Validation, Build System, Testing, Documentation, Dev Environment, Debugging & Observability, Security, Task Discovery, Product & Experimentation) — more granular and more explicitly structured than adx's four vitals (TDS/FRR/BER/HDI).
- **Factory has no accountability, sign-off, or audit-ledger mechanism anywhere in its product line** — checked both Agent Readiness and the Droid code-review product directly. This is the correction to the framing: Factory isn't "better" at the thing adx's Agency Ladder does. It doesn't attempt that problem at all.
- **Factory's own published methodology has an undisclosed-validation gap that closely parallels adx's uncited 7–8%/34% claim** — the only empirical number Factory discloses (variance dropping from 7% to 0.6% across 9 benchmark repos) is about scoring *reproducibility*, not whether higher scores predict better agent outcomes. Neither company publishes evidence that its scoring criteria causally improve agent performance.
- **Factory's Droid product does have a real, working permission model** — "autonomy levels" from fully-supervised to full-autonomy, gating what the agent can do before it acts. This is a genuinely different mechanism from adx's Agency Ladder: a runtime permission gate (what you're allowed to do) versus a retrospective accountability record (what level of human understanding was certified after the fact). Worth being precise about this distinction with Ahnaf — they solve adjacent but different problems.
## Full Content
### The comparison that holds up
==adx bundles measurement and governance into one tool; Factory keeps them separate and doesn't claim to solve governance at all — and the governance half of adx's bundle is the half proven non-functional in [[Safety-Critical Gaps]].==
This is the sharper, defensible version of "adx's real differentiator is currently faked": it's not that a competitor does accountability better. It's that adx claims to do *both* measurement and accountability, and only the measurement half has any live competitor doing it more rigorously (Factory's 9-pillar, 100+-signal Agent Readiness vs. adx's four vitals) — while the accountability half, which no other tool in this space appears to attempt, is the part [[Safety-Critical Gaps]] shows doesn't actually require human input in CI, hardcodes `signedBy: 'engineer'`, and is unaffected by every config variation tested.
### The comparison that doesn't hold up as stated
==Factory does not have a working accountability ledger to point to as superior — it simply doesn't compete in that category, on either of its two relevant products.==
Checked directly: Factory's Agent Readiness docs describe no approval workflow, sign-off tracking, or historical ledger — "purely diagnostic rather than governance-oriented." Factory's Droid code-review docs describe an operational review flow (inline comments, an approval action) with no persistent audit mechanism of its own; any record that exists is incidental to GitHub's native PR history, not a designed feature. Neither product has anything resembling adx's `.adx/state/adx-agency.json` ledger or the Agency Ladder's 7-level scale. This means the original framing — "Factory validates against real telemetry, adx doesn't" — needs a real correction, not just softening: Factory's own announcement discloses no study, dataset, or telemetry linking its readiness scores to actual agent-success outcomes. The one number it publishes is about scoring consistency across repeated runs, not efficacy. Both companies assert that their scoring criteria matter; neither publishes evidence that they do.
### Sources
- [Agent Readiness Overview — Factory Documentation](https://docs.factory.ai/web/agent-readiness/overview) — the 9 pillars, 5 maturity levels, 80%-of-previous-level gating rule
- [Introducing Agent Readiness — Factory.ai](https://factory.ai/news/agent-readiness) — the only disclosed empirical number (7%→0.6% variance across 9 benchmark repos), and the absence of outcome-validation data
- [Automated Code Review — Factory Documentation](https://docs.factory.ai/guides/droid-exec/code-review) — Droid's review flow, no persistent audit mechanism described
- Factory AI multi-agent platform reviews (secondary, for the autonomy-levels/permission-model description): [Factory AI Platform Review](https://www.digitalapplied.com/blog/factory-ai-multi-agent-coding-platform-review)
## Why It Matters
This is close to being the sharpest available comparison for the mentor conversation, and it's sharper *with* the correction than the original framing was without it: telling Ahnaf "Factory validates its numbers and you don't" would be wrong and checkable-as-wrong in about ten minutes. Telling him "no one in this space — including Factory — publishes evidence that their scoring predicts real agent outcomes, and your specific abstraction-overhead numbers are exactly as uncited as theirs, but your Agency Ladder is trying to solve a problem Factory doesn't even attempt" is accurate, sourced, and more useful to him.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[Safety-Critical Gaps]] — the evidence behind "the accountability half doesn't work"
- [[Distribution and Adoption Gaps]] — the direct parallel: adx's own uncited quantitative claim, checked the same way Factory's was here
- [[adx]] — its "Competitive Read" section currently doesn't mention Factory AI or CodeScene at all; this note is the candidate content for adding Factory
## Open Questions
- [ ] Should [[adx]]'s Competitive Read section be updated with this now, or held until after the mentor conversation in case the framing changes based on what Ahnaf says?
- [ ] Is the permission-gate vs. accountability-ledger distinction (Droid's autonomy levels vs. adx's Agency Ladder) worth its own follow-up — they're different enough mechanisms that "adx's ladder is better" isn't automatically true just because Factory doesn't have one.
