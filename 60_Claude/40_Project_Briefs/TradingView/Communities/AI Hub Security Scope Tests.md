---
type: community
members: 11
---

# AI Hub Security Scope Tests

**Members:** 11 nodes

## Members
- [[.test_env_listed_in_gitignore()]] - code - tests/test_security_scope.py
- [[.test_no_broker_sdk_in_dependencies()]] - code - tests/test_security_scope.py
- [[.test_no_execution_language_in_cli_help()]] - code - tests/test_security_scope.py
- [[.test_no_intraday_tick_options_paths()]] - code - tests/test_security_scope.py
- [[.test_no_llm_calls_in_ingestion_modules()]] - code - tests/test_security_scope.py
- [[.test_no_llm_imports_outside_agents_package()]] - code - tests/test_security_scope.py
- [[.test_no_predictive_language_in_cli_help()]] - code - tests/test_security_scope.py
- [[Extended C4 boundary (Phase 3).]] - rationale - tests/test_security_scope.py
- [[Security and scope boundary tests (Tasks 13.1–13.2).  Requirements 14.1, 14.5,]] - rationale - tests/test_security_scope.py
- [[TestSecurityAndScope]] - code - tests/test_security_scope.py
- [[test_security_scope.py]] - code - tests/test_security_scope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AI_Hub_Security_Scope_Tests
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_CLI IngestAuditBenchmark Commands]]
- 4 edges to [[_COMMUNITY_App Config Loading]]

## Top bridge nodes
- [[TestSecurityAndScope]] - degree 14, connects to 2 communities
- [[test_security_scope.py]] - degree 4, connects to 2 communities
