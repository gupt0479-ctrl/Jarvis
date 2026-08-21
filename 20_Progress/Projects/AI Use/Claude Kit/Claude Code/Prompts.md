---
type: input
status: active
created: 2026-08-11
updated: 2026-08-20
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
next: "Round 6, corrected, 2026-08-20. Both are independent, fresh sessions.
  Codebase: cwd = second-brain-claudekit, verify HEAD cea5ab0. Jarvis: cwd =
  Jarvis vault root, Windows. tests/ refinement and the third sync hop (Jarvis
  -> real project .claude/) are both explicitly out of scope for this round."
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==
## Sequencing
**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Round 6, corrected, 2026-08-20 — fresh session.** The previous version of this round's prompt was wrong about `skills/` (treated it as source-repo staging; it's actually live-synced, same as `agents/`, `commands/`, `hooks/`, `instructions/`) and only designed the live-sync leg instead of wiring it. Never ran — this replaces it, not round 7. HEAD should still be `cea5ab0` unless something else has landed since.

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`, `high` or `xhigh` effort.

```
Confirm HEAD with git log before starting; report if it's not cea5ab0 rather than assuming this description still matches.

The corrected model, confirmed directly by Anant, governs everything in this session:

sandbox/<repo>/ -> tested for real -> tested-tools/<type>/... or tested-tools/_future/<repo>/. NEITHER of these is ever live-synced with Jarvis. Moving something from tested-tools/ into a live folder is a manual, per-item, human decision -- you do not take this step for any specific piece of content in this session unless explicitly told to for that exact item. This session is about fixing the SYNC MECHANISM for content already decided ready, not promoting anything new.

Once something is explicitly decided ready, it lives in agents/<Project>/, commands/<Project>/, hooks/<Project>/, skills/<Project>/, and instructions/<Project>/ -- all five are live-synced with Jarvis via 60_Claude/scripts/sync-manifest.json and sync-all.sh. Jarvis mirrors these read-only.

Ten real entries need full, correct, live-synced coverage: second-brain-claudekit (this repo itself), CausalOps, Jarvis, Portfolio, Trading View, Resq, OpsPilot, The Plan, .claude_windows, .claude_wsl. Read 60_Claude/scripts/sync-manifest.json directly and confirm this list and each entry's current paths before doing anything else -- the specifics below are from an earlier direct read and may have drifted.

## 1. Fix the manifest for real, not just design it

- Remove .claude/settings.json from every entry that has it (confirmed earlier: second-brain-claudekit, Jarvis, Trading View, Resq, The Plan -- verify this list is still accurate against your own fresh read). Settings and secrets are never synced, no exceptions, confirm this is true for all 10 entries, not just the 5 already flagged.
- Add README.md to every one of the 10 entries' paths list. This was missed entirely until now.
- second-brain-claudekit's own entry: add _docs/** (the real files there today: PRD.md, Architecture.md, Design.md, Promotion-Criteria.md, Sync.md, Jarvis.md, Repo-Map.md, Gaps.md, Current-Setup.md, Repo-Map-Archive.md, Gaps-Archive.md -- confirm this list is current, it may have grown) so Jarvis finally has visibility into this repo's own governing docs.
- For .claude_windows and .claude_wsl specifically: confirm their current paths (agents, commands, skills, hooks, CLAUDE.md per the last direct read) are complete and correct -- these are the two global home directories and Anant has flagged them as currently too thin; make sure nothing real is missing from what should sync (check the actual home directory contents if reachable from this WSL session -- ~/.claude for WSL directly, /mnt/c/Users/"Anant Gupta"/.claude for the Windows one).

## 2. Build out all five live-sync folders for every one of the 10 entries, for real

For each of the 10 entries, based on what its manifest paths actually contain (do not assume every project has every category -- read each entry's real paths list and derive the correct category list per entry, some projects won't have all five):

- If the entry has an agents-shaped path: confirm/build agents/<EntryName>/ with real content matching what's actually promoted for that entry today (if nothing is promoted yet for that project, the folder is correctly empty -- do not invent placeholder content).
- Same pattern for commands/<EntryName>/, hooks/<EntryName>/, skills/<EntryName>/.
- instructions/<EntryName>/ gets every real instruction-shaped file for that entry -- CLAUDE.md, AGENTS.md, PRD.md, README.md (once added per item 1), and any nested .claude/-internal instruction file (Portfolio's .claude/CLAUDE.md and OpsPilot's .claude/PRD.md + .claude/README.md are the two already-known nonstandard cases -- confirm these are correctly represented, not skipped because they're nested).
- instructions/second-brain-claudekit/ specifically: this was wrongly excluded before on the reasoning that it would duplicate root CLAUDE.md. That reasoning is overridden -- every one of the 10 entries gets full, consistent treatment, this repo included. Build it with CLAUDE.md and the full _docs/ set from item 1.

Use a real discovery pass (list each entry's actual synced content, either via the Jarvis mirror or the real source path where directly reachable from this WSL session) -- do not guess what's promoted for a project from memory.

## 3. Do not touch the third hop

Jarvis mirrors reaching each real project's actual live repo is still an open question from a prior round, not answered yet. Do not wire anything that pushes content from a Jarvis mirror into a real project's actual .claude/ in this session, regardless of what you find. This session's scope ends at repo -> Jarvis mirror.

## 4. Close the loop

Update _docs/Gaps.md and _docs/Repo-Map.md with the real, complete state of all 10 entries after this session -- which categories exist for each, and confirm settings.json is gone from all 10. Note explicitly that tests/ needs a real refinement pass and is deferred to its own future session, not attempted here. Review the diff for secrets before committing (this session specifically touches sync-manifest.json and home-directory paths -- be careful). Commit in logically separated commits.

Apply every instruction above to all 10 entries, not a sample -- if you're tempted to handle 3 or 4 fully and wave at the rest, stop and do all 10.
```

# Jarvis

**Round 6, corrected, 2026-08-20.** Same correction as the codebase prompt: `skills/` is live-synced, not source-repo staging; `.claude_windows`/`.claude_wsl` need real depth, not just a mirror folder that exists. Never ran — replaces the previous version, not round 7.

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort.

```
The corrected model, confirmed directly by Anant: sandbox/ -> tested for real -> tested-tools/ (never live-synced) -> an explicit, per-item human decision -> agents/<Project>/, commands/<Project>/, hooks/<Project>/, skills/<Project>/, instructions/<Project>/ in second-brain-claudekit (all five live-synced) -> Jarvis mirrors these read-only under 20_Progress/AI/Claude Code/<Project>/. Ten entries: second-brain-claudekit, CausalOps, Jarvis, Portfolio, Trading View, Resq, OpsPilot, The Plan, .claude_windows, .claude_wsl.

## 1. Build real depth for the two home-directory mirrors

20_Progress/AI/Claude Code/.claude_windows/ and .claude_wsl/ are confirmed too thin as of today. List their real current contents directly. Compare against what should be there (agents, commands, skills, hooks, and now README.md per the parallel codebase-side fix -- confirm second-brain-claudekit's sync-manifest.json paths for these two entries once reachable, or work from real mirror contents if not). For whatever's genuinely thin or missing, build it out properly: the same "What Agents.md / How to Use Agents.md" depth the Toolkit/ folder already has for project-scoped tools, applied to these two home-directory-scoped entries specifically -- what's actually installed globally on each OS, distinguished clearly from project-scoped tooling, since a global skill and a project skill are different things and have been getting conflated. Real content only -- if something is genuinely sparse because nothing global has been promoted yet for one of the two, say that plainly rather than padding it.

## 2. Verify all 10 mirrors, not just the two home directories

For CausalOps, Jarvis, Portfolio, Trading View, Resq, OpsPilot, The Plan, and second-brain-claudekit: confirm each mirror folder's real content is current (cross-check against _All-Projects-Sync-Log.md's most recent entry per project, same method as before). Specifically confirm second-brain-claudekit's mirror now includes real content once the parallel codebase-side session adds _docs/** and expands its live-sync folders -- if you can't find evidence that landed yet, say so rather than assuming it did.

## 3. Confirm settings.json is gone everywhere

A parallel codebase session is removing .claude/settings.json from 5 manifest entries and confirming its absence from the other 5. Check whether any of the 10 mirror folders here still physically holds a settings.json copy from before that fix -- remove it if so, this is the one exception to "never edit inside a Jarvis mirror."

## 4. Record the corrected model as the real, dated source of truth

The model at the top of this prompt is the actual, confirmed architecture -- write it into Log.md as a dated entry, explicitly correcting anything a prior session may have recorded about skills/ being source-repo staging or the sync leg being merely "designed" rather than live. Cross-reference from Tool Map.md and 20_Progress/AI/Claude Code/MOC.md.

Report the real state of all 10 mirrors, what you built for the two home directories, and confirm item 3's cleanup.
```
