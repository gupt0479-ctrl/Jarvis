---
type: concept
status: seed
created: 2026-02-20
updated: 2026-07-27
related_progress:
  - "[[Gen AI Day - 2]]"
  - "[[Gen AI Day - 1]]"
  - "[[Chat Gpt Prompts]]"
  - "[[UMN Workflow]]"
tags:
  - concept
next: "[[Gen AI Meeting]]"
track:
  - ai
prerequisites: []
used_in: []
evidence: []
difficulty: 1
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-16
drill_interval: 21
---
# Gen AI Roadmap
## Definition
- This note is the “after-course plan” that combines:
	- The 5-level roadmap deck (AI generalist plan)
	- What was taught in sessions 1–4
	- What to build to prove skills (projects list)
## Levels
### Level 1: Foundations of AI + Language Models
- Learn:
	- What AI vs Generative AI is
	- Where LLMs came from + how they process language
	- LLM mechanics (tokenization, embeddings, attention)
- Projects:
	- Create system prompts
	- Create Claude Projects / Gemini Gems (custom assistants)
### Level 2: Advanced prompting + retrieval + refining prompts
- Learn:
	- Advanced prompting methods
	- Retrieval concepts (RAG)
	- Prompt refining + fine-tuning (conceptual)
	- Integrating AI with external tools
- Projects:
	- Build a RAG system that summarizes your documents
	- Build a voice assistant using advanced prompting
	- Build copilot agents
	- Build one AI workflow for your own problem statement (ex: training bot, HR bot).
### Level 3: AI for image + video creation
- Learn:
	- Diffusion science
	- Stable Diffusion + ComfyUI basics
	- Style transfer + upscaling
	- Video creation + ad filmmaking using AI
- Projects:
	- Build an image/video creation site (Leonardo-style)
	- Create marketing collateral workflows
	- Set up a faceless YouTube workflow with AI
	- Develop a film using AI
	- Create deepfake clones (be careful with safety/legal)
### Level 4: Automations + AI agents
- Learn:
	- How automation works
	- How to define an automatable process
	- Setting up automations
	- Understanding agents + orchestration
	- Connecting multiple agents (“agent army”)
- Projects:
	- Personal executive assistant
	- Email manager
	- Automatic job applier
	- Voice agents that can speak and book appointments
	- Automations for daily tasks (email, writing, blogs)
### Level 5: Building AI-powered applications
- Learn:
	- Connect AI + no-code tools for automations
	- No-code interfaces
	- UI/UX design thinking
	- Build MVP using low code + AI
- Projects:
	- Apps like: data processor, image generators, travel planners
	- Deploy an app that works on mobile
	- List on Product Hunt for perks/grants
## Recommended build sequence (minimum proof)
1. System prompt + assistant prompt (markdown structure)
2. Custom GPT or Gem that uses your prompt + knowledge
3. One automation (Make/Zapier): trigger → AI step → saved output
4. One vibe-coded app: CRUD + 1 AI feature
5. One AI video ad: brief → storyboard → assets → edit
## Weekly schedule (starter)
### Week 1: Level 1 basics
- LLM 5-step mental model + prompt basics
- Create 10 reusable prompts + 1 markdown “default assistant”
### Week 2: Level 2 prompting + retrieval concept
- Build a “notes search” concept (RAG-style) using your own docs (prototype)
### Week 3: Level 3 content build
- Produce one 15–30s ad using the full workflow (Session 3)
### Week 4: Level 4 automations + agent thinking
- Ship one automation + one “agent plan” doc (permissions + actions)
### Week 5: Level 5 app build
- Ship a small app demo (vibe coding) + documentation + portfolio writeup

---

## Deep Dive

### One-Sentence Version

A 5-level progression from LLM fundamentals through prompting, content creation, automations, and app building — each level has a concrete project that proves the skill, not just reading about it.

### What It Is

The roadmap is a structured learning path from the Gen AI Mastermind course, organized as 5 levels with increasing complexity:

- **Level 1** (Foundations): How LLMs work + prompt basics → build system prompts and custom assistants
- **Level 2** (Advanced prompting + RAG): Retrieval concepts, prompt refinement → build a RAG system and copilot agents
- **Level 3** (Content creation): Diffusion models, image/video pipelines → produce AI-generated video ads
- **Level 4** (Automations + agents): Process automation, agent orchestration → build personal assistant workflows
- **Level 5** (App building): No-code/low-code + AI features → ship a deployed MVP

Each level has a "minimum proof" project. The roadmap is useless without the projects — the levels are just categories, the projects are the actual learning.

### Why It Matters

- It sequences AI skills in dependency order: you can't build a RAG system (Level 2) without understanding embeddings (Level 1), and you can't orchestrate agents (Level 4) without understanding tool connections (Level 2-3).
- The weekly schedule (5 weeks, one level per week) is aggressive but gives a concrete timeline instead of open-ended "learn AI."
- For this vault specifically, the roadmap feeds directly into the `ai` track — each level maps to concepts that should become tracked, drilled, and eventually proven through outputs.

### Real Example

The recommended build sequence from the course: (1) system prompt + assistant prompt, (2) custom GPT using your prompt + knowledge, (3) one automation with Make/Zapier, (4) one vibe-coded app with CRUD + AI feature, (5) one AI video ad. Each artifact is small enough to finish in a week but concrete enough to demonstrate the skill.

### Contrast With

**Roadmap vs. tutorial collection**: A tutorial collection is unordered — you pick whatever looks interesting. This roadmap is sequenced with dependencies. Skipping Level 1 and jumping to Level 4 (agents) means you won't understand why your agent's tool calls fail, because you never learned how the model processes structured prompts.

**This roadmap vs. a university ML curriculum**: A university curriculum goes deep on math (linear algebra, probability, optimization) before touching applications. This roadmap is application-first — you build things immediately and learn theory as needed. The tradeoff: you ship faster but may lack the mathematical foundation to debug novel model behavior.

### Source Anchors

- Gen AI Mastermind course — 5-level deck and sessions 1-4
- [[Gen AI Day - 1]] — Level 1 content (LLM mechanics, prompting)
- [[Gen AI Day - 2]] — Levels 3-4 content (video workflow, vibe coding, MCP, automations)
- [[AI Workflow]] — implementation plan that operationalizes this roadmap into daily tool usage
