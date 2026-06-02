---
type: evergreen
status: sprout
created: 2026-06-01
updated: 2026-06-01
tags:
  - system
  - standards
notes:
  - "[[Concept Template]]"
  - "[[Summary to Distilled]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[HUMAN_WRITING]]"
---
# Concept Standard
==A concept note answers four questions in order — what is it, how does it work, what is it not, where has it shown up — and earns its keep on the third and fourth.==
This is the content standard for `concept` notes: course concepts and definitions that recur and will appear again on an exam, in an interview, or in another course. A summary records what a source said; a concept note records what *you* understand and can use. The decisive sections are the contrast and the failure modes — a concept with only a definition is a flashcard, not a note.
## Maps To
- Template: [[Concept Template]]
## Used By Workflow
- [[Summary to Distilled]] — concepts promoted out of source summaries are written here; course concepts are also created directly in Obsidian via the folder template. Read this Standard before writing either way.
## Per-Heading Standard
### Frontmatter
`type: concept`, `status: sprout`, `course` and `track` set, `mastery_level: 0` (0–10 integer — not the old `mastery (1/10)` string key), and the relational fields `prerequisites:`, `used_in:`, `evidence:` as wikilink lists (empty `[]` until real). `tags: [concept]`.
> [!WARNING]
> Reusing the invalid `mastery (1/10):` key (a parenthesis in a YAML key), or filling `evidence:` with notes that do not exist. Keep relational fields empty rather than fake.
### One-Line Answer
The concept in a single sentence, as you would say it to a peer. This is the `==highlight==` anchor for the note.
*Density:* one sentence, wrapped in `==...==`.
> [!WARNING]
> A textbook definition copied verbatim, or two sentences. "A team is a group with interdependent work, shared goals, and mutual accountability" — peer-level, not dictionary-level.
### Mechanism
**How** it works, not just what it is. Bold named sub-concepts. Use `$...$` for any notation and explain each symbol in prose.
*Density:* the core of the note — enough to actually use the concept. Break into the concept's natural parts (the Teams note uses the **IPO** breakdown: Inputs → States → Processes → Outputs).
*Plugins:* `**bold**` on each named part; `*Label:*` for sub-group intros; callouts only where a real warning or tip lives.
> [!WARNING]
> Listing features instead of explaining the driving mechanism. Teams § mechanism explains *why* a bad team underperforms a strong individual (coordination cost, loafing, groupthink), not just that teams have inputs.
### Contrast / What It Is Not
The nearby concept it gets confused with, and the distinction. Skip only if nothing is genuinely confusable.
*Density:* one to three contrasts, each naming the confusable pair and the line between them.
> [!WARNING]
> Omitting this section because it is the hardest to write. Teams contrasts task conflict (improves decisions) vs relationship conflict (destroys effort), and cohesion vs groupthink.
### Failure Modes / Misconceptions
Where the concept breaks or where people get it wrong. A real misconception beats a generic warning. Anchor with a `> [!WARNING]` callout.
*Density:* the genuine traps — Teams lists six ("calling any group a team", "treating storming as failure", "assuming virtual teams need less structure").
> [!WARNING]
> A vague "be careful here" with no specific misconception. Name the wrong belief and the correction.
### Evidence From This Vault
Verified wikilinks to notes where this concept actually appeared — a lecture, a project, a worked example. This is the retrieval path; Grep each link first.
*Density:* link the lecture week and any project that used it.
> [!WARNING]
> An empty section, or links to notes that do not exist. Teams links its Week 5 lecture and Chapter 17.
### Flashcards
`#cards/[track]`, 3–8 cards testing the mechanism and the contrast, not the label. Bold only terms meant to be hidden in review.
> [!WARNING]
> Cards that test the definition ("Team::a group...") instead of the distinction ("Task vs relationship conflict::task conflict can improve decisions; relationship conflict damages attention").
## Done Conditions
- The note explains how the concept works and what it is not, not merely what it is.
- One highlight (the One-Line Answer); failure modes and contrast are both present and specific.
- `evidence:` / Evidence section link real vault notes that prove the concept was used.
- 3–8 mechanism/contrast flashcards on the correct deck.
- Passes all 16 points of [[Vault Rules — Complete AI Ruleset]] Part 12.
## Gold Standard Example
- [[Teams and Team Effectiveness]] — mechanism-dense (IPO breakdown), explicit contrasts (task vs relationship conflict, cohesion vs groupthink), six named traps, and real course examples. It predates the current template heading names but demonstrates the depth this Standard requires under each.
