---
type: community
members: 10
---

# AI Hub Structural Guards (C4/D3)

**Members:** 10 nodes

## Members
- [[C4 LLM stack symbols only under agents (llm_client is the litellm site).]] - rationale - tests/test_ai_hub_security.py
- [[D3 GateHarnessConfig  Params never constructed with kwargs outside tests.]] - rationale - tests/test_ai_hub_security.py
- [[D3 hooks must not pull universesymbolscost-bps from params dict.]] - rationale - tests/test_ai_hub_security.py
- [[Structural guards for Phase 3 AI hub (C4, D3).]] - rationale - tests/test_ai_hub_security.py
- [[test_ai_hub_security.py]] - code - tests/test_ai_hub_security.py
- [[test_gate_harness_defaults_match_literature()]] - code - tests/test_ai_hub_security.py
- [[test_kronos_reserved_not_imported_under_agents()]] - code - tests/test_ai_hub_security.py
- [[test_llm_imports_only_under_agents()]] - code - tests/test_ai_hub_security.py
- [[test_no_nondefault_gate_params_outside_tests()]] - code - tests/test_ai_hub_security.py
- [[test_strategy_hooks_do_not_read_universe_from_params()]] - code - tests/test_ai_hub_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AI_Hub_Structural_Guards_C4/D3
SORT file.name ASC
```
