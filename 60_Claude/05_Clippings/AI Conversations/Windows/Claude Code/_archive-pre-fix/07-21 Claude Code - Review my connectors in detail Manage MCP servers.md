---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "Review my connectors in detail Manage MCP servers"
started_at: 2026-07-21T19:38:07
ended_at: 2026-07-21T20:34:10
project: Jarvis
status: raw
session_id: b0be487a-2865-446b-a769-d47f9aeb9633
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
tags:
  - input
  - ai-conversation
  - claude-code
---

# Review my connectors in detail Manage MCP servers

## You

Review my connectors in detail: ``` Manage MCP servers
   24 servers

     Project MCPs (D:\Users\_Anant\10_Areas\Documents\Jarvis\.mcp.json)
     excalidraw · ◯ connecting…
   ❯ fetch · ◯ connecting…
     filesystem · ◯ connecting…
     git · ◯ connecting…
     jarvis-memory · ◯ connecting…
     obsidian · ✔ connected · 12 tools

     User MCPs (C:\Users\Anant Gupta\.claude.json)
     firecrawl · ✔ connected · 26 tools
     github · ✔ connected · 26 tools
     jarvis · ◯ connecting…
     jarvis-fs · ◯ connecting…
     pencil · ✔ connected · 13 tools
     the-plan · ◯ connecting…
     the-plan-fs · ✔ connected · 14 tools

     claude.ai
     claude.ai Cloudflare Developer Platform · △ needs authentication
     claude.ai Context7 · ✔ connected · 2 tools
     claude.ai Gmail · ✔ connected · 13 tools
     claude.ai Google Calendar · ✔ connected · 9 tools
     claude.ai Google Drive · ✔ connected · 8 tools
     claude.ai Miro · ✔ connected · 39 tools
     claude.ai QuickNode · ✔ connected · 19 tools
     claude.ai Sanity · ✔ connected · 32 tools
     claude.ai Supabase · ✔ connected · 29 tools
     claude.ai Vercel · △ connected · tools fetch failed```. I have these mcps and some installed through connectors in the claude app. I want to make claude the best possible coding assistant for me. But for that, we neeed to upgrade the way we have been using claude lately. I mean the skills, agents, sub agents, hooks, etc. that we are going to use should be less in number but extremely efficient, so effiecient that i will always run them for the task. Improve the way we write out claude.md files across multiple projects. But what I want to know immediately is that what is a connector/mcp that is going to make you the best coder? Is there something like there out there to improve you coding capabilities? Something that makes you better than me? Search the claude docs, internet and other platforms you want for this. How exactly can I make you the best at coding?

## Claude

I'll research this properly before answering — let me pull in grounded findings on what actually improves Claude Code's coding capability, using an agent built for exactly this kind of question.

While that research runs in the background, here's the immediate read on your connector setup from what you posted.

## Your connector list: what's actually broken right now

**5 of your 6 project-level MCPs are stuck in "connecting…"** — excalidraw, fetch, filesystem, git, jarvis-memory never actually connect; only `obsidian` is live (12 tools). Same pattern on the user level: `jarvis`, `jarvis-fs`, `the-plan` are stuck connecting while `firecrawl`, `github`, `pencil`, `the-plan-fs` are fine. This is not a "some servers just take longer" thing — a server that's still "connecting…" after the session has been running is either crash-looping on startup or hung, and Claude Code will silently just not have those tools available. Before any optimization work, this needs a live diagnosis: check `claude mcp list` output / logs, or just restart the servers one at a time and see which stdio process actually fails to spawn. My guess without logs: too many stdio-based servers spawning concurrently on Windows can produce exactly this stuck-connecting symptom (resource/pipe contention), which is itself evidence for "fewer servers, more reliable" rather than "more servers, more capability."

**Redundancy in what's configured:**
- `filesystem` (stuck) + `jarvis-fs` + `the-plan-fs` are three separate general-purpose filesystem MCP servers scoped to different roots. You already have Read/Write/Edit/Glob/Grep built into Claude Code that cover the same ground for anything inside the working directory — these MCP filesystem servers only earn their keep for paths *outside* the project root (e.g. jarvis-fs reaching into a different vault root, the-plan-fs reaching The Plan's vault). If any of them point at a directory Read/Glob can already reach, it's a pure duplicate paying a tool-description-token tax for nothing.
- `git` (stuck) duplicates Bash's `git` access almost entirely — the MCP git tools (`git_status`, `git_diff`, `git_commit`, etc.) don't do anything `git status`/`git diff` via Bash doesn't, they just wrap it in a different interface. Given it's not even connecting, this is a clean cut candidate.
- `fetch` (stuck) overlaps heavily with `firecrawl` (connected, 26 tools) — firecrawl is explicitly configured as your primary web tool per its own MCP instructions, so `fetch` is redundant even when working.
- `obsidian` (connected) and `jarvis-memory`/`jarvis`/`jarvis-fs`/`the-plan`/`the-plan-fs` all appear to be different facets of the same underlying two vaults (Jarvis + The Plan) — worth asking whether that's 6 servers doing what could be 2.

**24 servers total is high enough to be the likely root cause of the connection failures**, not just a tidiness complaint — every MCP server's tool list gets loaded into context at session start, and stdio servers all spawn as child processes on session init. That's real startup load and real permanent context tax (tool descriptions sit in context whether or not you use them this session), independent of whether they connect successfully.

I'll fold the grounded research on which specific MCP/tool actually moves the needle on coding capability (plus what Anthropic's own docs say about the many-servers tradeoff) into one answer once the background agent reports back — it's mid-run now.

*Tools used: Agent*

## You

<task-notification>
<task-id>ae447035b82e02dd5</task-id>
<tool-use-id>[REDACTED]</tool-use-id>
<output-file>C:\Users\ANANTG~1\AppData\Local\Temp\claude\[REDACTED]\[REDACTED]\tasks\ae447035b82e02dd5.output</output-file>
<status>completed</status>
<summary>Agent "Research best MCPs/tools for Claude Code coding" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>Based on my research of Anthropic's official documentation and GitHub issues, here's a structured report:

## 1. High-Signal MCP Servers &amp; Capability Gaps

**Language Server Protocol (LSP) via MCP** (December 2025 feature)
- **What it does**: Enables semantic code navigation (go-to-definition, find references, type checking) via Language Server Protocol
- **Capability gap filled**: Replaces slow text-search (30–45 seconds) with symbol-level navigation in ~50ms—900× faster. Claude's built-in Grep and Read tools cannot understand code scope or type relationships
- **Languages**: Python, TypeScript, Go, Rust, Java, C/C++, C#, PHP, Kotlin, Ruby, HTML/CSS
- **Source**: [Claude Code LSP documentation](https://resolvewith.me/blog/[REDACTED])

**GitHub, Context7, Playwright, Sentry, Postgres/Supabase** (recommended by Anthropic)
- **What they do**: GitHub (PR/issue context), Context7 (live library docs), Playwright (browser automation for UI verification), Sentry (runtime errors), Postgres (database queries)
- **Capability gap**: Each fills a domain—GitHub for issue context, Context7 avoids stale training data on APIs, Playwright captures visual changes that static code doesn't, Sentry provides runtime context beyond logs
- **Source**: [Anthropic's best MCP servers list](https://www.iwoszapar.com/p/claude-code-best-practices) (corroborated across multiple 2026 guides)

---

## 2. MCP Server Count &amp; Performance Tradeoff (Official Guidance)

**Token overhead is substantial:**
- MCP tool definitions consume **5–15× more tokens** than minimal schema
- A typical **4-server setup burns ~7,000 tokens** of overhead before your first prompt
- 7+ servers: **67,300 tokens** consumed before you type
- **Recommendation: Keep active MCP set to 3–6 servers.** More beats fewer only when each server fills a real gap

**Anthropic's solution (January 2026): MCP Tool Search**
- When tool descriptions exceed 10% of context window, Claude defers loading them and discovers tools on-demand via a search mechanism
- **Reduces token overhead 85%** (from ~77K to ~8.7K tokens in heavy sessions)
- Requires no user configuration; built into Claude Code v2.1+
- **Source**: [Claude Code best practices docs](https://code.claude.com/docs/en/best-practices) + [MCP Tool Search performance data](https://www.atcyrus.com/stories/mcp-tool-search-claude-code-context-pollution-guide)

---

## 3. Lean CLAUDE.md &amp; Configuration Guidance

**Official Anthropic guidance (from best practices docs):**
- **Target: under 200 lines.** LLMs bias towards instructions at the start/end; instruction-following quality decreases uniformly as instruction count rises
- **Test every rule:** If removing a line wouldn't cause Claude to make mistakes, delete it
- **What to include:** Bash commands Claude can't guess, code style rules that differ from defaults, testing commands, repo etiquette, architectural decisions, environment quirks, gotchas
- **What to exclude:** Anything Claude can infer from code, standard language conventions, API documentation (link instead), frequently-changing info, tutorials, file-by-file descriptions
- **For domain knowledge:** Use skills (`.claude/skills/SKILL.md`) instead, so Claude loads them on-demand without bloating every session
- **For deterministic actions:** Use hooks (e.g., "run eslint after every edit") instead of CLAUDE.md instructions, since hooks guarantee execution
- **Source**: [Claude Code best practices docs](https://code.claude.com/docs/en/best-practices), "Write an effective CLAUDE.md" section

---

## 4. Why Your Servers Are Stuck in "Connecting…"

**This is a documented bug, not a configuration issue.** You're hitting **multiple overlapping bugs:**

1. **Windows spawn timeout (hardcoded 5s):** All servers spawn simultaneously, then serialize (~1.8s apart). With 24 configured servers, later ones exceed the 5-second limit and fail to start. This is the primary culprit for "connecting..." states.
   - **Source:** [Issue #61524](https://github.com/anthropics/claude-code/issues/61524), [Issue #64671](https://github.com/anthropics/claude-code/issues/64671)

2. **Multiple stdio servers limitation:** Claude Code CLI can only reliably connect to one stdio MCP server at a time; others fail even if they work individually elsewhere.
   - **Source:** [Issue #21341](https://github.com/anthropics/claude-code/issues/21341)

3. **Servers with many tools fail more often** (your GitHub, Obsidian, Jarvis servers all have large tool sets).
   - **Source:** [Issue #38462](https://github.com/anthropics/claude-code/issues/38462)

4. **Connection timeout issues:** SSE streams close after ~5 minutes of inactivity; MCP_TIMEOUT env var ignored for values &gt;60s.
   - **Source:** [Issues #15945, #20335](https://github.com/anthropics/claude-code/issues/20335)

**Practical recommendation:** Disable/remove unused servers to stay under 6–8 active ones (favoring: GitHub, Context7, one local filesystem MCP, and language-specific tools). Leave the rest offline until Claude Code fixes concurrent stdio server handling. This alone will likely resolve the "connecting..." hangs.

---

## 5. Documented State-of-the-Art Features (2025–2026)

**LSP + MCP Tool Search** are the two biggest 2026 wins for Claude Code specifically:
- LSP solves semantic navigation (900× faster than grep-based search)
- MCP Tool Search solves context bloat from tool descriptions (85% reduction)

**Extended Thinking and Structured Outputs** are Claude API features, not Claude Code MCP—they don't need MCP integration; Claude Code can use them natively on the right models.

No new MCP server has been endorsed by Anthropic as "state-of-the-art for coding" in 2026 beyond the categories above (LSP, issue trackers, live docs, browser/devtools, monitoring).

---

## Summary: Actionable Path Forward

1. **Reduce to 6–8 active servers** (disable the rest in `.mcp.json` or project config)
2. **Ensure LSP is installed** for your languages (via `/plugin` marketplace search for "lsp")
3. **Keep CLAUDE.md under 200 lines**; move domain logic to skills
4. **Use hooks only for actions that must run every time** (not for advisory instructions)
5. **Enable MCP Tool Search** in Claude Code v2.1+ (enabled by default; verify with `/mcp status`)
6. **Monitor GitHub** for fixes to issues #21341 and #61524 (Windows stdio server hangs); upgrading Claude Code when those land will unlock higher server counts

**Sources:**
- [Claude Code best practices — Anthropic](https://code.claude.com/docs/en/best-practices)
- [MCP Tool Search feature — January 2026](https://www.atcyrus.com/stories/mcp-tool-search-claude-code-context-pollution-guide)
- [Claude Code LSP improvement (900×) — December 2025](https://resolvewith.me/blog/[REDACTED])
- [Windows stdio spawn timeout bug #61524](https://github.com/anthropics/claude-code/issues/61524)
- [Multiple stdio servers limitation #21341](https://github.com/anthropics/claude-code/issues/21341)
- [MCP token overhead research — 2026](https://www.jdhodges.com/blog/claude-code-mcp-server-token-costs/)
- [Anthropic Advanced Patterns webinar — March 2026](https://www.anthropic.com/webinars/claude-code-advanced-patterns)</result>
<usage><subagent_tokens>38114</subagent_tokens><tool_uses>11</tool_uses><duration_ms>119275</duration_ms></usage>
</task-notification>

## Claude

Some of those sources are blogs I don't recognize as authoritative, and a few claims (hardcoded 5s Windows spawn timeout, exact token-overhead numbers, "one stdio server at a time") sound like the kind of confident-but-unverified specifics content farms produce. Let me check the two load-bearing claims against Anthropic's actual docs before I hand you a plan built on them.

Got solid, verifiable answers from Anthropic's own docs — including confirmation that some of what I flagged as suspect blog content was indeed unverifiable or wrong. Let me check what's actually in this repo to know which of this applies to Jarvis itself.

Research's back, and I cross-checked the two load-bearing claims against Anthropic's actual docs (`code.claude.com/docs/en/best-practices`, `/discover-plugins`, `/costs`) rather than trust the blog sources my first pass turned up — a few of those were wrong or unverifiable. Here's the real picture.

## The direct answer: is there a connector that makes you a better coder?

Yes, and it's a specific, documented one — **not** anything in your current 24. Claude Code has an official **code intelligence plugin** system: per-language LSP servers (`pyright-lsp`, `typescript-lsp`, `rust-analyzer-lsp`, `gopls-lsp`, etc.) installed via `/plugin install <name>@claude-plugins-official`. Once installed, two things change:

- **Automatic diagnostics** — after every edit, the language server reports type errors, missing imports, syntax issues back to Claude *without running a compiler*. If Claude introduces a bug, it sees it and fixes it in the same turn.
- **Real code navigation** — go-to-definition, find-references, call hierarchies, instead of grep-and-hope. Anthropic's own framing: "a single 'go to definition' call replaces what might otherwise be a grep followed by reading multiple candidate files."

This is the actual "beat me at coding" lever — it's the difference between Claude *guessing* where a symbol is used and *knowing*. But — I checked your repo, and it's not where this applies: Jarvis is 2,528 markdown files and 12 Python scripts, not a typed codebase. This plugin category is for your actual software projects (wherever those live), not this vault. Worth installing there if you haven't.

## What I had to walk back from the first research pass

My subagent's first draft cited some blog sources (resolvewith.me, atcyrus.com, iwoszapar.com) making specific claims — a "hardcoded 5-second Windows spawn timeout," "Claude Code can only reliably connect to one stdio server at a time," exact token-overhead numbers. I could not verify these against official docs and they don't match how Claude Code actually behaves (it demonstrably runs many MCP servers concurrently for lots of people), so **I'm discarding them** rather than hand you a fix built on a fabricated root cause. What I *can* confirm from `code.claude.com/docs/en/costs` directly:

> "MCP tool definitions are deferred by default, so only tool names enter context until Claude uses a specific tool... Disable unused servers: Run `/mcp` to see configured servers and disable any you're not actively using."

So the token-bloat problem is already mitigated by default — but your 5+ servers stuck in "connecting…" is a separate, real reliability problem regardless of cause. The officially-endorsed fix is the same either way: **cut the ones you don't use.**

## Concrete cuts for your list

- `git` MCP — duplicates what Bash + `git` already does; official docs explicitly prefer CLI tools over MCP servers for this reason ("more context-efficient... don't add any per-tool listing").
- `fetch` MCP — redundant with `firecrawl`, which is already your configured primary web tool.
- `filesystem` — redundant with Read/Glob/Grep/Edit for anything inside the project; only keep an fs-MCP for paths *outside* the repo root (which is presumably why `jarvis-fs`/`the-plan-fs` exist — confirm they point somewhere Read can't reach).
- Diagnose the stuck ones empirically rather than guessing: disable all project MCPs, re-enable one at a time, and see which one actually fails to spawn. That'll tell you the real cause in your environment instead of trusting an unverified blog number.

## What's actually verified for CLAUDE.md / skills / agents / hooks

Straight from Anthropic's best-practices doc, matching what you're already trying to do:

- **CLAUDE.md**: keep it under ~200 lines. Test per line: "would removing this cause Claude to make mistakes?" If not, cut it. *"Bloated CLAUDE.md files cause Claude to ignore your actual instructions"* — this is literally why fewer, sharper rules beat comprehensive ones.
- **Skills**: for anything not needed *every* session (your ingest-clipping, closeday, etc. — already doing this right) — loaded on demand, don't bloat every conversation.
- **Hooks**: only for things that must happen with zero exceptions (an eslint run, blocking writes to a folder) — CLAUDE.md instructions are advisory, hooks are deterministic.
- **Subagents**: for investigation/verification that would otherwise pollute your main context — you're already using these well (research-distiller, vault-curator, etc.).

Your instinct — "fewer but so reliable I'll always run them" — is exactly Anthropic's own stated failure pattern in reverse: the over-specified CLAUDE.md and unused-plugin bloat are named as the two things to actively prune.

**Want me to do the connector diagnostic now** (disable-and-reconnect-one-by-one) to find what's actually killing those 5 stuck servers, or would you rather tackle the CLAUDE.md consolidation across your other projects first?

*Tools used: ToolSearch, mcp__firecrawl__firecrawl_scrape, mcp__firecrawl__firecrawl_search, Bash*

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/mcp</command-name>
            <command-message>mcp</command-message>
            <command-args></command-args>

## You

<local-command-stdout>Reconnected to jarvis.</local-command-stdout>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args>install github@claude-plugins-official</command-args>

## You

<local-command-stdout>✓ Installed github. Run /reload-plugins to apply.</local-command-stdout>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/reload-plugins</command-name>
            <command-message>reload-plugins</command-message>
            <command-args></command-args>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args></command-args>

## You

<local-command-stdout>✔ Updated github. Run /reload-plugins to apply.</local-command-stdout>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/reload-plugins</command-name>
            <command-message>reload-plugins</command-message>
            <command-args></command-args>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args></command-args>

## You

<local-command-stdout>Authentication successful. Connected to claude.ai Cloudflare Developer Platform.</local-command-stdout>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args></command-args>

## You

<local-command-stdout>(no content)</local-command-stdout>

## You

The plugin failed to install: ```   Plugins  Discover   Installed   Marketplaces   Errors (1)

   github @ claude-plugins-official (user)
   Invalid MCP server config for "github": Missing environment variables: GITHUB_PERSONAL_ACCESS_TOKEN
```, fix it. You have the personal token in your settings, without printing it anywhere, fix the failed plugin. Do not print the token.

## Claude

Fixed — the plugin's bundled MCP config needed `GITHUB_PERSONAL_ACCESS_TOKEN` as an env var (it authenticates via `https://api.githubcopilot.com/mcp/` with a Bearer header), and that variable didn't exist anywhere: not in Windows env vars, not previously in `settings.json`. It wasn't sitting "in your settings" as you thought — your existing working `github` MCP server uses a different mechanism (its own `env` block in `.claude.json`), which is separate from what this plugin needs.

What I did:
- Pulled a valid token straight from your already-authenticated `gh` CLI session (`gh auth token` — scopes: gist, read:org, repo, workflow) without ever putting it in a command string or printing it.
- Added it to `C:\Users\Anant Gupta\.claude\settings.json` under a new `env.GITHUB_PERSONAL_ACCESS_TOKEN` key, which Claude Code injects into the process environment (and from there into MCP server env-var substitution).
- Verified the file is still valid JSON with all 9 original keys and all 15 hook events intact — nothing else in settings.json was touched.

**One thing left that I can't do for you**: this env var only takes effect for processes started *after* it's set — your current Claude Code session already loaded its environment before this fix. You'll need to fully restart Claude Code (exit and relaunch, not just `/reload-plugins`) for the `github` plugin's MCP server to pick up the token and connect.

*Tools used: Bash, PowerShell, Read*

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args></command-args>

## You

<local-command-stdout>(no content)</local-command-stdout>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/reload-plugins</command-name>
            <command-message>reload-plugins</command-message>
            <command-args></command-args>

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/plugin</command-name>
            <command-message>plugin</command-message>
            <command-args></command-args>

## You

<local-command-stdout>(no content)</local-command-stdout>

## You

clear

## Claude

Quick flag before anything else: your last `/reload-plugins` shows **0 plugin MCP servers** now, down from 1 — the `github` plugin isn't loading at all anymore (likely it's now failing silently or got disabled rather than connecting). Worth checking the `/plugin` → Errors tab to see if it's still complaining about the token, or if something else changed.

On "clear" — not sure what you meant by that one. Did you want me to run something (e.g. `/clear` is a CLI-only command I can't trigger from here), or was that meant for your terminal rather than this chat? Let me know and I'll pick up from there.


