---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
source_url: 60_Claude/05_Clippings/PDFs/Best MCP's 👾.pdf
source_note: "[[Best MCP's 👾.pdf]]"
input_kind: pdf
track: ai
---
# 5 Best Claude Code MCPs You Need to Install — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Best MCP's 👾.pdf`
**Ingested:** 2026-07-04
**Pages:** 3
## Source
A short listicle of five Claude Code MCP servers/plugins with install commands and a one-paste master prompt that installs all five in order.
## Key Claims
- ==These five "turn Claude Code from a chatbot into a weapon"== — browser control, live docs, planning, a second model, and persistent memory
- **Context7** stops the model hallucinating outdated APIs by pulling live version-specific docs (already installed in this vault's `.mcp.json` deferred tools)
- **Sequential Thinking** (Anthropic) is "plan mode times ten" — plans step by step, branches when wrong, revises before touching code
- **Knowledge Graph Memory** (Anthropic) gives persistent cross-session memory storing entities, relationships, observations in a local JSON file
## Full Content
| MCP | What it does | Install | When to use |
| --- | --- | --- | --- |
| **Playwright** | Claude controls a real browser (clicks, forms, scrapes) | `claude mcp add playwright -- npx @playwright/mcp@latest` | scrape a site with no API, test your own UI, automate repeatable web tasks |
| **Context7** | Pulls live documentation into chat | `claude mcp add --scope user context7 -- npx -y @upstash/context7-mcp` | library updated recently, model writes outdated syntax, want version-specific docs |
| **Sequential Thinking** | Step-by-step planning with branching/revision | `claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking` | multi-step problem, unclear scope, want it to think before coding |
| **Codex Plugin** | Runs OpenAI Codex inside Claude Code as an adversarial second opinion | `/plugin marketplace add openai/codex-plugin-cc` → `/plugin install codex@codex-plugin-cc` | second opinion before shipping; `/codex:review`, `/codex:adversarial-review`, `/codex:rescue` |
| **Knowledge Graph Memory** | Persistent cross-session memory (entities/relationships/observations) | `claude mcp add --scope project memory -e MEMORY_FILE_PATH=./.claude/memory.json -- npx -y @modelcontextprotocol/server-memory` | stop re-explaining your business; reference weeks-old decisions; sync across machines |
The master prompt pastes all five with "confirm each ran before the next, stop and report exact error on failure," then runs `/mcp` to verify all show connected.
## Why It Matters
Direct input for the [[Claude OS]] MCP roster. Context7 is already wired in this vault (it appears in the deferred-tool list); the genuinely additive ones for Jarvis are **Sequential Thinking** (the North Star's "plan before build" discipline as a tool) and **Codex Plugin** (an adversarial second-opinion loop, matching the Cursor/Kiro/Codex cross-tool pattern in [[10_Areas/AI/Codex|Codex]]). The **Knowledge Graph Memory** MCP overlaps with — and is weaker than — the custom `jarvis-memory` server, so it's a *don't-adopt* (jarvis-memory already does entities/links/observations over the whole vault). Caveat: this is anti-drift-listed territory (MCP setup is a time-boxed weekly slot, not daily ops per [[08 - Anti-Drift Rules]]).
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Best MCP's 👾.pdf`
- [[Claude OS]] — the MCP roster this feeds
- [[10_Areas/AI/Codex|Codex]] — the Codex-plugin adversarial-review pattern
## Open Questions
- [ ] Adopt Sequential Thinking + Codex Plugin in a weekly tool-slot, or is the built-in plan mode + existing Codex setup enough?
- [ ] Confirm the exact Codex-plugin slash-command syntax (the PDF flags it as unverified) against the repo README.
## Flashcards
#cards/ai
Why is the Knowledge Graph Memory MCP a "don't adopt" for Jarvis specifically?::Because the custom **jarvis-memory** server already stores entities/relationships/observations over the whole vault — the generic memory MCP is a weaker, project-scoped subset of what Jarvis already runs.
Which of the five MCPs solves outdated-API hallucination, and how?::**Context7** — it pulls **live, version-specific documentation** into the chat so the model writes current syntax instead of guessing from stale training data.
