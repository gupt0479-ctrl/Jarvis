---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - writing
  - ai-agents
notes:
  - "[[HUMAN_WRITING]]"
  - "[[Plugins]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]]"
---
# Jarvis Writing and Formatting

This file extends [[HUMAN_WRITING]] with Obsidian-specific rules.

[[HUMAN_WRITING]] is still the source of truth for voice. This note explains how that voice should appear inside Jarvis: frontmatter, wikilinks, headings, Dataview-friendly fields, Tasks syntax, flashcards, math, code, boards, and visual notes.

For deeper plugin-specific examples, use [[40_Resources/Obsidian/Plugins/Dataview and Dashboards]], [[40_Resources/Obsidian/Plugins/Tasks Kanban and Project Tracking]], [[40_Resources/Obsidian/Plugins/Spaced Repetition and Learning Loops]], [[40_Resources/Obsidian/Plugins/Visual Thinking with Canvas and Excalidraw]], and [[40_Resources/Obsidian/Plugins/Appearance Code Math and Reading Experience]].

## Relationship To Human Writing

Follow [[HUMAN_WRITING]] before anything here.

The note should sound like someone who understands the thing, not like someone performing expertise. Formatting cannot rescue vague writing.

Good Jarvis writing usually does one of these:

- explains a mechanism
- captures a decision
- contrasts nearby ideas
- names a failure mode
- links a claim to a real source or project
- gives a usable next action
- marks what is still uncertain

If a section only says that something is "important," "powerful," or "useful," rewrite it until it says why.

## Markdown Shape

Write for fast rereading.

- Use short paragraphs.
- Use headings when they help navigation or retrieval.
- Use bullets for comparison, steps, symptoms, examples, and constraints.
- Use tables only when comparison is clearer in rows.
- Use code blocks for code, syntax, commands, data examples, and exact formats.
- Use callouts sparingly for warnings, source notes, definitions, or important caveats.

Headings should name the thing inside the section. Avoid headings like "Overview" if a more precise heading exists.

Better headings:

- `## Why Retrieval Fails`
- `## Heap Construction Trap`
- `## When To Use Kanban`
- `## Source-Grounded Claims`

Weaker headings:

- `## Introduction`
- `## Important Information`
- `## Key Insights`
- `## Comprehensive Overview`

## Links

Use Obsidian wikilinks for internal notes.

Good:

- `[[HUMAN_WRITING]]`
- `[[40_Resources/Obsidian/Vault Operating System]]`
- `[[CSCI 2041 Board]]`
- `[[OCaml - Pattern Matching|pattern matching]]`

Use aliases when the sentence reads better with natural language.

Do not create plain-text mentions of existing notes when a wikilink would improve retrieval.

Do not create links just because a word could be linked. Link when the target note would help future reading.

## Frontmatter And Properties

Preserve existing frontmatter.

When creating new notes, use the vault's canonical fields from [[40_Resources/Obsidian/Vault Operating System]]:

```yaml
---
type: evergreen
status: sprout
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - evergreen
notes:
  - "[[Related Note]]"
next:
---
```

Use `updated:` only after meaningful changes. Fixing a typo usually does not need a semantic update. Adding a new section, changing claims, creating a new workflow, or changing the note's purpose does.

Important fields:

- `type`: note class such as `input`, `evergreen`, `concept`, `project`, `thought`, `brainstorm`, `class`, `plan`, `review`, `dashboard`, `index`, or `output`.
- `status`: maturity or state such as `seed`, `sprout`, `tree`, `active`, `paused`, `complete`, or `archived`.
- `created`: creation date.
- `updated`: last meaningful content update.
- `tags`: retrieval tags, not folder replacements.
- `notes`: primary related notes.
- `next`: concrete next action or next note.
- `source_url`: external source pointer.
- `track`: long-term domain such as `ai`, `systems`, `algorithms`, `career`, or `trading`.
- `enrichment_status`: `candidate`, `in-progress`, `enriched`, or `needs-review`.
- `source_status`: `vault-grounded`, `externally-sourced`, `mixed`, or `uncertain`.

Do not invent new metadata fields unless the current schema cannot represent the information.

## Dataview-Friendly Writing

Dataview works only when metadata is consistent.

Use structured fields for things dashboards need to query:

- active state
- due dates
- review dates
- enrichment state
- track/domain
- related projects
- source status
- mastery or drill dates

Do not hide queryable information only in prose.

Good:

```yaml
type: project
status: active
deadline: 2026-05-25
next: "Draft project brief"
```

Weak:

```markdown
This is probably still active and maybe due soon.
```

Use Dataview blocks for live indexes, not static tables that will immediately go stale.

## Tasks-Compatible Writing

Use task lines for real actions.

Good:

```markdown
- [ ] Draft the BOOM queue failure note by Friday
- [/] Verify whether `excalibrain` is installed in Obsidian
- [-] Replace old manual task table because Tasks query now covers it
```

Rules:

- Use `- [ ]` for open tasks.
- Use `- [/]` for in-progress tasks.
- Use `- [x]` for done tasks.
- Use `- [-]` for cancelled tasks.
- Let the Tasks plugin manage done and cancelled dates where possible.
- Add due/scheduled/priority metadata in the configured Tasks emoji format, not Dataview inline fields.

Do not turn a conceptual note into a task dump. Put only the next real actions in the note, and use dashboards for broad task retrieval.

## Spaced Repetition Cards

Use flashcards only for understood, atomic knowledge.

Vault settings:

- Flashcard tag: `#cards`.
- Single-line card separator: `::`.
- Reversed single-line separator: `:::`.
- Multiline separator: `?`.
- Reversed multiline separator: `??`.
- Highlight and bold clozes are enabled.

Good card:

```markdown
Why can bad retrieval make RAG worse?::Because the model receives confident-looking but irrelevant context, so generation becomes anchored to cleaner nonsense instead of the user's actual question. #cards
```

Better card after a real note:

```markdown
What is the retrieval failure mode in RAG?
?
The retriever surfaces documents that are lexically similar but decision-irrelevant. The model then grounds its answer in the wrong evidence, which can make the response look more cited while being less correct.
#cards
```

Avoid cards that only ask for labels:

```markdown
RAG stands for::Retrieval Augmented Generation #cards
```

That card may be useful once, but it does not build understanding.

## Code Blocks

Use fenced code blocks with language identifiers.

Good:

````markdown
```ts
type NoteStatus = "seed" | "sprout" | "tree";
```
````

For terminal examples:

````markdown
```powershell
Get-ChildItem .obsidian\plugins
```
````

For Dataview:

````markdown
```dataview
TABLE status, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived"
SORT file.mtime DESC
```
````

Rules:

- Keep code examples short.
- Include only code that explains the note.
- Put long source captures in `60_Claude/05_Clippings/` or a source summary, not inside evergreen notes.

## Math And Latex

Use LaTeX when notation is the clearest form.

Inline math is for small expressions like `$O(n \log n)$` or `$p(x)$`.

Display math is for equations that need visual space:

```markdown
$$
T(n) = 2T(n/2) + O(n)
$$
```

Rules:

- Explain what the equation means in prose.
- Prefer one worked example over five unexplained formulas.
- Do not use math notation to make a simple sentence look more advanced.

## Excalidraw Embeds

Use Excalidraw when the relationship is spatial.

Good uses:

- system architecture
- feedback loops
- dependency graphs
- visual concept maps
- process diagrams
- cause/effect chains

Text note plus drawing is better than drawing alone. The text note should state the main mechanism, and the drawing should make the relationships easier to see.

Embed drawings with wikilinks:

```markdown
![[Drawing Example.excalidraw]]
```

Do not rely on an image without nearby explanation. Future agents need searchable text.

## Kanban Board Writing

Use Kanban boards for lane-based execution.

Good board cards:

- `[[Habit Tracker Board]]`
- `Draft plugin guide`
- `Verify Excalibrain status`
- `Review flashcard backlog`

Weak board cards:

- `Stuff`
- `Important`
- `Make better`
- `Research`

Rules:

- Keep cards small.
- Link cards to notes when the card represents durable work.
- Do not put long explanations inside cards.
- Use notes for knowledge, boards for flow.

## Callouts

Use callouts only when they change how the reader should treat the content.

Good:

```markdown
> [!warning]
> Do not copy API keys from plugin `data.json` files into notes.
```

Useful callout types:

- `[!note]` for source context
- `[!warning]` for safety or correctness risks
- `[!question]` for unresolved questions
- `[!example]` for concrete examples

Do not stack callouts to make the note look designed. The vault's CSS already handles visual rhythm.

## How Not To Write

Do not write:

- generic productivity advice
- plugin feature lists without Jarvis-specific use
- fake confidence
- summaries that repeat the source without compressing it
- ornate transitions
- marketing language
- decorative formatting
- duplicate tables that Dataview should generate
- standalone flashcards before the concept is explained
- raw source material inside durable notes

Bad:

```markdown
Dataview is a powerful plugin that unlocks a comprehensive way to manage your knowledge landscape.
```

Better:

```markdown
Dataview is the dashboard layer. Use it when the list should update from frontmatter instead of being maintained by hand.
```

## Final Check

Before saving a note, ask:

- Did I preserve frontmatter?
- Did I update `updated:` only if the note changed meaningfully?
- Did I use wikilinks where future retrieval needs them?
- Did I write concrete mechanisms instead of polished filler?
- Did I keep raw capture separate from distillation?
- Did I use plugin syntax only where it helps the note work?

If the answer is no, fix the note before calling it done.
