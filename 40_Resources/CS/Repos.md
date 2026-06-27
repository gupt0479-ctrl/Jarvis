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
Organized by GitHub list. Each section mirrors the star list on [gupta-builds's profile](https://github.com/gupta-builds?tab=stars).
## Claude (28)

Claude Code tooling, memory systems, agent infrastructure. All entries have individual notes.
### MCPs

### Skills, Agents, Hooks & Scripts

### Context, Prompts and Templates

### Others


- [[ECC|ECC]] — agent harness for Claude Code: skills, instincts, persistent memory, and a security layer in a single install
- [[gstack|gstack]] — 13 cognitive-mode skills (founder review, eng review, paranoid QA) plus a Playwright browser for Claude Code (*GOOD*)
- [[mattpocock-skills|Skills (mattpocock)]] — 18 skills targeting the four main agent failure modes: misalignment, verbosity, broken feedback loops, entropy. (*EXTREMELY USEFUL - Copy skills*)
- [[agent-skills-addyosmani|Agent Skills (Addy Osmani)]] — 23 skills covering the full SDLC, each with rationalizations tables and evidence requirements. (*NEEDS TO MIMICKED*)
- [[obsidian-mind|Obsidian Mind]] — Obsidian vault template built for agents: 5 lifecycle hooks, 18 slash commands, 9 subagents, QMD semantic search. (*WORKFLOW NEEDS GO BE STUDIED AND MIMICKED*)
- [[cpr-compress-preserve-resume|CPR — Compress, Preserve, Resume]] — three slash commands (/preserve, /compress, /resume) for session lifecycle and ~55% token cost reduction on restart
- [[memsearch|memsearch (Zilliz)]] — auto-captures every Claude Code session to markdown, indexes with ONNX embeddings + Milvus, exposes /memory-recall (*Better option? HOW REALISTIC TO USE?*)
- [[context-sync|Context Sync]] — local SQLite MCP memory layer with `remember`/`recall` tools and git coupling analysis
- [[claude-context|Claude Context (Zilliz)]] — MCP server that indexes a codebase into Milvus for semantic code search; claims ~40% token reduction. (*WORTH USING? OVER USE OF CONTEXT?*)
- [[graphify|Graphify]] — Claude Code skill that builds a NetworkX knowledge graph from any folder and exports an Obsidian vault (*USING, UNDERSTAND BETTER*)
- [[spec-kit|Spec Kit (GitHub)]] — GitHub's spec-driven development CLI: constitution → specify → clarify → plan → tasks → implement. (*WORTH TRYING?*) Sounds like kiro
- [[beads|Beads (bd)]] — Dolt-backed CLI issue tracker with atomic task claiming and dependency graphs for multi-agent coordination (*HOW DIFFERENT FROM GRAPHIFY?* **USEFUL?**)
- [[claude-code-templates|Claude Code Templates]] — npm CLI to browse and install 100+ Claude Code agents, MCPs, hooks, and skills interactively (*IS IT USEFUL?*) - [Website](https://aitmpl.com/)
- [[ruflo|Ruflo (formerly claude-flow)]] — multi-agent orchestration with Q-Learning routing, 60+ specialized agents, and swarm coordination (*HOW TO USE? USEFUL*)
- [[awesome-mcp-servers|Awesome MCP Servers]] — canonical community index of MCP servers by category; check before building any new integration from scratch. (*NEEDS TO BE USED*)
- [[claude-code-best-practice|Claude Code Best Practice]] — 55K-star best practices collection with agents/commands/skills; reference read, not infrastructure *REALLY GOOD*
- [[system-prompts-and-models-of-ai-tools|system-prompts-and-models-of-ai-tools]] — extracted system prompts from Claude Code, Cursor, Devin, Manus, Replit; useful for CLAUDE.md and skill writing
- [[anthropics-financial-services|Claude for Financial Services (Anthropic)]] — official IB/equity research/KYC agents with Bloomberg, FactSet, S&P Global MCP connectors
- [[free-claude-code|Free Claude Code]] — proxy server that reroutes Claude Code API calls to NVIDIA NIM, OpenRouter, or local models
- [[dify|Dify]] — self-hosted LLM app platform for teams building products; full Docker deployment, not solo agentic tooling (*USEFUL?*)
- [[Scrapegraph-ai|ScrapeGraph AI]] — LLM-powered web scraping via natural language description; no Claude integration path
- [[Scrapling|Scrapling]] — resilient Python scraper that tracks elements across DOM changes; useful data pipeline utility. (*BEST SCRAPPER? COMPLICATED*) - alternative? or worth learning?
- [[unsloth|Unsloth]] — fine-tuning acceleration for local open models; orthogonal to Claude Code stack but useful for ML pipeline work. (*GOOD BUT FOR WHAT?* for my local models?) - moved to ai group starred. 
- [[jcode|jcode]] — Rust coding agent harness with 6,660 stars; can't evaluate (README empty at time of review) - Complex but claims to be extremely better than claude code. Does this run for local models? Useful with airllm?
- [[yt-dlp|yt-dlp]] — feature-rich CLI audio/video downloader for 1,800+ sites; useful utility. For youtube videos? What for? (*USEFUL?*)
- [[agency-agents|Agency Agents (msitarzewski)]] — 105K-star complete AI agency in your .claude: frontend wizard, Reddit ninja, whimsy injector, reality checker
- [Financial Services](https://github.com/anthropics/financial-services) - Useful for tradingview? how exactly better than the other resoruces?
- [Trading view mcp](https://github.com/tradesdontlie/tradingview-mcp) & [polymarket mcp](https://github.com/caiovicentino/polymarket-mcp-server) - Worth installing? for the tradingview product?
	- 45-tool MCP for claude desktop via polymarket's CLOB API. setup (~10 min):
		1. git clone the repo
		2. cd polymarket-mcp-server && ./quickstart.sh
		3. start in DEMO mode (no wallet, read-only)
		4. full mode needs a polygon wallet and is not available to US persons under polymarket's ToS
	- demo .env: `MAX_ORDER_SIZE_USD=50`, `MAX_TOTAL_EXPOSURE_USD=200`, `REQUIRE_CONFIRMATION_ABOVE_USD=25`
	- heads up: v0.1.0 experimental. engineering 
	- demo only - stay in demo if you're in the US. not financial advice, not legal advice.
- [Andrej karpathy skills](https://github.com/multica-ai/andrej-karpathy-skills) - extremely useful, needs to be mimicked. 
	- one curl command installs the file: `curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md`
	- drop it in your project root and claude code reads it automatically at every session start. 4 principles: don't assume (surface tradeoffs), keep it simple, surgical changes only, goal-driven execution
	- setup (2 min):
		1. git clone or just run the curl above
		2. drop CLAUDE.md in your project root
		3. open claude code in that directory - it reads it automatically
		4. for global use: add to your home directory
	- the thing to get right: add project-specific rules below the karpathy principles - the file is designed to be merged with your own conventions
	- heads up: clean tool, no controversies. only install from the official repos to avoid malicious forks.
- [Auto research](https://github.com/karpathy/autoresearch) - by karpathy needs to be used. Unless there is something better above
- [last30 day](https://github.com/mvanhorn/last30days-skill) - Searches search engine for the latest information
- [gbrain](https://github.com/garrytan/gbrain) - research and implement a better form for my second brain. 
- [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) - Best resource for making the most out of guard railed models. 
- [Agency agents](https://github.com/msitarzewski/agency-agents) - Really useful. how to use? why?
- 
---

## AI (27)

AI agents, frameworks, models, and LLM tooling.

- [hermes-agent](https://github.com/NousResearch/hermes-agent) — 171K-star Nous Research coding agent with ACP/MCP/Claude Code support; the most-starred agent on GitHub right now. (How to use? New to hermes and need an entire setup guide)
- [opencode](https://github.com/anomalyco/opencode) — 166K-star open source coding agent; terminal-first, multi-model, actively developed alternative to Claude Code. (HOW Useful if i hit claude limits? How useful with local models?)
- [browser-use](https://github.com/browser-use/browser-use) — 96K-star Python library making websites accessible for AI agents via Playwright; the standard for browser automation. (*USEFUL, how much?*)
- [[goose (github)|goose]] — 50K-star open source extensible AI agent (Rust); install/execute/edit/test with any LLM; ACP + MCP native; moved from `block/goose` to the Linux Foundation's Agentic AI Foundation. (*Confused to what exactly is this useful for? is this exactly like claude app?*)
- [PageIndex](https://github.com/VectifyAI/PageIndex) — 32K-star vectorless reasoning-based RAG (no embeddings); document index using LLM reasoning chains
- [multica](https://github.com/multica-ai/multica) — 34K-star open-source managed agents platform: assign tasks, track progress, compound skills; TypeScript. (Useful to distribute tasks? How many agents can be realisticly used for my uses?)
- [MiroFish](https://github.com/666ghj/MiroFish) — 63K-star swarm intelligence engine for prediction; financial forecasting + social prediction + knowledge graphs; Python. Very useful but how can I use it for my cases? Can be useful for prediction markets and stocks in tradingview?
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents; [paper](https://arxiv.org/pdf/2412.20138)
- [openhuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL; tinyhumans.ai. Honestly find it better than jan because it has the obsidian like memory system. Is this going to be my personal assistant now? Compare it to all other resources for assistants,
- [agentscope](https://github.com/agentscope-ai/agentscope) — 25K-star build and run agents you can see and trust; MCP-native, multi-modal, multi-agent; Alibaba-backed. (*USEFUL?*)
- [[promptfoo (github)|promptfoo]] — test prompts, agents, RAGs; red teaming + vulnerability scanning; used by OpenAI and Anthropic internally; now part of OpenAI (still MIT-licensed, open source)
- [jan](https://github.com/janhq/jan) — 42K-star fully offline ChatGPT alternative; runs 100% locally on your hardware; Tauri + LlamaCPP
- [dify](https://github.com/langgenius/dify) *(also in Claude)* — 143K-star production-ready agentic workflow platform; Docker deployment; team-scale LLM app builder
- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) — 35K-star in-depth tutorials on LLMs, RAGs, real-world agents (Jupyter notebooks); Daily Dose of DS
- [applied-ml](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan. (*GOLD*)
- [Kronos](https://github.com/shiyu-coder/Kronos) — 27K-star foundation model for financial markets language; time series + NLP; Python. (Tradingview: Going to be used but is there anything better out there yet?)
- [ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) — GAIR-NLP research on ASI-level task evolution for training superhuman agents; Python. (Best for research? Anything better?)
- [dots.ocr](https://github.com/rednote-hilab/dots.ocr) — multilingual document layout parsing in a single VLM; from RedNote (Xiaohongshu) research. (Useful for reading pdfs and images? Especially inside jarvis? any better alternative?)
- [whichllm](https://github.com/Andyyyy64/whichllm) — CLI: find the local LLM that actually runs on your hardware; ranked by real benchmarks, not parameter count (Replaced by llmfit)
- [llmfit](https://github.com/AlexsJones/llmfit) — hundreds of models/providers, one command to find what fits your hardware; Rust, GGUF/MLX support
- [airllm](https://github.com/lyogavin/airllm) — run 70B LLMs on a single 4GB GPU via layer-by-layer streaming; no quantization required. (*USEFUL FOR RUNNING LOCAL MODELS?*)
- [free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) — curated and updated list of free LLM inference endpoints accessible via API
- [mike](https://github.com/willchen96/mike) — open source AI legal platform; TypeScript + AGPL-3.0. (*Anything better?*)
- [unsloth](https://github.com/unslothai/unsloth) *(also in Claude)* — 65K-star fine-tuning acceleration for local open models (Gemma 4, Qwen3, DeepSeek); web UI included
- [GodMode](https://github.com/smol-ai/GodMode) — side-by-side ChatGPT/Claude/Bard/Bing in one Electron window; I use this as a quick comparison tool
- [jarvis (ethanplusai)](https://github.com/ethanplusai/jarvis) — voice-first AI assistant for macOS inspired by MCU; Claude + Three.js + Whisper
- [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) — free 10-week course: build AI Q&A systems over a knowledge base; RAG end-to-end
- [gst-core](https://github.com/open-gsd/gsd-core): Very useful? but how exactly are we going to work with the other installations?
- 

---

## Building (7)

Tools and starters for actually building things.

- [[pocketbase (github)|pocketbase]] — 59K-star open source realtime backend in one Go binary: auth, SQLite DB, file storage, realtime subscriptions; pre-v1.0.0, no compat guarantee yet
- [[n8n-workflows (github)|n8n-workflows]] — 4,343+ n8n automation workflow templates scraped from the official community site; README's AI-BOM banner claims hardcoded keys found in this exact set — audit before importing
- [public-apis](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category; first stop when a project needs external data
- [[tradingview-mcp (github)|tradingview-mcp]] — MCP server connecting Claude Code to TradingView Desktop for AI-assisted chart analysis via Chrome DevTools Protocol; requires active TradingView subscription
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
- [[promptfoo (github)|promptfoo]] *(also in AI)* — red teaming and vulnerability scanning specifically for LLM/agent systems; used by Anthropic

---

## See Also

- [[40_Resources/CS/Links]] — general CS links
- [[40_Resources/CS/AI/]] — AI-specific concept notes
- `60_Claude/30_Source_Summaries/Github Ingestion/` — individual repo deep-dives
