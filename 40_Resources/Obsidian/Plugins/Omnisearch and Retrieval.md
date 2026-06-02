---
type: evergreen
status: sprout
created: 2026-05-31
updated: 2026-05-31
tags:
  - evergreen
  - system
  - obsidian
  - omnisearch
  - search
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
  - "[[Search Linking and Navigation]]"
---
# Omnisearch and Retrieval
==Omnisearch is the fuzzy, ranked full-text search a human uses to find a note before creating a duplicate — but it only indexes Markdown, so the 18 PDFs in `05_Clippings/PDFs/` are invisible to it.== That blind spot is the main open decision for this plugin.
## Mechanism
Omnisearch ranks results by relevance (filename, headings, body) with typo tolerance, instead of the core search's literal matching. The problem it solves in Jarvis: the "search before you create" rule in [[AGENTS]] only works if search actually surfaces the existing note. Core search misses fuzzy matches and aliases; Omnisearch catches them. It weights filename and headings highest, so **a note with a precise H1 and real `##` headings is far more findable** — which is why heading quality is a retrieval concern, not a cosmetic one.
## Exact Current Settings
Read from `.obsidian/plugins/omnisearch/data.json` (welcome `1.21.0`):
- `useCache`: `true`.
- `fuzziness`: `1` (moderate typo tolerance).
- `PDFIndexing`: `false`; `officeIndexing`: `false`; `imagesIndexing`: `false`; `aiImageIndexing`: `false` — **only Markdown is indexed.**
- `httpApiEnabled`: `false` (port `51361`) — no external query surface.
- Weights: `weightBasename` `10`, `weightDirectory` `7`, `weightH1` `6`, `weightH2` `5`, `weightH3` `4`, `weightUnmarkedTags` `2`.
- `showExcerpt`: `true`; `highlight`: `true`; `showPreviousQueryResults`: `true`.
- `splitCamelCase`: `false`; `ignoreDiacritics`: `true`.
- `indexedFileTypes`: `[]` (no extra extensions).
## Integration Map
- **Omnisearch → "search before create":** it is the human-facing implementation of [[Search Linking and Navigation]] step 1. Agents use filesystem `Grep`/`Glob` instead, but both serve the same anti-duplication rule.
- **Omnisearch ← headings/filenames:** the weight table means [[Jarvis Writing and Formatting]]'s "name the mechanism in the heading" rule directly raises a note's rank. Headings like "Overview" rank a note for nothing.
- **Omnisearch ✗ PDFs:** because `PDFIndexing` is off, the PDF extraction workflow (pypdf in Vault Rules Part 9) is the *only* way to get a PDF's content into a searchable form — the resulting source summary in `60_Claude/10_Source_Summaries/` is what Omnisearch then indexes, not the PDF itself.
- **Omnisearch + Text Extractor:** enabling PDF/image indexing requires the **Text Extractor** companion plugin, which is not installed. This is a deliberate trade (index freshness/disk/privacy vs searchable attachments), not a missing checkbox.
## Agent Rules
- Do not assume any PDF, image, or Office file is searchable. If a fact lives only in an un-summarized PDF, it is not retrievable — summarize it first.
- When writing a note, treat the H1 and `##` headings as search keys: name the mechanism, not the mood.
- Agents should retrieve with `Grep`/`Glob` (exact, scriptable) and reserve Omnisearch guidance for the human workflow.
- Do not enable indexing settings or install Text Extractor without explicit user approval.
## Failure Modes
- **PDF blind spot (current):** a clipping's content exists in the vault but Omnisearch returns nothing, so an agent or human "can't find it" and may re-ingest or duplicate it.
- **Vague headings:** a note titled with generic headings ranks poorly and effectively hides behind better-named notes.
- **Assuming attachments are indexed:** leads to false "no such note" conclusions.
## Gold-Standard Example
The retrieval target Omnisearch should surface is a well-headed source summary or course note — e.g. [[10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 4|Week - 4]], whose precise H1 and section headings (`## Lecture-to-textbook synthesis`, `## Examples worth keeping`) are exactly the high-weight fields Omnisearch ranks on. Contrast: a PDF in `60_Claude/05_Clippings/PDFs/` returns nothing until it is summarized.
## Verified Open State
- Should PDF/image/Office indexing be enabled, accepting the Text Extractor dependency and its disk/privacy cost? — *needs user decision; the central question for this plugin*
- If yes, is Text Extractor acceptable given the AI-image-indexing privacy implications? — *contingent on the above*
- Should `httpApiEnabled` stay off? (It is currently off, which is the safe default.) — *no change recommended without a stated need*
## Sources
- [Omnisearch docs](https://publish.obsidian.md/omnisearch/Index)
- [Omnisearch community plugin page](https://community.obsidian.md/plugins/omnisearch)
- [Text Extractor plugin](https://github.com/scambier/obsidian-text-extractor)
- [[Search Linking and Navigation]]
