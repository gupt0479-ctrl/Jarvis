# remove-ai-slop

**Description:** Rewrite notes so they stop sounding AI-generated while preserving facts, links, and the user's actual meaning.

**Usage:** `/remove-ai-slop "path/to/note.md"` or `/remove-ai-slop` and then provide one or more note paths

---

## Instructions

When this skill is invoked:

### 1. Read the writing standard first

Before editing anything, read:

- `HUMAN_WRITING.md`
- `AGENTS.md`
- `40_Resources/Obsidian/Vault Operating System.md`

Treat `HUMAN_WRITING.md` as the canonical anti-slop contract.

### 2. Audit the target note

Look for:

- generic framing
- repeated points said in slightly different ways
- inflated transitions
- vague praise words with no mechanism
- summaries that sound smooth but teach nothing
- examples that could belong to any topic

Mark each suspect line mentally before rewriting.

### 3. Preserve what must survive

Do not damage:

- frontmatter
- wikilinks
- code blocks
- factual claims that are actually supported
- the note's real structure when it is already good

### 4. Rewrite by compression and grounding

For each slop-heavy paragraph:

1. delete filler
2. keep the factual core
3. replace abstraction with mechanism
4. replace generic examples with vault-specific examples when available
5. add a contrast, failure mode, or diagnostic question if that improves understanding

### 5. Preferred upgrades

If the note is still too floaty after cleanup, add one or more of:

- `## One-Line Answer`
- `## 30-Second Explanation`
- `## Teach It To A Beginner`
- `## Contrast With`
- `## Failure Modes`
- `## Diagnostic Questions`
- `## Understanding Proof`

Only add sections that genuinely improve the note.

### 6. Keep the result human

Target style:

- direct
- compressed
- specific
- useful on reread

Avoid:

- marketing tone
- fake confidence
- repetitive “why this matters” padding
- generic “in today's world” language

### 7. Report what changed

After rewriting, tell the user:

- which kinds of slop you removed
- whether you added any higher-signal sections
- any places where the underlying thought is still weak and needs real thinking, not just better prose

---

## Rewrite heuristics

### Kill these patterns on sight

- "This is important because it highlights..."
- "In today's rapidly evolving..."
- "This powerful framework..."
- "This comprehensive approach..."
- "It is crucial to understand..."

### Prefer these moves

- "This fails when..."
- "People confuse this with..."
- "In BOOM, this showed up when..."
- "The real tradeoff is..."
- "This matters only if..."

---

## Guardrails

- Never invent facts to make prose sound better.
- Never overwrite a raw clipping in `60_Claude/05_Clippings/`.
- If a note is weak because the thinking is weak, say so.
- Shorter is usually better if no meaning is lost.
