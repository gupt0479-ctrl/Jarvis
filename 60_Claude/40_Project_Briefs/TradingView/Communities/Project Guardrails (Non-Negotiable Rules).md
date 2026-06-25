---
type: community
cohesion: 0.36
members: 11
---

# Project Guardrails (Non-Negotiable Rules)

**Cohesion:** 0.36 - loosely connected
**Members:** 11 nodes

## Members
- [[Design Non-Goals]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Guardrails to Preserve]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Non-Negotiable Guardrails]] - rationale - CLAUDE.md
- [[Property 13 No Secrets in Stored Metadata]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 14 Security and Privacy]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 16 Scope Boundaries]] - rationale - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Risks, Non-Goals, and Guardrails]] - rationale - Docs/RESEARCH.md
- [[Task 13 Scope Boundary Enforcement and Security Checks]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 14 Final Checkpoint]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[guardrail-auditor Agent]] - document - .claude/agents/guardrail-auditor.md
- [[guardrail-check Skill]] - document - .claude/skills/guardrail-check/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Project_Guardrails_Non-Negotiable_Rules
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 3 edges to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 1 edge to [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs]]
- 1 edge to [[_COMMUNITY_2026 Research Baseline (FinGPTFinRobotFINRASEC)]]
- 1 edge to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 1 edge to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]
- 1 edge to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]

## Top bridge nodes
- [[guardrail-auditor Agent]] - degree 10, connects to 4 communities
- [[Non-Negotiable Guardrails]] - degree 6, connects to 2 communities
- [[Property 13 No Secrets in Stored Metadata]] - degree 4, connects to 2 communities
- [[Design Non-Goals]] - degree 7, connects to 1 community
- [[guardrail-check Skill]] - degree 7, connects to 1 community