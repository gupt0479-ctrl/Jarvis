---
description: Load current vault context into Claude's working memory for this session
---

Build a concise working context from the vault so Claude can act usefully without you re-explaining anything.

## Steps

1. Read `CLAUDE.md` for stable rules and preferences.
2. Scan `50_Claude/Sessions/` for the most recent session log (newest file by date). Load the `## State` and `## Open Loops` sections.
3. Scan `00_Daily/` for the last 3 daily notes. Extract:
   - Incomplete tasks (`- [ ]`)
   - Any lines tagged `#idea`, `#question`, or `#followup`
4. Scan `20_Projects/` for project notes with `status: active` in frontmatter. List their titles and current focus.
5. Output a **Session Brief** in this format:

```
## Session Brief — {{date}}

### Stable Rules (from CLAUDE.md)
(key behaviours Claude should apply this session)

### Picked Up From Last Session
(open loops, decisions pending, threads in progress)

### Active Projects
- [[project-name]] — current focus

### Uncompleted Tasks (last 3 days)
- [ ] task — source: [[note]]

### Ideas / Questions Surfaced Recently
- idea or question — source: [[note]]
```

6. Confirm context is loaded: *"Context loaded. Ready."*

Do not ask questions. Load and brief. Ask only if a file is missing or ambiguous.
