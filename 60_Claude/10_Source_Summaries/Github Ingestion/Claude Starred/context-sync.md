---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - mcp
source_url: https://github.com/Intina47/context-sync
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Context Sync

**What it is:** An MCP server (`npm install -g @context-sync/server`) that gives any AI coding tool a local persistent memory layer via 8 tools: `set_project`, `remember`, `recall`, `read_file`, `search`, `structure`, `git`, and `notion`.

**What it actually does:** Context Sync stores project identity, active work, decisions, constraints, and file context in a local SQLite database at `~/.context-sync/data.db`. On session start, you call `set_project({ path: "/absolute/path/to/project" })` then `recall()` to restore everything the agent knew about this codebase. `remember({ type: "decision", content: "..." })` stores structured facts that survive context resets. The `git` tool provides `hotspots` (frequently changed files), `coupling` (files that change together), and `analysis` — richer than just `git status`. Installing globally auto-configures Claude Desktop, Cursor, VS Code, Continue.dev, Codex CLI, and Claude Code via MCP. Git hooks (`post-commit`, `pre-push`, `post-merge`) auto-capture context.

**Why it matters for this vault/workflow:** Context Sync fills a gap between sessions at the project level — Jarvis handles personal/career memory, Claude Code's `CLAUDE.md` handles static project instructions, and Context Sync handles dynamic session-to-session state: what's currently in progress, decisions made mid-session, file paths currently being worked on. The `git coupling` analysis (files that change together) is genuinely useful for understanding a codebase's hidden dependency structure before making changes. The Notion read-only integration could link external research docs into the agent's context without duplicating them into the vault.

**How to use it:**
```bash
npm install -g @context-sync/server
# Auto-configures MCP on install, then restart your AI tool
# Standard session flow:
# 1. set_project({ path: "/abs/path" })
# 2. recall()
# 3. structure({ depth: 2 })
# 4. remember({ type: "decision", content: "..." })
```

**Failure modes / limitations:** Auto-configuration rewrites AI tool config files on install — verify what it changed before committing to any project. The git hooks are marked with "Context Sync Auto-Hook" and back up existing hooks, but in a repo with existing hooks, this needs careful review. The SQLite database is at a global path (`~/.context-sync/data.db`), not per-project — this could be a problem if multiple projects have conflicting notes about the same filename. The `notion` integration is read-only, so you can't write Notion pages from Claude.

**Verdict:** Install globally and use `remember`/`recall` as a lightweight complement to Jarvis's session log workflow — faster to write than a full `/om-dump`, useful for mid-session decision capture.
