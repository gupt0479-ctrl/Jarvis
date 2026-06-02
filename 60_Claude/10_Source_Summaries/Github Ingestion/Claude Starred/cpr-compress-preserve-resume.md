---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/EliaAlberti/cpr-compress-preserve-resume
notes:
  - "[[40_Resources/CS/Repos]]"
---
# CPR — Compress, Preserve, Resume

**What it is:** Three Claude Code slash commands (`/preserve`, `/compress`, `/resume`) that manage session memory by writing structured logs to `CC-Session-Logs/` and keeping `CLAUDE.md` current — claiming ~55% reduction in session-restart token cost.

**What it actually does:** The three skills work as a session lifecycle: `/preserve` updates `CLAUDE.md` with key learnings (architectural decisions, patterns) and auto-archives it when it exceeds 280 lines; `/compress` saves the full session to a structured markdown log (`GRAPH_REPORT` style: Quick Reference, Decisions, Learnings, Solutions, Files Modified, Pending Tasks, plus a raw archive that `/resume` never reads to save tokens); `/resume` loads `CLAUDE.md` + last N session summaries + supports keyword search across all past sessions. Critical dependency: disable auto-compact (`claude config set --global autoCompact false`) so you control when compression happens.

**Why it matters for this vault/workflow:** CPR solves a problem Jarvis doesn't — per-project session continuity within the Claude Code CLI. Jarvis is the long-term knowledge graph; CPR is the short-term working memory for active coding sessions. They're complementary: `/compress` + `/resume` handle the "what was I doing yesterday on this feature" question, while Jarvis handles "what decision did I make about this architecture six months ago." The `/preserve` → `CLAUDE.md` update cycle mirrors Jarvis's `CLAUDE.md` updating workflow. The estimated 83,250 tokens saved per 10-session project is meaningful at scale.

**How to use it:**
```bash
git clone https://github.com/eliaalberti/cpr-compress-preserve-resume.git
cp commands/*.md ~/.claude/commands/   # global install
# Or per-project: cp to .claude/commands/ in project root
# Then disable auto-compact:
claude config set --global autoCompact false
# Session workflow:
# Start: /resume
# Midway: /preserve (if major decision made)
# End: /compress → /compact (always in this order)
```

**Failure modes / limitations:** Requires disabling auto-compact globally — this means you must remember to run `/compress` before context fills, or lose the session. The 55% token reduction is an analytical estimate on modelled scenarios, not measured telemetry. The log storage path detection (nearest parent with `CLAUDE.md` or `.git`) can pick the wrong root in monorepos. Logs can grow large (hundreds of KB each with full raw session); the `/resume` summary-only loading keeps tokens low but the disk footprint accumulates.

**Verdict:** Install globally and wire into every Claude Code project — the `/compress` + `/resume` cycle eliminates the single most frustrating part of multi-session coding work (re-explaining what you were doing).
