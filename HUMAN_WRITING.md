# Human Writing Standard

This file is the writing contract for Jarvis. Any AI tool editing notes in this vault should read and follow it before drafting or rewriting Markdown.

## Voice here, structure in 30_Order

This file governs how prose should *sound*. It is one half of the writing standard. The other half — how a note is *shaped, filed, and which template it uses* — lives in `30_Order/`: read its `Templates/` and `Workflows/` before writing. For where each note type belongs, see [[40_Resources/Obsidian/Jarvis Vault Architecture]]. Voice without structure produces tidy notes in the wrong place; structure without voice produces slop in the right place. You need both.

## Objective

Write notes that sound like a sharp human who understands the material.

Do not write generic AI copy.
Do not inflate.
Do not smooth everything into the same tone.

The note should feel:

- specific
- grounded
- compressed
- honest about uncertainty
- useful when reread later

## The Core Test

Delete any sentence that could be pasted unchanged into a random productivity blog, AI newsletter, or study-hack page.

If a sentence survives only because it sounds polished, remove it.
If it survives because it carries a mechanism, example, contrast, or decision, keep it.

## What Good Notes Must Do

Each section should do at least one of these:

1. define the thing clearly
2. explain why it matters
3. show how it works
4. contrast it with a nearby concept
5. give a real example
6. record a failure mode or misconception
7. show where it was used
8. state what is still unclear

If a paragraph does none of these, it is probably filler.

## Anti-Slop Rules

### 1. Prefer concrete claims over polished framing

Bad:

- "This concept is incredibly important in today's fast-moving landscape."

Better:

- "This matters because the worker queue can fail in three different places and tracing shows which one broke."

### 2. Prefer mechanism over vibes

Bad:

- "RAG improves reliability and unlocks better performance."

Better:

- "RAG improves reliability only if retrieval actually surfaces relevant documents. Bad retrieval just feeds the model cleaner nonsense."

### 3. Prefer real context over generic examples

Use examples from:

- BOOM / UROP
- your courses
- your projects
- actual errors
- actual tradeoffs

### 4. Prefer contrast over isolated summary

Whenever possible, answer:

- what this is
- what it is not
- what people confuse it with

### 5. Prefer compression over repetition

Do not say the same point three ways unless the note is intentionally doing an explanation ladder.

### 6. Prefer plain language over inflated language

Avoid:

- transformative
- robust
- seamless
- leverage
- delve
- landscape
- journey
- unlock
- powerful
- comprehensive
- game-changer

These words are not banned forever, but they are suspicious. Use them only if they are the most accurate word, not the easiest polished word.

### 7. Keep uncertainty explicit

If something is inferred, say so.
If something is incomplete, say what is missing.
If the source is weak, say that too.

### 8. Do not write fake confidence

Never make a note sound finished if the underlying understanding is partial.

Good:

- "I understand the request flow, but I still need to verify why `BUILD-MAX-HEAP` is linear instead of `n log n`."

Bad:

- "This provides a complete framework for understanding heap construction."

## Preferred Note Moves

These are high-signal patterns for this vault:

- one-line answer
- 30-second explanation
- teach-it-to-a-beginner version
- contrast with
- failure modes
- diagnostic questions
- understanding proof
- source anchors

These force clarity better than generic summaries.

## Style Rules

- Use short paragraphs.
- Use bullets when comparing or listing.
- Use headings only when they help retrieval.
- Prefer direct verbs: "shows", "fails", "causes", "reveals", "depends on".
- Prefer ordinary words over corporate or academic padding.
- Keep transitions minimal.

## Voice Rules

Write like:

- a strong student who actually did the reading
- an engineer explaining what happened
- a researcher distinguishing what is known from what is guessed

Do not write like:

- a marketing page
- a LinkedIn post
- a generic study guide generator
- a chatbot trying to sound impressive

## Rewrite Procedure

When cleaning AI slop from an existing note:

1. preserve facts, links, and frontmatter
2. remove generic framing
3. collapse repeated claims
4. replace abstract praise with mechanism
5. add one concrete example if the note floats too much
6. add one contrast or misconception if the concept is easy to confuse
7. leave the note shorter or denser than before

## Vault Formatting Rules

These rules apply to all Markdown written in this vault. Voice rules above are about what you say; these rules are about how it sits on the page.

**Blank lines:**
- Zero blank lines between `---` (frontmatter close) and the `#` title
- Zero blank lines between any heading and its first content line
- Zero blank lines between consecutive list items or consecutive sections
- One blank line is permitted: after a callout (`> [!X]`) or blockquote (`> `) before a following paragraph of prose
- The vault's `headerspace.css` snippet handles visual spacing. Extra blank lines are not style — they are noise.

**Formatting markers** (`==`, `**`, `*`) carry SR cloze meaning — see [[Jarvis Writing and Formatting]] for the full pattern before using them.

## Final Check Before Saving
Ask:
1. Does this note contain actual information, or just smooth wording?
2. Could a smart human have written this after doing real work?
3. Does this note sound like this vault, or like the internet?
4. Did I preserve the user's actual meaning?
If the answer to any of these is no, rewrite again.
