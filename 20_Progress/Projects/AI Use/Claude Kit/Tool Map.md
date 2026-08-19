---
type: index
status: active
created: 2026-07-29
updated: 2026-08-19
tags:
  - claude-code
  - ai-use
  - ingestion
  - claude-kit
notes:
  - "[[Claude Kit Implementation|Claude Kit]]"
  - "[[40_Resources/CS/Repos]]"
  - "[[20_Progress/AI/Claude Code/MOC|Claude Code MOC]]"
next: Add a row here the same session anything new lands in second-brain-claudekit's sandbox/, tested-tools/, or a rigid folder — see that repo's _docs/Jarvis.md for the ritual
---
# Claude Kit — second-brain-claudekit Tool Map

==This is the living map of everything ingested into `gupta-builds/second-brain-claudekit`== (`~/projects/ai/claude/second-brain-claudekit` in WSL) — one row per tool, updated the same session its pipeline stage changes. **This file gets a new or updated entry every time something new is ingested, tested, blocked, or promoted** — the same append-only discipline as [[60_Claude/20_Distilled_Notes/Sources - Plan/_Notes Created From Ingestion|_Notes Created From Ingestion]], applied to tooling instead of vault notes.

This tracks a different layer than `20_Progress/AI/Claude Code/<Project>/Setup.md` — those are per-project, hand-maintained inventories of what's *actually deployed* in a real project's `.claude/`. Most rows below haven't reached that stage yet; this file exists precisely to track the stage *before* that. See `second-brain-claudekit/_docs/Jarvis.md` for the full division of labor.

**Pipeline stages** (full definitions: `second-brain-claudekit/_docs/Architecture.md`): `sandbox` → `tested-tools` → `promoted (repo-scoped)` / `promoted (global)`, or `blocked` / `dropped` / `undecided` / **`parked (future)`** at any point. `tested-tools` is the current name — the repo renamed `tested-skills/` → `tested-tools/` on 2026-08-09; this vault's own vocabulary was still calling it `tested-skills` until this pass caught the drift (real, still-unreconciled naming drift the other direction too — see `second-brain-claudekit/_docs/Gaps.md`). `parked (future)` is new as of 2026-08-19: a tool that clears `tested-tools/` review but has no current project need lands in `tested-tools/_future/<repo>/` with a `FOR-WHAT.md` naming the use case it's waiting for, per `60_Claude/vault-rules/pipeline-conventions.md`. Verified 2026-08-19 by direct listing: `tested-tools/_future/` is currently empty — correctly, not as a gap; nothing on this page has cleared review with no home yet.

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
- **Pipeline stage:** `tested-tools/skills/mattpocock-engineering/` — cleared `sandbox/`, sitting in the second-look stage. Not yet promoted to any rigid folder.
- **Why not promoted yet:** The interactive picker (`bunx skills@latest add mattpocock/skills`) doesn't complete non-interactively, so the whole `engineering/` category was copied for manual review rather than cherry-picked live. `personal`, `productivity`, `misc`, `in-progress`, `deprecated` categories exist in the same repo and haven't been looked at at all.
- **Verified 2026-08-19:** still 0 of the 17 skills individually tested — `tests/skills/mattpocock-engineering/README.md` now tracks this as an honest, dated backlog table (one "Tested?" column, all `No`) rather than leaving it implicit. This is the real state, not a placeholder — confirmed by direct read.

### cpr-compress-preserve-resume (EliaAlberti)
- **What:** Three markdown slash commands (`compress`, `preserve`, `resume`) implementing the same Compress→Preserve→Resume session-continuity pattern second-brain-claudekit's own hand-authored `commands/compress.md`/`preserve.md`/`resume.md` already used.
- **Useful for:** Session-lifecycle commands inside second-brain-claudekit specifically — not a general promotion candidate elsewhere.
- **Global vs. project-scoped:** Repo-scoped (Jarvis-only equivalent, i.e. scoped to second-brain-claudekit's own session pattern), per its `VERDICT.md`'s `destination:` field.
- **Pipeline stage:** `tested-tools/commands/cpr-compress-preserve-resume/` — the first individually-tested, evidence-backed promotion decision in this repo. **Verdict: blend**, verified by direct read of `VERDICT.md` and its backing `tests/commands/cpr-compress-preserve-resume/2026-08-19-test-log.md` (a real transcript, not a description): cloned into `sandbox/cpr-compress-preserve-resume/`, installed into a scratch project, and exercised for real — project-root detection, session-log folder creation, the "summary-only, stop before `## Raw Session Log`" read contract (confirmed via `awk`, 26/29 lines), and the 280-line archive-budget check (`wc -l` → 8, correctly not triggering).
- **What was adopted into the hand-authored trio:** `AskUserQuestion` multi-select (replacing free-text prompts), `allowed-tools:` frontmatter, the concrete 280-line/archive-file budget for `/preserve` (adapted to archive into `60_Claude/Sessions/_archive/`, not the source repo's bare `CLAUDE-Archive.md`), topic-named session-log filenames, and `/resume`'s topic-keyword grep search.
- **What was deliberately not adopted:** `model: opus` pinning (this repo's other commands don't pin models), full raw-conversation logging (conflicts with this repo's "structured-summary-only" session-log principle), and per-project-root detection via `CC-Session-Logs/` (superseded by the fixed `60_Claude/Sessions/` path this repo already anchors to).
- **Old hand-authored trio:** not deleted — archived to `.claude/_archive/superseded-commands/`.
- **Open, not resolved:** this folder sits at a literal two-level path (`tested-tools/commands/cpr-compress-preserve-resume/`), not the three-level `tested-tools/<type>/<use-case>/<repo>/` convention `tested-tools/README.md` states elsewhere. Flagged inside `VERDICT.md` itself, not silently fixed — a future pass should either rename it under a `session-continuity/` use-case layer or amend the convention to allow two levels when one tool *is* the use case.

### Native-scaffold relocation (batch — 15 files, 2026-08-19)
- **What:** The repo's top-level `agents/` (4 files: `connector`, `researcher`, `reviewer`, `writer`), `commands/` (8 files: `brainstorm`, `capture`, `connect`, `inbox-process`, `journal`, `research`, `review`, `summarize`), and `hooks/` (3 files: `auto-link`, `daily-summary`, `post-note-create`) — all traced to the repo's very first scaffold commit (`d35f0b7`, 2026-04-03), confirmed zero external provenance by cross-referencing distinctive phrases against every repo in `sandbox/` and `tested-tools/` (zero matches).
- **Useful for:** N/A — parked as native scaffold, not a tool being qualified for use.
- **Pipeline stage:** Relocated to `tested-tools/{agents,commands,hooks}/native-scaffold/`, per Anant's `AskUserQuestion` decision to bucket them together rather than review individually. Verified by direct listing 2026-08-19: exactly 4 + 8 + 3 = 15 files present at those three paths.
- **Why this matters for the top-level folders:** their retirement (below) is a direct consequence of this relocation — both provenance groups that used to sit flat in `agents/`, `commands/`, `hooks/` (this batch, plus the CPR trio above) are now resolved, which is what let those folders be repurposed.

### ECC (affaan-m/everything-claude-code)
- **What:** Cross-harness agent operating system — 67 agents, 281 skills, 94 legacy command shims, hooks, rules, MCP configs, AgentShield security scanning, and a Memory Vault. ECC 2.0 additionally ships a Rust-based control-plane scaffold (`ecc2/`, in-tree, builds locally): terminal UI dashboard, SQLite session store, background daemon mode. Alpha quality per its own README, not GA.
- **Useful for:** Undetermined at the whole-repo level — real testing has started but the "does this close a named gap nothing else already closes" question (Promotion-Criteria.md Q2/Q3) hasn't been answered for any specific component yet.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/ecc/` — real `git clone` (2026-07-30, in addition to the pre-existing WSL clone at `~/projects/ai/claude/everything-claude-code/`, kept separate rather than reused, per this repo's own "nothing skips sandbox/" rule). `npm install --no-audit --no-fund` completed clean (210 packages — the repo is markdown-heavy, not dependency-heavy: 3 runtime deps, 8 devDeps). `node tests/run-all.js` (the repo's own documented test command) run for a real pass/fail signal.
- **Real finding, new to this pipeline:** merely cloning ECC into `sandbox/ecc/` caused Claude Code to auto-load its `CLAUDE.md`, `.claude/rules/*.md`, and register a `.claude/skills/everything-claude-code` skill into the active session — no explicit install step required. This means `Docs/Architecture.md`'s assumption that `sandbox/` is inert until deliberately run is **false** for any tool shipping its own `CLAUDE.md`/rules/skills — Claude Code's own config auto-discovery already "runs" part of it just by existing on disk inside the project. Flagged for a correction to `Docs/Architecture.md`.
- **Scope discipline (per Docs/Design.md, Implement > Knowledge):** ECC's catalog (67 agents/281 skills/94 commands) is large enough that wholesale install (`./install.sh --profile full`) would itself be the anti-pattern this repo's philosophy exists to prevent. The real next decision is which specific named gap(s), if any, ECC's components close that nothing already-adopted (gbrain, mattpocock-engineering, this repo's own `/challenge` `/ideas` `/strategy` `/llm-council` skills) already closes — not "install all of it because the catalog is large." Not yet decided.
- **Next:** Identify 2-4 specific ECC components (an agent, a skill, a hook pattern) worth reviewing individually against a real gap, rather than evaluating all 442 components at once.

- **Real test results (2026-07-30):** `node tests/run-all.js` — **3378/3388 passed (99.7%), 10 failed, exit 0.** All 10 failures isolated to two files, not scattered: 9 in `integration/plan-canvas-e2e.test.js` (ECC 2.1's browser-based "Plan Canvas" review feature — every failure traces to `connect ETIMEDOUT 127.0.0.1:21517`, a local detached server never coming up in this sandboxed WSL environment; looks environment-specific, same shape as gstack's Playwright/Chromium blocker, not a confirmed ECC bug) and 1 in `lib/dry-run.test.js` ("--dry-run works with implicit install routing" — `Expected exit 0, got null`, not yet root-caused). Per Promotion-Criteria.md Q1 ("did it actually run without a manual workaround") this is an honest **partial-yes**: the core test suite runs clean; one experimental feature (Plan Canvas) and one dry-run edge case do not, named and specific rather than glossed over.

##### agent-skills (Addy Osmani)
- **What:** Agent skills collection from Addy Osmani.
- **Useful for:** Undetermined — clone only.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/agent-skills/` — `git clone --depth 1` only (2026-07-30). No install/run yet.
- **Upstream:** https://github.com/addyosmani/agent-skills

##### andrej-karpathy-skills
- **What:** Karpathy-style skills pack (multica-ai mirror/pack).
- **Useful for:** Undetermined — clone only.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/andrej-karpathy-skills/` — clone only (2026-07-30).
- **Upstream:** https://github.com/multica-ai/andrej-karpathy-skills

##### claude-skills-llm-council + llm-council (Karpathy original)
- **What:** LLM Council as Claude skills (`aiwithremy/claude-skills-llm-council`) plus the original Karpathy repo (`karpathy/llm-council`). Both cloned so they can be compared side by side.
- **Useful for:** Undetermined — this repo already has a `/llm-council` skill; need a real gap check before any promotion.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/claude-skills-llm-council/` and `sandbox/llm-council/` — clone only (2026-07-30).
- **Upstream:** https://github.com/aiwithremy/claude-skills-llm-council · https://github.com/karpathy/llm-council

##### last30days-skill
- **What:** Skill for researching / summarizing the last 30 days of a topic.
- **Useful for:** Undetermined — clone only.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/last30days-skill/` — clone only (2026-07-30).
- **Upstream:** https://github.com/mvanhorn/last30days-skill

##### spec-kit
- **What:** GitHub Spec Kit — spec-driven development tooling.
- **Useful for:** Undetermined — clone only. Previously listed as Tier-1 unexecuted in Design.md history.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/spec-kit/` — clone only (2026-07-30).
- **Upstream:** https://github.com/github/spec-kit

##### claude-context (Zilliz)
- **What:** Semantic code context for Claude / agents.
- **Useful for:** Marked **to use** — not just reference.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/claude-context/` — clone only (2026-07-30). Next: real install/run per Promotion-Criteria.
- **Upstream:** https://github.com/zilliztech/claude-context

##### graphify
- **What:** Build knowledge graphs from content (code, docs, papers, etc.).
- **Useful for:** Marked **to use** — local skill already exists at `~/.claude/skills/graphify`; sandbox clone is for qualification before trusting/promoting further.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/graphify/` — clone only (2026-07-30).
- **Upstream:** https://github.com/safishamsi/graphify

##### claude-code-best-practice
- **What:** Claude Code best-practice / learning reference guide.
- **Useful for:** Learning reference — not expected to install as runtime tooling.
- **Global vs. project-scoped:** N/A (reference).
- **Pipeline stage:** `sandbox/claude-code-best-practice/` — clone only (2026-07-30). Note: `Docs/Design.md` previously said reference-only repos stay out of sandbox; explicitly requested in on 2026-07-30.
- **Upstream:** https://github.com/shanraisshan/claude-code-best-practice

##### system-prompts-and-models-of-ai-tools + CL4R1T4S
- **What:** Large system-prompt corpora — compare the two for the best prompts when guardrail-bypass phrasing is needed for legitimate eval/red-team work.
- **Useful for:** Reference / prompt craft — not runtime install.
- **Global vs. project-scoped:** N/A (reference).
- **Pipeline stage:** `sandbox/system-prompts-and-models-of-ai-tools/` and `sandbox/CL4R1T4S/` — clone only (2026-07-30).
- **Upstream:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools · https://github.com/elder-plinius/CL4R1T4S

##### agentscope
- **What:** AgentScope multi-agent framework.
- **Useful for:** Reference for agent architectures — clone for study, not necessarily promote.
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/agentscope/` — clone only (2026-07-30).
- **Upstream:** https://github.com/agentscope-ai/agentscope

##### promptfoo
- **What:** Prompt / agent evaluation and scanning toolkit.
- **Useful for:** Marked **to use** — better agent structures and scans.
- **Global vs. project-scoped:** Not decided (likely global if it clears the bar).
- **Pipeline stage:** `sandbox/promptfoo/` — clone only (2026-07-30). Large shallow clone (~417M).
- **Upstream:** https://github.com/promptfoo/promptfoo

##### hiring-agent
- **What:** InterviewStreet hiring agent.
- **Useful for:** Evaluate usefulness for the internship research loop (`internship-research-loop`).
- **Global vs. project-scoped:** Likely project-scoped to internship work if useful.
- **Pipeline stage:** `sandbox/hiring-agent/` — clone only (2026-07-30). Next: run and decide.
- **Upstream:** https://github.com/interviewstreet/hiring-agent

##### autoresearch (Karpathy)
- **What:** Karpathy autoresearch — autonomous research loop.
- **Useful for:** Clone then implement against real use cases (not promote blindly).
- **Global vs. project-scoped:** Not decided.
- **Pipeline stage:** `sandbox/autoresearch/` — clone only (2026-07-30).
- **Upstream:** https://github.com/karpathy/autoresearch

##### TradingAgents
- **What:** Multi-agent LLM trading research framework (TauricResearch).
- **Useful for:** Trading / markets experiments; pair with OpenBB review for TradingView.
- **Global vs. project-scoped:** Likely project-scoped (TradingView / markets).
- **Pipeline stage:** `sandbox/TradingAgents/` — clone only (2026-07-30).
- **Upstream:** https://github.com/TauricResearch/TradingAgents

##### OpenBB
- **What:** OpenBB finance platform / SDK.
- **Useful for:** Review for TradingView project (data/platform patterns), not a Claude Code skill promotion candidate by default.
- **Global vs. project-scoped:** Project-scoped (TradingView) if anything is adopted.
- **Pipeline stage:** `sandbox/OpenBB/` — clone only (2026-07-30). Large shallow clone (~345M).
- **Upstream:** https://github.com/OpenBB-finance/OpenBB

## Not yet in `sandbox/` at all
Everything else in [[40_Resources/CS/Repos]] not named above — still starred, still where earlier GitHub ingestion left it. The 2026-07-30 batch (agent-skills through OpenBB, 17 new clones) is now in `sandbox/` as clone-only; none have been run for real yet. Update clones with `second-brain-claudekit/50_Claude/scripts/update-sandbox.sh`; inventory lives in `sandbox/README.md`.
