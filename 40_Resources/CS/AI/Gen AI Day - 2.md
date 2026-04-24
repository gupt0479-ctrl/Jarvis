---
type: concept
course: AI
status: seed
mastery (1/10): 0
created: 2026-02-15
updated: 2026-07-27
topics:
  - "[[Chat Gpt Prompts]]"
  - "[[Gen AI Day - 1]]"
  - "[[Gen AI Roadmap]]"
  - "[[UMN Workflow]]"
related:
  - "[[Gen AI Meeting]]"
tags:
  - concept
track:
  - ai
prerequisites:
  - "[[Gen AI Day - 1]]"
used_in: []
evidence: []
difficulty: 2
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-09
drill_interval: 14
---
# Day - 2
## MOC
- [[Chat Gpt Prompts]]: Obsidian Prompts and basics of prompting
- [[Gen AI Day - 1]]: Day 1 (sessions 1 & 2)
- [[Gen AI Meeting]]: Main file (resources + how to use)
- [[Gen AI Roadmap]]: Full plan after course
## Definition
- Day 2 focus (Session 3 + Session 4)
	- Session 3: professional AI image/video workflow (pre → pro → post)
	- Session 4: vibe coding (build apps iteratively with a clear spec + debugging loop)
## Meeting notes
### Session 3: Image + video creation (full workflow)[[Gen AI Day - 2#AI video workflow (pre → pro → post)]]
- Pre-production:
	- Idea → creative brief → script → storyboard → image assets
- Production:
	- Image-to-video generation + voiceover + music (assets
- Post-production:
	- Edit in Premiere or use CapCut/DaVinci Resolve → final cut + premiere review.
### Session 4: Vibe coding [[Gen AI Day - 2#Vibe Coding]]
- Iterative build loop is the core: build → test → fix → repeat
- App architecture basics (restaurant analogy)
- Feature extraction from competitors (screenshots + LLM)
- Pareto prioritization (core features first)
- PRD stages + debugging loop
## AI video workflow (pre → pro → post)
### Pre-production
#### Idea (what are we making?)
- Start with one clear concept for the ad/video
- Reminder from session: output quality depends on idea + story, not just visuals
#### Creative brief (alignment doc)
- Purpose: keep the project aligned (what, why, for whom, key message, tone, where it will be shown)
- The brief influences:
	- format/aspect ratio (TV vs vertical)
	- tone + target audience choices
#### Script creation (Claude)
- Prompt structure used:
	- set role (marketing copywriter)
	- set context (brand, audience, tone)
	- set task (30s spec ad, no cheesy lines)
	- paste brief and iterate
- They iterated until VO lines had better rhythm/flow
#### Storyboard (Figma / Canva)
- Storyboard = grid:
	- frame for visual + text area for VO line
	- scene/shot numbering helps organization
- Tools:
	- Figma recommended (free trial); Canva as simpler alternative 
#### Image prompting framework (director mindset)
- A prompt checklist they used for image shots:
	- subject
	- action (optional)
	- environment
	- atmosphere
	- camera + lens (optional)
	- lighting
	- style reference (cinematic / realistic etc.)
- Key idea: if you don’t know camera terms, skip them; still works
### Production
#### Image generation + model selection
- The instructor’s guidance:
	- don’t chase every tool; pick a few favorites and get strong with them.
- They used a model aggregator (Crea/Krea style) to access multiple models in one place.
#### Image-to-video generation
- Workflow:
	- generate strong still image → animate into video using an image-to-video model
- Models mentioned in the flow:
	- Google V3, Kling, Runway (and others shown as options)
#### Voiceover + music
- Voiceover: create VO lines (script) → generate voice with a TTS tool (ElevenLabs mentioned in pre-reads) 
- Music: generate an instrumental track matching tone (upbeat, futuristic, premium gym ad vibe)
#### Asset organization (non-negotiable)
- They repeatedly emphasized staying organized:
	- keep assets in folders (images, video clips, audio, exports) 
### Post-production
#### Edit + final cut
- Editing tools:
	- Adobe Premiere (used)
	- CapCut / DaVinci Resolve (free alternatives)
- Final: assemble clips + VO + music → export → group “premiere” review
## Extra Points
### Automations: Zapier / Make / n8n (turn AI into workflows)
1. Detailed explanations
	- **Trigger**: new email / new form entry / new file in Drive
	- **Action**: send content to an AI prompt endpoint
	- **Output routing**: store response in Sheets/Notion/Slack/DB
2. Practical workflows (beginner-friendly)
	1. **Weekly learning summary**
	    - Trigger: every Sunday
	    - Action: AI summarizes your notes
	    - Output: sends to Slack / email / a “Weekly Recap” page
	2. **Portfolio content helper**
	    - Trigger: new GitHub repo link in a sheet
	    - Action: AI drafts a project description + bullets
	    - Output: saved to a “Portfolio Drafts” doc
### MCP (Model Context Protocol): “AI can use my apps”
1. Brief summary: MCP is a standard way to connect an assistant (like Claude) to external tools/services so it can perform actions using structured tool calls.
2. Their concrete example (how to remember it):
	- “Claude + MCP + VAPI/WAPI” means you can instruct Claude to create/run a voice call flow without manually opening every dashboard step.
3. Implementation mindset (so you don’t get lost):
	- MCP = connectors + permissions + “tool menu”
	- Assistant = planner (“what should happen”)
	- Tools = doers (“make the call”, “scrape the page”, “save the file”).
### Local models for privacy (Ollama)
1. Brief summary: Ollama runs models on your laptop so data stays local—useful for private notes/docs.
2. Detailed explanations (what they were pushing as the “why” + “how”):
	- **Why use local**:
		- You can test prompts on sensitive material without sending it out.
		- You can keep a “local assistant” for private note cleanup, journaling, or personal docs.
	- **Basic commands (what you should remember)**:
		- `ollama list` → see what’s installed
		- `ollama pull <model-name>` → download a model
		- `ollama run <model-name>` → start chatting locally
	- **Practical uses (beginner-friendly)**:
		- Clean up transcripts into notes (locally).
		- Rewrite personal portfolio bullets from raw notes (locally).
		- Summarize course PDFs into checklists without uploading anywhere.
	- **How it fits your stack**:
		- Cloud model (ChatGPT/Claude) for best outputs + tools
		- Local model (Ollama) when privacy matters or you want offline.
### Model switching and choosing models (Bolt AI + OpenRouter)
The course pushes “use more than one model” and adjust settings (temperature, max tokens, penalties, top-p) to match the task.
1. Detailed explanations: Use **Bolt AI connected to OpenRouter** to access many models and tune parameters like temperature, max tokens, presence/frequency penalties, top-p/top-k.
	Why this matters:
	- Some models are better at coding, some at writing, some at long reasoning.
	- Settings change behavior:
	    - Higher temperature → more variety
	    - Lower temperature → more predictable
	    - Max tokens → longer answers
	    - Penalties → reduce repetition
2. Practical examples / applications
	- For coding/debugging: lower temperature, ask for step-by-step diagnosis.
	- For brainstorming UI copy: moderate temperature, ask for 10 variants.
## Vibe Coding
### Vibe Coding Overview
- “Iterative” build‑by‑feature process: build → test → fix → repeat
- No code required; AI handles generation, wiring, and deployment
- Mindset: small visible steps, loose timelines, fix gaps with AI prompts
- Core phases: idea generation → PRD creation → platform‑optimized spec → AI‑driven build
### The vibe coding rules (6 commandments)
- 1) Start with a plan
	- AI can’t read your mind; it can only follow what you write
	- Use the PRD stages before you build
- 2) Give clear, specific instructions
	- When stuck, use the ODA loop below
- 3) Build and test in small pieces
	- Add one feature at a time
	- Test after each addition, debug immediately
- 4) Save your work constantly
	- Bolt auto-saves, but still sync to GitHub as a backup
	- Bolt has bookmarks + restore so you can roll back to a working version
- 5) Make it responsive early
	- Use responsive mode to preview phone/tablet layouts while you build
- 6) Polish at the end, not the start
	- First get working flows (auth, DB, CRUD), then improve UI/animations
### ODA debugging loop (the default way to fix things)
- Observe: what exactly is broken (what did you expect vs what happened)
	- Copy the exact error text
	- Note where it shows up (screen + action)
- Diagnose: why you think it happened
	- Common buckets they implied:
		- missing env var
		- database/schema mismatch
		- UI state not updating
		- auth not connected correctly
- Ask: give Bolt a specific fix request
	- Include:
		- error text
		- the feature you were building
		- “only change what’s needed” (so it doesn’t rewrite everything)
### PRD Path (3 Stages)
- **Stage 1 – Simple Prompt**
	- One-liner idea to get an initial direction fast
	- Output: rough outline, features list, maybe wireframe-level ideas
- **Stage 2 – Basic PRD**
	- Problem, users, goals, feature list, acceptance criteria
	- Still platform-agnostic (describes what, not how)
- **Stage 3 – Platform-Optimized PRD**
	- “Speak the tool’s language”
	- The same PRD rewritten into instructions that match the platform/tool
		- Example: React + TS routes, DB schema, auth provider, API contracts, test cases
	- Their point: tools change every week; frameworks stay useful
#### Feature Ideation & Prioritization
- “Swagger-jacking”: copy competitor feature sets, then improve
- Two routes:
	- improve an existing app
	- invent a brand-new solution
- Use AI to extract feature lists from competitor pricing pages (Monday.com, Asana, Trello)
- Apply Pareto principle: focus on the small set of features that deliver most value
- Prioritize:
	1. Core task management (create, assign, due dates, status)
	2. Board/Kanban view (drag-and-drop)
	3. AI task-breakdown generator (differentiator)
### Application Architecture Analogy
- **Front-end = Dining area** – what users see and interact with
- **Back-end = Kitchen** – where business logic and data processing happen
- **API = Waiter** – carries requests/responses between front-end and back-end
- **Database = Pantry** – stores ingredients (users, projects, tasks) with unique IDs (UUIDs)
### Database Primer
- Relational model illustrated with Spotify (Users ↔ Playlists ↔ Songs)
- Tables needed for project-management app: users, boards, tasks, comments
- Primary keys (UUID) link records; foreign keys enforce relationships (board → tasks)
- AI can auto-generate schema from feature table via a simple prompt
### Platform-optimized prompts (Bolt “dialect”)
- What they did:
	- Google “Bolt new best practices”
	- Copy the prompting rules
	- Paste into Claude
	- Ask Claude to rewrite your Stage-2 PRD into a Stage-3 prompt that follows Bolt’s best practices
- Why this helps:
	- You avoid “generic” prompts that cause Bolt to guess your intent
	- You reduce random rewrites because the tool gets structured constraints
- The meta-skill they pushed:
	- Do not memorize one tool’s UI
	- Learn how to convert your intent into the “dialect” that tool expects
### Build flow they demo’d (what happened step-by-step)
1) Start with the app idea (project management tool)
2) Stage 1 prompt → generate initial outline
3) Convert into Stage 2 Basic PRD (problem, users, core differentiator)
4) Convert into Stage 3 platform-optimized prompt (tool-specific)
5) Build inside Bolt one feature at a time:
	- Landing page + sign-in flow
	- Database connection
	- CRUD for core entities (boards/tasks)
	- AI feature: task breakdown from a text description
6) Test each feature immediately
7) When something breaks: ODA loop → patch → test again
8) Save + sync:
	- Use Bolt bookmarks/restore if it breaks badly
	- Connect GitHub repo to keep code outside Bolt
9) Preview responsive mode (phone/tablet)
10) Only after core works: polish UI (theme, typography, animations)
### Testing & Iterative Development
- CRUD cycle: **Create**, **Read**, **Update**, **Delete**
	- Verify UI updates + DB updates after each action
- Test each feature immediately after generation; fix before moving on
- “Chaos monkey” mindset:
	- Try weird inputs so you find weak spots before users do
- Keep a “bug log” note:
	- error text
	- what you clicked
	- what fixed it (so you can reuse later)
### Payments and “real app” completeness
- They briefly walked through adding payments as “another module you can plug in”
- Mental model:
	- payments are just another integration:
		- create provider account
		- add keys
		- add pricing plan + checkout flow
		- test
- Keep this as “week 4/5 add-on” after your core app works.
## Flashcards (best 3–8)


---

## Deep Dive

### One-Sentence Version

Vibe coding is an iterative build loop (plan → build one feature → test → fix with ODA → repeat) where AI generates the code and you control scope, architecture, and verification — it works only when you constrain the AI tightly with PRDs and small steps.

### What It Is

Two distinct workflows from Session 3 and Session 4:

**AI Video Production** (Session 3): A pipeline from idea → creative brief → script → storyboard → image generation → image-to-video → voiceover + music → edit → final cut. Each stage uses a different AI tool (Claude for scripts, image models for stills, video models for animation, ElevenLabs for voice). The key insight: output quality depends on the brief and storyboard, not on which model generates the pixels.

**Vibe Coding** (Session 4): An iterative development method where AI writes the code and you manage the spec. The 6 commandments: start with a plan, give specific instructions, build in small pieces, save constantly, make it responsive early, polish last. The PRD path has 3 stages: simple prompt → basic PRD → platform-optimized PRD (rewritten in the tool's "dialect").

The ODA debugging loop (Observe → Diagnose → Ask) is the core recovery mechanism: copy the exact error, hypothesize why it broke, then give the AI a scoped fix request instead of letting it rewrite everything.

### Why It Matters

- Vibe coding lets you ship working prototypes without writing code yourself, but only if you maintain architectural control. Without a PRD and incremental testing, the AI generates plausible-looking code that breaks in non-obvious ways.
- The 3-stage PRD path is the most transferable skill from this session — it works with Bolt, Cursor, Replit, or any AI coding tool. The tool changes; the spec discipline doesn't.
- The ODA loop prevents the most common vibe-coding failure: asking the AI to "fix it" without context, which causes cascading rewrites.

### Real Example

From the course demo: they built a project management app in Bolt by starting with a Stage 1 prompt ("I want a project management tool"), converting it to a Stage 2 PRD (problem, users, core differentiator: AI task breakdown), then rewriting it as a Stage 3 Bolt-optimized prompt (React + TS routes, DB schema, auth provider, API contracts). Each feature was added one at a time — landing page, then auth, then CRUD, then the AI feature — with testing after each step.

When the database connection broke, they used ODA: copied the exact error, diagnosed it as a missing env var, and asked Bolt to "only fix the Supabase connection string, don't touch other files."

### Contrast With

**Vibe coding vs. traditional development**: In traditional dev, you write the code and the tests. In vibe coding, AI writes the code and you write the spec + verify. The failure mode flips: traditional dev fails from implementation bugs; vibe coding fails from underspecified requirements. If your PRD is vague, the AI builds something that looks right but doesn't work.

**Vibe coding vs. one-shot generation**: One-shot means "build me a full app from this description." Vibe coding explicitly rejects this — it's iterative by design. One-shot works for trivial demos; anything with auth, state, or external APIs needs the incremental loop.

### Source Anchors

- Gen AI Mastermind Sessions 3 & 4 — video production pipeline and vibe coding methodology
- [[Gen AI Day - 1]] — prerequisite: LLM fundamentals that explain why prompt structure matters for code generation
- [[Gen AI Roadmap]] — Levels 3-5 build on these workflows
- [[MCPs]] — MCP section from this session explains how AI tools connect to external systems
