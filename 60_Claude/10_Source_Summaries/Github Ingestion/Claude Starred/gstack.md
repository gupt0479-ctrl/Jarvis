---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
  - agents
source_url: https://github.com/garrytan/gstack
notes:
  - "[[40_Resources/CS/Repos]]"
---
# gstack

**What it is:** Thirteen opinionated Claude Code workflow skills that give you explicit "cognitive modes" — founder review, engineering review, design audit, paranoid code review, release execution, QA with a live browser, and post-ship documentation — each as a slash command.

**What it actually does:** gstack installs into `~/.claude/skills/gstack/` and symlinks each skill into `~/.claude/skills/`. The key innovation is the `/browse` skill: a compiled Playwright-based Chromium binary (~58MB) that gives Claude Code a persistent browser session with cookies, screenshots, console log access, and device emulation. This closes the loop from code to live UI — Claude can click through your actual deployed app, catch visual regressions, and verify login flows without you opening a browser. The other skills are structured prompts with specific cognitive frames: `/plan-ceo-review` asks "what is the 10-star version of this feature"; `/plan-eng-review` forces architecture diagrams and state machines before implementation; `/review` hunts for N+1 queries, race conditions, and trust boundary violations.

**Why it matters for this vault/workflow:** gstack solves the "mushy AI mode" problem — getting sharper, more differentiated responses by explicitly switching cognitive frames. For BOOM/UROP research projects, `/plan-eng-review` + `/review` would significantly improve code quality before shipping. The `/browse` + `/qa` combination replaces manual browser testing for web projects. `/retro` is directly relevant to Jarvis (weekly synthesis with commit-level data already lives in the vault's `thinking/` structure).

**How to use it:**
```
# Paste into Claude Code to install globally
Install gstack: run `git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` then add a "gstack" section to CLAUDE.md that lists the available skills: /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /review, /ship, /browse, /qa, /qa-only, /qa-design-review, /setup-browser-cookies, /retro, /document-release.
```
Requires: Claude Code, Git, Bun v1.0+. First `/browse` call auto-compiles the binary.

**Failure modes / limitations:** The `/browse` binary is macOS/Linux only (x64 and arm64). The Greptile integration in `/review` and `/ship` requires a separate Greptile account and GitHub App install. The `DESIGN.md` inference in `/plan-design-review` is useful but slow — it reads CSS across your entire project. The compiled binary means any Playwright security vulnerabilities in the bundled version require a manual upgrade (`/gstack-upgrade`).

**Verdict:** Install globally immediately, at minimum for `/plan-eng-review` and `/review` — these two skills alone significantly raise the floor on Claude Code output quality.
