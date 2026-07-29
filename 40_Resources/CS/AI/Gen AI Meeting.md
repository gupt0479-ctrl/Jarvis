---
type: concept
course: AI
status: sprout
mastery (1/10): 2
created: 2026-02-14
updated: 2026-07-29
topics:
  - "[[Chat Gpt Prompts]]"
related:
  - "[[40_Resources/CS/Links|Links]]"
  - "[[AI Generalist Roadmap — Outskill (PDF)]]"
---
# Gen AI Mastermind
==This course's own "5 levels" framing (see Meeting notes below) is the same curriculum Outskill also published as a marketing slide deck, separately ingested at [[AI Generalist Roadmap — Outskill (PDF)]] — same provider, same level structure, worth cross-checking against each other rather than treating as two unrelated sources.==
Mail: hi@outskill.com
## MOC
- [[Gen AI Day - 1]]: Day 1 (sessions 1 & 2)  
- [[Gen AI Day - 2]]: Day 2 (sessions 3 & 4)  
- [[Gen AI Roadmap]]: The full plan after the course
- [AI social media updates](https://docs.google.com/spreadsheets/d/1pGZR1F_GhqGRJ1JxSYU6hVaekLkRESSH_PisOpJfi38/edit?gid=0#gid=0)
- Notes for the Mastermind: [Resource Guide?](https://highfalutin-camel-f57.notion.site/OutSkill-s-Generative-AI-Mastermind-Session-1-Resource-Guide-2572c10dd7068090a415fa41db7b5d54)
	- [Image and video](https://www.notion.so/Outskill-Mastermind-Generative-AI-Image-and-Video-February-15-2026-2edb19856cb080e2952bf9c460a05ce8)
	- [AI Bots & Custom GPTs](https://marsh-top-656.notion.site/A-Comprehensive-Guide-to-build-AI-Bots-Custom-GPTs-Key-Tools-and-Processes-Session-by-Vaibhav-S-2599488ddc8080368939c978309f2f74)
	- [Vibe Coding](https://special-crater-db5.notion.site/Vibe-Coding-101-Resource-Guide-2906e0c1b86881949e32f5b7b927bb0b)
### Master Prompts
- [[UMN Workflow]]
- [[Chat Gpt Prompts]]: Obsidian Prompts and basics of prompting  
## Definition
- **What this file covers (big picture)**
	- How Gen AI tools fit together: prompts → assistants → automations → agents → products
	- How to go from “I have an idea” to “I shipped a working app” using vibe coding tools
- **Topics covered (from sessions + resources)**
	- LLM fundamentals: tokenization, embeddings, self-attention, token prediction (5-step mental model) [[Gen AI Day - 1#How LLMs work (5-step model)]]  
	- Prompt engineering: Magic Prompt Formula + prompting techniques (zero-shot, few-shot, CoT, ToT, meta prompting, prompt chaining) [[Gen AI Day - 1#Prompt engineering]]
	- Custom GPTs: GPT marketplace, create + configure, instructions as the “heart” of the app [[Gen AI Day - 1#Custom GPTs (GPT Marketplace)]]  
	- Markdown prompting: Role, Objective, Context, Instructions, Notes (structured “one-time onboarding”) [[Gen AI Day - 1#Markdown Prompting]]  
	- Content DNA workflow: style extraction → prompt → reusable assistant [[Gen AI Day - 1#Content DNA workflow]]  
	- Image + video creation: creative brief → script → storyboard → image prompt → image-to-video → VO/music → edit (full production workflow) [[Gen AI Day - 2#AI video workflow (pre → pro → post)]]  
	- Vibe coding: iterative build loop, app architecture basics, feature extraction from competitors, Pareto prioritization, PRD stages, debugging loop [[Gen AI Day - 2#Vibe Coding]]
- **Methods demonstrated**
	Ask AI to dissect past posts, generate a DNA report, turn the report into a reusable markdown prompt, copy the prompt from a code block, paste it into Custom GPT instructions or a Gemini Gem, upload a transcript as a knowledge base, test the app with a sample topic, refine the output, split the prompt into role objective and instructions for Lyser, use the agent API code to connect a UI built on Replit or similar, enable voice with WAPI by selecting a voice profile, trigger calls or messages via VAPI, pull portfolio data from Kite, scrape Instagram reels with Apify, let AI write and remix presentation slides in Chronicle, run local models with Ollama for privacy, switch models and parameters in Bolt AI, automate file operations with Goose, integrate Slack workflows with Zapier or Make.
## Resources
- **Key resources**
	1. **Core LLMs (text)**  
		- ChatGPT – https://chat.openai.com  
			- General LLM for writing, studying, prompts, coding help, Custom GPTs → no relations (generic tool, not individually ingested)
		- Claude – https://claude.ai  
			- Strong for long docs + structured thinking; used heavily for scripts + planning → no relations
		- Gemini – https://gemini.google.com  
			- LLM + Gemini Gems (custom assistants) → no relations
	2. **Research + transcripts** 
		- Perplexity – https://www.perplexity.ai/  
			- Research with citations for verification → no relations
		- Fireflies AI  
			- Meeting transcription + summaries → no relations
		- Otter AI  
			- Meeting transcription + searchable notes → no relations
		- Whisper Flow  
			- Voice-to-text capture (fast note capture) → no relations
		**Prompting references**
		- Prompt Engineering Guide – https://www.promptingguide.ai/  
			- Catalog of prompting methods + examples (reference when stuck) → no relations
		- Outskill website – https://outskill.com  
			- Course hub + learning paths + downloads → [[AI Generalist Roadmap — Outskill (PDF)]] (same course provider, separately ingested)
	3. **Data & Automation:**
		- N8N  
			- Self-hostable workflow automation (good if you want control) → [[How Anant Uses Each Repo]], [[ai-dev-tools-zoomcamp]], [[Useful Repos - Shortlist]] (same tool referenced across the Jarvis automation-layer discussion — not yet adopted there either)
		- Zapier – https://zapier.com  
			- Simple no/low-code automations across apps → no relations
		- Make – https://make.com  
			- Visual automation builder; flexible multi-step scenarios → no relations
	4. **Content (slides + docs + scraping)**  
		- Chronicle – https://chroniclehq.com/  
			- Presentation builder (generate + remix slides) → no relations
		- Apify – https://apify.com  
			- Web scraping + ready-made actors (ex: social data extraction) → [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/Outreach Automation Manual (PDF)]] (same tool proposed there for outreach contact-discovery, per [[10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status]])
		- Numerous AI  
			- AI inside Excel/Sheets for data transforms and analysis → no relations
		- Comet/Atlas  
			- Agentic browsing (automate browser tasks and extraction) → no relations
	5. **Finance / data APIs**
		- Kite Zerodha – https://kite.zerodha.com  
			- Brokerage platform + API access for holdings/portfolio tasks → no relations
	6. **Model switching + model access**
		- OpenRouter – https://openrouter.ai  
			- Single API key to access many models → [[40_Resources/CS/Links]] (same tool bookmarked there under "Free Models", no relations of its own)
		- Bolt – https://bolt.ai  
			- Vibe coding builder + model switching + restore + GitHub sync → no relations
		*Local Models*: Ollama – https://ollama.com
		- Run models locally (privacy + offline) → no relations
	7. **Agents + tool connectors**  
		- MCP (Model Context Protocol)  
			- Tool connector concept (assistant can access external tools) → [[40_Resources/Obsidian/MCP-Hub-Index]] (Jarvis's own MCP roster, the concrete instance of this concept)
		- Lyser – https://lyser.ai / https://www.lyzr.ai/  
			- Agent builder: prompts + tools + API output for front-end integration → no relations
		- Replit – https://replit.com  
			- Host/run small apps quickly; useful for wiring agent APIs to a UI → no relations
		- Lovable  
			- No/low-code app builder (used as an option alongside Bolt/Replit) → no relations
		- Goose  
			- Automation for file operations and local workflows → [[goose (github)]] (plausibly the same general-purpose Rust agent — description overlap, not confirmed identical product)
		- WAPI – https://wapi.ai  
			- Voice assistant for phone workflows (speak + call/message flows) → no relations
		- VAPI – https://vapi.ai  
			- Voice call flows and programmable call actions → no relations
	8. **Content & Marketing:**
		- Social Sonic  
			- LinkedIn content automation → no relations
		- SuperGrow  
			- LinkedIn distribution/repurposing → no relations
		- Suno AI  
			- AI music generation (useful for videos/reels) → no relations
		- HeyGen  
			- Video avatar + cloning style workflows → no relations
	9. **Image + video creation (from sessions + pre-reads)**
		- Midjourney  
			- Image generation tool (strong aesthetics) → no relations
		- Runway – https://runwayml.com/  
			- Video gen + editing tools (Gen 4.5 referenced) → no relations
		- Luma Dream Machine – https://lumalabs.ai/dream-machine  
			- Video creation from prompts (pre-reads) → no relations
		- Topaz AI  
			- Video upscaling/enhancement (pre-reads) → no relations
		- ElevenLabs – https://elevenlabs.io/  
			- Text-to-speech + voiceovers (pre-reads) → no relations
		- Canva – https://www.canva.com/  
			- Design tool + storyboard alternative (recommended if new) → no relations
		- Figma  
			- Storyboarding + layout tool (used in session) → no relations
		- Adobe Premiere Pro  
			- Video editing tool (post-production) → no relations
		- CapCut  
			- Free editing alternative (post-production) → no relations
		- DaVinci Resolve  
			- Free editing alternative (post-production) → no relations
		- Crea/Krea (model aggregator)  
			- Multi-model image/video playground mentioned in session 3 (one place, many models) → no relations
## How to use them
- **Core habit (from sessions): build one strong prompt, then reuse it everywhere**: ChatGPT / Claude / Gemini (core loop)
	- Keep a “master prompt” in markdown and paste into:  
		- ChatGPT instructions (Custom GPT)  
		- Gemini Gems  
		- Claude Projects  
		- Agent tools (Lyser)
	- Use one tool to *write or improve the prompt for that same tool* (they explicitly recommended: write Gem prompts in Gemini; Claude prompts in Claude; etc.).
- **Session 3 content stack**  
	- Creative brief + script (Claude) → storyboard (Figma/Canva) → image prompts → image-to-video (selected model) → VO (ElevenLabs or similar) + music → edit (Premiere/CapCut/Resolve) [[Gen AI Day - 2#AI video workflow (pre → pro → post)]]
- **ChatGPT (Custom GPTs)**
	- Explore GPTs → pick a GPT → observe behavior  
	- Create GPT → iterate by giving feedback → move to Configure → edit Instructions (the heart) [[Gen AI Day - 1#Custom GPTs (GPT Marketplace)]]
- **Claude**  
	- Best for: long docs, script drafts, structured writing, planning multi-step workflows  
	- Use when you need “long context + clear structure” [[Gen AI Day - 2#Script creation (Claude)]]
- **Gemini Gems**  
	- Gemini → Gem Manager → New Gem → paste markdown prompt into Instructions → save → test with a topic.
- **Lyser (agent builder)**  
	- Create agent → split prompt into Role / Goal / Instructions → add knowledge files → save → generate Agent API code → connect to a UI (Replit).
- **Bolt (vibe coding + model switching)**  
	- Start from a PRD → ask Bolt to build one feature → test → fix → repeat.
	- Use bookmarks/restore if a change breaks the project.
	- Connect GitHub so you always have a backup outside Bolt.
- **OpenRouter (model access)**  
	- Create account → get API key → plug into Bolt or your scripts → choose model per task (writing vs coding vs long docs).
- **Ollama (local models)**  
	- Install Ollama → `ollama list` → `ollama pull <model>` → `ollama run <model>` → ask questions locally (good for private notes/docs).
	- Use for private notes/docs when you don’t want to paste into cloud tools [[Gen AI Day - 1#Local models for privacy (Ollama)]]
- **MCP (connect assistants to tools)**  
	- Treat MCP like “tool connectors” that let an assistant trigger actions (calls, scraping, data pulls) via connected apps.
	- Typical use: Claude + MCP + (VAPI/WAPI/Apify/etc.) so you can write one instruction and the system executes it.
	- Assistant plans; connectors execute actions (calls/scraping/saving) [[Gen AI Day - 1#MCP (Model Context Protocol)]]
- **Make / Zapier / n8n (automations)**  
	- Pick a trigger (new email / schedule / new row in Sheets) → call your AI prompt → route output to email/Slack/Sheets/DB.
	- Use workbook blueprints as starter templates, then swap prompts + destinations.
	- Keep “draft-first” behavior until stable [[Gen AI Day - 1#Automations (Zapier / Make / n8n)]]
- **Apify (scraping)**  
	- Pick an Actor (ex: Instagram scraper) → configure input → run → export JSON/CSV → feed results into your content prompt for rewrite.
- **Chronicle (presentations)**  
	- Paste a brief → auto-generate slides → remix slides → replace placeholders → export final deck.
- **WAPI / VAPI (voice)**  
	- Build a voice assistant/flow → choose voice → connect number/message → test in sandbox → then use in workflows (often triggered via MCP or automations).
- **Perplexity (research)**  
	- Use for “source-backed” reads: ask for explanations + citations, then bring the verified notes into your own prompt/assistant.
# Meeting notes
The 2-Day Generative AI Mastermind covered a curriculum structured across five levels:
**Level 1 - AI Fundamentals:** LLM basics, prompting frameworks, reasoning vs non-reasoning, productivity tools  
**Level 2 - Automation:** MCP, voice agents, workflows, local models  
**Level 3 - Content Creation:** image/video/voice tools, presentation generation  
**Level 4 - Agents:** “do tasks for me” bots that use tools + workflows  
**Level 5 - Product Building:** vibe coding apps end-to-end
## [[#Levels]]
## Things To Do  
1. Build one “default tutor prompt” in markdown (Role/Objective/Context/Instructions/Notes) and test on 3 topics  
2. Build one Custom GPT that uses your tutor prompt  
3. Create one automation: weekly recap from notes → saved output  
4. Build one small vibe-coded app (CRUD + 1 AI feature)
## Flashcards (best 3–8)
