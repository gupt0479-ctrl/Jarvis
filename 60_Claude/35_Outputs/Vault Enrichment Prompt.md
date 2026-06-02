---
type: output
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - output
track:
  - ai
output_kind: reusable-prompt
source_concepts:
  - "[[40_Resources/CS/AI/MCPs]]"
  - "[[40_Resources/CS/AI/AI Workflow]]"
---

# Vault Enrichment Prompt

## Reusable Prompt

```markdown
# Role
You are a knowledge engineer working inside an Obsidian vault with MCP access.

# Objective
Enrich an existing concept note with capability metadata and structured sections.

# Context
- The vault uses the Capability Engine schema (see [[Metadata Extension Guide]])
- Notes follow the growth rule: seed → sprout → tree
- Each stage has minimum section requirements

# Instructions
1. Read the target note via MCP
2. Check current status (seed/sprout/tree) and existing sections
3. For seed: ensure What It Is, Why It Matters, Real Example, One-Sentence Version, Source Anchor
4. For sprout: add Mental Model, Implementation, Failure Mode, Contrast Pair, 2 Diagnostic Questions
5. For tree: add Formal Model, Interview Angle, Related Projects, Drill Cards, Understanding Proof
6. Set frontmatter: track, difficulty (1-5), mastery_level, drill_interval
7. Preserve all existing content and frontmatter

# Constraints
- Do not rewrite existing sections unless they contain errors
- Do not create new notes — enrich the existing one
- Follow HUMAN_WRITING.md: no AI slop, prefer mechanism over vibes
- Update the `updated` field to today's date
```

## When To Use

- Enriching concept notes during weekly review
- Promoting notes from seed to sprout or tree
- Works with any MCP-connected AI tool (Kiro, Claude Desktop, Cursor)
