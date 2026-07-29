---
type: class
input_kind: project
status: seed
created:
updated:
area:
tags:
  - "#class"
next:
---
# 

## Overview
- 
## Plan
- [ ] Break down tasks
- [ ] Solve core
- [ ] Writeup/tests
- [ ] Submit
## Work log
### What to build
The better move is: **do not build a chatbot. Build an AI proof system.**
1. **The Big Idea**: Build something I’d call **Portfolio ProofOS** or **AI Case File**.
	Instead of a visitor asking “Tell me about Anant,” they can paste a job description, click a project, hover a skill, or challenge a claim, and the site generates a live, visual case file:
	- “Is Anant a fit for this role?”
	- “Prove he can build AI products.”
	- “Show me the strongest evidence for full-stack/product/AI ability.”
	- “What would he build for my startup?”
	- “Where is he weak, and what evidence is missing?”
	The response should not be a paragraph. It should become UI:
	- fit score
	- cited evidence cards
	- highlighted sections on the page
	- project graph
	- timeline of proof
	- skill-to-project links
	- “why this matched”
	- gaps and counterarguments
	- downloadable/interview-ready proof pack
	That is much more impressive than a bot because the AI is not pretending to be you. It is **operating your portfolio as an evidence engine**.
2. **Why This Is The Right Direction**: Current AI interface work is moving beyond chat into **generative UI**, where AI selects or fills real interface components instead of returning plain markdown. Vercel described this as moving beyond plaintext chatbot responses into rich component-based interfaces. AG-UI describes the same broader pattern: agents streaming state, UI intents, tool calls, intermediate steps, and custom events into user-facing apps.
	For your portfolio, that means the AI should not say: “Anant has experience with Next.js and AI.”
	It should render:
	- 3 project cards proving Next.js depth
	- 2 technical decisions from those projects
	- a confidence meter
	- source links
	- an architecture mini-diagram
	- “missing evidence” if your data does not support the claim
	That feels credible and advanced.
3. **Best Implementation**
	My recommendation:
	1. **Remove OpenAI ChatKit completely.**: It anchors the product in “generic chatbot” land.
	2. **Keep Sanity and your local data folder.**: Sanity becomes the CMS. Your local data becomes the editable fallback. But enrich the data around proof, not just display content.
	3. **Create an AI evidence index.**: Each project, skill, experience, education item, blog post, and achievement becomes a small evidence chunk with tags, dates, confidence, source, and proof text.
	4. **Build a client-side retrieval engine.**: Start with keyword/BM25-style search. Add embeddings later. For a small portfolio, this is fast, free, and reliable.
	5. **Build a visual AI Lab UI.**: Not chat bubbles. Use modes:
	   - **Recruiter Lens:** paste job description, get fit case file.
	   - **Builder Lens:** click a project, get architecture/deep technical breakdown.
	   - **Skeptic Lens:** challenge a claim and force the site to prove it.
	   - **Founder Lens:** “what would Anant build for my idea?” with evidence-based pitch.
	1. **Optional wow layer: browser-local AI.**: Use WebLLM or Transformers.js only as progressive enhancement. WebLLM runs LLMs directly in the browser with WebGPU and no server inference. Transformers.js supports browser ML tasks including embeddings and feature extraction. But do not make this required for V1; model downloads and device support can hurt UX.
4. **The Astonishing Interaction**: The killer feature should be:
> A recruiter pastes a job description. The site transforms itself into a personalized proof dossier in 2 seconds.

It highlights relevant projects on the page, generates a “why me” proof pack, shows exact evidence, admits gaps, and gives the visitor a clean summary. That is memorable because it demonstrates AI, product thinking, information architecture, retrieval, UX, and engineering discipline at once.
**What I Would Avoid**: Do not build:
- an AI avatar
- a “talk to my AI twin” clone
- uncited free-form answers
- mandatory WebLLM on first load
- a fake agent that only talks
- a chatbot that answers “What are your hobbies?”
Build something that **acts on structured portfolio knowledge**.
**Research Signals**: Useful current references:
- [Vercel Generative UI](https://vercel.com/blog/ai-sdk-3-generative-ui): moving past markdown chat into component-based AI interfaces.
- [AG-UI](https://docs.ag-ui.com/introduction): agent-user interaction protocol for state, UI intents, tool rendering, and interactive agent UX.
- [Chrome WebMCP](https://developer.chrome.com/blog/webmcp-epp): 2026 direction for making websites agent-ready with structured tools.
- [WebLLM docs](https://webllm.mlc.ai/docs/index.html): browser-side LLM inference with WebGPU.
- [Transformers.js](https://huggingface.co/docs/transformers.js/en/index): browser/server ML, embeddings, search, summarization, and classification.
- [Fastfolio](https://www.fastfol.io/) and [FantasticPortfolios](https://fantasticportfolios.com/): examples showing that “AI portfolio answers questions” is already becoming commodity.
My strong take: **your portfolio should not contain an AI feature. Your portfolio should itself become an AI product demo.**
### 

## Concepts used
- [[Concept - ...]]
- [[Concept - ...]]
## Post-submit reflection
- What failed first?
- What pattern repeats?