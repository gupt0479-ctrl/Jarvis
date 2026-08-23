---
type: input
status: active
created: 2026-08-11
updated: 2026-08-22
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]]"
next: "Round 8, 2026-08-21 — instructions/ scope corrected for the third time, mechanism fixed so it can't recur. Codebase: fresh session. Jarvis: fresh Windows session, short, verification-only. After this: tests/ refinement is the next real phase."
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==
## Sequencing
**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Round 8, 2026-08-21 — fresh session.** Round 7 fixed the self-nesting bug but kept the wrong scope: `_docs` as a directory-shaped `instructions_paths` entry, flattened wholesale into `instructions/second-brain-claudekit/`. That was never the intent. `instructions/<repo>/` is a small, curated set of main files only — `CLAUDE.md`, `AGENTS.md`, `README.md`, `PRD.md`, `Architecture.md` (now confirmed at this repo's root, not in `_docs/`) — never an entire internal-documentation directory. This is the fourth time this folder's scope has needed correcting; this round makes the mechanism itself incapable of the mistake, not just the current data.

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`, `high` or `xhigh` effort.

```
Read sync-manifest.json fresh before anything else. The final rule, confirmed directly by Anant: instructions_paths (whatever the exact field is called — confirm from the real file) may only ever list explicit file paths, never a directory. A "main file" is a single top-level instruction/context document -- CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, or a real equivalent -- never an entire folder of internal reasoning docs (this repo's own _docs/, or a project's .claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows -- all directory-shaped, all the same class of mistake).

## 1. Simplify sync-all.sh: remove directory-flattening entirely

Round 7 added logic to sync-all.sh that resolves a directory-shaped instructions_paths entry into its real files and flattens them. Delete that logic. instructions_paths should only ever process explicit file entries -- copy each one flat into instructions/<repo>/<basename>.md, keeping the existing claude-<filename>.md prefix for a nested-vs-root name collision. If a directory-shaped entry is ever found in the manifest going forward, that's a data error to fix in the manifest, not something the script should try to handle gracefully.

## 2. Fix second-brain-claudekit's own entry

Remove _docs entirely from its instructions_paths. Confirm the real current root files (expected: CLAUDE.md, README.md, PRD.md, Architecture.md -- verify this list directly, don't assume) and set instructions_paths to exactly those, as explicit file entries.

## 3. Audit all 10 entries for the same mistake

Check every entry's instructions_paths for any directory-shaped entry. Resq and OpsPilot are the known suspects (.claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows all appear in their general paths lists -- confirm whether any of those also ended up in instructions_paths specifically, not just the general sync paths). Remove any directory entry found; keep only genuine main files (CLAUDE.md, AGENTS.md, README.md, PRD.md/README.md nested under .claude/ where that's the real pattern, per the already-established collision-prefix convention).

## 4. Rebuild every affected instructions/<repo>/ folder

For second-brain-claudekit and any other entry fixed in item 3: delete whatever landed there from a directory flatten that shouldn't have happened, and re-populate from the corrected, file-only instructions_paths list. Confirm the result is small and curated -- if any instructions/<repo>/ folder still has more than a handful of files after this, that's a signal something's still wrong, go back and check.

## 5. Write the definitive, final rule -- for real this time

Update _docs/Sync.md, 60_Claude/vault-rules/write-contract.md, and 60_Claude/vault-rules/pipeline-conventions.md with one unambiguous statement: instructions/<repo>/ holds only explicit main files (CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, and real equivalents) -- never a directory's contents, never an internal-documentation folder, no matter how relevant that folder seems. This scope has been corrected three times already; state it precisely enough that a fourth correction shouldn't be needed.

## 6. Close the loop

Update _docs/Gaps.md and _docs/Repo-Map.md with the real fix across all 10 entries. Review the diff for secrets before committing. Commit in logically separated commits.

Apply items 1-4 to all 10 entries, not just second-brain-claudekit -- the mechanism fix in item 1 should make this structurally impossible to get wrong again, verify that it actually does.
```

# Jarvis

**Round 8, 2026-08-21.** Short and verification-only — the sync-build phase is closing out and the next real work is `tests/`. Don't add new scope here.

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort.

```
A parallel codebase round is fixing instructions/<repo>/'s scope for the third time: it should only ever hold explicit main files (CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md), never an entire directory's contents (this repo's own _docs/ was wrongly flattened in there; Resq/OpsPilot's .claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows are being audited for the same mistake). sync-all.sh's directory-flattening logic is being removed entirely, not patched, so this class of bug becomes structurally impossible.

1. Verify it landed, for real -- check the actual repo (via the WSL UNC path or the mirror, whichever is genuinely current) for instructions/second-brain-claudekit/: it should hold a small handful of files (CLAUDE.md, README.md, PRD.md, Architecture.md), nothing from _docs/. If it still shows the old, over-populated state, or you can't confirm either way, say so plainly rather than assuming the fix landed.

2. Add one closing line to Log.md's sync-build entry from last round, noting this was the third and (per the mechanism fix) final correction to instructions/'s scope, with the real verification result from item 1.

3. Confirm this pipeline is actually ready to move to tests/ next: read tests/'s current real content (still just the two entries from 2026-08-19/20 last checked) and confirm _docs/Gaps.md still correctly flags it as needing a real refinement pass. Don't start that work here -- just confirm the handoff is accurate before the next round picks it up.

Report item 1's real finding first -- that's the one that matters most this round.
```

# Cursor — Grok 4.6 → Sonnet 5

**2026-08-22 — WSL + Windows global-config setup, two-phase handoff.** Scope: the two OS home directories' own AI-tool dotfile config (`~/.claude`, `~/.cursor`, etc. on WSL; `C:\Users\Anant Gupta\.claude` on Windows) — never a project repo under `~/projects/`. Two prompts, run in sequence, different models: **Grok 4.6 plans, Sonnet 5 executes.** Grok never edits anything; it only investigates and writes one plan file. Sonnet reads that plan file, independently re-verifies each claim against the real filesystem (a Grok-authored plan is a proposal, not ground truth), and only then applies it — showing the diff and stopping for confirmation before anything is written. Background: [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]], [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]].

**Known lead to hand Grok, already verified 2026-08-22 (don't make it re-derive this from scratch):** `~/.claude/settings.json`'s `autoMode.environment` and `autoMode.soft_deny` blocks are entirely about one specific repo — `internship-research-loop` / `gupta-builds` (branch protection, CI secrets, the Jarvis-vault promote-dossier consent flow, etc.) — sitting at the GLOBAL settings level, where every project's session inherits it. That's the concrete shape of the problem this task is solving; there are likely more instances like it.

## Prompt 1 — Grok 4.6, planning only

```
Role: You are working inside Cursor with the Grok 4.6 model, directly on Anant's machine — NOT inside a project repo. You investigate and PLAN. You do not edit, move, or delete anything. That is a separate, later step done by a different model.

<scope>
Two home directories, their own dotfile config only:
- WSL (Ubuntu 24.04): `/home/anant_gupta` (Cursor path: `\\wsl$\Ubuntu\home\anant_gupta`)
- Windows: `C:\Users\Anant Gupta`
Out of scope, do not open or read into for editing purposes: anything under `~/projects/` (or its Windows equivalent) — those are real, independent git repos, each already carrying its own project-scoped `.claude/`/`.cursor/`/`.kiro/`.
</scope>

<context>
WSL side (primary, well-developed):
- `~/.claude/` — CLAUDE.md is 226 bytes (only a graphify skill-trigger rule). agents/ has 3 files (all Obsidian-vault-specific: obsidian-architect, obsidian-researcher, obsidian-session-archivist). commands/ has 7 (obsidian-daily-review, obsidian-session-review, second-brain-capture/compress/graduate/resume/review). skills/ has 28, mostly Cloudflare platform skills plus per-course/per-project Obsidian helpers.
- `~/.claude/settings.json` sets `"model": "sonnet"` globally already, plus real PostToolUse/Stop/SessionEnd hook bindings (after-edit-log.ps1, wsl-session-export.ps1, session-wrapup.ps1 — confirm these three scripts still exist in ~/.claude/hooks/ and actually get invoked correctly), several enabled plugins, and an `autoMode` block. VERIFIED PROBLEM: `autoMode.environment`/`autoMode.soft_deny` in this global file are entirely about ONE repo (internship-research-loop/gupta-builds) — branch protection notes, CI secret names, a Jarvis-vault consent flow specific to that project. That has no business being global; find out whether Cursor/Claude Code's own auto-mode config supports a project-local override file instead, and where a repo-specific block like this actually belongs.
- `~/.mcp.json` and `~/.cursor/mcp.json` — global MCP servers (jarvis, the-plan, jarvis-fs, the-plan-fs, github). HOLD LIVE BEARER TOKENS AND A GITHUB PAT IN PLAINTEXT. Never print, log, quote, or copy any part of either file's contents anywhere — not into the plan file, not into chat output, not even a redacted-looking excerpt.
- `~/.cursor/`, `~/.codex/`, `~/.gemini/`, `~/.kiro/`, `~/.copilot/`, `~/.agents/` — parallel config for other AI tools already in real use here. Note what's there; don't restructure unless the plan explicitly proposes it.

Windows side (thin, confirmed nearly empty as of 2026-08-20):
- `C:\Users\Anant Gupta\.claude\` has no agents/, no hooks/, an empty commands/, no CLAUDE.md, and skills/ with exactly one real folder (export-ai-session/) plus ~30 firecrawl-* symlinks pointing outside .claude/ (leave those symlinks alone — don't even read through them).
</context>

<task>
1. Re-verify everything in <context> against what's actually there right now on both sides — correct anything stale.
2. Find every other instance of the same problem as the autoMode finding above: global config (CLAUDE.md, any agent, any command, any skill, any settings.json block) that is actually specific to one project, one course, or one narrow use case, masquerading as global. Sorting rule: something belongs at GLOBAL scope only if it's useful with no regard to which project is currently open.
3. Write ONE plan file and nothing else:
   - WSL: `~/.claude/_global-config-plan.md`
   - Windows: `C:\Users\Anant Gupta\.claude\_global-config-plan.md`
   (two separate plan files, one per OS, since you're covering both)
4. The plan file must be concrete and directly executable by someone who has NOT done your investigation: for every change, name the exact file, the exact before-state, the exact after-state (full replacement text for anything under ~30 lines, a precise diff/instruction for anything longer), and which of the two rules justified it (global-vs-project-scoped, or "genuinely stale/broken, confirmed by direct read"). No vague items like "clean up skills" — each skill/agent/command gets its own named verdict: keep global / push to project X's `.claude/` / delete (with why).
5. Do not write, move, or delete anything else. Do not touch `~/projects/`. Do not touch the firecrawl-* symlinks.
</task>

<style>
Iterate fast — a solid first-pass plan beats an internally-perfected one. Structure the plan file with clear markdown headers per area (CLAUDE.md / agents / commands / skills / settings.json / MCP config), not prose paragraphs.
</style>
```

## Prompt 2 — Sonnet 5, execution only

```
Role: You are Claude Code running Sonnet 5, in Cursor, directly on Anant's machine -- NOT inside a project repo. A separate Grok 4.6 planning pass already investigated and wrote two plan files. Your job has two phases: CORRECT the plan until every item is verified-true, then EXECUTE exactly the corrected plan. Finish phase 1 completely and show it before starting phase 2 -- don't blend them.

<input>
Read both plan files in full before doing anything else:
- WSL: `~/.claude/_global-config-plan.md`
- Windows: `C:\Users\Anant Gupta\.claude\_global-config-plan.md`
If either is missing, stop and say so -- don't improvise a plan yourself.
</input>

<phase-1-correct>
Treat the plan as a first draft written by a different model, not as ground truth -- even though it looks thorough and cites its own verification date. Go through it item by item:

1. For every "Before" state the plan quotes (file contents, byte sizes, mtimes, directory listings, "X exists" / "X does not exist" claims) -- re-read the real file or directory right now and confirm it matches exactly. If it doesn't, correct that item's Before/After text in the plan file itself to the real current state, and re-derive whether the item's verdict (KEEP GLOBAL / PUSH TO VAULT / DELETE / fix-in-place) still holds given the corrected facts.
2. For every factual claim about how Claude Code, Cursor, or their config format actually behaves (e.g. "Claude Code does not support project-local autoMode", "removed in v2.1.207", which env-var reference syntax Claude Code's MCP loader accepts, hook input arriving as JSON on stdin vs. environment variables) -- verify it against the live Anthropic docs per `60_Claude/vault-rules/anthropic-docs-reference.md` (`WebFetch https://platform.claude.com/llms.txt`, then the specific relevant page) rather than trusting the plan's citation. Correct the plan file in place if the docs say otherwise. This matters most for the MCP env-var reference syntax and the autoMode scoping rule -- both are easy to get subtly wrong and hard to notice broken later.
3. Flag and correct (or remove) any instruction in the plan that would touch something explicitly off-limits: anything under `~/projects/` other than the one named `internship-research-loop/CLAUDE.md` append, any `firecrawl-*` symlink, or any instruction that would print/log/quote a literal MCP secret value -- including inside the plan file itself.
4. Once every item is either confirmed-accurate or corrected in place, the plan file should read as a fully verified, standalone source of truth -- no "the plan says X but actually Y" gap left anywhere in it.
5. Show the full set of corrections you made, as a diff-style summary, file by file, item by item. If you made zero corrections, say that explicitly rather than silently skipping this report.
</phase-1-correct>

<phase-2-execute>
Only after phase 1's corrections are shown:
1. Apply exactly what the corrected plan specifies -- no extra cleanup, no scope creep, nothing the plan doesn't call for, in the order the plan lists it.
2. For the MCP secret migration specifically: move real values into the env file the plan names (creating it from the existing `.example` file's shape), rewrite the JSON to reference them, then grep every touched JSON file for secret-shaped literals (`Bearer `, `ghp_`, `sk-`) and confirm that grep is empty before considering that item done.
3. Before writing anything, show the full set of changes as a diff-style summary (file, before, after) and stop for explicit confirmation. This touches global config every project inherits, plus live credentials -- apply nothing until confirmed.
4. After applying, once confirmed correct, run the plan's own named final-state checks (e.g. the MCP secret grep, any "should hold N files" sanity check), then delete both `_global-config-plan.md` files -- they're scratch artifacts, not something that should linger in `.claude/`.
</phase-2-execute>

<constraints>
- Never modify anything inside ~/projects/ except the one named CLAUDE.md append the plan specifies.
- Never print, log, or write any MCP config file's secret values anywhere, even partially -- not in chat, not in the plan file, not in a commit.
- Don't touch any firecrawl-* symlink.
- If phase 1 finds the plan's core approach is wrong in a way that's more than a fact-level correction (a verdict's whole premise no longer holds, not just a stale detail), stop and report that instead of forcing an execution -- that's a re-plan, not a correction.
</constraints>
```
