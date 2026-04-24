---
type: concept
course: AI
status: seed
mastery (1/10): 0
created: 2026-02-15
updated: 2026-07-27
topics:
  - "[[Gen AI Day - 2]]"
  - "[[Chat Gpt Prompts]]"
related:
  - "[[Gen AI Meeting]]"
tags:
  - concept
track:
  - ai
prerequisites: []
used_in: []
evidence: []
difficulty: 2
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-09
drill_interval: 14
---
# Day - 1
## MOC
- [[Chat Gpt Prompts]]: Obsidian Prompts and basics of prompting
- [[Gen AI Day - 2]]: Day 2 (sessions 3 & 4)
- [[Gen AI Meeting]]: Main file (resources + how to use)
- [[Gen AI Roadmap]]: Full plan after course
## Definition
- Day 1 focus: (Session 1 + Session 2)
	- Understand how LLMs work (5-step model) so prompting makes sense
	- Learn prompt engineering structure (Magic Prompt Formula + markdown prompting)
	- Build Custom GPTs (simple → advanced) + Content DNA workflow
## Meeting notes
- Level 1: AI Fundamentals [[Gen AI Meeting#Meeting notes|Overview]]
	- How LLMs work (tokenization → embeddings → self-attention → prediction → output) [[Gen AI Day - 1#Detailed explanations]]
	- Magic Prompt Formula (98% tasks) [[Gen AI Day - 1#Magic Prompt Formula]]
	- Prompting techniques list (zero-shot, few-shot, CoT, ToT, meta prompting, prompt chaining) [[Gen AI Day - 1#Prompting foundations you’ll use daily]]
- Level 2 (preview on Day 1): assistants + tool usage [[Gen AI Meeting#How to use them|Tools]]
	- Custom GPTs (GPT marketplace + builder) [[Gen AI Day - 1#Custom GPTs (GPT Marketplace)]]
	- Markdown prompting for advanced assistants [[Gen AI Day - 1#Markdown Prompting]]
	- Content DNA workflow (style replication) [[Gen AI Day - 1#Content DNA workflow]]
- The main habit to build: write one reusable prompt, then reuse it across tools (ChatGPT / Gemini Gems / Claude projects) [[Gen AI Day - 1#Markdown Prompting|Reusable Prompts]]
	- The “repeatable workflow” they demonstrated:
		- Extract your style (Content DNA) → convert to markdown prompt → paste into assistant instructions → attach knowledge → test → refine
- The “tool stack” idea:
	- Model (ChatGPT/Claude/Gemini) + automation (Make/Zapier/n8n) + tool connectors (MCP) + optional local model (Ollama)
**Career Impact Discussion:**
- How AI affects different career stages (entrepreneurs, consultants, workers)
- The rise of AI generalists and the consulting opportunity for SMEs
- Future business landscape with AI-first companies
### AI Fundamentals
#### Detailed explanations
**LLM = Large Language Model**: a model trained to predict the next token. 
*How LLMs work (5-step model)*:
1. **Tokens**: chunks of text (often parts of words). Costs/limits are measured in tokens.
	- Why:
		- Computers operate on numbers; tokens map text to ids
		- Usage/cost is tied to tokens  
	- *Rule of thumb mentioned*: ~100 tokens ≈ ~75 words (rough estimate)
	- **Why it feels “smart”**: it’s good at pattern completion, instruction-following, and summarizing/rewriting—especially when you provide context and constraints.
> [!TIP] Tips for implementation: When you test any model output, always ask: “What assumptions did you make?” then correct it.
2. **Embeddings**
	- Token ids → *long numeric vectors* (meaning representation)
	- Meaning comes from training patterns: words used in similar contexts end up close (similarity)  
	- *Examples used*:
		- “apple” can cluster with fruit words or brand/tech words depending on context  
		- “bank” (river vs finance) shows how context picks different meaning vectors
3. **Self-attention** 
	- The model weighs which words in the input matter most while generating output.
    - This is why prompt structure (headers, bullets, constraints) improves results.
    - *Example idea*:
		- Adding “explain like I’m 5” changes what the model focuses on and changes the style/complexity of output.
4. **Next-token prediction**
	- Model assigns probability across many possible next tokens, then picks among high-probability options (not always the top one)
	- This is why outputs vary even with the same question
5. **Output generation**  
	- Repeats prediction token-by-token until it finishes the response
> [!TIP] Day 1 check: after any answer, ask: “What assumptions did you make?” (then correct them)
#### Prompting foundations you’ll use daily
1. Brief summary: You’ll build a _prompt library_ for repeat tasks (emails, summaries, research, coding help).
2. Detailed explanations The Session 1 workbook has you:
	 - Zero-shot: no examples
	- Few-shot: include a few examples
	- Chain-of-thought: break into steps (useful for complex tasks)
	- Tree-of-thought: explore multiple paths before choosing
	- Meta prompting: ask AI to generate the prompt or strategy
	- Prompt chaining: step outputs feed into next step
#### Gemini Gem style workflow
You can create a reusable assistant by generating a detailed prompt, converting it to markdown, then pasting it into a “Gem” manager.
1. Detailed explanations: The custom GPT / Gemini workflow shown in the workbook is:
	1. ask ChatGPT for a detailed prompt,
	2. rewrite it in markdown + code block so formatting doesn’t break,
	3. go to Gemini → Gem Manager → New Gem → paste instructions → test.
Make 2 assistants:
2. **Study Buddy Gem**: turns any PDF/notes into: key terms, mini quiz, mistakes to avoid.
3. **Portfolio Writer Gem**: turns project bullets into a polished README + resume bullets.
### Custom GPTs (GPT Marketplace)
#### GPT Marketplace
- “Explore GPTs” shows many GPT apps made by others
- You can search by task (ex: email writer) and test behavior quickly
#### Build a simple GPT in the GPT Builder
- Create GPT → describe what it should do → builder asks clarifying questions → you test in preview → keep refining  
- The “app behavior” is powered by the saved Instructions in Configure
#### Configure tab = heart of the GPT
- Configure → Instructions contains the full prompt that defines behavior
- The builder converts your chat feedback into a prompt automatically (useful for quick prototypes)
### Magic Prompt Formula
The **Magic Prompt Formula** is a structured prompting technique that works for most AI tasks. It consists of **4-6 key components**: **Role → Task → Context → Format** (+ optional data + rules).
**Core Components:**
1. **Role/Persona** - Define who the AI should act as (e.g., "You are an experienced email copywriter who has written for brands like Ogilvy")
2. **Task** - Clearly state what you want the AI to do
3. **Context** - Provide relevant background information, environment, and conditions
4. **Format** - Specify how you want the output structured (e.g., bullet points, table, paragraph)
**Optional Components:**
5. **Data** - Include any specific information needed
6. **Instructions/Goals** - Specify how the task should be completed
**Why It Works:**
The formula leverages self-attention, so the model focuses on the most important parts of your input. More context + clear output rules reduces generic filler.
**Example Application:**
Instead of asking "Draft an email to invite subscribers to Gen AI Workshop," a better prompt would include:
- Role: "You are an experienced email copywriter..."
- Context: "Workshop is for marketing, tech, and product professionals..."
- Task: "Create an engaging invitation email..."
- Format: "Include subject line, key benefits, and clear call-to-action".
### Markdown Prompting
Markdown prompting is a structured prompt format for assistants you’ll reuse (Custom GPT, Gemini Gem, agent tools). Core blocks: **Role, Objective, Context, Instructions, Notes**.
**Core Structure:**
**Markdown Elements Used:**
- **Headers** - Use `#` for main headings, `##` for subheadings, `###` for sub-sections
- **Bold text** - Wrap words with `**word**` for emphasis
- **Bullet points** - For lists of capabilities or rules
- **Code blocks** - For examples or specific formatting
**Why It Works:**
Markdown creates hierarchy. The model “sees” what’s important and what’s detail.
**Key Benefits:**
- **Better Organization** - Clear sections reduce missed instructions
- **Improved AI Understanding** - Easier to follow multi-step rules
- **Easier Maintenance** - Update one section without rewriting everything
### Content DNA workflow
The problem it solves
- “Write like me” is too vague
- You need a style report first
#### The workflow shown
1. Collect 10–20 past posts/writing
2. Ask AI to analyze patterns (tone, structure, hooks, CTAs, vocab, rhythm)
3. Convert analysis into a reusable prompt (markdown)
4. Paste into Custom GPT / Gemini Gem / Claude Project instructions
5. Test on a topic → refine → save as your “style engine”
### Productivity toolkit (mentioned in sessions)
- Whisper Flow for voice-to-text capture (faster input)
- Perplexity for citation-backed research
- Fireflies/Otter for transcript capture + summaries

## Flashcards (best 3–8)


---

## Deep Dive

### One-Sentence Version

An LLM predicts the next token by converting text into numeric vectors (embeddings), weighting which tokens matter most (self-attention), and sampling from a probability distribution — it does not "understand" anything, it pattern-matches at scale.

### What It Is

The 5-step model from Session 1 is the clearest mental model for how LLMs work:

1. **Tokenization** — text splits into subword chunks mapped to integer IDs. Costs and context limits are measured in tokens, not words (~100 tokens ≈ 75 words).
2. **Embeddings** — token IDs become high-dimensional vectors. Words used in similar contexts cluster together. "Bank" near "river" gets a different vector than "bank" near "finance."
3. **Self-attention** — the model assigns weights to decide which input tokens matter most for generating the current output token. This is why prompt structure (headers, bullets, constraints) changes output quality.
4. **Next-token prediction** — the model computes a probability distribution over all possible next tokens and samples from it. This is why the same prompt can produce different outputs.
5. **Output generation** — repeat step 4 token by token until the response is complete.

The model does not retrieve facts from a database. It reconstructs plausible continuations from patterns learned during training. This is why it can be confidently wrong.

### Why It Matters

- Understanding the 5-step pipeline explains *why* prompt engineering works: you're shaping what self-attention focuses on.
- It explains *why* LLMs hallucinate: next-token prediction optimizes for plausibility, not truth.
- It explains *why* temperature matters: higher temperature flattens the probability distribution (more variety), lower temperature sharpens it (more predictable).
- If you don't understand this pipeline, you'll treat the model as a search engine and get frustrated when it invents things.

### Real Example

From the Gen AI Mastermind course: when you add "explain like I'm 5" to a prompt, self-attention shifts weight toward simpler vocabulary and shorter sentences. The model doesn't "decide" to simplify — the attention weights change which token patterns get activated, and simpler patterns win.

Another example: the Magic Prompt Formula (Role → Task → Context → Format) works because each section gives self-attention distinct anchors to weight. Without structure, the model spreads attention across a flat blob of text and produces generic output.

### Contrast With

**LLMs vs. search engines**: A search engine retrieves existing documents that match a query. An LLM generates new text by predicting tokens. Search can't produce novel combinations; LLMs can't guarantee factual accuracy. RAG tries to bridge this gap by feeding retrieved documents into the LLM's context.

**LLMs vs. traditional NLP**: Older NLP systems (rule-based parsers, bag-of-words classifiers) operated on hand-crafted features. LLMs learn features from data via self-attention. The tradeoff: LLMs are far more flexible but far less interpretable — you can't inspect why a specific token was chosen the way you could trace a rule-based parse.

### Source Anchors

- Gen AI Mastermind Session 1 — the 5-step LLM mental model (tokenization → embeddings → self-attention → prediction → output)
- [[Gen AI Day - 2]] — builds on this with MCP and vibe coding applications
- [[Gen AI Roadmap]] — Level 1 foundations map directly to this note
- [[Chat Gpt Prompts]] — prompt patterns that exploit the attention mechanism described here
