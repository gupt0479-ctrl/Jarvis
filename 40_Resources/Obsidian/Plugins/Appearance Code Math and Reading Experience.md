---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - writing
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/7_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Appearance Code Math and Reading Experience

The visual system should make dense notes easier to read. It should not encourage decorative formatting or hide meaning in theme styling.

## Theme and Style Settings

Current appearance:

- Theme: AnuPpuccin.
- Style Settings plugin: enabled.
- Accent color: default/blank.
- Readable line length: enabled.

Agents should document current behavior but not edit theme settings, Style Settings values, or snippets unless the user explicitly asks.

## CSS Snippets

Enabled snippets:

| Snippet | Likely role | Agent rule |
|---|---|---|
| `headerspace.css` | Heading spacing. | Write normal headings; do not compensate with blank-line hacks. |
| `readingview.css` | Reading-view tweaks. | Keep notes readable in plain Markdown too. |
| `rainbowfile_colors.css` | File explorer colors. | Do not store meaning only in folder color. |
| `myedits.css` | Broad custom theme edits. | Needs verification before documenting exact visual effects. |

Do not modify snippets during documentation work.

## Code Styler

Current Code Styler facts:

- Selected theme: Solarized.
- Codeblock line numbers: enabled in the selected theme.
- Lines unwrap by default.
- Gutter highlight: enabled.
- Inline code styling: enabled.
- Excluded languages: `ad-*`, `reference`.
- Processed codeblock whitelist: `run-*`, `include`.

Use fenced code blocks for code, commands, queries, configuration examples, and exact syntax. Include a language whenever possible.

Example:

````markdown
```ts title:"status.ts" hl:2
type Status = "seed" | "sprout" | "tree";
const current: Status = "sprout";
```
````

Do not paste large source files into evergreen notes. Summarize the mechanism and link the source.

## Code Block Rules

Use:

````markdown
```dataview
TABLE status, next
FROM "20_Progress"
WHERE type = "project"
```
````

Use:

````markdown
```tasks
not done
path includes 20_Progress
sort by due
```
````

Use:

````markdown
```yaml
type: evergreen
status: sprout
```
````

Avoid:

- unlabeled code fences when a language exists
- code screenshots instead of text
- giant dumps from source files
- decorative code blocks that do not teach syntax

## Latex Suite

Latex Suite is enabled for math ergonomics.

Use inline math for short notation:

```markdown
The heapify bound is `$O(n)$`, not `$O(n \log n)$`.
```

Use display math when the structure matters:

```markdown
$$
T(n) = 2T(n/2) + O(n)
$$
```

Course-note rule: explain the equation in prose. Math notation should compress a mechanism, not replace it.

Needs verification: user-specific Latex Suite snippets and whether any custom snippets should be documented.

## Ninja Cursor

Ninja Cursor is UI-only. It affects cursor visibility and typing feel, not note syntax or vault structure.

Agents should not mention it in workflow instructions except in inventory/safety docs.

## Callouts and Reading View

Use callouts sparingly:

```markdown
> [!warning]
> DataviewJS is enabled. Prefer plain Dataview unless JavaScript is necessary.
```

Good callouts flag warnings, source status, decisions, or open questions. Bad callouts turn ordinary paragraphs into decoration.

## Markdown That Works Here

Use:

- YAML frontmatter
- specific headings
- short paragraphs
- comparison tables
- wikilinks
- normal Markdown links for external sources
- fenced code blocks with languages
- Tasks-compatible checkboxes
- concise Dataview blocks

Avoid:

- HTML layout
- color-coded prose
- hidden meaning stored only in styling
- random bolding in learning notes, because bold clozes are enabled
- image-only explanations
- generic "overview" sections that do not aid retrieval

The final test is still [[HUMAN_WRITING]]: the note should contain mechanism, contrast, examples, or decisions.

## Sources

- [Obsidian Help - Appearance](https://obsidian.md/help/appearance)
- [Code Styler README](https://github.com/mayurankv/Obsidian-Code-Styler)
- [Latex Suite README](https://github.com/artisticat1/obsidian-latex-suite)
- [Style Settings README](https://github.com/obsidian-community/obsidian-style-settings)
- [Ninja Cursor README](https://github.com/vrtmrz/ninja-cursor)
- [[HUMAN_WRITING]]
