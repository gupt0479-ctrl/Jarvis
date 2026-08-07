---
type: project
status: active
created: 2026-08-07
updated: 2026-08-07
deadline:
related_progress:
  - "[[Codebase Deep Read]]"
  - "[[adx]]"
tags:
  - "#progress"
next: Capture the actual Factory AI comparison into Jarvis before scoping the positioning GitHub issue.
---
# adx — Competitive Positioning
==This note is intentionally thin. It records a scoping decision, not a comparison — the comparison itself hasn't been done inside this vault yet.==
## What's Actually Established Here
Two things, both from direction given mid-review, not from research done in this pass:
1. **Factory AI, not CodeScene, is the right competitor to bring to Ahnaf** for the "adx's real differentiator — the Agency Ladder / accountability layer — is currently the thing that's faked" framing (see [[Safety-Critical Gaps]] for the CI-auto-approve and hardcoded-`signedBy` findings that framing rests on).
2. **The eventual GitHub issue set should keep exactly one issue scoped to this Factory-comparison/positioning angle, separate from the concrete bug-fix issues.** Don't fold this into a bug-fix issue or split it across several later.
## What's Missing
The substance of the Factory AI comparison — what Factory AI actually does, specifically how it handles the accountability/sign-off problem, and exactly where it's sharper than adx's current implementation — isn't captured anywhere in this session's research. `adx.md`'s existing "Competitive Read" section covers SonarQube/CodeClimate, Aider/OpenHands/SWE-agent/Devin, CodeRabbit/Greptile/Graphite, Stryker/PIT, and `llms.txt`/`AGENTS.md` — it doesn't mention Factory AI or CodeScene at all.
This note exists so the decision isn't lost, not to stand in for the research. Writing the actual comparison — and updating `adx.md`'s Competitive Read section with it — is separate follow-up work.
## Why It Matters
The single sharpest insight available for the mentor conversation is exactly the kind of claim that needs a real source behind it before it goes in front of Ahnaf: "adx's one differentiator is currently faked" is backed by hard evidence in [[Safety-Critical Gaps]]; "Factory AI does this better" isn't yet, in this vault.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[adx]] — its "Competitive Read" section is where the real comparison belongs once it exists
- [[Safety-Critical Gaps]] — the evidence behind the "currently faked" half of the framing
## Open Questions
- [ ] What does Factory AI actually do differently on the accountability/sign-off problem — worth a dedicated research pass before this becomes a GitHub issue.
- [ ] Should `adx.md`'s Competitive Read section be updated to include Factory AI once that research exists, given it's currently silent on both Factory AI and CodeScene?
