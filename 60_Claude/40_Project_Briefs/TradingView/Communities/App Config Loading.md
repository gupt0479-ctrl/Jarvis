---
type: community
cohesion: 0.18
members: 16
---

# App Config Loading

**Cohesion:** 0.18 - loosely connected
**Members:** 16 nodes

## Members
- [[AppConfig]] - code - src/research_data/config.py
- [[ConfigError]] - code - src/research_data/config.py
- [[Configuration loading and validation for research_data.  Loads and validates T]] - rationale - src/research_data/config.py
- [[Load and parse a TOML file, raising ConfigError on failure.]] - rationale - src/research_data/config.py
- [[Load and validate all configuration files.      Args         config_dir Pat]] - rationale - src/research_data/config.py
- [[Load and validate assets.toml configuration.]] - rationale - src/research_data/config.py
- [[Locate the config directory relative to the project root.      Searches from s]] - rationale - src/research_data/config.py
- [[Raised when configuration loading or validation fails.]] - rationale - src/research_data/config.py
- [[Top-level application configuration.]] - rationale - src/research_data/config.py
- [[Validate that the required API key is available in the environment.      Raise]] - rationale - src/research_data/config.py
- [[_find_config_dir()]] - code - src/research_data/config.py
- [[_load_toml_file()]] - code - src/research_data/config.py
- [[config.py]] - code - src/research_data/config.py
- [[load_assets_config()]] - code - src/research_data/config.py
- [[load_config()]] - code - src/research_data/config.py
- [[validate_api_key()]] - code - src/research_data/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/App_Config_Loading
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 7 edges to [[_COMMUNITY_Provider Config Loading & Validation]]
- 5 edges to [[_COMMUNITY_Provider Registry]]
- 3 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 2 edges to [[_COMMUNITY_Provider Registry Config-Loading Tests]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 2 edges to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 2 edges to [[_COMMUNITY_Provider Registry Internals]]
- 1 edge to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 1 edge to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]

## Top bridge nodes
- [[ConfigError]] - degree 18, connects to 9 communities
- [[AppConfig]] - degree 13, connects to 6 communities
- [[config.py]] - degree 13, connects to 3 communities
- [[load_config()]] - degree 8, connects to 3 communities
- [[validate_api_key()]] - degree 5, connects to 2 communities