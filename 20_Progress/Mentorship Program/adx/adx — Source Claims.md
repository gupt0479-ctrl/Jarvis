---
type: input
status: sprout
created: 2026-07-22
updated: 2026-07-22
tags:
  - summary
notes:
  - "[[adx — MOC]]"
  - "[[Mentor Details]]"
source_url: https://ahnafyy.github.io/adx/
input_kind: web
track: ai
---
# adx — Agentic Developer Experience — Summary
**Source:** `https://ahnafyy.github.io/adx/` (docs site, all 13 sidebar pages + landing page) and `https://github.com/ahnafyy/adx` (README.md)
**Ingested:** 2026-07-22
**Pages:** 14 docs pages (full site, verified against the live Astro sidebar config) + 1 README
## Source
**adx** ("Agentic Developer Experience") is an **open-source** developer-tooling project on GitHub, maintained by **ahnafyy**, built as a documentation site (Astro + Starlight) plus a TypeScript monorepo. Its stated purpose: give engineering teams the measurement, runtime harness, and merge-time gate needed to let autonomous AI coding agents write code in a codebase without losing human comprehension of what shipped.
## Key Claims
- adx is explicitly **not** a coding agent — it is meta-tooling that measures, contains, and governs whatever agent a team already uses (**Claude Code**, **GitHub Copilot** Agent mode, **Cursor**)
- The core thesis: traditional developer experience optimizes for human eyes; **agentic DX** optimizes for **token economy** and **context stability** — these are named as different, currently unaddressed optimization targets
- The product is structured as **three pillars**: Measure, Orchestrate, Govern — corresponding to `adx audit/shape/sweep`, `adx init/run/maintain`, and `adx gate`
- Four **ADX Vitals** combine into one composite 0–100 score: **TDS** (Token Density, 30%), **FRR** (File Revisit Ratio, 25%), **BER** (Boundary Evidence, 30%), **HDI** (Human Discernment, 15%)
- A score of **80–100** is "agent-ready"; **60–79** is "acceptable"; **below 60** is "high agent cost"
- `adx audit --ci` fails a CI build if the score drops below `minimumAdxScore` (default **60**)
- `adx shape` finds the worst per-file **Token Density Score**; **import cycles always score 0** on FRR
- `adx sweep` hunts **"dark code"**: orphaned exports, `TODO`/`FIXME`/`HACK`/`XXX` comments, and files 3× the project median size
- The **Agentic Harness** provisions an isolated **git worktree** per agent run so agents cannot break the main branch
- Context assembly for every agent iteration draws from three sources: **AGENTS.md**, **llms.txt**, and dynamic **backlog constraints** from prior verification failures
- **Oscillation detection**: if the same test failure repeats across iterations, `adx ratchet` writes a permanent constraint into `AGENTS.md` and the harness halts to stop token waste
- `adx init` generates **18 agent spec files** — 6 single-purpose sub-agents × 3 IDE formats (GitHub Copilot, Claude Code, Cursor) — plus MCP server registration exposing 6 tools to IDE agents directly
- `adx run --exec <cmd> --done "<condition>"` enables a **maker/checker split**: the model signals `isDone`, then the harness independently re-verifies before declaring success
- `adx maintain` installs a **git pre-commit hook** that physically blocks commits touching **frozen paths** (e.g. `src/core/auth`) unless an explicit override with a written reason is registered
- **"Comprehension debt"** — machines shipping code faster than humans can verify it — is named as *the* ultimate breakdown mode of agentic workflows
- `adx gate` runs a **3-layer check** on every diff: Abstraction Gate (wrapper-to-logic ratio, default threshold 8%), Mutation Testing (injects bugs to catch fake-passing tests), Intent Cross-Reference (stated vs actual files touched)
- A test suite that still passes after mutated bugs are injected is flagged as a **"tautological compliance facade"**
- Files touched outside an agent's stated intent are flagged as **"semantic drift"** — this does not auto-fail the gate, it is surfaced for human review
- The **Agency Ladder** is a 7-level scale (Flag → Execute → Diagnose → Propose → Recommend → **Resolve** → Discern) that every `adx gate` sign-off is recorded against
- **Levels 1–2 are the "rubber-stamp danger zone"**; a `rubberStampRate` above 30% is named as the leading indicator of comprehension debt
- `minimumHumanAgencyRequired` defaults to **Level 6 (Resolve)** — engineers must demonstrate understanding, not just approve
- Every gate run writes a committed **Evidence Bundle** to `.evidence/run-<timestamp>/` (`diff.patch`, `intent-map.json`, `test-log.txt`, `manifest.json`) — this is what makes BER scoreable
- The project explicitly admits an unsolved gap: **"adx does not yet automate bundle rotation."**
- The codebase is a TypeScript **monorepo of 8 packages** (`adx-core`, `adx` CLI, `adx-shape`, `adx-gate`, `adx-sweep`, `adx-maintain`, `adx-mcp`, `adx-vscode`) with **90 tests across 7 packages**
## Full Content
### Home — Landing Page
==adx unifies measurement (the four vitals) with infrastructure (the harness and the gate) to protect a codebase from comprehension debt and abstraction bloat as AI agents write more of it.==
Tagline: *"Agents don't fail because models are bad — they fail because codebases weren't designed for machine reasoning. Every token wasted on context, every undocumented boundary, every unverified diff compounds into drift."*
Score-your-codebase-in-30-seconds demo:
```
npm install -g adx && adx audit
```
Sample output shown on the landing page:
```
ADX SCORE   85/100   ▲ agent-ready
▲ Token Density        (TDS)   95/100
▲ File Revisit Ratio   (FRR)   56/100
▲ Boundary Evidence    (BER)   100/100
▲ Human Discernment    (HDI)   83/100
```
Score bands: ✅ **80–100** agent-ready (clean context, strong structure); ⚠️ **60–79** acceptable (some friction, wasted context); 🔴 **below 60** high agent cost (prioritize TDS or BER first).
*Four vitals, explained plainly on the landing page:*
- **Token Density (TDS)** — signal per token of context window; bloated/poorly structured files burn the window before real work begins. Fix: break large files apart, remove dead exports, sharpen names.
- **File Revisit Ratio (FRR)** — how often agents must re-read the same files; high rates mean tangled responsibilities and unclear ownership. Fix: single-responsibility modules, clean API boundaries.
- **Boundary Evidence (BER)** — whether module boundaries are actually documented in `AGENTS.md`/`llms.txt`/typed interfaces. Without it, agents reason by guessing. Fix: run `adx init`.
- **Human Discernment (HDI)** — whether humans can still tell intentional design from agent-generated noise; guards against abstraction bloat and dead-code drift. Fix: run `adx sweep`.
*Three pillars, restated with an extra command not documented elsewhere on the site:*
1. **Measure** — `adx audit`, `adx shape`, `adx sweep`
2. **Orchestrate** — `adx init`, `adx run`, `adx maintain`
3. **Govern** — `adx gate` (3-layer check) **and `adx ratchet`** — described here as "permanently encodes a past failure as a constraint in `AGENTS.md` so it can't repeat." No reference page documents `adx ratchet` as a standalone command anywhere on the site.
What `adx init` scaffolds (landing-page table): `adx.config.ts`, `AGENTS.md`, `llms.txt`, `.adx/state/adx-agency.json`, `.github/agents/`, `.claude/agents/`, `.cursor/rules/`, `.vscode/mcp.json`.
Get up and running: (1) `npm install -g adx` / `pnpm add -g adx`, (2) `adx init`, (3) `adx audit`, (4) `adx gate`.
### Getting Started
==Getting agent-ready is three commands: `adx init` scaffolds the harness, `adx audit` scores the codebase, and `adx gate` adds the merge-time evidence check.==
Install: `npm install -g adx` or `pnpm add -g adx`. Bootstrap: `adx init` in any repository — same scaffold table as the landing page. Score: `adx audit`; the page repeats the same 85/100 sample scorecard and states scores above 80 are agent-ready, below 60 indicate high agent cost ("your codebase will burn tokens quickly and produce worse results"). Next steps point to The ADX Vitals, `adx init` reference, and `adx gate` reference.
### Measure — The ADX Vitals
==The four vitals combine into one composite score: $ADX = 0.30 \times TDS + 0.25 \times FRR + 0.30 \times BER + 0.15 \times HDI$, with 80+ counted as agent-ready and under 60 as high agent cost.==
Framing line: *"Traditional developer experience optimizes for human eyes. Agentic DX optimizes for token economy and context stability."*

| Vital | What it measures | Weight |
| --- | --- | --- |
| TDS — Token Density Score | Signal-to-noise ratio per file; boilerplate/unused abstractions/verbose wrappers burn context and raise API costs | 30% |
| FRR — File Revisit Ratio | How often an agent re-reads the same file from tight coupling or import cycles; high FRR = architectural smell | 25% |
| BER — Boundary Evidence Rating | Whether CI enforces an immutable evidence bundle before agent code merges; no gate = no accountability | 30% |
| HDI — Human Discernment Index | How far up the **Agency Ladder** engineers operate across recent sign-offs; Level ≤2 is rubber-stamping, target Level 6+ | 15% |

Score table: **80–100** agent-ready (clean context, good structure, boundary controls in place); **60–79** acceptable (some friction but workable); **<60** high agent cost (context bloat, missing controls, or comprehension debt). The minimum threshold is enforced via `boundary.minimumAdxScore` in `adx.config.ts`, and `adx audit --ci` fails below it.
### adx audit
==`adx audit --ci` fails the build below `minimumAdxScore` (default 60), turning the vitals into an enforceable CI gate rather than a cosmetic score.==
Usage: `adx audit [options]`.

| Flag | Description |
| --- | --- |
| `--cwd <path>` | Directory to audit (default: current directory) |
| `--ci` | Exit code 1 if score is below `minimumAdxScore` |
| `--json` | Raw JSON output for scripting/CI |
| `--badge` | Write `.adx/badge.json` in shields.io endpoint format |

JSON output shape: `{ overall, tds: { score, estimatedTokens, flaggedFiles, signalRatio }, frr: { score, cycles, revisitProneFiles }, ber, hdi, filesScanned }`. The badge can be embedded in a README via `![ADX Score](https://img.shields.io/endpoint?url=...)`. CI usage shown: `adx audit --cwd . --ci --badge`.
### adx shape
==Import cycles always score 0 on File Revisit Ratio, because a cycle means an agent can never get a complete picture of a module without re-reading everything in it.==
Usage: `adx shape [options]`.

| Flag | Description |
| --- | --- |
| `--cwd <path>` | Directory to scan (default: current directory) |
| `--top <n>` | Show N worst-scoring files (default: 10) |
| `--json` | Raw JSON output |

TDS scoring bands: **90–100** high signal (mostly logic); **70–89** good/balanced; **50–69** low signal (consider splitting); **<50** poor (agents waste context reading it). FRR measures how often a single agent session would need to re-read the same file — files imported by many others, or sitting in tight import cycles, are "revisit-prone." Fixes stated: barrel files (`index.ts` with only `export *`) scoring low TDS is *expected, not a bug*; low-TDS logic files should be split with types extracted to `types.ts`; high FRR should be fixed by reducing the number of files importing from a single hub, moving toward more leaf nodes.
### adx sweep
==adx treats AI agents as reliable producers of "dark code" — orphaned exports, TODO/FIXME placeholders, and oversized files — because agents don't feel the maintenance pain that would stop a human from leaving them behind.==
Usage: `adx sweep [options]` (`--cwd <path>`, `--json`). Detects three categories:
- **Orphaned exports** — symbols `export`ed but never imported anywhere; described as "the most common form of agent-generated litter — the model declares a type or function 'for completeness' that nothing ever uses"
- **Dark comments** — `TODO`/`FIXME`/`HACK`/`XXX`; each one is described as "a promise the agent made and didn't keep"
- **Fat files** — files significantly larger than the project median; a file 3× the median signals an agent merged concerns it should have split
Sweep exits with code 1 if any dark pattern is found; combine with `continue-on-error: true` in CI for advisory-only mode.
### Orchestrate — The Agentic Harness
==The harness separates an autonomous Agent Inner Loop from a human Engineer Outer Loop, with the Evidence Gate as the one hard boundary code must cross between them.==
Framing quote: *"The agent is the system around the model. The scaffolding turns a model into a reliable engineering collaborator."* Inner/outer loop diagram: Context → Model Call → Chain-of-Thought → Verification Hooks (test runner) → Ratchet (on repeated failure) → Backlog, feeding back into Context; on `isDone` + verification pass, control crosses the **Evidence Gate** into the Engineer Outer Loop: Discernment Matrix → Sign-off → Agency Ledger.
*Context assembly* (every iteration): 1) `AGENTS.md` — conventions + ratcheted past-failure constraints, 2) `llms.txt` — machine-readable structural map, 3) backlog rules — dynamic constraints from prior verification failures. This gives the agent continuity across sessions despite LLMs having no persistent memory.
*Verification hooks* (after each iteration): runs the test suite (`vitest` by default); on failure, the failure is injected into next iteration's backlog; if the same failure repeats (oscillation detection), `adx ratchet` writes a permanent `AGENTS.md` constraint and the harness halts to prevent token waste.
*State persistence*: `.adx/state/progress.json` (gitignored, ephemeral chain-of-thought) and `.adx/state/adx-agency.json` (committed, permanent agency ledger).
*Workspace isolation*: each `adx run` provisions a fresh git worktree under `.adx/worktrees/`, torn down on completion.
### adx init
==`adx init` generates 18 agent spec files — 6 focused, single-tool sub-agents × 3 IDE formats (Copilot, Claude Code, Cursor) — so each IDE's agent picker gets a precise trigger instead of one generic catch-all agent.==
Usage: `adx init [options]` (`--cwd <path>`, `--force` to overwrite, `--worktree` to also provision an isolated worktree for the first session).
*Core harness files created:* `adx.config.ts`, `AGENTS.md`, `llms.txt` (a skeleton — "fill this in, it matters"), `.adx/state/progress.json` (gitignored), `.adx/state/adx-agency.json` (committed).
*The 6 sub-agents, one per adx tool:*

| Agent | Tool | Trigger |
| --- | --- | --- |
| adx-auditor | `adx_audit` | Before any task — get the quality baseline |
| adx-shaper | `adx_shape` | When context windows feel bloated |
| adx-sweeper | `adx_sweep` | Before merging — find dark code |
| adx-gate | `adx_gate_check` | After changes — check the diff |
| adx-ratchet | `adx_ratchet` | After a mistake — lock it into AGENTS.md |
| adx-planner | `adx_run_plan` | Before a large task — assemble context |

*Per-IDE file formats:*

| IDE | Location | Format | Frontmatter fields |
| --- | --- | --- | --- |
| GitHub Copilot | `.github/agents/*.agent.md` | `.agent.md` | `name`, `description`, `tools`, `user-invocable` |
| Claude Code | `.claude/agents/*.md` | plain markdown | `name`, `description` |
| Cursor | `.cursor/rules/*.mdc` | `.mdc` rules | `description`, `globs`, `alwaysApply` |

*MCP server registration* — configs are **not identical** across IDEs: VS Code uses a portable `${workspaceFolder}` variable; Claude Code and Cursor require absolute paths resolved at init time.

| File | Path style | Used by |
| --- | --- | --- |
| `.vscode/mcp.json` | `${workspaceFolder}/...` | VS Code · Copilot Agent |
| `.claude/mcp.json` | absolute path | Claude Code |
| `.cursor/mcp.json` | absolute path | Cursor |

`.github/copilot-instructions.md` is also generated — always-on workspace context, separate from the per-agent `.agent.md` files. Stated most-important next step after init: **fill in `llms.txt`** — the generated file is only a skeleton, and the more accurate it is, the fewer file revisits agents make. Suggested sequence: `adx init → fill in llms.txt → adx audit → adx maintain install`.
### adx run
==The `--done` flag enables a maker/checker split: only after the model itself signals `isDone: true` does the harness independently re-run verification hooks, and only if those pass does the run actually complete.==
Usage: `adx run "<task>" [options]`.

| Flag | Description |
| --- | --- |
| `--cwd <path>` | Project directory |
| `--plan` | Assemble context, write a task file, do not call the model |
| `--exec <cmd>` | Shell out to a CLI agent with the assembled context |
| `--done "<condition>"` | Verifiable done condition for the maker/checker split |
| `--max-iterations <n>` | Override `maxIterations` from config |

*Plan mode* writes `.adx/tasks/<run-id>.md` containing the task description, done condition, the full assembled system prompt (AGENTS.md + llms.txt + backlog constraints), and an estimated token count — meant to be handed to any IDE agent for consistent, context-rich execution.
*Exec mode* sequence: 1) provisions an isolated git worktree, 2) assembles the system prompt, 3) calls the model in a loop up to `maxIterations`, 4) runs verification hooks after each iteration, 5) ratchets repeated failures into `AGENTS.md`, 6) halts on oscillation detection.
Example: `adx run "Fix the rate-limiting bug in the API layer" --exec "claude" --done "pnpm test passes and adx audit --ci exits 0"`.
Every run writes `.adx/state/progress.json` with `projectId`, `runId`, `iteration`, `status`, a `chainOfThought` array (`iteration`, `intent`, `filesRead`, `filesModified`, `outcome`), and `backlog`. This chain-of-thought is what populates `statedFilesModified` in the `adx gate` evidence bundle.
### adx maintain
==Frozen paths are enforced by a real git pre-commit hook, not a convention — commits touching a frozen path are physically blocked until an engineer registers an explicit override with a reason.==
Three subcommands:
- **`adx maintain install`** — installs the git pre-commit hook; it reads `.adx/frozen-paths.json` on every commit and blocks staged files matching a frozen pattern
- **`adx maintain sync`** — syncs `frozenIntents` from `adx.config.ts` into `.adx/frozen-paths.json`; run after every config change to frozen paths
- **`adx maintain status`** — shows current frozen paths and hook install state (sample output: "Pre-commit hook installed", "Frozen paths 2")
Configuring frozen paths in `adx.config.ts`:
```
maintain: {
  frozenIntents: [
    './src/core/auth',
    './src/db/migrations',
  ],
},
```
Override flow: `adx maintain override --path "src/core/auth" --reason "Migrating to new session type — reviewed by @ahnafyy"`, then commit with `git commit --no-verify` — the hook warns but no longer blocks once the override is registered. Notably, `install`/`sync`/`status` each get a described usage pattern, but `override` gets only a single one-line example with no options table — inconsistent depth within the same page.
### Govern — The Loop Boundary Gate
==Comprehension debt — machines shipping code faster than humans can verify it — is named as the ultimate failure mode agentic workflows are prone to, and the gate exists specifically to force Level 6 engagement, not rubber-stamp approval.==
Quoted directly: *"The ultimate breakdown in agentic workflows is comprehension debt — machines shipping code faster than humans can verify it."* The gate is positioned as the hard boundary between **Agent Inner Loop** (capable generation) and **Engineer Outer Loop** (ultimate ownership); without it, "agents ship code and humans rubber-stamp it." The gate forces engagement at **Level 6 (Resolve)** — engineers must understand what changed, not just approve it.
*The 3 layers, as introduced on this overview page (fuller detail lives on the `adx gate` command page):*
1. **Abstraction Gate** — ratio of abstraction lines (interfaces, types, wrappers) to functional logic lines in the diff; flags if overhead exceeds the threshold (default 8%). Catches "the most common form of agent bloat: adding an `AbstractFactoryProvider` when a function would do."
2. **Mutation Testing** — injects controlled bugs into the agent's new code and runs the suite; tests still passing after injection means the suite is a **"tautological compliance facade"** — appearance of verification without real coverage. Sample output: `Mutations applied 4 / Mutations caught 3/4 / Score 75/100 / ✗ Tautological test detected: src/api/validate.ts "Flip > to <" not caught`.
3. **Intent Cross-Reference** — parses the agent's chain-of-thought (`progress.json`) and cross-references `filesModified` against the actual git diff; files touched outside stated intent are flagged as **"semantic drift."**
*Evidence bundle* written to `.evidence/run-<timestamp>/`: `diff.patch` (full session diff), `intent-map.json` (stated vs actual files), `test-log.txt` (mutation-testing output), `manifest.json` (scores, agency level, sign-off, timestamp) — all **committed**, forming the permanent audit trail that "makes BER meaningful."
*Sign-off*: after the three layers, the **Discernment Matrix** interactive terminal UI requires the engineer to (1) select their agency level 1–7, (2) explain any flagged change categories (`security`, `dependency-addition`). Recorded in `.adx/state/adx-agency.json`. If the gate score is below passing, minimum required agency level is **6 (Resolve)** regardless of config.
### adx gate
==Mutation testing is the layer that catches a test suite passing for the wrong reason: if injected bugs still let tests pass, the suite is flagged as a "tautological compliance facade."==
Usage: `adx gate [options]` (`--cwd <path>`, `--ci` for non-interactive CI mode, `--dry-run` to report without blocking).
Full interactive sample output (abridged): 14 changed files detected → Layer 1 abstraction analysis → Layer 2 mutation testing → taste-deficit analysis → Layer 3 intent cross-reference → evidence bundle saved → Discernment Matrix showing Layer 1 (token overhead 1%, PASS, 100/100), Layer 2 (4/4 mutations caught, 100/100), Layer 3 (intent recorded: yes, 100/100) → Gate Score 100/100 → GATE PASSED → Engineer Sign-Off prompt: *"Agency Ladder 1=Flag 2=Execute 3=Diagnose 4=Propose 5=Recommend 6=Resolve 7=Discern. Your agency level for this change [6]:"*.
Note: **"Taste deficit analysis"** appears explicitly in this sample terminal output as its own scan step, distinct from the three named/scored layers — the page never explains what it checks or whether/how it factors into the numeric gate score.
CI usage: `adx gate --cwd . --ci --dry-run` with `continue-on-error: true`, described as "advisory until BER ≥ 75" — remove `--dry-run` and `continue-on-error` once a team establishes that baseline.
Gate score composite: Layer 1 (0–100) + Layer 2 (0–100) + Layer 3 (0–100, defaults to 75 if no intent was recorded). A gate score below 60 blocks merge; minimum agency level required when blocked is Level 6 (Resolve). Evidence bundle written to `.evidence/run-<timestamp>/` — "commit this directory... what makes BER score 100."
### Concepts — The Agency Ladder
==A `rubberStampRate` above 30% in `adx-agency.json` is named as the leading indicator of comprehension debt — teams stuck at Levels 1–2 pay the full cost of AI tooling without capturing any of its productivity gain.==

| Level | Name | Description |
| --- | --- | --- |
| 1 | Flag | Agent scanned a log, created an issue, exited. No code written. |
| 2 | Execute | Agent wrote a fix from explicit, step-by-step human prompts. Human was the architect. |
| 3 | Diagnose | Agent correctly identified the root cause of an unprompted error, unassisted. |
| 4 | Propose | Agent generated multiple alternative branches and presented trade-offs. |
| 5 | Recommend | Agent picked the optimal branch with data-backed justification; human reviewed and approved. |
| 6 | Resolve | Agent found it, fixed it, verified it, looped human into the PR; human fully understood before signing off. |
| 7 | Discern | Agent/engineer determined a task was negative-value or an architectural trap and explicitly closed it: "Not worth fixing. Moving on." |

Stated grouping: Levels 1–2 = human doing most of the thinking, agent is "a fast typist"; Levels 3–4 = agent starting to reason, human still decision-maker; Levels 5–6 = agent is a genuine collaborator, human is accountable owner; Level 7 = "the rarest and most valuable: knowing what *not* to build." Harness goal: safely push toward Levels 5–6 while keeping Level 7 firmly human.
Recorded ledger entry shape (`.adx/state/adx-agency.json`): `projectId`, `entries: [{ timestamp, ref, level, summary, signedBy }]` — committed, the "permanent, auditable record of human oversight." Enforcement: `adx.config.ts` sets `boundary.minimumHumanAgencyRequired: AgencyLevel.Resolve` (Level 6); if the gate score is below passing, the requirement rises to Level 6 regardless of config.
HDI formula, stated directly: $HDI = \frac{(\text{mean agency level} - 1)}{6} \times 100$. An empty ledger returns HDI = 50 (neutral); a team entirely at Level 6 returns HDI ≈ 83; Level 7 throughout returns HDI = 100.
### Concepts — Evidence Bundles
==Evidence bundles are committed specifically because BER checks for their presence — gitignoring `.evidence/` drops BER to 0 and pulls the whole composite ADX score down with it.==
Bundle contents at `.evidence/run-<timestamp>/`:
- `diff.patch` — full `git diff HEAD` at gate time; lets reviewers see exactly what changed "even months later, independent of git history rewriting"
- `intent-map.json` — `statedFilesModified`, `actualFilesModified`, and a `drift` array of files changed without declared intent; non-empty drift doesn't auto-fail the gate, it's surfaced for human review — "unexplained changes to security-sensitive files are the most important thing to catch here"
- `test-log.txt` — captured mutation-testing output (mutations applied/caught/score, plus any tautological-test flags)
- `manifest.json` — signed summary: `generatedAt`, `runId`, `abstractionScore`, `mutationResult`, `semanticDrift`, `signedBy`, `agencyLevel`
> [!NOTE] Self-acknowledged limitation, quoted directly: "adx does not yet automate bundle rotation — this is a known gap." Suggested manual workarounds: archive older bundles with Git LFS, set a retention policy and script the cleanup, or keep only `manifest.json`/`intent-map.json` and drop `diff.patch`/`test-log.txt`.

What to commit vs gitignore (stated table): commit `.evidence/`, `.adx/state/adx-agency.json`, `.adx/badge.json`, `.adx/frozen-paths.json`; gitignore `.adx/state/progress.json`, `.adx/tasks/`, `.adx/worktrees/`. `adx init` sets up `.gitignore` with the correct entries automatically. Bundle growth is named directly: a typical bundle is 5–50KB; active projects gating every PR "might accumulate hundreds of bundles per year."
### Configuration Reference
==Every boundary default (`minimumHumanAgencyRequired: Resolve`, `minimumAdxScore: 60`, `maxTokenOverhead: '8%'`) is a config field an engineering team can loosen — the strict posture is the shipped default, not a hard-coded floor.==
`adx.config.ts` is the single configuration file, created via `adx init` or written manually with `createAgenticSystem()` from `adx-core`.
*`harness.context`:* `rules` (path to `llms.txt`, default `'./llms.txt'`), `memory` (`'disk' | 'none'`, default `'disk'`), `stateDir` (default `'.adx/state'`).
*`harness.control`:* `router` (only `'sequential'` supported currently — implies other routers may come later), `maxIterations` (default 15, overridable per-run with `--max-iterations`).
*`harness.observe`:* `telemetry` (`Array<'tokens' | 'file-revisits'>`, default both), `tests` (`'vitest' | 'jest' | 'none'`, default `'vitest'`).
*`harness.persist`:* `isolation` (`'git-worktree' | 'none'`, default `'git-worktree'`), `worktreeDir` (default `'.adx/worktrees'`).
*`harness.hooks`:* `onSlip` (`'retry-with-backoff' | 'halt-and-dump'`, default `retry-with-backoff`), `maxRetries` (default 3).
*`lifecycle.sweep`:* `pruneUnusedAbstractions` (boolean, default true), `maxTokenOverhead` (string, default `'8%'`).
*`lifecycle.maintain`:* `frozenIntents` (`string[]`, default `[]`, matched as path suffixes; run `adx maintain sync` after changes).
*`boundary`:* `minimumHumanAgencyRequired` (`AgencyLevel`, default `Resolve`/6), `enforceTasteCheck` (boolean, default true), `requireExplanationInvariants` (`string[]`, default `['security', 'dependency-addition']`), `minimumAdxScore` (number, default 60).
`AgencyLevel` enum exported from `adx-core`: `Flag`=1, `Execute`=2, `Diagnose`=3, `Propose`=4, `Recommend`=5, `Resolve`=6 (recommended minimum), `Discern`=7.
### GitHub README — Additional Details Not on the Docs Site
==The project is a TypeScript monorepo of 8 packages (`adx-core` through `adx-vscode`) with 90 tests across 7 packages, distributed as a single global npm install (`adx`) that wraps all of them.==
*Packages table:*

| Package | Purpose |
| --- | --- |
| `adx-core` | Harness engine, Agency Ladder, config types, state persistence |
| `adx` (`adx-cli`) | CLI entry point — all commands |
| `adx-shape` | Token density scanner — TDS and FRR per file |
| `adx-gate` | 3-layer evidence boundary gate + sign-off UI |
| `adx-sweep` | Dark code detector — orphaned exports, TODO debt, fat files |
| `adx-maintain` | Frozen path locks and git pre-commit hook |
| `adx-mcp` | MCP server — exposes all 6 adx tools to IDE agents |
| `adx-vscode` | VS Code extension — status bar score, gutter decorations, dashboard |

*CI integration example given in the README:*
```
- name: ADX Sweep — dark code scan
  run: adx sweep --cwd .
- name: ADX Gate — evidence boundary (non-blocking until BER ≥ 75)
  run: adx gate --cwd . --ci --dry-run
  continue-on-error: true
- name: ADX Audit — quality scorecard
  run: adx audit --cwd . --ci --badge
```
*Development commands (README's own dev workflow):* `pnpm install`, `pnpm build`, `pnpm test` (stated as "90 tests across 7 packages"), `pnpm typecheck`.
*Project layout tree (full, as given):* `adx.config.ts`, `AGENTS.md`, `llms.txt`, `.github/agents/`, `.claude/agents/`, `.cursor/rules/`, and `.adx/` containing `state/adx-agency.json` (committed permanent ledger) + `state/progress.json` (gitignored ephemeral) + `tasks/` (gitignored) + `worktrees/` (gitignored) + `badge.json`; plus a top-level `.evidence/run-<timestamp>/` (committed) holding `diff.patch`, `intent-map.json`, `test-log.txt`, `manifest.json`.
The README badge is a **live shields.io endpoint** reading `.adx/badge.json` from `raw.githubusercontent.com` — meaning adx literally scores its own repository and displays that score at the top of its own README.
## Why It Matters
This note is the factual foundation for a mentorship deliverable: **Ahnaf** (mentor, [[Mentor Details]]) asked for a detailed, honest third-party review of adx — usage, gaps, and how it compares to adjacent tooling. Every judgment call in [[adx — MOC]] traces back to a specific claim captured here, so the review stays checkable against what adx actually says about itself rather than a vague impression of it.
## Links Into The Vault
- [[adx — MOC]] — the analysis and judgment note built on top of this source capture
- [[Mentor Details]] — the mentor whose project this is
## Open Questions
- [ ] No reference page exists for `adx ratchet` despite it being named on the homepage and exposed as an MCP tool (`adx_ratchet`) — every other command (audit/shape/sweep/init/run/maintain/gate) has a full page
- [ ] "Taste deficit analysis" appears in the `adx gate` sample output and as `boundary.enforceTasteCheck` in the config reference, but no page explains what it checks or how/whether it factors into the numeric gate score
- [ ] The 6 MCP tool schemas (`adx_audit`, `adx_shape`, `adx_sweep`, `adx_gate_check`, `adx_ratchet`, `adx_run_plan`) are named but their parameters/return shapes are undocumented anywhere
- [ ] `adx-vscode` is listed in the README Packages table with a one-line description but has zero coverage anywhere on the docs site — no install path, no marketplace link, no screenshots
- [ ] No stated rationale anywhere for the vital weights (30/25/30/15) or the 8% abstraction-overhead default — presented as fixed with no empirical justification shown
- [ ] Every default (`vitest`/`jest`, npm/pnpm, `tsconfig`) assumes a Node/TypeScript project; no statement on whether non-JS ecosystems are in scope, planned, or explicitly out of scope
- [ ] No worked end-to-end example, FAQ, troubleshooting, changelog, or roadmap page exists in the nav — every command page uses synthetic sample output, never a real before/after repo
- [ ] `router: 'sequential'` is described as "currently only sequential is supported," implying other routers are planned, but no roadmap confirms this
## Flashcards
The four ADX vitals and their weights?::**TDS** 30%, **FRR** 25%, **BER** 30%, **HDI** 15% — composite via $ADX = 0.30TDS + 0.25FRR + 0.30BER + 0.15HDI$ #cards/ai
What distinguishes Agency Ladder Level 6 (**Resolve**) from Level 2 (**Execute**)?::At Level 2 the agent executes an explicit human-given fix; at Level 6 the agent found, fixed, and verified the issue itself, and the human fully understood the change before signing off — Level 2 is "rubber-stamp danger zone," Level 6 is genuine collaboration #cards/ai
What does `adx gate` Layer 2 (**Mutation Testing**) actually catch that a normal passing test suite would miss?::It injects controlled bugs into the agent's new code; if tests still pass, the suite is flagged as a **"tautological compliance facade"** — green tests that don't actually verify the logic #cards/ai
Why does File Revisit Ratio score an import cycle as exactly 0, never partial credit?::Because a cycle means an agent can never get a complete picture of the module without re-reading everything inside the cycle — there's no partial understanding possible #cards/ai
What happens to BER if `.evidence/` is gitignored instead of committed?::BER drops to 0, since BER checks for the presence of the committed evidence bundle — this pulls down the whole composite ADX score, since BER carries a 30% weight #cards/ai
