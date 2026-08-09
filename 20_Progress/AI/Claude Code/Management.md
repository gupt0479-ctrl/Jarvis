---
type: project
status: active
created: 2026-07-30
updated: 2026-07-30
tags:
  - claude-code
  - management
  - sync
  - claude-kit
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[20_Progress/AI/Claude Code/Write Log]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[Tool Map]]"
next: Get Anant's per-project go-ahead for the multi-project sync rollout (Sync - Unison.md, Step 0), then this file's blocker list shrinks by one row
---
# Claude Code — Management

The single current-status page for everything happening across this vault's Claude Code tooling — sync health, active blockers, and recent findings. [[20_Progress/AI/Claude Code/Write Log]] is the append-only chronological record this page summarizes; this page is the living, overwritten-in-place snapshot. [[20_Progress/AI/Claude Code/MOC]] is the per-project file inventory; [[Tool Map]] is the second-brain-claudekit tool-pipeline tracker (gbrain/gstack/mattpocock/ECC). None of the four duplicate each other — this one answers "what's the state right now," today.

## Sync status

**Mechanism:** Unison (`~/.local/bin/unison`, static binary, no root), driven by `second-brain-claudekit/50_Claude/scripts/sync-jarvis.sh`. Full research and tool-choice writeup: `second-brain-claudekit/Docs/Sync.md`. Real, tested: install, first sync, reverse-direction sync, and a genuine same-file-both-sides conflict (skipped and reported, not overwritten) — all verified for real on 2026-07-30, not simulated.

**Trigger:** Windows Task Scheduler task `SecondBrainClaudekit-JarvisSync`, created 2026-07-30. Runs `wsl.exe -d Ubuntu -- bash -lc '.../sync-jarvis.sh'` every **15 minutes**, indefinitely, "Logon Mode: Interactive only."

**How many times a day, honestly:** Not a flat number. Every-15-minutes caps out at 96 runs in a full 24-hour period *if* logged in continuously, but "Interactive only" means it only fires while Anant is actually logged into Windows — so the real daily count is bounded by logged-in hours, not a fixed schedule. The actual per-day count for any given day is verifiable, not estimated: count the timestamped lines in `20_Progress/AI/Claude Code/second-brain-claudekit/Sync-Log.md` (one line per run, `OK`/`CONFLICTS`/`TRANSFER ERRORS`/`FATAL` + exit code). Currently only `second-brain-claudekit` is wired to this trigger — see the rollout plan in [[20_Progress/AI/Claude Code/Sync - Unison]] for scaling this to every other project.

**Scope today:** Only `second-brain-claudekit`'s `.claude/{agents,commands,hooks,settings.json}` + root `CLAUDE.md`. Every other project listed below is mapped (real path, real git remote, real `.claude/` contents confirmed) but still `status: candidate`, not `status: live` — per [[20_Progress/AI/Claude Code/Sync - Unison]]'s Step 0, nothing goes live without an explicit per-project go-ahead first.

## Active blockers

| Blocker | Where | What's actually blocking it |
|---|---|---|
| gstack Chromium launch | `second-brain-claudekit/sandbox/gstack/` | Missing WSL system libs (`libnss3`, `libatk1.0-0`, etc.) — needs an interactive `sudo apt-get install` that hasn't been run |
| gbrain embedding provider | `second-brain-claudekit/sandbox/gbrain/` | Real, named cost/vendor decision (Voyage / ZeroEntropy free tier / OpenAI paid) — not a technical blocker, a choice not yet made |
| ECC scope | `second-brain-claudekit/sandbox/ecc/` | Identity resolved, core tests pass (3378/3388), cross-harness-portability angle evaluated and dropped (2026-07-30) — still open: which other named gap, if any, ECC's 67 agents/281 skills actually close |
| Multi-project sync rollout | `20_Progress/AI/Claude Code/Sync - Unison.md` | Every other project (CausalOps, Portfolio, Trading View, Resq, OpsPilot, Jarvis itself) is mapped and ready but needs Anant's explicit per-project go-ahead (Step 0) before any of them flips from `candidate` to `live` |
| mattpocock-skills remaining categories | `second-brain-claudekit/tested-skills/mattpocock-engineering/` | Only `engineering/` (17 of 41 skills) reviewed; `personal`/`productivity`/`misc`/`in-progress`/`deprecated` untouched |

## Recent findings (2026-07-30)

- **Claude Code's `sandbox/` isn't actually inert.** Cloning ECC into `second-brain-claudekit/sandbox/ecc/` auto-loaded its `CLAUDE.md`/`.claude/rules/`/skills with zero install step — confirmed against official docs, not assumed. Partial fix applied (`claudeMdExcludes` in that repo's `.claude/settings.json`); no fix exists for the rules/skills vector, documented as accepted residual risk in that repo's `Docs/Architecture.md`.
- **ECC identity, re-corrected.** `ecc2` is genuinely `affaan-m/everything-claude-code`'s own tracked ECC 2.0 Rust control-plane component, not an unrelated project — the 2026-07-29 note that said otherwise was itself wrong (it checked the leaf directory, not the parent repo's git remote). Fixed in [[40_Resources/CS/Repos]] and [[Tool Map]].
- **`/challenge` and `/strategy` (Jarvis `.claude/skills/`) — confirmed real, complete, not stubs.** A same-day contradiction in the vault's own notes (one said built, one said still-pending) is resolved: both files are real, dated 2026-07-29, fully operational.
- **Four real drift items found in Jarvis's own `.claude/` folder, not yet fixed (Anant's call, not fixed silently):**
  1. `skills/mcp-hub.md` has no matching `commands/mcp-hub.md` pointer — `/mcp-hub` may not be invocable as a slash command.
  2. `agents/anti-slop-editor.md` and `skills/remove-ai-slop.md` do the same job independently, with no delegation between them despite the agent's frontmatter implying there should be.
  3. `skills/startday/reference.md` still hardcodes old numbered-file paths (e.g. `08 - Anti-Drift Rules.md`) that the vault reorg removed, contradicting its own `SKILL.md`'s currency disclaimer.
  4. `skills/closeday/reference.md` still tracks `MATH 2230`/`HIST 1103` as active courses; `weekly-review.md` (2026-07-27) says both are complete.
  5. `.claude/README.md` documents `SessionStart`/`SessionEnd` hooks not present in the real `settings.json` (only a `PreToolUse` write-guard is registered).

## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude Code/Write Log]] · [[20_Progress/AI/Claude Code/Sync - Unison]] · [[Tool Map]] · [[20_Progress/Projects/AI Use/Claude Kit/Log]]
