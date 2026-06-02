---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - git
  - safety
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Git Recovery and Vault Safety

Obsidian Git and File Recovery protect the vault, but they are not permission to make broad edits.

## Current Obsidian Git Settings

Observed safe facts:

- Installed and lazy-loaded with short delay.
- Auto backup after file change: enabled.
- Auto-push interval: `5`.
- Auto-pull interval: `10`.
- Auto-pull on boot: enabled.
- Pull before push: enabled.
- Push disabled: false.
- Commit message pattern: `vault backup: {{date}}`.
- Diff style: split.
- Changed files shown in status bar.

Implication: the vault may sync or push through Obsidian while an agent is also editing files. Agents should check status before broad work and never assume the working tree is clean.

## Dirty Worktree Rules

Before broad edits, commits, pushes, moves, or deletes:

1. Check `git status`.
2. Identify which files belong to the current task.
3. Preserve unrelated user changes.
4. Do not stage unrelated files.
5. Do not run destructive Git commands unless explicitly asked.

Never run broad reset, checkout, clean, or history-rewrite operations without explicit approval.

## File Recovery

File Recovery is enabled and is useful when Obsidian has a better local snapshot than Git.

Use it for:

- a note accidentally damaged in the editor
- recovering a recent uncommitted version
- inspecting a narrow previous state

Do not rely on File Recovery as a normal editing strategy. It does not justify risky bulk edits.

## `.gitignore` Role

Current ignore rules protect:

- `.obsidian/workspace.json`
- `.obsidian/workspace-mobile.json`
- `.obsidian/cache`
- `.trash/`
- Copilot plugin `data.json`
- QuickAdd plugin `data.json`
- Local REST API plugin `data.json`
- Claude local settings
- Kiro settings
- Copilot vector indexes
- OS junk and temporary files

This matters because several plugin data files can contain credentials or regenerated machine state. Do not remove these ignores for convenience.

## Restore Boundaries

If an edit goes wrong:

1. Stop editing.
2. Identify the affected file and whether it was changed by this task.
3. Inspect a narrow diff.
4. Restore only the damaged content.
5. Ask before using Git checkout/reset or touching unrelated files.

The repair target is one file or one section, not the whole vault.

## Pre-Large-Edit Checklist

Before a future broad documentation pass:

- Read [[AI_CONTEXT]], [[00_Dashboard]], and recent session log entries.
- Check `git status`.
- Confirm destination folder and files.
- Confirm raw clippings and archive paths are excluded.
- Confirm no plugin settings will be edited.
- Use patches rather than uncontrolled rewrites when possible.
- Append a concise continuity log entry afterward.

## Agent Safety

Agents should not:

- commit automatically
- push automatically
- change Obsidian Git settings
- stage unrelated files
- rewrite `.gitignore` for convenience
- edit `.obsidian` plugin settings
- delete or move notes without permission
- touch `60_Claude/05_Clippings` unless explicitly asked
- treat `50_Archive` as normal write space

## Integration Map
- **Obsidian Git ↔ agent edits:** auto-backup-on-change plus a `5`-minute auto-push means the working tree can commit or sync *while an agent is mid-edit*. So an agent must check `git status` before broad work and never assume a clean tree. The plugin's convenience for a human is a coordination hazard for an agent.
- **`.gitignore` ↔ plugin secrets:** the ignore list covers `copilot`, `quickadd`, and `local-rest-api` `data.json`, plus Copilot vector indexes and workspace state. This is the safety net behind the "document behavior, never values" rule in [[AI Automation and Local Interfaces]] — do not remove these ignores for convenience.
- **Git ↔ session log:** the session log in `60_Claude/07_AI_Information/Session Logs/log.md` is the human-readable audit trail; Git is the byte-level one. After meaningful edits, the agent appends to the log but does **not** commit unless asked.
## Gold-Standard Example
The correct example is a process, not a note: the repo at the start of this very session had ~100 unrelated dirty files (plugin updates, Excalidraw, archive moves). The right handling is to edit only the task's files, stage nothing unrelated, leave the rest of the dirty tree untouched, and never run a broad `add -A` or `reset`. That restraint *is* the gold standard for Git in a vault that multiple tools edit.
## Verified Open State
- Is a `5`-minute auto-push cadence still safe while Claude, Cursor, Kiro, and Copilot all edit the vault? — *needs user decision; concurrent writers raise conflict risk*
- Should agents ever be allowed to commit, or remain commit-free by default? — *current rule is commit-free; confirm it stays*
## Sources

- [Obsidian Git docs - Features](https://publish.obsidian.md/git-doc/Features)
- [Obsidian Git README](https://github.com/Vinzent03/obsidian-git)
- [Obsidian Help - File Recovery](https://obsidian.md/help/plugins/file-recovery)
- [[AI_CONTEXT]]
- [[40_Resources/Obsidian/Vault Operating System]]
