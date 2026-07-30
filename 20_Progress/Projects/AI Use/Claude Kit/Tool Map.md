---
type: index
status: active
created: 2026-07-29
updated: 2026-07-29
tags:
  - claude-code
  - ai-use
  - ingestion
  - claude-kit
notes:
  - "[[60_Claude/10_Source_Summaries/Github Ingestion/Immediate Action|Immediate Action]]"
  - "[[40_Resources/CS/Repos]]"
  - "[[20_Progress/AI/Claude Code/MOC|Claude Code MOC]]"
next: "Add a row here the same session anything new lands in second-brain-claudekit's sandbox/, tested-skills/, or a rigid folder — see that repo's Docs/Jarvis.md for the ritual"
---
# Claude Kit — second-brain-claudekit Tool Map

==This is the living map of everything ingested into `gupta-builds/second-brain-claudekit`== (`~/projects/ai/claude/second-brain-claudekit` in WSL) — one row per tool, updated the same session its pipeline stage changes. **This file gets a new or updated entry every time something new is ingested, tested, blocked, or promoted** — the same append-only discipline as [[60_Claude/20_Distilled_Notes/Sources - Plan/_Notes Created From Ingestion|_Notes Created From Ingestion]], applied to tooling instead of vault notes.

This tracks a different layer than `20_Progress/AI/Claude Code/<Project>/Setup.md` — those are per-project, hand-maintained inventories of what's *actually deployed* in a real project's `.claude/`. Most rows below haven't reached that stage yet; this file exists precisely to track the stage *before* that. See `second-brain-claudekit/Docs/Jarvis.md` for the full division of labor.

**Pipeline stages** (full definitions: `second-brain-claudekit/Docs/Architecture.md`): `sandbox` → `tested-skills` → `promoted (repo-scoped)` / `promoted (global)`, or `blocked` / `dropped` / `undecided` at any point.

## Tools

### GBrain
- **What:** Personal-knowledge MCP with synthesis + gap-analysis (not just retrieval), PGLite-backed, no Docker.
- **Useful for:** Every project — Jarvis, BOOM, Portfolio, TradingView, CausalOps. A memory layer is not project-specific by nature.
- **Global vs. project-scoped:** **Global candidate**, confirmed — useful with no regard to which project is open (`second-brain-claudekit/Docs/Design.md`'s global test).
- **Pipeline stage:** `sandbox/gbrain/` — installed and tested for real. `bun install` (283 packages) → `bun run src/cli.ts init --pglite --no-embedding` → `doctor` reported **80/100 overall health, 100/100 brain score**, real PGLite database at `~/.gbrain/`.
- **Why not promoted yet:** One real, named, unresolved decision — which embedding provider (Voyage, ZeroEntropy, or OpenAI) to use for full semantic search. Currently running keyword/graph-only. Not a technical blocker, a cost/vendor decision.
- **Displaces:** Makes `memsearch` (auto-capture, no synthesis) and `context-sync` (thinner SQLite memory) both redundant once adopted — see [[40_Resources/CS/Repos]]'s entries for both.
- **Paired with:** gstack's own `/setup-gbrain` command (below) — same author, designed as a matched pair, not two independent tools.

### gstack
- **What:** ~34 slash commands + 55 generated skills (Playwright-based browse/design/PDF tooling), from the same author as GBrain.
- **Useful for:** Global by design — its own `./setup` targets Claude Code, Codex, Factory, and OpenCode simultaneously.
- **Global vs. project-scoped:** Global by design once unblocked. Currently project-based *only because it's blocked*, not by architecture — see `second-brain-claudekit/Docs/Design.md`.
- **Pipeline stage:** Stuck in `sandbox/gstack/`, **blocked**. `./setup` compiled the browse/design/PDF binaries, generated 55 skills (~893,538 tokens if all loaded at once), downloaded a 278MB Chromium build — then failed: `gstack setup failed: Playwright Chromium could not be launched`. Missing WSL system libraries (confirmed via `50_Claude/scripts/check_dependency.py --preset gstack` in the repo: `libnss3.so` missing, everything else present).
- **Fix required (not done, needs an interactive terminal):**
  ```bash
  sudo apt-get update && sudo apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2
  cd ~/projects/ai/claude/second-brain-claudekit/sandbox/gstack && ./setup
  ```
- **Confirmed NOT registered:** `~/.claude/skills/gstack` and `~/.claude/commands/gstack*` both absent — setup aborted before its own registration step.

### mattpocock-skills (`engineering/` category)
- **What:** 41 skills total (not the 18 originally assumed — a real correction from actually running the installer), fixing common agent failure modes. Only the `engineering/` category (17 skills: `code-review`, `tdd`, `diagnosing-bugs`, `implement`, `research`, `to-spec`, `to-tickets`, `codebase-design`, `domain-modeling`, `improve-codebase-architecture`, `resolving-merge-conflicts`, `triage`, `wayfinder`, `ask-matt`, `grill-with-docs`, `prototype`, `setup-matt-pocock-skills`) has been looked at.
- **Useful for:** Likely global (generic engineering-process skills, not project-specific), pending per-skill review.
- **Global vs. project-scoped:** **Undecided per-skill** — leaning global once reviewed, since nothing in the `engineering/` category is tied to a specific stack.
- **Pipeline stage:** `tested-skills/mattpocock-engineering/` — cleared `sandbox/`, sitting in the second-look stage. Not yet promoted to any rigid folder.
- **Why not promoted yet:** The interactive picker (`bunx skills@latest add mattpocock/skills`) doesn't complete non-interactively, so the whole `engineering/` category was copied for manual review rather than cherry-picked live. `personal`, `productivity`, `misc`, `in-progress`, `deprecated` categories exist in the same repo and haven't been looked at at all.

### ECC (affaan-m/everything-claude-code)
- **What:** Cross-harness agent operating system — 67 agents, 281 skills, 94 legacy command shims, hooks, rules, MCP configs, AgentShield security scanning, and a Memory Vault. ECC 2.0 additionally ships a Rust-based control-plane scaffold (`ecc2/`, in-tree, builds locally): terminal UI dashboard, SQLite session store, background daemon mode. Alpha quality per its own README, not GA.
- **Useful for:** Undetermined at the whole-repo level — real testing has started but the "does this close a named gap nothing else already closes" question (Promotion-Criteria.md Q2/Q3) hasn't been answered for any specific component yet.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/ecc/` — real `git clone` (2026-07-30, in addition to the pre-existing WSL clone at `~/projects/ai/claude/everything-claude-code/`, kept separate rather than reused, per this repo's own "nothing skips sandbox/" rule). `npm install --no-audit --no-fund` completed clean (210 packages — the repo is markdown-heavy, not dependency-heavy: 3 runtime deps, 8 devDeps). `node tests/run-all.js` (the repo's own documented test command) run for a real pass/fail signal.
- **Real finding, new to this pipeline:** merely cloning ECC into `sandbox/ecc/` caused Claude Code to auto-load its `CLAUDE.md`, `.claude/rules/*.md`, and register a `.claude/skills/everything-claude-code` skill into the active session — no explicit install step required. This means `Docs/Architecture.md`'s assumption that `sandbox/` is inert until deliberately run is **false** for any tool shipping its own `CLAUDE.md`/rules/skills — Claude Code's own config auto-discovery already "runs" part of it just by existing on disk inside the project. Flagged for a correction to `Docs/Architecture.md`.
- **Scope discipline (per Docs/Design.md, Implement > Knowledge):** ECC's catalog (67 agents/281 skills/94 commands) is large enough that wholesale install (`./install.sh --profile full`) would itself be the anti-pattern this repo's philosophy exists to prevent. The real next decision is which specific named gap(s), if any, ECC's components close that nothing already-adopted (gbrain, mattpocock-engineering, this repo's own `/challenge` `/ideas` `/strategy` `/llm-council` skills) already closes — not "install all of it because the catalog is large." Not yet decided.
- **Next:** Identify 2-4 specific ECC components (an agent, a skill, a hook pattern) worth reviewing individually against a real gap, rather than evaluating all 442 components at once.

- **Real test results (2026-07-30):** `node tests/run-all.js` — **3378/3388 passed (99.7%), 10 failed, exit 0.** All 10 failures isolated to two files, not scattered: 9 in `integration/plan-canvas-e2e.test.js` (ECC 2.1's browser-based "Plan Canvas" review feature — every failure traces to `connect ETIMEDOUT 127.0.0.1:21517`, a local detached server never coming up in this sandboxed WSL environment; looks environment-specific, same shape as gstack's Playwright/Chromium blocker, not a confirmed ECC bug) and 1 in `lib/dry-run.test.js` ("--dry-run works with implicit install routing" — `Expected exit 0, got null`, not yet root-caused). Per Promotion-Criteria.md Q1 ("did it actually run without a manual workaround") this is an honest **partial-yes**: the core test suite runs clean; one experimental feature (Plan Canvas) and one dry-run edge case do not, named and specific rather than glossed over.

## Not yet in `sandbox/` at all
Everything else in [[40_Resources/CS/Repos]] not named above — still starred, still exactly where the 2026-07-29 GitHub ingestion pass ([[00_Execution#Github|00_Execution's Github section]]) left it. Not forgotten, just genuinely not ingested into this repo yet.
