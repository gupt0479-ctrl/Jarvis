---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - agents
  - tooling
source_url: https://github.com/gastownhall/beads
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Beads (bd)

**What it is:** A CLI issue tracker (`bd`) backed by Dolt (a git-versioned SQL database) that gives AI agents a dependency-aware task graph with hash-based IDs, atomic claiming, and persistent memory — as an alternative to markdown TODO lists.

**What it actually does:** `bd init` in a project installs a Dolt database at `.beads/` and runs `bd setup claude` to wire Claude Code hooks and write `AGENTS.md` instructions. From there, agents use `bd ready` to find unblocked tasks, `bd update <id> --claim` to atomically take ownership, and `bd close <id>` when done. Tasks have hierarchical IDs (`bd-a3f8`, `bd-a3f8.1`, `bd-a3f8.1.1`) for epic → task → subtask structure. `bd remember "insight"` stores persistent memory that `bd prime` injects at session start. The Dolt backend means the issue database has branching, merging, and remote sync — multi-agent workflows on different branches don't conflict because Dolt resolves at the cell level.

**Why it matters for this vault/workflow:** Jarvis handles personal knowledge and performance tracking. Beads handles project-level task coordination between agents. The key difference from a markdown TODO: `bd update --claim` is atomic — two Claude Code subagents can't both claim the same task simultaneously. The `bd remember` / `bd prime` memory loop is complementary to Jarvis's `brain/` system: Jarvis stores career knowledge, Beads stores project-specific insights that should survive context resets. For BOOM/UROP multi-agent work, the hash-based IDs and dependency graph prevent the "agents stepping on each other" problem.

**How to use it:**
```bash
brew install beads           # or: npm install -g @beads/bd
cd your-project
bd init
bd setup claude              # installs hooks + writes AGENTS.md
bd create "Feature X" -p 1  # P1 task
bd ready                     # what can be worked on now
bd update bd-a1b2 --claim   # atomic claim
bd prime                     # inject memory at session start
```

**Failure modes / limitations:** Dolt adds ~50MB to the project. The embedded mode is single-writer (file locking) — only matters if you're running many parallel Claude Code sessions in the same project simultaneously. The `bd prime` injection on session start adds tokens to every session, which accumulates over a long project. The README notes that `BEADS_DIR` must be set for non-git use cases, which can be easy to forget in CI.

**Verdict:** Replace markdown TODO lists in any multi-session or multi-agent project with `bd` — the atomic claim alone is worth the setup overhead.
