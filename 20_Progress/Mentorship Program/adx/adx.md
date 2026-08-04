---
type: project
status: active
created: 2026-07-22
updated: 2026-07-22
deadline:
related_progress:
  - "[[Source Claims]]"
  - "[[Claims vs Implementation]]"
  - "[[Recommended Fixes]]"
  - "[[Mentor Details]]"
tags:
  - "#progress"
next: Share [[adx — Recommended Fixes]] with Ahnaf and get his read on priority before recommending any of it upstream.
---
# adx — MOC (Agentic Developer Experience)
=="adx" is meta-tooling — not an agent itself — that scores how "agent-ready" a codebase is, runs agent tasks inside an isolated harness, and gates every resulting diff behind a 3-layer check plus a mandatory human sign-off recorded on a 7-level Agency Ladder.==
## Goal
Understand adx deeply enough — usage, mechanism, gaps, competitive position — to give Ahnaf a genuinely useful third-person review, not a surface-level "looks good" pass.
## What Is adx
Per [[Source Claims]], adx structures the human/agent relationship across three pillars: **Measure** (`adx audit/shape/sweep` → four vitals — TDS, FRR, BER, HDI — combined into one 0–100 score), **Orchestrate** (`adx init/run/maintain` → scaffolds `AGENTS.md`/`llms.txt`/agent specs, runs tasks in an isolated git worktree with test verification after every iteration), **Govern** (`adx gate` → abstraction check + mutation testing + intent cross-reference, then a forced Agency Ladder sign-off before merge, writing a committed evidence bundle).
The idea doing the real conceptual work is the **Agency Ladder**, not the vitals or the gate mechanics. Everything else exists to push a team's sign-offs from the "rubber-stamp" levels (1–2) toward genuine ownership (Level 6) without pretending a human can line-by-line review everything an agent writes. Strip away the CLI and the vitals math, and the ladder alone is still a usable review rubric.
Distributed as a global npm CLI (`adx`) wrapping a TypeScript monorepo of 8 packages; integrates with Claude Code, GitHub Copilot Agent mode, and Cursor by generating IDE-specific agent spec files and registering an MCP server that exposes 6 of its tools directly inside those agents.
## How To Use It
Documented sequence: `adx init` (scaffold) → fill in the generated `llms.txt` skeleton (named as the single most important post-init step) → `adx audit` (baseline score) → `adx maintain install` (turn on frozen-path protection for sensitive directories) → `adx run "<task>" --exec <agent> --done "<verifiable condition>"` (execute agent work inside an isolated worktree) → `adx gate` (3-layer check + forced sign-off) before merge → wire `adx sweep` / `adx gate --dry-run` / `adx audit --ci` into CI.
Two distinct modes worth distinguishing when explaining this to someone new: **plan mode** (`adx run --plan` just assembles context into a task file for manual handoff to any IDE agent) versus **exec mode** (`--exec claude` actually drives the agent end-to-end). Plan mode is the safer onramp for a team not ready to hand over full autonomy yet — worth leading with when pitching this internally.
## Problem It Solves — Summary
In one line: as more code gets agent-written, review degrades into rubber-stamping ("comprehension debt") faster than teams notice, and agents produce architectural bloat and dark code at a rate humans wouldn't tolerate, because agents don't feel the maintenance pain that would normally stop it. The full problem statement, in adx's own words and structure, lives in [[Source Claims]] — see its "Govern — The Loop Boundary Gate" and "Concepts — The Agency Ladder" sections specifically.
## Competitive Read
No single competitor combines all three pillars — that combination, not any one piece, is adx's actual claim to novelty:
- **Static analysis / code quality tools** (SonarQube, CodeClimate) — measure quality generically; no concept of token cost or file-revisit cost to an LLM reader, no governance ledger
- **Agent orchestration frameworks** (Aider, OpenHands, SWE-agent, Devin) — own the execution loop, sometimes worktree isolation, but ship no measurement vitals and no accountability ledger
- **AI code review tools** (CodeRabbit, Greptile, Graphite's reviewer) — automate review commentary, but don't force an explicit agency-level declaration or maintain a signed, committed audit trail
- **Mutation testing tools** (Stryker, PIT) — adx's Layer 2 is a direct, narrower reuse of this established technique, repointed specifically at catching agent-written tautological tests
- **`llms.txt` / `AGENTS.md`** — these are open conventions adx adopts and operationalizes, not things it invented; worth being precise about this with Ahnaf, since the README's phrasing could read as claiming more originality than it has
The real open question — not a competitor gap, a positioning gap — is whether the three-pillar bundle earns its adoption friction against picking three best-of-breed point tools instead. Nothing in the docs argues this directly.
## Documentation Gaps — What Exists
The factual list of gaps as observed in the docs themselves lives in [[Source Claims]] § Open Questions (missing `adx ratchet` reference page, unexplained taste-deficit mechanism, undocumented MCP tool schemas, zero `adx-vscode` coverage, no stated rationale for the vital weights). Every one of those gaps, plus everything found by reading the actual code against those claims, is listed as an actionable item in [[Recommended Fixes]] — that note is where prioritization and "what to build next" judgment lives, not here.
## Verification Against The Codebase
Full line-level comparison lives in [[Claims vs Implementation]] — every claim in [[Source Claims]] checked directly against the actual package source (all 8 packages cloned and read, all 90 test cases counted, the single commit in the repo's history inspected). The website capture itself held up — nothing material was missed there. The gap is between what adx claims and what it does.
Three findings change the read on this product:
- **The core accountability claim doesn't survive contact with adx's own repository.** `.adx/state/adx-agency.json` — the "permanent record of human oversight" — has exactly one entry: Level 6 (Resolve), `"signedBy": "agent"`. Not a human. In CI mode `adx gate` auto-approves and stamps Level 6 with zero human input, and even in the interactive path `signedBy` is hardcoded to the literal string `'engineer'` — it never captures a real identity. The Agency Ladder exists specifically to catch this failure mode, and it shows up in the tool's own dogfooded history.
- **Two headline claims are false as stated.** "Import cycles always score 0" — a cyclic file actually gets a flat +0.5 risk bonus, not a forced floor, so one small cycle in a large codebase barely moves the aggregate FRR score. "Gate score below 60 blocks merge" — blocking is actually driven by three unrelated boolean triggers (abstraction flagged, any tautological test, more than 3 drifted files), independent of the numeric gate score entirely.
- **`adx sweep` has undocumented flags that delete code.** `--fix`, `--auto`, `--dry-run`, and `--comments` all exist and work — `--auto` batch-removes "orphaned" exports and dark comments across the repo with no confirmation prompt. None of the four appear anywhere on the docs site.
This also resolves the earlier open question below about JS/TS-only scope: `harness.observe.tests` already accepts `pytest` and a free-form `custom` + `testCommand`, so cross-language test execution is real today, just undocumented — not a permanent limitation.
## Open Questions
- [ ] Is adx meant to be adopted whole, or is the Agency Ladder useful standalone without any of the CLI tooling? Worth asking Ahnaf directly — it changes how a reviewer should frame the pitch
- [ ] Are the vital weights (30/25/30/15), the gate-score weights (40/40/20, undocumented anywhere), and the 8% abstraction threshold tuned against real repos, or reasonable-sounding defaults he chose?
- [ ] Is he aware the agency ledger's only entry is self-signed by "agent," and does he consider that a launch blocker or an acceptable artifact of solo dogfooding?
- [ ] Is the docs-vs-code drift (config fields, undocumented sweep flags, no ratchet CLI command) a documentation backlog he already knows about, or news to him?
## Next Action
Read the `adx-core` and `adx-gate` package source in the GitHub repo against the claims captured in [[Source Claims]] and flag any place the implementation doesn't match what the docs promise.
## Log
- **2026-07-22:** Read the full docs site (14 pages, verified against the live Astro sidebar config in the repo) and the GitHub README end to end; wrote [[Source Claims]] and this MOC. Codebase not yet reviewed — that's the next session.
- **2026-07-22:** Cloned and read the full repo (all 8 packages, 90 test cases, git history, self-dogfooded evidence); wrote [[Claims vs Implementation]]. Extracted every recommendation and prioritization judgment out of this note and that one into a new dedicated note, [[Recommended Fixes]], so this MOC and the two source-of-truth notes stay strictly factual.
