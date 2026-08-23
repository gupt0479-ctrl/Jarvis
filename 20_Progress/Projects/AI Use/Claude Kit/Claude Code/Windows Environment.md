---
type: reference
status: active
created: 2026-08-22
updated: 2026-08-22
tags:
  - claude-kit
  - windows
  - environment-map
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Prompts]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]]"
next: null
---
# Windows Environment — Reference Map
Short by design — the Windows side is genuinely thin today ("windows is barely built," per Anant, 2026-08-22). This exists so a Windows-side instruction pass starts from an accurate, confirmed-empty baseline instead of guessing or assuming parity with WSL. Fuller picture, and the pattern to apply here once real content exists: [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]].

## Identity
- Home: `C:\Users\Anant Gupta` (= `/mnt/c/Users/Anant Gupta` from WSL).
- `D:` holds both vaults: `D:\Users\_Anant\10_Areas\Documents\Jarvis` and `...\The Plan` — same content [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment|WSL]] reaches via `/mnt/d/...`.

## Current state — confirmed thin, not just assumed
Per `second-brain-claudekit`'s own `.claude_windows` sync-manifest entry (re-verified 2026-08-20, `_docs/Repo-Map.md`):
- No `agents/` at all.
- No `hooks/` at all.
- `commands/` exists but is empty.
- No `CLAUDE.md`.
- No `settings.json` of note either — meaning there is nothing to audit for [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment#`~/.claude/settings.json` — real hooks, real plugins, and one confirmed global/project-scope leak|the kind of global/project-scope leak found in WSL's `settings.json`]] — a real difference worth confirming still holds before writing anything, not assuming.
- `skills/` has exactly one real folder (`export-ai-session/`) plus ~30 `firecrawl-*` symlinks pointing outside `.claude/` to a machine-specific path (already excluded from sync — leave alone).

This has not been re-verified today (2026-08-22) with a direct `ls`/`cat` from this session — WSL's equivalent claims above were; Windows's weren't re-checked this pass since this session has no direct filesystem access to `C:\` beyond the `/mnt/c/` mount, which wasn't walked this round. Treat the bullet list above as last-verified 2026-08-20 and confirm it's still true before building on it.

## What this means for writing Windows-side instructions
- There is close to nothing to preserve or migrate — a Windows global `CLAUDE.md` is close to a blank slate, not a merge job.
- Don't assume parity with [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment|WSL Environment]] — nearly all real tool config and every real project live WSL-side today.
- Keep whatever gets written here minimal and Windows-true, informed by what WSL already got right (the agents/commands that pass the global-scope test) rather than a wholesale copy of it (WSL's `autoMode` leak should not be copied over).
