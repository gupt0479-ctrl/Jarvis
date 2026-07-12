---
type: community
members: 24
---

# Agents Runner & Critic Bundle

**Members:** 24 nodes

## Members
- [[.blocks_llm()]] - code - src/research_data/agents/assemble.py
- [[AnalystInputBundle]] - code - src/research_data/agents/assemble.py
- [[Analyze one symbol. Blocks LLM on MISSINGCONTRADICTORY (E1).]] - rationale - src/research_data/agents/runner.py
- [[Critic path — requires gate_summary for demo_eligible reviews.]] - rationale - src/research_data/agents/runner.py
- [[Critic prompts — gate-whitelist review, monotone confidence pressure (B1B4).  T]] - rationale - src/research_data/agents/critic.py
- [[Orchestration assemble → (optional LLM) → validate → write (C2).  Happy path (U]] - rationale - src/research_data/agents/runner.py
- [[Path_8]] - code
- [[QualityStatus_1]] - code
- [[Raised when analyzecritique cannot complete.]] - rationale - src/research_data/agents/runner.py
- [[RunnerError]] - code - src/research_data/agents/runner.py
- [[StructuredLLM]] - code - src/research_data/agents/llm_client.py
- [[The critic's entire evidence view whitelist projection (+ card prose).]] - rationale - src/research_data/agents/critic.py
- [[What the analyst may see for one symbol.]] - rationale - src/research_data/agents/assemble.py
- [[_insufficient_data_card()]] - code - src/research_data/agents/runner.py
- [[_validation_retry_note()]] - code - src/research_data/agents/runner.py
- [[build_allowlist_from_gate_summary()]] - code - src/research_data/cards/allowlist.py
- [[build_critic_user_prompt()]] - code - src/research_data/agents/critic.py
- [[critic.py]] - code - src/research_data/agents/critic.py
- [[main()_4]] - code - scripts/live_ai_card_smoke.py
- [[merge_allowlists()]] - code - src/research_data/cards/allowlist.py
- [[quality_blocks_llm()]] - code - src/research_data/agents/assemble.py
- [[run_analyze_symbol()]] - code - src/research_data/agents/runner.py
- [[run_critique_spec()]] - code - src/research_data/agents/runner.py
- [[runner.py]] - code - src/research_data/agents/runner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agents_Runner__Critic_Bundle
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EvidenceCardCriticReview Validators]]
- 8 edges to [[_COMMUNITY_Analyst Assembly & LLM Seam Tests]]
- 7 edges to [[_COMMUNITY_Numeric Allowlist (B3)]]
- 6 edges to [[_COMMUNITY_Analyst Prompt & Vault Writer]]
- 5 edges to [[_COMMUNITY_Assemble & Gate Projection Modules]]
- 4 edges to [[_COMMUNITY_LLM Client Router (C4)]]
- 3 edges to [[_COMMUNITY_Desk CLI Bundle Assembly]]
- 3 edges to [[_COMMUNITY_AI Hub Card Property Tests (20-23)]]
- 2 edges to [[_COMMUNITY_BrainStore Decisions & Persistence]]
- 2 edges to [[_COMMUNITY_Cards Models (EvidenceCardCriticReview)]]
- 1 edge to [[_COMMUNITY_Brain Test Run Records Store]]
- 1 edge to [[_COMMUNITY_CLI IngestAuditBenchmark Commands]]
- 1 edge to [[_COMMUNITY_Provider Protocol & Capabilities]]
- 1 edge to [[_COMMUNITY_OHLCVRecord Model Field Validators]]
- 1 edge to [[_COMMUNITY_AI Hub CardCritic Contracts & Branches]]

## Top bridge nodes
- [[run_analyze_symbol()]] - degree 24, connects to 6 communities
- [[run_critique_spec()]] - degree 20, connects to 6 communities
- [[AnalystInputBundle]] - degree 14, connects to 6 communities
- [[main()_4]] - degree 10, connects to 6 communities
- [[RunnerError]] - degree 10, connects to 4 communities
