---
type: evergreen
status: sprout
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - ai-agents
  - writing
  - philosophy
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[Note Writing System — Audit and Roadmap (2026-05-31)]]"
  - "[[Jarvis Writing and Formatting]]"
---
# Why We Write Notes
==A note in Jarvis exists to be retrieved, reused, reviewed, or to support a decision later — not to record that something was read.== This document answers the question every other rule assumes you have already answered: *should this become a note at all, and if so, for whom?* Read it before [[Vault Rules — Complete AI Ruleset]] tells you *how* — this tells you *whether* and *why*.
The vault is not an archive of everything encountered. It is a working memory with a retrieval cost: every note added is a note that future search, dashboards, and review must wade through. A note that no one will ever retrieve is not free — it is noise that hides the signal. So the bar is not "is this true?" but "will future-Anant or a future agent need this to surface?"
## Section 1 — The Use Case Test
A piece of information becomes a note only if it passes **at least one** of these five tests. If it fails all five, it stays in `60_Claude/05_Clippings/` as raw source and does not become a note.
1. **Future retrieval:** will future-Anant search for this and need it to appear? *If yes, it needs a precise title, headings, and wikilinks so search and backlinks find it.*
2. **Transfer:** does this mechanism show up in a different context — course → interview, project → portfolio, one class → another? *If yes, it belongs as a distilled concept, not buried in one source summary.*
3. **Review:** is this a concept worth practicing by spaced repetition? *If yes, it earns flashcards — but only after it is distilled, never straight from raw source.*
4. **Decision support:** is this a decision Anant will revisit, and does the note capture *why* a choice was made, not just what? *If yes, record the reasoning and the alternatives rejected.*
5. **Action:** is this a task, next step, or open question that must be tracked? *If yes, it is a `- [ ]` task or a `next:` field, not a paragraph.*
> [!TIP]
> The test is "which reader needs this and when," not "is this interesting." Interesting-but-unretrievable belongs in clippings, not in a note.

## Section 2 — The Reader Model
Every note has a specific intended reader. Write for that reader, not for the satisfaction of having captured something. A note that serves no named reader is the most common failure in this vault.
- **Future-Anant (3 months out):** needs the *mechanism*, not a summary. Needs to know what he was confused about, what he understood, and what he still does not know. A note that hides uncertainty behind confident prose lies to this reader. See [[HUMAN_WRITING]] on keeping uncertainty explicit.
- **Future AI agent:** needs structured frontmatter, verified wikilinks, and plugin-compatible syntax it can pattern-match. A broken `notes:` link or a duplicate YAML key corrupts what this reader relies on.
- **Spaced Repetition:** needs one well-formed question per card with a mechanism-based answer. Label trivia (`RAG stands for::Retrieval Augmented Generation`) wastes this reader's review time. See [[Spaced Repetition and Learning Loops]].
- **Dataview:** needs clean, consistent frontmatter fields matching what the dashboard queries. A note with `type:` missing is invisible to this reader. See [[Dataview and Dashboards]].
- **Obsidian graph / backlinks:** needs meaningful wikilinks that reflect real relationships, not reflexive linking of every keyword.
## Section 3 — Note Types and Their Purpose
Each type answers one question and produces one thing. The decisive column is *when to extend instead of create* — most duplication in this vault comes from creating a new note where extending the canonical one was correct.
| Note type | Question it answers | When to create | When to extend |
|---|---|---|---|
| Source summary (`input`) | What did this source say, and what is worth keeping? | Once per source, when the source is worth keeping | Never — source summaries are fixed captures of one source |
| Distilled note (`evergreen`) | What is the mechanism behind this concept? | When the concept recurs across multiple sources or contexts | When new evidence, examples, or contrasts arrive |
| Concept note (`concept`) | What does this term mean, how does it work, what breaks it? | When a concept recurs in coursework and will appear again | As mastery grows or examples accumulate |
| Project note (`project`) | What is the current state and next action for this work? | When a project starts | At every meaningful milestone (append to `## Log`, update `next:`) |
| Flashcard set | What must I recall on demand? | Only after distillation; never from raw source | When a new card is sharper than an old one |
| Review note (`review`) | What happened this period, what must change? | Periodically via Periodic Notes | Never — each period gets a fresh review |
## Section 4 — The Compression Hierarchy
Information moves through four stages, each compressing further and serving a different reader:
```
Raw source        →  Source summary   →  Distilled note   →  Flashcard
(05_Clippings)       (10_Source_Sum.)    (20_Distilled)      (#cards)
verbatim, audit      what one source     the mechanism       one recallable
trail                said, compressed    across sources      distinction
```
The rule: **each step earns the next.** A flashcard made directly from a raw clipping skips the two compressions that make it answerable — the result is a card that tests a fragment no one understands. An agent that jumps from PDF to flashcards has not done the work that makes the card meaningful. This is why card creation from `05_Clippings/` is forbidden in [[Vault Rules — Complete AI Ruleset]].
## Section 5 — What Makes a Note Fail
These are the concrete failure modes, drawn from the real errors in [[Note Writing System — Audit and Roadmap (2026-05-31)]]. Each names what the note looks like when it fails a test above.
- **Captures everything, compresses nothing.** The Quant Foundations note captured ~40% of the source and still read as a transcript dump — failing both retrieval (too long to reread) and the compression hierarchy. The note should *replace* the source; if reopening the original reveals anything new, the note is incomplete.
- **No wikilinks.** A note with no links is invisible: backlinks, the graph, and Dataview never surface it. It fails the future-retrieval and graph readers at once.
- **Vague or broken frontmatter.** The trial note had a duplicate `notes:` key (YAML silently kept the last, dropping the first) and six wikilinks to files that did not exist. Both corrupt the AI-agent and Dataview readers silently — no error, just missing data.
- **Fake confidence.** A note that sounds finished but rests on partial understanding misleads future-Anant and any reviewer. Say what is inferred and what is still unverified, as [[HUMAN_WRITING]] requires.
- **No flashcards on a reviewable concept.** All the distillation work is done, but nothing is retained — the review reader gets nothing. Conversely, flashcards on un-distilled material fail the same reader with noise.
- **Written without reading the vault first.** The trial note invented formatting conventions because the agent did not read the MGMT 3001 notes first. The result was inconsistent with every real note. The fix is mechanical: read 3–5 existing notes in the same category before writing — see [[Vault Rules — Complete AI Ruleset]] Part 1.
## The One-Line Decision
Before writing, ask: *which named reader needs this, and through which retrieval path will they find it?* If you cannot answer both, the information is not a note yet — it is raw source, and it stays in `60_Claude/05_Clippings/`.
