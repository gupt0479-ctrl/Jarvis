---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
source_url: 60_Claude/05_Clippings/PDFs/claude-code-statusbar-resource.pdf
source_note: "[[claude-code-statusbar-resource.pdf]]"
input_kind: pdf
track: ai
---
# Claude Code Status Bar — Summary
**Source:** `60_Claude/05_Clippings/PDFs/claude-code-statusbar-resource.pdf`
**Ingested:** 2026-07-04
**Pages:** 3
## Source
A resource drop (@byarnieverma) on setting up a persistent Claude Code status line — folder, branch, model, and a context-usage bar always visible at the bottom of the terminal, so you stop typing `/status`, `/usage`, `/model` mid-build.
## Key Claims
- ==The whole setup is one prompt: `/statusline show folder, git branch, model name, and context percentage with a progress bar` — Claude Code generates and installs the script automatically==
- The **context-percentage bar is the point**: it shows when Claude is about to "forget" earlier work, so you can `/compact` or `/clear` before it does
- Claude Code passes live session data to the script via **stdin as JSON** (model, cwd, cost, session ID); the script outputs one formatted line; refresh at most every 300ms, ANSI colors supported
- Manual config lives in `~/.claude/settings.json` under a `statusLine` block pointing at any executable script
## Full Content
**Quick setup:** type `/statusline show folder, git branch, model name, and context percentage with a progress bar`. Output shows working folder, git branch, active model (Opus/Sonnet/Haiku), and a context-window progress bar.
**Manual config** (`~/.claude/settings.json`): `"statusLine": {"type":"command","command":"~/.claude/statusline.sh","padding":0}`. Claude passes JSON via stdin; script reads it, prints one line.
**Community repos:** `sirmalloc/ccstatusline` (zero-config TUI wizard, powerline, cost/usage tracking — easiest), `daniel3303/ClaudeCodeStatusLine` (color-codes green→red as context fills), `tmck-code/yet-another-statusline` (plugin marketplace, themes), `nilbuild/claude-statusline` (minimal, backs up existing config), `Haleclipse/CCometixLine` (Rust, single binary, cross-platform).
**Official docs:** docs.anthropic.com/en/docs/claude-code/statusline.
**Pro tips:** set the bar to change color at 70%+ context so you know when to `/compact`; the status bar retires `/status`, `/usage`, `/model`.
## Why It Matters
Small, high-frequency quality-of-life fix for the primary implementation surface ([[10_Areas/AI/Claude Code|Claude Code]]). The context-percentage bar directly serves the vault's token-economy discipline (North Star Part 6) — a visible "compact before you forget" cue is exactly the kind of always-on signal the token rules want. A one-line `/statusline` setup is inside the anti-drift budget (not a rabbit-hole), unlike adopting one of the community Rust/TUI repos. Worth doing once.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/claude-code-statusbar-resource.pdf`
- [[10_Areas/AI/Claude Code|Claude Code]] — the tool this configures
## Open Questions
- [ ] Set the one-line `/statusline` (folder + branch + model + context bar) with a 70% color warning?
## Flashcards
#cards/ai
What's the fastest way to add a Claude Code status bar?::Type `/statusline show folder, git branch, model name, and context percentage with a progress bar` — Claude Code generates and installs the script automatically.
Why is the context-percentage bar the most useful part?::It shows when the context window is filling up so you can **`/compact` or `/clear` before Claude forgets earlier work** — an always-on cue that serves the token-economy discipline.
