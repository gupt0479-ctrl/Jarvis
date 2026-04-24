# distill-note

**Description:** Convert messy notes, conversation outputs, or raw captures into clean Obsidian-ready evergreen notes.

**Usage:** `/distill-note` (prompts for input) or provide note content directly

---

## Instructions

When this skill is invoked:

Before drafting, read:

- `AI_CONTEXT.md`
- `HUMAN_WRITING.md`
- `40_Resources/Obsidian/Vault Operating System.md`

### 1. Get Input

Ask the user:

- "Which note would you like me to distill?" (provide path)
- Or: "Paste the content you'd like distilled"

### 2. Analyze the Content

Identify:

- **Core concept** — What is this note fundamentally about?
- **Type** — `evergreen`, `concept`, `input`, `project`, `thought`
- **Key insights** — The 3-8 most important points
- **Gaps** — Missing definitions, unclear claims, unsupported assertions
- **Connections** — What existing notes this should link to

### 3. Search for Related Notes

Use MCP search to find:

- Existing notes on the same topic (avoid duplicates)
- Related concepts that should be linked
- Projects or contexts where this knowledge applies

### 4. Create or Update the Note

**If creating new:**

Place in appropriate location:
- `60_Claude/20_Distilled_Notes/` — General evergreen knowledge
- `40_Resources/CS/` — CS-specific concepts
- `40_Resources/CS/AI/` — AI/ML topics
- `20_Progress/` — If tied to active project

Use frontmatter template:

```yaml
---
type: evergreen        # or: concept, input
status: sprout         # seed → sprout → tree
created: YYYY-MM-DD
tags:
  - evergreen
notes:
  - "[[Related Note 1]]"
  - "[[Related Note 2]]"
next: "[[Next Action]]"  # optional
---
```

**If updating existing:**

- Preserve all existing frontmatter keys
- Add new `notes:` backlinks
- Update `updated:` date if key changes made
- Add content under appropriate headings

### 5. Structure the Content

Organize with clear headings:

```markdown
# [Clear Title]

## Definition

[One-sentence essence of the note]

## Key Insights

- [Insight 1]
- [Insight 2]
- [Insight 3]

## Explanation

[Main body — 2-5 paragraphs, concise and scannable]

## Examples

[Concrete examples if applicable]

## Connections

- [[Related Concept 1]] — how they relate
- [[Related Concept 2]] — contrast or complement

## Sources

- [[Source Note]] — if distilled from somewhere

## Open Questions

- [Question that needs answering]

## Next Actions

- [ ] [Action if applicable]
```

### 6. Suggest Improvements

After distilling, tell the user:

- What links were added
- What gaps remain
- What follow-up notes might be useful
- Whether this should be filed elsewhere

---

## Style Guidelines

- **Human voice** — Write like a person explaining to a person, not a textbook
- **Scannable** — Use headings, bullets, short paragraphs
- **Concrete** — Prefer examples over abstractions
- **Linked** — Every note should have 2+ backlinks
- **Actionable** — Include "Next Actions" or "Open Questions" where relevant

---

## Example Transformation

**Input (messy):**

> ok so the thing about RAG is it's like retrieval augmented generation and basically the idea is you don't just rely on the model's training you pull in external docs at query time which helps with hallucinations and keeps things grounded but you need good embeddings and a decent vector store otherwise retrieval sucks

**Output (distilled):**

```markdown
# Retrieval Augmented Generation (RAG)

## Definition

RAG enhances LLM responses by retrieving relevant external documents at query time, grounding answers in source material rather than relying solely on training data.

## Key Insights

- Reduces hallucinations by anchoring responses to retrieved documents
- Requires quality embeddings and vector storage for effective retrieval
- Sits between pure parametric knowledge and pure search

## How It Works

1. User asks a question
2. System embeds the query and searches vector store
3. Top-k relevant documents are retrieved
4. Documents are passed to LLM as context
5. LLM generates answer grounded in retrieved sources

## Connections

- [[Embeddings]] — how documents are represented for retrieval
- [[Vector Databases]] — where embeddings are stored
- [[Hallucination Mitigation]] — one of RAG's primary benefits

## Open Questions

- What's the optimal k value for retrieval in practice?
- How do you handle conflicting information in retrieved docs?
```
