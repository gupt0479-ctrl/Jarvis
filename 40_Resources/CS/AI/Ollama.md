---
type: concept
course: AI
status: sprout
mastery (1/10): 0
created: 2026-03-20
updated: 2026-04-24
topics: []
related:
  - "[[40_Resources/CS/Links|Links]]"
track:
  - ai
prerequisites:
  - "[[MCPs]]"
  - "[[AI Workflow]]"
used_in:
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
evidence: []
difficulty: 2
mastery_level: novice
enrichment_status: enriched
enrichment_level: standard
source_status: vault-grounded
---
# Ollama
## MOC
- [[AI Workflow]]
- [[Gen AI Roadmap]]
## Definition
- 
## Resources
- 
### How to use them
1. 
2. 
## Starting
2. The workflow I recommend for you: 
	You do **not** want one giant agent doing everything. You want a **layered setup**.
### Layer A - private local brain
Use Ollama for:
- indexing your folders
- reading your codebase
- generating architecture summaries
- generating prompts for Cursor
- analyzing private journals and notes
- extracting recurring problems, goals, and habits
### Layer B - coding hands
Use Cursor for:
- making actual edits
- running repo commands
- fixing lint/type errors
- implementing the prompt you prepared with Ollama
### Layer C - escalation
Use Claude Code only later, if you move to Pro or Max and decide it is worth it. Pro includes Claude Code; Max gives more usage than Pro.
### Layer D - optional personal assistant
Use OpenClaw onlwy for:
- messaging-style assistant workflows
- controlled tools
- later, maybe calendar/email/task automation
Do **not** start with OpenClaw as your main coding engine. On your hardware and current setup, it adds complexity before you need it.
## Models
### Cloud Models vs Local Models (Ollama)
Cloud Models (what we're using now):
- Run on remote servers (OpenAI's infrastructure)
- No local GPU/CPU requirements
- Always up-to-date with latest versions
- No local installation needed - you're connecting via API
- Better performance on complex reasoning tasks
- Requires internet connection
- Usage may have costs/limit
Local Models (Ollama):
- Run entirely on your machine
- Work offline
- Your data never leaves your computer
- Performance depends on your hardware
- You manage updates yourself
- Free to use indefinitely
- May be less capable than frontier models
## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)

## Jarvis Enrichment

### Precise Definition

Ollama is a local model runtime: it lets you download, run, and call open-weight language and embedding models from your own machine through a local CLI or HTTP API.

The key word is **runtime**. Ollama is not the model itself, not a second brain by itself, and not a replacement for Obsidian. It is the local engine Jarvis can use for private extraction, embeddings, structured outputs, and cheap first-pass summarization.

### Mechanism

The normal Ollama loop is:

1. pull a model onto the machine
2. send text to the local Ollama service
3. receive generated text or embeddings
4. store the result somewhere useful, such as a Markdown note, SQLite index, or vector store

For Jarvis, the most useful pattern is not "chat with Ollama." It is:

```text
vault note -> local extraction -> structured JSON -> append-safe enrichment -> dashboard queue
```

That keeps private notes local while still letting stronger cloud models handle harder synthesis when needed.

### Why It Matters

Ollama is useful in Jarvis because many second-brain tasks are repetitive and privacy-sensitive:

- classify note type
- detect missing sections
- extract entities and concepts
- generate embeddings for semantic search
- draft quick definitions before a critic pass
- summarize private notes without uploading them

Those jobs do not always need a frontier model. They need consistency, low cost, and local access.

### Concrete Example From This Vault

The [[Jarvis Enrichment Engine]] can use Ollama as the first pass for notes like [[OCaml]] or [[Time Complexity]]:

- extract existing definitions
- identify missing headings
- propose prerequisite links
- generate 3 diagnostic questions
- leave the final enrichment for a stronger model or human review

This is different from asking Ollama to rewrite the note. The output should be structured and reviewable.

### Contrast With

- **Ollama vs ChatGPT/Claude**: Ollama runs local models; ChatGPT/Claude run hosted frontier models. Local is better for privacy and cheap repetition. Hosted is usually better for hard reasoning and polished synthesis.
- **Ollama vs Obsidian**: Obsidian stores and links knowledge. Ollama computes over that knowledge.
- **Ollama vs MCP**: MCP is a tool protocol. Ollama is a model runtime that can sit behind a tool.

### Failure Modes / Misconceptions

- Local does not automatically mean better. Smaller local models can hallucinate or miss nuance.
- A local model still needs source anchors. Privacy does not replace evidence.
- Running Ollama does not create a second brain. The useful part is the pipeline around it.
- Hardware limits matter. Long notes, large models, and embeddings can become slow.

### Diagnostic Questions

- Which Jarvis tasks need privacy more than frontier-level reasoning?
- Which tasks should produce structured JSON instead of prose?
- When should Jarvis escalate from Ollama to a stronger cloud model?

### Source Anchors

- [[AI Workflow]] - tool-lane model for Claude, ChatGPT, Cursor, and Codex.
- [[MCPs]] - shows how local tools can become callable by agents.
- [[Jarvis Enrichment Engine]] - defines where local extraction fits in the enrichment pipeline.

### Drill Cards

#cards/ai

- Ollama::A local runtime for running open-weight models and embeddings on your own machine.
- Best Jarvis use for Ollama::Private, repetitive first-pass extraction and semantic indexing.
- Ollama vs Obsidian::Ollama computes over knowledge; Obsidian stores and links it.

### Understanding Proof

- I can explain why Ollama is a runtime, not the second brain itself.
- I can name one Jarvis workflow that should stay local and one that should escalate to a stronger cloud model.
- I can design an Ollama task that returns structured data instead of vague prose.
