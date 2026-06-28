---
type: evergreen
status: sprout
created: 2026-05-05
updated: 2026-06-27
tags:
  - evergreen
  - github
  - resources
notes: null
---
# GitHub Stars Index
Organized by GitHub list. Each section mirrors the star list on [gupta-builds's profile](https://github.com/gupta-builds?tab=stars).
## Claude (23)
Claude Code tooling, memory, agent infrastructure.
### Skills & Agents
- [ECC](https://github.com/affaan-m/ECC) — agent harness for Claude Code: skills, instincts, persistent memory, and a security layer in a single install (*FORK*)
- [gstack](https://github.com/garrytan/gstack) — 13 cognitive-mode skills (founder review, eng review, paranoid QA) plus a Playwright browser for Claude Code (*COPY*)
- [Skills (mattpocock)](https://github.com/mattpocock/skills) — 18 skills targeting the four main agent failure modes: misalignment, verbosity, broken feedback loops, entropy. (*COPY: GLOBALLY*)
- [Agent Skills (Addy Osmani)](https://github.com/addyosmani/agent-skills) — 23 skills covering the full SDLC, each with rationalizations tables and evidence requirements. (*COPY 1/2: BUILD OVER*)
- [Ruflo](https://github.com/ruvnet/ruflo) — multi-agent orchestration with Q-Learning routing, 60+ specialized agents, and swarm coordination (*COPY BUT HOW? SELF IMPROVING*)
- [Agency Agents](https://github.com/msitarzewski/agency-agents) — 105K-star complete AI agency in your .claude: frontend wizard, Reddit ninja, whimsy injector, reality checker - ==not written==
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) — CLAUDE.md drop-in with 4 Karpathy principles: don't assume, keep it simple, surgical changes, goal-driven. (*COPY: GLOBALLY*) - ==no detail written==
- [Claude Skills LLM Council](https://github.com/aiwithremy/claude-skills-llm-council) — [Original Karpathy Repo](https://github.com/karpathy/llm-council): skill that runs 5 expert advisors on a question and synthesizes a verdict. Use for hard decisions. Multiple resources listed in vault. (*COPY (CUSTOMIZE 1/2): GLOBALLY*)
- [Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill) — Claude Code skill that searches for information from the last 30 days. (*COPY GLOBALLY*) - ==no detail written==
### MCPs & CLI Tools
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) — canonical community index of MCP servers by category; check before building any new integration from scratch. (*NEEDS TO BE USED*)
- [Claude Code Templates](https://github.com/davila7/claude-code-templates) — npm CLI to browse and install 100+ Claude Code agents, MCPs, hooks, and skills interactively (*IS IT USEFUL?*) · [website](https://aitmpl.com/)
- [Spec Kit](https://github.com/github/spec-kit) — GitHub's spec-driven development CLI: constitution → specify → clarify → plan → tasks → implement. (*WORTH TRYING?*)
- [Beads](https://github.com/gastownhall/beads) — Dolt-backed CLI issue tracker with atomic task claiming and dependency graphs for multi-agent coordination (*HOW DIFFERENT FROM GRAPHIFY?* **USEFUL?**)
- [TradingView MCP](https://github.com/tradesdontlie/tradingview-mcp) — MCP server connecting Claude Code to TradingView Desktop for AI-assisted chart analysis via Chrome DevTools Protocol; requires active TradingView subscription
- [Polymarket MCP](https://github.com/caiovicentino/polymarket-mcp-server) — 45-tool MCP for Claude Desktop via Polymarket's CLOB API; demo mode read-only; full mode requires polygon wallet and unavailable to US persons under ToS. Worth installing? for the tradingview product?
- [Free Claude Code](https://github.com/Alishahryar1/free-claude-code) — proxy server that reroutes Claude Code API calls to NVIDIA NIM, OpenRouter, or local models

### Memory & Context

- [Graphify](https://github.com/safishamsi/graphify) — Claude Code skill that builds a NetworkX knowledge graph from any folder and exports an Obsidian vault (*USING, UNDERSTAND BETTER*)
- [Claude Context](https://github.com/zilliztech/claude-context) — MCP server that indexes a codebase into Milvus for semantic code search; claims ~40% token reduction. (*WORTH USING? OVER USE OF CONTEXT?*)
- [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) — Best resource for making the most out of guard railed models.

### Other

- [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) — 55K-star best practices collection with agents/commands/skills; reference read, not infrastructure *REALLY GOOD*
- [System Prompts Collection](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — extracted system prompts from Claude Code, Cursor, Devin, Manus, Replit; useful for CLAUDE.md and skill writing
- [Claude for Financial Services](https://github.com/anthropics/financial-services) — official IB/equity research/KYC agents with Bloomberg, FactSet, S&P Global MCP connectors. Useful for tradingview? how exactly better than the other resources?
- [Dify](https://github.com/langgenius/dify) — self-hosted LLM app platform for teams building products; full Docker deployment, not solo agentic tooling (*USEFUL?*)

---

## AI (33)

AI agents, frameworks, models, and LLM tooling.

### Agents & Frameworks

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — 171K-star Nous Research coding agent with ACP/MCP/Claude Code support; the most-starred agent on GitHub right now. (How to use? New to hermes and need an entire setup guide)
- [OpenCode](https://github.com/anomalyco/opencode) — 166K-star open source coding agent; terminal-first, multi-model, actively developed alternative to Claude Code. (HOW Useful if i hit claude limits? How useful with local models?)
- [Browser Use](https://github.com/browser-use/browser-use) — 96K-star Python library making websites accessible for AI agents via Playwright; the standard for browser automation. (*USEFUL, how much?*)
- [Goose](https://github.com/aaif-goose/goose) — 50K-star open source extensible AI agent (Rust); install/execute/edit/test with any LLM; ACP + MCP native; moved from block/goose to the Linux Foundation's Agentic AI Foundation. (*Confused to what exactly is this useful for? is this exactly like claude app?*)
- [Multica](https://github.com/multica-ai/multica) — 34K-star open-source managed agents platform: assign tasks, track progress, compound skills; TypeScript. (Useful to distribute tasks? How many agents can be realistically used for my uses?)
- [AgentScope](https://github.com/agentscope-ai/agentscope) — 25K-star build and run agents you can see and trust; MCP-native, multi-modal, multi-agent; Alibaba-backed. (*USEFUL?*)
- [Promptfoo](https://github.com/promptfoo/promptfoo) — test prompts, agents, RAGs; red teaming + vulnerability scanning; used by OpenAI and Anthropic internally; now part of OpenAI (still MIT-licensed, open source)
- [OpenHuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL; tinyhumans.ai. Honestly find it better than jan because it has the obsidian like memory system. Is this going to be my personal assistant now? Compare it to all other resources for assistants. *(also in: Projects)*
- [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus) — self-hosted AI workspace: chat, agents, deep research, documents, email, notes, calendar, local models; AGPL-3.0; Docker setup
- [Paperclip](https://github.com/paperclipai/paperclip) — multi-agent company orchestration: org charts, budgets, governance, task tracking for 20+ simultaneous agents; Node.js, self-hosted *not useful*
- [Hiring Agent](https://github.com/interviewstreet/hiring-agent) — AI agent for automated technical interview workflows from HackerRank *(also in: Jobs)*
- [MiroFish](https://github.com/666ghj/MiroFish) — 63K-star swarm intelligence engine for prediction; financial forecasting + social prediction + knowledge graphs; Python. Very useful but how can I use it for my cases? Can be useful for prediction markets and stocks in tradingview?

### Models & Hardware

- [Unsloth](https://github.com/unslothai/unsloth) — 65K-star fine-tuning acceleration for local open models (Gemma 4, Qwen3, DeepSeek); web UI included
- [AirLLM](https://github.com/lyogavin/airllm) — run 70B LLMs on a single 4GB GPU via layer-by-layer streaming; no quantization required. (*USEFUL FOR RUNNING LOCAL MODELS?*)
- [llmfit](https://github.com/AlexsJones/llmfit) — hundreds of models/providers, one command to find what fits your hardware; Rust, GGUF/MLX support
- [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources) — curated and updated list of free LLM inference endpoints accessible via API

### Other

- [Applied ML](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan. (*GOLD*) *(also in: Projects)*
- [ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) — GAIR-NLP research on ASI-level task evolution for training superhuman agents; Python. (Best for research? Anything better?)
- [dots.ocr](https://github.com/rednote-hilab/dots.ocr) — multilingual document layout parsing in a single VLM; from RedNote (Xiaohongshu) research. (Useful for reading pdfs and images? Especially inside jarvis? any better alternative?)
- [Mike](https://github.com/willchen96/mike) — open source AI legal platform; TypeScript + AGPL-3.0. (*Anything better?*) *not useful*
- [GSD Core](https://github.com/open-gsd/gsd-core) — meta-prompting + context engineering system for Claude Code. Very useful? but how exactly are we going to work with the other installations?
- [Autoresearch](https://github.com/karpathy/autoresearch) — Karpathy's automated research agent; by karpathy needs to be used. Unless there is something better above *(also in: Building)*
- [LLM Council](https://github.com/karpathy/llm-council) — Karpathy's research: ensemble multiple LLM judges for evaluation; Python
- [Obsidian Mind](https://github.com/breferrari/obsidian-mind) — Obsidian vault template built for agents: 5 lifecycle hooks, 18 slash commands, 9 subagents, QMD semantic search. (*WORKFLOW NEEDS TO BE STUDIED AND MIMICKED*)
- [memsearch](https://github.com/zilliztech/memsearch) — auto-captures every Claude Code session to markdown, indexes with ONNX embeddings + Milvus, exposes /memory-recall (*Better option? HOW REALISTIC TO USE?*)
- [GBrain](https://github.com/garrytan/gbrain) — research and implement a better form for my second brain.
- [ScrapeGraph AI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — LLM-powered web scraping via natural language description; no Claude integration path
- [Scrapling](https://github.com/D4Vinci/Scrapling) — resilient Python scraper that tracks elements across DOM changes (*BEST SCRAPPER? COMPLICATED*) — alternative? or worth learning?
- [jcode](https://github.com/1jehuang/jcode) — Rust coding agent harness; claims to be extremely better than Claude Code. Does this run for local models? Useful with airllm?
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — feature-rich CLI audio/video downloader for 1,800+ sites; useful utility. For youtube videos? What for? (*USEFUL?*)
- [Public APIs](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category; first stop when a project needs external data *(also in: Projects)*
- [Firecrawl](https://github.com/firecrawl/firecrawl) — open-source web scraping and crawling platform; REST API, Python/JS SDKs, LLM-ready markdown output
- [Crawl4AI](https://github.com/unclecode/crawl4ai) — open-source async Python web crawler optimized for LLM extraction; structured output, session handling

---

## Fullstack (4)

Web development and fullstack tools.

- [React Three Fiber](https://github.com/pmndrs/react-three-fiber) — 30K-star React renderer for Three.js; declarative 3D in React with full Three.js access *not useful*
- [Pocketbase](https://github.com/pocketbase/pocketbase) — 59K-star open source realtime backend in one Go binary: auth, SQLite DB, file storage, realtime subscriptions; pre-v1.0.0, no compat guarantee yet
- [Bumblebee](https://github.com/perplexityai/bumblebee) — read-only developer endpoint scanner from Perplexity: checks on-disk packages/extensions for known supply-chain compromises; Go
- [Modern JS Cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet) — comprehensive modern JavaScript reference; ES6+ concepts with examples *not useful*

---

## Building (10)

Tools and starters for actually building things.

- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents; [paper](https://arxiv.org/pdf/2412.20138) *(also in: Projects)*
- [OpenBB](https://github.com/OpenBB-finance/OpenBB) — open-source financial data platform; stocks, crypto, macro data; Python; programmatic Bloomberg terminal alternative
- [Kronos](https://github.com/shiyu-coder/Kronos) — 27K-star foundation model for financial markets language; time series + NLP; Python. (Tradingview: Going to be used but is there anything better out there yet?)
- [Jan](https://github.com/janhq/jan) — 42K-star fully offline ChatGPT alternative; runs 100% locally; Tauri + LlamaCPP
- [PageIndex](https://github.com/VectifyAI/PageIndex) — 32K-star vectorless reasoning-based RAG (no embeddings); document index using LLM reasoning chains
- [Obsidian Dashboard](https://github.com/handrovermeulen/Obsidian-Dashboard) — community Obsidian vault dashboard template with statistics and navigation
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus) — (to be evaluated)
- [Pretext](https://github.com/chenglou/pretext) — (to be evaluated) *not useful*
- [Autoresearch](https://github.com/karpathy/autoresearch) — Karpathy's automated research agent *(also in: AI)*
- [Ghostty Blackhole](https://github.com/s0xDk/ghostty-blackhole) — Ghostty terminal emulator configuration and theme collection *not useful*

---

## Jobs (7)

Internship lists, interview prep, and job search resources.

- [Summer 2026 Internships](https://github.com/SimplifyJobs/Summer2026-Internships) — 44K-star: daily-updated SWE/DS/AI/quant internship postings for Summer 2026; maintained by Simplify + Pitt CSC
- [Underclassmen Internships](https://github.com/zapplyjobs/underclassmen-internships) — curated list of internships/fellowships exclusive to CS freshmen and sophomores (updated for 2026)
- [Interview Company-wise Problems](https://github.com/liquidslr/interview-company-wise-problems) — CSV files of company-tagged LeetCode questions; updated June 2025; Google/Amazon/Meta focus
- [Tech Interview Handbook](https://github.com/yangshun/tech-interview-handbook) — 139K-star curated coding interview prep: algorithms, behavioral, system design, negotiation
- [Coding Interview University](https://github.com/jwasham/coding-interview-university) — 347K-star complete CS study plan for SWE roles: data structures, algorithms, system design, OS
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — 350K-star: learn how to design large-scale systems; interview prep + Anki flashcards *(also in: Learning)*
- [Hiring Agent](https://github.com/interviewstreet/hiring-agent) — AI agent for automated technical interview workflows from HackerRank *(also in: AI)*

---

## Learning (15)

Courses, zoomcamps, and structured learning paths.

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) — 41K-star free 9-week course: Docker, Kafka, Spark, dbt, Kestra, production data pipelines
- [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) — 13K-star free 4-month ML engineering course: deployment, Docker, Kubernetes, FastAPI
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — 14K-star free MLOps course: tracking, deployment, monitoring, workflow orchestration
- [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) — free 10-week course: RAG, vector search, LLM evaluation, monitoring
- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) — free course: use Claude Code, MCP, and coding agents effectively
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — 350K-star: learn how to design large-scale systems; interview prep + Anki flashcards *(also in: Jobs)*
- [Project Based Learning](https://github.com/practical-tutorials/project-based-learning) — 266K-star curated tutorials for building real projects in every major language
- [ProjectLearn](https://github.com/Xtremilicious/projectlearn-project-based-learning) — web app frontend for browsing project tutorials by technology and category *not useful*
- [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) — 445K-star open-source curriculum: math, CS, data structures, ML; full certifications available free
- [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) — 389K-star index of freely available programming books in all languages; CC-BY-4.0 *not useful*
- [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) — 35K-star in-depth tutorials on LLMs, RAGs, real-world agents (Jupyter notebooks); Daily Dose of DS
- [LeetCode Company-wise](https://github.com/snehasishroy/leetcode-companywise-interview-questions) — company-wise LeetCode questions as of May 2026; Java solutions
- [Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) — Anthropic's official interactive prompt engineering course; hands-on exercises with solutions
- [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) — community-driven learning roadmaps organized by technology track *(also in: Projects)*
- [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — end-to-end AI engineering curriculum from foundations to production deployment *(also in: Projects)*

---

## Projects (15)

Project ideas, inspiration, and curated resources.

- [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x) — 506K-star: master programming by recreating technologies from scratch (DB, OS, browser, shell, etc.)
- [App Ideas](https://github.com/florinpop17/app-ideas) — 94K-star app ideas organized by difficulty: Newbie / Intermediate / Advanced tiers with specs
- [500 AI/ML Projects](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) — 500 AI/ML/CV/NLP project ideas with code; organized by domain
- [Semantic Search Starter](https://github.com/dabit3/semantic-search-nextjs-pinecone-langchain-chatgpt) — embed text → Pinecone, semantic search with GPT3 + LangChain in Next.js UI *not useful*
- [Jarvis](https://github.com/ethanplusai/jarvis) — voice-first AI assistant for macOS inspired by MCU; Claude + Three.js + Whisper *not useful*
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents *(also in: Building)*
- [AI Weekend Builds](https://github.com/kju4q/ai-weekend-builds) — weekend AI project starters using Anthropic API; Python/Node with READMEs and starter code
- [OpenHuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL *(also in: AI)*
- [Applied ML](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan. (*GOLD*) *(also in: AI)*
- [Public APIs](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category *(also in: AI)*
- [DevOps Projects](https://github.com/NotHarshhaa/DevOps-Projects) — 50+ real-world DevOps projects with solutions across AWS, Docker, Kubernetes, Jenkins
- [DevOps Projects (techiescamp)](https://github.com/techiescamp/devops-projects) — beginner-to-advanced DevOps project tutorials with step-by-step guides
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — curated collection of LLM app examples with Agno, OpenAI, Anthropic, Gemini; use as inspiration for project ideas
- [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — end-to-end AI engineering curriculum *(also in: Learning)*
- [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) — community-driven learning roadmaps organized by technology track *(also in: Learning)*

---

## Cybersecurity (4)

Security tooling and research.

- [CAI](https://github.com/aliasrobotics/cai) — Cybersecurity AI framework: AI-powered pentesting and security research; Python + multi-agent; from Alias Robotics
- [KeyHacks](https://github.com/streaak/keyhacks) — quick ways to verify if leaked API keys from bug bounty programs are valid; reference for bug bounty + key auditing
- [PentestGPT](https://github.com/GreyDGL/PentestGPT) — LLM-powered penetration testing assistant: knowledge reasoning + guided penetration testing workflow
- [MantisHack](https://github.com/deonmenezes/mantishack) — autonomous security framework on Claude Code (fork of RAPTOR): scan, validate, exploit, patch via slash commands (/mantis-agentic, /mantis-scan, /mantis-auth-audit, etc.)

---

## See Also

- [[40_Resources/CS/Links]] — general CS links
- [[40_Resources/CS/AI/]] — AI-specific concept notes
- `60_Claude/10_Source_Summaries/Github Ingestion/` — individual repo deep-dives
