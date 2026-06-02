---
type: evergreen
status: sprout
created: 2026-05-29
tags:
  - evergreen
  - github
  - claude-code
  - action
notes:
  - "[[40_Resources/CS/Repos]]"
  - "[[AI_CONTEXT]]"
---

# Repos Deep Analysis — Action File

Source: [[40_Resources/CS/Repos]] (95 repos, 7 sections)
Today's goal: Claude Code fully configured + VS Code as single SDE CLI (Cursor, Kiro, Copilot as CLIs) + Obsidian↔VS Code bridge.

---

## Action Queue

HIGH priority only. Do these in order.

| # | Repo | Action |
|---|------|--------|
| 1 | **claude-code-templates** | `npx claude-code-templates` — browse+install agents/MCPs/hooks/skills interactively. Run this before installing anything else. |
| 2 | **agency-agents** | `git clone https://github.com/msitarzewski/agency-agents && cp -r agency-agents/.claude/* .claude/` — drops 105K-star agent personas directly into your project's `.claude/`. |
| 3 | **CPR** | Clone repo → copy `/preserve`, `/compress`, `/resume` commands into `.claude/commands/`. Verify exact install in README. |
| 4 | **ECC** | Single install (verify README for `npx` or `claude install` command) — adds skills + instincts + persistent memory + security layer to Claude Code. |
| 5 | **context-sync** | Add to MCP config in `~/.claude.json` as a local SQLite server — gives Claude Code `remember`/`recall` tools with no external deps. Verify exact config in README. |
| 6 | **mattpocock-skills** | `npx skills add mattpocock` (verify) — 18 skills targeting agent failure modes. |
| 7 | **gstack** | `npx skills add gstack` (verify) — 13 cognitive-mode skills + Playwright browser tool for Claude Code. |
| 8 | **agent-skills-addyosmani** | `npx skills add addyosmani` (verify) — 23 SDLC skills with evidence requirements. |
| 9 | **system-prompts-and-models-of-ai-tools** | Read Cursor + Kiro system prompts from this repo before writing CLAUDE.md rules for multi-CLI setup. Prevents behavioral conflicts. |
| 10 | **obsidian-mind** | Clone → overlay on Jarvis vault (merge selectively, don't overwrite existing structure). Sets up 5 lifecycle hooks + 9 subagents for agent-native Obsidian. |
| 11 | **graphify** | `npx skills add graphify` (verify) — Claude Code skill that builds a NetworkX graph from any folder and exports an Obsidian vault. Runs on VS Code projects to push knowledge into Jarvis. |
| 12 | **get-shit-done** | Read and implement the meta-prompting + spec-driven workflow system into CLAUDE.md. It's a methodology, not a CLI install. |

---

## CLAUDE Section (28 repos)

### ECC
**What it does:** Wraps Claude Code with a security layer (blocks prompt injection), persistent memory (survives session restarts), pre-loaded skills, and behavioral instincts — delivered as a single install, no config juggling.
**Today use case:** Install as the base layer before loading other skills packs. Sets the security perimeter first.
**Long-term use case:** Memory layer that grows with your codebase; instincts enforce coding standards across every Claude Code session.
**Priority:** High
**Action:** Find exact install command in README (likely `npx ecc` or `claude install ecc`). Install before skills packs #6-8.

---

### gstack
**What it does:** 13 skills organized as cognitive modes (founder review = strategic critique, eng review = technical critique, paranoid QA = adversarial testing) plus a Playwright browser tool Claude Code can call directly.
**Today use case:** Install skills pack. The "paranoid QA" mode is immediately useful when testing any new Claude Code setup.
**Long-term use case:** Playwright browser tool enables agent-driven UI testing and scraping inside Claude Code sessions.
**Priority:** High
**Action:** `npx skills add gstack` — verify exact command in README.

---

### mattpocock-skills (Skills by mattpocock)
**What it does:** 18 skills that directly counter the four ways agents break down: misalignment (wrong goal), verbosity (padding), broken feedback loops (no correction signal), entropy (context drift). Each skill is a targeted patch.
**Today use case:** Install immediately. These patch the exact failure modes you'll hit today while configuring Claude Code.
**Long-term use case:** Permanent quality floor for all Claude Code work.
**Priority:** High
**Action:** `npx skills add mattpocock` — verify in README.

---

### agent-skills-addyosmani (Agent Skills by Addy Osmani)
**What it does:** 23 skills covering the full SDLC — planning, implementation, testing, review, deployment — each with a rationalizations table explaining *why* the skill works and evidence requirements before the agent acts.
**Today use case:** Install. The evidence requirements mechanic prevents Claude Code from hallucinating completed steps.
**Long-term use case:** Use as the reference architecture when writing custom skills for this vault.
**Priority:** High
**Action:** `npx skills add addyosmani` — verify in README.

---

### obsidian-mind
**What it does:** Obsidian vault template purpose-built for AI agents: 5 lifecycle hooks (on-open, on-close, on-file-create, etc.), 18 slash commands, 9 subagents, and QMD semantic search over notes. The hooks fire when Obsidian events happen, triggering agent actions.
**Today use case:** Core piece of the Obsidian↔VS Code bridge. Merge selectively into Jarvis — don't overwrite existing CLAUDE.md or folder structure.
**Long-term use case:** The lifecycle hooks are the mechanism that makes Jarvis agent-reactive. A file created in VS Code can trigger an Obsidian hook that routes it to the right vault folder.
**Priority:** High
**Action:** Clone, diff against Jarvis structure, selectively copy hooks + subagents into `.claude/`. Do NOT overwrite `CLAUDE.md` or `AI_CONTEXT.md`.

---

### CPR — Compress, Preserve, Resume
**What it does:** Three slash commands that manage Claude Code session lifecycle: `/preserve` snapshots the current context to disk, `/compress` reduces token count by ~55% via structured summarization, `/resume` reloads a preserved session from scratch. Solves context window exhaustion on long tasks.
**Today use case:** Install before starting any long configuration session. The 55% token reduction pays for the install cost in the first session.
**Long-term use case:** Every multi-hour development session. Especially important for agentic tasks that span multiple days.
**Priority:** High
**Action:** Clone repo → copy slash commands to `.claude/commands/` → verify in README if there's an npm install path.

---

### memsearch (Zilliz)
**What it does:** Auto-captures every Claude Code session to a markdown file, then indexes all sessions using ONNX embeddings and Milvus vector DB, exposing a `/memory-recall` command for semantic search across past sessions.
**Today use case:** Not today — Milvus requires Docker and is heavyweight for a first-day setup.
**Long-term use case:** When you want cross-session semantic search ("what did I figure out about X three weeks ago"). Pairs well with context-sync for a two-layer memory system.
**Priority:** Medium
**Action:** After Claude Code is stable, `docker compose up -d` to start Milvus, then follow README install. Save for week 2.

---

### context-sync
**What it does:** Local SQLite MCP server that exposes `remember` and `recall` tools to Claude Code. Also runs git coupling analysis (identifies which files change together) as a background index. No external services.
**Today use case:** Install as MCP server today. SQLite means zero infrastructure. `remember` stores arbitrary facts; `recall` retrieves them semantically. Lighter than memsearch, works immediately.
**Long-term use case:** Grows into a persistent knowledge base about your codebase that survives across sessions.
**Priority:** High
**Action:** Add MCP server config to `~/.claude.json`. Verify exact config block in README.

---

### claude-context (Zilliz)
**What it does:** MCP server that crawls a codebase, chunks it, embeds into Milvus, and exposes semantic code search to Claude Code. Claims 40% token reduction by letting the agent fetch relevant code snippets instead of loading entire files.
**Today use case:** Not today — Milvus dependency again.
**Long-term use case:** For large codebases (>50K LOC) where full-file loading is too expensive. Run on any production repo you're contributing to.
**Priority:** Medium
**Action:** Install after Milvus is running from memsearch setup. One infrastructure, two tools.

---

### graphify
**What it does:** Claude Code skill that takes a folder path, builds a NetworkX knowledge graph (nodes = files/entities, edges = relationships/imports/references), and exports a structured Obsidian vault from that graph. The export lands directly in a vault folder you specify.
**Today use case:** Core PKM↔dev bridge mechanism. Run on a VS Code project to auto-generate Obsidian notes for entities, modules, and their relationships.
**Long-term use case:** Run after every major refactor to keep Jarvis's knowledge layer in sync with actual code structure.
**Priority:** High
**Action:** `npx skills add graphify` (verify) → test on one VS Code project folder today → point output to a `60_Claude/` subfolder.

---

### spec-kit (GitHub)
**What it does:** GitHub's spec-driven dev CLI: you write a constitution (values/constraints) → `specify` generates a spec → `clarify` asks disambiguation questions → `plan` builds a task tree → `tasks` breaks tasks into atomic units → `implement` executes. Forces alignment before any code is written.
**Today use case:** Not today — useful once the Claude Code environment is stable. Don't add process overhead before tooling is in place.
**Long-term use case:** Use for every non-trivial feature. Prevents scope creep and agent hallucination on large implementations.
**Priority:** Medium
**Action:** `npm install -g spec-kit` (verify) → use on next non-trivial feature after today's setup is done.

---

### beads (bd)
**What it does:** CLI issue tracker backed by Dolt (a Git-compatible SQL database) with atomic task claiming (prevents two agents from taking the same task) and dependency graphs for multi-agent coordination.
**Today use case:** Not relevant today — you don't have multi-agent workflows running yet.
**Long-term use case:** When running parallel agents on a project (e.g., ruflo swarm). Dolt means your issue history is version-controlled like code.
**Priority:** Low
**Action:** Revisit when you have >2 agents running concurrently on a project.

---

### claude-code-templates
**What it does:** Interactive npm CLI that browses 100+ Claude Code agents, MCPs, hooks, and skills in a terminal UI. You select what you want, it installs into the right locations. Discovery + install in one command.
**Today use case:** Run this first. It's the catalog for everything else you're trying to set up.
**Long-term use case:** Re-run when looking for any new Claude Code capability. Faster than browsing GitHub.
**Priority:** High
**Action:** `npx claude-code-templates` — run immediately.

---

### ruflo (formerly claude-flow)
**What it does:** Multi-agent orchestration layer with Q-Learning-based routing (agents learn which sub-agent handles which task type over time), 60+ specialized pre-built agents, and swarm coordination primitives.
**Today use case:** Not today — complex setup, overkill for single-developer environment.
**Long-term use case:** When you want to delegate whole workflows (e.g., "analyze this codebase and write tests") to a self-organizing agent swarm.
**Priority:** Medium
**Action:** Install and experiment after individual agent setup is stable. Check README for `npm install -g ruflo`.

---

### awesome-mcp-servers
**What it does:** Community-maintained index of MCP servers, organized by category (databases, APIs, tools, etc.). The canonical "what MCP exists for X" reference.
**Today use case:** Check here before building any MCP integration. Saves hours.
**Long-term use case:** Ongoing reference. Check before every new tool integration.
**Priority:** High (reference)
**Action:** Bookmark https://github.com/punkpeye/awesome-mcp-servers. Check today when adding MCP servers for VS Code, Obsidian, or trading tools.

---

### awesome-agent-skills
**What it does:** Index of 630+ agent skills from official dev teams: Anthropic, Vercel, Stripe, Supabase, etc. Organized by provider and use case.
**Today use case:** Browse before installing skills packs — may surface official skills better than community forks.
**Long-term use case:** First stop before writing any new custom skill.
**Priority:** High (reference)
**Action:** Bookmark. Browse before steps 6-8 in the Action Queue.

---

### claude-code-best-practice
**What it does:** 55K-star collection of Claude Code agents, commands, and skills organized as best practices. Covers CLAUDE.md patterns, hook configurations, and agent design.
**Today use case:** Read the CLAUDE.md patterns section before finalizing your vault's `CLAUDE.md` for multi-CLI setup.
**Long-term use case:** Reference when writing new agents or auditing existing ones.
**Priority:** Medium
**Action:** Read README and the `CLAUDE.md` section today. Don't install anything — it's a reference, not a package.

---

### system-prompts-and-models-of-ai-tools
**What it does:** Extracted and decoded system prompts from Claude Code, Cursor, Devin, Manus, and Replit Agent. Shows exactly what instructions each tool gives itself internally.
**Today use case:** Read the Claude Code and Cursor prompts before configuring your multi-CLI setup. Understanding what Cursor tells itself prevents you from writing CLAUDE.md rules that conflict with Cursor's own behavior.
**Long-term use case:** Reference for writing better skills and agents — learn from how professional teams structure their system prompts.
**Priority:** High (reference)
**Action:** Read `cursor.md` and `claude-code.md` from the repo today. Note any behavioral constraints that would conflict with your `CLAUDE.md`.

---

### anthropics-financial-services
**What it does:** Official Anthropic agents for IB/equity research/KYC workflows, with pre-built MCP connectors for Bloomberg, FactSet, and S&P Global. Production-grade financial agent templates.
**Today use case:** Not today — requires Bloomberg/FactSet access.
**Long-term use case:** When building a trading/research agent stack. These are the reference implementations for financial AI agents.
**Priority:** Medium
**Action:** Revisit when pursuing finance/trading track. Save the MCP connector patterns for S&P Global even if the full agents aren't relevant.

---

### free-claude-code
**What it does:** Proxy server that intercepts Claude Code API calls and reroutes them to NVIDIA NIM, OpenRouter, or local models.
**Today use case:** Not relevant — you have a subscription.
**Priority:** Skip
**Action:** Archive.

---

### vibe-kanban
**What it does:** Kanban board UI for managing parallel agent workflows in isolated git worktrees.
**Priority:** Skip
**Action:** Archive — explicitly sunsetting per vault notes.

---

### dify
**What it does:** Self-hosted LLM app platform for teams: workflow builder, model abstraction, API layer, Docker deployment.
**Priority:** Skip
**Action:** Archive — team-scale infrastructure, not solo agentic tooling.

---

### Scrapegraph-ai
**What it does:** LLM-powered web scraper where you describe what to extract in natural language and it generates the scraping pipeline.
**Today use case:** Not today.
**Long-term use case:** Useful for any data ingestion pipeline that pulls from unstructured web sources.
**Priority:** Low
**Action:** Note in data pipeline context. No integration path with Claude Code directly.

---

### Scrapling
**What it does:** Python scraper that tracks elements across DOM changes using fingerprinting — if a website redesigns, it still finds the same content.
**Today use case:** Not today.
**Long-term use case:** More robust than BeautifulSoup for long-running scrapers in production pipelines.
**Priority:** Low
**Action:** `pip install scrapling` when you need a production-grade scraper.

---

### unsloth
**What it does:** Fine-tuning acceleration for local open-source models (Gemma 4, Qwen3, DeepSeek). Reduces VRAM usage and speeds up training.
**Today use case:** Not today.
**Long-term use case:** When running local model experiments or fine-tuning for specialized tasks.
**Priority:** Low
**Action:** Bookmark for ML pipeline work.

---

### jcode
**What it does:** Rust coding agent harness (6,660 stars). README was empty at time of review.
**Priority:** Skip
**Action:** Archive — can't evaluate.

---

### yt-dlp
**What it does:** CLI downloader for 1,800+ sites.
**Priority:** Skip
**Action:** Archive — not relevant to dev setup.

---

### agency-agents (msitarzewski)
**What it does:** 105K-star repo of complete AI agency personas for `.claude/`: a frontend wizard (knows React/CSS patterns), Reddit ninja (understands social dynamics), whimsy injector (adds personality), reality checker (adversarial critique). Drop `.claude/` contents into any project.
**Today use case:** Clone and copy `.claude/` contents into your global or project-level `.claude/` directory. Instant persona library.
**Long-term use case:** Use as the base set of sub-agent personas. Fork and add your own domain-specific agents.
**Priority:** High
**Action:** `git clone https://github.com/msitarzewski/agency-agents && cp -r agency-agents/.claude/* ~/.claude/`

---

## AI Section (27 repos)

### hermes-agent (Nous Research)
**What it does:** 171K-star coding agent with native ACP (Agent Communication Protocol) and MCP support, meaning it can share MCP servers with Claude Code and be orchestrated by an ACP host.
**Today use case:** Not today — adds complexity before Claude Code is even configured.
**Long-term use case:** Run as a second coding agent on the same MCP server pool. ACP means Claude Code and hermes-agent can hand off tasks to each other.
**Priority:** Medium
**Action:** Install and test after Claude Code is stable. `pip install hermes-agent` (verify).

---

### opencode
**What it does:** 166K-star terminal-first coding agent supporting multiple models (GPT-4, Claude, Gemini, local) from a single TUI.
**Today use case:** Not today — redundant with Claude Code for now.
**Long-term use case:** Use as fallback when Claude Code quota hits or when you want a different model on the same task. Multi-model testing.
**Priority:** Medium
**Action:** `npm install -g opencode` (verify). Install after Claude Code is configured.

---

### browser-use
**What it does:** Python library that wraps Playwright to make web pages agent-accessible: extracts structured data from any page, fills forms, clicks, scrolls — all from a Python API callable by an AI agent.
**Today use case:** Not today.
**Long-term use case:** Standard integration layer for any agent that needs to interact with web UIs. Use with Claude Code's Playwright hook or with hermes-agent.
**Priority:** Medium
**Action:** `pip install browser-use` when building browser-automation agents.

---

### goose
**What it does:** Open-source AI agent in Rust with ACP + MCP native support. Can install/execute/edit/test with any LLM. Rust = fast and low overhead.
**Today use case:** Not today.
**Long-term use case:** ACP native means goose can participate in multi-agent workflows alongside Claude Code and hermes-agent. Good third agent for specialized tasks.
**Priority:** Medium
**Action:** Check Rust install instructions in README. Defer to week 2.

---

### PageIndex
**What it does:** RAG system that uses LLM reasoning chains instead of embeddings to index documents. No vector DB required — the LLM itself does the indexing by reading and structuring the document hierarchy.
**Today use case:** Not today.
**Long-term use case:** Alternative to Milvus-based RAG for document collections where you want explainable retrieval. Good for Jarvis's source summaries if you want to query across them.
**Priority:** Low
**Action:** Test on a `60_Claude/30_Source_Summaries/` folder when evaluating RAG options.

---

### multica
**What it does:** Managed agents platform: assign tasks to agents, track progress, compound agent capabilities. TypeScript, 34K stars.
**Today use case:** Not today.
**Long-term use case:** Platform-level agent management. More useful if you're building a team product than for solo dev.
**Priority:** Low
**Action:** Revisit if building a multi-user agentic product.

---

### MiroFish
**What it does:** Swarm intelligence engine: combines financial forecasting models, social prediction (sentiment from social data), and knowledge graph reasoning into a single prediction pipeline.
**Today use case:** Not today.
**Long-term use case:** If building a trading system, this is one component for the prediction layer. Pairs with TradingAgents.
**Priority:** Low
**Action:** Revisit when building the trading agent stack.

---

### TradingAgents
**What it does:** Multi-agent LLM framework for financial trading with specialized roles: bull analyst, bear analyst, researcher, trader, risk manager. Each agent runs independently and debates before the trader executes.
**Today use case:** Not today.
**Long-term use case:** Reference architecture for building a trading agent. Has an arxiv paper — read that first before trying to run the code.
**Priority:** Medium
**Action:** Read the paper (https://arxiv.org/pdf/2412.20138) first. Then test the framework in a paper trading environment.

---

### openhuman
**What it does:** Personal AI described as "super intelligence" — private, offline, Rust/GPL. Minimal docs from vault notes.
**Priority:** Skip
**Action:** Vault notes are too vague to evaluate. Skip unless more context emerges.

---

### agentscope (Alibaba)
**What it does:** Multi-agent platform: build, visualize, and run agents. MCP-native, multi-modal, backed by Alibaba research. Good reference for seeing how a production multi-agent system is architected.
**Today use case:** Not today — platform overhead.
**Long-term use case:** Reference architecture for multi-agent design. The visualization tools are useful for debugging agent behavior.
**Priority:** Low
**Action:** Read architecture docs. Don't install the full platform.

---

### promptfoo
**What it does:** Testing framework for prompts and agents: write test cases with expected outputs, run them, get pass/fail with diffs. Also does red teaming: generates adversarial prompts to find jailbreaks and hallucination patterns. Used internally by OpenAI and Anthropic.
**Today use case:** Not today — test before you have something to test.
**Long-term use case:** After Claude Code is set up, write a promptfoo test suite for your CLAUDE.md and core skills. Catches regressions when you update skills.
**Priority:** Medium
**Action:** `npm install -g promptfoo` — install in week 2. Run against your CLAUDE.md and key skills.

---

### jan
**What it does:** Fully offline ChatGPT-like interface running 100% on your hardware via LlamaCPP. Tauri desktop app.
**Today use case:** Not today.
**Long-term use case:** Offline fallback when you need AI without internet. Also useful for testing local models.
**Priority:** Low
**Action:** Install if you need offline capability. Not urgent.

---

### ai-engineering-hub
**What it does:** Notebook-first tutorials covering LLMs, RAG, and real-world agents. Published as Jupyter notebooks with runnable code.
**Today use case:** Not today.
**Long-term use case:** Fill knowledge gaps. When you don't understand how a component works (e.g., reranking in RAG), there's likely a notebook here.
**Priority:** Low
**Action:** Bookmark. Use as a reference, not a course.

---

### applied-ml (Eugene Yan)
**What it does:** Curated list of papers and engineering blog posts from companies describing how they run ML in production (Netflix recommendations, Uber demand forecasting, etc.).
**Today use case:** Not today.
**Long-term use case:** When designing any ML pipeline, check here first to see how companies at scale solved the same problem.
**Priority:** Low
**Action:** Bookmark.

---

### Kronos
**What it does:** Foundation model pre-trained on financial time series data. Time series → NLP joint training.
**Priority:** Low
**Action:** Note for finance ML work. Not actionable today.

---

### ASI-Evolve, dots.ocr, whichllm, llmfit, airllm
**Priority:** Skip
**Action:** Archive — research artifacts, local model tools (you have a Claude subscription), or out-of-scope.

---

### free-llm-api-resources
**What it does:** Updated list of free LLM API endpoints with rate limits and capabilities.
**Today use case:** Not today.
**Long-term use case:** If Claude Code quota is exhausted and you need a fallback.
**Priority:** Low
**Action:** Bookmark https://github.com/cheahjs/free-llm-api-resources.

---

### mike
**Priority:** Skip — AI legal platform, out of scope.

---

### GodMode
**What it does:** Electron app showing Claude, GPT, Gemini, and Bing side-by-side in split panes for direct model comparison.
**Today use case:** Already in use per vault notes.
**Long-term use case:** Model comparison during agent design decisions.
**Priority:** Low
**Action:** Already installed per vault notes. No action needed.

---

### jarvis (ethanplusai)
**What it does:** Voice-first AI assistant for macOS using Claude + Whisper + Three.js.
**Priority:** Skip — macOS only.

---

### llm-zoomcamp
**What it does:** 10-week course building a complete RAG system from scratch: vector search, LLM evaluation, monitoring, deployment.
**Today use case:** Not today.
**Long-term use case:** Structured path to understanding RAG deeply. Take after memsearch/claude-context are running and you want to understand what they're doing.
**Priority:** Low
**Action:** Start Module 1 when pursuing the ML/RAG track.

---

## Building Section (7 repos)

### pocketbase
**What it does:** Single Go binary: auth system, SQLite database, file storage, realtime subscriptions over WebSocket, REST + realtime API auto-generated from schema. Zero deployment overhead.
**Today use case:** Not today's setup goal, but if you build anything this week that needs a backend, use this instead of spinning up a full stack.
**Long-term use case:** Backend for any quick app or tool: agent dashboards, data collection, PKM API layer.
**Priority:** Medium
**Action:** `./pocketbase serve` — it's a single binary download. Keep it in your tools folder.

---

### n8n-workflows
**What it does:** 5,000+ automation workflow templates exported from the n8n community. Not the n8n platform itself — just JSON workflow definitions you import.
**Today use case:** If you're running n8n, import these to find Obsidian→VS Code automation templates.
**Long-term use case:** Automation between Obsidian, GitHub, VS Code, and any web service without writing code. Good for the Jarvis→dev layer bridge.
**Priority:** Medium
**Action:** Check if n8n is installed. If yes, browse this repo for Obsidian + GitHub workflows.

---

### public-apis
**What it does:** 437K-star list of free APIs organized by category.
**Priority:** Low (reference)
**Action:** Check here when a project needs an external data source.

---

### tradingview-mcp
**What it does:** MCP server that connects Claude Code to TradingView Desktop: reads active chart data, indicators, and timeframes via the MCP protocol.
**Today use case:** Install if TradingView is on this machine — it's a direct Claude Code MCP integration.
**Long-term use case:** AI-assisted chart analysis inside Claude Code sessions.
**Priority:** Medium
**Action:** Check if TradingView Desktop is installed. If yes, add this MCP server to `~/.claude.json`. Verify config in README.

---

### react-three-fiber
**What it does:** Declarative React wrapper for Three.js — write 3D scenes as React components.
**Priority:** Low
**Action:** Reference when building 3D UIs.

---

### semantic-search-nextjs-pinecone-langchain-chatgpt
**What it does:** Reference implementation: embed documents into Pinecone, semantic search via LangChain + GPT-3, surfaced in a Next.js UI.
**Priority:** Low (reference)
**Action:** Use as a starting template if building a semantic search UI.

---

### ai-weekend-builds
**What it does:** Weekend project starters using the Anthropic API — Python and Node with READMEs.
**Priority:** Low
**Action:** Browse when starting a new Anthropic API project.

---

## Projects Section (11 repos)

### build-your-own-x
**What it does:** 506K-star: step-by-step tutorials for rebuilding core technologies from scratch (databases, shells, operating systems, browsers, git).
**Priority:** Low (reference)
**Action:** Use when you want deep understanding of a technology. Don't try to work through this linearly.

---

### project-based-learning
**What it does:** 266K-star curated list of tutorials that produce working projects, organized by programming language.
**Priority:** Low (reference)
**Action:** Use when starting a new language or framework.

---

### app-ideas
**What it does:** 94K-star app ideas with difficulty tiers: Newbie / Intermediate / Advanced. Each idea has specs.
**Priority:** Low
**Action:** Use the Advanced tier as a project difficulty calibrator.

---

### 500-AI-ML-projects
**What it does:** 500 AI/ML/CV/NLP project ideas with code, organized by domain.
**Priority:** Low (reference)
**Action:** Browse when choosing ML learning projects.

---

### free-programming-books, freeCodeCamp, projectlearn-project-based-learning
**Priority:** Skip — too general or beginner-level.

---

### hermes-desktop-os1
**What it does:** Native macOS UI for Hermes Agent on cloud computers.
**Priority:** Skip — macOS only.

---

### ai-dev-tools-zoomcamp (DataTalksClub)
**What it does:** Free structured course on using AI dev tools effectively: MCP, Claude Code, coding agents, prompt engineering for developers. From the same team as the ML/data engineering zoomcamps.
**Today use case:** This is directly about what you're doing today. Module 1 likely covers Claude Code setup.
**Long-term use case:** Structured path through the exact tools you're configuring.
**Priority:** Medium
**Action:** Start Module 1 this week at https://github.com/DataTalksClub/ai-dev-tools-zoomcamp.

---

## Jobs Section (6 repos)

### Summer2026-Internships
**What it does:** Daily-updated spreadsheet of SWE/DS/AI/quant internship postings for Summer 2026. Maintained by Simplify + Pitt CSC.
**Today use case:** Not today's dev goal, but check this weekly.
**Priority:** Medium (career track)
**Action:** Bookmark and check weekly. Set a recurring reminder.

---

### underclassmen-internships
**What it does:** Curated list of internships and fellowships exclusive to CS freshmen and sophomores for 2026.
**Priority:** Medium (career track)
**Action:** Check once — many of these have early deadlines.

---

### leetcode-companywise-interview-questions, interview-company-wise-problems
**What it does:** Company-tagged LeetCode problems.
**Priority:** Low
**Action:** Use when targeting a specific company for interviews.

---

### tech-interview-handbook
**What it does:** 139K-star: algorithms, behavioral, system design, negotiation — complete interview prep guide.
**Priority:** Low (reference)
**Action:** Read the negotiation section when you have an offer. Use the algorithm patterns as a refresher before interviews.

---

### coding-interview-university
**What it does:** 347K-star complete CS study plan for SWE roles. Covers data structures, algorithms, system design, operating systems — months of content.
**Priority:** Low (long-term)
**Action:** Use as a checklist, not a linear curriculum.

---

## Learning Section (14 repos)

### get-shit-done
**What it does:** 63K-star meta-system for Claude Code by TÂCHES: combines meta-prompting (tells Claude how to think about the task), context engineering (what to load when), and spec-driven execution (constitution → plan → implement). It's a methodology you embed in your CLAUDE.md and workflow.
**Today use case:** Read and extract the CLAUDE.md patterns today. These are directly applicable to the Jarvis CLAUDE.md.
**Long-term use case:** The spec-driven execution pattern replaces ad-hoc prompting for any serious feature work.
**Priority:** High
**Action:** Read README, extract CLAUDE.md patterns, merge into Jarvis CLAUDE.md. No CLI install — it's a methodology.

---

### data-engineering-zoomcamp
**What it does:** 9-week free course: Docker, Postgres, dbt, Kafka, Spark, Kestra, production data pipelines end-to-end.
**Priority:** Low (long-term)
**Action:** Start when pursuing data engineering track. Structured path to production pipelines.

---

### machine-learning-zoomcamp
**What it does:** 4-month free ML engineering course: training, deployment, Docker, Kubernetes, FastAPI serving.
**Priority:** Low (long-term)
**Action:** Start after data engineering zoomcamp.

---

### mlops-zoomcamp
**What it does:** Free MLOps course: experiment tracking (MLflow), deployment (BentoML), monitoring (Evidently), workflow orchestration (Prefect/Airflow).
**Priority:** Low (long-term)
**Action:** Start after machine-learning-zoomcamp. This is the production layer.

---

*(llm-zoomcamp, ai-dev-tools-zoomcamp, applied-ml, system-design-primer, project-based-learning, free-programming-books, 500-AI-ML-projects, app-ideas, ai-engineering-hub — already covered in other sections.)*

---

## Cybersecurity Section (4 repos)

### bumblebee (Perplexity)
**What it does:** Read-only Go CLI that scans on-disk packages and VS Code extensions against a known supply-chain compromise database. Doesn't modify anything — just reports.
**Today use case:** Run this on your dev machine before adding a bunch of new tools. Takes 30 seconds.
**Long-term use case:** Run after every major package install or extension addition.
**Priority:** Medium
**Action:** Check Go install at https://github.com/perplexityai/bumblebee. Run scan today.

---

### keyhacks
**What it does:** Reference list of shell commands to test if leaked API keys are still valid. Used in bug bounty work.
**Priority:** Low
**Action:** Bookmark for security research.

---

### cai (Alias Robotics)
**What it does:** AI-powered pentesting framework: multi-agent, runs automated security assessments.
**Priority:** Low
**Action:** Revisit if doing security research or CTF work.

---

### promptfoo *(also in AI section)*
**What it does:** Testing + red teaming for LLM systems.
**Priority:** Medium — covered above.
**Action:** See AI section entry.

---

## Duplicates (not re-analyzed)

The following repos appear in multiple sections with identical notes:
- `dify` (Claude + AI): Skip
- `unsloth` (Claude + AI): Low
- `llm-zoomcamp` (AI + Learning): Low
- `ai-dev-tools-zoomcamp` (Projects + Learning): Medium — start Module 1 this week
- `applied-ml` (AI + Learning): Low
- `agentscope` (AI + Projects): Low
- `agency-agents` (Claude + Learning): High — covered in Claude section
- `project-based-learning` (Projects + Learning): Low
- `free-programming-books` (Projects + Learning): Skip
- `500-AI-ML-projects` (Projects + Learning): Low
- `app-ideas` (Projects + Learning): Low
- `ai-engineering-hub` (AI + Learning): Low
- `semantic-search-nextjs-pinecone-langchain-chatgpt` (Building + Projects): Low
- `promptfoo` (AI + Cybersecurity): Medium — see AI section

---

*Last updated: 2026-05-29 | Source: [[40_Resources/CS/Repos]]*
