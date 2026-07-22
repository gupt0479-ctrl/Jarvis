---
type: project
status: active
created: 2026-07-22
updated: 2026-07-22
deadline:
related_progress:
  - "[[adx — Source Claims]]"
  - "[[Mentor Details]]"
tags:
  - "#progress"
next: "Read the adx-core and adx-gate package source against the claims in [[adx — Source Claims]] and flag any mismatch before the next mentor conversation."
---
# adx — MOC (Agentic Developer Experience)
=="adx" is meta-tooling — not an agent itself — that scores how "agent-ready" a codebase is, runs agent tasks inside an isolated harness, and gates every resulting diff behind a 3-layer check plus a mandatory human sign-off recorded on a 7-level Agency Ladder.==
## Goal
Understand adx deeply enough — usage, mechanism, gaps, competitive position — to give Ahnaf a genuinely useful third-person review, not a surface-level "looks good" pass.
## What Is adx
Per [[adx — Source Claims]], adx structures the human/agent relationship across three pillars: **Measure** (`adx audit/shape/sweep` → four vitals — TDS, FRR, BER, HDI — combined into one 0–100 score), **Orchestrate** (`adx init/run/maintain` → scaffolds `AGENTS.md`/`llms.txt`/agent specs, runs tasks in an isolated git worktree with test verification after every iteration), **Govern** (`adx gate` → abstraction check + mutation testing + intent cross-reference, then a forced Agency Ladder sign-off before merge, writing a committed evidence bundle).
The idea doing the real conceptual work is the **Agency Ladder**, not the vitals or the gate mechanics. Everything else exists to push a team's sign-offs from the "rubber-stamp" levels (1–2) toward genuine ownership (Level 6) without pretending a human can line-by-line review everything an agent writes. Strip away the CLI and the vitals math, and the ladder alone is still a usable review rubric.
Distributed as a global npm CLI (`adx`) wrapping a TypeScript monorepo of 8 packages; integrates with Claude Code, GitHub Copilot Agent mode, and Cursor by generating IDE-specific agent spec files and registering an MCP server that exposes 6 of its tools directly inside those agents.
## How To Use It
Documented sequence: `adx init` (scaffold) → fill in the generated `llms.txt` skeleton (named as the single most important post-init step) → `adx audit` (baseline score) → `adx maintain install` (turn on frozen-path protection for sensitive directories) → `adx run "<task>" --exec <agent> --done "<verifiable condition>"` (execute agent work inside an isolated worktree) → `adx gate` (3-layer check + forced sign-off) before merge → wire `adx sweep` / `adx gate --dry-run` / `adx audit --ci` into CI.
Two distinct modes worth distinguishing when explaining this to someone new: **plan mode** (`adx run --plan` just assembles context into a task file for manual handoff to any IDE agent) versus **exec mode** (`--exec claude` actually drives the agent end-to-end). Plan mode is the safer onramp for a team not ready to hand over full autonomy yet — worth leading with when pitching this internally.
## Problem It Solves — Summary
In one line: as more code gets agent-written, review degrades into rubber-stamping ("comprehension debt") faster than teams notice, and agents produce architectural bloat and dark code at a rate humans wouldn't tolerate, because agents don't feel the maintenance pain that would normally stop it. The full problem statement, in adx's own words and structure, lives in [[adx — Source Claims]] — see its "Govern — The Loop Boundary Gate" and "Concepts — The Agency Ladder" sections specifically.
## Competitive Read
No single competitor combines all three pillars — that combination, not any one piece, is adx's actual claim to novelty:
- **Static analysis / code quality tools** (SonarQube, CodeClimate) — measure quality generically; no concept of token cost or file-revisit cost to an LLM reader, no governance ledger
- **Agent orchestration frameworks** (Aider, OpenHands, SWE-agent, Devin) — own the execution loop, sometimes worktree isolation, but ship no measurement vitals and no accountability ledger
- **AI code review tools** (CodeRabbit, Greptile, Graphite's reviewer) — automate review commentary, but don't force an explicit agency-level declaration or maintain a signed, committed audit trail
- **Mutation testing tools** (Stryker, PIT) — adx's Layer 2 is a direct, narrower reuse of this established technique, repointed specifically at catching agent-written tautological tests
- **`llms.txt` / `AGENTS.md`** — these are open conventions adx adopts and operationalizes, not things it invented; worth being precise about this with Ahnaf, since the README's phrasing could read as claiming more originality than it has
The real open question — not a competitor gap, a positioning gap — is whether the three-pillar bundle earns its adoption friction against picking three best-of-breed point tools instead. Nothing in the docs argues this directly.
## Documentation Gaps — My Read
Full factual list lives in [[adx — Source Claims]] § Open Questions. Two are worth raising directly with Ahnaf because they're cheap, concrete, and independently verifiable:
- **`adx ratchet` has no reference page.** It's named on the homepage and exposed as an MCP tool (`adx_ratchet`), but unlike every other command it has no usage/options page. Either ship the page or stop presenting it as a first-class command alongside audit/shape/sweep/init/run/maintain/gate.
- **Evidence bundle rotation is a self-acknowledged unsolved gap** — the docs say so outright. This is the single highest-leverage thing to build next: BER carries 30% of the composite score and depends entirely on `.evidence/` staying committed and not spiraling in size.
Everything else (taste-deficit scoring left unexplained, MCP tool schemas undocumented, the vscode extension having zero docs coverage, no stated rationale for the vital weights) is real but lower-urgency — it reads as "the docs haven't caught up to the product" rather than "the product has a hole."
## What Would Make It Extremely Useful
Ranked by leverage:
1. Ship the bundle-rotation solution — the one gap adx admits to itself
2. Publish the `adx ratchet` reference page — cheapest fix, highest advertised-vs-documented mismatch
3. One real before/after case study repo (ADX score 40 → 85 across actual commits) — every command page currently shows only synthetic sample output; this is the biggest credibility gap for a skeptical adopter evaluating whether to install it
4. State the weight-tuning rationale (30/25/30/15 vitals, 8% abstraction threshold) — even "these are opinionated defaults, not empirically derived" beats silence
5. Resolve whether adx primarily wants to be a product, a framework, or a methodology — `adx-core`'s `createAgenticSystem()` is framework-shaped, the CLI is product-shaped, and the Agency Ladder is adoptable as pure methodology with zero tooling installed; the docs read as all three at once without ever picking one
## Open Questions
- [ ] Is adx meant to be adopted whole, or is the Agency Ladder useful standalone without any of the CLI tooling? Worth asking Ahnaf directly — it changes how a reviewer should frame the pitch
- [ ] Are the vital weights (30/25/30/15) and the 8% abstraction threshold tuned against real repos, or reasonable-sounding defaults he chose?
- [ ] Is JS/TS-only a permanent scope decision, or just "haven't gotten to other ecosystems yet"?
- [ ] Has this run against a real team's repo yet, or is it still pre-adoption / solo-dogfooded? The badge on adx's own README scoring itself is the only usage evidence visible from outside the project
## Next Action
Read the `adx-core` and `adx-gate` package source in the GitHub repo against the claims captured in [[adx — Source Claims]] and flag any place the implementation doesn't match what the docs promise.
## Log
- **2026-07-22:** Read the full docs site (14 pages, verified against the live Astro sidebar config in the repo) and the GitHub README end to end; wrote [[adx — Source Claims]] and this MOC. Codebase not yet reviewed — that's the next session.
