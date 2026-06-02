---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - search
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Search Linking and Navigation

Jarvis depends on retrieval. Search, links, previews, and pinned navigation should make the correct note easier to find than creating a duplicate.

## Search Before Create

Before creating a note:

1. Search exact title candidates.
2. Search likely aliases and abbreviations.
3. Check relevant boards and dashboards.
4. Check backlinks from the closest existing concept/project/source note.
5. Extend the canonical note unless the new note has a distinct durable job.

Agents should use filesystem search or available vault search tools first. Humans should use Omnisearch, Quick Switcher, backlinks, and dashboards.

## Backlinks and Unlinked Mentions

Backlinks work when links are intentional.

Use wikilinks when:

- a project uses a concept
- a course note depends on a concept
- a source supports a claim
- a summary should lead back to the source
- an agent workflow explains a repeated action

Use unlinked mentions to discover missed connections, not as proof that two notes belong together.

Do not link every keyword. Link retrieval paths.

## Page Preview and Hover Editor

Page Preview and Hover Editor make headings and first paragraphs matter.

Current Hover Editor settings:

- Auto focus: enabled.
- Auto pin: `onMove`.
- Trigger delay: `300ms`.
- Close delay: `600ms`.
- Initial size: `400px` by `340px`.
- Embeds in hover: enabled.

Writing implication: the first paragraph under a heading should say the mechanism or decision, not warm-up prose. A hover preview should let the reader decide whether to open the note.

## Omnisearch
Omnisearch has its own deep reference now: [[Omnisearch and Retrieval]]. Short version: fuzzy ranked full-text search, weights filenames and headings highest, indexes Markdown only (PDF/Office/image indexing all off). Use it for broad human retrieval; do not assume any attachment is searchable. The Text Extractor decision and full settings live in that doc.

## Quick Switcher and Recent Files

Quick Switcher is for known-note navigation. It is useful when the note name is already close to mind.

Recent Files is weak session context. It can help a human resume work, but agents should not treat it as the source of truth. Read [[00_Dashboard]] and the session log instead.

## File Explorer++

File Explorer++ supports pinned and hidden navigation filters.

Treat pinned files as navigation landmarks:

- dashboards
- course boards
- project boards
- habit boards
- system reference notes

Do not rewrite pin/hide filters during documentation work. These are human layout preferences.

## Paste URL Into Selection

Paste URL into selection is a human link hygiene tool. It turns selected text into a Markdown link when a URL is pasted.

Agents writing directly should create normal Markdown links:

```markdown
[source label](https://example.com)
```

Use `source_url` in frontmatter when a note has one primary external source.

## Headings, Aliases, and Wikilinks

Retrieval improves when notes have:

- specific H1 titles
- headings that name mechanisms, not moods
- aliases when a concept has multiple names
- wikilinks from projects, courses, and source summaries
- source anchors near claims

Avoid:

- duplicate notes with slightly different titles
- orphan stable docs
- headings like "Overview" repeated everywhere without context
- source links buried at the bottom when the claim needs them nearby

## Agent Workflow

When an agent cannot find a note:

1. Search title and alias variants.
2. Search by folder role.
3. Search by likely field values, such as `type: project` or `#cards`.
4. Check relevant dashboards.
5. Create a new note only after naming why it is not a duplicate.

## Integration Map
- **Hover Editor ← first lines:** the `300ms` hover preview shows a note's opening. So the rule "the first line under a heading states the mechanism, not warm-up prose" is a Hover Editor optimization, not a style preference — a good first line lets the reader decide without opening the note.
- **Hover Editor → Omnisearch:** both reward the same thing — precise headings and a useful first paragraph. Omnisearch ranks them; Hover Editor displays them. See [[Omnisearch and Retrieval]].
- **File Explorer++ → navigation landmarks:** pinned dashboards/boards are the human entry points; agents should read [[00_Dashboard]] and the session log instead of relying on Recent Files, which is weak session context.
## Gold-Standard Example
[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Algorithms/HeapSort|HeapSort]] previews well on hover because its first lines state the mechanism, and it ranks well in Omnisearch because its headings name specific things. Contrast a note whose first heading is "Overview" followed by warm-up prose — it previews as noise and ranks for nothing.
## Verified Open State
- Should source-summary folders (`60_Claude/10_Source_Summaries/`) be pinned in File Explorer++ for quick navigation, as the audit suggested? — *human layout preference; needs user choice*
- Is the `Alt+C` Calendar hotkey live, or a leftover from an uninstalled Calendar plugin? — *unresolved across inventory*
## Sources

- [Obsidian Help - Backlinks](https://help.obsidian.md/plugins)
- [Omnisearch docs](https://publish.obsidian.md/omnisearch/Index)
- [Omnisearch community plugin page](https://community.obsidian.md/plugins/omnisearch)
- [Hover Editor README](https://github.com/nothingislost/obsidian-hover-editor)
- [File Explorer++ README](https://github.com/kelszo/obsidian-file-explorer-plus)
- [Recent Files README](https://github.com/tgrosinger/recent-files-obsidian)
- [Paste URL into selection README](https://github.com/denolehov/obsidian-url-into-selection)
