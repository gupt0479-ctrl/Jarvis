---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-31
tags:
  - evergreen
  - system
  - writing
  - ai-agents
notes:
  - "[[HUMAN_WRITING]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
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

## Blank Lines Rule

The vault's `headerspace.css` CSS snippet handles visual heading spacing. Blank lines are not needed for visual breathing room.

Rules:
- Zero blank lines between `---` (frontmatter close) and the `#` title
- Zero blank lines between any heading (`##`, `###`) and its first content line
- Zero blank lines between consecutive list items
- Zero blank lines between consecutive sections
- **One blank line is acceptable:** immediately after a callout (`> [!X]`) or blockquote (`> `) before a following paragraph of prose

Extra blank lines are not stylistic — they are an error. They bloat the file and signal that the agent added them instead of relying on CSS.

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

## Formatting Markers

These markers have semantic meaning in this vault. Because SR cloze is enabled for both bold and highlight, using them carelessly creates accidental flashcards.

- `==text==` → **highlight cloze.** Use for the ONE most important definitional claim per section. Becomes an SR cloze card automatically when the note is tagged `#cards`. Do not use more than once per heading.
- `**text**` → **bold cloze.** Use for named concepts and entities on introduction, category labels, key contrast words. In `#cards` sections, every bold term becomes an automatic cloze. Use deliberately — not for general emphasis.
- `*label:*` → *italic sub-label.* Use for sub-category intro labels: *Mechanism:*, *Failure mode:*, *Interview value:*, *Core Python skills:*. Not a cloze.

Numbered list items with a bold title follow this pattern:

```markdown
1. **Title**
	sub-content indented with a tab, not spaces
```

Derived from MGMT 3001 and CSCI 2041 chapter notes. Any deviation from this in agent output is an error.

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
> [!WARNING]
> Do not copy API keys from plugin `data.json` files into notes.
```

Callout types used in this vault:
- `> [!NOTE]` — source context, background information
- `> [!TIP]` — practical shortcut or usage tip
- `> [!WARNING]` — safety or correctness risk
- `> [!QUESTION]` — unresolved question, known gap
- `> [!SUMMARY]` — section or source summary
- `> [!EXAMPLE]` — concrete worked example

After a callout or blockquote, leave one blank line before the next paragraph of prose. This is the one permitted blank line. Do not stack callouts to make the note look designed. The vault's CSS already handles visual rhythm.

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

## PDF and Source Ingestion Notes

These rules apply to any note created from a PDF, paper, textbook chapter, or external source.

**Structure order:**
1. Frontmatter (with `track:` matching the subject domain)
2. `# Title`
3. Section content under `##` headings — no blank line between heading and content
4. `## Open Questions` — Tasks (`- [ ]`) for unresolved claims or follow-up actions
5. `## Flashcards` — SR cards after concepts are explained, not before

**Math notation:** Use `$...$` for any inline mathematical expression. Do not spell out notation in prose when symbols are clearer. For display equations use `$$...$$` on its own line. Example: "The expected value $E[X] = \sum x \cdot P(X=x)$ is the probability-weighted sum."

**Tasks for open questions:** Open questions from the source should be Tasks, not prose. Use emoji metadata where relevant.

```markdown
## Open Questions
- [ ] Verify whether the author's claim about $O(n)$ convergence holds for non-convex loss surfaces 📅 2026-06-01
- [ ] Check if the dataset referenced on p. 12 is publicly available
```

**Flashcards section:** Every ingested source note should end with a `## Flashcards` section tagged `#cards/[track]`, where `[track]` matches the note's `track:` frontmatter field.

```markdown
## Flashcards
What is the retrieval failure mode in RAG?
?
The retriever surfaces documents that are lexically similar but decision-irrelevant. The model grounds its answer in the wrong evidence — response looks more cited, is less correct.
#cards/ai
```

Do not create cards from raw clippings. Cards belong after the note has a processed mechanism worth recalling. See [[40_Resources/Obsidian/Plugins/Spaced Repetition and Learning Loops]] for full card syntax.

## Content Density Standard

==Every line in the source must appear in the note in some form. The note replaces the source — the user should never need to open the original again.==

Applies to any note created from an external source (PDF, article, video, conversation).

- Map the document structure first: list every heading and subheading before writing anything.
- Preserve the source's own section order. Use `###` headings with the source's exact section titles verbatim.
- Reproduce all numbered steps, frameworks, and lists in full — do not compress.
- Every named concept, term, entity, tool, company, and person gets captured.
- Every warning or "key insight" marker in the source becomes a callout in the note.
- After writing, re-read: if opening the original would reveal anything not in the note, it is incomplete.

Partial capture is a failure, not a draft.

## Source Note Format Rules

Rules specific to notes created from external sources.

**`source_note` format:** `source_note: "[[Filename.pdf]]"` — filename with extension, no folder path. Not `[[60_Claude/05_Clippings/PDFs/Filename.pdf]]`. Not `[[Filename]]` (without extension).

**`source_status` field:** Do not include unless the specific workflow document explicitly requires it.

**Wikilinks in frontmatter:** Every `notes:` wikilink must refer to a file that actually exists. Grep for the filename to confirm before writing. Broken frontmatter links corrupt metadata silently. Stubs belong only in the note body, labeled `(to create)`, never in frontmatter.

**`---` in the body:** Forbidden. `---` is the YAML frontmatter terminator. It appears exactly once per file, after the frontmatter, before the title. Never use it as a visual separator in the note body.

**No trailing blank lines** at the end of a file. No footer comments (`*Ingested by...*`, `*Generated by...*`).

**Structure order for any source note:**
1. Frontmatter (`track:` matching subject domain; no duplicate keys; all wikilinks verified)
2. `# Title — Summary` (no blank line after frontmatter close)
3. `**Source:**`, `**Ingested:**`, `**Pages:**` header lines immediately after title
4. `## Source` — one sentence: what it is, who produced it, stated purpose
5. `## Key Claims` — every distinct claim; bold the key word in each bullet
6. `## Full Content` — `###` subheadings using the source's exact section titles verbatim
7. `## Why It Matters` — connection to active vault work; no padding
8. `## Links Into The Vault` — verified wikilinks; stubs labeled `(to create)`
9. `## Open Questions` — `- [ ]` Tasks format
10. `## Flashcards` — `#cards/[track]` cards, 3–5 minimum, test mechanisms not labels

## Quality Gate

==Run this 16-point checklist before saving any note. Do not save until all pass.==

1. **Duplicate frontmatter keys?** → scan and fix; one key, one value
2. **Every `notes:` wikilink confirmed to exist?** → Grep each one; fix or move to body labeled `(to create)`
3. **`---` anywhere in the body?** → remove
4. **Blank line between frontmatter `---` and `#` title?** → remove
5. **Blank line between any heading and its first content line?** → remove
6. **Blank lines between list items?** → remove
7. **Extra blank lines except after callout/blockquote before prose?** → remove
8. **Every major `##` section has exactly one ==highlight== anchor?** → add the single most important definitional claim
9. **Named concepts, terms, and entities bolded on first introduction?** → add `**bold**`
10. **Sub-category intro labels italicized?** → `*Label:*` on every sub-group intro
11. **Interview emphasis, warnings, key facts in callouts?** → add where missing
12. **Tab-indented (not space-indented) sub-content under `1. **Title**` items?** → fix
13. **LaTeX notation (`$...$`) for any mathematical expression?** → add if missing
14. **`## Open Questions` in `- [ ]` Tasks format?** → fix if prose
15. **`## Flashcards` section with `#cards/[track]` cards?** → add if missing (source notes); minimum 3–5; test mechanisms not labels
16. **Does re-reading this note replace opening the original?** → if no, add what is missing

## Safety Rules

Never do without explicit instruction:

- Create a file or folder at the vault root
- Modify `60_Claude/05_Clippings/` — raw sources are read-only after capture
- Read or write `50_Archive/`
- Edit `.obsidian/`, `.claude/`, `.cursor/`, `.kiro/`, `.codex`, `.git/` settings files
- Copy API keys, tokens, or plugin credentials into notes
- Run Git commit, push, or pull
- Restructure `status: tree` notes — propose first
- Delete or move notes without explicit instruction
- Bulk-dump AI output into `40_Resources/`

Pause and confirm before restructuring system docs, modifying plugin settings, or any destructive file operation. When in doubt: write to `60_Claude/00_Inbox/`.

## Final Check

Before saving a note, ask:

- Did I preserve frontmatter?
- Did I update `updated:` only if the note changed meaningfully?
- Did I use wikilinks where future retrieval needs them?
- Did I write concrete mechanisms instead of polished filler?
- Did I keep raw capture separate from distillation?
- Did I use plugin syntax only where it helps the note work?

If the answer is no, fix the note before calling it done.
