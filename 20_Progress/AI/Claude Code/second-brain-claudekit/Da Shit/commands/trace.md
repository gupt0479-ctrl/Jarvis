---
description: Trace the origin and evolution of an idea across the vault
---

Follow an idea, concept, or decision backward and forward through the vault to map its full history.

## Steps

1. Ask: *"What idea, concept, or decision do you want to trace?"* (one question only).
2. Search for the term across all vault notes (all folders except `50_Claude/Templates/`).
3. Build a **timeline** ordered by `created` frontmatter date:
   - First mention
   - Key developments (note titles + dates)
   - Current most-developed form
4. Identify **mutations**: places where the idea changed, was questioned, or was refined.
5. Surface any **contradictions**: notes where the idea is challenged by other notes.
6. Output a **Trace Map**:

```
## Trace: "{{concept}}"

### Origin
- [[first-note]] — {{date}} — first appearance

### Evolution
- [[note-2]] — {{date}} — how it developed
- [[note-3]] — {{date}} — key refinement

### Current Form
- [[latest-note]] — best current articulation

### Contradictions / Tensions
- [[conflicting-note]] ↔ [[other-note]] — reason

### Suggested Next Step
- Consider graduating this into an evergreen note: [[concept-evergreen]]
```

7. Suggest whether the idea is ready to graduate (see `/graduate`).
