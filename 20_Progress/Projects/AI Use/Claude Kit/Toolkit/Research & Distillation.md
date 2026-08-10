---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - use-case
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]]"
next:
---
# Research & Distillation
==Turning a raw source — PDF, clipping, transcript, AI conversation — into a durable vault note, and tracing where an idea already showed up before writing it again.==
Use the `research-distiller` agent ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents#Research & Distillation|Agents]]) for anything long or multi-source: a PDF needing section-by-section extraction, a batch of clippings, a whole GitHub repo. Use `/ingest-clipping` directly ([[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills#Research & Distillation|Skills]]) for a single, already-captured source — it is the command the agent itself calls for the routine case. Use `/trace-topic` first, before either, to check whether the topic already has notes scattered across the vault — distilling into a new note without checking `/trace-topic` first is how duplicate evergreen notes happen.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]] · [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]]
