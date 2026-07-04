---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[AI Engineer Roadmap — roadmap.sh (web)]]"
source_url: 60_Claude/05_Clippings/PDFs/Road Map.pdf
source_note: "[[Road Map.pdf]]"
input_kind: pdf
track: ai
---
# AI Generalist Roadmap (Outskill) — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Road Map.pdf`
**Ingested:** 2026-07-04
**Pages:** 19 (slide deck)
## Source
A marketing/course slide deck from **Outskill** defining the "AI Generalist" and laying out a **6-level roadmap** with concepts, tools, and projects per level. Broader and less rigorous than the roadmap.sh AI Engineer roadmap — it spans image/video generation and no-code building alongside LLMs and agents.
## Key Claims
- ==AI Generalist = "a full-stack problem solver who has deep understanding of all AI models, knows which to use where and how, and can build solutions to complex problems using AI"== — a model-orchestrator, not a model-builder
- The framing hook is "AI will take 4 out of 5 jobs" (marketing hyperbole — no source)
- Everyone (entrepreneurs, working professionals, hustlers) "must master all 5 levels to win in the AI-first world"
- The four superpowers the levels grant: **Think with AI, Build with AI, Automate with AI, Network with AI**
## Full Content — the 6 levels
1. **Level 1–2: Foundations + Advanced Prompting/RAG/Fine-Tuning.** Concepts: LLM origins & how they process language, Generative AI applications, integrating AI with external tools, advanced prompting, RAG pipelines, prompt refinement/fine-tuning, ethics/safety. Tools: OpenAI, DeepSeek, DeepMind, NotebookLM, Perplexity, Hugging Face, Mistral, Predibase, Qwen2.5, Retell/VAPI/Millis (voice), Julius. Projects: system prompts, a RAG that summarizes your own docs, a voice assistant, a domain AI workflow (sales-training bot, AI HR), Claude Projects / Gemini Gems / Copilot agents.
2. **Level 3: AI for Image & Video Creation.** Concepts: diffusion science, Stable Diffusion + ComfyUI, style transfer & upscaling, fine-tuning diffusion, consistent characters, AI film/ad-making. Tools: ComfyUI, Stability, Flux.1, Kling, Luma, MiniMax, Hailuo, Civitai, Tencent Hunyuan, Janus Pro. Projects: an image/video-gen site (Leonardo-style), marketing collateral workflows, a faceless YouTube channel, a film, deepfake clones. *(The "money-making machine / deepfake clones" framing is where this deck leans into low-quality hustle content.)*
3. **Level 4: Automating Tasks with AI Agents.** Concepts: how automation works, designing an automatable process, agent orchestration, connecting agents into an "agent army." Tools: Make, Zapier, n8n, CrewAI, Lindy, **Relevance AI**. Projects: personal executive assistant, marketing/support/research agents, email manager, automatic job applier, appointment-booking voice agents.
4. **Level 5: Building with AI without code.** Concepts: connecting AI + no-code tools, no-code interfaces, design-thinking UI/UX, MVP with low-code + AI. Tools: Supabase, Vercel, Bubble, Cursor, Bolt, Lovable, Adalo, Framer, Dora, Jotform, bot9. Projects: no-code SaaS MVP + first 100 users, list on Product Hunt for perks/grants, solve a real startup problem.
5. **Level 6: Connect the dots** — a "bigger picture" collage of the full tool stack across all levels; projects: build a super-agent, build an app that solves a problem.
## Why It Matters
This is the **breadth-first, no-code-leaning counterpart** to the [[AI Engineer Roadmap — roadmap.sh (web)]]'s depth-first engineering path — useful mainly as a *tool inventory* (it surfaces the image/video and automation tools the engineering roadmap skips) and as confirmation that "which model where" orchestration is the meta-skill. For Anant specifically it's lower-signal than the engineering roadmap: he's on the CS/engineering track (the roadmap.sh path fits), and this deck's audience is non-technical hustlers, with several projects (deepfake clones, faceless YouTube, "money machine") that are off-strategy. The genuinely useful pull is the **Level 4 automation-tool list** (Make/Zapier/n8n/CrewAI/Relevance AI) — the same tools the [[Relevance AI — AI Agents for Sales & GTM (web)]] note covers — and the Level 3 creative-AI tool names, worth knowing exist. Signal caveat: course-marketing deck, unsourced "4 of 5 jobs" hook, hustle-culture projects — mine for tool names, ignore the pitch.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Road Map.pdf`
- [[AI Engineer Roadmap — roadmap.sh (web)]] — the rigorous engineering counterpart
- [[Relevance AI — AI Agents for Sales & GTM (web)]] — overlaps the Level 4 automation tools
## Open Questions
- [ ] Is any Level 3 creative-AI skill (ComfyUI, video gen) relevant to the Portfolio project, or off-track for the CS/engineering path?
- [ ] Do the Level 4 no-code automation tools (n8n/Make) belong in the stack, or does Claude Code + MCP already cover that ground?
## Flashcards
#cards/ai
How does the "AI Generalist" framing define the role?::A **full-stack problem solver** who understands all AI models, knows which to use where and how, and can build solutions — a model *orchestrator*, not a model builder.
How does the Outskill roadmap differ from the roadmap.sh AI Engineer roadmap?::It's **breadth-first and no-code-leaning** (adds image/video generation and no-code app building for a non-technical audience), vs roadmap.sh's **depth-first engineering** path (LLMs → RAG → agents → evals).
