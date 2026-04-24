# Jarvis Ops CLI

Small operational CLI for the Jarvis Obsidian vault.

The tool is intentionally conservative: it reads Markdown and reports on vault health. It does not rewrite notes, repair links, normalize frontmatter, or edit clippings. The only command that writes is `report`, which creates a new Markdown report under:

`60_Claude/50_Reviews/Ops Reports/`

## Commands

Run from the vault root:

```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 health
.\30_Order\System\jarvis-cli\jarvis.ps1 context
.\30_Order\System\jarvis-cli\jarvis.ps1 projects
.\30_Order\System\jarvis-cli\jarvis.ps1 links
.\30_Order\System\jarvis-cli\jarvis.ps1 dates
.\30_Order\System\jarvis-cli\jarvis.ps1 encoding
.\30_Order\System\jarvis-cli\jarvis.ps1 enrich-candidates
.\30_Order\System\jarvis-cli\jarvis.ps1 report
```

Use `--limit N` to show more rows:

```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 links --limit 50
```

Use `--include-tools` when you explicitly want hidden tool folders included in scans:

```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 health --include-tools
```

## What Each Command Checks

- `health`: summary counts for metadata gaps, future dates, missing project next actions, duplicate filenames, link health, and likely encoding damage.
- `context`: compact context pack from `AI_CONTEXT.md`, `00_Dashboard.md`, the Vault Operating System, the session log tail, and active projects.
- `projects`: active project notes, missing `next` fields, and stale file-modified dates.
- `links`: broken and ambiguous wikilinks. Template-heavy zones are filtered for obvious placeholder links.
- `dates`: future-dated `created`, `updated`, `reviewed`, `last_drilled`, and `next_drill` fields relative to `2026-04-24`.
- `encoding`: likely mojibake artifacts, such as common broken smart-punctuation and UTF-8 marker sequences.
- `enrich-candidates`: ranked notes that are good candidates for Jarvis enrichment based on missing learning sections, note type, track metadata, and maturity.
- `report`: writes a diagnostic Markdown report. Existing notes are not changed.

## Safety Rules

- Markdown remains the source of truth.
- Audit commands are read-only.
- Hidden tool folders are skipped unless `--include-tools` is passed.
- `.obsidian` plugin data is not scanned.
- Generated reports are diagnostic, not cleanup scripts.

## Current Scope

This is Phase 1 of the Jarvis automation layer. It provides visibility before repair. Conversation registries, promotion manifests, and automated cleanup commands should come after the audit output is trustworthy.
