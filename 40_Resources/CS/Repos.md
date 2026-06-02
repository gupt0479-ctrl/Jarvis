---
type: evergreen
status: sprout
created: 2026-05-05
updated: 2026-05-29
tags:
  - evergreen
  - github
  - resources
notes: null
---
# GitHub Stars Index
Organized by GitHub list. Each section mirrors the star list on [gupt0479-ctrl's profile](https://github.com/gupt0479-ctrl?tab=stars).
## Claude (28)

Claude Code tooling, memory systems, agent infrastructure. All entries have individual notes.

- [[ECC|ECC]] — agent harness for Claude Code: skills, instincts, persistent memory, and a security layer in a single install
- [[gstack|gstack]] — 13 cognitive-mode skills (founder review, eng review, paranoid QA) plus a Playwright browser for Claude Code
- [[mattpocock-skills|Skills (mattpocock)]] — 18 skills targeting the four main agent failure modes: misalignment, verbosity, broken feedback loops, entropy
- [[agent-skills-addyosmani|Agent Skills (Addy Osmani)]] — 23 skills covering the full SDLC, each with rationalizations tables and evidence requirements
- [[obsidian-mind|Obsidian Mind]] — Obsidian vault template built for agents: 5 lifecycle hooks, 18 slash commands, 9 subagents, QMD semantic search
- [[cpr-compress-preserve-resume|CPR — Compress, Preserve, Resume]] — three slash commands (/preserve, /compress, /resume) for session lifecycle and ~55% token cost reduction on restart
- [[memsearch|memsearch (Zilliz)]] — auto-captures every Claude Code session to markdown, indexes with ONNX embeddings + Milvus, exposes /memory-recall
- [[context-sync|Context Sync]] — local SQLite MCP memory layer with `remember`/`recall` tools and git coupling analysis
- [[claude-context|Claude Context (Zilliz)]] — MCP server that indexes a codebase into Milvus for semantic code search; claims ~40% token reduction
- [[graphify|Graphify]] — Claude Code skill that builds a NetworkX knowledge graph from any folder and exports an Obsidian vault
- [[spec-kit|Spec Kit (GitHub)]] — GitHub's spec-driven development CLI: constitution → specify → clarify → plan → tasks → implement
- [[beads|Beads (bd)]] — Dolt-backed CLI issue tracker with atomic task claiming and dependency graphs for multi-agent coordination
- [[claude-code-templates|Claude Code Templates]] — npm CLI to browse and install 100+ Claude Code agents, MCPs, hooks, and skills interactively
- [[ruflo|Ruflo (formerly claude-flow)]] — multi-agent orchestration with Q-Learning routing, 60+ specialized agents, and swarm coordination
- [[awesome-mcp-servers|Awesome MCP Servers]] — canonical community index of MCP servers by category; check before building any new integration from scratch
- [[awesome-agent-skills|Awesome Agent Skills]] — 630+ agent skills index from official dev teams (Anthropic, Vercel, Stripe, Supabase, etc.)
- [[claude-code-best-practice|Claude Code Best Practice]] — 55K-star best practices collection with agents/commands/skills; reference read, not infrastructure
- [[system-prompts-and-models-of-ai-tools|system-prompts-and-models-of-ai-tools]] — extracted system prompts from Claude Code, Cursor, Devin, Manus, Replit; useful for CLAUDE.md and skill writing
- [[anthropics-financial-services|Claude for Financial Services (Anthropic)]] — official IB/equity research/KYC agents with Bloomberg, FactSet, S&P Global MCP connectors
- [[free-claude-code|Free Claude Code]] — proxy server that reroutes Claude Code API calls to NVIDIA NIM, OpenRouter, or local models
- [[vibe-kanban|Vibe Kanban]] — sunsetting kanban board for parallel agent workflows in isolated worktrees; watch for a successor
- [[dify|Dify]] — self-hosted LLM app platform for teams building products; full Docker deployment, not solo agentic tooling
- [[Scrapegraph-ai|ScrapeGraph AI]] — LLM-powered web scraping via natural language description; no Claude integration path
- [[Scrapling|Scrapling]] — resilient Python scraper that tracks elements across DOM changes; useful data pipeline utility
- [[unsloth|Unsloth]] — fine-tuning acceleration for local open models; orthogonal to Claude Code stack but useful for ML pipeline work
- [[jcode|jcode]] — Rust coding agent harness with 6,660 stars; can't evaluate (README empty at time of review)
- [[yt-dlp|yt-dlp]] — feature-rich CLI audio/video downloader for 1,800+ sites; useful utility
- [[agency-agents|Agency Agents (msitarzewski)]] — 105K-star complete AI agency in your .claude: frontend wizard, Reddit ninja, whimsy injector, reality checker

---

## AI (27)

AI agents, frameworks, models, and LLM tooling.

- [hermes-agent](https://github.com/NousResearch/hermes-agent) — 171K-star Nous Research coding agent with ACP/MCP/Claude Code support; the most-starred agent on GitHub right now
- [opencode](https://github.com/anomalyco/opencode) — 166K-star open source coding agent; terminal-first, multi-model, actively developed alternative to Claude Code
- [browser-use](https://github.com/browser-use/browser-use) — 96K-star Python library making websites accessible for AI agents via Playwright; the standard for browser automation
- [goose](https://github.com/aaif-goose/goose) — 46K-star open source extensible AI agent (Rust); install/execute/edit/test with any LLM; ACP + MCP native
- [PageIndex](https://github.com/VectifyAI/PageIndex) — 32K-star vectorless reasoning-based RAG (no embeddings); document index using LLM reasoning chains
- [multica](https://github.com/multica-ai/multica) — 34K-star open-source managed agents platform: assign tasks, track progress, compound skills; TypeScript
- [MiroFish](https://github.com/666ghj/MiroFish) — 63K-star swarm intelligence engine for prediction; financial forecasting + social prediction + knowledge graphs; Python
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents; [paper](https://arxiv.org/pdf/2412.20138)
- [openhuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL; tinyhumans.ai
- [agentscope](https://github.com/agentscope-ai/agentscope) — 25K-star build and run agents you can see and trust; MCP-native, multi-modal, multi-agent; Alibaba-backed
- [promptfoo](https://github.com/promptfoo/promptfoo) — test prompts, agents, RAGs; red teaming + vulnerability scanning; used by OpenAI and Anthropic internally
- [jan](https://github.com/janhq/jan) — 42K-star fully offline ChatGPT alternative; runs 100% locally on your hardware; Tauri + LlamaCPP
- [dify](https://github.com/langgenius/dify) *(also in Claude)* — 143K-star production-ready agentic workflow platform; Docker deployment; team-scale LLM app builder
- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) — 35K-star in-depth tutorials on LLMs, RAGs, real-world agents (Jupyter notebooks); Daily Dose of DS
- [applied-ml](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan
- [Kronos](https://github.com/shiyu-coder/Kronos) — 27K-star foundation model for financial markets language; time series + NLP; Python
- [ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) — GAIR-NLP research on ASI-level task evolution for training superhuman agents; Python
- [dots.ocr](https://github.com/rednote-hilab/dots.ocr) — multilingual document layout parsing in a single VLM; from RedNote (Xiaohongshu) research
- [whichllm](https://github.com/Andyyyy64/whichllm) — CLI: find the local LLM that actually runs on your hardware; ranked by real benchmarks, not parameter count
- [llmfit](https://github.com/AlexsJones/llmfit) — hundreds of models/providers, one command to find what fits your hardware; Rust, GGUF/MLX support
- [airllm](https://github.com/lyogavin/airllm) — run 70B LLMs on a single 4GB GPU via layer-by-layer streaming; no quantization required
- [free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) — curated and updated list of free LLM inference endpoints accessible via API
- [mike](https://github.com/willchen96/mike) — open source AI legal platform; TypeScript + AGPL-3.0
- [unsloth](https://github.com/unslothai/unsloth) *(also in Claude)* — 65K-star fine-tuning acceleration for local open models (Gemma 4, Qwen3, DeepSeek); web UI included
- [GodMode](https://github.com/smol-ai/GodMode) — side-by-side ChatGPT/Claude/Bard/Bing in one Electron window; I use this as a quick comparison tool
- [jarvis (ethanplusai)](https://github.com/ethanplusai/jarvis) — voice-first AI assistant for macOS inspired by MCU; Claude + Three.js + Whisper
- [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) — free 10-week course: build AI Q&A systems over a knowledge base; RAG end-to-end

---

## Building (7)

Tools and starters for actually building things.

- [pocketbase](https://github.com/pocketbase/pocketbase) — 58K-star open source realtime backend in one Go binary: auth, SQLite DB, file storage, realtime subscriptions
- [n8n-workflows](https://github.com/Zie619/n8n-workflows) — 5K+ n8n automation workflow templates scraped from the official community site
- [public-apis](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category; first stop when a project needs external data
- [tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) — MCP server connecting Claude Code to TradingView Desktop for AI-assisted chart analysis
- [react-three-fiber](https://github.com/pmndrs/react-three-fiber) — 30K-star React renderer for Three.js; declarative 3D in React with full Three.js access
- [semantic-search-nextjs-pinecone-langchain-chatgpt](https://github.com/dabit3/semantic-search-nextjs-pinecone-langchain-chatgpt) — starter: embed text → Pinecone, semantic search with GPT3 + LangChain in Next.js UI
- [ai-weekend-builds](https://github.com/kju4q/ai-weekend-builds) — weekend AI project starters using Anthropic API; Python/Node with READMEs and starter code

---

## Projects (11)

Project ideas, inspiration, and curated learning resources.

- [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) — 506K-star: master programming by recreating technologies from scratch (DB, OS, browser, shell, etc.)
- [project-based-learning](https://github.com/practical-tutorials/project-based-learning) — 266K-star curated tutorials for building real projects in every major language
- [app-ideas](https://github.com/florinpop17/app-ideas) — 94K-star app ideas organized by difficulty: Newbie / Intermediate / Advanced tiers with specs
- [500-AI-ML-projects](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) — 500 AI/ML/CV/NLP project ideas with code; organized by domain
- [free-programming-books](https://github.com/EbookFoundation/free-programming-books) — 389K-star index of freely available programming books in all languages; CC-BY-4.0
- [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) — 445K-star open-source curriculum: math, CS, data structures, ML; full certifications available free
- [projectlearn-project-based-learning](https://github.com/Xtremilicious/projectlearn-project-based-learning) — web app frontend for browsing project tutorials by technology and category
- [hermes-desktop-os1](https://github.com/nickvasilescu/hermes-desktop-os1) — native macOS workspace for Hermes Agent on Orgo cloud computers and SSH hosts; Swift
- [ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) — free course: use AI dev tools (MCP, Claude Code, agents) to write better code faster
- [agentscope](https://github.com/agentscope-ai/agentscope) *(also in AI)* — good reference for multi-agent architecture patterns and real-world agent deployment
- [semantic-search-nextjs-pinecone-langchain-chatgpt](https://github.com/dabit3/semantic-search-nextjs-pinecone-langchain-chatgpt) *(also in Building)* — reference implementation for RAG over docs in a Next.js app

---

## Jobs (6)

Internship lists, interview prep, and job search resources.

- [Summer2026-Internships](https://github.com/SimplifyJobs/Summer2026-Internships) — 44K-star: daily-updated SWE/DS/AI/quant internship postings for Summer 2026; maintained by Simplify + Pitt CSC
- [underclassmen-internships](https://github.com/zapplyjobs/underclassmen-internships) — curated list of internships/fellowships exclusive to CS freshmen and sophomores (updated for 2026)
- [leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) — company-wise LeetCode questions as of May 2026; Java solutions
- [interview-company-wise-problems](https://github.com/liquidslr/interview-company-wise-problems) — CSV files of company-tagged LeetCode questions; updated June 2025; Google/Amazon/Meta focus
- [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) — 139K-star curated coding interview prep: algorithms, behavioral, system design, negotiation
- [coding-interview-university](https://github.com/jwasham/coding-interview-university) — 347K-star complete CS study plan for SWE roles: data structures, algorithms, system design, OS

---

## Learning (14)

Courses, zoomcamps, and structured learning paths.

- [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) — 41K-star free 9-week course: Docker, Kafka, Spark, dbt, Kestra, production data pipelines
- [machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) — 13K-star free 4-month ML engineering course: deployment, Docker, Kubernetes, FastAPI
- [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — 14K-star free MLOps course: tracking, deployment, monitoring, workflow orchestration
- [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) *(also in AI)* — free 10-week course: RAG, vector search, LLM evaluation, monitoring
- [ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) *(also in Projects)* — free course: use Claude Code, MCP, and coding agents effectively
- [applied-ml](https://github.com/eugeneyan/applied-ml) *(also in AI)* — production ML papers and blogs; best reference for seeing how real companies do ML
- [system-design-primer](https://github.com/donnemartin/system-design-primer) — 350K-star: learn how to design large-scale systems; interview prep + Anki flashcards
- [project-based-learning](https://github.com/practical-tutorials/project-based-learning) *(also in Projects)* — learn by building; organized by language
- [free-programming-books](https://github.com/EbookFoundation/free-programming-books) *(also in Projects)* — canonical free books index
- [500-AI-ML-projects](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) *(also in Projects)* — use as a project roadmap for ML learning
- [app-ideas](https://github.com/florinpop17/app-ideas) *(also in Projects)* — use difficulty tiers as a skill progression map
- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) *(also in AI)* — notebook-first tutorials on LLMs and agents; good for filling knowledge gaps
- [get-shit-done](https://github.com/gsd-build/get-shit-done) — 63K-star meta-prompting + context engineering + spec-driven system for Claude Code; by TÂCHES
- [agency-agents](https://github.com/msitarzewski/agency-agents) *(also in Claude)* — 105K-star: study these agent definitions to understand how to write good sub-agent personas

---

## Cybersecurity (2)

Security tooling and research.

- [bumblebee](https://github.com/perplexityai/bumblebee) — read-only developer endpoint scanner from Perplexity: checks on-disk packages/extensions for known supply-chain compromises; Go
- [keyhacks](https://github.com/streaak/keyhacks) — quick ways to verify if leaked API keys from bug bounty programs are valid; reference for bug bounty + key auditing
- [cai](https://github.com/aliasrobotics/cai) — Cybersecurity AI framework: AI-powered pentesting and security research; Python + multi-agent; from Alias Robotics
- [promptfoo](https://github.com/promptfoo/promptfoo) *(also in AI)* — red teaming and vulnerability scanning specifically for LLM/agent systems; used by Anthropic

---

## See Also

- [[40_Resources/CS/Links]] — general CS links
- [[40_Resources/CS/AI/]] — AI-specific concept notes
- `60_Claude/30_Source_Summaries/Github Ingestion/` — individual repo deep-dives
