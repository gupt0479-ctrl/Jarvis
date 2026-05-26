---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - learning
  - spaced-repetition
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/7_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Spaced Repetition and Learning Loops

Spaced Repetition should turn understood notes into retrieval practice. It should not turn raw source text into trivia.

Use it after the note has a mechanism, contrast, or worked example worth recalling.

## Current Settings

- Flashcard tag: `#cards`.
- Convert folders to decks: enabled.
- Single-line separator: `::`.
- Single-line reversed separator: `:::`.
- Multiline separator: `?`.
- Multiline reversed separator: `??`.
- Bold text creates clozes: enabled.
- Highlighted text creates clozes: enabled.
- Curly-brace clozes: disabled.
- Randomize card order: enabled.
- Show context in cards: enabled.
- Ignored folders setting returned no explicit value in the current data scan; needs verification against UI.

Because bold and highlight clozes are enabled, formatting choices can accidentally create cards.

## Card Syntax

Single direction:

```markdown
Why can bad retrieval make RAG worse?::Because the model gets confident-looking but irrelevant context and anchors on the wrong evidence. #cards
```

Reversed:

```markdown
Consistent frontmatter keeps dashboards trustworthy.:::What makes Dataview useful in Jarvis? #cards
```

Multiline:

```markdown
What should happen before a raw clipping becomes flashcards?
?
It should be summarized, linked to the source, and distilled into a concept or course note. Cards should test the processed idea, not pasted source fragments.
#cards
```

Multiline reversed:

```markdown
A project note's `next:` field should name one current move.
??
What belongs in `next:` instead of a task list?
#cards
```

Cloze:

```markdown
The query fails because **metadata drift** makes correct Dataview syntax return the wrong set of notes. #cards
```

Use bold or highlight only when the hidden term is worth recalling.

## Good Jarvis Cards

A good card tests one useful distinction:

- Mechanism: "Why does `BUILD-MAX-HEAP` run in linear time?"
- Contrast: "When should Jarvis use Dataview instead of Tasks?"
- Failure mode: "What happens if a project note has no `next:`?"
- Exam-style prompt: "Given this OCaml pattern match, what case is missing?"
- Project/application prompt: "Where should a BOOM source clipping go before synthesis?"

A bad card tests a label without use:

```markdown
Dataview is::A plugin #cards
```

That card adds review load without improving recall.

## Learning Loops

Coursework:

1. Put cards near the concept, week, lab, or exam note they test.
2. Prefer mechanism, contrast, mistake, and exam-prompt cards.
3. Link cards to boards when a course has a review map.

Algorithms and systems:

1. Start with invariants, state transitions, failure cases, and complexity traps.
2. Add Excalidraw diagrams only when the visual state helps.
3. Use cards to test why an invariant holds, not just what it is called.

AI concepts:

1. Test pipeline failure modes: retrieval, grounding, tool use, evaluation, memory drift.
2. Anchor cards in project notes or source summaries when the idea came from a real build.
3. Avoid cards that only repeat model/product names.

Interview prep:

1. Use cards for prompts that force explanation under pressure.
2. Include one "what mistake is this question baiting?" card for tricky topics.
3. Link to proof artifacts under capability dashboards when relevant.

## Connecting Cards To Dashboards

Dataview can surface notes tagged `#cards`:

```dataview
LIST
FROM #cards
WHERE !contains(file.folder, "30_Order/Templates")
SORT file.mtime DESC
LIMIT 10
```

Capability notes can also use:

- `last_drilled`
- `next_drill`
- `drill_interval`
- `mastery_level`
- `mastery_score`

Use those fields when the note belongs to long-term capability tracking, not for every small course note.

## Agent Rules

Agents may add cards when:

- the source has been processed into a summary or concept note
- the answer is stable
- the card tests one mechanism or contrast
- the card is near its explanatory context

Agents should avoid:

- creating cards from `60_Claude/05_Clippings`
- turning every bold phrase into accidental cloze material
- creating large flashcard banks in one pass
- using cards to hide weak explanations

Review should improve the note. If a card feels hard because the underlying note is vague, fix the note first.

## Sources

- [Spaced Repetition README](https://github.com/st3v3nmw/obsidian-spaced-repetition)
- [Spaced Repetition resources](https://www.stephenmwangi.com/obsidian-spaced-repetition/resources/)
- [[00_Dashboard]]
- [[40_Resources/Obsidian/Vault Operating System]]
