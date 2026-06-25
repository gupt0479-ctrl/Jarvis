---
type: community
cohesion: 0.22
members: 13
---

# Spec Requirements/Properties/Tasks Cross-Refs

**Cohesion:** 0.22 - loosely connected
**Members:** 13 nodes

## Members
- [[Property 10 Provider Registry Rejects Invalid Configuration]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 12 Duplicate Primary Key Rejection]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 19 Ingestion Idempotence for Identical Payloads]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 1 OHLCV Validation Rejects Invalid Records]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 4 Raw Before Normalized Ordering Invariant]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 1 Provider Registry and Configuration]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 5 Data Validation]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 8 Storage Schema]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Task 12 CLI Interface]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 1 Project Structure, Configuration, Core Models]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 2 Storage Layer and DuckDB Schema]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 3 Provider Registry and Base Provider Interface]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 4 Checkpoint - Ensure All Tests Pass]] - document - .kiro/specs/data-ingestion-foundation/tasks.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Spec_Requirements/Properties/Tasks_Cross-Refs
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AI-Ready Evidence Contract & Schemas]]
- 3 edges to [[_COMMUNITY_Provider Landscape & Backup Sources]]
- 2 edges to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 2 edges to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 2 edges to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 2 edges to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 1 edge to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]
- 1 edge to [[_COMMUNITY_V1 Universe Config (assets.toml)]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]

## Top bridge nodes
- [[Task 1 Project Structure, Configuration, Core Models]] - degree 7, connects to 3 communities
- [[Requirement 1 Provider Registry and Configuration]] - degree 6, connects to 3 communities
- [[Requirement 5 Data Validation]] - degree 6, connects to 3 communities
- [[Task 12 CLI Interface]] - degree 5, connects to 3 communities
- [[Requirement 8 Storage Schema]] - degree 5, connects to 2 communities