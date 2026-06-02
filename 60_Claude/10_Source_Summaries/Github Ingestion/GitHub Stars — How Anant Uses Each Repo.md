---
type: evergreen
status: sprout
created: 2026-05-29
tags:
  - github
  - resources
  - workflow
  - reference
notes:
  - "[[40_Resources/CS/Repos]]"
---
# GitHub Stars — How Anant Uses Each Repo

Two questions for every starred repo: **how does he use it**, **why does he use it**.

Context: Anant is a UMN CS sophomore (class 2028). He runs BOOM (Rust/Kafka/MongoDB observability work), a Next.js cosmic portfolio with an AI Lab, Jarvis (this vault), a trading AI project, and is setting up VS Code as source of truth with Claude Code, Cursor, Kiro, and Copilot as CLIs. He wants internships, is building toward ML/AI engineering, and needs to actually ship things today.

---

## Today's Goal: VS Code + Claude Setup

These repos are the most immediately relevant to what Anant is doing right now.

---

### ECC (affaan-m)
**How:** Install it. Run `npx ecc install` inside your VS Code project. It drops in a CLAUDE.md, skills, memory layer, and security hooks for Claude Code in one shot. Then point Cursor, Kiro, and Copilot at the same CLAUDE.md so every agent reads the same context.
**Why:** You have four coding agents (Claude, Cursor, Kiro, Copilot) and no shared context between them. ECC is the single fastest way to make VS Code the source of truth — one install wires persistent memory, skills, and constraints into every agent that reads CLAUDE.md.

---

### gstack (garrytan)
**How:** Clone it, read the 23 skill files, steal the ones relevant to BOOM and the portfolio. Specifically: the `founder-review`, `eng-manager`, and `release-manager` skills. Copy them into your `.claude/` directory. Run them as slash commands when shipping.
**Why:** Garry Tan's setup is the most battle-tested public Claude Code config. His skills encode real engineering decisions (security review, QA paranoia, doc writing) as reusable behaviors. You're setting up Claude today — start with a proven skeleton rather than inventing from scratch.

---

### mattpocock-skills
**How:** Install via `npx skills add mattpocock/skills`. Each skill targets a specific Claude failure mode. Use `verbose-thinking` when Claude is producing surface-level answers, `entropy-check` when a refactor starts getting weird, `feedback-loop` for the portfolio AI Lab.
**Why:** Matt's skills are the most opinionated and shortest. They fix the exact problems you'll hit today: Claude going off-track, over-engineering, losing thread. Four skills, four problems. Install before you do any serious Claude Code work this morning.

---

### addyosmani/agent-skills
**How:** `npx skills add addyosmani/agent-skills`. 23 skills covering the full SDLC. The most useful for you today: `spec-first` (use before touching the portfolio), `test-before-ship` (for BOOM), and `observability-check` (directly relevant to your BOOM OpenTelemetry work).
**Why:** Addy works on Chrome DevTools and thinks in production systems. His skills have rationalization tables — they explain why a decision was made, not just what to do. That's exactly what you need when pairing with Kiro or Cursor on BOOM code.

---

### spec-kit (GitHub)
**How:** Install the CLI. Before touching the portfolio today, run `npx spec-kit specify "AI Lab feature"`. It produces a constitution → spec → plan → tasks chain. Feed that plan to Claude Code. Use it for the TradingAgents integration and the portfolio AI Lab rebuild.
**Why:** You have a lot of ambiguous work ahead (portfolio UI, AI Lab, trading dashboard). Spec Kit turns ambiguity into a structured task list before you write a single line. It's how GitHub's own teams avoid vibe coding.

---

### get-shit-done (gsd-build)
**How:** Clone it, read the meta-prompting templates. Before starting any complex session today — portfolio refactor, BOOM instrumentation, Jarvis ingestion — use the GSD "context dump" template to prime Claude with the right state. It takes 2 minutes and saves 20 minutes of drift.
**Why:** Context engineering is the most underrated skill in working with Claude Code. GSD's system gives you a structured way to front-load context so Claude stays on task. Use it every time you start a new VS Code session today.

---

### claude-code-best-practice (shanraisshan)
**How:** Read it once, top to bottom, before the VS Code setup. Copy the CLAUDE.md template, the agent patterns, and the hooks section directly into your Jarvis `.claude/` directory.
**Why:** 55K stars means this is the community consensus on what works. It's a reference, not infrastructure. Read it today, apply the patterns, move on.

---

### system-prompts-and-models-of-ai-tools
**How:** Open the Cursor and Kiro system prompt files. Copy the relevant constraint language into your `.cursor/rules` and Kiro's agent config. Specifically look at how Windsurf and Devin handle context prioritization — steal those patterns for your CLAUDE.md.
**Why:** You're running four agents in VS Code. Each has a different default system prompt. Understanding what they're told by default lets you write CLAUDE.md overrides that actually stick rather than fighting their defaults.

---

### agency-agents (msitarzewski)
**How:** Browse the agent files. The `frontend-wizard`, `reality-checker`, and `tech-debt-ninja` agents are directly useful. Drop them as Claude subagents in your `.claude/agents/` directory. Use `reality-checker` when the portfolio UI refactor gets too ambitious.
**Why:** 105K stars. These agents encode the specific personality + process patterns that make sub-agents useful rather than just prompt alternatives. Your Jarvis already has `anti-slop-editor` and `career-operator` — these fill the product and frontend gaps.

---

### beads (gastownhall)
**How:** Install it for BOOM. When you're doing parallel agent work — Claude handles API, Kiro handles scheduler, Cursor handles observability — use Beads as the shared task tracker. Atomic task claiming means agents don't stomp on each other.
**Why:** BOOM has multiple subsystems. When you're doing multi-agent work in VS Code, you need a coordination layer. Beads is the lightest one that works with Claude Code natively.

---

### vibe-kanban (BloopAI)
**How:** Don't install it yet — it's sunsetting. But read the architecture docs. The worktree-isolation pattern is worth stealing for your own multi-agent workflow: each agent gets an isolated git worktree, they merge back when done.
**Why:** The pattern is more valuable than the tool. When you're running Claude + Cursor + Kiro on the same codebase today, worktree isolation prevents conflicts. The tool is dead but the idea works.

---

### claude-code-templates (davila7)
**How:** Run `npx aitmpl` in your VS Code terminal. Browse the agent/MCP/hook templates. Install the ones relevant to your stack: Next.js, Rust, Python ML pipeline. Takes 10 minutes, gives you a working agent scaffold for every project.
**Why:** You're setting up Claude from scratch today. This CLI gives you 100+ templates instead of writing agent configs by hand. Start with templates, customize as you go.

---

### ruflo (ruvnet)
**How:** Use Ruflo when you need multi-agent swarm behavior — specifically for the trading project where you want analyst + researcher + trader agents coordinating. Run `npx ruflo deploy --agents analyst,researcher,trader` and wire it to your trading data pipeline.
**Why:** Your trading AI Hub needs multiple coordinated agents. Ruflo has Q-Learning routing (agents learn which sub-agent to call) and built-in swarm coordination. It's the only open-source option that approaches TradingAgents' architecture at the infrastructure level.

---

### awesome-mcp-servers (punkpeye)
**How:** Before building any new integration today, ctrl+F the README. If there's already an MCP server for it (TradingView, Supabase, Obsidian), use it instead of building from scratch. Required reading before the Jarvis MCP setup.
**Why:** You have Jarvis MCP, Gmail MCP, Calendar MCP, Supabase MCP all running. Before wiring up anything new today, check this list. It saves hours.

---

### awesome-agent-skills (VoltAgent)
**How:** Search it for "rust", "observability", "next.js". For every BOOM subsystem and portfolio component, check if a skill already exists. Install via the listed command, then customize.
**Why:** 23K skills from official dev teams including Supabase (which you're using) and Vercel (which you may deploy to). The skills for your exact stack probably already exist.

---

### memsearch (Zilliz)
**How:** Install it as a Claude Code plugin. It auto-captures every session and makes your Claude Code memory searchable. After today's vault ingestion, every session becomes findable. Configure it to index your Jarvis vault directory as well.
**Why:** You lose context between Claude Code sessions. Memsearch fixes this by auto-indexing sessions to markdown with hybrid search. Given you're doing serious vault ingestion today, having session memory is critical.

---

### obsidian-mind
**How:** Read the vault structure, not the code. Their 5 lifecycle hooks and 9 subagents are directly portable to Jarvis. The `on-session-start` and `on-session-end` hooks are exactly what your CLAUDE.md is missing. Copy the hook patterns into `.claude/skills/`.
**Why:** You're setting up Jarvis to be the context layer for all your agents today. Obsidian Mind is the most similar vault to Jarvis in structure. Their lifecycle hooks solve exactly the problem you have: agents that don't know where to look on startup.

---

### context-sync
**How:** Deploy it as a local MCP server. It gives Claude Code a persistent SQLite memory with `remember`/`recall` tools. Point it at your Jarvis vault path. Use it as a lightweight alternative to memsearch for the VS Code setup.
**Why:** It's simpler than memsearch, no vector DB needed. For your immediate VS Code setup today, SQLite-backed memory is faster to get running than Milvus. Start with context-sync, graduate to memsearch later.

---

### cpr-compress-preserve-resume
**How:** Install the three slash commands: `/preserve` before ending a session, `/compress` when context gets long, `/resume` at the start of a new session. Use this in every Claude Code session today — Jarvis ingestion is a long session that will hit context limits.
**Why:** Today's vault ingestion will run long. Without CPR, you'll lose context mid-session and waste time re-explaining. The 55% token cost reduction on resume means fewer context resets.

---

### claude-context (Zilliz)
**How:** Install it as an MCP server for BOOM and the portfolio. It indexes your entire codebase into Milvus (or local) and lets Claude Code do semantic code search. Most useful for BOOM's sprawling Rust codebase — instead of telling Claude where things are, let it search.
**Why:** BOOM has `src/alert/*`, `src/api/*`, `src/scheduler/*`, `src/kafka/*`, `src/utils/o11y/*` — it's large. Claude Code without semantic search will hit token limits trying to hold the full codebase. This gets you to ~40% token reduction.

---

### graphify
**How:** Run it on your Jarvis vault after today's ingestion. It builds a NetworkX knowledge graph from any folder and exports an Obsidian vault — which you already have. The output is a visual map of your knowledge connections that you can't see in the file tree.
**Why:** You're ingesting 100 repos + all your vault today. After this session, your vault will have hundreds of cross-links. Graphify shows you which areas are dense (well-connected) and which are orphaned, so tomorrow you know where to focus enrichment.

---

### free-claude-code
**How:** If you hit Claude Code rate limits today during the heavy vault ingestion, set up the proxy. It routes Claude Code API calls to NVIDIA NIM or OpenRouter using cheaper/free models. Keep Claude itself for high-stakes writing; route grunt work through the proxy.
**Why:** Today is a heavy session. Rate limits will hurt. The proxy means you don't stop when your Claude credits get thin — you downgrade gracefully to a free model for the mechanical tasks.

---

### anthropics/financial-services
**How:** Study the agent architecture, not the code. The Bloomberg MCP + FactSet connector pattern is the template for your trading dashboard. When you build the trading AI Hub, model the data agent on Anthropic's equity research agent.
**Why:** This is Anthropic's official finance agent implementation. Your Stocks Trading AI Hub needs the same pattern: data ingestion agent → analysis agent → signal agent. The official implementation shows you the right agent boundary design.

---

---

## BOOM (Rust / Observability / Distributed Systems)

---

### promptfoo
**How:** Set it up to test BOOM's alert processing pipeline. Write test cases for edge-case alert inputs (malformed packets, missing fields, duplicate source IDs). Run `promptfoo eval` in CI before merging.
**Why:** You built observability for BOOM. The next step is testing it. Promptfoo tests AI agent behavior the same way OpenTelemetry tests service behavior — with structured inputs and expected outputs. Used by Anthropic internally.

---

### dots.ocr (rednote-hilab)
**How:** Use it in BOOM's enrichment pipeline for any alert that includes image cutouts (BOOM stores image cutouts). Instead of a custom OCR step, pipe cutout images through dots.ocr to extract text/metadata from the image.
**Why:** BOOM stores astronomical image cutouts. If any enrichment logic needs to parse text from those images (source catalog overlays, instrument metadata burned into images), dots.ocr handles it without a separate ML model deployment.

---

### airllm
**How:** Run the BOOM enrichment classifier models locally on your laptop using airllm. You have a 4GB GPU; airllm lets you run 70B parameter models in that constraint via layer streaming. Use this when testing model outputs for the ML pipeline project.
**Why:** Your Observability-First ML Pipeline brief calls for ONNX or scikit-learn inference. Airllm extends that — when you want to test LLM-based enrichment locally without cloud costs.

---

### ASI-Evolve (GAIR-NLP)
**How:** Read the paper. The task evolution methodology — starting with simple tasks and evolving toward ASI-level complexity — is directly applicable to your filter evaluation pipeline in BOOM. Use it to design a training curriculum for BOOM's classifiers.
**Why:** BOOM classifiers need to generalize across rare astronomical events. ASI-Evolve's curriculum-based training is the right pattern for rare-event classification where you can't just throw data at the problem.

---

---

## Portfolio (Next.js / Three.js / AI Lab)

---

### browser-use
**How:** Use it to build the "Portfolio Lab" AI agent on your portfolio website. Instead of a static chatbot, the AI Lab can use browser-use to navigate your GitHub, pull your latest commit activity, and present it dynamically to a recruiter.
**Why:** Your portfolio's AI Lab needs to be dynamic, not static. Browser-use gives it the ability to actually browse and retrieve live information rather than just answering from embedded data. This is the differentiator that makes "AI Lab" feel real.

---

### semantic-search-nextjs-pinecone-langchain-chatgpt
**How:** This is the exact template for your portfolio AI Lab. Fork it, replace the Pinecone/OpenAI stack with your preferred backend (Supabase pgvector + Claude), and embed your resume, README files, and BOOM docs as the knowledge base.
**Why:** The portfolio's AI Lab feature is essentially this: embed your materials, semantic search over them, return relevant answers. This repo is a working implementation. Instead of building from scratch, adapt it.

---

### react-three-fiber
**How:** You're already using Three.js in the portfolio. Migrate the `ObsidianBackground` component to use react-three-fiber for cleaner React integration. The particle sphere becomes a proper R3F scene with hooks, declarative JSX, and better performance.
**Why:** Your portfolio has Three.js spaghetti right now. R3F brings it into the React component model — declarative, composable, hookable. The cosmic background, particle sphere, and floating card effects all become maintainable.

---

### pocketbase
**How:** Replace Sanity with PocketBase for the portfolio's data layer. PocketBase is one Go binary: auth, database, file storage, realtime — all in one. No paid CMS subscription, runs locally and on a $5 VPS.
**Why:** Sanity has pricing. PocketBase is free and self-hosted. For a portfolio that needs profile data, projects, experience, and blog posts — PocketBase handles all of it in one binary. You can deploy it on the same VPS as your portfolio.

---

### GodMode (smol-ai)
**How:** Use it when comparing Claude vs Cursor vs Kiro responses side by side during the portfolio AI Lab development. Open GodMode, paste your prompt, see all four model responses simultaneously.
**Why:** You're building an AI Lab that needs to give good answers. Testing your prompts across multiple models simultaneously is the fastest way to find the best approach without switching between browser tabs.

---

### jarvis (ethanplusai)
**How:** Study the voice interface pattern. For your portfolio's AI Lab, a voice-activated overlay would be a standout feature. ethanplusai's jarvis is exactly this: talk → Three.js visualizes response → Claude acts. Copy the voice interface pattern.
**Why:** Your portfolio brief mentions "charismatic", "interactive", "impressive small things". Voice interaction is one of those things. ethanplusai has already built it in Python — port the voice pipeline into your Next.js AI Lab.

---

### dify
**How:** Don't install it for the portfolio. But read the workflow builder UI. Dify's visual pipeline builder is the inspiration for your portfolio's "proof pack" generator — the feature that auto-generates a recruiter brief from your materials.
**Why:** Your portfolio AI Lab needs a "Generate proof pack" button. Dify's workflow templates show you how to structure the multi-step pipeline (retrieve materials → summarize → format for recruiter) as a proper agentic workflow.

---

---

## Trading / Finance

---

### TradingAgents
**How:** Use this as the architecture for your Stocks Trading AI Hub. The analyst/researcher/trader/risk-manager agent structure maps directly to your project brief. Replace their data source with Alpha Vantage, keep the agent communication pattern.
**Why:** Your trading project is currently a monolithic pipeline. TradingAgents shows you the right separation: each agent is a specialist, they communicate through structured messages. This is how you go from a toy model to something portfolio-worthy.

---

### Kronos
**How:** Fine-tune or prompt Kronos (or use their pre-trained weights) as the time-series foundation model for your trading signals. Feed it the same Alpha Vantage data you're already pulling. Kronos understands financial language natively.
**Why:** Your trading project uses scikit-learn classifiers. Kronos is a foundation model trained on financial market language — it understands price sequences the same way an LLM understands text. The signal quality difference is significant.

---

### MiroFish
**How:** Integrate MiroFish's swarm intelligence approach as the decision layer for your trading dashboard. Instead of one model predicting direction, run a swarm of agents with different market views and take the consensus signal.
**Why:** Ensemble models beat individual models. MiroFish's swarm approach is the production pattern for financial forecasting. Your dashboard gets a qualitatively better signal source without building a new model — you just architect the agents differently.

---

### tradingview-mcp
**How:** Connect it to Claude Code. Use it to run chart analysis on your Alpha Vantage data: send a ticker, get Claude's interpretation of the chart pattern, route that interpretation into the analyst agent of your TradingAgents setup.
**Why:** Your trading dashboard needs chart analysis. Instead of building a technical analysis module from scratch, tradingview-mcp gives you Claude's visual chart reading as a tool call. It connects your existing TradingView workflow to the AI pipeline.

---

### Scrapegraph-ai
**How:** Use it in the trading data pipeline to scrape financial news, earnings summaries, and market commentary. Natural language description of what to scrape → structured data. Hook it into the researcher agent in your TradingAgents setup.
**Why:** Your trading project needs news and sentiment data alongside price data. Scrapegraph-ai lets you describe what you want in English and get structured output — no CSS selectors, no brittle scrapers.

---

### Scrapling
**How:** Use Scrapling instead of raw BeautifulSoup for the trading pipeline's data ingestion. It tracks DOM elements across site changes, so when Yahoo Finance or Alpha Vantage's HTML changes, your scraper doesn't break.
**Why:** Your trading pipeline scrapes price data. All scrapers break when sites change their HTML. Scrapling tracks elements adaptively — when the DOM changes, it still finds what you asked for.

---

---

## Jarvis / Knowledge System

---

### PageIndex
**How:** Build Jarvis's query engine on top of PageIndex. When you ask "what do I know about observability?", PageIndex runs reasoning over your vault's document index rather than similarity search. This is better for the complex cross-domain queries Jarvis needs to answer.
**Why:** Jarvis's retrieval is currently based on Obsidian search and Dataview. PageIndex gives you vectorless RAG — the LLM reasons about your vault structure rather than matching embeddings. For a knowledge system built on connections between ideas, this is architecturally better.

---

### memsearch (Zilliz)
**How:** Install it for all your Claude Code sessions. Every session gets auto-indexed to markdown and stored with ONNX embeddings + Milvus. When you start a new session tomorrow, `/memory-recall "BOOM observability"` surfaces exactly what you worked on.
**Why:** Jarvis's north star is "every AI reads shared context before helping". Memsearch makes that real for Claude Code — your sessions become searchable memory, not lost context.

---

### graphify
**How:** Run monthly on the full Jarvis vault. The NetworkX knowledge graph shows you which concepts are densely connected (mature areas) and which are orphaned (gaps to fill). Export to Obsidian format for integration.
**Why:** You're building a research engine. Graphify gives you the meta-level view — where are the knowledge clusters, where are the deserts. This is what the Knowledge Enrichment Dashboard is trying to show but can't without a graph.

---

### obsidian-mind
**How:** Extract the 5 lifecycle hooks. Implement them in your CLAUDE.md:
- `on-session-start`: read log.md tail + dashboard
- `on-task-complete`: write to log.md
- `on-context-full`: trigger /compress
- `on-vault-write`: validate frontmatter
- `on-session-end`: run /closeday
**Why:** Jarvis's biggest gap right now is that Claude doesn't have reliable lifecycle behavior — it sometimes reads context, sometimes doesn't. Lifecycle hooks make this structural rather than hoped-for.

---

### context-sync
**How:** Run as a local MCP. Wire it to Jarvis so Claude Code can `remember` key facts from sessions and `recall` them on the next session start. Use it alongside memsearch — context-sync for fast recall, memsearch for deep search.
**Why:** The two-layer memory architecture: context-sync handles quick facts (SQLite, instant), memsearch handles semantic search (Milvus, thorough). Together they cover Jarvis's memory needs without over-engineering.

---

### n8n-workflows
**How:** Browse the 5K+ workflows. The ones immediately useful: GitHub → Obsidian sync, email digest → vault note, web scrape → vault clipping. Use them to automate the "raw capture" step for Jarvis's ingestion pipeline.
**Why:** Jarvis's ingestion pipeline (web → clippings → summaries) is currently manual. n8n workflows automate the web-to-vault step. Pick 3 workflows today that replace manual work you're doing.

---

---

## Learning / DataTalksClub Courses

---

### data-engineering-zoomcamp
**How:** Work through it in parallel with BOOM. Week 1 covers Docker + Kafka — directly relevant to BOOM's architecture. Week 3 covers dbt + data warehousing — use it to design the BOOM MongoDB → analytics pipeline.
**Why:** BOOM is a data engineering system. This course formalizes the patterns you're already using. Doing it while working on BOOM means you can apply each concept immediately.

---

### machine-learning-zoomcamp
**How:** Work through it for the trading AI Hub. The deployment + Docker + Kubernetes weeks are exactly what you need to take your trading model from a Jupyter notebook to something running on a VPS.
**Why:** Your trading dashboard brief ends at "Week 4: documentation." This course shows you Week 5: deployment, monitoring, and maintenance — the parts that make a project portfolio-worthy rather than just demo-worthy.

---

### mlops-zoomcamp
**How:** Apply it to the Observability-First ML Pipeline project. The MLOps patterns (tracking, deployment, monitoring, workflow orchestration) are the production version of what your project brief is sketching. Use MLOps Zoomcamp as the production blueprint.
**Why:** Your Observability-First ML Pipeline brief is a week-4 project. MLOps Zoomcamp shows you what a real production version of that system looks like. The gap between your brief and the course content is your growth edge.

---

### llm-zoomcamp
**How:** Work through the RAG and vector search weeks for Jarvis's query engine. The evaluation week is critical — build the same eval framework for Jarvis so you can measure whether answers are getting better.
**Why:** Jarvis needs a measurable quality standard. Right now you don't know if your RAG setup is good or bad. LLM Zoomcamp's evaluation module gives you the tooling to find out.

---

### ai-dev-tools-zoomcamp
**How:** Go through it this week. It covers Claude Code, MCP, and coding agents explicitly — exactly what you're setting up today. The course gives you the structured path that makes this session's "set up Claude completely" goal actually stick.
**Why:** You're learning Claude Code by doing today, which is the right approach. But a structured course prevents the gaps. DataTalksClub courses are free, cohort-based, and built for practitioners.

---

### applied-ml
**How:** Bookmark the sections on recommendation systems, search, and embeddings. When you're building the Jarvis semantic index or the portfolio AI Lab, check this list for real company implementations of what you're building. Then do the same thing better.
**Why:** Eugene Yan curates actual production ML papers from Google, Spotify, Netflix, Airbnb. Your implementations should match or beat industry baseline. This is how you know what "good" looks like.

---

### ai-engineering-hub
**How:** Pull it as a Jupyter notebook reference. Before implementing any RAG pipeline — for Jarvis, for the portfolio, for the trading system — check if there's a working notebook here. There usually is.
**Why:** 35K stars, all notebooks. When you're stuck on "how do I actually implement this RAG pattern", there's a working example. Reference first, implement second.

---

---

## Career / Internships

---

### Summer2026-Internships
**How:** Star the specific companies you're targeting. Check it daily. Set up a GitHub notification or build a simple n8n workflow to alert you when new postings appear for your target companies.
**Why:** This repo is updated daily. Internship postings expire fast. Checking it once a week is too slow — you need a daily trigger.

---

### underclassmen-internships
**How:** Go through every entry. As a freshman/sophomore (class 2028), you qualify for all of these. Add the open applications to your Internship tracker in `20_Progress/Internship/`. Apply to at least 5 this week.
**Why:** You're a sophomore. Most internship lists are aimed at juniors. This list exists specifically for you. Every entry is an opportunity you can actually apply to.

---

### tech-interview-handbook
**How:** Use the behavioral interview section now. Use the algorithm section 2 months before interviewing. The system design section is relevant for BOOM — practice explaining BOOM's architecture as a system design answer.
**Why:** BOOM is a real distributed system. You can use it as your system design answer: "I worked on a Rust-based alert broker processing survey streams through Kafka → Redis → MongoDB with OpenTelemetry observability." This handbook shows you how to frame that for an interview.

---

### coding-interview-university
**How:** Use it as a structured study plan, not a reading list. Pick one topic per week that aligns with your coursework. Hash tables while you're taking algorithms. Trees when you hit tree problems at BOOM.
**Why:** 347K stars means this is the community consensus on what you need to know. It's comprehensive to a fault — don't try to do it all. Use it as a checklist: what have I learned, what do I still need.

---

### leetcode-companywise-interview-questions
**How:** Before interviewing at a specific company, look up their tag. Sort by frequency, do the top 10 problems. Then do the top 3 again until you're fast.
**Why:** Generic LeetCode practice is inefficient. Company-specific practice is high-signal. When you have a Google phone screen, do Google's top 10 LeetCode problems, not random mediums.

---

### interview-company-wise-problems
**How:** Download the CSVs for your target companies (Google, Amazon, Meta, Anthropic). Import them into a tracking spreadsheet. Cross off problems as you solve them.
**Why:** More up-to-date than the other repo (updated June 2025). Better structured for bulk download and tracking. Use this alongside the other one — they have different coverage.

---

### system-design-primer
**How:** Read the "Design a distributed message queue" and "Design a search system" sections. Map each pattern to BOOM: BOOM's Kafka = distributed message queue, BOOM's MongoDB filter system = search with ranking.
**Why:** System design interviews for any data/backend role will include distributed systems. You've actually built one. The primer helps you articulate what you built in interview language.

---

---

## AI Agents & Frameworks

---

### hermes-agent (NousResearch)
**How:** Study the architecture, not the code. The agent-grows-with-you model means persistent skill accumulation — copy that pattern into your Jarvis agent setup. Use their MCP integration config as a template for connecting Kiro to Jarvis.
**Why:** 171K stars means this is what the community converged on. Whether you use it or not, understanding its architecture tells you what people expect from a modern coding agent. Build Jarvis to match the best of it.

---

### opencode (anomalyco)
**How:** Install it as your fallback CLI when Claude Code hits rate limits. It's TypeScript, multi-model, and works with your existing `.claude/` directory. Point it at the same CLAUDE.md.
**Why:** You need redundancy. When Claude Code is rate-limited, you need another agent that reads the same context. opencode is the closest thing to a drop-in CLI alternative.

---

### goose (aaif-goose)
**How:** Use Goose for the tasks where you want an autonomous agent that installs dependencies, runs commands, and edits files without you being in the loop. Point it at the BOOM repo and ask it to add a test for the Kafka consumer.
**Why:** Claude Code is interactive; Goose is more autonomous. For BOOM's test-writing tasks (which are mechanical and well-defined), Goose can run autonomously while you do other things. ACP + MCP native means it reads your existing tool configuration.

---

### multica
**How:** Use it when you need to assign work across multiple agents in parallel. The "turn coding agents into teammates" model: you create a task, multica routes it to the right agent, tracks progress. Use it for the portfolio refactor where frontend (Cursor) and backend (Claude) can work in parallel.
**Why:** You're running Claude, Cursor, Kiro, and Copilot. Without task coordination, you'll end up with merge conflicts and duplicated work. Multica is the task dispatch layer.

---

### agentscope
**How:** Use agentscope's multi-agent patterns as the template for your TradingAgents implementation. The library has built-in support for MCP, multi-modal, and multi-agent pipelines — wire it to your trading data sources.
**Why:** TradingAgents needs a production-grade multi-agent runtime. Agentscope is Alibaba-backed, actively maintained, and specifically designed for the analyst-researcher-trader agent pattern. It's more structured than rolling your own.

---

### jan
**How:** Install Jan for local model testing. When you need to test a prompt or pipeline without hitting Claude API costs, run it in Jan first. Keep it running in the background as a cheap inference layer.
**Why:** Local inference for development, Claude API for production. Jan runs every major open-weight model. Use it to prototype the Jarvis query engine before paying for Claude API calls.

---

### whichllm
**How:** Run it: `npx whichllm`. It scans your hardware, finds all compatible GGUF models, ranks them by actual benchmark scores. Use the output to pick the right local model for each task: coding (use a code model), writing (use a general model), summarization (use a cheap model).
**Why:** You have Jan installed, you have local models. But "which model should I run?" is a real question. whichllm answers it based on your actual hardware, not parameter count.

---

### llmfit
**How:** Run it before installing any local model. It tells you what fits your hardware across hundreds of models and providers. Use it alongside whichllm: whichllm for GGUF local, llmfit for API providers.
**Why:** You want to use cheap models for grunt work (janitor tasks, formatting, simple rewrites) and expensive models for hard work (architecture decisions, code review). llmfit maps your hardware to the right model tier.

---

### free-llm-api-resources
**How:** Before paying for any API access today, check this list. For prototype-level work on the trading dashboard and portfolio AI Lab, free inference endpoints reduce burn rate.
**Why:** You're building multiple projects. Running all of them on paid APIs adds up fast. Free endpoints for development, paid for production.

---

### openhuman
**How:** Watch this project. When you build the portfolio AI Lab's core model, openhuman's local-first AI super intelligence pattern is the long-term direction — private, not calling home to Anthropic.
**Why:** Your portfolio's AI Lab is currently OpenAI-dependent. openhuman is the 29K-star proof that a serious local-first AI assistant is possible. For a privacy-conscious portfolio AI that recruiters can interact with without data leaving the server, this is the architecture.

---

---

## Project Starters & Ideas

---

### build-your-own-x
**How:** When you need a portfolio project that demonstrates deep understanding, use this. Pick something you use daily (a mini Kafka, a simple MongoDB driver, a basic HTTP server in Rust) and build it. The process teaches more than reading docs.
**Why:** You work on BOOM which uses Kafka, MongoDB, and a custom HTTP API. Building toy versions of these tools makes you genuinely understand them — not just use them. This is the difference between "I used Kafka" and "I understand Kafka."

---

### app-ideas
**How:** Use the Advanced tier when you need a portfolio project that's scoped correctly — complex enough to be interesting, not so complex it takes months. Pick one that intersects with your skills: a full-stack app with a Python ML backend.
**Why:** The Newbie/Intermediate/Advanced tiers give you an honest difficulty estimate. As a sophomore building toward ML internships, Advanced-tier full-stack + ML projects are the right target.

---

### 500-AI-ML-projects
**How:** Use it as a roadmap. Find the 5 projects most relevant to your stated ML focus (data pipelines, RAG, agents) and do those first. The project list is essentially a curriculum.
**Why:** You want to build toward ML/AI engineering. This list maps the landscape of what people actually build. Use it to avoid reinventing common projects and instead extend them.

---

### project-based-learning
**How:** Use the Rust section for BOOM-adjacent projects. Use the Python section for the trading pipeline. Use it when you want to go deep on a specific language rather than just using it for a project.
**Why:** Learning Rust for BOOM is different from learning Rust for systems programming. The project-based approach ties the learning to a deliverable, which matches how you learn.

---

### freeCodeCamp
**How:** Use the data visualization and ML certifications. Both are directly relevant: data viz for the trading dashboard, ML for the pipeline project. Do the certification to have something concrete to show.
**Why:** Free, self-paced, respected certification. As a sophomore, certifications fill the credentialing gap that employment history hasn't filled yet.

---

### free-programming-books
**How:** Use it to find free textbooks for your coursework. When you're covering algorithms or systems in class and the course textbook is expensive, find the free equivalent here.
**Why:** Textbooks are expensive. Free equivalents exist for everything you're studying. This list aggregates them.

---

### ai-weekend-builds
**How:** Pick one project from this list this weekend. They all use the Anthropic API (which you have) and have starter code. The goal is a shipped demo by Sunday, not a perfect project.
**Why:** You need shipped demos for your portfolio. These are scoped to two days with working starter code. This is how you go from "projects I'm building" to "projects I shipped."

---

### hermes-desktop-os1
**How:** Study it when building the portfolio AI Lab interface. The macOS workspace pattern — agent running on cloud computer, accessible from local UI — is what your portfolio's AI Lab could become.
**Why:** Your portfolio AI Lab's most impressive version is an agent that actually does things (runs code, browses GitHub, generates reports) rather than just answering questions. Hermes desktop is the reference architecture for agent-as-workspace.

---

---

## Security

---

### bumblebee (Perplexity)
**How:** Run it on your development machine and BOOM's deployment environment. It scans installed packages and extensions for known supply-chain compromises. Run it before any major dependency update.
**Why:** You're adding MCPs and plugins to VS Code today. Every MCP is a supply chain attack surface. Run bumblebee first, then add extensions.

---

### keyhacks
**How:** When you find a leaked API key (in a repo, in logs, in a commit history), use this to verify if it's still active before reporting it. Also use it to audit your own repos for accidentally committed keys.
**Why:** You're working with API keys (Alpha Vantage, Anthropic, Supabase, etc.). This is the reference for what a leaked key can do and how to verify it. Know this before you accidentally commit one.

---

### cai (aliasrobotics)
**How:** Use it for the cybersecurity section of your portfolio. Run CAI against your own portfolio's authentication flow (if you add auth) and your trading API endpoints. Document the findings.
**Why:** A portfolio that includes "I ran AI-assisted pentesting on my own system and documented the findings" is significantly more impressive than one that doesn't. CAI is the tool; your BOOM API is the target.

---

### promptfoo *(also relevant here)*
**How:** Use promptfoo's red teaming mode against your portfolio's AI Lab. Try to jailbreak your own AI Lab before a recruiter does. Document what you found and fixed.
**Why:** Your portfolio AI Lab is a public-facing LLM interface. Prompt injection is a real attack vector. Testing your own system and documenting the security measures is a strong engineering signal.

---

---

## Utility

---

### public-apis
**How:** Before building any data pipeline that needs external data, ctrl+F this list. For your trading dashboard, find free financial APIs. For the portfolio AI Lab, find APIs that make it dynamic.
**Why:** Building an API client from scratch when a free API exists is wasted time. This is the canonical list. Check it first.

---

### yt-dlp
**How:** Use it to download conference talks and YouTube tutorials for offline study. Build a small n8n workflow: interesting YouTube video → yt-dlp download → Whisper transcription → Jarvis vault note.
**Why:** You consume a lot of technical content on YouTube. yt-dlp + Whisper transcription turns video into searchable text in your vault. This is a Jarvis enrichment pipeline worth building.

---

### mike
**How:** Keep it bookmarked for when you need legal document analysis. The open source AI legal platform can help interpret internship contract clauses, IP assignment agreements, and research agreements.
**Why:** UROP contracts, internship offers, and open-source licenses all have legal language. Mike gives you AI-assisted interpretation without paying a lawyer.

---

### GodMode *(utility use)*
**How:** Use it for prompt comparison during model selection. When choosing between Claude, Cursor, and Copilot for a specific task, paste the prompt into GodMode and see all responses side-by-side.
**Why:** You have four AI subscriptions. GodMode shows you which one actually gives the best answer for a given task. This is how you allocate agents intelligently rather than defaulting to whatever you have open.

---

---

## Summary: Use Order for Today

1. **Install first** (takes < 10 minutes each): ECC, mattpocock-skills, cpr-compress-preserve-resume, context-sync
2. **Read before writing** (15 minutes): get-shit-done templates, claude-code-best-practice top section, system-prompts
3. **Run on your codebase**: bumblebee (security check), claude-code-templates (scaffold), whichllm (pick local model)
4. **Architecture reference** (open as tabs): TradingAgents, PageIndex, semantic-search-nextjs, obsidian-mind
5. **Apply later this week**: spec-kit for portfolio AI Lab, promptfoo for testing, memsearch for persistent memory
6. **Work through over the next month**: DataTalksClub zoomcamps (data-eng, mlops, llm), coding-interview-university, applied-ml
