---
description: Surface notes that have drifted — stale, orphaned, or quietly out of date
---

Find notes in the vault that have silently become stale, disconnected, or contradicted by newer thinking.

## Steps

1. Scan all permanent folders (`10_Areas/`, `20_Projects/`, `30_Knowledge/`, `40_Career/`).
2. Flag notes in each of these **drift categories**:

   **Stale** — `created` or `modified` date is 90+ days ago AND no other note links to it recently.
   
   **Orphaned** — has 0 incoming backlinks and no `#moc` tag.
   
   **Superseded** — another note covers the same topic with a more recent `created` date and higher link count.
   
   **Status mismatch** — `status: active` but no edits in 60+ days (likely a zombie project or area).

3. Output a **Drift Report**:

```
## Drift Report — {{date}}

### Stale ({{N}} notes)
- [[note-slug]] — last touched {{date}}, {{N}} links

### Orphaned ({{N}} notes)
- [[note-slug]] — 0 incoming links

### Possibly Superseded
- [[old-note]] → possibly replaced by [[newer-note]]

### Status Mismatches
- [[project-note]] — status: active, last edited {{date}}
```

4. For each category, suggest the action: **re-link**, **archive**, **merge**, or **review**.
5. Do not archive or delete anything without my explicit confirmation.
