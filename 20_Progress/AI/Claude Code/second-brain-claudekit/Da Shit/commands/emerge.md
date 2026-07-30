---
description: Surface patterns and themes emerging from recent notes that haven't been named yet
---

Scan recent vault activity and surface latent patterns — recurring ideas, themes, or questions that haven't been explicitly captured yet.

## Steps

1. Read the last 7 daily notes from `00_Daily/`.
2. Read all notes created or modified in the last 14 days (check `created` and `modified` frontmatter).
3. Identify **recurring themes**: concepts, words, or questions that appear in 3+ notes but have no dedicated note yet.
4. Identify **open loops**: questions raised but not answered, tasks deferred more than 3 times, intentions stated but not acted on.
5. Identify **surprising connections**: two notes from different domains that share a structural similarity.
6. Output an **Emergence Report**:

```
## Emergence Report — {{date}}

### Themes Appearing (not yet captured as notes)
1. "{{theme}}" — appeared in [[note-a]], [[note-b]], [[note-c]]
   → Suggested note: [[theme-slug]]

### Open Loops
- "{{loop}}" — first appeared [[date]] in [[note]], still open
  → Suggested action: ...

### Surprising Connections
- [[note-a]] ≈ [[note-b]] — both are about {{shared structure}}
  → Suggested link or MOC: ...
```

7. Ask: *"Want me to create any of these suggested notes or links?"*
