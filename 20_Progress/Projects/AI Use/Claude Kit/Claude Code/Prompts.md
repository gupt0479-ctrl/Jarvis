---
type: input
status: active
created: 2026-08-11
updated: 2026-08-21
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session
    Context]]"
next: "Round 8, 2026-08-21 — instructions/ scope corrected for the third time,
  mechanism fixed so it can't recur. Codebase: fresh session. Jarvis: fresh
  Windows session, short, verification-only. After this: tests/ refinement is
  the next real phase."
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
