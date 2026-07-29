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

### ECC (affaan-m/ECC)
- **What:** Cross-harness agent operating system — 261 public skills, Claude Code/Codex/OpenCode/Cursor/Gemini/Zed support, a `worktree-lifecycle` service for parallel-agent conflict prediction.
- **Useful for:** Undetermined — real install state was never established this session.
- **Global vs. project-scoped:** Not decided — blocked on the correction below, not on a usefulness question.
- **Pipeline stage:** **Undecided, not started.** `everything-claude-code/ecc2` in `~/projects/ai/claude/` (the sibling of `second-brain-claudekit`) turned out to be an *unrelated Rust project* with a coincidentally similar name — not affaan-m/ECC. This was a real correction made this session, not a footnote: earlier vault notes assumed ECC was installed via this folder, and it isn't. `second-brain-claudekit/CLAUDE.md` now explicitly flags this folder as off-limits to avoid the same mistake recurring.
- **Next:** Actually clone `affaan-m/ECC` into `sandbox/` before any further decision — nothing about it has been tested for real yet.

## Not yet in `sandbox/` at all
Everything else in [[40_Resources/CS/Repos]] not named above — still starred, still exactly where the 2026-07-29 GitHub ingestion pass ([[00_Execution#Github|00_Execution's Github section]]) left it. Not forgotten, just genuinely not ingested into this repo yet.
