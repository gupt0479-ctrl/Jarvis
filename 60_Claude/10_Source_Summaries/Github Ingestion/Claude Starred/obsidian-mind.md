---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - agents
  - automation
source_url: https://github.com/breferrari/obsidian-mind
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Obsidian Mind

**What it is:** A pre-structured Obsidian vault template that gives Claude Code (and Codex CLI / Gemini CLI) persistent memory across sessions via five lifecycle hooks, 18 slash commands, 9 specialized subagents, and optional QMD semantic search integration.

**What it actually does:** The vault structure is purpose-built for the agent: `brain/North Star.md` is read every session; `work/`, `org/people/`, `perf/`, and `reference/` folders have fixed schemas with YAML frontmatter so agents can navigate by convention rather than discovery. Five hooks automate the lifecycle — `SessionStart` injects North Star + active projects + git summary + vault file listing; `UserPromptSubmit` classifies every message (decision, incident, win, 1:1, project update) and injects routing hints; `PostToolUse` validates frontmatter after every `.md` write; `PreCompact` backs up session transcripts. The QMD MCP integration adds semantic search over the vault — agents call `mcp__qmd__query` to find relevant notes by meaning rather than filename.

**Why it matters for this vault/workflow:** Obsidian Mind is doing what Jarvis is doing, but from a different starting point. Jarvis evolved organically; Obsidian Mind was designed top-down for agent interaction. The specific gaps this addresses: (1) the `SessionStart` hook pattern for injecting context is directly applicable to Jarvis's `CLAUDE.md` — Obsidian Mind's hook architecture is more complete than what Jarvis likely has now; (2) the subagent design (`brag-spotter`, `context-loader`, `review-fact-checker`) for running heavy operations in isolated context windows is a pattern worth adopting; (3) the QMD MCP integration would make Jarvis queries semantic rather than filename-based.

**How to use it:**
```bash
npm install -g shardmind
mkdir ~/obsidian-mind && cd ~/obsidian-mind
shardmind install github:breferrari/obsidian-mind
# Open as Obsidian vault, enable Obsidian CLI, then:
claude   # or codex, or gemini
```
Alternatively: `git clone` and manually fill in `brain/North Star.md`.

**Failure modes / limitations:** The vault structure assumes you're starting fresh — migrating an existing Obsidian vault like Jarvis requires running `/om-vault-upgrade`, which classifies and transforms every existing note. This could take significant time and may mis-classify notes that don't fit the expected schema. The `SessionStart` hook injects ~2K tokens per session — on long projects with many sessions, this adds up. QMD requires a ~328MB embedding model download on first use, plus ~1.28GB for the LLM reranker (though these are optional). The shardmind package manager is from the same author — more coupling than a plain git clone.

**Verdict:** Don't replace Jarvis with Obsidian Mind — instead, extract the hook architecture (specifically `SessionStart` and `UserPromptSubmit` patterns) and the subagent design patterns for use in Jarvis. The `/om-vault-upgrade` command is worth running on Jarvis to see what it produces, in a dry-run first.
