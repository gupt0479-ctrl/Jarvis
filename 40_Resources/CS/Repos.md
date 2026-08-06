---
type: evergreen
status: sprout
created: 2026-05-05
updated: 2026-07-29
tags:
  - evergreen
  - github
  - resources
notes: null
---
# GitHub Stars Index
Organized by GitHub list. Each section mirrors the star list on [gupta-builds's profile](https://github.com/gupta-builds?tab=stars).
==**Implement > Knowledge (2026-07-29):** install only what closes a named gap or unlocks a blocked project; reference everything else via the Awesome-index repos before building from scratch; test in one session before committing.== Source: [[PDF's Ingestion Implementation#Claude Code Skills & Repos: Implement vs. Knowledge Matrix - REVIEW|Claude Code Skills & Repos Matrix]], confirmed by [[00_Execution]]'s GitHub pass — neither this doc's annotations nor the companion [[How Anant Uses Each Repo]] had actually been executed three weeks after being written. Markers below now record real decisions (`(*INSTALL: QUEUED*)`, `(*SKIP*)`, `(*EVAL: DATE*)`, `(*DEFERRED*)`) instead of open questions — "QUEUED" means decided but not yet run, not installed. Full per-repo reasoning: [[00_Execution#Github|00_Execution § Github]].
Every repo below now also carries a `→` marker to its individual deep-dive note in `60_Claude/10_Source_Summaries/Github Ingestion/` where one exists, or `→ no relations` where the repo was starred but never individually ingested.
## Claude (23)
Claude Code tooling, memory, agent infrastructure.
### Skills & Agents
- [ECC](https://github.com/affaan-m/ECC) — agent harness for Claude Code: skills, instincts, persistent memory, and a security layer in a single install (*RE-CORRECTED: 2026-07-30 — the 2026-07-29 "unrelated Rust project" call on `ecc2` was itself wrong: `git remote -v` confirms `ecc2` is `affaan-m/everything-claude-code`'s own in-tree ECC 2.0 Rust control-plane scaffold (`git ls-files` confirms it's tracked, not a stray clone), not an unrelated repo. Real testing has now happened: cloned into `second-brain-claudekit/sandbox/ecc/`, `npm install` clean (210 packages), full test suite run — 3378/3388 passing (99.7%), 10 failures isolated to the experimental Plan Canvas feature (environment-specific `ETIMEDOUT`, likely this sandbox's networking, not a confirmed ECC bug) and one dry-run edge case. Catalog is large (67 agents/281 skills/94 commands) — per Implement > Knowledge, still deciding which specific named gap(s) it closes rather than installing wholesale; cross-harness-portability angle evaluated 2026-07-30, see [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]*) → [[ECC]]
- [gstack](https://github.com/garrytan/gstack) — 13 cognitive-mode skills (founder review, eng review, paranoid QA) plus a Playwright browser for Claude Code (*BLOCKED: 2026-07-29 — cloned + `./setup` run for real in `second-brain-claudekit/sandbox`; now 55 skills (~893K tokens), compiled fine, but fails at Chromium launch (missing WSL system libs, needs interactive `sudo apt install`); nothing registered yet — see [[Claude Kit Implementation]]*) → [[gstack]]
- [Skills (mattpocock)](https://github.com/mattpocock/skills) — 18 skills targeting the four main agent failure modes: misalignment, verbosity, broken feedback loops, entropy. (*PARTIAL: 2026-07-29 — now 41 skills; `engineering/` category (17 skills) copied into `second-brain-claudekit/tested-skills/` for review, not yet promoted to global — see [[Claude Kit Implementation]]*) → [[mattpocock-skills]]
- [Agent Skills (Addy Osmani)](https://github.com/addyosmani/agent-skills) — 23 skills covering the full SDLC, each with rationalizations tables and evidence requirements. (*COPY 1/2: BUILD OVER*) → [[agent-skills-addyosmani]]
- [Ruflo](https://github.com/ruvnet/ruflo) — multi-agent orchestration with Q-Learning routing, 60+ specialized agents, and swarm coordination (*DEFERRED: 2026-07-29 — Claude Code's native subagent tooling + ECC 2.0's worktree-lifecycle service cover the real near-term need; revisit once true concurrent-agent work exists*) → [[ruflo]]
- [Agency Agents](https://github.com/msitarzewski/agency-agents) — 105K-star complete AI agency in your .claude: frontend wizard, Reddit ninja, whimsy injector, reality checker - ==not written== → [[agency-agents]]
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) — CLAUDE.md drop-in with 4 Karpathy principles: don't assume, keep it simple, surgical changes, goal-driven. (*COPY: GLOBALLY*) - ==no detail written== → [[andrej-karpathy-skills]]
- [Claude Skills LLM Council](https://github.com/aiwithremy/claude-skills-llm-council) — [Original Karpathy Repo](https://github.com/karpathy/llm-council): skill that runs 5 expert advisors on a question and synthesizes a verdict. Use for hard decisions. Multiple resources listed in vault. (*BUILT: 2026-07-29 — installed as `.claude/skills/llm-council.md`, see [[Claude Council (LLM Council Skill Install)]]*) → [[LLM Council skills]], [[Claude Council (LLM Council Skill Install)]]
- [Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill) — Claude Code skill that searches for information from the last 30 days. (*COPY: QUEUED — recency-biased search across Reddit/X/YouTube/HN/Polymarket in one pass, install for the trading research workflow*) → [[last30days-skill]]
### MCPs & CLI Tools
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) — canonical community index of MCP servers by category; check before building any new integration from scratch. (*MATERIAL*) → [[awesome-mcp-servers]]
- [Claude Code Templates](https://github.com/davila7/claude-code-templates) — npm CLI to browse and install 100+ Claude Code agents, MCPs, hooks, and skills interactively (*not useful*) · [website](https://aitmpl.com/) → [[claude-code-templates]]
- [Spec Kit](https://github.com/github/spec-kit) — GitHub's spec-driven development CLI: constitution → specify → clarify → plan → tasks → implement. (*INSTALL: GLOBALLY — QUEUED, Tier-1, agreed across both master triage docs, still not run as of 2026-07-29*) → [[spec-kit]]
- [Beads](https://github.com/gastownhall/beads) — Dolt-backed CLI issue tracker with atomic task claiming and dependency graphs for multi-agent coordination (*HOW DIFFERENT FROM GRAPHIFY?* **USEFUL?** - ==not sure==) → [[beads]]
- [TradingView MCP](https://github.com/tradesdontlie/tradingview-mcp) — MCP server connecting Claude Code to TradingView Desktop for AI-assisted chart analysis via Chrome DevTools Protocol; requires active TradingView subscription (*INSTALL: free TradingView Desktop tier, not paid subscription — confirmed 2026-07-29; duplicate ingestion file merge still pending, see [[How Anant Uses Each Repo]]*) → [[tradingview-mcp (github)]] (duplicate raw-clip file `tradingview-mcp - AI-assisted TradingView chart analysis` pending merge/delete)
- [Polymarket MCP](https://github.com/caiovicentino/polymarket-mcp-server) — 45-tool MCP for Claude Desktop via Polymarket's CLOB API; demo mode read-only; full mode requires polygon wallet and unavailable to US persons under ToS. (*REFERENCE ONLY: 2026-07-29 — demo-mode confirmed correctly scoped; use as the architecture reference for a read-only market-data MCP against TradingView's own providers, don't install live for actual trading*) → [[polymarket-mcp-server]]
- [Free Claude Code](https://github.com/Alishahryar1/free-claude-code) — proxy server that reroutes Claude Code API calls to NVIDIA NIM, OpenRouter, or local models (*NEED AN ON & OFF BUTTON* **OR** *AN ALTERNATIVE*) → [[free-claude-code]]
### Memory & Context
- [Graphify](https://github.com/safishamsi/graphify) — Claude Code skill that builds a NetworkX knowledge graph from any folder and exports an Obsidian vault (*USING, UNDERSTAND BETTER*) - ==detailed commands and usage needs to be written== → [[graphify]]
- [Claude Context](https://github.com/zilliztech/claude-context) — MCP server that indexes a codebase into Milvus for semantic code search; claims ~40% token reduction. (*INSTALL: QUEUED — BOOM project-scoped only, not global; complementary to Graphify (structure) not competing, real blocker is the Milvus/Docker dependency*) → [[claude-context]]
- [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) — Best resource for making the most out of guard railed models. - ==not written== → [[CL4R1T4S]]
### Other
- [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) — 55K-star best practices collection with agents/commands/skills; reference read, not infrastructure (*REALLY GOOD FOR LEARNING*) → [[claude-code-best-practice]]
- [System Prompts Collection](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — extracted system prompts from Claude Code, Cursor, Devin, Manus, Replit; useful for CLAUDE.md and skill writing (*MATERIAL*) → [[system-prompts-and-models-of-ai-tools]]
- [Claude for Financial Services](https://github.com/anthropics/financial-services) — official IB/equity research/KYC agents with Bloomberg, FactSet, S&P Global MCP connectors. Useful for tradingview? how exactly better than the other resources? (*INSTALL FOR TRADINGVIEW*) - ==no detail written== → [[anthropics-financial-services]]
- [Dify](https://github.com/langgenius/dify) — self-hosted LLM app platform for teams building products; full Docker deployment, not solo agentic tooling (*not useful*) - ==move to ai== → [[dify]]

---

## AI (33)

AI agents, frameworks, models, and LLM tooling.

### Agents & Frameworks

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — 171K-star Nous Research coding agent with ACP/MCP/Claude Code support; the most-starred agent on GitHub right now. (How to use? New to hermes and need an entire setup guide) → [[hermes-agent]] (this is the NousResearch coding-agent repo, not zachdoesai's "Hermes Agent" framework — see [[Hermes Agent Framework — Corrected Framing]] for that distinct, unrelated use of the same name)
- [OpenCode](https://github.com/anomalyco/opencode) — 166K-star open source coding agent; terminal-first, multi-model, actively developed alternative to Claude Code. (HOW Useful if i hit claude limits? How useful with local models?) → [[opencode]]
- [Browser Use](https://github.com/browser-use/browser-use) — 96K-star Python library making websites accessible for AI agents via Playwright; the standard for browser automation. (*USEFUL, how much?*) → [[browser-use]]
- [Goose](https://github.com/aaif-goose/goose) — 50K-star open source extensible AI agent (Rust); install/execute/edit/test with any LLM; ACP + MCP native; moved from block/goose to the Linux Foundation's Agentic AI Foundation. (*Confused to what exactly is this useful for? is this exactly like claude app?*) → [[goose (github)]]
- [Multica](https://github.com/multica-ai/multica) — 34K-star open-source managed agents platform: assign tasks, track progress, compound skills; TypeScript. (Useful to distribute tasks? How many agents can be realistically used for my uses?) → [[multica]]
- [AgentScope](https://github.com/agentscope-ai/agentscope) — 25K-star build and run agents you can see and trust; MCP-native, multi-modal, multi-agent; Alibaba-backed. (*USEFUL?*) → [[agentscope]]
- [Promptfoo](https://github.com/promptfoo/promptfoo) — test prompts, agents, RAGs; red teaming + vulnerability scanning; used by OpenAI and Anthropic internally; now part of OpenAI (still MIT-licensed, open source) → [[promptfoo (github)]], [[04 - Eval Harness — promptfoo]] (already the real eval gate for Orby, see [[10 - Orby Golden Eval Dataset (Grounding Cases)]])
- [OpenHuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL; tinyhumans.ai. Honestly find it better than jan because it has the obsidian like memory system. Is this going to be my personal assistant now? Compare it to all other resources for assistants. *(also in: Projects)* → [[openhuman]]
- [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus) — self-hosted AI workspace: chat, agents, deep research, documents, email, notes, calendar, local models; AGPL-3.0; Docker setup → [[odysseus]]
- [Paperclip](https://github.com/paperclipai/paperclip) — multi-agent company orchestration: org charts, budgets, governance, task tracking for 20+ simultaneous agents; Node.js, self-hosted *not useful* → no relations
- [Hiring Agent](https://github.com/interviewstreet/hiring-agent) — AI agent for automated technical interview workflows from HackerRank *(also in: Jobs)* → [[hiring-agent]]
- [MiroFish](https://github.com/666ghj/MiroFish) — 63K-star swarm intelligence engine for prediction; financial forecasting + social prediction + knowledge graphs; Python. Very useful but how can I use it for my cases? Can be useful for prediction markets and stocks in tradingview? → [[MiroFish]]

### Models & Hardware

- [Unsloth](https://github.com/unslothai/unsloth) — 65K-star fine-tuning acceleration for local open models (Gemma 4, Qwen3, DeepSeek); web UI included → [[unsloth]], [[Model Distillation]] (the Unsloth fine-tuning step in the deferred 70B→3B pipeline)
- [AirLLM](https://github.com/lyogavin/airllm) — run 70B LLMs on a single 4GB GPU via layer-by-layer streaming; no quantization required. (*USEFUL FOR RUNNING LOCAL MODELS?*) → [[airllm]]
- [llmfit](https://github.com/AlexsJones/llmfit) — hundreds of models/providers, one command to find what fits your hardware; Rust, GGUF/MLX support → [[llmfit]]
- [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources) — curated and updated list of free LLM inference endpoints accessible via API → [[free-llm-api-resources]]

### Other

- [Applied ML](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan. (*GOLD*) *(also in: Projects)* → [[applied-ml]]
- [ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) — GAIR-NLP research on ASI-level task evolution for training superhuman agents; Python. (Best for research? Anything better?) → [[ASI-Evolve]]
- [dots.ocr](https://github.com/rednote-hilab/dots.ocr) — multilingual document layout parsing in a single VLM; from RedNote (Xiaohongshu) research. (Useful for reading pdfs and images? Especially inside jarvis? any better alternative?) → [[dots.ocr]]
- [Mike](https://github.com/willchen96/mike) — open source AI legal platform; TypeScript + AGPL-3.0. (*Anything better?*) *not useful* → no relations
- [GSD Core](https://github.com/open-gsd/gsd-core) — meta-prompting + context engineering system for Claude Code. Very useful? but how exactly are we going to work with the other installations? → [[gsd-core]]
- [Autoresearch](https://github.com/karpathy/autoresearch) — Karpathy's automated research agent; by karpathy needs to be used. Unless there is something better above *(also in: Building)* → [[autoresearch]]
- [LLM Council](https://github.com/karpathy/llm-council) — Karpathy's research: ensemble multiple LLM judges for evaluation; Python → [[LLM Council skills]] (the Claude-skill adaptation of this original repo, now built as `.claude/skills/llm-council.md` — see [[Claude Council (LLM Council Skill Install)]])
- [Obsidian Mind](https://github.com/breferrari/obsidian-mind) — Obsidian vault template built for agents: 5 lifecycle hooks, 18 slash commands, 9 subagents, QMD semantic search. (*WORKFLOW NEEDS TO BE STUDIED AND MIMICKED*) → [[obsidian-mind]]
- [memsearch](https://github.com/zilliztech/memsearch) — auto-captures every Claude Code session to markdown, indexes with ONNX embeddings + Milvus, exposes /memory-recall (*SKIP: 2026-07-29 — superseded by GBrain, which duplicates the auto-capture without GBrain's synthesis layer*) → [[memsearch]]
- [GBrain](https://github.com/garrytan/gbrain) — personal-knowledge MCP with synthesis + gap-analysis (not just retrieval), benchmarked +31.4 points over vector-only RAG on a rich-prose corpus; PGLite, no Docker. (*INSTALLED + TESTED: 2026-07-29 — real `bun install` + `gbrain init --pglite --no-embedding` in `second-brain-claudekit/sandbox`; `doctor` reports 80/100 health, working PGLite brain; needs an embedding API key (Voyage/ZeroEntropy free tier or OpenAI paid) for full semantic search, not yet chosen; also makes context-sync unnecessary as a separate install — see [[Claude Kit Implementation]]*) → [[gbrain]]
- [ScrapeGraph AI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — LLM-powered web scraping via natural language description; no Claude integration path → [[Scrapegraph-ai]]
- [Scrapling](https://github.com/D4Vinci/Scrapling) — resilient Python scraper that tracks elements across DOM changes (*BEST SCRAPPER? COMPLICATED*) — alternative? or worth learning? → [[Scrapling]]
- [jcode](https://github.com/1jehuang/jcode) — Rust coding agent harness; claims to be extremely better than Claude Code. Does this run for local models? Useful with airllm? → [[jcode]]
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — feature-rich CLI audio/video downloader for 1,800+ sites; useful utility. For youtube videos? What for? (*USEFUL?*) → [[yt-dlp]]
- [Public APIs](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category; first stop when a project needs external data *(also in: Projects)* → [[public-apis]]
- [Firecrawl](https://github.com/firecrawl/firecrawl) — open-source web scraping and crawling platform; REST API, Python/JS SDKs, LLM-ready markdown output → no relations (already adopted and in daily use as an MCP server + skill suite, but never itself individually ingested as a repo summary)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) — open-source async Python web crawler optimized for LLM extraction; structured output, session handling → no relations

---

## Fullstack (4)

Web development and fullstack tools.

- [React Three Fiber](https://github.com/pmndrs/react-three-fiber) — 30K-star React renderer for Three.js; declarative 3D in React with full Three.js access *not useful* → no relations
- [Pocketbase](https://github.com/pocketbase/pocketbase) — 59K-star open source realtime backend in one Go binary: auth, SQLite DB, file storage, realtime subscriptions; pre-v1.0.0, no compat guarantee yet → [[pocketbase (github)]]
- [Bumblebee](https://github.com/perplexityai/bumblebee) — read-only developer endpoint scanner from Perplexity: checks on-disk packages/extensions for known supply-chain compromises; Go (*INSTALL: QUEUED — run first, before any other repo on this page installs*) → [[bumblebee]]
- [Modern JS Cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet) — comprehensive modern JavaScript reference; ES6+ concepts with examples *not useful* → no relations

---

## Building (10)

Tools and starters for actually building things.

- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents; [paper](https://arxiv.org/pdf/2412.20138) *(also in: Projects)* → [[TradingAgents]]
- [OpenBB](https://github.com/OpenBB-finance/OpenBB) — open-source financial data platform; stocks, crypto, macro data; Python; programmatic Bloomberg terminal alternative (*INSTALL: QUEUED — TradingView project-scoped, provider-agnostic swap-in for [[AI Market Analyzer - Data Sources]]'s hardcoded provider risk*) → [[openbb]]
- [Kronos](https://github.com/shiyu-coder/Kronos) — 27K-star foundation model for financial markets language; time series + NLP; Python. (Tradingview: Going to be used but is there anything better out there yet?) → [[Kronos]]
- [Jan](https://github.com/janhq/jan) — 42K-star fully offline ChatGPT alternative; runs 100% locally; Tauri + LlamaCPP → [[jan]]
- [PageIndex](https://github.com/VectifyAI/PageIndex) — 32K-star vectorless reasoning-based RAG (no embeddings); document index using LLM reasoning chains → [[PageIndex]] (the earlier-flagged duplicate ingestion file no longer exists, confirmed in the GitHub pass)
- [Obsidian Dashboard](https://github.com/handrovermeulen/Obsidian-Dashboard) — community Obsidian vault dashboard template with statistics and navigation → [[obsidian-dashboard]]
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus) — (to be evaluated) → [[gitnexus]]
- [Pretext](https://github.com/chenglou/pretext) — (to be evaluated) *not useful* → no relations
- [Autoresearch](https://github.com/karpathy/autoresearch) — Karpathy's automated research agent *(also in: AI)* → [[autoresearch]]
- [Ghostty Blackhole](https://github.com/s0xDk/ghostty-blackhole) — Ghostty terminal emulator configuration and theme collection *not useful* → no relations

---

## Jobs (7)

Internship lists, interview prep, and job search resources.

- [Summer 2026 Internships](https://github.com/SimplifyJobs/Summer2026-Internships) — 44K-star: daily-updated SWE/DS/AI/quant internship postings for Summer 2026; maintained by Simplify + Pitt CSC → [[summer2026-internships]]
- [Underclassmen Internships](https://github.com/zapplyjobs/underclassmen-internships) — curated list of internships/fellowships exclusive to CS freshmen and sophomores (updated for 2026) → [[underclassmen-internships]]
- [Interview Company-wise Problems](https://github.com/liquidslr/interview-company-wise-problems) — CSV files of company-tagged LeetCode questions; updated June 2025; Google/Amazon/Meta focus → [[interview-company-wise-problems]]
- [Tech Interview Handbook](https://github.com/yangshun/tech-interview-handbook) — 139K-star curated coding interview prep: algorithms, behavioral, system design, negotiation → [[tech-interview-handbook]]
- [Coding Interview University](https://github.com/jwasham/coding-interview-university) — 347K-star complete CS study plan for SWE roles: data structures, algorithms, system design, OS → [[coding-interview-university]]
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — 350K-star: learn how to design large-scale systems; interview prep + Anki flashcards *(also in: Learning)* → [[system-design-primer]]
- [Hiring Agent](https://github.com/interviewstreet/hiring-agent) — AI agent for automated technical interview workflows from HackerRank *(also in: AI)* → [[hiring-agent]]

---

## Learning (15)

Courses, zoomcamps, and structured learning paths.

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) — 41K-star free 9-week course: Docker, Kafka, Spark, dbt, Kestra, production data pipelines → [[data-engineering-zoomcamp]]
- [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) — 13K-star free 4-month ML engineering course: deployment, Docker, Kubernetes, FastAPI → [[machine-learning-zoomcamp]]
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — 14K-star free MLOps course: tracking, deployment, monitoring, workflow orchestration → [[mlops-zoomcamp]]
- [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) — free 10-week course: RAG, vector search, LLM evaluation, monitoring → [[llm-zoomcamp]], [[Portfolio Option A — RAG + Hybrid Search (jarvis-memory Build)]] (load-bearing for the jarvis-memory RAG build)
- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) — free course: use Claude Code, MCP, and coding agents effectively → [[ai-dev-tools-zoomcamp]]
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — 350K-star: learn how to design large-scale systems; interview prep + Anki flashcards *(also in: Jobs)* → [[system-design-primer]]
- [Project Based Learning](https://github.com/practical-tutorials/project-based-learning) — 266K-star curated tutorials for building real projects in every major language → [[project-based-learning]]
- [ProjectLearn](https://github.com/Xtremilicious/projectlearn-project-based-learning) — web app frontend for browsing project tutorials by technology and category *not useful* → no relations
- [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) — 445K-star open-source curriculum: math, CS, data structures, ML; full certifications available free → [[freeCodeCamp]]
- [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) — 389K-star index of freely available programming books in all languages; CC-BY-4.0 *not useful* → no relations
- [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) — 35K-star in-depth tutorials on LLMs, RAGs, real-world agents (Jupyter notebooks); Daily Dose of DS → [[ai-engineering-hub]]
- [LeetCode Company-wise](https://github.com/snehasishroy/leetcode-companywise-interview-questions) — company-wise LeetCode questions as of May 2026; Java solutions → [[leetcode-companywise]]
- [Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) — Anthropic's official interactive prompt engineering course; hands-on exercises with solutions → [[prompt-eng-interactive-tutorial]]
- [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) — community-driven learning roadmaps organized by technology track *(also in: Projects)* → [[developer-roadmap]]
- [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — end-to-end AI engineering curriculum from foundations to production deployment *(also in: Projects)* → [[ai-engineering-from-scratch]]

---

## Projects (15)

Project ideas, inspiration, and curated resources.

- [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x) — 506K-star: master programming by recreating technologies from scratch (DB, OS, browser, shell, etc.) → [[build-your-own-x]]
- [App Ideas](https://github.com/florinpop17/app-ideas) — 94K-star app ideas organized by difficulty: Newbie / Intermediate / Advanced tiers with specs → [[app-ideas]]
- [500 AI/ML Projects](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) — 500 AI/ML/CV/NLP project ideas with code; organized by domain → [[500-ai-ml-projects]]
- [Semantic Search Starter](https://github.com/dabit3/semantic-search-nextjs-pinecone-langchain-chatgpt) — embed text → Pinecone, semantic search with GPT3 + LangChain in Next.js UI *not useful* → no relations
- [Jarvis](https://github.com/ethanplusai/jarvis) — voice-first AI assistant for macOS inspired by MCU; Claude + Three.js + Whisper *not useful* → no relations
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — 80K-star multi-agent LLM financial trading framework: analyst/researcher/trader/risk manager agents *(also in: Building)* → [[TradingAgents]]
- [AI Weekend Builds](https://github.com/kju4q/ai-weekend-builds) — weekend AI project starters using Anthropic API; Python/Node with READMEs and starter code → [[ai-weekend-builds]]
- [OpenHuman](https://github.com/tinyhumansai/openhuman) — 29K-star personal AI super intelligence; private, simple, Rust/GPL *(also in: AI)* → [[openhuman]]
- [Applied ML](https://github.com/eugeneyan/applied-ml) — 29K-star papers + tech blogs from companies sharing ML/data science in production; by Eugene Yan. (*GOLD*) *(also in: AI)* → [[applied-ml]]
- [Public APIs](https://github.com/public-apis/public-apis) — 437K-star collective list of free APIs organized by category *(also in: AI)* → [[public-apis]]
- [DevOps Projects](https://github.com/NotHarshhaa/DevOps-Projects) — 50+ real-world DevOps projects with solutions across AWS, Docker, Kubernetes, Jenkins → [[devops-projects-notharshha]]
- [DevOps Projects (techiescamp)](https://github.com/techiescamp/devops-projects) — beginner-to-advanced DevOps project tutorials with step-by-step guides → [[devops-projects-techiescamp]]
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — curated collection of LLM app examples with Agno, OpenAI, Anthropic, Gemini; use as inspiration for project ideas → [[awesome-llm-apps]]
- [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — end-to-end AI engineering curriculum *(also in: Learning)* → [[ai-engineering-from-scratch]]
- [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) — community-driven learning roadmaps organized by technology track *(also in: Learning)* → [[developer-roadmap]]

---

## Cybersecurity (4)

Security tooling and research.

- [CAI](https://github.com/aliasrobotics/cai) — Cybersecurity AI framework: AI-powered pentesting and security research; Python + multi-agent; from Alias Robotics → [[cai]]
- [KeyHacks](https://github.com/streaak/keyhacks) — quick ways to verify if leaked API keys from bug bounty programs are valid; reference for bug bounty + key auditing → [[keyhacks]]
- [PentestGPT](https://github.com/GreyDGL/PentestGPT) — LLM-powered penetration testing assistant: knowledge reasoning + guided penetration testing workflow → [[pentestgpt]]
- [MantisHack](https://github.com/deonmenezes/mantishack) — autonomous security framework on Claude Code (fork of RAPTOR): scan, validate, exploit, patch via slash commands (/mantis-agentic, /mantis-scan, /mantis-auth-audit, etc.) → [[mantishack]]

---
# Removed
Repos decided against, reasoned per entry — either genuinely not useful, or fully redundant with something already adopted (a "drained" repo: everything worth extracting from it already has been, and it does nothing further for an active project). Full reasoning for the GitHub pass overall lives in [[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution#Github|00_Execution § Github]].
**Already self-marked *not useful* — confirmed, no re-litigation:** Claude Code Templates (redundant with the plugin marketplaces now used directly), Dify (team-scale infra, not solo tooling), React Three Fiber, Modern JS Cheatsheet, ProjectLearn, Free Programming Books, Ghostty Blackhole, Mike, Paperclip, Jarvis (ethanplusai, macOS-only), Semantic Search Starter, Pretext.
**Dropped this pass, with reason:**
- **GitNexus** — dropped per your own header tag on [[PDF's Ingestion Implementation]]; CausalOps's own graphify report already gives blast-radius visibility, no second tool needed.
- **Free Claude Code** — proxy fallback to NVIDIA NIM/OpenRouter for quota exhaustion; not needed with an active Claude subscription.
- **jcode** — README was empty at time of review; can't evaluate, nothing to fork.
- **Odysseus** — self-hosted AI workspace (chat/agents/research/email/calendar); fully redundant with Jarvis + gbrain + the ECC harness already being adopted — a second personal-AI-workspace platform fragments rather than helps.
- **OpenHuman** — same reasoning as Odysseus: a second "private personal AI assistant" framework competes with, rather than extends, Jarvis + gbrain + jarvis-memory. Drop, not build a parallel system.
- **Hiring Agent** — this is a tool for companies *running* technical interviews (HackerRank), not for a candidate taking them; no application to Anant's own job search.
- **Obsidian Dashboard** (community template) — redundant now that Jarvis's own dashboard is a custom DataviewJS build already ahead of a generic template.
- **ScrapeGraph-ai, Scrapling** — both redundant with Firecrawl, which is already integrated as a full skill suite (18+ firecrawl skills active) and covers the same scraping need with a working install, not a hypothetical one.
- **Crawl4AI** — same reasoning: redundant scraping framework, Firecrawl already does this.
- **ASI-Evolve, dots.ocr, AirLLM** — local-model/research-artifact tools with no active use case while on a Claude subscription with no local-inference workflow yet; drained of near-term relevance, not of quality.
## See Also

- [[40_Resources/CS/Links]] — general CS links
- [[40_Resources/CS/AI/]] — AI-specific concept notes
- `60_Claude/10_Source_Summaries/Github Ingestion/` — individual repo deep-dives
