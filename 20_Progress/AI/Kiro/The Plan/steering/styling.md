---
inclusion: always
---

# Styling
Read `HUMAN_WRITING.md` first. This file covers formatting, not prose quality.
## Spacing
- No blank line between a heading and the first line of content below it.
- No blank line between the last line of content and the next heading.
- One blank line between sections only when the previous section ends with a code block, table, or callout.
- Single blank line between list items only when each item is a multi-line block.
## Headings
- `#` for the note title. One per note.
- `##` for top-level sections: MOC, Definition, Core Ideas, Complexity + Tradeoffs, Mini-test, Flashcards, Jarvis Enrichment.
- `###` for subsections inside those.
- Do not skip levels. Do not use `####` unless nesting inside a `###`.
- Heading text is short and retrieval-oriented. No articles, no verbs unless necessary.
## Lists
- Bullets (`-`) for parallel items, comparisons, and unordered sets.
- Numbered lists (`1.`) for sequences, steps, and ordered procedures.
- Indent with a tab for sub-items.
- Bold the lead term when defining something inline: `- **Max-heap** means every parent key is at least as large as its children.`
- Keep list items to one or two lines. If an item needs a paragraph, it should be its own subsection.
## Wikilinks
- Use `[[wikilinks]]` aggressively. Link concepts, weeks, chapters, boards, and source notes.
- Prefer display aliases when the path is long: `[[10_UMN/CSCI 4041/Week - 5|Week - 5]]`.
- Link inside headings and list items when it helps retrieval.
- Do not link the same target twice in the same section.
## Callouts
- `> [!summary]` for boxed reference info like complexity tables or algorithm summaries.
- `> [!NOTE]` for contextual asides and reminders.
- `> [!INFO]` for key term definitions inside lecture notes.
- Keep callout content short. If it grows past five lines, use a subsection instead.
## Tables
- Use tables for structured comparisons: complexity tradeoffs, property definitions, region invariants.
- Always include a header row.
- Align columns with `---` separators, no extra padding.
- Prefer tables over bullet lists when three or more attributes are compared per item.
## Code Blocks
- Always specify the language tag: `python`, `ocaml`, `text`, `sql`, etc.
- Code Styler is active with line numbers enabled. Keep blocks short enough to read without scrolling.
- Use `text` for pseudocode or informal algorithm traces.
- Inline code for single expressions, variable names, and short commands.
## Math
- LaTeX Suite is active. Use `$...$` for inline math and `$$...$$` for display math.
- Prefer inline math in running text and list items.
- Use display math only for standalone equations or derivations.
## Dataview Queries
- Use Dataview code blocks for dynamic content: project lists, task queues, metadata audits, orphan detection.
- Prefer `TABLE` for structured output, `LIST` for simple enumerations, `TASK` for action items.
- Always include a `SORT` and `LIMIT` to keep rendered output manageable.
- Add a `WHERE` filter that excludes templates and system notes unless the query is specifically about them.
## Tasks Plugin
- Use `- [ ]` for open tasks, `- [x]` for done, `- [/]` for in progress, `- [-]` for cancelled.
- Tasks plugin auto-sets done and cancelled dates. Do not add them manually.
- Place tasks inside the relevant note, not in a separate task file.
## Spaced Repetition / Flashcards
- Tag flashcard sections with `#cards/<COURSE_OR_TRACK>` (e.g. `#cards/CSCI4041`, `#cards/CSCI2041`).
- Format: `Front::Back.` on a single line.
- Keep cards atomic. One fact per card.
- Place the `## Flashcards` section at the bottom of the note, after Mini-test.
## Frontmatter
- Every note must have `type` and `status` at minimum.
- Use the canonical properties from `Vault Operating System.md`. Do not invent new ones without updating that file.
- `status` values follow the growth metaphor: `seed`, `sprout`, `tree` for knowledge notes; `active`, `paused`, `complete`, `archived` for projects.
- List-type properties (`notes`, `topics`, `related`, `track`, `prerequisites`, `used_in`, `evidence`) use YAML list syntax with wikilink strings.
## Templater
- Use Templater syntax (`2026-07-04`) in templates only, never in finished notes.
- Templates live in `30_Order/Templates/` and nowhere else.
## Theme Awareness
- AnuPpuccin with Catppuccin Mocha dark, AMOLED background, lavender accent.
- Colored headers are enabled (H1 lavender, H2 mauve, H3 flamingo, H4 peach, H5 flamingo, H6 rosewater). Headings carry visual weight already; do not add emoji or decorators.
- Custom checkboxes are active. Use the status symbols above and they render correctly.
- Rainbow folders and colored file explorer are on. Folder names carry color meaning from the numbering scheme.
- Bold renders in mauve, italic in sapphire, highlight in rosewater. Use these for emphasis sparingly since they are visually loud.