---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Build Fable 5 TradingView year-ahead research base"
started_at: 2026-07-10T15:22:04
ended_at: 2026-07-10T18:01:44
duration_minutes: 160
exported_at: 2026-07-30T16:47:46.9270578+04:00
project: tradingview
cwd: '/home/anant_gupta/projects/hub/tradingview'
session_id: 92f7e8da-1704-4be4-9ed9-25c0398c4d75
status: raw
turn_count: 7
tools_used:
  Bash: 27
  Edit: 17
  mcp__jarvis__vault_append: 1
  mcp__jarvis__vault_patch: 6
  mcp__jarvis-fs__list_allowed_directories: 1
  Read: 21
  TaskCreate: 10
  TaskUpdate: 17
  ToolSearch: 4
  Write: 48
tokens:
  input: 123898
  output: 545537
  cache_creation: 1942725
  cache_read: 49943987
  total: 52556147
cost_usd: 117.314317
model:
  - claude-fable-5
files_touched:
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Fable 5 — Read Order (TradingView folder).md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Session Findings — Cursor Alignment Pass (2026-07-10).md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Math-First Map — Existing Code to Factor Brain.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/AI Market Analyzer - Strategy Engine.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Research - Systematic Equity Strategy Edge (2026-06-25).md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Research - Kronos Foundation Model Deep Dive (2026-06-25).md"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/models.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/storage.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/read_api.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/config.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/quality.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/providers/base.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/providers/csv_fixture.py"
  - "/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md"
  - "/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/env.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/__init__.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/models.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/loop.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_brain_store.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_brain_loop.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/packets.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ranking.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/momentum.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/safety.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/quality_fcf.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/etf_baseline.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ta_context.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/engine.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/__init__.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/synthetic.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_factors_math.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_factors_engine.py"
  - "/home/anant_gupta/projects/hub/tradingview/config/assets.toml"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/__init__.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/models.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/fmp.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/sec.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/store.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_income.json"
  - "/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_balance.json"
  - "/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_cashflow.json"
  - "/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_companyfacts.json"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_fundamentals.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/metrics.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/oos.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/monte_carlo.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/walk_forward.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/deflated_sharpe.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/harness.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/__init__.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_gates.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/__init__.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/models.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/store.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/engine.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_paper.py"
  - "/home/anant_gupta/projects/hub/tradingview/src/research_data/kronos_reserved.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_kronos_reserved.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/hooks_momentum.py"
  - "/home/anant_gupta/projects/hub/tradingview/tests/test_closed_loop.py"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/RESEARCH.md"
  - "/tmp/claude-1001/-home-anant-gupta-projects-hub-tradingview/92f7e8da-1704-4be4-9ed9-25c0398c4d75/tasks/bxgvbmmll.output"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Build Fable 5 TradingView year-ahead research base

## You

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## You

<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args></command-args>

## You

<local-command-stdout>Set model to [1mFable 5[22m and saved as your default for new sessions</local-command-stdout>

## You

# Fable 5 — TradingView year-ahead base (hard slice)

## Why
Build the durable personal US stocks/ETFs research desk base that should still be correct a year from now. Value = paper→real P&L + journal discipline. Software is private/personal-only (portfolio may mention it; never sold). Cursor Q&A session findings written under the vault TradingView folder are source of truth when notes conflict.

## How to run
- Long autonomous build: prefer weekly-quota depth. Do not stop or hand off early due to context/time anxiety. Continue until Definition of Done or a blocker only the user can resolve (missing secrets, irreversible action, true scope change).
- When you have enough information, act. Do not re-litigate settled law. Do not survey unused options.
- Before progress claims, audit against tool results from this session. Report test failures with output.
- Self-verify every ~60–90 minutes (or after each major module) against Definition of Done; fix gaps before expanding.
- Keep `Docs/fable5_run_memory.md`: short lessons (corrections + confirmed approaches). Read it at each work block. No duplicates of git/chat.
- Delegate independent subtasks to subagents; keep moving. No drive-by refactors. Simplest durable design.
- User-facing updates: outcome first. Never use BUY/SELL/guaranteed/risk-free language.

## Env (assume present — do not print secrets)
Repo: `/home/anant_gupta/projects/hub/tradingview`. Load `.env` only if gitignored (add safe dotenv load if missing). Expected vars: `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (format: `PersonalAITradingDesk email@domain`). Use live APIs when keys work; always keep fixtures + offline tests. Never commit `.env`. Redact secrets in stored metadata.

## Settled law
1. Personal-only local desk; no auth/tenancy/billing.
2. Stocks/ETFs only. Zero Kalshi/Polymarket code, schema fields, stubs, or shared-core placeholders.
3. Python owns facts/factors/tests/paper fills. AI proposes/explains from evidence only — never invents numbers.
4. Actions: WATCH|HOLD|ACCUMULATE|REDUCE|AVOID|INSUFFICIENT_DATA.
5. App = research hub (brain, strategies, review, charts/indicators). TradingView.com = later real-trade record — out of this build.
6. Brain module closed loop (x-factor): citation → proposed spec → human approve → Python hook → four gates → promote/demote → journal link → next proposal. Built alongside real DuckDB data (existing read_api/csv_fixture/polygon when keyed).
7. Factor core: momentum 12-1 rank, safety/vol rank, quality_fcf + valuation FCF/EV, ETF baseline vs VOO. TA (MA/RSI/Bollinger) = context only.
8. Kronos: reserved schema/gates only (USABLE + RankIC). No inference; no promote/demote influence.
9. Demo paper eligibility only after: OOS → Monte Carlo → walk-forward → deflated Sharpe (order fixed). Vs VOO; costs; drawdown; trade count; no lookahead; literature defaults.
10. Paper: pre-approve thesis → timed auto-entry in test windows; (a) accelerated historical replay writing journal-as-if-time-passed; (b) live calendar paper book with review jump-ahead hooks.
11. Differentiator: quant math first-class; test-gated self-improving lab + local journal; proof over narrative. Barebone = UX reference only.
12. Guardrails: no fabrication; quality caps confidence; no LLM in ingestion path; no broker SDKs; no options/futures/crypto/margin/intraday this phase.

## OUT OF SCOPE (Cursor later — do not own as main work)
.kiro leftovers: quality tests 7.2–7.4, evidence.py builder, benchmark.py, polygon.py completion, full CLI tasks 9–13. Use existing `src/research_data/` (models, storage, quality, read_api, normalization, calendar, csv_fixture). Implement polygon client only if required to unblock live prices and it is small; otherwise document for Cursor.

## IN SCOPE
### Read first
Vault folder (primary): `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\TradingView\` — especially session findings / decision notes written by Cursor Agent, plus Postmortem, RESEARCH, Strategy Engine, Systematic Equity Strategy Edge, Kronos (deferral only), Product Spec.
Also if needed: `60_Claude/20_Distilled_Notes/Trading Resources Integration — TradingView Architecture Roadmap.md`, Hermes distilled, AI-Assisted Trading.md (pipeline + anti-overfit). Ignore PM-execution pressure that violates settled law #2.
Repo: `.kiro/specs/data-ingestion-foundation/{design,tasks,requirements}.md`, `CLAUDE.md`, `src/research_data/**`, `config/**`, `tests/**`.

### Design notes
Patch/extend notes under vault `20_Progress/Projects/CS/TradingView/` by heading; preserve frontmatter keys. Do not touch `60_Claude/40_Project_Briefs/TradingView/`. Mirror architecture contract into `Docs/YEAR_AHEAD_BASE.md` in-repo.

### Build (order unless dependency forces otherwise)
1. Brain under `src/research_data/brain/` (or equivalent): citations, strategy specs proposed|approved, test-run records, promote/demote, paper-journal links — real persistence + APIs + tests.
2. Factor engine → structured score packets; expand `config/assets.toml` to 14 symbols if needed (VOO VTI SPY QQQ AAPL MSFT NVDA AMZN GOOGL META BRK.B JPM COST TSLA).
3. Minimal fundamentals: FMP + SEC (User-Agent from env); provenance; fixtures if offline; enough for FCF/EV, margins, debt.
4. Four-gate harness with real logic + tests; eligibility flag for demo paper.
5. Paper-test contracts/storage/APIs (UI thin OK).
6. Kronos reserved fields/docs only.

## Definition of Done
Durable year-ahead base exists: vault notes updated + `Docs/YEAR_AHEAD_BASE.md` + working brain loop + factor(+fundamentals) math + four-gate harness + paper-test contracts + Kronos reserved, with tests run and results reported honestly. Also: how to run, Cursor-only leftovers, open risks.

## Start
Read vault TradingView folder + repo state → write/update `Docs/YEAR_AHEAD_BASE.md` → implement brain → factors/fundamentals → gates → paper contracts → self-verify → stop at Done or true blocker.

## Claude

Starting the year-ahead base build. First I'll load the vault filesystem tools and survey the current repo state in parallel.

The vault isn't reachable via jarvis-fs (repo-only). I'll try the WSL mount and the jarvis vault MCP tools.

I have the contract. Now reading the remaining key research notes plus the repo's actual code in parallel.

I have the research context locked. Now reading the repo's actual code spine so the new packages integrate cleanly.

Docs done. Now the brain module — starting with the small safe `.env` loader, then brain models.

Now the brain package — models first.

Brain package written. Now its tests.

Two timestamp round-trip failures — likely DuckDB converting tz-aware datetimes to local time on insert. Verifying, then fixing the store to normalize to naive UTC.

Confirmed: DuckDB stores tz-aware datetimes as naive *local* time. Fixing by normalizing to naive UTC on write.

Seed 4 gives TSLA the intended profile (−40% return, 0.49 vol). Updating the test.

Factors green. Expanding the universe to 14 symbols.

The append ran but the symbols-line edit was rejected (file not Read via the Read tool). Fixing.

Now fundamentals fixtures and tests.

Fundamentals done (13 tests). Now the four-gate harness — the statistical core.

Now the harness that runs the gates in fixed order and records to the brain.

The harness needs `BrainStore.list_runs_for_gate` — adding it.

Gates done (23 tests). Now the paper-test contracts.

Now paper tests.

Transient harness error — retrying the test run.

While Bash is temporarily unavailable, I'll continue writing the Kronos reservation and the closed-loop integration test, then run everything together.

Bash is still throttled. I'll log lessons to run memory, then retry.

While waiting out the throttle, I'll patch the stable vault notes (the parts that don't depend on final test counts).

You've hit your session limit · resets 9pm (Asia/Dubai)

**Tool calls:**

- `ToolSearch` — `{"query":"select:mcp__jarvis-fs__read_text_file,mcp__jarvis-fs__list_directory,mcp__jarvis-fs__directory_tree,mcp__jarvis-fs__search_files,mcp__jarvis-fs__edit_file,mcp__jarvis-fs__write_file,mcp__jarvis-fs__list_allowed_directories","max_results":7}`
- `Bash` — `find /home/anant_gupta/projects/hub/tradingview -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" \) -not -path "*/.venv/*" -not -path "*/.git/*" | sort`
  ```
<persisted-output>
Output too large (238.2KB). Full output saved to: /home/anant_gupta/.claude/projects/-home-anant-gupta-projects-hub-tradingview/[REDACTED]/tool-results/bk8afouxe.txt

Preview (first 2KB):
/home/anant_gupta/projects/hub/tradingview/.claude/agents/guardrail-auditor.md
/home/anant_gupta/projects/hub/tradingview/.claude/agents/spec-implementer.md
/home/anant_gupta/projects/hub/tradingview/.claude/skills/guardrail-check/SKILL.md
/home/anant_gupta/projects/hub/tradingview/.claude/skills/kiro-status/SKILL.md
/home/anant_gupta/projects/hub/tradingview/.kiro/specs/data-ingestion-foundation/design.md
/home/anant_gupta/projects/hub/tradingview/.kiro/specs/data-ingestion-foundation/requirements.md
/home/anant_gupta/projects/hub/tradingview/.kiro/specs/data-ingestion-foundation/tasks.md
/home/anant_gupta/projects/hub/tradingview/.pytest_cache/README.md
/home/anant_gupta/projects/hub/tradingview/CLAUDE.md
/home/anant_gupta/projects/hub/tradingview/Docs/RESEARCH.md
/home/anant_gupta/projects/hub/tradingview/README.md
/home/anant_gupta/projects/hub/tradingview/config/assets.toml
/home/anant_gupta/projects/hub/tradingview/config/providers.toml
/home/anant_gupta/projects/hub/tradingview/graphify-out/GRAPH_REPORT.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/00 Overview.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/2026 Research Baseline (FinGPTFinRobotFINRASEC).md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/AI-Ready Evidence Contract & Schemas.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/Adjusted Close Positivity Rule.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/Adjustment Policy CaseWhitespace Normalization.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/Adjustment Policy Empty String - UNKNOWN.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/Adjustment Policy Mapping Tests.md
/home/anant_gupta/projects/hub/tradingview/graphify-out/jarvis_curated/Communities/Adjustment Policy Unknown String - UNKNOWN.md
...
</persisted-output>
  ```
- `mcp__jarvis-fs__list_allowed_directories` — `{}`
- `Bash` — `ls -R /home/anant_gupta/projects/hub/tradingview/src /home/anant_gupta/projects/hub/tradingview/tests /home/anant_gupta/projects/hub/tradingview/Docs /home/anant_gupta/projects/hub/tradingview/config 2>/dev/null; echo ---; ls /home/anant_gupta/projects/hub/tradingview; echo ---; cat /home/anant_gupta/projects/hub/tradingview/.gitignore 2>/dev/null`
  ```
/home/anant_gupta/projects/hub/tradingview/Docs:
Quant Foundations.pdf
Quant Foundations.pdf:Zone.Identifier
RESEARCH.md

/home/anant_gupta/projects/hub/tradingview/config:
assets.toml
providers.toml

/home/anant_gupta/projects/hub/tradingview/src:
research_data
research_data.egg-info

/home/anant_gupta/projects/hub/tradingview/src/research_data:
__init__.py
__pycache__
calendar.py
config.py
models.py
normalization.py
providers
quality.py
read_api.py
storage.py

/home/anant_gupta/projects/hub/tradingview/src/research_data/__pycache__:
__init__.cpython-312.pyc
calendar.cpython-312.pyc
config.cpython-312.pyc
models.cpython-312.pyc
normalization.cpython-312.pyc
quality.cpython-312.pyc
storage.cpython-312.pyc

/home/anant_gupta/projects/hub/tradingview/src/research_data/providers:
__init__.py
__pycache__
base.py
csv_fixture.py

/home/anant_gupta/projects/hub/tradingview/src/research_data/providers/__pycache__:
__init__.cpython-312.pyc
base.cpython-312.pyc
csv_fixture.cpython-312.pyc

/home/anant_gupta/projects/hub/tradingview/src/research_data.egg-info:
PKG-INFO
SOURCES.txt
dependency_links.txt
requires.txt
top_level.txt

/home/anant_gupta/projects/hub/tradingview/tests:
__init__.py
__pycache__
fixtures
test_calendar.py
test_models.py
test_models_validation.py
test_normalization.py
test_property_adjustment_mapping.py
test_property_duplicate_pk.py
test_property_market_calendar.py
test_property_no_fabrication.py
test_property_no_secrets.py
test_property_ohlcv_validation.py
test_property_provider_registry.py
test_property_raw_payload_hash.py
test_property_roundtrip.py
test_provider_registry.py
test_storage.py

/home/anant_gupta/projects/hub/tradingview/tests/__pycache__:
__init__.cpython-312.pyc
test_calendar.cpython-312-pytest-9.0.3.pyc
test_models.cpython-312-pytest-9.0.3.pyc
test_models_validation.cpython-312-pytest-9.0.3.pyc
test_normalization.cpython-312-pytest-9.0.3.pyc
test_property_adjustment_mapping.cpython-312-pytest-9.0.3.pyc
test_property_duplicate_pk.cpython-312-pytest-9.0.3.pyc
test_property_market_calendar.cpython-312-pytest-9.0.3.pyc
test_property_no_fabrication.cpython-312-pytest-9.0.3.pyc
test_property_no_secrets.cpython-312-pytest-9.0.3.pyc
test_property_ohlcv_validation.cpython-312-pytest-9.0.3.pyc
test_property_provider_registry.cpython-312-pytest-9.0.3.pyc
test_property_raw_payload_hash.cpython-312-pytest-9.0.3.pyc
test_property_roundtrip.cpython-312-pytest-9.0.3.pyc
test_provider_registry.cpython-312-pytest-9.0.3.pyc
test_storage.cpython-312-pytest-9.0.3.pyc

/home/anant_gupta/projects/hub/tradingview/tests/fixtures:
MSFT.csv
SPY.csv
VOO.csv
---
CLAUDE.md
Docs
README.md
config
graphify-out
pyproject.toml
src
tests
---
# Python
__pycache__/
*.py[cod]
*.egg-info/
.eggs/
build/
dist/

# Virtual environment
.venv/
venv/

# Test / property-testing caches
.pytest_cache/
.hypothesis/

# Environment / secrets
.env
.env.*
!.env.example

# Local research data (raw payloads, DuckDB files) - regenerated locally, never committed
data/

# Claude Code personal/local settings (project-shared config lives in .claude/settings.json)
.claude/settings.local.json

# graphify knowledge-graph output (regenerated locally, copied into Jarvis manually)
graphify-out/

# Windows NTFS zone-identifier artifacts picked up via WSL mounts
*Zone.Identifier*

# OS
.DS_Store
  ```
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_list,mcp__jarvis__vault_read,mcp__jarvis__vault_write,mcp__jarvis__vault_patch,mcp__jarvis__search_simple","max_results":5}`
- `Bash` — `ls "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/" 2>&1`
  ```
AI Market Analyzer - 4 Month Build Plan.md
AI Market Analyzer - AI Engine Architecture.md
AI Market Analyzer - Data Sources.md
AI Market Analyzer - Product Spec.md
AI Market Analyzer - Strategy Engine.md
Fable 5 — Read Order (TradingView folder).md
Links.md
Math-First Map — Existing Code to Factor Brain.md
Postmortem - Stocks-ETFs First, Prediction Markets Second.md
RESEARCH.md
Reddit.md
Research - Kronos Foundation Model Deep Dive (2026-06-25).md
Research - Systematic Equity Strategy Edge (2026-06-25).md
Research - Trading Fundamentals Gap Fill (2026-06-25).md
Session Findings — Cursor Alignment Pass (2026-07-10).md
Trading Tools and Platforms.md
Trading with Ai.md
Trading.md
Year-Ahead Base — Fable 5 Architecture Contract.md
  ```
- `Bash` — `cd "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/" && wc -c *.md | sort -n`
  ```
   708 Trading.md
  2080 Fable 5 — Read Order (TradingView folder).md
  2610 Links.md
  3368 Trading Tools and Platforms.md
  4572 AI Market Analyzer - Product Spec.md
  5242 Reddit.md
  5641 Trading with Ai.md
  5813 AI Market Analyzer - Data Sources.md
  6496 Math-First Map — Existing Code to Factor Brain.md
  7243 Year-Ahead Base — Fable 5 Architecture Contract.md
  8163 AI Market Analyzer - 4 Month Build Plan.md
 10480 AI Market Analyzer - AI Engine Architecture.md
 12378 Postmortem - Stocks-ETFs First, Prediction Markets Second.md
 13536 Research - Kronos Foundation Model Deep Dive (2026-06-25).md
 13794 Session Findings — Cursor Alignment Pass (2026-07-10).md
 15145 Research - Systematic Equity Strategy Edge (2026-06-25).md
 15534 Research - Trading Fundamentals Gap Fill (2026-06-25).md
 18908 AI Market Analyzer - Strategy Engine.md
 33011 RESEARCH.md
184722 total
Shell cwd was reset to /home/anant_gupta/projects/hub/tradingview
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Fable 5 — Read Order (TradingView folder).md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Session Findings — Cursor Alignment Pass (2026-07-10).md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Math-First Map — Existing Code to Factor Brain.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/AI Market Analyzer - Strategy Engine.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Research - Systematic Equity Strategy Edge (2026-06-25).md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Research - Kronos Foundation Model Deep Dive (2026-06-25).md`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/models.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/storage.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/read_api.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/config.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/quality.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/providers/base.py`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/providers/csv_fixture.py`
- `Bash` — `cat config/assets.toml config/providers.toml pyproject.toml && ls -la .env* 2>/dev/null; head -3 tests/fixtures/VOO.csv; wc -l tests/fixtures/*.csv`
  ```
# V1 Universe - Initial set of symbols for research data ingestion
# These are major US equity ETFs and large-cap stocks

[universe]
name = "v1"
description = "Initial research universe: broad ETFs and mega-cap equities"
symbols = ["VOO", "VTI", "SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META"]

[benchmarks]
default = "VOO"

[benchmarks.mappings]
VOO = "S&P 500 ETF (Vanguard)"
VTI = "Total Stock Market ETF (Vanguard)"
SPY = "S&P 500 ETF (SPDR)"
QQQ = "Nasdaq-100 ETF (Invesco)"

[assets.VOO]
symbol = "VOO"
asset_type = "etf"
name = "Vanguard S&P 500 ETF"
exchange = "NYSE"
currency = "USD"
benchmark_symbol = "VOO"

[assets.VTI]
symbol = "VTI"
asset_type = "etf"
name = "Vanguard Total Stock Market ETF"
exchange = "NYSE"
currency = "USD"
benchmark_symbol = "VOO"

[assets.SPY]
symbol = "SPY"
asset_type = "etf"
name = "SPDR S&P 500 ETF Trust"
exchange = "NYSE"
currency = "USD"
benchmark_symbol = "VOO"

[assets.QQQ]
symbol = "QQQ"
asset_type = "etf"
name = "Invesco QQQ Trust"
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.AAPL]
symbol = "AAPL"
asset_type = "equity"
name = "Apple Inc."
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.MSFT]
symbol = "MSFT"
asset_type = "equity"
name = "Microsoft Corporation"
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.NVDA]
symbol = "NVDA"
asset_type = "equity"
name = "NVIDIA Corporation"
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.AMZN]
symbol = "AMZN"
asset_type = "equity"
name = "Amazon.com Inc."
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.GOOGL]
symbol = "GOOGL"
asset_type = "equity"
name = "Alphabet Inc. Class A"
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.META]
symbol = "META"
asset_type = "equity"
name = "Meta Platforms Inc."
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"
# Provider configuration for research data ingestion
# Each provider must include: source_name, source_url, license_note,
# requires_api_key, rate_limit, adjustment_policy

[default]
provider = "polygon"

[providers.polygon]
source_name = "polygon"
source_url = "https://api.polygon.io"
license_note = "Polygon Basic plan - free tier with end-of-day data, 2 years history, 5 calls/minute"
requires_api_key = true
rate_limit = 5
adjustment_policy = "split_dividend_adjusted"
api_key_env_var = "POLYGON_API_KEY"
supports_daily_ohlcv = true
supports_adjusted_prices = true
supports_corporate_actions = true
min_history_years_free = 2.0
experimental = false

[providers.csv_fixture]
source_name = "csv_fixture"
source_url = "file://tests/fixtures/"
license_note = "Local test fixtures - no external data license required"
requires_api_key = false
rate_limit = 0
adjustment_policy = "split_dividend_adjusted"
supports_daily_ohlcv = true
supports_adjusted_prices = true
supports_corporate_actions = false
min_history_years_free = 0.5
experimental = false

[providers.tiingo]
source_name = "tiingo"
source_url = "https://api.tiingo.com"
license_note = "Tiingo EOD - verify current terms before production use"
requires_api_key = true
rate_limit = 50
adjustment_policy = "split_dividend_adjusted"
api_key_env_var = "TIINGO_API_KEY"
supports_daily_ohlcv = true
supports_adjusted_prices = true
supports_corporate_actions = false
min_history_years_free = 5.0
experimental = false

[providers.alpha_vantage]
source_name = "alpha_vantage"
source_url = "https://www.alphavantage.co"
license_note = "Alpha Vantage - free tier with daily compact limits"
requires_api_key = true
rate_limit = 5
adjustment_policy = "split_adjusted"
api_key_env_var = "ALPHA_VANTAGE_API_KEY"
supports_daily_ohlcv = true
supports_adjusted_prices = true
supports_corporate_actions = false
min_history_years_free = 20.0
experimental = false

[providers.fmp]
source_name = "fmp"
source_url = "https://financialmodelingprep.com/api"
license_note = "FMP - verify current plan limits before production use"
requires_api_key = true
rate_limit = 10
adjustment_policy = "split_dividend_adjusted"
api_key_env_var = "FMP_API_KEY"
supports_daily_ohlcv = true
supports_adjusted_prices = true
supports_corporate_actions = true
min_history_years_free = 5.0
experimental = false
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "research-data"
version = "0.1.0"
description = "Provider-agnostic market data ingestion and quality auditing for research"
requires-python = ">=3.11"
dependencies = [
    "pydantic>=2.0",
    "duckdb>=0.9",
    "typer>=0.9",
    "tomli>=2.0;python_version<'3.11'",
    "hypothesis>=6.0",
    "pytest>=7.0",
    "exchange_calendars>=4.5",
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
-rw-r--r-- 1 anant_gupta anant_gupta 155 Jul 10 19:30 .env
date,open,high,low,close,volume,adjusted_close
2024-01-02,454.32,458.08,453.8,455.68,3657290,455.68
2024-01-03,452.13,453.82,449.87,452.03,3382181,452.03
   66 tests/fixtures/MSFT.csv
   66 tests/fixtures/SPY.csv
   66 tests/fixtures/VOO.csv
  198 total
  ```
- `ToolSearch` — `{"query":"select:TaskCreate,TaskUpdate,TaskList","max_results":3}`
- `Bash` — `cut -d= -f1 .env && source .venv/bin/activate && python -m pytest -q 2>&1 | tail -5`
  ```
POLYGON_API_KEY
FMP_API_KEY
SEC_USER_AGENT
........................................................................ [ 28%]
........................................................................ [ 56%]
........................................................................ [ 84%]
.......................................                                  [100%]
255 passed in 25.15s
  ```
- `TaskCreate` — `{"subject":"Write Docs/YEAR_AHEAD_BASE.md + Docs/fable5_run_memory.md","description":"Mirror the vault architecture contract into the repo; start the run-memory file with lessons."}`
- `TaskCreate` — `{"subject":"Implement brain module (citations, specs, test runs, promote/demote, journal links)","description":"src/research_data/brain/: pydantic models + DuckDB persistence + closed-loop APIs (propose → human approve → hook → gates → promote/demote → journal). Tests included."}`
- `TaskCreate` — `{"subject":"Implement factor engine + score packets + long fixtures; expand universe to 14 symbols","description":"src/research_data/factors/: momentum 12-1 rank, safety vol rank, quality_fcf composite, valuation FCF/EV, ETF baseline vs VOO, TA context-only. Deterministic long CSV fixtures (2y+) for tests. assets.toml → 14 symbols (add BRK.B→BRKB handling, JPM, COST, TSLA)."}`
- `TaskCreate` — `{"subject":"Implement minimal fundamentals path (FMP + SEC EDGAR)","description":"src/research_data/fundamentals/: snapshot model with provenance, FMP client, SEC companyfacts client (SEC_USER_AGENT), DuckDB store, offline fixtures. Enough for FCF/EV, margins, debt."}`
- `TaskCreate` — `{"subject":"Implement four-gate promotion harness","description":"src/research_data/gates/: OOS → Monte Carlo → walk-forward → deflated Sharpe (fixed order), pure-python math (NormalDist), costs/drawdown/trade-count, vs-VOO comparison, eligibility flag, records to brain. Tests with synthetic series."}`
- `TaskCreate` — `{"subject":"Implement paper-test contracts (thesis approval, timed entry, replay journal, live book)","description":"src/research_data/paper/: models + DuckDB store + engine for pre-approved thesis → timed auto-entry in windows; replay mode writing journal-as-if-time-passed; live book with review jump-ahead hooks; voo_return_same_period required on exits."}`
- `TaskCreate` — `{"subject":"Reserve Kronos schema/gates (no inference)","description":"KronosForecastEvidence model with required model_rankic_on_universe, RANKIC_MIN=0.03 gate, USABLE-only guard. Docs. Zero inference code."}`
- `TaskCreate` — `{"subject":"Closed-loop integration test (citation → spec → approve → hook → gates → promote → journal)","description":"One end-to-end test exercising the full brain x-factor loop on fixture data."}`
- `TaskCreate` — `{"subject":"Update vault notes to match what was built","description":"Patch vault TradingView notes by heading (preserve frontmatter); do not touch 60_Claude/40_Project_Briefs."}`
- `TaskCreate` — `{"subject":"Self-verify: full pytest, guardrail sweep, honest final report","description":"Run all tests, /guardrail-check-style sweep, verify Definition of Done, report failures honestly, list Cursor leftovers and open risks."}`
- `TaskUpdate` — `{"taskId":"1","status":"in_progress","activeForm":"Writing YEAR_AHEAD_BASE.md and run memory"}`
- `Write` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
  ```
# Year-Ahead Base — Architecture Contract (repo mirror)

> Mirror of the vault note `20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md`
> (decisions locked in `Session Findings — Cursor Alignment Pass (2026-07-10)`). If this file and the vault
> conflict, the vault session-findings note wins. Built by Fable 5, 2026-07-10.

## One-sentence goal

Leave a durable base for this personal US stocks/ETFs research desk that is still correct a year from now:
brain loop, factor(+fundamentals) math, four-gate promotion, paper-test contracts, Kronos reserved — not a
disposable demo.

## Settled law (do not re-open)

1. Personal-only local desk; no auth/tenancy/billing; never sold (portfolio may mention it).
2. Stocks/ETFs only. Zero Kalshi/Polymarket code, schema fields, stubs, or shared-core placeholders.
3. Python owns facts/factors/tests/paper fills. AI proposes/explains from evidence only — never invents numbers.
4. Action vocabulary everywhere: `WATCH | HOLD | ACCUMULATE | REDUCE | AVOID | INSUFFICIENT_DATA`.
5. This app is the research hub. TradingView.com = later real-trade record — out of this build.
6. Brain closed loop is the x-factor: citation → proposed spec → **human approve** → Python hook → four gates →
   promote/demote → journal link → next proposal.
7. Primary math = fixed factor stack (momentum 12-1, safety/vol, quality_fcf, valuation FCF/EV, ETF baseline
   vs VOO). TA (MA/RSI/Bollinger) = context only, never a sole action driver.
8. Kronos: reserved schema/gates only (USABLE-only input, RankIC ≥ 0.03 threshold). No inference, no
   promote/demote influence, until a RankIC validation pass happens later.
9. Demo-paper eligibility only after all four gates pass **in order**: out-of-sample → Monte Carlo →
   walk-forward → deflated Sharpe. Always vs VOO; costs, drawdown, trade count; no lookahead;
   literature-default parameters over curve-fit.
10. Paper trading: pre-approved thesis → timed auto-entry inside approved test windows. Two modes:
    (a) accelerated historical replay writing journal-as-if-time-passed; (b) live-calendar paper book with
    review jump-ahead hooks.
11. Guardrails: no fabrication; quality caps confidence; no LLM calls in the ingestion path; no broker SDKs;
    no options/futures/crypto/margin/intraday this phase; no execution language (`BUY`/`SELL`/"guaranteed"/
    "risk-free") anywhere.

## Module map

```text
src/research_data/
  models.py            # OHLCV + quality + evidence-packet models (ingestion spine — keep clean)
  config.py            # providers.toml / assets.toml loaders, API-key env validation
  env.py               # safe .env loader (gitignored file only; values never logged)
  storage.py           # DuckDB ingestion schema: daily_ohlcv, raw payloads, runs, quality reports
  normalization.py     # ProviderFetchResult → OHLCVRecord (prices only; no factor logic here)
  calendar.py          # NYSE/NASDAQ session math (shared by quality, factors, gates, paper)
  quality.py           # DataQualityAuditor: MISSING > CONTRADICTORY > STALE > INSUFFICIENT_DATA > PARTIAL > USABLE
  read_api.py          # PriceReadAPI.get_price_frame — sole price read path for downstream modules
  kronos_reserved.py   # Kronos evidence schema + admission gates ONLY — no inference imports
  providers/           # csv_fixture (offline default), polygon/tiingo/alpha_vantage/fmp price clients
  brain/               # THE X-FACTOR — closed research loop
    models.py          #   Citation, StrategySpec (proposed|approved|rejected|retired), TestRunRecord,
                       #   PromotionDecision, JournalLink
    store.py           #   BrainStore: DuckDB persistence + typed APIs (approve requires a human identity)
    loop.py            #   Loop rules: legal state transitions, gate-order enforcement, eligibility
  factors/             # deterministic scorers → structured score packets
    packets.py         #   ScorePacket + sub-score models (formula, inputs, as_of on every score)
    momentum.py        #   12-1 month total-return rank in universe
    safety.py          #   inverse rank of 12m realized vol (annualized σ of daily returns)
    quality_fcf.py     #   composite: FCF/EV, FCF margin, op-margin stability, debt (needs fundamentals)
    etf_baseline.py    #   symbol vs VOO on overlapping usable sessions
    ta_context.py      #   SMA50/200, RSI14, Bollinger, 52w drawdown — DESCRIPTIVE ONLY
    engine.py          #   FactorEngine: universe prices+fundamentals → packets (quality caps confidence)
  fundamentals/        # minimal FCF/EV-margins-debt path
    models.py          #   FundamentalsSnapshot (per statement period, full provenance)
    fmp.py             #   FMP statements client (FMP_API_KEY)
    sec.py             #   SEC EDGAR companyfacts client (SEC_USER_AGENT header, fair-access rate limit)
    store.py           #   fundamentals_snapshots DuckDB table + read API
  gates/               # four-gate promotion harness (order fixed)
    metrics.py         #   returns, Sharpe, max drawdown, trade count, cost model (bps per side)
    oos.py             #   gate 1: time-ordered train/test split, OOS degradation + net-Sharpe check
    monte_carlo.py     #   gate 2: seeded bootstrap of daily returns, tail-percentile checks
    walk_forward.py    #   gate 3: rolling windows, fraction-positive + pooled OOS Sharpe
    deflated_sharpe.py #   gate 4: Bailey/López de Prado DSR with trial count from brain test records
    harness.py         #   runs gates in order, writes TestRunRecords, sets demo-paper eligibility
  paper/               # paper-test contracts (UI thin; storage/APIs real)
    models.py          #   Thesis (pre-approval required), PaperFill (open|close — no BUY/SELL words),
                       #   JournalEntry (voo_return_same_period required on close), ReplayRun
    store.py           #   PaperStore: DuckDB persistence
    engine.py          #   timed auto-entry inside approved windows; replay writes journal as-if-time-passed
tests/                 # offline by default; property tests prefixed test_property_
  fixtures/            # short CSVs (ingestion tests) + long/ (2y+ synthetic OHLCV for factor/gate tests)
                       # + fundamentals/ (statement fixtures)
config/
  assets.toml          # 14-symbol universe: VOO VTI SPY QQQ AAPL MSFT NVDA AMZN GOOGL META BRKB JPM COST TSLA
  providers.toml       # price + fundamentals providers; API keys via env vars only
Docs/
  YEAR_AHEAD_BASE.md   # this file — keep the module map accurate when files move
  fable5_run_memory.md # short lessons from the build run (corrections + confirmed approaches)
```

## Data flow

```text
provider APIs → raw payloads (disk + DuckDB, secrets redacted)
  → normalization → daily_ohlcv → DataQualityAuditor → PriceReadAPI
  → factors (deterministic math, quality-capped confidence) ┐
  fundamentals (FMP/SEC, provenance per field) ─────────────┤
                                                            ▼
                                              ScorePacket (typed, as-of, provenance)
                                                            ▼
brain: citation → proposed spec → human approve → Python hook (strategy returns)
  → gates harness (OOS → MC → WF → DSR, vs VOO, costs) → promote/demote decision
  → paper: approved thesis → timed auto-entry (replay or live book) → journal (+VOO same-period)
  → journal lesson feeds the next proposal        [AI agents consume packets only — later phase]
```

## The four gates (fixed order, literature defaults)

| # | Gate | Default pass rule | Source |
|---|---|---|---|
| 1 | Out-of-sample | time-ordered split (70/30); OOS net Sharpe > 0 AND OOS Sharpe ≥ 0.5 × in-sample Sharpe | Pardo 1992 degradation heuristic |
| 2 | Monte Carlo | seeded bootstrap (1000 paths) of daily net returns; 5th-percentile annualized return > 0 | resampling stress standard |
| 3 | Walk-forward | rolling train 504 / test 126 bars; ≥ 60% of OOS windows positive AND pooled OOS Sharpe > 0 | Pardo 1992 |
| 4 | Deflated Sharpe | DSR probability ≥ 0.95, trial count taken from recorded brain test runs | Bailey & López de Prado 2014/2018 |

Every gate report includes: net-of-cost returns (default 5 bps/side), max drawdown, trade count, and the
same-window VOO comparison. A failed gate is recorded, never silent — the spec is not demo-eligible.

## Fundamentals field set (minimal, provenance on every field)

revenue, operating_income (→ operating margin), operating cash flow, capex (→ FCF = OCF − capex),
total_debt, cash_and_equivalents, shares_outstanding, equity. Derived at scoring time with explicit as-of:
market_cap = price × shares; EV = market_cap + total_debt − cash; FCF/EV; FCF margin; debt/equity.
ETFs have no issuer fundamentals → quality/valuation scores return `INSUFFICIENT_DATA`, never a synthesized value.

## Kronos reservation (no inference)

`kronos_reserved.py` defines the evidence shape a future Kronos integration must fill
(`model_rankic_on_universe` is required — untested forecasts cannot surface) and two admission gates:
input quality must be `USABLE`, and validated RankIC ≥ 0.03 on this universe. Nothing downloads or runs
the model; nothing feeds promote/demote.

## Out of scope here (Cursor next / later phases)

- `.kiro` leftovers: quality tests 7.2–7.4, `evidence.py` builder, `benchmark.py`, polygon client completion,
  CLI tasks 9–13.
- Multi-agent debate layer, Streamlit UI, charting library choice.
- Kronos download/inference + RankIC validation pass.
- Real-money surface, TradingView.com record-keeping, Kalshi/Polymarket vertical (only after paper readiness).

## How to run

```bash
source .venv/bin/activate
pip install -e .          # once
pytest                    # offline; all tests must pass without network or keys
```

Live keys (`.env`, gitignored): `POLYGON_API_KEY`, `FMP_API_KEY`,
`SEC_USER_AGENT` (format `PersonalAITradingDesk email@domain`). `research_data.env.load_dotenv()` loads them
safely; values are never printed or stored unredacted.

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```
# Fable 5 run memory — year-ahead base build (started 2026-07-10)

Short lessons only: corrections + confirmed approaches. Read at each work block. No duplication of git/chat.

## Confirmed approaches

- Vault is reachable at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/`
  (WSL mount). `jarvis-fs` MCP only allows the repo; use plain file reads/writes on the mount for vault edits.
- Source of truth on conflicts: `Session Findings — Cursor Alignment Pass (2026-07-10).md`.
- Baseline before any new code: 255 tests passed (2026-07-10). Any regression below that is mine.
- Keep dependencies minimal: gates math in pure Python (`statistics.NormalDist` has cdf + inv_cdf — no scipy);
  HTTP via `urllib.request` (requests/httpx are not project deps).
- Existing short fixtures (65 rows) are for ingestion tests; factor/gate tests need 2y+ deterministic synthetic
  fixtures under `tests/fixtures/long/` — synthetic *test* data is fine, fabricated *product* data is not.
- `BRK.B` fails the `^[A-Z]{1,10}$` symbol rule → use `BRKB` in the universe with a note (provider clients map
  to their own punctuation, e.g. Polygon `BRK.B`, SEC `BRK-B`).

## Corrections

- (none yet)

  ```
- `TaskUpdate` — `{"taskId":"1","status":"completed"}`
- `TaskUpdate` — `{"taskId":"2","status":"in_progress","activeForm":"Implementing brain module"}`
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/env.py`
  ```
"""Safe .env loading for local development.

Loads KEY=VALUE pairs from a gitignored .env file into os.environ without
overriding variables that are already set, and without ever logging or
returning secret values. No third-party dependency.
"""

from __future__ import annotations

import os
from pathlib import Path


def _project_root() -> Path:
    """Project root is two levels up from src/research_data/."""
    return Path(__file__).resolve().parent.parent.parent


def load_dotenv(path: str | Path | None = None) -> list[str]:
    """Load environment variables from a .env file if it exists.

    Existing environment variables are never overridden. Values are never
    logged or echoed; only the variable *names* that were newly set are
    returned, so callers can report what was loaded without leaking secrets.

    Args:
        path: Path to the .env file. Defaults to <project root>/.env.

    Returns:
        Sorted list of variable names that were newly set (may be empty).
    """
    env_path = Path(path) if path is not None else _project_root() / ".env"
    if not env_path.is_file():
        return []

    loaded: list[str] = []
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key or key in os.environ:
            continue
        os.environ[key] = value
        loaded.append(key)

    return sorted(loaded)

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/__init__.py`
  ```
"""Brain module — the closed research loop (the x-factor of this desk).

citation → proposed spec → human approve → Python hook → four gates →
promote/demote → journal link → next proposal.

AI may propose strategy specs; only a human may approve them; only the
four-gate harness may make a spec demo-paper eligible. Every transition is
persisted with evidence references so the loop is auditable a year from now.

Public surface: models + BrainStore + loop rules. Keep it thin.
"""

from research_data.brain.models import (
    GATE_ORDER,
    Citation,
    GateName,
    JournalLink,
    PromotionDecision,
    PromotionState,
    SpecStatus,
    StrategySpec,
    TestRunRecord,
)
from research_data.brain.store import BrainStore
from research_data.brain.loop import (
    BrainLoopError,
    gate_sequence_passes,
    is_demo_eligible,
    record_gate_outcome_decision,
    resolve_hook,
)

__all__ = [
    "GATE_ORDER",
    "BrainLoopError",
    "BrainStore",
    "Citation",
    "GateName",
    "JournalLink",
    "PromotionDecision",
    "PromotionState",
    "SpecStatus",
    "StrategySpec",
    "TestRunRecord",
    "gate_sequence_passes",
    "is_demo_eligible",
    "record_gate_outcome_decision",
    "resolve_hook",
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/models.py`
  ```
"""Typed records for the brain closed loop.

Every model here is an auditable fact: who proposed what, based on which
citations, which gates ran with which inputs/outputs, and why a spec was
promoted or demoted. Nothing in this module fetches data or calls an LLM.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _new_id() -> str:
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class SpecStatus(str, Enum):
    """Lifecycle of a strategy spec. Only a human moves PROPOSED → APPROVED."""

    PROPOSED = "proposed"
    APPROVED = "approved"
    REJECTED = "rejected"
    RETIRED = "retired"


class PromotionState(str, Enum):
    """Where a spec stands against the four-gate promotion wall."""

    UNPROVEN = "unproven"
    DEMO_ELIGIBLE = "demo_eligible"
    DEMOTED = "demoted"


class GateName(str, Enum):
    """The four promotion gates. Order is fixed and non-negotiable."""

    OUT_OF_SAMPLE = "out_of_sample"
    MONTE_CARLO = "monte_carlo"
    WALK_FORWARD = "walk_forward"
    DEFLATED_SHARPE = "deflated_sharpe"


#: Fixed gate order: OOS → Monte Carlo → walk-forward → deflated Sharpe.
GATE_ORDER: tuple[GateName, ...] = (
    GateName.OUT_OF_SAMPLE,
    GateName.MONTE_CARLO,
    GateName.WALK_FORWARD,
    GateName.DEFLATED_SHARPE,
)


class DecisionKind(str, Enum):
    """Kinds of promotion decisions recorded in the loop."""

    PROMOTE = "promote"
    DEMOTE = "demote"
    HOLD = "hold"


# Identities that must never appear as a human approver. The human gate is a
# product guarantee, not a formality; this is a tripwire, not authentication.
_NON_HUMAN_IDENTITIES = frozenset(
    {"ai", "agent", "assistant", "bot", "claude", "cursor", "fable", "llm", "model", "system"}
)


def validate_human_identity(value: str, field_name: str) -> str:
    """Require a plausible human identity string for gated actions."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must be a non-empty human identity")
    if cleaned.lower() in _NON_HUMAN_IDENTITIES:
        raise ValueError(
            f"{field_name} must be a human identity, got {cleaned!r}: "
            "AI agents may propose specs but must not approve or decide promotion"
        )
    return cleaned


# ---------------------------------------------------------------------------
# Records
# ---------------------------------------------------------------------------


class Citation(BaseModel):
    """A research source the brain can cite: paper, article, dataset, or a
    lesson recorded in the paper journal."""

    citation_id: str = Field(default_factory=_new_id)
    source_type: str  # e.g. "paper", "article", "dataset", "journal_lesson"
    title: str
    url: str | None = None
    authors: str | None = None
    retrieved_at: datetime
    claims: list[str] = Field(default_factory=list)
    license_note: str | None = None
    created_at: datetime = Field(default_factory=_utcnow)

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("citation title must be non-empty")
        return v


class StrategySpec(BaseModel):
    """A strategy specification moving through the closed loop.

    ``hook_ref`` names the Python implementation hook as ``"module:function"``.
    Python implements only approved specs; the hook must be deterministic and
    must derive every number from stored data.
    """

    spec_id: str = Field(default_factory=_new_id)
    name: str
    version: int = 1
    status: SpecStatus = SpecStatus.PROPOSED
    promotion_state: PromotionState = PromotionState.UNPROVEN
    description: str
    proposed_by: str  # "human" or an AI proposer label, e.g. "ai:analyst"
    citation_ids: list[str] = Field(default_factory=list)
    factor_dependencies: list[str] = Field(default_factory=list)
    params: dict[str, Any] = Field(default_factory=dict)
    hook_ref: str | None = None
    created_at: datetime = Field(default_factory=_utcnow)
    approved_by: str | None = None
    approved_at: datetime | None = None
    status_reason: str | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("spec name must be non-empty")
        return v

    @field_validator("version")
    @classmethod
    def validate_version(cls, v: int) -> int:
        if v < 1:
            raise ValueError(f"version must be >= 1, got {v}")
        return v


class TestRunRecord(BaseModel):
    """One gate execution against one spec: inputs, outputs, pass/fail, as-of."""

    test_run_id: str = Field(default_factory=_new_id)
    spec_id: str
    gate_name: GateName
    sequence_index: int  # 0-based position in GATE_ORDER for this run batch
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    passed: bool
    as_of: date
    created_at: datetime = Field(default_factory=_utcnow)

    @field_validator("sequence_index")
    @classmethod
    def validate_sequence_index(cls, v: int) -> int:
        if not 0 <= v < len(GATE_ORDER):
            raise ValueError(
                f"sequence_index must be in [0, {len(GATE_ORDER) - 1}], got {v}"
            )
        return v


class PromotionDecision(BaseModel):
    """A promote/demote/hold decision with the evidence that justified it."""

    decision_id: str = Field(default_factory=_new_id)
    spec_id: str
    decision: DecisionKind
    from_state: PromotionState
    to_state: PromotionState
    rationale: str
    evidence_test_run_ids: list[str] = Field(default_factory=list)
    evidence_citation_ids: list[str] = Field(default_factory=list)
    journal_entry_ids: list[str] = Field(default_factory=list)
    decided_by: str
    created_at: datetime = Field(default_factory=_utcnow)

    @field_validator("rationale")
    @classmethod
    def validate_rationale(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("a promotion decision requires a non-empty rationale")
        return v

    @field_validator("decided_by")
    @classmethod
    def validate_decided_by(cls, v: str) -> str:
        return validate_human_identity(v, "decided_by")


class JournalLink(BaseModel):
    """Link between a strategy spec and a paper-journal entry."""

    link_id: str = Field(default_factory=_new_id)
    spec_id: str
    journal_entry_id: str
    relation: str  # e.g. "lesson", "entry", "exit", "review"
    created_at: datetime = Field(default_factory=_utcnow)

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py`
  ```
"""DuckDB persistence for the brain closed loop.

Separate tables from the ingestion schema (``daily_ohlcv`` and friends stay
clean). All writes go through typed models; approval and promotion decisions
require a human identity (see ``models.validate_human_identity``).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

import duckdb

from research_data.brain.models import (
    Citation,
    DecisionKind,
    GateName,
    JournalLink,
    PromotionDecision,
    PromotionState,
    SpecStatus,
    StrategySpec,
    TestRunRecord,
    validate_human_identity,
)


class BrainStoreError(Exception):
    """Raised on illegal brain-store operations (bad transitions, unknown ids)."""


_CREATE_CITATIONS = """\
CREATE TABLE IF NOT EXISTS brain_citations (
    citation_id VARCHAR PRIMARY KEY,
    source_type VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    url VARCHAR,
    authors VARCHAR,
    retrieved_at TIMESTAMP NOT NULL,
    claims JSON NOT NULL,
    license_note VARCHAR,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_SPECS = """\
CREATE TABLE IF NOT EXISTS brain_strategy_specs (
    spec_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    version INTEGER NOT NULL,
    status VARCHAR NOT NULL,
    promotion_state VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    proposed_by VARCHAR NOT NULL,
    citation_ids JSON NOT NULL,
    factor_dependencies JSON NOT NULL,
    params JSON NOT NULL,
    hook_ref VARCHAR,
    created_at TIMESTAMP NOT NULL,
    approved_by VARCHAR,
    approved_at TIMESTAMP,
    status_reason VARCHAR,
    UNIQUE (name, version)
);
"""

_CREATE_TEST_RUNS = """\
CREATE TABLE IF NOT EXISTS brain_test_runs (
    test_run_id VARCHAR PRIMARY KEY,
    spec_id VARCHAR NOT NULL,
    gate_name VARCHAR NOT NULL,
    sequence_index INTEGER NOT NULL,
    inputs JSON NOT NULL,
    outputs JSON NOT NULL,
    passed BOOLEAN NOT NULL,
    as_of DATE NOT NULL,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_DECISIONS = """\
CREATE TABLE IF NOT EXISTS brain_decisions (
    decision_id VARCHAR PRIMARY KEY,
    spec_id VARCHAR NOT NULL,
    decision VARCHAR NOT NULL,
    from_state VARCHAR NOT NULL,
    to_state VARCHAR NOT NULL,
    rationale VARCHAR NOT NULL,
    evidence_test_run_ids JSON NOT NULL,
    evidence_citation_ids JSON NOT NULL,
    journal_entry_ids JSON NOT NULL,
    decided_by VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_JOURNAL_LINKS = """\
CREATE TABLE IF NOT EXISTS brain_journal_links (
    link_id VARCHAR PRIMARY KEY,
    spec_id VARCHAR NOT NULL,
    journal_entry_id VARCHAR NOT NULL,
    relation VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
"""


class BrainStore:
    """Typed persistence API for citations, specs, test runs, decisions, links."""

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def init_schema(self) -> None:
        """Create brain tables if they do not exist. Preserves existing data."""
        for stmt in (
            _CREATE_CITATIONS,
            _CREATE_SPECS,
            _CREATE_TEST_RUNS,
            _CREATE_DECISIONS,
            _CREATE_JOURNAL_LINKS,
        ):
            self._conn.execute(stmt)

    # -- citations ----------------------------------------------------------

    def add_citation(self, citation: Citation) -> str:
        self._conn.execute(
            """
            INSERT INTO brain_citations (
                citation_id, source_type, title, url, authors,
                retrieved_at, claims, license_note, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                citation.citation_id,
                citation.source_type,
                citation.title,
                citation.url,
                citation.authors,
                citation.retrieved_at,
                json.dumps(citation.claims),
                citation.license_note,
                citation.created_at,
            ],
        )
        return citation.citation_id

    def get_citation(self, citation_id: str) -> Citation:
        row = self._conn.execute(
            "SELECT * FROM brain_citations WHERE citation_id = ?", [citation_id]
        ).fetchone()
        if row is None:
            raise BrainStoreError(f"Unknown citation_id: {citation_id}")
        return _row_to_citation(row)

    def list_citations(self) -> list[Citation]:
        rows = self._conn.execute(
            "SELECT * FROM brain_citations ORDER BY created_at, citation_id"
        ).fetchall()
        return [_row_to_citation(r) for r in rows]

    # -- specs ---------------------------------------------------------------

    def propose_spec(self, spec: StrategySpec) -> str:
        """Store a new spec. It must enter the loop as PROPOSED / UNPROVEN."""
        if spec.status != SpecStatus.PROPOSED:
            raise BrainStoreError(
                f"New specs must have status PROPOSED, got {spec.status.value}"
            )
        if spec.promotion_state != PromotionState.UNPROVEN:
            raise BrainStoreError(
                "New specs must enter with promotion_state UNPROVEN, "
                f"got {spec.promotion_state.value}"
            )
        for citation_id in spec.citation_ids:
            # A proposal must cite research that actually exists in the store.
            self.get_citation(citation_id)
        self._conn.execute(
            """
            INSERT INTO brain_strategy_specs (
                spec_id, name, version, status, promotion_state, description,
                proposed_by, citation_ids, factor_dependencies, params,
                hook_ref, created_at, approved_by, approved_at, status_reason
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                spec.spec_id,
                spec.name,
                spec.version,
                spec.status.value,
                spec.promotion_state.value,
                spec.description,
                spec.proposed_by,
                json.dumps(spec.citation_ids),
                json.dumps(spec.factor_dependencies),
                json.dumps(spec.params),
                spec.hook_ref,
                spec.created_at,
                spec.approved_by,
                spec.approved_at,
                spec.status_reason,
            ],
        )
        return spec.spec_id

    def get_spec(self, spec_id: str) -> StrategySpec:
        row = self._conn.execute(
            "SELECT * FROM brain_strategy_specs WHERE spec_id = ?", [spec_id]
        ).fetchone()
        if row is None:
            raise BrainStoreError(f"Unknown spec_id: {spec_id}")
        return _row_to_spec(row)

    def list_specs(self, status: SpecStatus | None = None) -> list[StrategySpec]:
        if status is None:
            rows = self._conn.execute(
                "SELECT * FROM brain_strategy_specs ORDER BY created_at, spec_id"
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM brain_strategy_specs WHERE status = ? "
                "ORDER BY created_at, spec_id",
                [status.value],
            ).fetchall()
        return [_row_to_spec(r) for r in rows]

    def approve_spec(
        self,
        spec_id: str,
        approved_by: str,
        approved_at: datetime | None = None,
    ) -> StrategySpec:
        """Human gate: PROPOSED → APPROVED. ``approved_by`` must be a human."""
        approved_by = validate_human_identity(approved_by, "approved_by")
        spec = self.get_spec(spec_id)
        if spec.status != SpecStatus.PROPOSED:
            raise BrainStoreError(
                f"Only PROPOSED specs can be approved; {spec_id} is {spec.status.value}"
            )
        approved_at = approved_at or datetime.now(timezone.utc)
        self._conn.execute(
            """
            UPDATE brain_strategy_specs
            SET status = ?, approved_by = ?, approved_at = ?
            WHERE spec_id = ?
            """,
            [SpecStatus.APPROVED.value, approved_by, approved_at, spec_id],
        )
        return self.get_spec(spec_id)

    def reject_spec(self, spec_id: str, reason: str, decided_by: str) -> StrategySpec:
        """Human gate: PROPOSED → REJECTED with a stated reason."""
        decided_by = validate_human_identity(decided_by, "decided_by")
        if not reason.strip():
            raise BrainStoreError("rejection requires a non-empty reason")
        spec = self.get_spec(spec_id)
        if spec.status != SpecStatus.PROPOSED:
            raise BrainStoreError(
                f"Only PROPOSED specs can be rejected; {spec_id} is {spec.status.value}"
            )
        self._conn.execute(
            "UPDATE brain_strategy_specs SET status = ?, status_reason = ? WHERE spec_id = ?",
            [SpecStatus.REJECTED.value, reason, spec_id],
        )
        return self.get_spec(spec_id)

    def retire_spec(self, spec_id: str, reason: str, decided_by: str) -> StrategySpec:
        """Human gate: APPROVED → RETIRED (spec leaves active rotation)."""
        decided_by = validate_human_identity(decided_by, "decided_by")
        if not reason.strip():
            raise BrainStoreError("retiring requires a non-empty reason")
        spec = self.get_spec(spec_id)
        if spec.status != SpecStatus.APPROVED:
            raise BrainStoreError(
                f"Only APPROVED specs can be retired; {spec_id} is {spec.status.value}"
            )
        self._conn.execute(
            "UPDATE brain_strategy_specs SET status = ?, status_reason = ? WHERE spec_id = ?",
            [SpecStatus.RETIRED.value, reason, spec_id],
        )
        return self.get_spec(spec_id)

    # -- test runs ------------------------------------------------------------

    def record_test_run(self, run: TestRunRecord) -> str:
        # A gate run is only meaningful against a spec that exists and was
        # approved by a human — gates never run on unapproved proposals.
        spec = self.get_spec(run.spec_id)
        if spec.status != SpecStatus.APPROVED:
            raise BrainStoreError(
                f"Gates run only against APPROVED specs; {run.spec_id} is {spec.status.value}"
            )
        self._conn.execute(
            """
            INSERT INTO brain_test_runs (
                test_run_id, spec_id, gate_name, sequence_index,
                inputs, outputs, passed, as_of, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                run.test_run_id,
                run.spec_id,
                run.gate_name.value,
                run.sequence_index,
                json.dumps(run.inputs, default=str),
                json.dumps(run.outputs, default=str),
                run.passed,
                run.as_of,
                run.created_at,
            ],
        )
        return run.test_run_id

    def list_test_runs(self, spec_id: str) -> list[TestRunRecord]:
        rows = self._conn.execute(
            """
            SELECT * FROM brain_test_runs WHERE spec_id = ?
            ORDER BY created_at, sequence_index, test_run_id
            """,
            [spec_id],
        ).fetchall()
        return [_row_to_test_run(r) for r in rows]

    def count_tested_specs(self) -> int:
        """Number of distinct specs with at least one recorded gate run.

        This is the trial count fed to the deflated-Sharpe gate: every strategy
        configuration that reached testing counts as a selection-bias trial.
        """
        row = self._conn.execute(
            "SELECT COUNT(DISTINCT spec_id) FROM brain_test_runs"
        ).fetchone()
        return int(row[0]) if row else 0

    # -- decisions -------------------------------------------------------------

    def record_decision(self, decision: PromotionDecision) -> str:
        """Persist a promote/demote/hold decision and move the spec's state."""
        spec = self.get_spec(decision.spec_id)
        if spec.promotion_state != decision.from_state:
            raise BrainStoreError(
                f"Decision from_state {decision.from_state.value} does not match "
                f"spec promotion_state {spec.promotion_state.value}"
            )
        if decision.decision != DecisionKind.HOLD and decision.from_state == decision.to_state:
            raise BrainStoreError("promote/demote decisions must change state")
        for run_id in decision.evidence_test_run_ids:
            row = self._conn.execute(
                "SELECT test_run_id FROM brain_test_runs WHERE test_run_id = ?",
                [run_id],
            ).fetchone()
            if row is None:
                raise BrainStoreError(f"Unknown evidence test_run_id: {run_id}")
        self._conn.execute(
            """
            INSERT INTO brain_decisions (
                decision_id, spec_id, decision, from_state, to_state, rationale,
                evidence_test_run_ids, evidence_citation_ids, journal_entry_ids,
                decided_by, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                decision.decision_id,
                decision.spec_id,
                decision.decision.value,
                decision.from_state.value,
                decision.to_state.value,
                decision.rationale,
                json.dumps(decision.evidence_test_run_ids),
                json.dumps(decision.evidence_citation_ids),
                json.dumps(decision.journal_entry_ids),
                decision.decided_by,
                decision.created_at,
            ],
        )
        self._conn.execute(
            "UPDATE brain_strategy_specs SET promotion_state = ? WHERE spec_id = ?",
            [decision.to_state.value, decision.spec_id],
        )
        return decision.decision_id

    def list_decisions(self, spec_id: str) -> list[PromotionDecision]:
        rows = self._conn.execute(
            "SELECT * FROM brain_decisions WHERE spec_id = ? ORDER BY created_at, decision_id",
            [spec_id],
        ).fetchall()
        return [_row_to_decision(r) for r in rows]

    # -- journal links -----------------------------------------------------------

    def link_journal(self, link: JournalLink) -> str:
        self.get_spec(link.spec_id)
        self._conn.execute(
            """
            INSERT INTO brain_journal_links (
                link_id, spec_id, journal_entry_id, relation, created_at
            ) VALUES (?, ?, ?, ?, ?)
            """,
            [link.link_id, link.spec_id, link.journal_entry_id, link.relation, link.created_at],
        )
        return link.link_id

    def list_journal_links(self, spec_id: str) -> list[JournalLink]:
        rows = self._conn.execute(
            "SELECT * FROM brain_journal_links WHERE spec_id = ? ORDER BY created_at, link_id",
            [spec_id],
        ).fetchall()
        return [
            JournalLink(
                link_id=r[0],
                spec_id=r[1],
                journal_entry_id=r[2],
                relation=r[3],
                created_at=_as_utc(r[4]),
            )
            for r in rows
        ]


# ---------------------------------------------------------------------------
# Row converters
# ---------------------------------------------------------------------------


def _as_utc(value: datetime | None) -> datetime | None:
    if value is not None and value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


def _loads(value: Any) -> Any:
    return json.loads(value) if isinstance(value, str) else value


def _row_to_citation(row: tuple) -> Citation:
    return Citation(
        citation_id=row[0],
        source_type=row[1],
        title=row[2],
        url=row[3],
        authors=row[4],
        retrieved_at=_as_utc(row[5]),
        claims=_loads(row[6]),
        license_note=row[7],
        created_at=_as_utc(row[8]),
    )


def _row_to_spec(row: tuple) -> StrategySpec:
    return StrategySpec(
        spec_id=row[0],
        name=row[1],
        version=row[2],
        status=SpecStatus(row[3]),
        promotion_state=PromotionState(row[4]),
        description=row[5],
        proposed_by=row[6],
        citation_ids=_loads(row[7]),
        factor_dependencies=_loads(row[8]),
        params=_loads(row[9]),
        hook_ref=row[10],
        created_at=_as_utc(row[11]),
        approved_by=row[12],
        approved_at=_as_utc(row[13]),
        status_reason=row[14],
    )


def _row_to_test_run(row: tuple) -> TestRunRecord:
    return TestRunRecord(
        test_run_id=row[0],
        spec_id=row[1],
        gate_name=GateName(row[2]),
        sequence_index=row[3],
        inputs=_loads(row[4]),
        outputs=_loads(row[5]),
        passed=row[6],
        as_of=row[7],
        created_at=_as_utc(row[8]),
    )


def _row_to_decision(row: tuple) -> PromotionDecision:
    return PromotionDecision(
        decision_id=row[0],
        spec_id=row[1],
        decision=DecisionKind(row[2]),
        from_state=PromotionState(row[3]),
        to_state=PromotionState(row[4]),
        rationale=row[5],
        evidence_test_run_ids=_loads(row[6]),
        evidence_citation_ids=_loads(row[7]),
        journal_entry_ids=_loads(row[8]),
        decided_by=row[9],
        created_at=_as_utc(row[10]),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/loop.py`
  ```
"""Closed-loop rules: gate-order enforcement, eligibility, hook resolution.

The loop this module guards:

    citation → proposed spec → human approve → Python hook → four gates
    → promote/demote → journal link → next proposal

Nothing here computes gate statistics (that lives in ``research_data.gates``);
this module only enforces *when* results count and *how* they change state.
"""

from __future__ import annotations

import importlib
from typing import Callable

from research_data.brain.models import (
    GATE_ORDER,
    DecisionKind,
    PromotionDecision,
    PromotionState,
    SpecStatus,
    TestRunRecord,
)
from research_data.brain.store import BrainStore


class BrainLoopError(Exception):
    """Raised when the closed loop's rules are violated."""


def gate_sequence_passes(runs: list[TestRunRecord]) -> bool:
    """True iff ``runs`` form one complete, ordered, all-passing gate batch.

    Rules (all must hold):
    - exactly one run per gate in ``GATE_ORDER``;
    - sequence indexes match the fixed order (OOS=0 … deflated Sharpe=3);
    - every run passed.

    A short batch (e.g. stopped after a failed gate) never passes.
    """
    if len(runs) != len(GATE_ORDER):
        return False
    ordered = sorted(runs, key=lambda r: r.sequence_index)
    for index, (run, expected_gate) in enumerate(zip(ordered, GATE_ORDER)):
        if run.sequence_index != index or run.gate_name != expected_gate:
            return False
        if not run.passed:
            return False
    return True


def latest_gate_batch(store: BrainStore, spec_id: str) -> list[TestRunRecord]:
    """Return the most recent gate batch for a spec.

    A batch starts at a run with ``sequence_index == 0``; the latest batch is
    everything from the last such run onward (runs are stored in time order).
    """
    runs = store.list_test_runs(spec_id)
    if not runs:
        return []
    start = 0
    for i, run in enumerate(runs):
        if run.sequence_index == 0:
            start = i
    return runs[start:]


def is_demo_eligible(store: BrainStore, spec_id: str) -> bool:
    """Demo-paper eligibility: approved spec + latest full gate batch passed
    + promotion state DEMO_ELIGIBLE (i.e. a recorded human decision).

    All three must hold; test results alone never flip eligibility without a
    recorded decision, and a decision cannot stand without passing gates.
    """
    spec = store.get_spec(spec_id)
    if spec.status != SpecStatus.APPROVED:
        return False
    if spec.promotion_state != PromotionState.DEMO_ELIGIBLE:
        return False
    return gate_sequence_passes(latest_gate_batch(store, spec_id))


def record_gate_outcome_decision(
    store: BrainStore,
    spec_id: str,
    decided_by: str,
    rationale: str,
    journal_entry_ids: list[str] | None = None,
) -> PromotionDecision:
    """Record the promote/demote decision implied by the latest gate batch.

    - full batch, all gates passed  → promote to DEMO_ELIGIBLE
    - anything else (failed/partial) → demote to DEMOTED (from DEMO_ELIGIBLE)
      or hold at UNPROVEN/DEMOTED (state cannot silently improve)

    The decision cites the batch's test-run ids as evidence. ``decided_by``
    must be a human identity — the loop keeps the human in charge.
    """
    spec = store.get_spec(spec_id)
    if spec.status != SpecStatus.APPROVED:
        raise BrainLoopError(
            f"Promotion decisions apply to APPROVED specs only; "
            f"{spec_id} is {spec.status.value}"
        )
    batch = latest_gate_batch(store, spec_id)
    if not batch:
        raise BrainLoopError(f"No gate runs recorded for spec {spec_id}")

    passed = gate_sequence_passes(batch)
    from_state = spec.promotion_state
    if passed:
        decision_kind = DecisionKind.PROMOTE
        to_state = PromotionState.DEMO_ELIGIBLE
        if from_state == PromotionState.DEMO_ELIGIBLE:
            decision_kind = DecisionKind.HOLD
    else:
        if from_state == PromotionState.DEMO_ELIGIBLE:
            decision_kind = DecisionKind.DEMOTE
            to_state = PromotionState.DEMOTED
        else:
            decision_kind = DecisionKind.HOLD
            to_state = from_state

    decision = PromotionDecision(
        spec_id=spec_id,
        decision=decision_kind,
        from_state=from_state,
        to_state=to_state,
        rationale=rationale,
        evidence_test_run_ids=[r.test_run_id for r in batch],
        evidence_citation_ids=spec.citation_ids,
        journal_entry_ids=journal_entry_ids or [],
        decided_by=decided_by,
    )
    store.record_decision(decision)
    return decision


def resolve_hook(hook_ref: str) -> Callable:
    """Resolve a spec's ``"module:function"`` hook reference to a callable.

    The hook is the Python implementation of an approved spec: a deterministic
    function that produces the strategy return series the gates evaluate.
    """
    module_name, sep, attr = hook_ref.partition(":")
    if not sep or not module_name or not attr:
        raise BrainLoopError(
            f"hook_ref must look like 'package.module:function', got {hook_ref!r}"
        )
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        raise BrainLoopError(f"Cannot import hook module {module_name!r}: {e}") from e
    hook = getattr(module, attr, None)
    if not callable(hook):
        raise BrainLoopError(f"Hook {hook_ref!r} does not resolve to a callable")
    return hook

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_brain_store.py`
  ```
"""Tests for the brain persistence layer (citations, specs, runs, decisions)."""

from __future__ import annotations

from datetime import date, datetime, timezone

import duckdb
import pytest

from research_data.brain import (
    BrainStore,
    Citation,
    GateName,
    JournalLink,
    PromotionDecision,
    PromotionState,
    SpecStatus,
    StrategySpec,
    TestRunRecord,
)
from research_data.brain.models import DecisionKind
from research_data.brain.store import BrainStoreError


NOW = datetime(2026, 7, 10, 12, 0, 0, tzinfo=timezone.utc)


@pytest.fixture()
def store() -> BrainStore:
    conn = duckdb.connect(":memory:")
    s = BrainStore(conn)
    s.init_schema()
    return s


def make_citation(**overrides) -> Citation:
    defaults = dict(
        source_type="paper",
        title="Returns to Buying Winners and Selling Losers",
        url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227214",
        authors="Jegadeesh, Titman",
        retrieved_at=NOW,
        claims=["12-1 month momentum persists 3-12 months out of sample"],
    )
    defaults.update(overrides)
    return Citation(**defaults)


def make_spec(citation_ids: list[str] | None = None, **overrides) -> StrategySpec:
    defaults = dict(
        name="momentum_tilt",
        version=1,
        description="Rank universe by 12-1 month return; tilt watchlist priority.",
        proposed_by="ai:analyst",
        citation_ids=citation_ids or [],
        factor_dependencies=["momentum"],
        params={"lookback_days": 252, "skip_days": 21},
        hook_ref="research_data.factors.momentum:momentum_strategy_hook",
    )
    defaults.update(overrides)
    return StrategySpec(**defaults)


def test_citation_roundtrip(store: BrainStore) -> None:
    citation = make_citation()
    store.add_citation(citation)
    loaded = store.get_citation(citation.citation_id)
    assert loaded.title == citation.title
    assert loaded.claims == citation.claims
    assert loaded.retrieved_at == NOW


def test_propose_spec_requires_existing_citations(store: BrainStore) -> None:
    spec = make_spec(citation_ids=["missing-citation"])
    with pytest.raises(BrainStoreError, match="Unknown citation_id"):
        store.propose_spec(spec)


def test_propose_and_get_spec_roundtrip(store: BrainStore) -> None:
    cid = store.add_citation(make_citation())
    spec = make_spec(citation_ids=[cid])
    store.propose_spec(spec)
    loaded = store.get_spec(spec.spec_id)
    assert loaded.status == SpecStatus.PROPOSED
    assert loaded.promotion_state == PromotionState.UNPROVEN
    assert loaded.params == {"lookback_days": 252, "skip_days": 21}
    assert loaded.citation_ids == [cid]


def test_new_spec_cannot_enter_pre_approved(store: BrainStore) -> None:
    spec = make_spec(status=SpecStatus.APPROVED)
    with pytest.raises(BrainStoreError, match="PROPOSED"):
        store.propose_spec(spec)


def test_approve_spec_human_gate(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    approved = store.approve_spec(spec.spec_id, approved_by="Anant", approved_at=NOW)
    assert approved.status == SpecStatus.APPROVED
    assert approved.approved_by == "Anant"
    assert approved.approved_at == NOW


@pytest.mark.parametrize("identity", ["", "  ", "ai", "Claude", "AGENT", "cursor"])
def test_non_human_identities_cannot_approve(store: BrainStore, identity: str) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    with pytest.raises(ValueError):
        store.approve_spec(spec.spec_id, approved_by=identity)
    assert store.get_spec(spec.spec_id).status == SpecStatus.PROPOSED


def test_reject_and_retire_transitions(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    rejected = store.reject_spec(spec.spec_id, reason="duplicate of v1", decided_by="Anant")
    assert rejected.status == SpecStatus.REJECTED
    # Rejected specs cannot be approved afterwards.
    with pytest.raises(BrainStoreError):
        store.approve_spec(spec.spec_id, approved_by="Anant")

    other = make_spec(name="momentum_tilt_v2", version=2)
    store.propose_spec(other)
    store.approve_spec(other.spec_id, approved_by="Anant")
    retired = store.retire_spec(other.spec_id, reason="superseded", decided_by="Anant")
    assert retired.status == SpecStatus.RETIRED


def test_duplicate_name_version_rejected(store: BrainStore) -> None:
    store.propose_spec(make_spec())
    with pytest.raises(Exception):
        store.propose_spec(make_spec())


def test_test_runs_only_against_approved_specs(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    run = TestRunRecord(
        spec_id=spec.spec_id,
        gate_name=GateName.OUT_OF_SAMPLE,
        sequence_index=0,
        passed=True,
        as_of=date(2026, 7, 10),
    )
    with pytest.raises(BrainStoreError, match="APPROVED"):
        store.record_test_run(run)


def test_test_run_roundtrip_and_trial_count(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    store.approve_spec(spec.spec_id, approved_by="Anant")
    run = TestRunRecord(
        spec_id=spec.spec_id,
        gate_name=GateName.OUT_OF_SAMPLE,
        sequence_index=0,
        inputs={"train_fraction": 0.7},
        outputs={"oos_sharpe": 0.42},
        passed=True,
        as_of=date(2026, 7, 10),
    )
    store.record_test_run(run)
    runs = store.list_test_runs(spec.spec_id)
    assert len(runs) == 1
    assert runs[0].gate_name == GateName.OUT_OF_SAMPLE
    assert runs[0].outputs == {"oos_sharpe": 0.42}
    assert store.count_tested_specs() == 1


def test_decision_updates_promotion_state(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    store.approve_spec(spec.spec_id, approved_by="Anant")
    run_id = store.record_test_run(
        TestRunRecord(
            spec_id=spec.spec_id,
            gate_name=GateName.OUT_OF_SAMPLE,
            sequence_index=0,
            passed=True,
            as_of=date(2026, 7, 10),
        )
    )
    decision = PromotionDecision(
        spec_id=spec.spec_id,
        decision=DecisionKind.PROMOTE,
        from_state=PromotionState.UNPROVEN,
        to_state=PromotionState.DEMO_ELIGIBLE,
        rationale="all four gates passed on fixture data",
        evidence_test_run_ids=[run_id],
        decided_by="Anant",
    )
    store.record_decision(decision)
    assert store.get_spec(spec.spec_id).promotion_state == PromotionState.DEMO_ELIGIBLE
    decisions = store.list_decisions(spec.spec_id)
    assert len(decisions) == 1
    assert decisions[0].evidence_test_run_ids == [run_id]


def test_decision_requires_matching_from_state_and_real_evidence(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    store.approve_spec(spec.spec_id, approved_by="Anant")

    mismatched = PromotionDecision(
        spec_id=spec.spec_id,
        decision=DecisionKind.DEMOTE,
        from_state=PromotionState.DEMO_ELIGIBLE,
        to_state=PromotionState.DEMOTED,
        rationale="state mismatch",
        decided_by="Anant",
    )
    with pytest.raises(BrainStoreError, match="from_state"):
        store.record_decision(mismatched)

    phantom_evidence = PromotionDecision(
        spec_id=spec.spec_id,
        decision=DecisionKind.PROMOTE,
        from_state=PromotionState.UNPROVEN,
        to_state=PromotionState.DEMO_ELIGIBLE,
        rationale="cites a run that does not exist",
        evidence_test_run_ids=["no-such-run"],
        decided_by="Anant",
    )
    with pytest.raises(BrainStoreError, match="test_run_id"):
        store.record_decision(phantom_evidence)


def test_decisions_require_human_identity() -> None:
    with pytest.raises(ValueError):
        PromotionDecision(
            spec_id="s",
            decision=DecisionKind.PROMOTE,
            from_state=PromotionState.UNPROVEN,
            to_state=PromotionState.DEMO_ELIGIBLE,
            rationale="gates passed",
            decided_by="ai",
        )


def test_journal_link_roundtrip(store: BrainStore) -> None:
    spec = make_spec()
    store.propose_spec(spec)
    link = JournalLink(spec_id=spec.spec_id, journal_entry_id="journal-1", relation="lesson")
    store.link_journal(link)
    links = store.list_journal_links(spec.spec_id)
    assert len(links) == 1
    assert links[0].journal_entry_id == "journal-1"

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_brain_loop.py`
  ```
"""Tests for closed-loop rules: gate ordering, eligibility, hook resolution."""

from __future__ import annotations

from datetime import date, datetime, timezone

import duckdb
import pytest

from research_data.brain import (
    GATE_ORDER,
    BrainLoopError,
    BrainStore,
    GateName,
    PromotionState,
    StrategySpec,
    TestRunRecord,
    gate_sequence_passes,
    is_demo_eligible,
    record_gate_outcome_decision,
    resolve_hook,
)
from research_data.brain.models import DecisionKind

AS_OF = date(2026, 7, 10)


@pytest.fixture()
def store() -> BrainStore:
    conn = duckdb.connect(":memory:")
    s = BrainStore(conn)
    s.init_schema()
    return s


def approved_spec(store: BrainStore, name: str = "momentum_tilt") -> StrategySpec:
    spec = StrategySpec(
        name=name,
        description="test spec",
        proposed_by="ai:analyst",
        params={},
    )
    store.propose_spec(spec)
    return store.approve_spec(spec.spec_id, approved_by="Anant")


def make_batch(spec_id: str, passed_flags: list[bool]) -> list[TestRunRecord]:
    return [
        TestRunRecord(
            spec_id=spec_id,
            gate_name=gate,
            sequence_index=i,
            passed=passed_flags[i],
            as_of=AS_OF,
        )
        for i, gate in enumerate(GATE_ORDER[: len(passed_flags)])
    ]


def test_gate_order_is_fixed() -> None:
    assert [g.value for g in GATE_ORDER] == [
        "out_of_sample",
        "monte_carlo",
        "walk_forward",
        "deflated_sharpe",
    ]


def test_full_passing_batch_passes(store: BrainStore) -> None:
    spec = approved_spec(store)
    batch = make_batch(spec.spec_id, [True, True, True, True])
    assert gate_sequence_passes(batch) is True


def test_partial_or_failed_batches_do_not_pass(store: BrainStore) -> None:
    spec = approved_spec(store)
    assert gate_sequence_passes(make_batch(spec.spec_id, [True, True, True])) is False
    assert gate_sequence_passes(make_batch(spec.spec_id, [True, True, False, True])) is False
    assert gate_sequence_passes([]) is False


def test_out_of_order_batch_does_not_pass(store: BrainStore) -> None:
    spec = approved_spec(store)
    batch = make_batch(spec.spec_id, [True, True, True, True])
    # Swap gate names so the sequence indexes no longer match the fixed order.
    batch[0].gate_name, batch[1].gate_name = batch[1].gate_name, batch[0].gate_name
    assert gate_sequence_passes(batch) is False


def test_promotion_via_recorded_decision(store: BrainStore) -> None:
    spec = approved_spec(store)
    for run in make_batch(spec.spec_id, [True, True, True, True]):
        store.record_test_run(run)

    assert is_demo_eligible(store, spec.spec_id) is False  # no decision yet

    decision = record_gate_outcome_decision(
        store, spec.spec_id, decided_by="Anant", rationale="all gates passed"
    )
    assert decision.decision == DecisionKind.PROMOTE
    assert decision.to_state == PromotionState.DEMO_ELIGIBLE
    assert is_demo_eligible(store, spec.spec_id) is True


def test_failed_batch_cannot_promote(store: BrainStore) -> None:
    spec = approved_spec(store)
    for run in make_batch(spec.spec_id, [True, False]):
        store.record_test_run(run)
    decision = record_gate_outcome_decision(
        store, spec.spec_id, decided_by="Anant", rationale="monte carlo failed"
    )
    assert decision.decision == DecisionKind.HOLD
    assert decision.to_state == PromotionState.UNPROVEN
    assert is_demo_eligible(store, spec.spec_id) is False


def test_later_failed_batch_demotes(store: BrainStore) -> None:
    spec = approved_spec(store)
    for run in make_batch(spec.spec_id, [True, True, True, True]):
        store.record_test_run(run)
    record_gate_outcome_decision(store, spec.spec_id, decided_by="Anant", rationale="passed")
    assert is_demo_eligible(store, spec.spec_id) is True

    # A new (re-test) batch starts at sequence_index 0 and fails at walk-forward.
    for run in make_batch(spec.spec_id, [True, True, False]):
        store.record_test_run(run)
    decision = record_gate_outcome_decision(
        store, spec.spec_id, decided_by="Anant", rationale="walk-forward regression"
    )
    assert decision.decision == DecisionKind.DEMOTE
    assert decision.to_state == PromotionState.DEMOTED
    assert is_demo_eligible(store, spec.spec_id) is False


def test_decision_requires_gate_runs(store: BrainStore) -> None:
    spec = approved_spec(store)
    with pytest.raises(BrainLoopError, match="No gate runs"):
        record_gate_outcome_decision(store, spec.spec_id, decided_by="Anant", rationale="x")


def test_resolve_hook_roundtrip() -> None:
    hook = resolve_hook("research_data.env:load_dotenv")
    assert callable(hook)


@pytest.mark.parametrize("bad_ref", ["no_colon", ":func", "module:", "nope.nope:fn"])
def test_resolve_hook_rejects_bad_refs(bad_ref: str) -> None:
    with pytest.raises(BrainLoopError):
        resolve_hook(bad_ref)

  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -15`
  ```
tests/test_brain_store.py:102: AssertionError
=============================== warnings summary ===============================
src/research_data/brain/models.py:160
  /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/models.py:160: PytestCollectionWarning: cannot collect test class 'TestRunRecord' because it has a __init__ constructor (from: tests/test_brain_store.py)
    class TestRunRecord(BaseModel):

src/research_data/brain/models.py:160
  /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/models.py:160: PytestCollectionWarning: cannot collect test class 'TestRunRecord' because it has a __init__ constructor (from: tests/test_brain_loop.py)
    class TestRunRecord(BaseModel):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_brain_store.py::test_citation_roundtrip - AssertionError: a...
FAILED tests/test_brain_store.py::test_approve_spec_human_gate - AssertionErr...
2 failed, 30 passed, 2 warnings in 1.32s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python -c "
import duckdb
from datetime import datetime, timezone
c = duckdb.connect(':memory:')
c.execute('CREATE TABLE t (ts TIMESTAMP)')
c.execute('INSERT INTO t VALUES (?)', [datetime(2026,7,10,12,0,0,tzinfo=timezone.utc)])
print(c.execute('SELECT ts FROM t').fetchone())
print('tz:', datetime.now().astimezone().tzinfo)
"
  ```
  ```
(datetime.datetime(2026, 7, 10, 16, 0),)
tz: +04
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py`
  ```diff
  - class BrainStoreError(Exception):
    """Raised on illegal brain-store operations (bad transitions, unknown ids)."""
  + class BrainStoreError(Exception):
    """Raised on illegal brain-store operations (bad transitions, unknown ids)."""


def _to_db_ts(value: datetime | None) -> datetime | None:
    """Normalize to naive UTC before insert.

    DuckDB TIMESTAMP columns convert tz-aware datetimes to *local* time and
    drop the offset, which corrupts round-trips on non-UTC machines.
    """
    if value is None or value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)
  ```
- `Bash`:
  ```bash
python - <<'EOF'
import re
p = 'src/research_data/brain/store.py'
s = open(p).read()
subs = [
    ("citation.retrieved_at,", "_to_db_ts(citation.retrieved_at),"),
    ("citation.created_at,", "_to_db_ts(citation.created_at),"),
    ("spec.created_at,\n                spec.approved_by,\n                spec.approved_at,", "_to_db_ts(spec.created_at),\n                spec.approved_by,\n                _to_db_ts(spec.approved_at),"),
    ("[SpecStatus.APPROVED.value, approved_by, approved_at, spec_id],", "[SpecStatus.APPROVED.value, approved_by, _to_db_ts(approved_at), spec_id],"),
    ("run.as_of,\n                run.created_at,", "run.as_of,\n                _to_db_ts(run.created_at),"),
    ("decision.decided_by,\n                decision.created_at,", "decision.decided_by,\n                _to_db_ts(decision.created_at),"),
    ("link.relation, link.created_at]", "link.relation, _to_db_ts(link.created_at)]"),
]
for old, new in subs:
    assert old in s, old
    s = s.replace(old, new)
open(p, 'w').write(s)
print("ok")
EOF
source .venv/bin/activate && python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -3
  ```
  ```
/bin/bash: line 20: python: command not found
FAILED tests/test_brain_store.py::test_citation_roundtrip - AssertionError: a...
FAILED tests/test_brain_store.py::test_approve_spec_human_gate - AssertionErr...
2 failed, 30 passed, 2 warnings in 2.55s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python - <<'EOF'
p = 'src/research_data/brain/store.py'
s = open(p).read()
subs = [
    ("citation.retrieved_at,", "_to_db_ts(citation.retrieved_at),"),
    ("citation.created_at,", "_to_db_ts(citation.created_at),"),
    ("spec.created_at,\n                spec.approved_by,\n                spec.approved_at,", "_to_db_ts(spec.created_at),\n                spec.approved_by,\n                _to_db_ts(spec.approved_at),"),
    ("[SpecStatus.APPROVED.value, approved_by, approved_at, spec_id],", "[SpecStatus.APPROVED.value, approved_by, _to_db_ts(approved_at), spec_id],"),
    ("run.as_of,\n                run.created_at,", "run.as_of,\n                _to_db_ts(run.created_at),"),
    ("decision.decided_by,\n                decision.created_at,", "decision.decided_by,\n                _to_db_ts(decision.created_at),"),
    ("link.relation, link.created_at]", "link.relation, _to_db_ts(link.created_at)]"),
]
for old, new in subs:
    assert old in s, old
    s = s.replace(old, new)
open(p, 'w').write(s)
print("ok")
EOF
python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -3
  ```
  ```
ok

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
32 passed, 2 warnings in 2.32s
  ```
- `TaskUpdate` — `{"taskId":"2","status":"completed"}`
- `TaskUpdate` — `{"taskId":"3","status":"in_progress","activeForm":"Implementing factor engine"}`
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```diff
  - ## Corrections

- (none yet)
  + ## Corrections

- DuckDB `TIMESTAMP` columns convert tz-aware datetimes to **local** naive time on insert (machine is UTC+4)
  → always normalize to naive UTC before insert (`_to_db_ts` in brain/store.py; reused pattern for paper store).
  Existing `storage.py` has the same latent issue — flagged as a Cursor leftover, do not fix drive-by.
- Long factor fixtures: generating synthetic OHLCV records in-test (seeded, `tests/synthetic.py`) beats
  committing 14 × 600-row CSVs; existing short CSVs stay for ingestion/provider tests.
  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/packets.py`
  ```
"""Score packet models — the typed output of the factor engine.

Every score carries its formula inputs, window, and status so a downstream
reader (human or AI) can verify the number instead of trusting it. Scores
never carry action labels; action vocabulary (WATCH | HOLD | ACCUMULATE |
REDUCE | AVOID | INSUFFICIENT_DATA) belongs to the downstream evidence layer
and paper theses, not to raw factor math.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field

from research_data.models import QualityStatus


class ScoreStatus(str, Enum):
    """Whether a score could be computed from real data."""

    OK = "ok"
    INSUFFICIENT_DATA = "insufficient_data"


class MomentumScore(BaseModel):
    """12-1 month total-return rank within the universe (Jegadeesh-Titman).

    Formula: P[t-21] / P[t-252] - 1 on trading days, ranked ascending —
    rank == universe_size is the strongest 12-1 return, rank 1 the weakest.
    """

    status: ScoreStatus
    rank: int | None = None
    universe_size: int
    ranked_count: int = 0  # symbols that actually had enough history to rank
    twelve_minus_one_return: float | None = None
    window_start: date | None = None
    window_end: date | None = None
    price_field: str = "adjusted_close"
    context: str = ""


class SafetyScore(BaseModel):
    """Inverse rank of 12-month realized volatility (low vol → high rank).

    Formula: stdev of daily simple returns over the trailing 252 sessions,
    annualized by sqrt(252). Lowest volatility gets rank == universe_size.
    """

    status: ScoreStatus
    rank: int | None = None
    universe_size: int
    ranked_count: int = 0
    realized_vol_annualized: float | None = None
    window_start: date | None = None
    window_end: date | None = None
    context: str = ""


class QualityFCFComponents(BaseModel):
    """Raw inputs behind the quality composite, all as-of a statement period."""

    fcf_ev: float | None = None
    fcf_margin: float | None = None
    op_margin_stability: float | None = None  # stdev of operating margin (lower = steadier)
    debt_to_equity: float | None = None
    enterprise_value: float | None = None
    market_cap: float | None = None
    fundamentals_as_of: date | None = None
    fundamentals_source: str | None = None


class QualityFCFScore(BaseModel):
    """Composite 0-100 of FCF/EV, FCF margin, margin stability, and leverage.

    Weighted rank-average across the universe (weights in factors/quality_fcf.py).
    ETFs and symbols without fundamentals report INSUFFICIENT_DATA — never a
    synthesized value.
    """

    status: ScoreStatus
    value: float | None = Field(default=None, ge=0.0, le=100.0)
    universe_size: int
    ranked_count: int = 0
    components: QualityFCFComponents = Field(default_factory=QualityFCFComponents)
    context: str = ""


class ValuationContext(BaseModel):
    """Cash-based valuation context. FCF/EV is primary; P/E is never the driver."""

    status: ScoreStatus
    fcf_ev: float | None = None
    p_fcf: float | None = None
    sector_note: str = ""
    caveats: list[str] = Field(default_factory=list)


class BaselineWindowComparison(BaseModel):
    """Symbol vs benchmark total return over one overlapping-session window."""

    window_sessions: int
    symbol_return: float
    benchmark_return: float
    overlapping_sessions: int


class EtfBaselineComparison(BaseModel):
    """Comparison against the ETF baseline (default VOO) on overlapping sessions."""

    status: ScoreStatus
    benchmark_symbol: str
    windows: list[BaselineWindowComparison] = Field(default_factory=list)
    context: str = ""


class TAContext(BaseModel):
    """Descriptive technical context ONLY — never drives an action by itself.

    (MA/RSI/Bollinger have no robust standalone out-of-sample evidence; they
    describe price state for the reader. See the strategy-edge research note.)
    """

    sma_50: float | None = None
    sma_200: float | None = None
    price_vs_sma_50: str | None = None  # "above" | "below"
    price_vs_sma_200: str | None = None
    ma_cross: str | None = None  # "golden" | "death" | None
    rsi_14: float | None = None
    bollinger_position: float | None = None  # std devs from the 20-day mean
    drawdown_from_52w_high: float | None = None
    note: str = "Descriptive context only; not an action driver."


class PacketDataQuality(BaseModel):
    """Quality status and the confidence ceiling it imposes downstream."""

    status: QualityStatus
    max_confidence: float = Field(ge=0.0, le=1.0)
    price_rows_used: int = 0
    notes: list[str] = Field(default_factory=list)


class PacketProvenance(BaseModel):
    """Where every number in the packet came from."""

    price_source: str | None = None
    price_field: str = "adjusted_close"
    first_price_date: date | None = None
    last_price_date: date | None = None
    fundamentals_source: str | None = None
    generated_at: datetime


class ScorePacket(BaseModel):
    """Structured factor output for one symbol, as of one date.

    Downstream AI receives this packet; it does not recompute or invent
    numbers. Confidence anywhere downstream is capped by
    ``data_quality.max_confidence``.
    """

    symbol: str
    as_of: date
    universe: list[str]
    momentum_score: MomentumScore
    safety_score: SafetyScore
    quality_fcf_score: QualityFCFScore
    valuation: ValuationContext
    etf_baseline: EtfBaselineComparison
    ta_context: TAContext
    risk_flags: list[str] = Field(default_factory=list)
    data_quality: PacketDataQuality
    provenance: PacketProvenance

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ranking.py`
  ```
"""Deterministic cross-sectional ranking helpers shared by factor scorers."""

from __future__ import annotations


def ascending_ranks(values: dict[str, float | None]) -> dict[str, int | None]:
    """Rank symbols 1..K ascending by value (1 = lowest, K = highest).

    Symbols with ``None`` values are unranked (``None``); K is the count of
    rankable symbols, not the universe size. Ties break deterministically by
    symbol name so repeated runs produce identical ranks.
    """
    rankable = sorted(
        ((v, s) for s, v in values.items() if v is not None),
        key=lambda pair: (pair[0], pair[1]),
    )
    ranks: dict[str, int | None] = {s: None for s in values}
    for position, (_, symbol) in enumerate(rankable, start=1):
        ranks[symbol] = position
    return ranks


def inverse_ranks(values: dict[str, float | None]) -> dict[str, int | None]:
    """Rank symbols 1..K descending by value (K = lowest value).

    Used where *low* is good (e.g. realized volatility → safety): the symbol
    with the lowest value receives the highest rank.
    """
    asc = ascending_ranks(values)
    ranked_count = sum(1 for r in asc.values() if r is not None)
    return {
        s: (ranked_count - r + 1 if r is not None else None) for s, r in asc.items()
    }

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/momentum.py`
  ```
"""Cross-sectional 12-1 month momentum (Jegadeesh-Titman 1993).

Formula (trading-day approximation of "month -12 to month -2"):

    r_12_1 = P[t-21] / P[t-252] - 1

where P is the daily close series (adjusted when available), t the last
session at or before the as-of date, 21 skipped sessions ≈ the most recent
month (short-term reversal), 252 sessions ≈ 12 months.

Kill condition: fewer than 253 sessions of usable history → no rank, status
INSUFFICIENT_DATA. The score ranks; it never produces an action by itself.
Parameters are literature defaults — not optimized on our data.
"""

from __future__ import annotations

from datetime import date

LOOKBACK_SESSIONS = 252
SKIP_SESSIONS = 21
MIN_SESSIONS = LOOKBACK_SESSIONS + 1


def twelve_minus_one_return(closes: list[float]) -> float | None:
    """12-1 month total return from a time-ordered daily close series.

    Returns None when history is insufficient (< MIN_SESSIONS bars) — the
    caller must surface INSUFFICIENT_DATA, never a substitute value.
    """
    if len(closes) < MIN_SESSIONS:
        return None
    end_price = closes[-1 - SKIP_SESSIONS]
    start_price = closes[-MIN_SESSIONS]
    if start_price <= 0:
        return None
    return end_price / start_price - 1.0


def momentum_window(dates: list[date]) -> tuple[date, date] | None:
    """The (start, end) trading dates the 12-1 return was computed over."""
    if len(dates) < MIN_SESSIONS:
        return None
    return dates[-MIN_SESSIONS], dates[-1 - SKIP_SESSIONS]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/safety.py`
  ```
"""Safety score: 12-month realized volatility, inverse-ranked.

Fills the QMJ safety dimension (Asness-Frazzini-Pedersen 2014) and overlaps
the low-volatility / Betting-Against-Beta evidence (Frazzini-Pedersen 2014):

    vol = stdev(daily simple returns over trailing 252 sessions) * sqrt(252)

Lowest volatility in the universe gets the highest rank. A low safety rank is
a risk flag, not a disqualifier. Kill condition: < 253 sessions → no rank,
INSUFFICIENT_DATA.
"""

from __future__ import annotations

import math
import statistics

VOL_WINDOW_SESSIONS = 252
MIN_SESSIONS = VOL_WINDOW_SESSIONS + 1
ANNUALIZATION_FACTOR = math.sqrt(252)

#: Annualized realized vol above this level is flagged as a risk regardless of rank.
HIGH_VOL_FLAG_THRESHOLD = 0.40


def realized_volatility_annualized(closes: list[float]) -> float | None:
    """Annualized stdev of daily simple returns over the trailing 252 sessions.

    Returns None on insufficient history (< 253 bars) or non-positive prices.
    """
    if len(closes) < MIN_SESSIONS:
        return None
    window = closes[-MIN_SESSIONS:]
    returns: list[float] = []
    for prev, curr in zip(window, window[1:]):
        if prev <= 0:
            return None
        returns.append(curr / prev - 1.0)
    if len(returns) < 2:
        return None
    return statistics.stdev(returns) * ANNUALIZATION_FACTOR

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/quality_fcf.py`
  ```
"""Quality/FCF composite and cash-based valuation context.

Composite of four sub-signals (weights below), each rank-scored across the
universe and combined into a 0-100 value:

- FCF/EV (primary weight): free cash flow / enterprise value. Hardest
  valuation metric to manipulate; strongest documented large-cap factor.
- FCF margin: FCF / revenue.
- Operating-margin stability: stdev of operating margin across trailing
  periods (lower stdev = steadier = better).
- Debt-to-equity: lower is better within the universe.

Derivations (explicit, no fabrication):
    fcf            = operating_cash_flow - capex
    market_cap     = price_as_of * shares_outstanding
    enterprise_val = market_cap + total_debt - cash_and_equivalents
    fcf_ev         = fcf / enterprise_value
    fcf_margin     = fcf / revenue
    debt_to_equity = total_debt / total_equity

Kill conditions: ETFs and symbols without fundamentals get no composite —
status INSUFFICIENT_DATA. Missing sub-fields shrink the composite's inputs
and are reported, never imputed.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from datetime import date

from research_data.factors.ranking import ascending_ranks, inverse_ranks

#: Sub-signal weights (must sum to 1.0). FCF/EV carries the primary weight.
WEIGHTS: dict[str, float] = {
    "fcf_ev": 0.40,
    "fcf_margin": 0.25,
    "op_margin_stability": 0.15,
    "debt_to_equity": 0.20,
}


@dataclass(frozen=True)
class FundamentalInputs:
    """Per-symbol fundamentals needed by the composite, with provenance.

    All monetary values in the statement's reporting currency (USD for the
    V1 universe). ``operating_margins`` holds trailing per-period operating
    margins (most recent last) for the stability check.
    """

    symbol: str
    as_of: date
    source: str
    revenue: float | None = None
    operating_cash_flow: float | None = None
    capex: float | None = None
    total_debt: float | None = None
    cash_and_equivalents: float | None = None
    total_equity: float | None = None
    shares_outstanding: float | None = None
    operating_margins: list[float] = field(default_factory=list)

    @property
    def fcf(self) -> float | None:
        if self.operating_cash_flow is None or self.capex is None:
            return None
        return self.operating_cash_flow - abs(self.capex)


@dataclass(frozen=True)
class QualityMetrics:
    """Derived per-symbol metrics feeding the cross-sectional composite."""

    symbol: str
    fcf_ev: float | None
    fcf_margin: float | None
    op_margin_stability: float | None  # stdev of operating margins (lower better)
    debt_to_equity: float | None
    market_cap: float | None
    enterprise_value: float | None
    fundamentals_as_of: date | None
    fundamentals_source: str | None


def derive_metrics(
    inputs: FundamentalInputs, price_as_of: float | None
) -> QualityMetrics:
    """Derive composite inputs from fundamentals + an as-of price.

    Every None stays None: a missing field is reported missing downstream,
    never replaced with an estimate.
    """
    market_cap: float | None = None
    if price_as_of is not None and inputs.shares_outstanding:
        market_cap = price_as_of * inputs.shares_outstanding

    enterprise_value: float | None = None
    if (
        market_cap is not None
        and inputs.total_debt is not None
        and inputs.cash_and_equivalents is not None
    ):
        enterprise_value = market_cap + inputs.total_debt - inputs.cash_and_equivalents

    fcf = inputs.fcf

    fcf_ev: float | None = None
    if fcf is not None and enterprise_value is not None and enterprise_value > 0:
        fcf_ev = fcf / enterprise_value

    fcf_margin: float | None = None
    if fcf is not None and inputs.revenue is not None and inputs.revenue > 0:
        fcf_margin = fcf / inputs.revenue

    stability: float | None = None
    if len(inputs.operating_margins) >= 4:
        stability = statistics.stdev(inputs.operating_margins)

    debt_to_equity: float | None = None
    if (
        inputs.total_debt is not None
        and inputs.total_equity is not None
        and inputs.total_equity > 0
    ):
        debt_to_equity = inputs.total_debt / inputs.total_equity

    return QualityMetrics(
        symbol=inputs.symbol,
        fcf_ev=fcf_ev,
        fcf_margin=fcf_margin,
        op_margin_stability=stability,
        debt_to_equity=debt_to_equity,
        market_cap=market_cap,
        enterprise_value=enterprise_value,
        fundamentals_as_of=inputs.as_of,
        fundamentals_source=inputs.source,
    )


def composite_scores(metrics: dict[str, QualityMetrics]) -> dict[str, float | None]:
    """Cross-sectional 0-100 composite per symbol via weighted rank-average.

    For each sub-signal, symbols are ranked across the universe (higher rank =
    better: high FCF/EV and FCF margin, low margin stdev, low leverage). Each
    rank is scaled to 0-100 and combined with WEIGHTS, renormalizing over the
    sub-signals the symbol actually has. A symbol with no sub-signals at all
    gets None.
    """
    fcf_ev_ranks = ascending_ranks({s: m.fcf_ev for s, m in metrics.items()})
    fcf_margin_ranks = ascending_ranks({s: m.fcf_margin for s, m in metrics.items()})
    stability_ranks = inverse_ranks(
        {s: m.op_margin_stability for s, m in metrics.items()}
    )
    leverage_ranks = inverse_ranks({s: m.debt_to_equity for s, m in metrics.items()})

    per_signal_ranks: dict[str, dict[str, int | None]] = {
        "fcf_ev": fcf_ev_ranks,
        "fcf_margin": fcf_margin_ranks,
        "op_margin_stability": stability_ranks,
        "debt_to_equity": leverage_ranks,
    }

    scores: dict[str, float | None] = {}
    for symbol in metrics:
        weighted_sum = 0.0
        weight_total = 0.0
        for signal, ranks in per_signal_ranks.items():
            rank = ranks[symbol]
            if rank is None:
                continue
            ranked_count = sum(1 for r in ranks.values() if r is not None)
            if ranked_count < 2:
                continue  # a rank within a single-symbol field carries no signal
            scaled = (rank - 1) / (ranked_count - 1) * 100.0
            weighted_sum += WEIGHTS[signal] * scaled
            weight_total += WEIGHTS[signal]
        scores[symbol] = round(weighted_sum / weight_total, 2) if weight_total else None
    return scores

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/etf_baseline.py`
  ```
"""ETF baseline comparison — every symbol is judged against VOO first.

Total return over overlapping usable sessions for standard windows
(~3, 6, 12 months of trading days). Refuses to compare when overlap is
insufficient; never interpolates missing sessions.
"""

from __future__ import annotations

from datetime import date

from research_data.factors.packets import BaselineWindowComparison

#: Trading-session windows: ~3 months, ~6 months, ~12 months.
DEFAULT_WINDOWS = (63, 126, 252)


def compare_to_benchmark(
    symbol_series: list[tuple[date, float]],
    benchmark_series: list[tuple[date, float]],
    windows: tuple[int, ...] = DEFAULT_WINDOWS,
) -> list[BaselineWindowComparison]:
    """Compare symbol vs benchmark total return on overlapping sessions.

    Both series are time-ordered (date, close). Only sessions present in BOTH
    series count; a window is produced only when the overlap covers at least
    ``window + 1`` shared sessions. No fill-forward, no fabrication.
    """
    benchmark_by_date = dict(benchmark_series)
    shared = [
        (d, price, benchmark_by_date[d])
        for d, price in symbol_series
        if d in benchmark_by_date
    ]

    comparisons: list[BaselineWindowComparison] = []
    for window in windows:
        if len(shared) < window + 1:
            continue
        window_slice = shared[-(window + 1) :]
        _, sym_start, bench_start = window_slice[0]
        _, sym_end, bench_end = window_slice[-1]
        if sym_start <= 0 or bench_start <= 0:
            continue
        comparisons.append(
            BaselineWindowComparison(
                window_sessions=window,
                symbol_return=sym_end / sym_start - 1.0,
                benchmark_return=bench_end / bench_start - 1.0,
                overlapping_sessions=len(window_slice),
            )
        )
    return comparisons

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ta_context.py`
  ```
"""Descriptive technical context — NEVER an action driver.

SMA 50/200, RSI-14 (Wilder smoothing), Bollinger position (std devs from the
20-day mean), and drawdown from the 52-week high. These describe price state
for a reader; none of them has robust standalone out-of-sample evidence, so
they are reported as values, not directives (factor-zoo filter).
"""

from __future__ import annotations

import statistics

from research_data.factors.packets import TAContext

RSI_PERIOD = 14
BOLLINGER_PERIOD = 20
SMA_SHORT = 50
SMA_LONG = 200
HIGH_52W_SESSIONS = 252


def simple_moving_average(closes: list[float], period: int) -> float | None:
    if len(closes) < period:
        return None
    return sum(closes[-period:]) / period


def rsi_14(closes: list[float], period: int = RSI_PERIOD) -> float | None:
    """Relative Strength Index with Wilder's smoothing. Reported, not acted on."""
    if len(closes) < period + 1:
        return None
    gains: list[float] = []
    losses: list[float] = []
    for prev, curr in zip(closes, closes[1:]):
        change = curr - prev
        gains.append(max(change, 0.0))
        losses.append(max(-change, 0.0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for gain, loss in zip(gains[period:], losses[period:]):
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period
    if avg_loss == 0:
        return 100.0
    relative_strength = avg_gain / avg_loss
    return 100.0 - 100.0 / (1.0 + relative_strength)


def bollinger_position(closes: list[float], period: int = BOLLINGER_PERIOD) -> float | None:
    """How many standard deviations the last close sits from the period mean."""
    if len(closes) < period:
        return None
    window = closes[-period:]
    mean = sum(window) / period
    stdev = statistics.stdev(window)
    if stdev == 0:
        return 0.0
    return (closes[-1] - mean) / stdev


def drawdown_from_52w_high(closes: list[float]) -> float | None:
    """Percentage decline of the last close from the trailing 52-week high."""
    if not closes:
        return None
    window = closes[-HIGH_52W_SESSIONS:]
    high = max(window)
    if high <= 0:
        return None
    return closes[-1] / high - 1.0


def build_ta_context(closes: list[float]) -> TAContext:
    """Compute all descriptive fields; anything uncomputable stays None."""
    sma_50 = simple_moving_average(closes, SMA_SHORT)
    sma_200 = simple_moving_average(closes, SMA_LONG)
    last = closes[-1] if closes else None

    price_vs_50 = None
    price_vs_200 = None
    ma_cross = None
    if last is not None and sma_50 is not None:
        price_vs_50 = "above" if last >= sma_50 else "below"
    if last is not None and sma_200 is not None:
        price_vs_200 = "above" if last >= sma_200 else "below"
    if sma_50 is not None and sma_200 is not None:
        ma_cross = "golden" if sma_50 >= sma_200 else "death"

    return TAContext(
        sma_50=sma_50,
        sma_200=sma_200,
        price_vs_sma_50=price_vs_50,
        price_vs_sma_200=price_vs_200,
        ma_cross=ma_cross,
        rsi_14=rsi_14(closes),
        bollinger_position=bollinger_position(closes),
        drawdown_from_52w_high=drawdown_from_52w_high(closes),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/engine.py`
  ```
"""FactorEngine — deterministic universe scoring into ScorePackets.

Reads prices exclusively through ``PriceReadAPI`` (require_usable=True),
takes fundamentals as explicit inputs (no fetching here), computes each
factor with its documented formula, and stamps quality + provenance on the
result. No LLM calls, no fabricated values: what cannot be computed is
reported as INSUFFICIENT_DATA.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

from research_data.factors import momentum as momentum_mod
from research_data.factors import safety as safety_mod
from research_data.factors.etf_baseline import compare_to_benchmark
from research_data.factors.packets import (
    EtfBaselineComparison,
    MomentumScore,
    PacketDataQuality,
    PacketProvenance,
    QualityFCFComponents,
    QualityFCFScore,
    SafetyScore,
    ScorePacket,
    ScoreStatus,
    TAContext,
    ValuationContext,
)
from research_data.factors.quality_fcf import (
    FundamentalInputs,
    composite_scores,
    derive_metrics,
)
from research_data.factors.ranking import ascending_ranks, inverse_ranks
from research_data.factors.ta_context import build_ta_context
from research_data.models import OHLCVRecord, QualityStatus
from research_data.read_api import PriceReadAPI

#: Calendar days of history requested to cover 253 trading sessions comfortably.
HISTORY_CALENDAR_DAYS = 550

#: Sessions needed for full momentum/safety windows.
FULL_WINDOW_SESSIONS = 253

#: Last price older than this many calendar days before as_of → STALE.
STALE_CALENDAR_DAYS = 5


class FactorEngine:
    """Computes ScorePackets for a universe as of a date."""

    def __init__(
        self,
        price_api: PriceReadAPI,
        benchmark_symbol: str = "VOO",
        price_source: str | None = None,
    ) -> None:
        self._price_api = price_api
        self._benchmark_symbol = benchmark_symbol
        self._price_source = price_source

    def compute_packets(
        self,
        symbols: list[str],
        as_of: date,
        fundamentals: dict[str, FundamentalInputs] | None = None,
        start: date | None = None,
    ) -> list[ScorePacket]:
        """Score every symbol in ``symbols`` as of ``as_of``.

        ``fundamentals`` maps symbol → FundamentalInputs for equities that
        have statement data; symbols absent from the map (including all ETFs)
        get INSUFFICIENT_DATA quality/valuation scores.
        """
        fundamentals = fundamentals or {}
        start = start or (as_of - timedelta(days=HISTORY_CALENDAR_DAYS))

        query_symbols = list(symbols)
        if self._benchmark_symbol not in query_symbols:
            query_symbols.append(self._benchmark_symbol)

        records = self._price_api.get_price_frame(
            symbols=query_symbols,
            start=start,
            end=as_of,
            source=self._price_source,
            require_usable=True,
        )
        by_symbol: dict[str, list[OHLCVRecord]] = {s: [] for s in query_symbols}
        for record in records:
            by_symbol[record.symbol].append(record)

        series: dict[str, list[tuple[date, float]]] = {}
        price_fields: dict[str, str] = {}
        for symbol, recs in by_symbol.items():
            use_adjusted = bool(recs) and all(r.adjusted_close is not None for r in recs)
            price_fields[symbol] = "adjusted_close" if use_adjusted else "close"
            series[symbol] = [
                (r.trading_date, r.adjusted_close if use_adjusted else r.close)
                for r in recs
            ]

        # Cross-sectional signals over the requested universe only.
        momentum_returns = {
            s: momentum_mod.twelve_minus_one_return([p for _, p in series[s]])
            for s in symbols
        }
        momentum_ranks = ascending_ranks(momentum_returns)
        momentum_ranked_count = sum(1 for r in momentum_ranks.values() if r is not None)

        vols = {
            s: safety_mod.realized_volatility_annualized([p for _, p in series[s]])
            for s in symbols
        }
        safety_ranks = inverse_ranks(vols)
        safety_ranked_count = sum(1 for r in safety_ranks.values() if r is not None)

        metrics = {}
        for symbol in symbols:
            inputs = fundamentals.get(symbol)
            if inputs is None:
                continue
            last_price = series[symbol][-1][1] if series[symbol] else None
            metrics[symbol] = derive_metrics(inputs, last_price)
        quality_values = composite_scores(metrics) if metrics else {}
        quality_ranked_count = sum(1 for v in quality_values.values() if v is not None)

        benchmark_series = series.get(self._benchmark_symbol, [])
        generated_at = datetime.now(timezone.utc)

        return [
            self._build_packet(
                symbol=symbol,
                as_of=as_of,
                universe=list(symbols),
                records=by_symbol[symbol],
                series=series[symbol],
                price_field=price_fields[symbol],
                momentum_return=momentum_returns[symbol],
                momentum_rank=momentum_ranks[symbol],
                momentum_ranked_count=momentum_ranked_count,
                vol=vols[symbol],
                safety_rank=safety_ranks[symbol],
                safety_ranked_count=safety_ranked_count,
                quality_value=quality_values.get(symbol),
                quality_ranked_count=quality_ranked_count,
                quality_metrics=metrics.get(symbol),
                benchmark_series=benchmark_series,
                generated_at=generated_at,
            )
            for symbol in symbols
        ]

    # -- per-symbol assembly ---------------------------------------------------

    def _build_packet(
        self,
        *,
        symbol: str,
        as_of: date,
        universe: list[str],
        records: list[OHLCVRecord],
        series: list[tuple[date, float]],
        price_field: str,
        momentum_return: float | None,
        momentum_rank: int | None,
        momentum_ranked_count: int,
        vol: float | None,
        safety_rank: int | None,
        safety_ranked_count: int,
        quality_value: float | None,
        quality_ranked_count: int,
        quality_metrics,
        benchmark_series: list[tuple[date, float]],
        generated_at: datetime,
    ) -> ScorePacket:
        closes = [p for _, p in series]
        dates = [d for d, _ in series]
        universe_size = len(universe)
        is_etf = bool(records) and records[0].asset_type == "etf"

        window = momentum_mod.momentum_window(dates)
        momentum_score = MomentumScore(
            status=ScoreStatus.OK if momentum_rank is not None else ScoreStatus.INSUFFICIENT_DATA,
            rank=momentum_rank,
            universe_size=universe_size,
            ranked_count=momentum_ranked_count,
            twelve_minus_one_return=momentum_return,
            window_start=window[0] if window else None,
            window_end=window[1] if window else None,
            price_field=price_field,
            context=(
                f"Ranks {momentum_rank} of {momentum_ranked_count} rankable symbols "
                f"on 12-1 month total return."
                if momentum_rank is not None
                else "Insufficient history for the 12-1 month window (needs 253 sessions)."
            ),
        )

        safety_score = SafetyScore(
            status=ScoreStatus.OK if safety_rank is not None else ScoreStatus.INSUFFICIENT_DATA,
            rank=safety_rank,
            universe_size=universe_size,
            ranked_count=safety_ranked_count,
            realized_vol_annualized=vol,
            window_start=dates[-safety_mod.MIN_SESSIONS] if len(dates) >= safety_mod.MIN_SESSIONS else None,
            window_end=dates[-1] if dates else None,
            context=(
                f"Ranks {safety_rank} of {safety_ranked_count} on inverse 12m realized "
                f"volatility (higher rank = lower volatility)."
                if safety_rank is not None
                else "Insufficient history for the 252-session volatility window."
            ),
        )

        if quality_metrics is not None:
            components = QualityFCFComponents(
                fcf_ev=quality_metrics.fcf_ev,
                fcf_margin=quality_metrics.fcf_margin,
                op_margin_stability=quality_metrics.op_margin_stability,
                debt_to_equity=quality_metrics.debt_to_equity,
                enterprise_value=quality_metrics.enterprise_value,
                market_cap=quality_metrics.market_cap,
                fundamentals_as_of=quality_metrics.fundamentals_as_of,
                fundamentals_source=quality_metrics.fundamentals_source,
            )
        else:
            components = QualityFCFComponents()

        quality_score = QualityFCFScore(
            status=ScoreStatus.OK if quality_value is not None else ScoreStatus.INSUFFICIENT_DATA,
            value=quality_value,
            universe_size=universe_size,
            ranked_count=quality_ranked_count,
            components=components,
            context=(
                "Weighted rank composite of FCF/EV, FCF margin, margin stability, leverage."
                if quality_value is not None
                else (
                    "ETF: issuer fundamentals not applicable."
                    if is_etf
                    else "No fundamentals available; composite not computed."
                )
            ),
        )

        p_fcf = None
        fcf_ev = quality_metrics.fcf_ev if quality_metrics else None
        if (
            quality_metrics is not None
            and quality_metrics.market_cap
            and quality_metrics.fcf_ev is not None
            and quality_metrics.enterprise_value
        ):
            fcf = quality_metrics.fcf_ev * quality_metrics.enterprise_value
            if fcf > 0:
                p_fcf = quality_metrics.market_cap / fcf
        valuation = ValuationContext(
            status=ScoreStatus.OK if fcf_ev is not None else ScoreStatus.INSUFFICIENT_DATA,
            fcf_ev=fcf_ev,
            p_fcf=p_fcf,
            sector_note=(
                "ETF — valuation applies to holdings, not the fund wrapper."
                if is_etf
                else "Raw P/E is not comparable across sectors; FCF/EV is primary."
            ),
            caveats=(
                []
                if fcf_ev is not None
                else ["FCF/EV unavailable — valuation context not computed."]
            ),
        )

        if symbol == self._benchmark_symbol:
            etf_baseline = EtfBaselineComparison(
                status=ScoreStatus.OK,
                benchmark_symbol=self._benchmark_symbol,
                windows=[],
                context="This symbol is the benchmark.",
            )
        else:
            comparisons = compare_to_benchmark(series, benchmark_series)
            etf_baseline = EtfBaselineComparison(
                status=ScoreStatus.OK if comparisons else ScoreStatus.INSUFFICIENT_DATA,
                benchmark_symbol=self._benchmark_symbol,
                windows=comparisons,
                context=(
                    "Total return vs benchmark over overlapping usable sessions."
                    if comparisons
                    else "Insufficient overlapping sessions with the benchmark."
                ),
            )

        ta = build_ta_context(closes) if closes else TAContext()

        data_quality = self._derive_data_quality(records, dates, as_of)

        risk_flags: list[str] = []
        if vol is not None and vol > safety_mod.HIGH_VOL_FLAG_THRESHOLD:
            risk_flags.append(
                f"12m realized volatility {vol:.2f} exceeds {safety_mod.HIGH_VOL_FLAG_THRESHOLD:.2f} —"
                " risk is elevated regardless of trend."
            )
        if (
            safety_rank is not None
            and safety_ranked_count >= 6
            and safety_rank <= max(2, safety_ranked_count // 5)
        ):
            risk_flags.append(
                f"safety_score rank {safety_rank} of {safety_ranked_count}: among the most volatile in the universe."
            )
        if not is_etf and quality_value is None:
            risk_flags.append("No fundamentals coverage — quality/valuation unassessed.")
        if data_quality.status != QualityStatus.USABLE:
            risk_flags.append(
                f"Data quality {data_quality.status.value}: confidence capped at {data_quality.max_confidence:.1f}."
            )

        provenance = PacketProvenance(
            price_source=records[0].source if records else None,
            price_field=price_field,
            first_price_date=dates[0] if dates else None,
            last_price_date=dates[-1] if dates else None,
            fundamentals_source=(
                quality_metrics.fundamentals_source if quality_metrics else None
            ),
            generated_at=generated_at,
        )

        return ScorePacket(
            symbol=symbol,
            as_of=as_of,
            universe=universe,
            momentum_score=momentum_score,
            safety_score=safety_score,
            quality_fcf_score=quality_score,
            valuation=valuation,
            etf_baseline=etf_baseline,
            ta_context=ta,
            risk_flags=risk_flags,
            data_quality=data_quality,
            provenance=provenance,
        )

    def _derive_data_quality(
        self, records: list[OHLCVRecord], dates: list[date], as_of: date
    ) -> PacketDataQuality:
        """Quality status for the packet, consistent with quality.py precedence.

        MISSING > STALE > INSUFFICIENT_DATA > PARTIAL > USABLE (CONTRADICTORY
        cannot occur here: require_usable filtering upstream excludes it).
        """
        rows = len(records)
        notes: list[str] = []
        if rows == 0:
            return PacketDataQuality(
                status=QualityStatus.MISSING,
                max_confidence=0.0,
                price_rows_used=0,
                notes=["No usable price rows in the requested window."],
            )
        last_date = dates[-1]
        if (as_of - last_date).days > STALE_CALENDAR_DAYS:
            status, cap = QualityStatus.STALE, 0.5
            notes.append(f"Last usable price is {last_date}, as_of is {as_of}.")
        elif rows < 50:
            status, cap = QualityStatus.INSUFFICIENT_DATA, 0.4
            notes.append(f"Only {rows} usable sessions (<50).")
        elif rows < FULL_WINDOW_SESSIONS:
            status, cap = QualityStatus.PARTIAL, 0.7
            notes.append(
                f"{rows} usable sessions — momentum/safety windows need {FULL_WINDOW_SESSIONS}."
            )
        else:
            status, cap = QualityStatus.USABLE, 1.0
        return PacketDataQuality(
            status=status, max_confidence=cap, price_rows_used=rows, notes=notes
        )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/factors/__init__.py`
  ```
"""Factor engine — deterministic, documented, killable math.

Primary signals (evidence-backed): momentum 12-1 rank, safety (inverse vol)
rank, quality/FCF composite, valuation FCF/EV, ETF baseline vs VOO.
TA (MA/RSI/Bollinger) is descriptive context only.

Every score carries its formula inputs, window, and status; anything that
cannot be computed from real data is INSUFFICIENT_DATA, never a guess.
"""

from research_data.factors.engine import FactorEngine
from research_data.factors.packets import (
    EtfBaselineComparison,
    MomentumScore,
    PacketDataQuality,
    PacketProvenance,
    QualityFCFScore,
    SafetyScore,
    ScorePacket,
    ScoreStatus,
    TAContext,
    ValuationContext,
)
from research_data.factors.quality_fcf import FundamentalInputs

__all__ = [
    "EtfBaselineComparison",
    "FactorEngine",
    "FundamentalInputs",
    "MomentumScore",
    "PacketDataQuality",
    "PacketProvenance",
    "QualityFCFScore",
    "SafetyScore",
    "ScorePacket",
    "ScoreStatus",
    "TAContext",
    "ValuationContext",
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/synthetic.py`
  ```
"""Deterministic synthetic OHLCV generators for factor/gate/paper tests.

Clearly labeled test data (source="synthetic_fixture") — used only to
exercise math and storage paths offline. Product code never fabricates data;
tests need long, controlled series that real 65-row CSV fixtures cannot give.
"""

from __future__ import annotations

import hashlib
import math
import random
from datetime import date, datetime, time, timedelta, timezone

from research_data.models import OHLCVRecord, PriceAdjustment, QualityStatus

SYNTHETIC_SOURCE = "synthetic_fixture"


def trading_days(end: date, sessions: int) -> list[date]:
    """The last ``sessions`` weekdays ending at ``end`` (inclusive if weekday).

    Weekend-skipping approximation of the NYSE calendar — good enough for
    factor-window math in tests.
    """
    days: list[date] = []
    current = end
    while len(days) < sessions:
        if current.weekday() < 5:
            days.append(current)
        current -= timedelta(days=1)
    return list(reversed(days))


def make_price_records(
    symbol: str,
    *,
    end: date,
    sessions: int,
    base_price: float = 100.0,
    daily_drift: float = 0.0004,
    daily_vol: float = 0.01,
    seed: int = 7,
    asset_type: str = "equity",
    exchange: str = "NASDAQ",
) -> list[OHLCVRecord]:
    """Seeded geometric random-walk daily bars, valid under OHLCV validation."""
    rng = random.Random(f"{symbol}:{seed}")
    dates = trading_days(end, sessions)
    retrieved_at = datetime.combine(end, time(23, 0), tzinfo=timezone.utc)
    payload_hash = hashlib.sha256(f"{symbol}:{seed}:{sessions}".encode()).hexdigest()

    records: list[OHLCVRecord] = []
    close = base_price
    for trading_date in dates:
        open_price = close
        close = open_price * math.exp(daily_drift + daily_vol * rng.gauss(0.0, 1.0))
        spread = abs(rng.gauss(0.0, daily_vol / 2))
        high = max(open_price, close) * (1 + spread)
        low = min(open_price, close) * (1 - spread)
        records.append(
            OHLCVRecord(
                symbol=symbol,
                asset_type=asset_type,
                exchange=exchange,
                trading_date=trading_date,
                open=round(open_price, 4),
                high=round(high, 4),
                low=round(low, 4),
                close=round(close, 4),
                adjusted_close=round(close, 4),
                volume=rng.randint(1_000_000, 5_000_000),
                split_factor=1.0,
                dividend_cash=0.0,
                price_adjustment=PriceAdjustment.SPLIT_DIVIDEND_ADJUSTED,
                currency="USD",
                source=SYNTHETIC_SOURCE,
                retrieved_at=retrieved_at,
                data_as_of=trading_date,
                raw_payload_hash=payload_hash,
                quality_status=QualityStatus.USABLE,
            )
        )
    return records


def daily_returns(records: list[OHLCVRecord]) -> list[float]:
    """Simple daily returns from a record series (adjusted close)."""
    closes = [r.adjusted_close or r.close for r in records]
    return [curr / prev - 1.0 for prev, curr in zip(closes, closes[1:])]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_factors_math.py`
  ```
"""Unit tests for individual factor formulas (kill-tests included)."""

from __future__ import annotations

import math
from datetime import date, timedelta

import pytest

from research_data.factors.etf_baseline import compare_to_benchmark
from research_data.factors.momentum import (
    MIN_SESSIONS,
    SKIP_SESSIONS,
    twelve_minus_one_return,
)
from research_data.factors.quality_fcf import (
    FundamentalInputs,
    composite_scores,
    derive_metrics,
)
from research_data.factors.ranking import ascending_ranks, inverse_ranks
from research_data.factors.safety import realized_volatility_annualized
from research_data.factors.ta_context import (
    bollinger_position,
    build_ta_context,
    drawdown_from_52w_high,
    rsi_14,
    simple_moving_average,
)


# -- momentum -----------------------------------------------------------------


def test_momentum_needs_full_window() -> None:
    assert twelve_minus_one_return([100.0] * (MIN_SESSIONS - 1)) is None


def test_momentum_skips_most_recent_month() -> None:
    # Flat at 100 for the 12-1 window, then a +50% melt-up in the skipped month:
    # the skip means the melt-up must NOT appear in the signal.
    closes = [100.0] * (MIN_SESSIONS - SKIP_SESSIONS) + [150.0] * SKIP_SESSIONS
    assert len(closes) == MIN_SESSIONS
    result = twelve_minus_one_return(closes)
    assert result == pytest.approx(0.0)


def test_momentum_known_value() -> None:
    # Price doubles linearly across the whole window.
    closes = [100.0 + i for i in range(MIN_SESSIONS)]
    expected = closes[-1 - SKIP_SESSIONS] / closes[0] - 1.0
    assert twelve_minus_one_return(closes) == pytest.approx(expected)


# -- ranking --------------------------------------------------------------------


def test_ascending_ranks_with_missing_values() -> None:
    ranks = ascending_ranks({"A": 0.10, "B": None, "C": -0.05, "D": 0.30})
    assert ranks == {"C": 1, "A": 2, "D": 3, "B": None}


def test_inverse_ranks_low_value_gets_top_rank() -> None:
    ranks = inverse_ranks({"LOWVOL": 0.10, "MIDVOL": 0.20, "HIGHVOL": 0.50})
    assert ranks == {"LOWVOL": 3, "MIDVOL": 2, "HIGHVOL": 1}


def test_rank_ties_break_deterministically_by_symbol() -> None:
    assert ascending_ranks({"B": 1.0, "A": 1.0}) == {"A": 1, "B": 2}


# -- safety -----------------------------------------------------------------------


def test_volatility_needs_full_window() -> None:
    assert realized_volatility_annualized([100.0] * 200) is None


def test_constant_prices_have_zero_volatility() -> None:
    vol = realized_volatility_annualized([100.0] * 300)
    assert vol == pytest.approx(0.0)


def test_alternating_returns_volatility() -> None:
    closes = [100.0]
    for i in range(299):
        closes.append(closes[-1] * (1.01 if i % 2 == 0 else 0.99))
    vol = realized_volatility_annualized(closes)
    assert vol is not None
    # Daily swing of ±1% → annualized vol near 0.01 * sqrt(252) ≈ 0.159.
    assert 0.10 < vol < 0.20


# -- quality / valuation -------------------------------------------------------------


def make_inputs(symbol: str, **overrides) -> FundamentalInputs:
    defaults = dict(
        symbol=symbol,
        as_of=date(2026, 3, 31),
        source="fixture",
        revenue=100e9,
        operating_cash_flow=40e9,
        capex=10e9,
        total_debt=20e9,
        cash_and_equivalents=15e9,
        total_equity=80e9,
        shares_outstanding=1e9,
        operating_margins=[0.30, 0.31, 0.29, 0.30],
    )
    defaults.update(overrides)
    return FundamentalInputs(**defaults)


def test_derive_metrics_formulas() -> None:
    metrics = derive_metrics(make_inputs("AAPL"), price_as_of=200.0)
    # market_cap = 200 * 1e9 = 200e9 ; EV = 200e9 + 20e9 - 15e9 = 205e9
    assert metrics.market_cap == pytest.approx(200e9)
    assert metrics.enterprise_value == pytest.approx(205e9)
    # fcf = 40e9 - 10e9 = 30e9 → fcf_ev ≈ 0.14634 ; fcf_margin = 0.30
    assert metrics.fcf_ev == pytest.approx(30e9 / 205e9)
    assert metrics.fcf_margin == pytest.approx(0.30)
    assert metrics.debt_to_equity == pytest.approx(0.25)
    assert metrics.op_margin_stability is not None


def test_derive_metrics_never_fabricates() -> None:
    metrics = derive_metrics(
        make_inputs("MSFT", operating_cash_flow=None, operating_margins=[]),
        price_as_of=None,
    )
    assert metrics.market_cap is None
    assert metrics.enterprise_value is None
    assert metrics.fcf_ev is None
    assert metrics.fcf_margin is None
    assert metrics.op_margin_stability is None


def test_composite_orders_better_fundamentals_higher() -> None:
    strong = derive_metrics(make_inputs("STRONG"), price_as_of=100.0)
    weak = derive_metrics(
        make_inputs(
            "WEAK",
            operating_cash_flow=12e9,
            total_debt=60e9,
            operating_margins=[0.10, 0.25, 0.05, 0.30],
        ),
        price_as_of=100.0,
    )
    scores = composite_scores({"STRONG": strong, "WEAK": weak})
    assert scores["STRONG"] is not None and scores["WEAK"] is not None
    assert scores["STRONG"] > scores["WEAK"]
    assert 0.0 <= scores["WEAK"] <= scores["STRONG"] <= 100.0


def test_composite_returns_none_without_data() -> None:
    empty = derive_metrics(
        FundamentalInputs(symbol="ETF", as_of=date(2026, 3, 31), source="fixture"),
        price_as_of=None,
    )
    strong = derive_metrics(make_inputs("STRONG"), price_as_of=100.0)
    other = derive_metrics(make_inputs("OTHER", total_debt=30e9), price_as_of=90.0)
    scores = composite_scores({"ETF": empty, "STRONG": strong, "OTHER": other})
    assert scores["ETF"] is None


# -- ETF baseline ----------------------------------------------------------------


def _series(start: date, prices: list[float]) -> list[tuple[date, float]]:
    days = []
    current = start
    while len(days) < len(prices):
        if current.weekday() < 5:
            days.append(current)
        current += timedelta(days=1)
    return list(zip(days, prices))


def test_compare_to_benchmark_overlapping_windows() -> None:
    start = date(2025, 1, 6)
    symbol = _series(start, [100.0 * math.exp(0.001 * i) for i in range(300)])
    benchmark = _series(start, [50.0 * math.exp(0.0005 * i) for i in range(300)])
    comparisons = compare_to_benchmark(symbol, benchmark)
    assert [c.window_sessions for c in comparisons] == [63, 126, 252]
    for c in comparisons:
        assert c.symbol_return > c.benchmark_return > 0
        assert c.overlapping_sessions == c.window_sessions + 1


def test_compare_to_benchmark_refuses_thin_overlap() -> None:
    start = date(2026, 5, 1)
    symbol = _series(start, [100.0] * 30)
    benchmark = _series(start, [50.0] * 30)
    assert compare_to_benchmark(symbol, benchmark) == []


# -- TA context (descriptive only) --------------------------------------------------


def test_sma_and_rsi_bounds() -> None:
    closes = [100.0 + (i % 7) for i in range(260)]
    assert simple_moving_average(closes, 50) is not None
    rsi = rsi_14(closes)
    assert rsi is not None and 0.0 <= rsi <= 100.0


def [REDACTED]() -> None:
    closes = [100.0 * (1.01**i) for i in range(30)]
    assert rsi_14(closes) == pytest.approx(100.0)


def test_bollinger_and_drawdown() -> None:
    closes = [100.0] * 19 + [110.0]
    pos = bollinger_position(closes)
    assert pos is not None and pos > 2.0
    dd = drawdown_from_52w_high([100.0, 120.0, 90.0])
    assert dd == pytest.approx(90.0 / 120.0 - 1.0)


def test_ta_context_is_descriptive_only() -> None:
    context = build_ta_context([100.0 + i * 0.1 for i in range(260)])
    dumped = context.model_dump_json().lower()
    # Guardrail: TA context must not carry action or execution words.
    for forbidden in ("buy", "sell", "accumulate", "reduce", "guaranteed"):
        assert forbidden not in dumped
    assert context.ma_cross == "golden"
    assert context.price_vs_sma_200 == "above"

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_factors_engine.py`
  ```
"""Integration tests for FactorEngine on synthetic DuckDB data."""

from __future__ import annotations

import json
from datetime import date

import duckdb
import pytest

from research_data.factors import FactorEngine, FundamentalInputs, ScoreStatus
from research_data.models import QualityStatus
from research_data.read_api import PriceReadAPI
from research_data.storage import batch_insert_ohlcv, init_db

from tests.synthetic import make_price_records

AS_OF = date(2026, 6, 30)
FULL = 320  # sessions — enough for the 253-session windows
SHORT = 120  # sessions — PARTIAL quality, no momentum/safety rank


@pytest.fixture(scope="module")
def engine_and_packets():
    conn = duckdb.connect(":memory:")
    init_db(conn)
    records = []
    # VOO: benchmark, moderate drift/vol.
    records += make_price_records(
        "VOO", end=AS_OF, sessions=FULL, base_price=400.0,
        daily_drift=0.0004, daily_vol=0.008, asset_type="etf", exchange="NYSE",
    )
    # HIGHMO: strong uptrend → top momentum rank.
    records += make_price_records(
        "AAPL", end=AS_OF, sessions=FULL, base_price=150.0,
        daily_drift=0.0020, daily_vol=0.012,
    )
    # LOWVOL: quiet series → top safety rank.
    records += make_price_records(
        "MSFT", end=AS_OF, sessions=FULL, base_price=300.0,
        daily_drift=0.0002, daily_vol=0.004,
    )
    # WILD: high volatility, negative drift → bottom safety rank + risk flag.
    records += make_price_records(
        "TSLA", end=AS_OF, sessions=FULL, base_price=200.0,
        daily_drift=-0.0010, daily_vol=0.035,
    )
    # SHORTHIST: not enough sessions for the factor windows.
    records += make_price_records(
        "META", end=AS_OF, sessions=SHORT, base_price=500.0,
        daily_drift=0.0005, daily_vol=0.015,
    )
    batch_insert_ohlcv(conn, records)

    fundamentals = {
        "AAPL": FundamentalInputs(
            symbol="AAPL", as_of=date(2026, 3, 31), source="fixture",
            revenue=400e9, operating_cash_flow=110e9, capex=11e9,
            total_debt=100e9, cash_and_equivalents=60e9, total_equity=70e9,
            shares_outstanding=15e9,
            operating_margins=[0.30, 0.31, 0.30, 0.29],
        ),
        "MSFT": FundamentalInputs(
            symbol="MSFT", as_of=date(2026, 3, 31), source="fixture",
            revenue=250e9, operating_cash_flow=120e9, capex=30e9,
            total_debt=45e9, cash_and_equivalents=80e9, total_equity=240e9,
            shares_outstanding=7.4e9,
            operating_margins=[0.44, 0.45, 0.44, 0.46],
        ),
        # TSLA: deliberately no fundamentals → INSUFFICIENT_DATA path for an equity.
    }

    engine = FactorEngine(PriceReadAPI(conn), benchmark_symbol="VOO")
    universe = ["VOO", "AAPL", "MSFT", "TSLA", "META"]
    packets = engine.compute_packets(universe, AS_OF, fundamentals=fundamentals)
    return engine, {p.symbol: p for p in packets}


def test_every_symbol_gets_a_packet(engine_and_packets) -> None:
    _, packets = engine_and_packets
    assert set(packets) == {"VOO", "AAPL", "MSFT", "TSLA", "META"}


def test_momentum_ranks_reflect_drift(engine_and_packets) -> None:
    _, packets = engine_and_packets
    ranked = {s: p.momentum_score.rank for s, p in packets.items()}
    # 4 rankable (META lacks history); AAPL's strong drift must rank top.
    assert ranked["AAPL"] == 4
    assert packets["AAPL"].momentum_score.twelve_minus_one_return > 0
    assert ranked["META"] is None
    assert packets["META"].momentum_score.status == ScoreStatus.INSUFFICIENT_DATA


def test_safety_ranks_reflect_volatility(engine_and_packets) -> None:
    _, packets = engine_and_packets
    assert packets["MSFT"].safety_score.rank == 4  # lowest vol of 4 rankable
    assert packets["TSLA"].safety_score.rank == 1  # wildest
    assert packets["TSLA"].safety_score.realized_vol_annualized > 0.4


def test_wild_symbol_carries_risk_flags(engine_and_packets) -> None:
    _, packets = engine_and_packets
    flags = " ".join(packets["TSLA"].risk_flags)
    assert "volatility" in flags


def test_quality_scores_only_with_fundamentals(engine_and_packets) -> None:
    _, packets = engine_and_packets
    assert packets["AAPL"].quality_fcf_score.status == ScoreStatus.OK
    assert packets["MSFT"].quality_fcf_score.status == ScoreStatus.OK
    assert 0 <= packets["AAPL"].quality_fcf_score.value <= 100
    # Equity without fundamentals: insufficient, flagged, never fabricated.
    tsla_quality = packets["TSLA"].quality_fcf_score
    assert tsla_quality.status == ScoreStatus.INSUFFICIENT_DATA
    assert tsla_quality.value is None
    # ETF: explicitly not applicable.
    voo_quality = packets["VOO"].quality_fcf_score
    assert voo_quality.status == ScoreStatus.INSUFFICIENT_DATA
    assert "ETF" in voo_quality.context


def test_valuation_derived_from_same_components(engine_and_packets) -> None:
    _, packets = engine_and_packets
    valuation = packets["MSFT"].valuation
    assert valuation.status == ScoreStatus.OK
    assert valuation.fcf_ev == packets["MSFT"].quality_fcf_score.components.fcf_ev
    assert valuation.p_fcf is not None and valuation.p_fcf > 0


def test_etf_baseline_windows_present(engine_and_packets) -> None:
    _, packets = engine_and_packets
    baseline = packets["AAPL"].etf_baseline
    assert baseline.benchmark_symbol == "VOO"
    assert [w.window_sessions for w in baseline.windows] == [63, 126, 252]
    assert packets["VOO"].etf_baseline.context == "This symbol is the benchmark."


def test_data_quality_caps_confidence(engine_and_packets) -> None:
    _, packets = engine_and_packets
    assert packets["AAPL"].data_quality.status == QualityStatus.USABLE
    assert packets["AAPL"].data_quality.max_confidence == 1.0
    meta_quality = packets["META"].data_quality
    assert meta_quality.status == QualityStatus.PARTIAL
    assert meta_quality.max_confidence == 0.7
    assert any("capped" in f for f in packets["META"].risk_flags)


def test_missing_symbol_reports_missing_not_fabricated() -> None:
    conn = duckdb.connect(":memory:")
    init_db(conn)
    batch_insert_ohlcv(
        conn,
        make_price_records("VOO", end=AS_OF, sessions=FULL, base_price=400.0,
                           asset_type="etf", exchange="NYSE"),
    )
    engine = FactorEngine(PriceReadAPI(conn), benchmark_symbol="VOO")
    packets = {p.symbol: p for p in engine.compute_packets(["VOO", "JPM"], AS_OF)}
    jpm = packets["JPM"]
    assert jpm.data_quality.status == QualityStatus.MISSING
    assert jpm.data_quality.max_confidence == 0.0
    assert jpm.momentum_score.status == ScoreStatus.INSUFFICIENT_DATA
    assert jpm.provenance.price_source is None


def test_packets_contain_no_execution_language(engine_and_packets) -> None:
    _, packets = engine_and_packets
    for packet in packets.values():
        dumped = json.dumps(packet.model_dump(mode="json")).lower()
        for forbidden in ('"buy"', '"sell"', "guaranteed", "risk-free", "risk free"):
            assert forbidden not in dumped, f"{packet.symbol}: {forbidden}"


def test_ta_context_never_produces_actions(engine_and_packets) -> None:
    _, packets = engine_and_packets
    for packet in packets.values():
        assert "not an action driver" in packet.ta_context.note.lower()

  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_factors_math.py tests/test_factors_engine.py -q 2>&1 | tail -8`
  ```
        # 4 rankable (META lacks history); AAPL's strong drift must rank top.
>       assert ranked["AAPL"] == 4
E       assert 3 == 4

tests/test_factors_engine.py:88: AssertionError
=========================== short test summary info ============================
FAILED tests/test_factors_engine.py::test_momentum_ranks_reflect_drift - asse...
1 failed, 29 passed in 9.39s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python - <<'EOF'
from datetime import date
from tests.synthetic import make_price_records
from research_data.factors.momentum import twelve_minus_one_return
AS_OF = date(2026, 6, 30)
for sym, drift, vol in [("VOO",0.0004,0.008),("AAPL",0.0020,0.012),("MSFT",0.0002,0.004),("TSLA",-0.0010,0.035)]:
    recs = make_price_records(sym, end=AS_OF, sessions=320, base_price=100.0, daily_drift=drift, daily_vol=vol, asset_type="etf" if sym=="VOO" else "equity", exchange="NYSE")
    closes = [r.adjusted_close for r in recs]
    print(sym, round(twelve_minus_one_return(closes), 4))
EOF
  ```
  ```
VOO -0.0611
AAPL 0.2355
MSFT 0.1071
TSLA 0.6624
  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python - <<'EOF'
from datetime import date
from tests.synthetic import make_price_records
from research_data.factors.momentum import twelve_minus_one_return
from research_data.factors.safety import realized_volatility_annualized
AS_OF = date(2026, 6, 30)
for seed in range(3, 15):
    recs = make_price_records("TSLA", end=AS_OF, sessions=320, base_price=200.0, daily_drift=-0.0010, daily_vol=0.035, seed=seed)
    closes = [r.adjusted_close for r in recs]
    print(seed, round(twelve_minus_one_return(closes),4), round(realized_volatility_annualized(closes),3))
EOF
  ```
  ```
3 -0.572 0.553
4 -0.4036 0.486
5 0.139 0.574
6 -0.7472 0.531
7 0.6624 0.609
8 -0.3979 0.57
9 1.311 0.55
10 -0.5798 0.517
11 0.3532 0.54
12 -0.5209 0.506
13 0.4779 0.528
14 -0.8086 0.56
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/tests/test_factors_engine.py`
  ```diff
  -     # WILD: high volatility, negative drift → bottom safety rank + risk flag.
    records += make_price_records(
        "TSLA", end=AS_OF, sessions=FULL, base_price=200.0,
        daily_drift=-0.0010, daily_vol=0.035,
    )
  +     # WILD: high volatility, negative drift → bottom safety rank + risk flag.
    # seed=4 keeps this walk's 12-1 return below AAPL's (vol 0.035 can out-drift
    # it on other seeds).
    records += make_price_records(
        "TSLA", end=AS_OF, sessions=FULL, base_price=200.0,
        daily_drift=-0.0010, daily_vol=0.035, seed=4,
    )
  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_factors_math.py tests/test_factors_engine.py -q 2>&1 | tail -3`
  ```
..............................                                           [100%]
30 passed in 8.78s
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/config/assets.toml`
  ```diff
  - symbols = ["VOO", "VTI", "SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META"]
  + symbols = ["VOO", "VTI", "SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "BRKB", "JPM", "COST", "TSLA"]
  ```
- `Bash`:
  ```bash
cat >> config/assets.toml <<'EOF'

[assets.BRKB]
# Canonical symbol is letters-only (BRKB); provider clients map to their own
# punctuation (Polygon "BRK.B", SEC "BRK-B").
symbol = "BRKB"
asset_type = "equity"
name = "Berkshire Hathaway Inc. Class B (BRK.B)"
exchange = "NYSE"
currency = "USD"
benchmark_symbol = "VOO"

[assets.JPM]
symbol = "JPM"
asset_type = "equity"
name = "JPMorgan Chase & Co."
exchange = "NYSE"
currency = "USD"
benchmark_symbol = "VOO"

[assets.COST]
symbol = "COST"
asset_type = "equity"
name = "Costco Wholesale Corporation"
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"

[assets.TSLA]
symbol = "TSLA"
asset_type = "equity"
name = "Tesla, Inc."
exchange = "NASDAQ"
currency = "USD"
benchmark_symbol = "VOO"
EOF
source .venv/bin/activate && python -c "
from research_data.config import load_config
c = load_config()
assert len(c.universe.symbols) == 14, c.universe.symbols
assert set(c.universe.symbols) == set(c.universe.assets), 'symbols/assets mismatch'
print('universe ok:', c.universe.symbols)
" && python -m pytest tests/test_provider_registry.py tests/test_property_provider_registry.py -q 2>&1 | tail -2
  ```
  ```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
AssertionError: ['VOO', 'VTI', 'SPY', 'QQQ', 'AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META']
  ```
- `Read` — `/home/anant_gupta/projects/hub/tradingview/config/assets.toml`
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/config/assets.toml`
  ```diff
  - symbols = ["VOO", "VTI", "SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META"]
  + symbols = ["VOO", "VTI", "SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "BRKB", "JPM", "COST", "TSLA"]
  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python -c "
from research_data.config import load_config
c = load_config()
assert len(c.universe.symbols) == 14, c.universe.symbols
assert set(c.universe.symbols) == set(c.universe.assets), 'symbols/assets mismatch'
print('universe ok, 14 symbols')
" && python -m pytest -q 2>&1 | tail -2
  ```
  ```
universe ok, 14 symbols
......                                                                   [100%]
366 passed in 61.97s (0:01:01)
  ```
- `TaskUpdate` — `{"taskId":"3","status":"completed"}`
- `TaskUpdate` — `{"taskId":"4","status":"in_progress","activeForm":"Implementing fundamentals path"}`
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/__init__.py`
  ```
"""Minimal fundamentals path: FMP + SEC EDGAR → provenance-stamped snapshots.

Just enough for the quality/valuation factors: revenue, operating income,
operating cash flow, capex (→ FCF), debt, cash, equity, shares outstanding.
Parsing is pure and offline-testable; live clients are thin and keyed via
environment variables (FMP_API_KEY, SEC_USER_AGENT). Missing fields stay
None — they are never imputed.
"""

from research_data.fundamentals.models import (
    FundamentalsFetchResult,
    FundamentalsSnapshot,
)
from research_data.fundamentals.store import FundamentalsStore, to_factor_inputs
from research_data.fundamentals.fmp import FMPFundamentalsClient, parse_fmp_statements
from research_data.fundamentals.sec import SECEdgarClient, parse_companyfacts

__all__ = [
    "FMPFundamentalsClient",
    "FundamentalsFetchResult",
    "FundamentalsSnapshot",
    "FundamentalsStore",
    "SECEdgarClient",
    "parse_companyfacts",
    "parse_fmp_statements",
    "to_factor_inputs",
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/models.py`
  ```
"""Typed fundamentals records with full provenance."""

from __future__ import annotations

import uuid
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class FundamentalsSnapshot(BaseModel):
    """One statement period for one symbol from one source.

    All monetary fields are in ``currency`` (USD for the V1 universe) and may
    be None when the source did not report them — missing means missing.
    ``capex`` is stored as a positive magnitude (cash spent on PP&E).
    """

    snapshot_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    symbol: str
    source: str  # "fmp" | "sec_edgar" | "fixture"
    period_type: Literal["annual", "quarter"]
    fiscal_period_end: date
    retrieved_at: datetime
    raw_payload_hash: str
    currency: str = "USD"

    revenue: float | None = None
    operating_income: float | None = None
    operating_cash_flow: float | None = None
    capex: float | None = None
    total_debt: float | None = None
    cash_and_equivalents: float | None = None
    total_equity: float | None = None
    shares_outstanding: float | None = None

    @field_validator("raw_payload_hash")
    @classmethod
    def validate_hash(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("raw_payload_hash must be non-empty (provenance required)")
        return v

    @property
    def operating_margin(self) -> float | None:
        if self.operating_income is None or self.revenue is None or self.revenue <= 0:
            return None
        return self.operating_income / self.revenue


class FundamentalsFetchResult(BaseModel):
    """Result of a fundamentals fetch: snapshots + raw payloads for audit.

    ``request_urls`` must already be secret-free (API keys stripped before
    storage — see the clients).
    """

    symbol: str
    source: str
    retrieved_at: datetime
    request_urls: list[str] = Field(default_factory=list)
    raw_payloads: dict[str, str] = Field(default_factory=dict)  # label → raw JSON
    snapshots: list[FundamentalsSnapshot] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/fmp.py`
  ```
"""Financial Modeling Prep fundamentals client.

Pure parsing (offline-testable) + a thin live client. The API key is read
from the environment at call time, appended to the request URL for the call
only, and never stored: ``request_urls`` in results are key-free.
"""

from __future__ import annotations

import hashlib
import json
import os
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

from research_data.fundamentals.models import (
    FundamentalsFetchResult,
    FundamentalsSnapshot,
)

FMP_BASE_URL = "https://financialmodelingprep.com/api/v3"
API_KEY_ENV_VAR = "FMP_API_KEY"
_STATEMENTS = ("income-statement", "balance-sheet-statement", "cash-flow-statement")


class FMPError(Exception):
    """Raised when the FMP client cannot fetch or parse fundamentals."""


def parse_fmp_statements(
    symbol: str,
    income_json: str,
    balance_json: str,
    cashflow_json: str,
    retrieved_at: datetime,
    source: str = "fmp",
) -> list[FundamentalsSnapshot]:
    """Merge FMP income/balance/cash-flow statements into snapshots by period.

    Only fields present in the payloads are set; anything absent stays None.
    Periods missing from any statement produce a snapshot with the fields
    that exist — never estimated ones.
    """
    payload_hash = hashlib.sha256(
        (income_json + balance_json + cashflow_json).encode("utf-8")
    ).hexdigest()

    def load(raw: str, label: str) -> list[dict]:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            raise FMPError(f"Invalid JSON in FMP {label} payload: {e}") from e
        if not isinstance(data, list):
            raise FMPError(f"Unexpected FMP {label} payload shape: expected a list")
        return data

    by_period: dict[tuple[str, str], dict[str, dict]] = {}
    for label, raw in (
        ("income", income_json),
        ("balance", balance_json),
        ("cashflow", cashflow_json),
    ):
        for entry in load(raw, label):
            key = (str(entry.get("date", "")), str(entry.get("period", "")))
            if not key[0]:
                continue
            by_period.setdefault(key, {})[label] = entry

    snapshots: list[FundamentalsSnapshot] = []
    for (period_end, period_label), parts in sorted(by_period.items()):
        income = parts.get("income", {})
        balance = parts.get("balance", {})
        cashflow = parts.get("cashflow", {})
        period_type = "annual" if period_label.upper() == "FY" else "quarter"
        capex = _num(cashflow.get("capitalExpenditure"))
        snapshots.append(
            FundamentalsSnapshot(
                symbol=symbol,
                source=source,
                period_type=period_type,
                fiscal_period_end=date.fromisoformat(period_end),
                retrieved_at=retrieved_at,
                raw_payload_hash=payload_hash,
                currency=str(income.get("reportedCurrency") or "USD"),
                revenue=_num(income.get("revenue")),
                operating_income=_num(income.get("operatingIncome")),
                operating_cash_flow=_num(cashflow.get("operatingCashFlow")),
                capex=abs(capex) if capex is not None else None,
                total_debt=_num(balance.get("totalDebt")),
                cash_and_equivalents=_num(balance.get("cashAndCashEquivalents")),
                total_equity=_num(balance.get("totalStockholdersEquity")),
                shares_outstanding=_num(income.get("weightedAverageShsOut")),
            )
        )
    return snapshots


def _num(value) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


class FMPFundamentalsClient:
    """Thin live client. Requires FMP_API_KEY in the environment."""

    def __init__(self, timeout_seconds: float = 30.0) -> None:
        self._timeout = timeout_seconds

    def fetch_statements(
        self, symbol: str, period: str = "quarter", limit: int = 8
    ) -> FundamentalsFetchResult:
        """Fetch income/balance/cash-flow statements and parse to snapshots."""
        api_key = os.environ.get(API_KEY_ENV_VAR)
        if not api_key:
            raise FMPError(
                f"{API_KEY_ENV_VAR} is not set; cannot fetch FMP fundamentals. "
                "Offline paths must use fixtures instead."
            )
        retrieved_at = datetime.now(timezone.utc)
        raw: dict[str, str] = {}
        clean_urls: list[str] = []
        warnings: list[str] = []
        for statement in _STATEMENTS:
            params = {"period": period, "limit": str(limit)}
            clean_url = (
                f"{FMP_BASE_URL}/{statement}/{urllib.parse.quote(symbol)}"
                f"?{urllib.parse.urlencode(params)}"
            )
            clean_urls.append(clean_url)  # stored: no apikey
            request_url = f"{clean_url}&apikey={urllib.parse.quote(api_key)}"
            request = urllib.request.Request(
                request_url, headers={"Accept": "application/json"}
            )
            try:
                with urllib.request.urlopen(request, timeout=self._timeout) as response:
                    raw[statement] = response.read().decode("utf-8")
            except OSError as e:
                raise FMPError(f"FMP request failed for {clean_url}: {e}") from e

        snapshots = parse_fmp_statements(
            symbol,
            raw["income-statement"],
            raw["balance-sheet-statement"],
            raw["cash-flow-statement"],
            retrieved_at,
        )
        if not snapshots:
            warnings.append(
                f"FMP returned no statement periods for {symbol}; "
                "surfacing empty result (no fabrication)."
            )
        return FundamentalsFetchResult(
            symbol=symbol,
            source="fmp",
            retrieved_at=retrieved_at,
            request_urls=clean_urls,
            raw_payloads=raw,
            snapshots=snapshots,
            warnings=warnings,
        )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/sec.py`
  ```
"""SEC EDGAR companyfacts client.

Free, keyless, but identity-required: every request carries the User-Agent
from SEC_USER_AGENT (format "PersonalAITradingDesk email@domain") per SEC
fair-access policy, with a polite minimum interval between requests.

Parsing is pure (offline-testable) over the companyfacts JSON shape:
us-gaap/dei concepts → the minimal field set the quality factor needs.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
from datetime import date, datetime, timezone

from research_data.fundamentals.models import (
    FundamentalsFetchResult,
    FundamentalsSnapshot,
)

SEC_USER_AGENT_ENV_VAR = "SEC_USER_AGENT"
COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
COMPANYFACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:0>10}.json"

#: SEC fair-access: stay well under 10 requests/second.
MIN_REQUEST_INTERVAL_SECONDS = 0.15

#: Canonical letters-only symbols → SEC ticker punctuation.
SEC_TICKER_OVERRIDES = {"BRKB": "BRK-B"}

# us-gaap concept fallbacks, first hit wins.
_CONCEPTS: dict[str, tuple[str, ...]] = {
    "revenue": (
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "SalesRevenueNet",
    ),
    "operating_income": ("OperatingIncomeLoss",),
    "operating_cash_flow": ("NetCashProvidedByUsedInOperatingActivities",),
    "capex": (
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsToAcquireProductiveAssets",
    ),
    "total_debt": ("LongTermDebt", "LongTermDebtNoncurrent"),
    "cash_and_equivalents": ("CashAndCashEquivalentsAtCarryingValue",),
    "total_equity": ("StockholdersEquity",),
}


class SECEdgarError(Exception):
    """Raised when the SEC client cannot fetch or parse companyfacts."""


def parse_companyfacts(
    symbol: str,
    companyfacts_json: str,
    retrieved_at: datetime,
    max_periods: int = 12,
    source: str = "sec_edgar",
) -> list[FundamentalsSnapshot]:
    """Extract per-period snapshots from a companyfacts payload.

    Facts are grouped by (fiscal period end, form type): 10-K FY entries make
    annual snapshots, 10-Q entries quarterly ones. Duration concepts (revenue,
    cash flow) use their period ``end``; instant concepts (debt, cash, equity)
    attach to the same end date. Fields the filer did not tag stay None.
    """
    try:
        data = json.loads(companyfacts_json)
    except json.JSONDecodeError as e:
        raise SECEdgarError(f"Invalid companyfacts JSON: {e}") from e

    payload_hash = hashlib.sha256(companyfacts_json.encode("utf-8")).hexdigest()
    gaap = data.get("facts", {}).get("us-gaap", {})
    dei = data.get("facts", {}).get("dei", {})

    periods: dict[tuple[str, str], dict[str, float]] = {}

    def collect(concept_data: dict, field_name: str) -> None:
        units = concept_data.get("units", {})
        entries = units.get("USD") or units.get("shares") or []
        for entry in entries:
            end = entry.get("end")
            form = str(entry.get("form", ""))
            value = entry.get("val")
            if not end or value is None:
                continue
            if form not in ("10-K", "10-Q"):
                continue
            fp = str(entry.get("fp", ""))
            period_type = "annual" if form == "10-K" and fp == "FY" else "quarter"
            # For duration concepts, an annual 10-K entry spans the full year;
            # keep quarterly and annual periods separate.
            key = (end, period_type)
            periods.setdefault(key, {})[field_name] = float(value)

    for field_name, concept_names in _CONCEPTS.items():
        for concept in concept_names:
            if concept in gaap:
                collect(gaap[concept], field_name)
                break

    shares_concept = dei.get("EntityCommonStockSharesOutstanding")
    if shares_concept:
        collect(shares_concept, "shares_outstanding")

    snapshots: list[FundamentalsSnapshot] = []
    for (end, period_type), fields in sorted(periods.items())[-max_periods:]:
        capex = fields.get("capex")
        snapshots.append(
            FundamentalsSnapshot(
                symbol=symbol,
                source=source,
                period_type=period_type,  # type: ignore[arg-type]
                fiscal_period_end=date.fromisoformat(end),
                retrieved_at=retrieved_at,
                raw_payload_hash=payload_hash,
                revenue=fields.get("revenue"),
                operating_income=fields.get("operating_income"),
                operating_cash_flow=fields.get("operating_cash_flow"),
                capex=abs(capex) if capex is not None else None,
                total_debt=fields.get("total_debt"),
                cash_and_equivalents=fields.get("cash_and_equivalents"),
                total_equity=fields.get("total_equity"),
                shares_outstanding=fields.get("shares_outstanding"),
            )
        )
    return snapshots


class SECEdgarClient:
    """Thin live client. Requires SEC_USER_AGENT in the environment."""

    def __init__(self, timeout_seconds: float = 30.0) -> None:
        self._timeout = timeout_seconds
        self._last_request_time = 0.0
        self._ticker_to_cik: dict[str, int] | None = None

    def _user_agent(self) -> str:
        user_agent = os.environ.get(SEC_USER_AGENT_ENV_VAR, "").strip()
        if not user_agent:
            raise SECEdgarError(
                f"{SEC_USER_AGENT_ENV_VAR} is not set. SEC fair-access policy "
                "requires an identifying User-Agent "
                "(format: 'PersonalAITradingDesk email@domain')."
            )
        return user_agent

    def _get(self, url: str) -> str:
        elapsed = time.monotonic() - self._last_request_time
        if elapsed < MIN_REQUEST_INTERVAL_SECONDS:
            time.sleep(MIN_REQUEST_INTERVAL_SECONDS - elapsed)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": self._user_agent(), "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                body = response.read().decode("utf-8")
        except OSError as e:
            raise SECEdgarError(f"SEC request failed for {url}: {e}") from e
        finally:
            self._last_request_time = time.monotonic()
        return body

    def get_cik(self, symbol: str) -> int:
        """Resolve a canonical symbol to its SEC CIK via company_tickers.json."""
        sec_ticker = SEC_TICKER_OVERRIDES.get(symbol, symbol)
        if self._ticker_to_cik is None:
            raw = self._get(COMPANY_TICKERS_URL)
            try:
                listing = json.loads(raw)
            except json.JSONDecodeError as e:
                raise SECEdgarError(f"Invalid company_tickers.json: {e}") from e
            self._ticker_to_cik = {
                str(entry["ticker"]).upper(): int(entry["cik_str"])
                for entry in listing.values()
            }
        cik = self._ticker_to_cik.get(sec_ticker.upper())
        if cik is None:
            raise SECEdgarError(f"No CIK found for symbol {symbol} ({sec_ticker})")
        return cik

    def fetch_companyfacts(self, symbol: str) -> FundamentalsFetchResult:
        """Fetch and parse companyfacts for one symbol."""
        retrieved_at = datetime.now(timezone.utc)
        cik = self.get_cik(symbol)
        url = COMPANYFACTS_URL.format(cik=cik)
        raw = self._get(url)
        snapshots = parse_companyfacts(symbol, raw, retrieved_at)
        warnings = []
        if not snapshots:
            warnings.append(
                f"companyfacts had no usable 10-K/10-Q periods for {symbol}; "
                "surfacing empty result (no fabrication)."
            )
        return FundamentalsFetchResult(
            symbol=symbol,
            source="sec_edgar",
            retrieved_at=retrieved_at,
            request_urls=[COMPANY_TICKERS_URL, url],
            raw_payloads={"companyfacts": raw},
            snapshots=snapshots,
            warnings=warnings,
        )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/store.py`
  ```
"""DuckDB persistence for fundamentals snapshots + factor-input assembly."""

from __future__ import annotations

from datetime import datetime, timezone

import duckdb

from research_data.factors.quality_fcf import FundamentalInputs
from research_data.fundamentals.models import FundamentalsSnapshot

_CREATE_SNAPSHOTS = """\
CREATE TABLE IF NOT EXISTS fundamentals_snapshots (
    snapshot_id VARCHAR NOT NULL,
    symbol VARCHAR NOT NULL,
    source VARCHAR NOT NULL,
    period_type VARCHAR NOT NULL,
    fiscal_period_end DATE NOT NULL,
    retrieved_at TIMESTAMP NOT NULL,
    raw_payload_hash VARCHAR NOT NULL,
    currency VARCHAR NOT NULL,
    revenue DOUBLE,
    operating_income DOUBLE,
    operating_cash_flow DOUBLE,
    capex DOUBLE,
    total_debt DOUBLE,
    cash_and_equivalents DOUBLE,
    total_equity DOUBLE,
    shares_outstanding DOUBLE,
    PRIMARY KEY (symbol, source, period_type, fiscal_period_end)
);
"""


def _to_db_ts(value: datetime | None) -> datetime | None:
    """Naive-UTC normalization (DuckDB TIMESTAMP converts aware → local)."""
    if value is None or value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)


class FundamentalsStore:
    """Upsert + read API over fundamentals_snapshots."""

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def init_schema(self) -> None:
        self._conn.execute(_CREATE_SNAPSHOTS)

    def upsert_snapshots(self, snapshots: list[FundamentalsSnapshot]) -> int:
        for snapshot in snapshots:
            self._conn.execute(
                """
                INSERT OR REPLACE INTO fundamentals_snapshots (
                    snapshot_id, symbol, source, period_type, fiscal_period_end,
                    retrieved_at, raw_payload_hash, currency,
                    revenue, operating_income, operating_cash_flow, capex,
                    total_debt, cash_and_equivalents, total_equity, shares_outstanding
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    snapshot.snapshot_id,
                    snapshot.symbol,
                    snapshot.source,
                    snapshot.period_type,
                    snapshot.fiscal_period_end,
                    _to_db_ts(snapshot.retrieved_at),
                    snapshot.raw_payload_hash,
                    snapshot.currency,
                    snapshot.revenue,
                    snapshot.operating_income,
                    snapshot.operating_cash_flow,
                    snapshot.capex,
                    snapshot.total_debt,
                    snapshot.cash_and_equivalents,
                    snapshot.total_equity,
                    snapshot.shares_outstanding,
                ],
            )
        return len(snapshots)

    def get_snapshots(
        self,
        symbol: str,
        source: str | None = None,
        period_type: str | None = None,
    ) -> list[FundamentalsSnapshot]:
        conditions = ["symbol = ?"]
        params: list = [symbol]
        if source is not None:
            conditions.append("source = ?")
            params.append(source)
        if period_type is not None:
            conditions.append("period_type = ?")
            params.append(period_type)
        rows = self._conn.execute(
            f"""
            SELECT snapshot_id, symbol, source, period_type, fiscal_period_end,
                   retrieved_at, raw_payload_hash, currency,
                   revenue, operating_income, operating_cash_flow, capex,
                   total_debt, cash_and_equivalents, total_equity, shares_outstanding
            FROM fundamentals_snapshots
            WHERE {' AND '.join(conditions)}
            ORDER BY fiscal_period_end ASC
            """,
            params,
        ).fetchall()
        return [_row_to_snapshot(r) for r in rows]


def _row_to_snapshot(row: tuple) -> FundamentalsSnapshot:
    retrieved_at = row[5]
    if retrieved_at is not None and retrieved_at.tzinfo is None:
        retrieved_at = retrieved_at.replace(tzinfo=timezone.utc)
    return FundamentalsSnapshot(
        snapshot_id=row[0],
        symbol=row[1],
        source=row[2],
        period_type=row[3],
        fiscal_period_end=row[4],
        retrieved_at=retrieved_at,
        raw_payload_hash=row[6],
        currency=row[7],
        revenue=row[8],
        operating_income=row[9],
        operating_cash_flow=row[10],
        capex=row[11],
        total_debt=row[12],
        cash_and_equivalents=row[13],
        total_equity=row[14],
        shares_outstanding=row[15],
    )


def to_factor_inputs(
    symbol: str,
    snapshots: list[FundamentalsSnapshot],
    margin_periods: int = 8,
) -> FundamentalInputs | None:
    """Assemble FactorEngine inputs from stored snapshots.

    Point-in-time fields come from the latest snapshot that carries each field
    (statement coverage varies by source); the operating-margin history comes
    from the trailing quarterly snapshots. Returns None when there are no
    snapshots at all — the factor layer then reports INSUFFICIENT_DATA.
    """
    if not snapshots:
        return None
    ordered = sorted(snapshots, key=lambda s: s.fiscal_period_end)
    latest = ordered[-1]

    def latest_field(name: str) -> float | None:
        for snapshot in reversed(ordered):
            value = getattr(snapshot, name)
            if value is not None:
                return value
        return None

    quarterly = [s for s in ordered if s.period_type == "quarter"]
    margins = [
        m
        for m in (s.operating_margin for s in quarterly[-margin_periods:])
        if m is not None
    ]

    return FundamentalInputs(
        symbol=symbol,
        as_of=latest.fiscal_period_end,
        source=latest.source,
        revenue=latest_field("revenue"),
        operating_cash_flow=latest_field("operating_cash_flow"),
        capex=latest_field("capex"),
        total_debt=latest_field("total_debt"),
        cash_and_equivalents=latest_field("cash_and_equivalents"),
        total_equity=latest_field("total_equity"),
        shares_outstanding=latest_field("shares_outstanding"),
        operating_margins=margins,
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_income.json`
  ```
[
  {"date": "2026-03-28", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q2",
   "revenue": 95000000000, "operatingIncome": 29500000000, "weightedAverageShsOut": 15000000000},
  {"date": "2025-12-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q1",
   "revenue": 124000000000, "operatingIncome": 42500000000, "weightedAverageShsOut": 15100000000},
  {"date": "2025-09-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "FY",
   "revenue": 391000000000, "operatingIncome": 123000000000, "weightedAverageShsOut": 15200000000}
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_balance.json`
  ```
[
  {"date": "2026-03-28", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q2",
   "totalDebt": 98000000000, "cashAndCashEquivalents": 32000000000, "totalStockholdersEquity": 67000000000},
  {"date": "2025-12-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q1",
   "totalDebt": 97000000000, "cashAndCashEquivalents": 30000000000, "totalStockholdersEquity": 66000000000},
  {"date": "2025-09-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "FY",
   "totalDebt": 96000000000, "cashAndCashEquivalents": 29000000000, "totalStockholdersEquity": 65000000000}
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_cashflow.json`
  ```
[
  {"date": "2026-03-28", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q2",
   "operatingCashFlow": 28000000000, "capitalExpenditure": -2900000000},
  {"date": "2025-12-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "Q1",
   "operatingCashFlow": 39000000000, "capitalExpenditure": -3100000000},
  {"date": "2025-09-27", "symbol": "AAPL", "reportedCurrency": "USD", "period": "FY",
   "operatingCashFlow": 118000000000, "capitalExpenditure": -11000000000}
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_companyfacts.json`
  ```
{
  "cik": 320193,
  "entityName": "Apple Inc.",
  "facts": {
    "dei": {
      "EntityCommonStockSharesOutstanding": {
        "units": {
          "shares": [
            {"end": "2026-03-28", "val": 15000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"end": "2025-09-27", "val": 15200000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      }
    },
    "us-gaap": {
      "RevenueFromContractWithCustomerExcludingAssessedTax": {
        "units": {
          "USD": [
            {"start": "2025-12-28", "end": "2026-03-28", "val": 95000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"start": "2024-09-29", "end": "2025-09-27", "val": 391000000000, "form": "10-K", "fp": "FY", "fy": 2025},
            {"start": "2023-10-01", "end": "2024-09-28", "val": 383000000000, "form": "8-K", "fp": "FY", "fy": 2024}
          ]
        }
      },
      "OperatingIncomeLoss": {
        "units": {
          "USD": [
            {"start": "2025-12-28", "end": "2026-03-28", "val": 29500000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"start": "2024-09-29", "end": "2025-09-27", "val": 123000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      },
      "NetCashProvidedByUsedInOperatingActivities": {
        "units": {
          "USD": [
            {"start": "2025-12-28", "end": "2026-03-28", "val": 28000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"start": "2024-09-29", "end": "2025-09-27", "val": 118000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      },
      "PaymentsToAcquirePropertyPlantAndEquipment": {
        "units": {
          "USD": [
            {"start": "2025-12-28", "end": "2026-03-28", "val": 2900000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"start": "2024-09-29", "end": "2025-09-27", "val": 11000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      },
      "LongTermDebt": {
        "units": {
          "USD": [
            {"end": "2026-03-28", "val": 98000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"end": "2025-09-27", "val": 96000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      },
      "CashAndCashEquivalentsAtCarryingValue": {
        "units": {
          "USD": [
            {"end": "2026-03-28", "val": 32000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"end": "2025-09-27", "val": 29000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      },
      "StockholdersEquity": {
        "units": {
          "USD": [
            {"end": "2026-03-28", "val": 67000000000, "form": "10-Q", "fp": "Q2", "fy": 2026},
            {"end": "2025-09-27", "val": 65000000000, "form": "10-K", "fp": "FY", "fy": 2025}
          ]
        }
      }
    }
  }
}

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_fundamentals.py`
  ```
"""Fundamentals path tests: parsing, storage, factor-input assembly, guards.

All offline — live clients are only tested for their fail-closed behavior
when keys/identities are absent.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

import duckdb
import pytest

from research_data.fundamentals import (
    FMPFundamentalsClient,
    FundamentalsSnapshot,
    FundamentalsStore,
    SECEdgarClient,
    parse_companyfacts,
    parse_fmp_statements,
    to_factor_inputs,
)
from research_data.fundamentals.fmp import FMPError
from research_data.fundamentals.sec import SECEdgarError

FIXTURES = Path(__file__).parent / "fixtures" / "fundamentals"
RETRIEVED_AT = datetime(2026, 7, 10, 12, 0, tzinfo=timezone.utc)


@pytest.fixture()
def fmp_snapshots() -> list[FundamentalsSnapshot]:
    return parse_fmp_statements(
        "AAPL",
        (FIXTURES / "AAPL_fmp_income.json").read_text(),
        (FIXTURES / "AAPL_fmp_balance.json").read_text(),
        (FIXTURES / "AAPL_fmp_cashflow.json").read_text(),
        RETRIEVED_AT,
    )


# -- FMP parsing ---------------------------------------------------------------


def test_fmp_parses_all_periods(fmp_snapshots) -> None:
    assert len(fmp_snapshots) == 3
    by_end = {s.fiscal_period_end: s for s in fmp_snapshots}
    annual = by_end[date(2025, 9, 27)]
    assert annual.period_type == "annual"
    assert annual.revenue == 391e9
    assert annual.operating_cash_flow == 118e9
    assert annual.capex == 11e9  # stored as positive magnitude
    q2 = by_end[date(2026, 3, 28)]
    assert q2.period_type == "quarter"
    assert q2.total_debt == 98e9
    assert q2.operating_margin == pytest.approx(29.5 / 95.0)


def test_fmp_snapshots_carry_provenance(fmp_snapshots) -> None:
    for snapshot in fmp_snapshots:
        assert snapshot.source == "fmp"
        assert len(snapshot.raw_payload_hash) == 64
        assert snapshot.retrieved_at == RETRIEVED_AT


def test_fmp_parse_rejects_malformed_json() -> None:
    with pytest.raises(FMPError, match="Invalid JSON"):
        parse_fmp_statements("AAPL", "{not json", "[]", "[]", RETRIEVED_AT)
    with pytest.raises(FMPError, match="shape"):
        parse_fmp_statements("AAPL", '{"a": 1}', "[]", "[]", RETRIEVED_AT)


def test_fmp_empty_payloads_yield_no_snapshots() -> None:
    assert parse_fmp_statements("AAPL", "[]", "[]", "[]", RETRIEVED_AT) == []


def test_fmp_live_client_fails_closed_without_key(monkeypatch) -> None:
    monkeypatch.delenv("FMP_API_KEY", raising=False)
    with pytest.raises(FMPError, match="FMP_API_KEY"):
        FMPFundamentalsClient().fetch_statements("AAPL")


# -- SEC parsing -----------------------------------------------------------------


def test_sec_parses_companyfacts_periods() -> None:
    snapshots = parse_companyfacts(
        "AAPL", (FIXTURES / "AAPL_companyfacts.json").read_text(), RETRIEVED_AT
    )
    by_key = {(s.fiscal_period_end, s.period_type): s for s in snapshots}
    annual = by_key[(date(2025, 9, 27), "annual")]
    assert annual.revenue == 391e9
    assert annual.operating_cash_flow == 118e9
    assert annual.capex == 11e9
    assert annual.total_debt == 96e9
    assert annual.total_equity == 65e9
    quarter = by_key[(date(2026, 3, 28), "quarter")]
    assert quarter.revenue == 95e9
    assert quarter.shares_outstanding == 15e9


def [REDACTED]() -> None:
    snapshots = parse_companyfacts(
        "AAPL", (FIXTURES / "AAPL_companyfacts.json").read_text(), RETRIEVED_AT
    )
    # The 8-K FY2024 revenue entry must not create a period.
    assert not any(s.fiscal_period_end == date(2024, 9, 28) for s in snapshots)


def test_sec_parse_rejects_malformed_json() -> None:
    with pytest.raises(SECEdgarError, match="Invalid"):
        parse_companyfacts("AAPL", "{oops", RETRIEVED_AT)


def test_sec_live_client_fails_closed_without_user_agent(monkeypatch) -> None:
    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    with pytest.raises(SECEdgarError, match="SEC_USER_AGENT"):
        SECEdgarClient().fetch_companyfacts("AAPL")


# -- store ------------------------------------------------------------------------


def test_store_roundtrip_and_idempotent_upsert(fmp_snapshots) -> None:
    conn = duckdb.connect(":memory:")
    store = FundamentalsStore(conn)
    store.init_schema()
    assert store.upsert_snapshots(fmp_snapshots) == 3
    # Second upsert of the same periods replaces, not duplicates.
    store.upsert_snapshots(fmp_snapshots)
    loaded = store.get_snapshots("AAPL", source="fmp")
    assert len(loaded) == 3
    assert loaded[0].fiscal_period_end < loaded[-1].fiscal_period_end
    assert loaded[-1].retrieved_at == RETRIEVED_AT

    quarters = store.get_snapshots("AAPL", period_type="quarter")
    assert len(quarters) == 2


# -- factor-input assembly -----------------------------------------------------------


def test_to_factor_inputs_uses_latest_fields_and_quarterly_margins(fmp_snapshots) -> None:
    inputs = to_factor_inputs("AAPL", fmp_snapshots)
    assert inputs is not None
    assert inputs.as_of == date(2026, 3, 28)
    assert inputs.total_debt == 98e9
    assert inputs.operating_cash_flow == 28e9
    assert inputs.fcf == 28e9 - 2.9e9
    # Margins come from the two quarterly periods only.
    assert len(inputs.operating_margins) == 2


def test_to_factor_inputs_empty_is_none() -> None:
    assert to_factor_inputs("VOO", []) is None


def test_fmp_and_sec_agree_on_shared_fields() -> None:
    """Cross-provider sanity: the two parsers must produce comparable numbers
    for the same underlying periods (fixtures encode the same statements)."""
    fmp = parse_fmp_statements(
        "AAPL",
        (FIXTURES / "AAPL_fmp_income.json").read_text(),
        (FIXTURES / "AAPL_fmp_balance.json").read_text(),
        (FIXTURES / "AAPL_fmp_cashflow.json").read_text(),
        RETRIEVED_AT,
    )
    sec = parse_companyfacts(
        "AAPL", (FIXTURES / "AAPL_companyfacts.json").read_text(), RETRIEVED_AT
    )
    fmp_annual = next(s for s in fmp if s.period_type == "annual")
    sec_annual = next(s for s in sec if s.period_type == "annual")
    assert fmp_annual.revenue == sec_annual.revenue
    assert fmp_annual.operating_cash_flow == sec_annual.operating_cash_flow
    assert fmp_annual.capex == sec_annual.capex

  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_fundamentals.py -q 2>&1 | tail -3`
  ```
.............                                                            [100%]
13 passed in 0.58s
  ```
- `TaskUpdate` — `{"taskId":"4","status":"completed"}`
- `TaskUpdate` — `{"taskId":"5","status":"in_progress","activeForm":"Implementing four-gate harness"}`
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/metrics.py`
  ```
"""Shared return-series types and performance metrics for the gate harness.

Pure Python (statistics.NormalDist covers the distribution math — no scipy).
Every metric here is a plain formula over supplied returns; nothing fetches
data or invents values.
"""

from __future__ import annotations

import math
from datetime import date

from pydantic import BaseModel, Field, model_validator

TRADING_DAYS_PER_YEAR = 252

#: Default one-way transaction cost in basis points (literature-conservative
#: for liquid US large caps / ETFs).
DEFAULT_COST_BPS_PER_SIDE = 5.0


class StrategyReturns(BaseModel):
    """Time-ordered daily strategy returns with turnover for cost accounting.

    ``gross_returns[i]`` is the strategy's return for ``dates[i]``;
    ``turnover[i]`` is the fraction of the portfolio traded that day
    (0.0 = no trade, 1.0 = full rotation). Produced by a spec's Python hook —
    dates must be strictly increasing (time order is a guardrail, not a hint).
    """

    strategy_name: str
    dates: list[date]
    gross_returns: list[float]
    turnover: list[float]

    @model_validator(mode="after")
    def validate_alignment(self) -> "StrategyReturns":
        if not (len(self.dates) == len(self.gross_returns) == len(self.turnover)):
            raise ValueError(
                "dates, gross_returns, and turnover must have equal length"
            )
        for previous, current in zip(self.dates, self.dates[1:]):
            if current <= previous:
                raise ValueError(
                    f"dates must be strictly increasing; {current} follows {previous}"
                )
        for t in self.turnover:
            if t < 0:
                raise ValueError(f"turnover cannot be negative, got {t}")
        return self

    def net_returns(self, cost_bps_per_side: float = DEFAULT_COST_BPS_PER_SIDE) -> list[float]:
        """Gross returns minus linear transaction costs on turnover."""
        cost_rate = cost_bps_per_side / 10_000.0
        return [
            r - t * cost_rate for r, t in zip(self.gross_returns, self.turnover)
        ]

    @property
    def trade_count(self) -> int:
        return sum(1 for t in self.turnover if t > 0)


class PerformanceSummary(BaseModel):
    """Standard honest-reporting block: return, risk, drawdown, activity."""

    periods: int
    total_return: float
    annualized_return: float | None
    sharpe_annualized: float | None
    max_drawdown: float
    trade_count: int | None = None


class GateResult(BaseModel):
    """Outcome of one gate: pass/fail plus every number that drove it."""

    gate: str
    passed: bool
    inputs: dict = Field(default_factory=dict)
    outputs: dict = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)


# -- scalar metrics -------------------------------------------------------------


def total_return(returns: list[float]) -> float:
    compounded = 1.0
    for r in returns:
        compounded *= 1.0 + r
    return compounded - 1.0


def annualized_return(returns: list[float]) -> float | None:
    if not returns:
        return None
    compounded = 1.0 + total_return(returns)
    if compounded <= 0:
        return -1.0  # total loss floor; geometric annualization undefined below 0
    years = len(returns) / TRADING_DAYS_PER_YEAR
    if years <= 0:
        return None
    return compounded ** (1.0 / years) - 1.0


def mean_std(returns: list[float]) -> tuple[float, float]:
    n = len(returns)
    if n < 2:
        return (returns[0] if returns else 0.0, 0.0)
    mean = sum(returns) / n
    variance = sum((r - mean) ** 2 for r in returns) / (n - 1)
    return mean, math.sqrt(variance)


def sharpe_annualized(returns: list[float]) -> float | None:
    """Annualized Sharpe (rf = 0). None when the series has no variance."""
    mean, std = mean_std(returns)
    if std == 0.0:
        return None
    return mean / std * math.sqrt(TRADING_DAYS_PER_YEAR)


def sharpe_per_period(returns: list[float]) -> float | None:
    mean, std = mean_std(returns)
    if std == 0.0:
        return None
    return mean / std


def max_drawdown(returns: list[float]) -> float:
    """Most negative peak-to-trough equity decline (0.0 = never below peak)."""
    equity = 1.0
    peak = 1.0
    worst = 0.0
    for r in returns:
        equity *= 1.0 + r
        peak = max(peak, equity)
        worst = min(worst, equity / peak - 1.0)
    return worst


def skewness(returns: list[float]) -> float:
    """Population skewness g1 = m3 / m2^1.5 (0.0 for degenerate series)."""
    n = len(returns)
    if n < 3:
        return 0.0
    mean = sum(returns) / n
    m2 = sum((r - mean) ** 2 for r in returns) / n
    if m2 == 0:
        return 0.0
    m3 = sum((r - mean) ** 3 for r in returns) / n
    return m3 / m2**1.5


def kurtosis(returns: list[float]) -> float:
    """Population kurtosis g2 = m4 / m2^2 (normal ≈ 3.0; 3.0 for degenerate)."""
    n = len(returns)
    if n < 4:
        return 3.0
    mean = sum(returns) / n
    m2 = sum((r - mean) ** 2 for r in returns) / n
    if m2 == 0:
        return 3.0
    m4 = sum((r - mean) ** 4 for r in returns) / n
    return m4 / m2**2


def percentile(values: list[float], pct: float) -> float:
    """Linear-interpolation percentile (pct in [0, 100]) of a value list."""
    if not values:
        raise ValueError("percentile of empty list")
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (pct / 100.0) * (len(ordered) - 1)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def summarize(returns: list[float], trade_count: int | None = None) -> PerformanceSummary:
    return PerformanceSummary(
        periods=len(returns),
        total_return=total_return(returns),
        annualized_return=annualized_return(returns),
        sharpe_annualized=sharpe_annualized(returns),
        max_drawdown=max_drawdown(returns),
        trade_count=trade_count,
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/oos.py`
  ```
"""Gate 1 — out-of-sample screening.

Time-ordered split (no shuffling — lookahead is a guardrail violation).
The strategy's net-of-cost out-of-sample segment must stand on its own AND
must not collapse relative to in-sample (Pardo-style degradation check).
The same-window benchmark (VOO buy-and-hold) is always reported.

Default pass rule:
    oos_net_sharpe > 0
    AND (in-sample sharpe <= 0 OR oos_sharpe >= 0.5 * in-sample sharpe)
"""

from __future__ import annotations

from dataclasses import dataclass

from research_data.gates.metrics import (
    DEFAULT_COST_BPS_PER_SIDE,
    GateResult,
    StrategyReturns,
    sharpe_annualized,
    summarize,
)


@dataclass(frozen=True)
class OOSParams:
    train_fraction: float = 0.70
    min_oos_sharpe: float = 0.0
    max_degradation: float = 0.50  # OOS must keep ≥ 50% of in-sample Sharpe
    cost_bps_per_side: float = DEFAULT_COST_BPS_PER_SIDE
    min_oos_periods: int = 60  # fewer OOS sessions than this cannot pass


def run_oos_gate(
    strategy: StrategyReturns,
    benchmark_returns: list[float],
    params: OOSParams = OOSParams(),
) -> GateResult:
    """Evaluate the out-of-sample gate. Insufficient data fails closed."""
    net = strategy.net_returns(params.cost_bps_per_side)
    split = int(len(net) * params.train_fraction)
    train, test = net[:split], net[split:]
    inputs = {
        "train_fraction": params.train_fraction,
        "min_oos_sharpe": params.min_oos_sharpe,
        "max_degradation": params.max_degradation,
        "cost_bps_per_side": params.cost_bps_per_side,
        "total_periods": len(net),
        "oos_periods": len(test),
    }

    if len(test) < params.min_oos_periods or len(train) < params.min_oos_periods:
        return GateResult(
            gate="out_of_sample",
            passed=False,
            inputs=inputs,
            outputs={},
            notes=[
                f"Insufficient data: train={len(train)}, oos={len(test)} sessions "
                f"(need >= {params.min_oos_periods} each). Fails closed."
            ],
        )

    is_sharpe = sharpe_annualized(train)
    oos_sharpe = sharpe_annualized(test)
    oos_trades = sum(1 for t in strategy.turnover[split:] if t > 0)
    strategy_summary = summarize(test, trade_count=oos_trades)
    benchmark_summary = summarize(benchmark_returns[split:])

    passed = (
        oos_sharpe is not None
        and oos_sharpe > params.min_oos_sharpe
        and (
            is_sharpe is None
            or is_sharpe <= 0
            or oos_sharpe >= params.max_degradation * is_sharpe
        )
    )

    notes = []
    if oos_sharpe is None:
        notes.append("OOS returns have no variance; Sharpe undefined — fails.")
    if passed and strategy_summary.total_return < benchmark_summary.total_return:
        notes.append(
            "OOS return trails the benchmark buy-and-hold over the same window —"
            " reported for the promotion decision."
        )

    return GateResult(
        gate="out_of_sample",
        passed=bool(passed),
        inputs=inputs,
        outputs={
            "in_sample_sharpe": is_sharpe,
            "oos_sharpe": oos_sharpe,
            "oos_strategy": strategy_summary.model_dump(),
            "oos_benchmark": benchmark_summary.model_dump(),
        },
        notes=notes,
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/monte_carlo.py`
  ```
"""Gate 2 — Monte Carlo bootstrap stress.

Resamples the strategy's net daily returns with replacement (seeded, fully
reproducible) and checks the left tail: if the 5th percentile of resampled
annualized returns is below the floor (default 0.0), the "edge" doesn't
survive path luck and the gate fails. Drawdown tail is reported alongside.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from research_data.gates.metrics import (
    DEFAULT_COST_BPS_PER_SIDE,
    GateResult,
    StrategyReturns,
    annualized_return,
    max_drawdown,
    percentile,
)


@dataclass(frozen=True)
class MonteCarloParams:
    n_simulations: int = 1000
    tail_percentile: float = 5.0
    min_tail_annualized_return: float = 0.0
    seed: int = 42
    cost_bps_per_side: float = DEFAULT_COST_BPS_PER_SIDE
    min_periods: int = 120


def run_monte_carlo_gate(
    strategy: StrategyReturns,
    params: MonteCarloParams = MonteCarloParams(),
) -> GateResult:
    """Bootstrap the net return series; the tail must clear the floor."""
    net = strategy.net_returns(params.cost_bps_per_side)
    inputs = {
        "n_simulations": params.n_simulations,
        "tail_percentile": params.tail_percentile,
        "min_tail_annualized_return": params.min_tail_annualized_return,
        "seed": params.seed,
        "cost_bps_per_side": params.cost_bps_per_side,
        "periods": len(net),
    }

    if len(net) < params.min_periods:
        return GateResult(
            gate="monte_carlo",
            passed=False,
            inputs=inputs,
            outputs={},
            notes=[
                f"Insufficient data: {len(net)} sessions "
                f"(need >= {params.min_periods}). Fails closed."
            ],
        )

    rng = random.Random(params.seed)
    n = len(net)
    sim_annualized: list[float] = []
    sim_drawdowns: list[float] = []
    for _ in range(params.n_simulations):
        path = [net[rng.randrange(n)] for _ in range(n)]
        ann = annualized_return(path)
        sim_annualized.append(ann if ann is not None else -1.0)
        sim_drawdowns.append(max_drawdown(path))

    tail_return = percentile(sim_annualized, params.tail_percentile)
    tail_drawdown = percentile(sim_drawdowns, params.tail_percentile)
    loss_probability = sum(1 for a in sim_annualized if a < 0) / len(sim_annualized)

    passed = tail_return > params.min_tail_annualized_return

    return GateResult(
        gate="monte_carlo",
        passed=passed,
        inputs=inputs,
        outputs={
            "tail_annualized_return": tail_return,
            "median_annualized_return": percentile(sim_annualized, 50.0),
            "tail_max_drawdown": tail_drawdown,
            "probability_negative_year": loss_probability,
        },
        notes=(
            []
            if passed
            else [
                f"{params.tail_percentile:.0f}th percentile annualized return "
                f"{tail_return:.4f} does not clear the floor "
                f"{params.min_tail_annualized_return:.4f}."
            ]
        ),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/walk_forward.py`
  ```
"""Gate 3 — walk-forward consistency (Pardo 1992).

Rolling train/test windows advance through time; each test segment is
evaluated net of costs. Parameters are fixed to literature defaults — this
harness does NOT re-optimize per window (our universe is too small for
honest per-window optimization; the gate checks *consistency*, which is the
part of walk-forward that survives at this scale — recorded in the result).

Default pass rule: >= 60% of test windows have positive net return AND the
pooled out-of-window Sharpe is positive.
"""

from __future__ import annotations

from dataclasses import dataclass

from research_data.gates.metrics import (
    DEFAULT_COST_BPS_PER_SIDE,
    GateResult,
    StrategyReturns,
    sharpe_annualized,
    summarize,
    total_return,
)


@dataclass(frozen=True)
class WalkForwardParams:
    train_sessions: int = 504  # ~2 years
    test_sessions: int = 126  # ~6 months
    step_sessions: int = 126
    min_fraction_positive: float = 0.60
    min_pooled_sharpe: float = 0.0
    cost_bps_per_side: float = DEFAULT_COST_BPS_PER_SIDE
    min_windows: int = 3


def run_walk_forward_gate(
    strategy: StrategyReturns,
    benchmark_returns: list[float],
    params: WalkForwardParams = WalkForwardParams(),
) -> GateResult:
    """Roll train/test windows through the net return series."""
    net = strategy.net_returns(params.cost_bps_per_side)
    inputs = {
        "train_sessions": params.train_sessions,
        "test_sessions": params.test_sessions,
        "step_sessions": params.step_sessions,
        "min_fraction_positive": params.min_fraction_positive,
        "min_pooled_sharpe": params.min_pooled_sharpe,
        "cost_bps_per_side": params.cost_bps_per_side,
        "periods": len(net),
        "parameter_note": "parameters fixed to literature defaults; not re-optimized per window",
    }

    windows: list[dict] = []
    pooled: list[float] = []
    start = 0
    while start + params.train_sessions + params.test_sessions <= len(net):
        test_start = start + params.train_sessions
        test_end = test_start + params.test_sessions
        segment = net[test_start:test_end]
        benchmark_segment = benchmark_returns[test_start:test_end]
        windows.append(
            {
                "test_start_index": test_start,
                "test_return": total_return(segment),
                "test_sharpe": sharpe_annualized(segment),
                "benchmark_return": total_return(benchmark_segment),
            }
        )
        pooled.extend(segment)
        start += params.step_sessions

    if len(windows) < params.min_windows:
        return GateResult(
            gate="walk_forward",
            passed=False,
            inputs=inputs,
            outputs={"windows": windows},
            notes=[
                f"Insufficient data: only {len(windows)} walk-forward windows "
                f"(need >= {params.min_windows}). Fails closed."
            ],
        )

    positive = sum(1 for w in windows if w["test_return"] > 0)
    fraction_positive = positive / len(windows)
    pooled_sharpe = sharpe_annualized(pooled)
    pooled_summary = summarize(pooled)

    passed = (
        fraction_positive >= params.min_fraction_positive
        and pooled_sharpe is not None
        and pooled_sharpe > params.min_pooled_sharpe
    )

    return GateResult(
        gate="walk_forward",
        passed=bool(passed),
        inputs=inputs,
        outputs={
            "n_windows": len(windows),
            "fraction_positive": fraction_positive,
            "pooled_sharpe": pooled_sharpe,
            "pooled_summary": pooled_summary.model_dump(),
            "windows": windows,
        },
        notes=(
            []
            if passed
            else [
                f"fraction_positive={fraction_positive:.2f} "
                f"(need >= {params.min_fraction_positive}), "
                f"pooled_sharpe={pooled_sharpe}."
            ]
        ),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/deflated_sharpe.py`
  ```
"""Gate 4 — deflated Sharpe ratio (Bailey & López de Prado 2014, SSRN 2460551).

The best backtest among N tried configurations has an inflated Sharpe. The
DSR asks: given how many trials were run (from brain test-run records) and
the non-normality of the returns, what is the probability that the true
Sharpe exceeds the expected maximum Sharpe of N skill-less trials?

    DSR = Phi( ((SR_hat - SR0) * sqrt(T - 1)) /
               sqrt(1 - g3*SR_hat + ((g4 - 1)/4) * SR_hat^2) )

with SR_hat the per-period Sharpe, T the number of returns, g3 skewness,
g4 (non-excess) kurtosis, and SR0 the expected max trial Sharpe:

    SR0 = sqrt(V[SR_trials]) * ((1-γ) * Z^-1(1 - 1/N) + γ * Z^-1(1 - 1/(N·e)))

γ = Euler-Mascheroni. With one trial (or no trial-Sharpe variance) SR0 = 0
and the DSR reduces to the probabilistic Sharpe ratio against 0.

Default pass rule: DSR >= 0.95.
"""

from __future__ import annotations

import math
import statistics as stats_mod
from dataclasses import dataclass

from research_data.gates.metrics import (
    DEFAULT_COST_BPS_PER_SIDE,
    GateResult,
    StrategyReturns,
    kurtosis,
    mean_std,
    skewness,
)

EULER_MASCHERONI = 0.5772156649015329
_NORMAL = stats_mod.NormalDist()


def expected_max_sharpe(n_trials: int, variance_trial_sharpes: float) -> float:
    """E[max SR] across n skill-less trials with the given SR variance."""
    if n_trials <= 1 or variance_trial_sharpes <= 0:
        return 0.0
    z1 = _NORMAL.inv_cdf(1.0 - 1.0 / n_trials)
    z2 = _NORMAL.inv_cdf(1.0 - 1.0 / (n_trials * math.e))
    return math.sqrt(variance_trial_sharpes) * (
        (1.0 - EULER_MASCHERONI) * z1 + EULER_MASCHERONI * z2
    )


def deflated_sharpe_probability(
    returns: list[float],
    n_trials: int,
    trial_sharpes: list[float] | None = None,
) -> tuple[float | None, dict]:
    """DSR probability and its intermediate values (for the audit trail).

    ``trial_sharpes`` are per-period Sharpes of other tried configurations
    (from brain test runs); their variance drives the deflation term. Without
    at least two, SR0 falls back to 0 (pure PSR — no selection-bias credit is
    *added*, none is forgiven).
    """
    t = len(returns)
    if t < 3:
        return None, {"reason": f"only {t} returns; need >= 3"}
    mean, std = mean_std(returns)
    if std == 0:
        return None, {"reason": "returns have no variance; Sharpe undefined"}
    sr_hat = mean / std
    g3 = skewness(returns)
    g4 = kurtosis(returns)

    variance_trials = 0.0
    if trial_sharpes is not None and len(trial_sharpes) >= 2:
        variance_trials = stats_mod.pvariance(trial_sharpes)
    sr0 = expected_max_sharpe(n_trials, variance_trials)

    denominator_sq = 1.0 - g3 * sr_hat + ((g4 - 1.0) / 4.0) * sr_hat**2
    if denominator_sq <= 0:
        return None, {
            "reason": "non-normality adjustment is degenerate for this series",
            "sr_hat": sr_hat,
            "skewness": g3,
            "kurtosis": g4,
        }
    z = (sr_hat - sr0) * math.sqrt(t - 1) / math.sqrt(denominator_sq)
    probability = _NORMAL.cdf(z)
    return probability, {
        "sr_hat_per_period": sr_hat,
        "sr0_expected_max": sr0,
        "n_trials": n_trials,
        "variance_trial_sharpes": variance_trials,
        "skewness": g3,
        "kurtosis": g4,
        "t_periods": t,
        "z_statistic": z,
    }


@dataclass(frozen=True)
class DeflatedSharpeParams:
    min_probability: float = 0.95
    cost_bps_per_side: float = DEFAULT_COST_BPS_PER_SIDE


def run_deflated_sharpe_gate(
    strategy: StrategyReturns,
    n_trials: int,
    trial_sharpes: list[float] | None = None,
    params: DeflatedSharpeParams = DeflatedSharpeParams(),
) -> GateResult:
    """The DSR probability must clear ``min_probability`` (default 0.95)."""
    net = strategy.net_returns(params.cost_bps_per_side)
    probability, details = deflated_sharpe_probability(net, n_trials, trial_sharpes)
    inputs = {
        "min_probability": params.min_probability,
        "cost_bps_per_side": params.cost_bps_per_side,
        "n_trials": n_trials,
        "n_trial_sharpes_provided": len(trial_sharpes or []),
    }
    if probability is None:
        return GateResult(
            gate="deflated_sharpe",
            passed=False,
            inputs=inputs,
            outputs=details,
            notes=[f"DSR undefined: {details.get('reason', 'unknown')}. Fails closed."],
        )
    passed = probability >= params.min_probability
    return GateResult(
        gate="deflated_sharpe",
        passed=passed,
        inputs=inputs,
        outputs={"deflated_sharpe_probability": probability, **details},
        notes=(
            []
            if passed
            else [
                f"DSR probability {probability:.4f} < required {params.min_probability}."
            ]
        ),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/harness.py`
  ```
"""Four-gate harness: fixed order, short-circuit on failure, recorded runs.

Order is non-negotiable: out-of-sample → Monte Carlo → walk-forward →
deflated Sharpe. A failed gate stops the batch (later gates are not run and
therefore cannot pass); every executed gate is written to the brain as a
TestRunRecord so failures are auditable, never silent.

Demo-paper eligibility additionally requires a recorded human promotion
decision — see ``research_data.brain.loop``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date

from research_data.brain.models import GateName, TestRunRecord
from research_data.brain.store import BrainStore
from research_data.gates.deflated_sharpe import (
    DeflatedSharpeParams,
    run_deflated_sharpe_gate,
)
from research_data.gates.metrics import (
    TRADING_DAYS_PER_YEAR,
    GateResult,
    StrategyReturns,
)
from research_data.gates.monte_carlo import MonteCarloParams, run_monte_carlo_gate
from research_data.gates.oos import OOSParams, run_oos_gate
from research_data.gates.walk_forward import WalkForwardParams, run_walk_forward_gate


@dataclass(frozen=True)
class GateHarnessConfig:
    oos: OOSParams = field(default_factory=OOSParams)
    monte_carlo: MonteCarloParams = field(default_factory=MonteCarloParams)
    walk_forward: WalkForwardParams = field(default_factory=WalkForwardParams)
    deflated_sharpe: DeflatedSharpeParams = field(default_factory=DeflatedSharpeParams)


@dataclass(frozen=True)
class GateBatchOutcome:
    results: list[GateResult]
    test_run_ids: list[str]
    all_passed: bool
    n_trials: int


class GateHarness:
    """Runs the four gates against a strategy return series."""

    def __init__(self, config: GateHarnessConfig | None = None) -> None:
        self._config = config or GateHarnessConfig()

    def run(
        self,
        strategy: StrategyReturns,
        benchmark_returns: list[float],
        n_trials: int,
        trial_sharpes: list[float] | None = None,
    ) -> list[GateResult]:
        """Run gates in fixed order; stop at the first failure."""
        if len(benchmark_returns) != len(strategy.gross_returns):
            raise ValueError(
                "benchmark_returns must align 1:1 with the strategy series "
                f"({len(benchmark_returns)} vs {len(strategy.gross_returns)})"
            )
        results: list[GateResult] = []

        result = run_oos_gate(strategy, benchmark_returns, self._config.oos)
        results.append(result)
        if not result.passed:
            return results

        result = run_monte_carlo_gate(strategy, self._config.monte_carlo)
        results.append(result)
        if not result.passed:
            return results

        result = run_walk_forward_gate(
            strategy, benchmark_returns, self._config.walk_forward
        )
        results.append(result)
        if not result.passed:
            return results

        results.append(
            run_deflated_sharpe_gate(
                strategy, n_trials, trial_sharpes, self._config.deflated_sharpe
            )
        )
        return results

    def run_and_record(
        self,
        store: BrainStore,
        spec_id: str,
        strategy: StrategyReturns,
        benchmark_returns: list[float],
        as_of: date,
    ) -> GateBatchOutcome:
        """Run the gates and persist every executed gate as a TestRunRecord.

        The deflated-Sharpe trial count comes from the brain itself: every
        spec that ever reached testing counts as one selection-bias trial
        (including this one), and prior recorded OOS Sharpes provide the
        trial-Sharpe variance.
        """
        already_tested = bool(store.list_test_runs(spec_id))
        n_trials = store.count_tested_specs() + (0 if already_tested else 1)
        trial_sharpes = collect_trial_sharpes(store)

        results = self.run(strategy, benchmark_returns, n_trials, trial_sharpes)

        run_ids: list[str] = []
        for index, result in enumerate(results):
            record = TestRunRecord(
                spec_id=spec_id,
                gate_name=GateName(result.gate),
                sequence_index=index,
                inputs=result.inputs,
                outputs={**result.outputs, "notes": result.notes},
                passed=result.passed,
                as_of=as_of,
            )
            run_ids.append(store.record_test_run(record))

        all_passed = len(results) == 4 and all(r.passed for r in results)
        return GateBatchOutcome(
            results=results,
            test_run_ids=run_ids,
            all_passed=all_passed,
            n_trials=n_trials,
        )


def collect_trial_sharpes(store: BrainStore) -> list[float]:
    """Per-period OOS Sharpes from all recorded out-of-sample gate runs.

    These feed the deflation term: the more configurations were tried (and
    the more their Sharpes varied), the higher the bar for the current one.
    """
    sharpes: list[float] = []
    for run in store.list_runs_for_gate(GateName.OUT_OF_SAMPLE):
        value = run.outputs.get("oos_sharpe")
        if isinstance(value, (int, float)):
            sharpes.append(float(value) / math.sqrt(TRADING_DAYS_PER_YEAR))
    return sharpes

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/gates/__init__.py`
  ```
"""Four-gate promotion harness (order fixed, all literature defaults).

1. out-of-sample screening   (Pardo degradation heuristic)
2. Monte Carlo bootstrap     (seeded, reproducible tail check)
3. walk-forward consistency  (rolling windows, no per-window re-optimization)
4. deflated Sharpe ratio     (Bailey & López de Prado; trial count from brain)

Nothing is demo-paper eligible without all four passing in order, a recorded
TestRunRecord per gate, and a human promotion decision.
"""

from research_data.gates.deflated_sharpe import (
    DeflatedSharpeParams,
    deflated_sharpe_probability,
    expected_max_sharpe,
    run_deflated_sharpe_gate,
)
from research_data.gates.harness import (
    GateBatchOutcome,
    GateHarness,
    GateHarnessConfig,
    collect_trial_sharpes,
)
from research_data.gates.metrics import (
    DEFAULT_COST_BPS_PER_SIDE,
    GateResult,
    PerformanceSummary,
    StrategyReturns,
    summarize,
)
from research_data.gates.monte_carlo import MonteCarloParams, run_monte_carlo_gate
from research_data.gates.oos import OOSParams, run_oos_gate
from research_data.gates.walk_forward import WalkForwardParams, run_walk_forward_gate

__all__ = [
    "DEFAULT_COST_BPS_PER_SIDE",
    "DeflatedSharpeParams",
    "GateBatchOutcome",
    "GateHarness",
    "GateHarnessConfig",
    "GateResult",
    "MonteCarloParams",
    "OOSParams",
    "PerformanceSummary",
    "StrategyReturns",
    "WalkForwardParams",
    "collect_trial_sharpes",
    "deflated_sharpe_probability",
    "expected_max_sharpe",
    "run_deflated_sharpe_gate",
    "run_monte_carlo_gate",
    "run_oos_gate",
    "run_walk_forward_gate",
    "summarize",
]

  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py`
  ```diff
  -     def count_tested_specs(self) -> int:
  +     def list_runs_for_gate(self, gate_name: GateName) -> list[TestRunRecord]:
        """All recorded runs of one gate across every spec (trial history)."""
        rows = self._conn.execute(
            "SELECT * FROM brain_test_runs WHERE gate_name = ? "
            "ORDER BY created_at, test_run_id",
            [gate_name.value],
        ).fetchall()
        return [_row_to_test_run(r) for r in rows]

    def count_tested_specs(self) -> int:
  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_gates.py`
  ```
"""Tests for the four-gate harness and its statistics."""

from __future__ import annotations

import random
from datetime import date

import duckdb
import pytest

from research_data.brain import (
    BrainStore,
    StrategySpec,
    gate_sequence_passes,
    is_demo_eligible,
    latest_gate_batch,
    record_gate_outcome_decision,
)
from research_data.gates import (
    GateHarness,
    MonteCarloParams,
    OOSParams,
    StrategyReturns,
    WalkForwardParams,
    deflated_sharpe_probability,
    expected_max_sharpe,
    run_deflated_sharpe_gate,
    run_monte_carlo_gate,
    run_oos_gate,
    run_walk_forward_gate,
)
from research_data.gates.metrics import (
    max_drawdown,
    percentile,
    sharpe_annualized,
    total_return,
)

from tests.synthetic import trading_days

AS_OF = date(2026, 6, 30)
SESSIONS = 1200  # enough for 504-train/126-test walk-forward windows


def make_strategy(
    name: str, mean: float, std: float, seed: int = 1, sessions: int = SESSIONS
) -> StrategyReturns:
    rng = random.Random(f"{name}:{seed}")
    dates = trading_days(AS_OF, sessions)
    returns = [rng.gauss(mean, std) for _ in range(sessions)]
    # Monthly rebalance: 20% of the book turns over every 21st session.
    turnover = [0.2 if i % 21 == 0 else 0.0 for i in range(sessions)]
    return StrategyReturns(
        strategy_name=name, dates=dates, gross_returns=returns, turnover=turnover
    )


def benchmark_like(seed: int = 99, sessions: int = SESSIONS) -> list[float]:
    rng = random.Random(f"benchmark:{seed}")
    return [rng.gauss(0.0004, 0.008) for _ in range(sessions)]


EDGE = make_strategy("edge", mean=0.0011, std=0.008)
NOISE = make_strategy("noise", mean=0.0, std=0.010)
LOSER = make_strategy("loser", mean=-0.0012, std=0.010)
BENCHMARK = benchmark_like()


# -- metrics --------------------------------------------------------------------


def test_total_return_and_drawdown_known_values() -> None:
    assert total_return([0.10, -0.10]) == pytest.approx(-0.01)
    assert max_drawdown([0.10, -0.50, 0.20]) == pytest.approx(-0.50)
    assert max_drawdown([0.01, 0.02]) == 0.0


def test_sharpe_none_for_constant_series() -> None:
    assert sharpe_annualized([0.01] * 100) is None


def test_percentile_interpolates() -> None:
    values = [1.0, 2.0, 3.0, 4.0]
    assert percentile(values, 0) == 1.0
    assert percentile(values, 100) == 4.0
    assert percentile(values, 50) == pytest.approx(2.5)


def test_strategy_returns_validation() -> None:
    days = trading_days(AS_OF, 3)
    with pytest.raises(ValueError, match="equal length"):
        StrategyReturns(
            strategy_name="x", dates=days, gross_returns=[0.0], turnover=[0.0, 0.0, 0.0]
        )
    with pytest.raises(ValueError, match="strictly increasing"):
        StrategyReturns(
            strategy_name="x",
            dates=[days[0], days[0], days[2]],
            gross_returns=[0.0, 0.0, 0.0],
            turnover=[0.0, 0.0, 0.0],
        )
    with pytest.raises(ValueError, match="turnover"):
        StrategyReturns(
            strategy_name="x", dates=days, gross_returns=[0.0] * 3, turnover=[0.0, -0.1, 0.0]
        )


def test_net_returns_subtract_costs_on_turnover_days() -> None:
    days = trading_days(AS_OF, 2)
    strategy = StrategyReturns(
        strategy_name="x", dates=days, gross_returns=[0.01, 0.01], turnover=[1.0, 0.0]
    )
    net = strategy.net_returns(cost_bps_per_side=10.0)
    assert net[0] == pytest.approx(0.01 - 0.001)
    assert net[1] == pytest.approx(0.01)
    assert strategy.trade_count == 1


# -- gate 1: out-of-sample ---------------------------------------------------------


def test_oos_gate_passes_real_edge_and_reports_benchmark() -> None:
    result = run_oos_gate(EDGE, BENCHMARK)
    assert result.passed is True
    assert result.outputs["oos_sharpe"] > 0
    assert "oos_benchmark" in result.outputs
    assert result.outputs["oos_strategy"]["trade_count"] > 0


def test_oos_gate_fails_loser() -> None:
    assert run_oos_gate(LOSER, BENCHMARK).passed is False


def test_oos_gate_fails_closed_on_short_series() -> None:
    short = make_strategy("short", mean=0.002, std=0.005, sessions=100)
    result = run_oos_gate(short, benchmark_like(sessions=100))
    assert result.passed is False
    assert "Insufficient data" in result.notes[0]


# -- gate 2: Monte Carlo -------------------------------------------------------------


def test_monte_carlo_is_deterministic_for_a_seed() -> None:
    a = run_monte_carlo_gate(EDGE, MonteCarloParams(n_simulations=200, seed=7))
    b = run_monte_carlo_gate(EDGE, MonteCarloParams(n_simulations=200, seed=7))
    assert a.outputs == b.outputs


def test_monte_carlo_passes_edge_fails_noise() -> None:
    assert run_monte_carlo_gate(EDGE).passed is True
    assert run_monte_carlo_gate(NOISE).passed is False


def test_monte_carlo_reports_tails() -> None:
    outputs = run_monte_carlo_gate(EDGE).outputs
    assert outputs["tail_annualized_return"] < outputs["median_annualized_return"]
    assert outputs["tail_max_drawdown"] <= 0
    assert 0.0 <= outputs["probability_negative_year"] <= 1.0


# -- gate 3: walk-forward --------------------------------------------------------------


def test_walk_forward_passes_edge_fails_loser() -> None:
    edge_result = run_walk_forward_gate(EDGE, BENCHMARK)
    assert edge_result.passed is True
    assert edge_result.outputs["n_windows"] >= 3
    assert run_walk_forward_gate(LOSER, BENCHMARK).passed is False


def test_walk_forward_fails_closed_without_enough_windows() -> None:
    short = make_strategy("shortwf", mean=0.002, std=0.005, sessions=700)
    result = run_walk_forward_gate(
        short, benchmark_like(sessions=700), WalkForwardParams()
    )
    assert result.passed is False
    assert "Insufficient data" in result.notes[0]


# -- gate 4: deflated Sharpe --------------------------------------------------------------


def test_expected_max_sharpe_grows_with_trials() -> None:
    assert expected_max_sharpe(1, 0.01) == 0.0
    few = expected_max_sharpe(5, 0.01)
    many = expected_max_sharpe(100, 0.01)
    assert 0 < few < many


def test_dsr_single_trial_reduces_to_psr() -> None:
    probability, details = deflated_sharpe_probability(
        EDGE.net_returns(), n_trials=1
    )
    assert probability is not None and probability > 0.95
    assert details["sr0_expected_max"] == 0.0


def test_dsr_deflates_with_many_varied_trials() -> None:
    net = EDGE.net_returns()
    baseline, _ = deflated_sharpe_probability(net, n_trials=1)
    trial_sharpes = [-0.1, 0.0, 0.05, 0.1, 0.15, -0.05]
    deflated, details = deflated_sharpe_probability(
        net, n_trials=500, trial_sharpes=trial_sharpes
    )
    assert deflated is not None and deflated < baseline
    assert details["sr0_expected_max"] > 0


def test_dsr_gate_fails_closed_on_degenerate_series() -> None:
    days = trading_days(AS_OF, 10)
    flat = StrategyReturns(
        strategy_name="flat",
        dates=days,
        gross_returns=[0.0] * 10,
        turnover=[0.0] * 10,
    )
    result = run_deflated_sharpe_gate(flat, n_trials=1)
    assert result.passed is False
    assert "Fails closed" in result.notes[0]


# -- harness ----------------------------------------------------------------------------


@pytest.fixture()
def store() -> BrainStore:
    conn = duckdb.connect(":memory:")
    s = BrainStore(conn)
    s.init_schema()
    return s


def approved_spec(store: BrainStore, name: str) -> StrategySpec:
    spec = StrategySpec(name=name, description="d", proposed_by="ai:analyst")
    store.propose_spec(spec)
    return store.approve_spec(spec.spec_id, approved_by="Anant")


def test_harness_short_circuits_on_first_failure() -> None:
    results = GateHarness().run(LOSER, BENCHMARK, n_trials=1)
    assert len(results) == 1
    assert results[0].gate == "out_of_sample"
    assert results[0].passed is False


def test_harness_runs_all_four_in_order_for_edge() -> None:
    results = GateHarness().run(EDGE, BENCHMARK, n_trials=1)
    assert [r.gate for r in results] == [
        "out_of_sample",
        "monte_carlo",
        "walk_forward",
        "deflated_sharpe",
    ]
    assert all(r.passed for r in results)


def test_harness_rejects_misaligned_benchmark() -> None:
    with pytest.raises(ValueError, match="align"):
        GateHarness().run(EDGE, BENCHMARK[:-5], n_trials=1)


def test_run_and_record_full_promotion_path(store: BrainStore) -> None:
    spec = approved_spec(store, "edge_strategy")
    outcome = GateHarness().run_and_record(
        store, spec.spec_id, EDGE, BENCHMARK, as_of=AS_OF
    )
    assert outcome.all_passed is True
    assert outcome.n_trials == 1
    assert len(outcome.test_run_ids) == 4

    batch = latest_gate_batch(store, spec.spec_id)
    assert gate_sequence_passes(batch) is True

    record_gate_outcome_decision(
        store, spec.spec_id, decided_by="Anant", rationale="all four gates passed"
    )
    assert is_demo_eligible(store, spec.spec_id) is True


def test_run_and_record_failure_is_persisted_not_silent(store: BrainStore) -> None:
    spec = approved_spec(store, "loser_strategy")
    outcome = GateHarness().run_and_record(
        store, spec.spec_id, LOSER, BENCHMARK, as_of=AS_OF
    )
    assert outcome.all_passed is False
    runs = store.list_test_runs(spec.spec_id)
    assert len(runs) == 1  # only the failed OOS gate ran — and it is on record
    assert runs[0].passed is False
    assert is_demo_eligible(store, spec.spec_id) is False


def test_trial_count_grows_across_specs(store: BrainStore) -> None:
    first = approved_spec(store, "first")
    GateHarness().run_and_record(store, first.spec_id, EDGE, BENCHMARK, as_of=AS_OF)
    second = approved_spec(store, "second")
    outcome = GateHarness().run_and_record(
        store, second.spec_id, NOISE, BENCHMARK, as_of=AS_OF
    )
    assert outcome.n_trials == 2  # the brain remembers the first trial

  ```
- `Bash`:
  ```bash
source .venv/bin/activate && python - <<'EOF'
p = 'src/research_data/brain/__init__.py'
s = open(p).read()
s = s.replace("from research_data.brain.loop import (\n    BrainLoopError,\n    gate_sequence_passes,",
              "from research_data.brain.loop import (\n    BrainLoopError,\n    gate_sequence_passes,\n    latest_gate_batch,")
s = s.replace('    "gate_sequence_passes",', '    "gate_sequence_passes",\n    "latest_gate_batch",')
open(p, 'w').write(s)
print("ok")
EOF
python -m pytest tests/test_gates.py -q 2>&1 | tail -5
  ```
  ```
ok
.......................                                                  [100%]
23 passed in 7.41s
  ```
- `TaskUpdate` — `{"taskId":"5","status":"completed"}`
- `TaskUpdate` — `{"taskId":"6","status":"in_progress","activeForm":"Implementing paper-test contracts"}`
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/__init__.py`
  ```
"""Paper-test contracts: pre-approved theses, timed auto-entry, journal.

The paper book is the real test of knowledge. Rules baked in:

- Nothing enters the book without a pre-approved thesis (human approval),
  and auto-entry happens only inside the thesis's approved time window.
- Two modes share one schema: REPLAY (accelerated historical verification,
  journal written as-if-time-passed) and LIVE (real-calendar paper book with
  review jump-ahead hooks).
- Every exit journal entry must record what VOO returned over the same
  holding period — alpha honesty is not optional.
- Action vocabulary is fixed: WATCH | HOLD | ACCUMULATE | REDUCE | AVOID |
  INSUFFICIENT_DATA. No execution language anywhere.
"""

from research_data.paper.models import (
    ActionLabel,
    JournalEntry,
    PaperFill,
    PaperMode,
    PositionEffect,
    ReplayRun,
    Thesis,
    ThesisStatus,
)
from research_data.paper.store import PaperStore, PaperStoreError
from research_data.paper.engine import PaperEngine, PaperEngineError

__all__ = [
    "ActionLabel",
    "JournalEntry",
    "PaperEngine",
    "PaperEngineError",
    "PaperFill",
    "PaperMode",
    "PaperStore",
    "PaperStoreError",
    "PositionEffect",
    "ReplayRun",
    "Thesis",
    "ThesisStatus",
]

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/models.py`
  ```
"""Typed paper-trading records. No execution language, full provenance."""

from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _new_id() -> str:
    return str(uuid.uuid4())


class ActionLabel(str, Enum):
    """The only action vocabulary allowed anywhere in this system."""

    WATCH = "WATCH"
    HOLD = "HOLD"
    ACCUMULATE = "ACCUMULATE"
    REDUCE = "REDUCE"
    AVOID = "AVOID"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ThesisStatus(str, Enum):
    PROPOSED = "proposed"
    APPROVED = "approved"
    EXECUTED = "executed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"


class PaperMode(str, Enum):
    REPLAY = "replay"  # accelerated historical verification
    LIVE = "live"  # real-calendar paper book


class PositionEffect(str, Enum):
    """Paper fills open or close exposure — no directional trade words."""

    OPEN = "open"
    CLOSE = "close"


class Thesis(BaseModel):
    """A pre-approval contract: why, what, when, and how much.

    Timed auto-entry is only legal inside [entry_window_start,
    entry_window_end] and only after a human approves. ``invalidation_conditions``
    state, up front, what would prove the thesis wrong.
    """

    thesis_id: str = Field(default_factory=_new_id)
    spec_id: str | None = None  # strategy spec this thesis came from, if any
    symbol: str
    action: ActionLabel
    thesis_text: str
    invalidation_conditions: list[str] = Field(default_factory=list)
    size_fraction: float = Field(gt=0.0, le=1.0)
    entry_window_start: date
    entry_window_end: date
    entry_rule: dict[str, Any] = Field(
        default_factory=lambda: {"type": "first_session_close"}
    )
    status: ThesisStatus = ThesisStatus.PROPOSED
    proposed_by: str = "human"
    approved_by: str | None = None
    approved_at: datetime | None = None
    next_review_date: date | None = None
    created_at: datetime = Field(default_factory=_utcnow)

    @field_validator("thesis_text")
    @classmethod
    def validate_thesis_text(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("thesis_text must be non-empty — no entry without a thesis")
        return v

    @model_validator(mode="after")
    def validate_window(self) -> "Thesis":
        if self.entry_window_end < self.entry_window_start:
            raise ValueError(
                f"entry_window_end ({self.entry_window_end}) is before "
                f"entry_window_start ({self.entry_window_start})"
            )
        return self


class PaperFill(BaseModel):
    """One paper execution, priced from a stored OHLCV row (provenance kept)."""

    fill_id: str = Field(default_factory=_new_id)
    thesis_id: str
    symbol: str
    position_effect: PositionEffect
    quantity: float = Field(gt=0.0)
    fill_date: date
    fill_price: float = Field(gt=0.0)
    price_source: str  # provider of the daily_ohlcv row used
    price_payload_hash: str  # raw_payload_hash of that row
    mode: PaperMode
    created_at: datetime = Field(default_factory=_utcnow)


class JournalEntry(BaseModel):
    """Journal record; in REPLAY mode ``as_of`` is the simulated date.

    Exits must carry ``voo_return_same_period`` — without the benchmark
    comparison it is impossible to say whether the strategy earned anything
    beyond market exposure.
    """

    entry_id: str = Field(default_factory=_new_id)
    mode: PaperMode
    entry_type: str  # "thesis" | "entry" | "exit" | "review" | "lesson"
    as_of: date
    body: str
    spec_id: str | None = None
    thesis_id: str | None = None
    symbol: str | None = None
    realized_return: float | None = None
    voo_return_same_period: float | None = None
    next_review_date: date | None = None
    created_at: datetime = Field(default_factory=_utcnow)

    @model_validator(mode="after")
    def validate_exit_requires_benchmark(self) -> "JournalEntry":
        if self.entry_type == "exit" and self.voo_return_same_period is None:
            raise ValueError(
                "exit journal entries require voo_return_same_period "
                "(benchmark-relative honesty is mandatory)"
            )
        return self


class ReplayRun(BaseModel):
    """One accelerated historical replay over a date range."""

    replay_id: str = Field(default_factory=_new_id)
    spec_id: str | None = None
    start_date: date
    end_date: date
    status: str = "created"  # "created" | "completed"
    description: str = ""
    created_at: datetime = Field(default_factory=_utcnow)

    @model_validator(mode="after")
    def validate_range(self) -> "ReplayRun":
        if self.end_date <= self.start_date:
            raise ValueError("replay end_date must be after start_date")
        return self

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/store.py`
  ```
"""DuckDB persistence for theses, fills, journal entries, and replay runs."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import duckdb

from research_data.brain.models import validate_human_identity
from research_data.paper.models import (
    ActionLabel,
    JournalEntry,
    PaperFill,
    PaperMode,
    PositionEffect,
    ReplayRun,
    Thesis,
    ThesisStatus,
)


class PaperStoreError(Exception):
    """Raised on illegal paper-store operations."""


def _to_db_ts(value: datetime | None) -> datetime | None:
    """Naive-UTC normalization (DuckDB TIMESTAMP converts aware → local)."""
    if value is None or value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)


def _as_utc(value: datetime | None) -> datetime | None:
    if value is not None and value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


_CREATE_THESES = """\
CREATE TABLE IF NOT EXISTS paper_theses (
    thesis_id VARCHAR PRIMARY KEY,
    spec_id VARCHAR,
    symbol VARCHAR NOT NULL,
    action VARCHAR NOT NULL,
    thesis_text VARCHAR NOT NULL,
    invalidation_conditions JSON NOT NULL,
    size_fraction DOUBLE NOT NULL,
    entry_window_start DATE NOT NULL,
    entry_window_end DATE NOT NULL,
    entry_rule JSON NOT NULL,
    status VARCHAR NOT NULL,
    proposed_by VARCHAR NOT NULL,
    approved_by VARCHAR,
    approved_at TIMESTAMP,
    next_review_date DATE,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_FILLS = """\
CREATE TABLE IF NOT EXISTS paper_fills (
    fill_id VARCHAR PRIMARY KEY,
    thesis_id VARCHAR NOT NULL,
    symbol VARCHAR NOT NULL,
    position_effect VARCHAR NOT NULL,
    quantity DOUBLE NOT NULL,
    fill_date DATE NOT NULL,
    fill_price DOUBLE NOT NULL,
    price_source VARCHAR NOT NULL,
    price_payload_hash VARCHAR NOT NULL,
    mode VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_JOURNAL = """\
CREATE TABLE IF NOT EXISTS paper_journal_entries (
    entry_id VARCHAR PRIMARY KEY,
    mode VARCHAR NOT NULL,
    entry_type VARCHAR NOT NULL,
    as_of DATE NOT NULL,
    body VARCHAR NOT NULL,
    spec_id VARCHAR,
    thesis_id VARCHAR,
    symbol VARCHAR,
    realized_return DOUBLE,
    voo_return_same_period DOUBLE,
    next_review_date DATE,
    created_at TIMESTAMP NOT NULL
);
"""

_CREATE_REPLAY_RUNS = """\
CREATE TABLE IF NOT EXISTS paper_replay_runs (
    replay_id VARCHAR PRIMARY KEY,
    spec_id VARCHAR,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
"""


class PaperStore:
    """Typed persistence API for the paper book."""

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def init_schema(self) -> None:
        for stmt in (_CREATE_THESES, _CREATE_FILLS, _CREATE_JOURNAL, _CREATE_REPLAY_RUNS):
            self._conn.execute(stmt)

    # -- theses ------------------------------------------------------------

    def propose_thesis(self, thesis: Thesis) -> str:
        if thesis.status != ThesisStatus.PROPOSED:
            raise PaperStoreError("new theses must enter as PROPOSED")
        self._conn.execute(
            """
            INSERT INTO paper_theses (
                thesis_id, spec_id, symbol, action, thesis_text,
                invalidation_conditions, size_fraction,
                entry_window_start, entry_window_end, entry_rule,
                status, proposed_by, approved_by, approved_at,
                next_review_date, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                thesis.thesis_id,
                thesis.spec_id,
                thesis.symbol,
                thesis.action.value,
                thesis.thesis_text,
                json.dumps(thesis.invalidation_conditions),
                thesis.size_fraction,
                thesis.entry_window_start,
                thesis.entry_window_end,
                json.dumps(thesis.entry_rule),
                thesis.status.value,
                thesis.proposed_by,
                thesis.approved_by,
                _to_db_ts(thesis.approved_at),
                thesis.next_review_date,
                _to_db_ts(thesis.created_at),
            ],
        )
        return thesis.thesis_id

    def get_thesis(self, thesis_id: str) -> Thesis:
        row = self._conn.execute(
            "SELECT * FROM paper_theses WHERE thesis_id = ?", [thesis_id]
        ).fetchone()
        if row is None:
            raise PaperStoreError(f"Unknown thesis_id: {thesis_id}")
        return _row_to_thesis(row)

    def list_theses(self, status: ThesisStatus | None = None) -> list[Thesis]:
        if status is None:
            rows = self._conn.execute(
                "SELECT * FROM paper_theses ORDER BY created_at, thesis_id"
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM paper_theses WHERE status = ? ORDER BY created_at, thesis_id",
                [status.value],
            ).fetchall()
        return [_row_to_thesis(r) for r in rows]

    def approve_thesis(
        self, thesis_id: str, approved_by: str, approved_at: datetime | None = None
    ) -> Thesis:
        """Human gate: PROPOSED → APPROVED. Auto-entry is illegal before this."""
        approved_by = validate_human_identity(approved_by, "approved_by")
        thesis = self.get_thesis(thesis_id)
        if thesis.status != ThesisStatus.PROPOSED:
            raise PaperStoreError(
                f"Only PROPOSED theses can be approved; {thesis_id} is {thesis.status.value}"
            )
        approved_at = approved_at or datetime.now(timezone.utc)
        self._conn.execute(
            "UPDATE paper_theses SET status = ?, approved_by = ?, approved_at = ? "
            "WHERE thesis_id = ?",
            [ThesisStatus.APPROVED.value, approved_by, _to_db_ts(approved_at), thesis_id],
        )
        return self.get_thesis(thesis_id)

    def set_thesis_status(self, thesis_id: str, status: ThesisStatus) -> None:
        self.get_thesis(thesis_id)
        self._conn.execute(
            "UPDATE paper_theses SET status = ? WHERE thesis_id = ?",
            [status.value, thesis_id],
        )

    # -- fills --------------------------------------------------------------

    def record_fill(self, fill: PaperFill) -> str:
        """Persist a fill. OPEN fills demand an approved thesis and a fill
        date inside the approved entry window — the timed-entry contract."""
        thesis = self.get_thesis(fill.thesis_id)
        if fill.position_effect == PositionEffect.OPEN:
            if thesis.status not in (ThesisStatus.APPROVED, ThesisStatus.EXECUTED):
                raise PaperStoreError(
                    f"OPEN fill requires an APPROVED thesis; {fill.thesis_id} "
                    f"is {thesis.status.value}"
                )
            if not (thesis.entry_window_start <= fill.fill_date <= thesis.entry_window_end):
                raise PaperStoreError(
                    f"OPEN fill date {fill.fill_date} is outside the approved "
                    f"entry window [{thesis.entry_window_start}, {thesis.entry_window_end}]"
                )
        self._conn.execute(
            """
            INSERT INTO paper_fills (
                fill_id, thesis_id, symbol, position_effect, quantity,
                fill_date, fill_price, price_source, price_payload_hash,
                mode, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                fill.fill_id,
                fill.thesis_id,
                fill.symbol,
                fill.position_effect.value,
                fill.quantity,
                fill.fill_date,
                fill.fill_price,
                fill.price_source,
                fill.price_payload_hash,
                fill.mode.value,
                _to_db_ts(fill.created_at),
            ],
        )
        return fill.fill_id

    def list_fills(self, thesis_id: str | None = None) -> list[PaperFill]:
        if thesis_id is None:
            rows = self._conn.execute(
                "SELECT * FROM paper_fills ORDER BY fill_date, created_at, fill_id"
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM paper_fills WHERE thesis_id = ? "
                "ORDER BY fill_date, created_at, fill_id",
                [thesis_id],
            ).fetchall()
        return [_row_to_fill(r) for r in rows]

    # -- journal -------------------------------------------------------------

    def add_journal_entry(self, entry: JournalEntry) -> str:
        self._conn.execute(
            """
            INSERT INTO paper_journal_entries (
                entry_id, mode, entry_type, as_of, body, spec_id, thesis_id,
                symbol, realized_return, voo_return_same_period,
                next_review_date, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                entry.entry_id,
                entry.mode.value,
                entry.entry_type,
                entry.as_of,
                entry.body,
                entry.spec_id,
                entry.thesis_id,
                entry.symbol,
                entry.realized_return,
                entry.voo_return_same_period,
                entry.next_review_date,
                _to_db_ts(entry.created_at),
            ],
        )
        return entry.entry_id

    def list_journal_entries(
        self,
        mode: PaperMode | None = None,
        thesis_id: str | None = None,
    ) -> list[JournalEntry]:
        conditions: list[str] = []
        params: list = []
        if mode is not None:
            conditions.append("mode = ?")
            params.append(mode.value)
        if thesis_id is not None:
            conditions.append("thesis_id = ?")
            params.append(thesis_id)
        where = f"WHERE {' AND '.join(conditions)}" if conditions else ""
        rows = self._conn.execute(
            f"SELECT * FROM paper_journal_entries {where} "
            "ORDER BY as_of, created_at, entry_id",
            params,
        ).fetchall()
        return [_row_to_journal(r) for r in rows]

    def pending_reviews(self, as_of: date) -> list[JournalEntry]:
        """Review jump-ahead hook: journal entries whose review date is due."""
        rows = self._conn.execute(
            "SELECT * FROM paper_journal_entries "
            "WHERE next_review_date IS NOT NULL AND next_review_date <= ? "
            "ORDER BY next_review_date, entry_id",
            [as_of],
        ).fetchall()
        return [_row_to_journal(r) for r in rows]

    # -- replay runs ------------------------------------------------------------

    def create_replay_run(self, run: ReplayRun) -> str:
        self._conn.execute(
            """
            INSERT INTO paper_replay_runs (
                replay_id, spec_id, start_date, end_date, status, description, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            [
                run.replay_id,
                run.spec_id,
                run.start_date,
                run.end_date,
                run.status,
                run.description,
                _to_db_ts(run.created_at),
            ],
        )
        return run.replay_id

    def complete_replay_run(self, replay_id: str) -> None:
        self._conn.execute(
            "UPDATE paper_replay_runs SET status = 'completed' WHERE replay_id = ?",
            [replay_id],
        )

    def get_replay_run(self, replay_id: str) -> ReplayRun:
        row = self._conn.execute(
            "SELECT * FROM paper_replay_runs WHERE replay_id = ?", [replay_id]
        ).fetchone()
        if row is None:
            raise PaperStoreError(f"Unknown replay_id: {replay_id}")
        return ReplayRun(
            replay_id=row[0],
            spec_id=row[1],
            start_date=row[2],
            end_date=row[3],
            status=row[4],
            description=row[5],
            created_at=_as_utc(row[6]),
        )


# ---------------------------------------------------------------------------
# Row converters
# ---------------------------------------------------------------------------


def _loads(value):
    return json.loads(value) if isinstance(value, str) else value


def _row_to_thesis(row: tuple) -> Thesis:
    return Thesis(
        thesis_id=row[0],
        spec_id=row[1],
        symbol=row[2],
        action=ActionLabel(row[3]),
        thesis_text=row[4],
        invalidation_conditions=_loads(row[5]),
        size_fraction=row[6],
        entry_window_start=row[7],
        entry_window_end=row[8],
        entry_rule=_loads(row[9]),
        status=ThesisStatus(row[10]),
        proposed_by=row[11],
        approved_by=row[12],
        approved_at=_as_utc(row[13]),
        next_review_date=row[14],
        created_at=_as_utc(row[15]),
    )


def _row_to_fill(row: tuple) -> PaperFill:
    return PaperFill(
        fill_id=row[0],
        thesis_id=row[1],
        symbol=row[2],
        position_effect=PositionEffect(row[3]),
        quantity=row[4],
        fill_date=row[5],
        fill_price=row[6],
        price_source=row[7],
        price_payload_hash=row[8],
        mode=PaperMode(row[9]),
        created_at=_as_utc(row[10]),
    )


def _row_to_journal(row: tuple) -> JournalEntry:
    return JournalEntry(
        entry_id=row[0],
        mode=PaperMode(row[1]),
        entry_type=row[2],
        as_of=row[3],
        body=row[4],
        spec_id=row[5],
        thesis_id=row[6],
        symbol=row[7],
        realized_return=row[8],
        voo_return_same_period=row[9],
        next_review_date=row[10],
        created_at=_as_utc(row[11]),
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/engine.py`
  ```
"""PaperEngine — timed auto-entry and accelerated historical replay.

Timed auto-entry contract: inside an approved thesis's entry window the
engine has full power to enter the paper book (that is the point of the
test window); outside it, or without human approval, it has none.

Replay contract: the engine walks a historical range using stored prices
only, fills entries when windows open, closes them at range end, and writes
the journal *as of the simulated dates* — verification on past markets, not
cinema playback. Every exit records the same-period VOO return.

Only ACCUMULATE theses auto-enter (they are the only thesis kind that opens
paper exposure). WATCH/HOLD/REDUCE/AVOID/INSUFFICIENT_DATA theses are
journaled decisions, not entries.
"""

from __future__ import annotations

from datetime import date

from research_data.models import OHLCVRecord
from research_data.paper.models import (
    ActionLabel,
    JournalEntry,
    PaperFill,
    PaperMode,
    PositionEffect,
    ReplayRun,
    Thesis,
    ThesisStatus,
)
from research_data.paper.store import PaperStore
from research_data.read_api import PriceReadAPI

#: Paper book notional per full-size thesis (size_fraction scales this).
DEFAULT_BOOK_NOTIONAL = 100_000.0


class PaperEngineError(Exception):
    """Raised when the paper engine cannot honor a contract."""


class PaperEngine:
    """Executes approved theses against stored prices. Deterministic."""

    def __init__(
        self,
        store: PaperStore,
        price_api: PriceReadAPI,
        benchmark_symbol: str = "VOO",
        book_notional: float = DEFAULT_BOOK_NOTIONAL,
        price_source: str | None = None,
    ) -> None:
        self._store = store
        self._price_api = price_api
        self._benchmark_symbol = benchmark_symbol
        self._book_notional = book_notional
        self._price_source = price_source

    # -- timed auto-entry ---------------------------------------------------

    def execute_timed_entries(self, as_of: date, mode: PaperMode) -> list[PaperFill]:
        """Enter every approved, unfilled ACCUMULATE thesis whose window has
        opened by ``as_of``, at the first usable session close in the window.

        Uses only stored usable prices; a thesis whose window has no usable
        session yet is skipped (tried again next call), and one whose window
        fully passed without data expires — it never back-fills an entry.
        """
        fills: list[PaperFill] = []
        for thesis in self._store.list_theses(status=ThesisStatus.APPROVED):
            if thesis.action != ActionLabel.ACCUMULATE:
                continue
            if thesis.entry_window_start > as_of:
                continue  # window not open yet
            if self._store.list_fills(thesis.thesis_id):
                continue  # already entered

            window_end = min(thesis.entry_window_end, as_of)
            records = self._price_records(
                thesis.symbol, thesis.entry_window_start, window_end
            )
            if not records:
                if thesis.entry_window_end < as_of:
                    self._store.set_thesis_status(thesis.thesis_id, ThesisStatus.EXPIRED)
                    self._store.add_journal_entry(
                        JournalEntry(
                            mode=mode,
                            entry_type="review",
                            as_of=as_of,
                            body=(
                                f"Thesis expired unfilled: no usable {thesis.symbol} "
                                "session inside the approved entry window. "
                                "No entry was fabricated."
                            ),
                            thesis_id=thesis.thesis_id,
                            spec_id=thesis.spec_id,
                            symbol=thesis.symbol,
                        )
                    )
                continue

            first = records[0]
            price = first.adjusted_close or first.close
            quantity = (self._book_notional * thesis.size_fraction) / price
            fill = PaperFill(
                thesis_id=thesis.thesis_id,
                symbol=thesis.symbol,
                position_effect=PositionEffect.OPEN,
                quantity=quantity,
                fill_date=first.trading_date,
                fill_price=price,
                price_source=first.source,
                price_payload_hash=first.raw_payload_hash,
                mode=mode,
            )
            self._store.record_fill(fill)
            self._store.set_thesis_status(thesis.thesis_id, ThesisStatus.EXECUTED)
            self._store.add_journal_entry(
                JournalEntry(
                    mode=mode,
                    entry_type="entry",
                    as_of=first.trading_date,
                    body=(
                        f"Timed auto-entry for pre-approved thesis: opened "
                        f"{quantity:.4f} units of {thesis.symbol} at "
                        f"{price:.4f} ({first.source}). Window "
                        f"[{thesis.entry_window_start} → {thesis.entry_window_end}]."
                    ),
                    thesis_id=thesis.thesis_id,
                    spec_id=thesis.spec_id,
                    symbol=thesis.symbol,
                    next_review_date=thesis.next_review_date,
                )
            )
            fills.append(fill)
        return fills

    # -- accelerated historical replay -----------------------------------------

    def run_replay(self, replay: ReplayRun) -> list[JournalEntry]:
        """Walk the replay range, enter windows as they open, close at range
        end, and write the journal as-if-time-passed.

        Returns the journal entries written by this replay (in as-of order).
        """
        self._store.create_replay_run(replay)
        written: list[JournalEntry] = []

        self.execute_timed_entries(replay.end_date, PaperMode.REPLAY)

        # Close every position this replay opened, at the last usable session
        # in range, and compare against the benchmark over the same holding
        # period. Positions with no usable exit price stay open and are
        # flagged — never valued at an invented price.
        for thesis in self._store.list_theses(status=ThesisStatus.EXECUTED):
            open_fills = [
                f
                for f in self._store.list_fills(thesis.thesis_id)
                if f.mode == PaperMode.REPLAY
                and f.position_effect == PositionEffect.OPEN
            ]
            closed = {
                f.thesis_id
                for f in self._store.list_fills(thesis.thesis_id)
                if f.position_effect == PositionEffect.CLOSE
            }
            for fill in open_fills:
                if fill.thesis_id in closed:
                    continue
                exit_records = self._price_records(
                    fill.symbol, fill.fill_date, replay.end_date
                )
                if not exit_records or exit_records[-1].trading_date <= fill.fill_date:
                    written.append(
                        self._journal(
                            JournalEntry(
                                mode=PaperMode.REPLAY,
                                entry_type="review",
                                as_of=replay.end_date,
                                body=(
                                    f"Replay ended with {fill.symbol} position still "
                                    "open: no usable exit session after entry. "
                                    "Position not marked at a fabricated price."
                                ),
                                thesis_id=fill.thesis_id,
                                spec_id=thesis.spec_id,
                                symbol=fill.symbol,
                            )
                        )
                    )
                    continue
                last = exit_records[-1]
                exit_price = last.adjusted_close or last.close
                realized = exit_price / fill.fill_price - 1.0
                voo_return = self._benchmark_return(fill.fill_date, last.trading_date)
                self._store.record_fill(
                    PaperFill(
                        thesis_id=fill.thesis_id,
                        symbol=fill.symbol,
                        position_effect=PositionEffect.CLOSE,
                        quantity=fill.quantity,
                        fill_date=last.trading_date,
                        fill_price=exit_price,
                        price_source=last.source,
                        price_payload_hash=last.raw_payload_hash,
                        mode=PaperMode.REPLAY,
                    )
                )
                body = (
                    f"Replay exit: closed {fill.symbol} at {exit_price:.4f} "
                    f"(entered {fill.fill_price:.4f} on {fill.fill_date}). "
                    f"Realized {realized:+.4%}"
                )
                if voo_return is not None:
                    body += f"; {self._benchmark_symbol} same period {voo_return:+.4%}."
                else:
                    body += (
                        f"; {self._benchmark_symbol} same-period return unavailable "
                        "in stored data."
                    )
                written.append(
                    self._journal(
                        JournalEntry(
                            mode=PaperMode.REPLAY,
                            entry_type="exit",
                            as_of=last.trading_date,
                            body=body,
                            thesis_id=fill.thesis_id,
                            spec_id=thesis.spec_id,
                            symbol=fill.symbol,
                            realized_return=realized,
                            # Exits require the benchmark figure; when it is
                            # genuinely unavailable we record 0-information
                            # honestly as None → model forbids that, so we
                            # fall back to flagging via a review entry above.
                            voo_return_same_period=(
                                voo_return if voo_return is not None else float("nan")
                            ),
                        )
                    )
                )

        self._store.complete_replay_run(replay.replay_id)
        return written

    # -- helpers -------------------------------------------------------------------

    def _journal(self, entry: JournalEntry) -> JournalEntry:
        self._store.add_journal_entry(entry)
        return entry

    def _price_records(self, symbol: str, start: date, end: date) -> list[OHLCVRecord]:
        if end < start:
            return []
        return self._price_api.get_price_frame(
            symbols=[symbol],
            start=start,
            end=end,
            source=self._price_source,
            require_usable=True,
        )

    def _benchmark_return(self, start: date, end: date) -> float | None:
        records = self._price_records(self._benchmark_symbol, start, end)
        if len(records) < 2:
            return None
        first = records[0].adjusted_close or records[0].close
        last = records[-1].adjusted_close or records[-1].close
        if first <= 0:
            return None
        return last / first - 1.0

  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/paper/engine.py`
  ```diff
  -                 body = (
                    f"Replay exit: closed {fill.symbol} at {exit_price:.4f} "
                    f"(entered {fill.fill_price:.4f} on {fill.fill_date}). "
                    f"Realized {realized:+.4%}"
                )
                if voo_return is not None:
                    body += f"; {self._benchmark_symbol} same period {voo_return:+.4%}."
                else:
                    body += (
                        f"; {self._benchmark_symbol} same-period return unavailable "
                        "in stored data."
                    )
                written.append(
                    self._journal(
                        JournalEntry(
                            mode=PaperMode.REPLAY,
                            entry_type="exit",
                            as_of=last.trading_date,
                            body=body,
                            thesis_id=fill.thesis_id,
                            spec_id=thesis.spec_id,
                            symbol=fill.symbol,
                            realized_return=realized,
                            # Exits require the benchmark figure; when it is
                            # genuinely unavailable we record 0-information
                            # honestly as None → model forbids that, so we
                            # fall back to flagging via a review entry above.
                            voo_return_same_period=(
                                voo_return if voo_return is not None else float("nan")
                            ),
                        )
                    )
                )
  +                 base_body = (
                    f"Replay exit: closed {fill.symbol} at {exit_price:.4f} "
                    f"(entered {fill.fill_price:.4f} on {fill.fill_date}). "
                    f"Realized {realized:+.4%}"
                )
                if voo_return is not None:
                    written.append(
                        self._journal(
                            JournalEntry(
                                mode=PaperMode.REPLAY,
                                entry_type="exit",
                                as_of=last.trading_date,
                                body=base_body
                                + f"; {self._benchmark_symbol} same period {voo_return:+.4%}.",
                                thesis_id=fill.thesis_id,
                                spec_id=thesis.spec_id,
                                symbol=fill.symbol,
                                realized_return=realized,
                                voo_return_same_period=voo_return,
                            )
                        )
                    )
                else:
                    # An "exit" entry requires the benchmark figure. When VOO
                    # data is genuinely missing we say so in a review entry —
                    # we do not invent a benchmark number.
                    written.append(
                        self._journal(
                            JournalEntry(
                                mode=PaperMode.REPLAY,
                                entry_type="review",
                                as_of=last.trading_date,
                                body=base_body
                                + f"; {self._benchmark_symbol} same-period return "
                                "unavailable in stored data — benchmark comparison "
                                "missing, flagged for follow-up.",
                                thesis_id=fill.thesis_id,
                                spec_id=thesis.spec_id,
                                symbol=fill.symbol,
                                realized_return=realized,
                            )
                        )
                    )
  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_paper.py`
  ```
"""Paper-test contract tests: thesis gate, timed entry, replay journal."""

from __future__ import annotations

import json
from datetime import date, timedelta

import duckdb
import pytest

from research_data.paper import (
    ActionLabel,
    JournalEntry,
    PaperEngine,
    PaperFill,
    PaperMode,
    PaperStore,
    PaperStoreError,
    PositionEffect,
    ReplayRun,
    Thesis,
    ThesisStatus,
)
from research_data.read_api import PriceReadAPI
from research_data.storage import batch_insert_ohlcv, init_db

from tests.synthetic import make_price_records, trading_days

AS_OF = date(2026, 6, 30)
SESSIONS = 130
DATES = trading_days(AS_OF, SESSIONS)  # ~2026-01 → 2026-06


@pytest.fixture()
def env():
    conn = duckdb.connect(":memory:")
    init_db(conn)
    records = make_price_records(
        "AAPL", end=AS_OF, sessions=SESSIONS, base_price=200.0,
        daily_drift=0.001, daily_vol=0.01,
    )
    records += make_price_records(
        "VOO", end=AS_OF, sessions=SESSIONS, base_price=450.0,
        daily_drift=0.0004, daily_vol=0.007, asset_type="etf", exchange="NYSE",
    )
    batch_insert_ohlcv(conn, records)
    store = PaperStore(conn)
    store.init_schema()
    engine = PaperEngine(store, PriceReadAPI(conn))
    return store, engine


def make_thesis(**overrides) -> Thesis:
    defaults = dict(
        symbol="AAPL",
        action=ActionLabel.ACCUMULATE,
        thesis_text="Quality composite rank 2/14 with momentum rank 12/14; "
        "entry sized small pending next filing.",
        invalidation_conditions=["Operating margin deteriorates in next filing."],
        size_fraction=0.10,
        entry_window_start=DATES[10],
        entry_window_end=DATES[20],
        next_review_date=DATES[40],
    )
    defaults.update(overrides)
    return Thesis(**defaults)


# -- model validation -----------------------------------------------------------


def test_thesis_requires_text_and_valid_window() -> None:
    with pytest.raises(ValueError, match="thesis_text"):
        make_thesis(thesis_text="   ")
    with pytest.raises(ValueError, match="entry_window_end"):
        make_thesis(entry_window_start=DATES[20], entry_window_end=DATES[10])
    with pytest.raises(ValueError):
        make_thesis(size_fraction=0.0)
    with pytest.raises(ValueError):
        make_thesis(size_fraction=1.5)


def test_exit_journal_requires_benchmark_return() -> None:
    with pytest.raises(ValueError, match="voo_return_same_period"):
        JournalEntry(
            mode=PaperMode.LIVE,
            entry_type="exit",
            as_of=AS_OF,
            body="closed position",
            realized_return=0.05,
        )


# -- thesis lifecycle -------------------------------------------------------------


def test_thesis_approval_human_gate(env) -> None:
    store, _ = env
    thesis = make_thesis()
    store.propose_thesis(thesis)
    with pytest.raises(ValueError):
        store.approve_thesis(thesis.thesis_id, approved_by="agent")
    approved = store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    assert approved.status == ThesisStatus.APPROVED
    with pytest.raises(PaperStoreError, match="PROPOSED"):
        store.approve_thesis(thesis.thesis_id, approved_by="Anant")


def test_open_fill_requires_approval_and_window(env) -> None:
    store, _ = env
    thesis = make_thesis()
    store.propose_thesis(thesis)

    fill = PaperFill(
        thesis_id=thesis.thesis_id,
        symbol="AAPL",
        position_effect=PositionEffect.OPEN,
        quantity=10.0,
        fill_date=DATES[12],
        fill_price=200.0,
        price_source="synthetic_fixture",
        price_payload_hash="h",
        mode=PaperMode.LIVE,
    )
    with pytest.raises(PaperStoreError, match="APPROVED"):
        store.record_fill(fill)

    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    outside = fill.model_copy(update={"fill_date": DATES[30], "fill_id": "f2"})
    with pytest.raises(PaperStoreError, match="entry window"):
        store.record_fill(outside)


# -- timed auto-entry ---------------------------------------------------------------


def test_timed_entry_fills_first_session_in_window(env) -> None:
    store, engine = env
    thesis = make_thesis()
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")

    fills = engine.execute_timed_entries(AS_OF, PaperMode.LIVE)
    assert len(fills) == 1
    fill = fills[0]
    assert fill.fill_date == DATES[10]  # first session of the window
    assert fill.position_effect == PositionEffect.OPEN
    assert fill.price_source == "synthetic_fixture"
    assert fill.quantity * fill.fill_price == pytest.approx(100_000 * 0.10)
    assert store.get_thesis(thesis.thesis_id).status == ThesisStatus.EXECUTED

    journal = store.list_journal_entries(thesis_id=thesis.thesis_id)
    assert len(journal) == 1
    assert journal[0].entry_type == "entry"
    assert journal[0].as_of == DATES[10]

    # Idempotent: a second sweep must not double-enter.
    assert engine.execute_timed_entries(AS_OF, PaperMode.LIVE) == []


def test_no_entry_before_window_opens(env) -> None:
    store, engine = env
    thesis = make_thesis(
        entry_window_start=AS_OF + timedelta(days=5),
        entry_window_end=AS_OF + timedelta(days=15),
        next_review_date=None,
    )
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    assert engine.execute_timed_entries(AS_OF, PaperMode.LIVE) == []
    assert store.get_thesis(thesis.thesis_id).status == ThesisStatus.APPROVED


def test_non_accumulate_theses_never_auto_enter(env) -> None:
    store, engine = env
    thesis = make_thesis(action=ActionLabel.WATCH)
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    assert engine.execute_timed_entries(AS_OF, PaperMode.LIVE) == []


def test_window_without_data_expires_honestly(env) -> None:
    store, engine = env
    # JPM has no stored prices at all.
    thesis = make_thesis(symbol="JPM")
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    assert engine.execute_timed_entries(AS_OF, PaperMode.LIVE) == []
    assert store.get_thesis(thesis.thesis_id).status == ThesisStatus.EXPIRED
    journal = store.list_journal_entries(thesis_id=thesis.thesis_id)
    assert len(journal) == 1
    assert "No entry was fabricated" in journal[0].body


# -- replay -------------------------------------------------------------------------


def test_replay_writes_journal_as_if_time_passed(env) -> None:
    store, engine = env
    thesis = make_thesis()
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")

    replay = ReplayRun(
        spec_id=None,
        start_date=DATES[0],
        end_date=AS_OF,
        description="verification replay over H1 2026",
    )
    written = engine.run_replay(replay)

    fills = store.list_fills(thesis.thesis_id)
    assert [f.position_effect for f in fills] == [PositionEffect.OPEN, PositionEffect.CLOSE]
    open_fill, close_fill = fills
    assert close_fill.fill_date == DATES[-1]

    exits = [e for e in written if e.entry_type == "exit"]
    assert len(exits) == 1
    exit_entry = exits[0]
    # Journal-as-if-time-passed: as_of is the simulated exit session.
    assert exit_entry.as_of == DATES[-1]
    assert exit_entry.realized_return == pytest.approx(
        close_fill.fill_price / open_fill.fill_price - 1.0
    )
    assert exit_entry.voo_return_same_period is not None

    assert store.get_replay_run(replay.replay_id).status == "completed"


def test_pending_reviews_jump_ahead_hook(env) -> None:
    store, engine = env
    thesis = make_thesis()
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    engine.execute_timed_entries(AS_OF, PaperMode.LIVE)

    due = store.pending_reviews(DATES[40])
    assert len(due) == 1
    assert due[0].thesis_id == thesis.thesis_id
    assert store.pending_reviews(DATES[39]) == []


# -- guardrails -----------------------------------------------------------------------


def test_paper_records_contain_no_execution_language(env) -> None:
    store, engine = env
    thesis = make_thesis()
    store.propose_thesis(thesis)
    store.approve_thesis(thesis.thesis_id, approved_by="Anant")
    engine.run_replay(
        ReplayRun(start_date=DATES[0], end_date=AS_OF, description="sweep")
    )
    for entry in store.list_journal_entries():
        text = json.dumps(entry.model_dump(mode="json")).lower()
        for forbidden in ('"buy"', '"sell"', "guaranteed", "risk-free"):
            assert forbidden not in text
    for fill in store.list_fills():
        assert fill.position_effect in (PositionEffect.OPEN, PositionEffect.CLOSE)


def test_action_vocabulary_is_closed() -> None:
    assert {a.value for a in ActionLabel} == {
        "WATCH", "HOLD", "ACCUMULATE", "REDUCE", "AVOID", "INSUFFICIENT_DATA",
    }

  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_paper.py -q 2>&1 | tail -6`
  ```
claude-opus-4-8[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_paper.py -q 2>&1 | tail -6`
  ```
claude-opus-4-8[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/src/research_data/kronos_reserved.py`
  ```
"""Kronos foundation model — RESERVED architecture only. No inference.

Kronos (Tsinghua, arXiv 2508.02739, AAAI 2026 — not Amazon Chronos) is a
K-line foundation model that MAY later become one evidence input. This
module reserves the contract it must satisfy; it deliberately imports no
model code and downloads nothing.

Admission gates (both mandatory, per the Kronos deep-dive note 2026-06-25):

1. Input quality must be USABLE — PARTIAL/STALE/worse data is never fed to a
   forecaster; the pipeline surfaces INSUFFICIENT_DATA instead.
2. Validated RankIC on THIS universe must be >= 0.03. Until a validation
   pass produces that number, no Kronos output may appear in evidence, and
   nothing Kronos says may influence promote/demote decisions.

A forecast without ``model_rankic_on_universe`` populated is unrepresentable
by design: untested model predictions cannot surface.
"""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, Field, model_validator

from research_data.models import QualityStatus

#: Below this validated RankIC the model adds no signal on our universe.
KRONOS_RANKIC_MIN = 0.03

#: Kronos evidence may only ever be built from USABLE-quality inputs.
KRONOS_REQUIRED_QUALITY = QualityStatus.USABLE

#: Path-spread width (10th–90th pct of forecast return) above which the
#: evidence must carry an explicit high-uncertainty flag.
KRONOS_WIDE_SPREAD_THRESHOLD = 0.05


class KronosForecastEvidence(BaseModel):
    """The ONLY shape Kronos output may take if it is ever integrated.

    A price-path forecast becomes an evidence *claim* with provenance and a
    validated-skill figure — never an action label, never a standalone signal.
    """

    symbol: str
    model_variant: str  # e.g. "kronos_small_zero_shot"
    forecast_horizon_sessions: int = Field(gt=0)
    median_forecast_return: float
    path_spread_p10_p90: float = Field(ge=0.0)
    sample_count: int = Field(gt=1)
    input_quality_status: QualityStatus
    model_rankic_on_universe: float  # REQUIRED — no default, no None
    data_as_of: date
    generated_at: datetime
    caveat: str = (
        "Zero-shot model forecast. Not a directional signal in isolation; "
        "confidence is bounded by validated RankIC on this universe."
    )

    @model_validator(mode="after")
    def validate_admission_gates(self) -> "KronosForecastEvidence":
        if self.input_quality_status != KRONOS_REQUIRED_QUALITY:
            raise ValueError(
                f"Kronos evidence requires USABLE input data, got "
                f"{self.input_quality_status.value} — surface INSUFFICIENT_DATA instead"
            )
        if self.model_rankic_on_universe < KRONOS_RANKIC_MIN:
            raise ValueError(
                f"model_rankic_on_universe {self.model_rankic_on_universe} is below "
                f"the {KRONOS_RANKIC_MIN} admission threshold — this forecast may "
                "not surface as evidence"
            )
        return self

    @property
    def high_uncertainty(self) -> bool:
        return self.path_spread_p10_p90 > KRONOS_WIDE_SPREAD_THRESHOLD

    @property
    def max_confidence(self) -> float:
        """Confidence ceiling: the validated RankIC itself (capped at 1.0),
        halved when the path spread is wide."""
        ceiling = min(self.model_rankic_on_universe, 1.0)
        return ceiling / 2 if self.high_uncertainty else ceiling


def kronos_admission_check(
    quality_status: QualityStatus, validated_rankic: float | None
) -> tuple[bool, str]:
    """Pre-flight check before any future Kronos inference call.

    Returns (allowed, reason). Today nothing calls Kronos; this exists so
    the future integration has exactly one place where the gates live.
    """
    if quality_status != KRONOS_REQUIRED_QUALITY:
        return False, (
            f"input quality is {quality_status.value}; Kronos requires "
            f"{KRONOS_REQUIRED_QUALITY.value}"
        )
    if validated_rankic is None:
        return False, (
            "no RankIC validation pass has been run on this universe; "
            "Kronos may not be used"
        )
    if validated_rankic < KRONOS_RANKIC_MIN:
        return False, (
            f"validated RankIC {validated_rankic} < {KRONOS_RANKIC_MIN}; "
            "Kronos adds no admissible signal on this universe"
        )
    return True, "admission gates satisfied"

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_kronos_reserved.py`
  ```
"""Kronos reservation tests: gates hold, no inference code exists."""

from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from research_data.kronos_reserved import (
    KRONOS_RANKIC_MIN,
    KronosForecastEvidence,
    kronos_admission_check,
)
from research_data.models import QualityStatus


def make_evidence(**overrides) -> KronosForecastEvidence:
    defaults = dict(
        symbol="MSFT",
        model_variant="kronos_small_zero_shot",
        forecast_horizon_sessions=20,
        median_forecast_return=0.023,
        path_spread_p10_p90=0.079,
        sample_count=20,
        input_quality_status=QualityStatus.USABLE,
        model_rankic_on_universe=0.07,
        data_as_of=date(2026, 6, 25),
        generated_at=datetime(2026, 6, 25, tzinfo=timezone.utc),
    )
    defaults.update(overrides)
    return KronosForecastEvidence(**defaults)


def test_evidence_requires_usable_quality() -> None:
    with pytest.raises(ValueError, match="USABLE"):
        make_evidence(input_quality_status=QualityStatus.PARTIAL)


def test_evidence_requires_validated_rankic_above_threshold() -> None:
    with pytest.raises(ValueError, match="admission threshold"):
        make_evidence(model_rankic_on_universe=0.02)
    assert KRONOS_RANKIC_MIN == 0.03


def test_wide_spread_halves_confidence_ceiling() -> None:
    wide = make_evidence()
    assert wide.high_uncertainty is True
    assert wide.max_confidence == pytest.approx(0.07 / 2)
    narrow = make_evidence(path_spread_p10_p90=0.02)
    assert narrow.high_uncertainty is False
    assert narrow.max_confidence == pytest.approx(0.07)


def test_admission_check_fails_closed() -> None:
    allowed, reason = kronos_admission_check(QualityStatus.STALE, 0.10)
    assert allowed is False and "stale" in reason
    allowed, reason = kronos_admission_check(QualityStatus.USABLE, None)
    assert allowed is False and "validation" in reason
    allowed, reason = kronos_admission_check(QualityStatus.USABLE, 0.01)
    assert allowed is False
    allowed, _ = kronos_admission_check(QualityStatus.USABLE, 0.05)
    assert allowed is True


def test_no_inference_dependencies_reserved_module() -> None:
    """The reservation must not import torch/transformers/huggingface/etc."""
    import research_data.kronos_reserved as module

    source = open(module.__file__).read().lower()
    for banned in ("torch", "transformers", "huggingface", "from_pretrained", "onnx"):
        assert banned not in source

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/hooks_momentum.py`
  ```
"""Python implementation hook for the closed-loop integration test.

This is what a spec's ``hook_ref`` resolves to: a deterministic function
that turns stored prices into a StrategyReturns series for the gate
harness. Monthly-rebalanced equal-weight tilt into the top-K symbols by
12-1 month momentum. Every number derives from the price frame passed in —
nothing is invented.
"""

from __future__ import annotations

from datetime import date

from research_data.factors.momentum import MIN_SESSIONS, twelve_minus_one_return
from research_data.gates.metrics import StrategyReturns
from research_data.read_api import PriceReadAPI

REBALANCE_EVERY_SESSIONS = 21


def momentum_tilt_hook(
    params: dict,
    price_api: PriceReadAPI,
    universe: list[str],
    start: date,
    end: date,
    benchmark_symbol: str = "VOO",
) -> tuple[StrategyReturns, list[float]]:
    """Build (strategy returns, aligned benchmark returns) from stored prices.

    Assumes the test universe shares one session calendar (synthetic data
    guarantees it); raises if that does not hold rather than aligning by
    guesswork.
    """
    top_k = int(params.get("top_k", 2))
    symbols = [s for s in universe if s != benchmark_symbol]
    records = price_api.get_price_frame(
        symbols=symbols + [benchmark_symbol], start=start, end=end
    )

    closes: dict[str, list[float]] = {s: [] for s in symbols + [benchmark_symbol]}
    dates: dict[str, list[date]] = {s: [] for s in symbols + [benchmark_symbol]}
    for record in records:
        closes[record.symbol].append(record.adjusted_close or record.close)
        dates[record.symbol].append(record.trading_date)

    calendar = dates[benchmark_symbol]
    for symbol in symbols:
        if dates[symbol] != calendar:
            raise ValueError(f"{symbol} calendar differs from benchmark calendar")

    n = len(calendar)
    if n <= MIN_SESSIONS:
        raise ValueError(f"need more than {MIN_SESSIONS} sessions, got {n}")

    strategy_dates: list[date] = []
    gross: list[float] = []
    turnover: list[float] = []
    benchmark_returns: list[float] = []
    holdings: list[str] = []

    for i in range(MIN_SESSIONS, n):
        if (i - MIN_SESSIONS) % REBALANCE_EVERY_SESSIONS == 0:
            momentum = {
                s: twelve_minus_one_return(closes[s][: i + 1]) for s in symbols
            }
            ranked = sorted(
                (s for s in symbols if momentum[s] is not None),
                key=lambda s: (momentum[s], s),
                reverse=True,
            )
            new_holdings = ranked[:top_k]
            changed = set(new_holdings) != set(holdings)
            holdings = new_holdings
            day_turnover = 1.0 if changed else 0.0
        else:
            day_turnover = 0.0

        day_return = (
            sum(closes[s][i] / closes[s][i - 1] - 1.0 for s in holdings) / len(holdings)
            if holdings
            else 0.0
        )
        strategy_dates.append(calendar[i])
        gross.append(day_return)
        turnover.append(day_turnover)
        benchmark_returns.append(
            closes[benchmark_symbol][i] / closes[benchmark_symbol][i - 1] - 1.0
        )

    return (
        StrategyReturns(
            strategy_name="momentum_tilt",
            dates=strategy_dates,
            gross_returns=gross,
            turnover=turnover,
        ),
        benchmark_returns,
    )

  ```
- `Write` — `/home/anant_gupta/projects/hub/tradingview/tests/test_closed_loop.py`
  ```
"""The x-factor, end to end:

citation → proposed spec → human approve → Python hook → four gates →
promote → paper thesis → replay journal → lesson → next proposal.

One test walks the entire loop on synthetic stored prices; if any link
breaks (schema, gate order, human gate, journal contract), this fails.
"""

from __future__ import annotations

from datetime import date, datetime, timezone

import duckdb
import pytest

from research_data.brain import (
    BrainStore,
    Citation,
    JournalLink,
    PromotionState,
    SpecStatus,
    StrategySpec,
    is_demo_eligible,
    record_gate_outcome_decision,
    resolve_hook,
)
from research_data.gates import GateHarness
from research_data.paper import (
    ActionLabel,
    PaperEngine,
    PaperMode,
    PaperStore,
    ReplayRun,
    Thesis,
)
from research_data.read_api import PriceReadAPI
from research_data.storage import batch_insert_ohlcv, init_db

from tests.synthetic import make_price_records, trading_days

AS_OF = date(2026, 6, 30)
SESSIONS = 1300  # enough history for momentum warm-up + 3 walk-forward windows
UNIVERSE = ["VOO", "AAPL", "MSFT", "AMZN", "GOOGL"]
NOW = datetime(2026, 7, 10, tzinfo=timezone.utc)


@pytest.fixture(scope="module")
def conn():
    conn = duckdb.connect(":memory:")
    init_db(conn)
    profiles = {
        "VOO": (400.0, 0.0004, 0.007, "etf", "NYSE"),
        "AAPL": (150.0, 0.0012, 0.008, "equity", "NASDAQ"),
        "MSFT": (300.0, 0.0009, 0.007, "equity", "NASDAQ"),
        "AMZN": (180.0, 0.0003, 0.010, "equity", "NASDAQ"),
        "GOOGL": (140.0, 0.0002, 0.009, "equity", "NASDAQ"),
    }
    records = []
    for symbol, (base, drift, vol, asset_type, exchange) in profiles.items():
        records += make_price_records(
            symbol, end=AS_OF, sessions=SESSIONS, base_price=base,
            daily_drift=drift, daily_vol=vol, asset_type=asset_type, exchange=exchange,
        )
    batch_insert_ohlcv(conn, records)
    return conn


def test_full_closed_loop(conn) -> None:
    brain = BrainStore(conn)
    brain.init_schema()
    paper_store = PaperStore(conn)
    paper_store.init_schema()
    price_api = PriceReadAPI(conn)

    # 1. Citation enters the brain.
    citation = Citation(
        source_type="paper",
        title="Returns to Buying Winners and Selling Losers (Jegadeesh-Titman 1993)",
        url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227214",
        retrieved_at=NOW,
        claims=["12-1 month cross-sectional momentum persists out of sample"],
    )
    brain.add_citation(citation)

    # 2. AI proposes a spec citing it.
    spec = StrategySpec(
        name="momentum_tilt_top2",
        description="Monthly equal-weight tilt into top-2 symbols by 12-1 momentum.",
        proposed_by="ai:analyst",
        citation_ids=[citation.citation_id],
        factor_dependencies=["momentum"],
        params={"top_k": 2},
        hook_ref="tests.hooks_momentum:momentum_tilt_hook",
    )
    brain.propose_spec(spec)
    assert brain.get_spec(spec.spec_id).status == SpecStatus.PROPOSED

    # 3. Human approves (the only way forward).
    brain.approve_spec(spec.spec_id, approved_by="Anant")

    # 4. Python hook implements the approved spec from stored data.
    hook = resolve_hook(spec.hook_ref)
    dates = trading_days(AS_OF, SESSIONS)
    strategy, benchmark = hook(
        spec.params, price_api, UNIVERSE, dates[0], AS_OF
    )
    assert len(strategy.gross_returns) > 900

    # 5. Four gates run in order and are recorded.
    outcome = GateHarness().run_and_record(
        brain, spec.spec_id, strategy, benchmark, as_of=AS_OF
    )
    assert [r.gate for r in outcome.results] == [
        "out_of_sample", "monte_carlo", "walk_forward", "deflated_sharpe",
    ]
    assert outcome.all_passed, [
        (r.gate, r.notes) for r in outcome.results if not r.passed
    ]

    # 6. Promotion is a recorded human decision citing the gate runs.
    decision = record_gate_outcome_decision(
        brain, spec.spec_id, decided_by="Anant",
        rationale="All four gates passed on the synthetic verification set.",
    )
    assert decision.to_state == PromotionState.DEMO_ELIGIBLE
    assert is_demo_eligible(brain, spec.spec_id) is True

    # 7. A pre-approved thesis enters the paper book inside its window.
    window = trading_days(AS_OF, 40)
    thesis = Thesis(
        spec_id=spec.spec_id,
        symbol="AAPL",
        action=ActionLabel.ACCUMULATE,
        thesis_text="Spec momentum_tilt_top2 is demo-eligible; AAPL ranks top "
        "of universe on 12-1 momentum. Small starter size in the test window.",
        invalidation_conditions=["Momentum rank drops below universe median."],
        size_fraction=0.10,
        entry_window_start=window[0],
        entry_window_end=window[10],
    )
    paper_store.propose_thesis(thesis)
    paper_store.approve_thesis(thesis.thesis_id, approved_by="Anant")

    # 8. Accelerated replay: timed entry + exit, journal as-if-time-passed.
    engine = PaperEngine(paper_store, price_api)
    written = engine.run_replay(
        ReplayRun(
            spec_id=spec.spec_id,
            start_date=window[0],
            end_date=AS_OF,
            description="closed-loop verification replay",
        )
    )
    exits = [e for e in written if e.entry_type == "exit"]
    assert len(exits) == 1
    assert exits[0].voo_return_same_period is not None

    # 9. The journal lesson links back into the brain…
    lesson = exits[0]
    brain.link_journal(
        JournalLink(
            spec_id=spec.spec_id,
            journal_entry_id=lesson.entry_id,
            relation="lesson",
        )
    )
    assert brain.list_journal_links(spec.spec_id)[0].journal_entry_id == lesson.entry_id

    # 10. …and feeds the next proposal as a citable source: loop closed.
    lesson_citation = Citation(
        source_type="journal_lesson",
        title="Replay lesson: momentum_tilt_top2 entry behaved as specified",
        retrieved_at=NOW,
        claims=[
            f"Replay realized {lesson.realized_return:+.4%} vs benchmark "
            f"{lesson.voo_return_same_period:+.4%} over the same period."
        ],
    )
    brain.add_citation(lesson_citation)
    next_spec = StrategySpec(
        name="momentum_tilt_top2",
        version=2,
        description="v2: add safety-rank filter before the momentum tilt.",
        proposed_by="ai:analyst",
        citation_ids=[citation.citation_id, lesson_citation.citation_id],
        factor_dependencies=["momentum", "safety"],
        params={"top_k": 2, "min_safety_rank": 2},
        hook_ref="tests.hooks_momentum:momentum_tilt_hook",
    )
    brain.propose_spec(next_spec)
    assert brain.get_spec(next_spec.spec_id).status == SpecStatus.PROPOSED
    # The v2 proposal is unproven until it passes its own gates.
    assert brain.get_spec(next_spec.spec_id).promotion_state == PromotionState.UNPROVEN

  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_paper.py tests/test_kronos_reserved.py tests/test_closed_loop.py -q 2>&1 | tail -8`
  ```
claude-opus-4-8[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```diff
  - - Long factor fixtures: generating synthetic OHLCV records in-test (seeded, `tests/synthetic.py`) beats
  committing 14 × 600-row CSVs; existing short CSVs stay for ingestion/provider tests.
  + - Long factor fixtures: generating synthetic OHLCV records in-test (seeded, `tests/synthetic.py`) beats
  committing 14 × 600-row CSVs; existing short CSVs stay for ingestion/provider tests.
- Missing-benchmark exits: never write a placeholder (NaN) into `voo_return_same_period` — an "exit" journal
  entry requires the real figure; when VOO data is absent, write a "review" entry that says so instead.
- Synthetic random walks with high vol can out-drift the intended winner — pin per-symbol seeds in tests
  after checking the actual 12-1 numbers (TSLA needed seed=4).
  ```
- `Bash` — `source .venv/bin/activate && python -m pytest tests/test_paper.py tests/test_kronos_reserved.py tests/test_closed_loop.py -q 2>&1 | tail -8`
  ```
claude-opus-4-8[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md`
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md`
  ```diff
  - ## Current State
- Ingestion foundation partial (`research_data`: models, config, storage, normalization, calendar, quality, read_api, csv_fixture).
- No brain, factor engine, fundamentals path, four-gate harness, paper journal, or strategy UI in code yet.
- Alignment decisions locked in [[Session Findings — Cursor Alignment Pass (2026-07-10)]].
- `.env` prepared for `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (never commit).
  + ## Current State
- ==Executed by Fable 5 on 2026-07-10== — see [[Year-Ahead Base — Build Report (2026-07-10)]] for what landed, test results, and leftovers.
- In repo now: `brain/` (closed loop, human-gated), `factors/` (momentum 12-1, safety, quality_fcf, valuation, ETF baseline, TA context-only), `fundamentals/` (FMP + SEC EDGAR parsers/clients/store), `gates/` (OOS → Monte Carlo → walk-forward → deflated Sharpe), `paper/` (theses, timed auto-entry, replay journal, live-book hooks), `kronos_reserved.py` (schema/gates only), 14-symbol `assets.toml` (BRK.B stored as `BRKB`), `Docs/YEAR_AHEAD_BASE.md` mirror.
- Ingestion foundation still partial where it was (`evidence.py`, `benchmark.py`, polygon client, CLI, quality tests 7.2–7.4 remain Cursor leftovers).
- Alignment decisions locked in [[Session Findings — Cursor Alignment Pass (2026-07-10)]].
- `.env` prepared for `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (never commit).
  ```
- `Bash` — `grep -n "^#" "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/RESEARCH.md" | head -40`
  ```
claude-opus-4-8[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/RESEARCH.md`
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md`
  ```diff
  - ## Current State
- Ingestion foundation partial (`research_data`: models, config, storage, normalization, calendar, quality, read_api, csv_fixture).
- No brain, factor engine, fundamentals path, four-gate harness, paper journal, or strategy UI in code yet.
- Alignment decisions locked in [[Session Findings — Cursor Alignment Pass (2026-07-10)]].
- `.env` prepared for `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (never commit).
  + ## Current State
- ==Executed by Fable 5 on 2026-07-10== — see [[Year-Ahead Base — Build Report (2026-07-10)]] for what landed, test results, and leftovers.
- In repo now: `brain/` (closed loop, human-gated), `factors/` (momentum 12-1, safety, quality_fcf, valuation, ETF baseline, TA context-only), `fundamentals/` (FMP + SEC EDGAR parsers/clients/store), `gates/` (OOS → Monte Carlo → walk-forward → deflated Sharpe), `paper/` (theses, timed auto-entry, replay journal, live-book hooks), `kronos_reserved.py` (schema/gates only), 14-symbol `assets.toml` (BRK.B stored as `BRKB`), `Docs/YEAR_AHEAD_BASE.md` mirror.
- Ingestion foundation still partial where it was (`evidence.py`, `benchmark.py`, polygon client, CLI, quality tests 7.2–7.4 remain Cursor leftovers).
- Alignment decisions locked in [[Session Findings — Cursor Alignment Pass (2026-07-10)]].
- `.env` prepared for `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (never commit).
  ```

## You

# Fable 5 — RESUME year-ahead base (finish only; do not rebuild)

## Why
Previous run hit session limit mid-finish. Most code is already landed and green. Your job is to **verify, sync notes, and close Definition of Done** — not re-implement brain/factors/gates/paper/kronos.

## Mistakes from last run — do not repeat
1. Do **not** use `jarvis-fs` for vault access. Use the **jarvis MCP** only: `vault_list`, `vault_read`, `vault_get_document_map`, `vault_patch`, `vault_append`, `vault_write`. Prefer `vault_patch` by heading; preserve frontmatter keys.
2. Do **not** recreate packages that already exist under `src/research_data/{brain,factors,fundamentals,gates,paper}/` or `kronos_reserved.py`.
3. Do **not** re-open settled law (personal-only, no Kalshi/Polymarket, Kronos = reserved only, four-gate order, no BUY/SELL language).
4. DuckDB: keep naive-UTC normalization on write (`_to_db_ts` pattern). Do not “fix” unrelated `storage.py` drive-by.
5. When Bash/tools throttle: wait and retry; do not invent alternate architectures.
6. Act when you have enough info. Pause only for true blockers. Before progress claims, audit against tool results from THIS session.

## Current verified state (Cursor re-check, trust then re-confirm)
- Repo: `/home/anant_gupta/projects/hub/tradingview`
- Packages + tests for brain/factors/fundamentals/gates/paper/kronos/closed-loop already present
- `pytest -q` recently: **420 passed**
- Vault SoT folder: `20_Progress/Projects/CS/TradingView/` — start with `Fable 5 — Read Order`, then Session Findings
- Stale: vault `Year-Ahead Base — Fable 5 Architecture Contract.md` → Current State still claims modules missing
- Stale: `Docs/YEAR_AHEAD_BASE.md` Out-of-scope still lists `.kiro` 7.2–13 as Cursor leftovers — those are **DONE** (ingestion complete)

## Remaining work (in order) — this is the whole job
1. `source .venv/bin/activate && pytest -q` — if anything fails, fix only the failure; do not expand scope.
2. Guardrail sweep: no BUY/SELL/guaranteed/risk-free; no PM schema; no Kronos inference imports; no secrets in repo; `.env` gitignored.
3. Update vault via **jarvis MCP** (patch by heading):
   - `Year-Ahead Base — Fable 5 Architecture Contract.md` — Current State, Next Action, Done reflection matching what was actually built
   - `Math-First Map — Existing Code to Factor Brain.md` — mark Fable slice done; note Cursor finished `.kiro` plumbing
   - `Session Findings — Cursor Alignment Pass (2026-07-10).md` — short Log/Open Questions update if needed
   - Append one line to `60_Claude/07_AI_Information/Session Logs/log.md`
4. Update `Docs/YEAR_AHEAD_BASE.md`: accurate module map; fix Out-of-scope (remove completed `.kiro` leftovers); how-to-run still correct.
5. Append lessons to `Docs/fable5_run_memory.md` (jarvis MCP > jarvis-fs; session-limit resume; 420-pass baseline).
6. Honest final report to user: what exists, pytest count, vault files patched, Cursor leftovers (if any real ones), risks. Lead with outcome.

## Out of scope on this resume
- Rebuilding factors/gates/brain/paper from scratch
- Streamlit/UI/charting library
- Kronos download/inference
- Kalshi/Polymarket
- Multi-agent debate layer
- Drive-by refactors of ingestion spine

## Definition of Done
Vault + Docs match the code; full pytest green; guardrails clean; one clear final report. Then stop.

## Claude

Suite is still running. Meanwhile, checking what Cursor's new modules do so the Docs module map is accurate.

**420 passed** — confirmed green in this session. Now syncing the vault via the jarvis MCP.

Vault synced. Now updating the repo docs — re-reading `Docs/YEAR_AHEAD_BASE.md` first in case Cursor touched it.

Now appending the resume lessons to the run memory.

**The year-ahead base is done and verified: 420 tests passing, guardrails clean, vault and repo docs now match the code.** Definition of Done is closed; nothing was rebuilt on this resume — I verified, fixed the stale notes, and stopped.

## What was verified this session

- **Full suite: 420 passed, 0 failed** (`pytest -q`, offline, ~2.5 min). This covers both slices: the Fable base (`brain/`, `factors/`, `fundamentals/`, `gates/`, `paper/`, `kronos_reserved.py`, closed-loop integration test) and Cursor's completed `.kiro` plumbing (`evidence.py`, `benchmark.py`, `cli.py` + `__main__.py`, `providers/polygon.py`, quality/property/scope tests — all 60 spec tasks checked).
- **Guardrail sweep clean.** No execution language in output paths (the `BUY`/`SELL` grep hits are `benchmark.py`'s own forbidden-token checklist — enforcement, not violation). No Kalshi/Polymarket code or schema. No Kronos inference imports (torch/transformers/from_pretrained absent, enforced by a test). No broker SDKs. No hardcoded secrets; `.env` is confirmed gitignored.

## What was synced

**Vault** (via jarvis MCP, patched by heading, frontmatter preserved):
- `Year-Ahead Base — Fable 5 Architecture Contract` — Current State rewritten to reflect the landed modules and 420-test result; Next Action now points at the live-data shakeout; Definition of Done checked off item by item.
- `Math-First Map — Existing Code to Factor Brain` — slice A (Fable) and slice B (Cursor `.kiro`) both marked done; slice C remains the future queue.
- `Session Findings — Cursor Alignment Pass (2026-07-10)` — Open Questions updated: base+plumbing checked off, live-data shakeout added as the new first item.
- One summary line appended to `60_Claude/07_AI_Information/Session Logs/log.md`.

**Repo docs:**
- `Docs/YEAR_AHEAD_BASE.md` — status banner added (base complete, 420 tests), module map now includes `evidence.py`/`benchmark.py`/`cli.py`/`polygon.py`, the fixtures description matches reality (`tests/synthetic.py`, no phantom `long/` dir), and the out-of-scope section no longer lists the completed `.kiro` leftovers.
- `Docs/fable5_run_memory.md` — resume lessons added (jarvis MCP for vault, 420 baseline, grep-sweep whitelist for enforcement code, throttle handling) and the two stale lines corrected.

## Leftovers and risks (honest list)

- **Nothing committed to git.** Everything from both build sessions sits as modified/untracked working-tree files (`git status` shows ~20 new files). Say the word and I'll commit on a branch — I didn't commit since that wasn't in the resume scope.
- **Live-data shakeout not run**: polygon/FMP/SEC clients are tested against fixtures and fail closed without keys, but no real API call has been made yet. First real ingestion of the 14-symbol universe is the next phase's opening move.
- **Known latent issue, deliberately untouched**: `storage.py` (ingestion spine) still stores tz-aware timestamps as naive local time; the new stores normalize to naive UTC. Flagged in run memory — fix belongs to a deliberate pass, not a drive-by.
- Deferred by design: Kronos inference (needs RankIC validation first), UI/charting choice, multi-agent layer, anything real-money or PM-vertical.

**Tool calls:**

- `Bash` — `source .venv/bin/activate && python -m pytest -q 2>&1 | tail -3`
  ```
Command running in background with ID: bxgvbmmll. Output is being written to: /tmp/claude-1001/-home-anant-gupta-projects-hub-tradingview/[REDACTED]/tasks/bxgvbmmll.output. You will be notified when it completes. To check interim output, use Read on that file path.
  ```
- `Bash` — `git log --oneline -8 && git status --short | head -20 && ls src/research_data src/research_data/providers && ls tests | head -40`
  ```
7361948 Set up Claude Code tooling for the data-ingestion-foundation workflow
b7dd9fc Initial commit: data ingestion foundation
 M .kiro/specs/data-ingestion-foundation/tasks.md
 M config/assets.toml
 M src/research_data/calendar.py
 M src/research_data/read_api.py
 M src/research_data/storage.py
?? Docs/YEAR_AHEAD_BASE.md
?? Docs/fable5_run_memory.md
?? src/research_data/__main__.py
?? src/research_data/benchmark.py
?? src/research_data/brain/
?? src/research_data/cli.py
?? src/research_data/env.py
?? src/research_data/evidence.py
?? src/research_data/factors/
?? src/research_data/fundamentals/
?? src/research_data/gates/
?? src/research_data/kronos_reserved.py
?? src/research_data/paper/
?? src/research_data/providers/polygon.py
?? tests/conftest.py
src/research_data:
__init__.py
__main__.py
__pycache__
benchmark.py
brain
calendar.py
cli.py
config.py
env.py
evidence.py
factors
fundamentals
gates
kronos_reserved.py
models.py
normalization.py
paper
providers
quality.py
read_api.py
storage.py

src/research_data/providers:
__init__.py
__pycache__
base.py
csv_fixture.py
polygon.py
__init__.py
__pycache__
conftest.py
fixtures
helpers.py
hooks_momentum.py
synthetic.py
test_benchmark.py
test_brain_loop.py
test_brain_store.py
test_calendar.py
test_cli.py
test_closed_loop.py
test_factors_engine.py
test_factors_math.py
test_fundamentals.py
test_gates.py
test_kronos_reserved.py
test_models.py
test_models_validation.py
test_normalization.py
test_paper.py
test_polygon.py
test_property_adjustment_mapping.py
test_property_duplicate_pk.py
test_property_evidence.py
test_property_ingestion.py
test_property_market_calendar.py
test_property_no_fabrication.py
test_property_no_secrets.py
test_property_ohlcv_validation.py
test_property_provider_registry.py
test_property_quality_status.py
test_property_raw_payload_hash.py
test_property_read_api.py
test_property_rejected_records.py
test_property_roundtrip.py
test_provider_registry.py
test_quality.py
test_security_scope.py
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/hub/tradingview
echo "== execution language in src (BUY/SELL as labels, guaranteed, risk-free) =="
grep -rniE '"(buy|sell)"|'"'"'(buy|sell)'"'"'|\bguaranteed\b|risk[- ]free' src/ --include="*.py" | grep -viv "buy-and-hold\|buy_hold\|buying winners\|selling losers" || echo "CLEAN"
echo "== PM / out-of-scope asset classes in src =="
grep -rniE 'kalshi|polymarket|prediction.market|option[s]? chain|futures|crypto|margin|leverage|intraday|tick data' src/ --include="*.py" || echo "CLEAN"
echo "== Kronos inference imports =="
grep -rniE 'torch|transformers|huggingface|from_pretrained|onnx' src/ --include="*.py" || echo "CLEAN"
echo "== broker SDKs =="
grep -rniE 'alpaca|ibkr|interactive.?brokers|robinhood|ccxt|broker' src/ --include="*.py" || echo "CLEAN"
echo "== .env gitignored =="
git check-ignore .env && echo "ignored OK"
echo "== potential secrets in tracked+untracked source =="
grep -rniE '(api_key|token|secret)\s*=\s*["'"'"'][A-Za-z0-9]{12,}' src/ tests/ config/ || echo "CLEAN"
  ```
  ```
== execution language in src (BUY/SELL as labels, guaranteed, risk-free) ==
src/research_data/benchmark.py:20:_EXECUTION_TOKENS = frozenset({"BUY", "SELL", "HOLD", "BUY NOW", "SELL NOW"})
src/research_data/benchmark.py:250:    for token in ("BUY", "SELL", "HOLD"):
== PM / out-of-scope asset classes in src ==
src/research_data/fundamentals/store.py:139:    margin_periods: int = 8,
src/research_data/fundamentals/store.py:144:    (statement coverage varies by source); the operating-margin history comes
src/research_data/fundamentals/store.py:161:    margins = [
src/research_data/fundamentals/store.py:163:        for m in (s.operating_margin for s in quarterly[-margin_periods:])
src/research_data/fundamentals/store.py:178:        operating_margins=margins,
src/research_data/factors/quality_fcf.py:8:- FCF margin: FCF / revenue.
src/research_data/factors/quality_fcf.py:9:- Operating-margin stability: stdev of operating margin across trailing
src/research_data/factors/quality_fcf.py:18:    fcf_margin     = fcf / revenue
src/research_data/factors/quality_fcf.py:37:    "fcf_margin": 0.25,
src/research_data/factors/quality_fcf.py:38:    "op_margin_stability": 0.15,
src/research_data/factors/quality_fcf.py:48:    V1 universe). ``operating_margins`` holds trailing per-period operating
src/research_data/factors/quality_fcf.py:49:    margins (most recent last) for the stability check.
src/research_data/factors/quality_fcf.py:62:    operating_margins: list[float] = field(default_factory=list)
src/research_data/factors/quality_fcf.py:77:    fcf_margin: float | None
src/research_data/factors/quality_fcf.py:78:    op_margin_stability: float | None  # stdev of operating margins (lower better)
src/research_data/factors/quality_fcf.py:112:    fcf_margin: float | None = None
src/research_data/factors/quality_fcf.py:114:        fcf_margin = fcf / inputs.revenue
src/research_data/factors/quality_fcf.py:117:    if len(inputs.operating_margins) >= 4:
src/research_data/factors/quality_fcf.py:118:        stability = statistics.stdev(inputs.operating_margins)
src/research_data/factors/quality_fcf.py:131:        fcf_margin=fcf_margin,
src/research_data/factors/quality_fcf.py:132:        op_margin_stability=stability,
src/research_data/factors/quality_fcf.py:145:    better: high FCF/EV and FCF margin, low margin stdev, low leverage). Each
src/research_data/factors/quality_fcf.py:151:    fcf_margin_ranks = ascending_ranks({s: m.fcf_margin for s, m in metrics.items()})
src/research_data/factors/quality_fcf.py:153:        {s: m.op_margin_stability for s, m in metrics.items()}
src/research_data/factors/quality_fcf.py:155:    leverage_ranks = inverse_ranks({s: m.debt_to_equity for s, m in metrics.items()})
src/research_data/factors/quality_fcf.py:159:        "fcf_margin": fcf_margin_ranks,
src/research_data/factors/quality_fcf.py:160:        "op_margin_stability": stability_ranks,
src/research_data/factors/quality_fcf.py:161:        "debt_to_equity": leverage_ranks,
src/research_data/fundamentals/models.py:46:    def operating_margin(self) -> float | None:
src/research_data/factors/packets.py:66:    fcf_margin: float | None = None
src/research_data/factors/packets.py:67:    op_margin_stability: float | None = None  # stdev of operating margin (lower = steadier)
src/research_data/factors/packets.py:76:    """Composite 0-100 of FCF/EV, FCF margin, margin stability, and leverage.
src/research_data/factors/engine.py:220:                fcf_margin=quality_metrics.fcf_margin,
src/research_data/factors/engine.py:221:                op_margin_stability=quality_metrics.op_margin_stability,
src/research_data/factors/engine.py:238:                "Weighted rank composite of FCF/EV, FCF margin, margin stability, leverage."
== Kronos inference imports ==
CLEAN
== broker SDKs ==
src/research_data/__init__.py:9:broker integration, or execution capabilities.
== .env gitignored ==
.env
ignored OK
== potential secrets in tracked+untracked source ==
CLEAN
  ```
- `Read` — `/tmp/claude-1001/-home-anant-gupta-projects-hub-tradingview/92f7e8da-1704-4be4-9ed9-25c0398c4d75/tasks/bxgvbmmll.output`
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/hub/tradingview
for f in evidence.py benchmark.py cli.py __main__.py providers/polygon.py; do echo "== $f =="; head -12 src/research_data/$f | sed -n '1,12p'; done
echo "== tasks.md checkbox summary =="; grep -c "\[x\]" .kiro/specs/data-ingestion-foundation/tasks.md; grep -c "\[ \]" .kiro/specs/data-ingestion-foundation/tasks.md || true
  ```
  ```
== evidence.py ==
"""Evidence packet builder for downstream AI consumption.

Builds DataEvidencePacket instances from stored OHLCV records and quality
reports with full provenance. Does not call any LLM APIs.

Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6
"""

from __future__ import annotations

from datetime import date, datetime, timezone

== benchmark.py ==
"""Benchmark reporter for data-sanity metrics (not a strategy engine).

Computes return, volatility, drawdown, and excess return versus a configured
ETF baseline. Refuses computation for insufficient or stale data. Never emits
execution language (BUY/SELL/HOLD).

Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6
"""

from __future__ import annotations

import math
== cli.py ==
"""Typer CLI for the research_data ingestion foundation.

Commands: init-db, ingest-prices, audit-prices, benchmark.
Wires ProviderRegistry → raw payload writer → normalizer → quality auditor
→ storage. Never emits BUY/SELL/HOLD execution language.

Requirements: 9.1–9.7, 13.1–13.6, 14.1, 14.5
"""

from __future__ import annotations

import hashlib
== __main__.py ==
"""Module entrypoint: python -m research_data.cli"""

from research_data.cli import main

if __name__ == "__main__":
    main()
== providers/polygon.py ==
"""Polygon.io daily OHLCV provider.

Fetches end-of-day aggregates from the Polygon stocks API with rate limiting
and retry/backoff. Never fabricates data on empty responses.

Requirements: 2.1, 2.2, 2.3, 2.4, 2.5
"""

from __future__ import annotations

import hashlib
import json
== tasks.md checkbox summary ==
60
0
  ```
- `Read` — `/tmp/claude-1001/-home-anant-gupta-projects-hub-tradingview/92f7e8da-1704-4be4-9ed9-25c0398c4d75/tasks/bxgvbmmll.output`
- `TaskUpdate` — `{"taskId":"6","status":"completed"}`
- `TaskUpdate` — `{"taskId":"7","status":"completed"}`
- `TaskUpdate` — `{"taskId":"8","status":"completed"}`
- `TaskUpdate` — `{"taskId":"9","status":"in_progress","activeForm":"Syncing vault notes"}`
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_append,mcp__jarvis__vault_get_document_map","max_results":2}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md","targetType":"heading","target":"Year-Ahead Base — Fable 5 Architecture Contract::Current State","operation":"replace","content":"- ==Base executed (2026-07-10)==: Fable 5 landed the hard slice; Cursor completed the `.kiro` ingestion plumbing (all 60 spec tasks checked). Full offline suite: **420 tests passing**.\n- In repo now: `brain/` (closed loop — citations, specs, human-gated approve, test runs, promote/demote, journal links), `factors/` (momentum 12-1, safety/vol, quality_fcf, valuation FCF/EV, ETF baseline vs VOO, TA context-only → `ScorePacket`), `fundamentals/` (FMP + SEC EDGAR parsers/clients/store, provenance on every field, offline fixtures), `gates/` (OOS → Monte Carlo → walk-forward → deflated Sharpe; costs, drawdown, trade count, vs-VOO; fail-closed on thin data), `paper/` (pre-approved theses, timed auto-entry in windows, replay journal-as-if-time-passed, live-book review jump-ahead hooks, `voo_return_same_period` required on exits), `kronos_reserved.py` (schema + USABLE/RankIC≥0.03 admission gates, zero inference).\n- Cursor's `.kiro` completions: `evidence.py`, `benchmark.py` (refuses execution language), `cli.py` (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`), `providers/polygon.py`, quality/property tests, scope/security checks.\n- Universe expanded to 14 symbols; canonical letters-only `BRKB` stands for BRK.B (providers map their own punctuation).\n- Contract mirrored in-repo at `Docs/YEAR_AHEAD_BASE.md`; build lessons in `Docs/fable5_run_memory.md`.\n- `.env` (gitignored) holds `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT`; `research_data.env.load_dotenv()` loads it without echoing values.\n"}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md","targetType":"heading","target":"Year-Ahead Base — Fable 5 Architecture Contract::Next Action","operation":"replace","content":"Contract executed end-to-end (2026-07-10). Next phase (new handoff, not this contract): live-data shakeout with real keys (polygon prices, FMP/SEC fundamentals into the stores), first real replay studies on the 14-symbol universe, then charting/UI choice and the agent layer consuming `ScorePacket`s. Kronos stays reserved until a RankIC validation pass on this universe.\n"}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md","targetType":"heading","target":"Year-Ahead Base — Fable 5 Architecture Contract::Definition of Done (Fable 5)","operation":"replace","content":"All met 2026-07-10 (verified against `pytest` output, 420 passing):\n- [x] Vault notes under this folder updated to match what was built\n- [x] `Docs/YEAR_AHEAD_BASE.md` exists and matches code\n- [x] Brain loop persists and is tested (incl. full closed-loop integration test `tests/test_closed_loop.py`)\n- [x] Factor(+fundamentals) path produces score packets on fixture data (live keys pending shakeout)\n- [x] Four gates runnable with pass/fail records (fail-closed, recorded in brain, never silent)\n- [x] Paper-test contracts stored (thesis gate, timed entry, replay + live modes; UI intentionally absent)\n- [x] Kronos reserved only (no inference imports — enforced by test)\n- [x] Honest report delivered: what passed, leftovers, risks\n"}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Math-First Map — Existing Code to Factor Brain.md","targetType":"heading","target":"Math-First Map — Existing Code to Factor Brain::Still Left and Necessary (ordered)::A — Fable 5 hard slice (now)","operation":"replace","content":"==Done 2026-07-10 (Fable 5).== All seven items landed with tests:\n1. [x] Brain persistence + closed-loop APIs (`brain/models|store|loop`) — human-gated approve/promote, gate-order enforcement\n2. [x] Factor scorers + `ScorePacket`s (`factors/`) — formulas, windows, INSUFFICIENT_DATA kill-paths\n3. [x] Minimal FMP/SEC fundamentals path (`fundamentals/`) — pure parsers, fail-closed live clients, DuckDB store\n4. [x] Four-gate harness + eligibility (`gates/`) — OOS/MC/WF/DSR, short-circuit, recorded to brain\n5. [x] Paper-test contracts (`paper/`) — approve → timed entry; replay journal-as-if-time-passed; live-book review hooks\n6. [x] Vault + `Docs/YEAR_AHEAD_BASE.md` mirror\n7. [x] Kronos reserved fields/docs only (`kronos_reserved.py`)\n"}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Math-First Map — Existing Code to Factor Brain.md","targetType":"heading","target":"Math-First Map — Existing Code to Factor Brain::Still Left and Necessary (ordered)::B — Cursor next (plumbing, not the hard product problem)","operation":"replace","content":"==Done 2026-07-10 (Cursor).== All `.kiro` data-ingestion-foundation tasks are checked (60/60):\n1. [x] Quality tests 7.2–7.4\n2. [x] `evidence.py` builder (`DataEvidencePacket` for downstream agents)\n3. [x] `benchmark.py` reporter (refuses execution language)\n4. [x] `providers/polygon.py` with rate limiting + retry/backoff\n5. [x] CLI (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`) + property tests\n6. [x] Scope/security checks (task 13, `tests/test_security_scope.py`)\n\nFull offline suite after both slices: **420 tests passing**. Section C below remains the future queue.\n"}`
- `mcp__jarvis__vault_patch` — `{"path":"20_Progress/Projects/CS/TradingView/Session Findings — Cursor Alignment Pass (2026-07-10).md","targetType":"heading","target":"Session Findings — Cursor Alignment Pass (2026-07-10)::Open Questions","operation":"replace","content":"- [x] Fable 5 year-ahead base landed AND Cursor completed `.kiro` 7.2–13 leftovers (2026-07-10; 420 offline tests green — see [[Year-Ahead Base — Fable 5 Architecture Contract]] Current State)\n- [ ] Live-data shakeout: run polygon/FMP/SEC clients with real keys, ingest the 14-symbol universe, first real replay study\n- [ ] RankIC validation pass before any Kronos inference\n- [ ] Re-check shared-core shape only after real paper-journal weeks exist (Postmortem residual risk) — still **no PM code** until paper readiness\n- [ ] In-app charting library choice (durable, navigable, not a widget junk drawer)\n"}`
- `mcp__jarvis__vault_append` — `{"path":"60_Claude/07_AI_Information/Session Logs/log.md","content":"\n- 2026-07-10 — Fable 5 (resume): TradingView year-ahead base closed out. Verified 420 offline tests green; guardrail sweep clean (no execution language, no PM code, no Kronos inference, no secrets, `.env` ignored). Vault synced: Architecture Contract (Current State / Next Action / DoD), Math-First Map (slices A+B done), Session Findings (Open Questions). Repo docs: `Docs/YEAR_AHEAD_BASE.md` + `Docs/fable5_run_memory.md` updated. Next: live-data shakeout, replay studies, charting/agent layer.\n"}`
- `Read` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
  ```diff
  - > conflict, the vault session-findings note wins. Built by Fable 5, 2026-07-10.
  + > conflict, the vault session-findings note wins. Built by Fable 5, 2026-07-10.
>
> **Status 2026-07-10:** base complete. Fable 5 slice (brain/factors/fundamentals/gates/paper/kronos-reserved)
> and Cursor's `.kiro` ingestion plumbing (evidence, benchmark, CLI, polygon — all 60 spec tasks) are both
> landed. Full offline suite: **420 tests passing**.
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
  ```diff
  -   read_api.py          # PriceReadAPI.get_price_frame — sole price read path for downstream modules
  kronos_reserved.py   # Kronos evidence schema + admission gates ONLY — no inference imports
  providers/           # csv_fixture (offline default), polygon/tiingo/alpha_vantage/fmp price clients
  +   read_api.py          # PriceReadAPI.get_price_frame — sole price read path for downstream modules
  evidence.py          # DataEvidencePacket builder for downstream AI (no LLM calls)
  benchmark.py         # data-sanity benchmark reporter vs ETF baseline (refuses execution language)
  cli.py, __main__.py  # Typer CLI: init-db | ingest-prices | audit-prices | benchmark
  kronos_reserved.py   # Kronos evidence schema + admission gates ONLY — no inference imports
  providers/           # csv_fixture (offline default), polygon.py (rate-limited live client)
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
  ```diff
  - tests/                 # offline by default; property tests prefixed test_property_
  fixtures/            # short CSVs (ingestion tests) + long/ (2y+ synthetic OHLCV for factor/gate tests)
                       # + fundamentals/ (statement fixtures)
  + tests/                 # offline by default; property tests prefixed test_property_
  synthetic.py         # seeded synthetic OHLCV generator (long series for factor/gate/paper tests)
  fixtures/            # short CSVs (ingestion tests) + fundamentals/ (FMP + SEC statement fixtures)
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md`
  ```diff
  - ## Out of scope here (Cursor next / later phases)

- `.kiro` leftovers: quality tests 7.2–7.4, `evidence.py` builder, `benchmark.py`, polygon client completion,
  CLI tasks 9–13.
- Multi-agent debate layer, Streamlit UI, charting library choice.
- Kronos download/inference + RankIC validation pass.
- Real-money surface, TradingView.com record-keeping, Kalshi/Polymarket vertical (only after paper readiness).
  + ## Out of scope here (later phases)

- ~~`.kiro` leftovers~~ — completed by Cursor 2026-07-10 (quality tests, evidence builder, benchmark,
  polygon client, CLI, scope checks).
- Live-data shakeout: first real polygon/FMP/SEC ingestion with keys, real replay studies.
- Multi-agent debate layer, Streamlit UI, charting library choice.
- Kronos download/inference + RankIC validation pass.
- Real-money surface, TradingView.com record-keeping, Kalshi/Polymarket vertical (only after paper readiness).
  ```
- `Read` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```diff
  - - Vault is reachable at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/`
  (WSL mount). `jarvis-fs` MCP only allows the repo; use plain file reads/writes on the mount for vault edits.
  + - Vault edits: use the **jarvis MCP** (`vault_patch` by heading, `vault_append`, `vault_read`) — not
  `jarvis-fs` (repo-only) and not raw writes on the `/mnt/d` mount. Patch by heading preserves frontmatter.
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```diff
  - - Synthetic random walks with high vol can out-drift the intended winner — pin per-symbol seeds in tests
  after checking the actual 12-1 numbers (TSLA needed seed=4).
  + - Synthetic random walks with high vol can out-drift the intended winner — pin per-symbol seeds in tests
  after checking the actual 12-1 numbers (TSLA needed seed=4).

## Resume (2026-07-10, after session limit)

- Session limits mid-build are survivable: code was already green; the resume job was verify → sync notes →
  report, NOT rebuild. Re-confirm state from tool output before touching anything.
- Post-resume verified baseline: **420 tests passing** (Fable slice + Cursor's completed `.kiro` plumbing:
  `evidence.py`, `benchmark.py`, `cli.py`, `providers/polygon.py`, quality/property/scope tests — 60/60 tasks).
- Guardrail sweep note: `benchmark.py` legitimately *contains* the strings BUY/SELL — as a forbidden-token
  checklist it asserts its own output against. Grep sweeps must whitelist enforcement code.
- When Bash/Edit throttle ("classifier unavailable"): wait and retry; read-only tools keep working — do not
  switch architectures or improvise alternate write paths.
  ```
- `Edit` — `/home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md`
  ```diff
  - - Existing short fixtures (65 rows) are for ingestion tests; factor/gate tests need 2y+ deterministic synthetic
  fixtures under `tests/fixtures/long/` — synthetic *test* data is fine, fabricated *product* data is not.
  + - Existing short fixtures (65 rows) are for ingestion tests; factor/gate tests use seeded synthetic series
  from `tests/synthetic.py` — synthetic *test* data is fine, fabricated *product* data is not.
  ```
- `TaskUpdate` — `{"taskId":"9","status":"completed"}`
- `TaskUpdate` — `{"taskId":"10","status":"completed"}`

## Actions Taken
- Files created: /home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md, /home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md, /home/anant_gupta/projects/hub/tradingview/src/research_data/env.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/__init__.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/models.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/loop.py, /home/anant_gupta/projects/hub/tradingview/tests/test_brain_store.py, /home/anant_gupta/projects/hub/tradingview/tests/test_brain_loop.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/packets.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ranking.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/momentum.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/safety.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/quality_fcf.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/etf_baseline.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/ta_context.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/engine.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/factors/__init__.py, /home/anant_gupta/projects/hub/tradingview/tests/synthetic.py, /home/anant_gupta/projects/hub/tradingview/tests/test_factors_math.py, /home/anant_gupta/projects/hub/tradingview/tests/test_factors_engine.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/__init__.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/models.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/fmp.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/sec.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/fundamentals/store.py, /home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_income.json, /home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_balance.json, /home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_fmp_cashflow.json, /home/anant_gupta/projects/hub/tradingview/tests/fixtures/fundamentals/AAPL_companyfacts.json, /home/anant_gupta/projects/hub/tradingview/tests/test_fundamentals.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/metrics.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/oos.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/monte_carlo.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/walk_forward.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/deflated_sharpe.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/harness.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/gates/__init__.py, /home/anant_gupta/projects/hub/tradingview/tests/test_gates.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/paper/__init__.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/paper/models.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/paper/store.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/paper/engine.py, /home/anant_gupta/projects/hub/tradingview/tests/test_paper.py, /home/anant_gupta/projects/hub/tradingview/src/research_data/kronos_reserved.py, /home/anant_gupta/projects/hub/tradingview/tests/test_kronos_reserved.py, /home/anant_gupta/projects/hub/tradingview/tests/hooks_momentum.py, /home/anant_gupta/projects/hub/tradingview/tests/test_closed_loop.py
- Files modified: /home/anant_gupta/projects/hub/tradingview/src/research_data/brain/store.py, /home/anant_gupta/projects/hub/tradingview/Docs/fable5_run_memory.md, /home/anant_gupta/projects/hub/tradingview/tests/test_factors_engine.py, /home/anant_gupta/projects/hub/tradingview/config/assets.toml, /home/anant_gupta/projects/hub/tradingview/src/research_data/paper/engine.py, /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/Year-Ahead Base — Fable 5 Architecture Contract.md, /home/anant_gupta/projects/hub/tradingview/Docs/YEAR_AHEAD_BASE.md
- Files deleted: (none)
- Commands run: find /home/anant_gupta/projects/hub/tradingview -type f \( -name "*.py" -o -name "*.toml" -o -name "*.md" \) -not -path "*/.venv/*" -not -path "*/.git/*" | sort, ls -R /home/anant_gupta/projects/hub/tradingview/src /home/anant_gupta/projects/hub/tradingview/tests /home/anant_gupta/projects/hub/tradingview/Docs /home/anant_gupta/projects/hub/tradingview/config 2>/dev/null; echo ---; ls /home/anant_gupta/projects/hub/tradingview; echo ---; cat /home/anant_gupta/projects/hub/tradingview/.gitignore 2>/dev/null, ls "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/" 2>&1, cd "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/" && wc -c *.md | sort -n, cat config/assets.toml config/providers.toml pyproject.toml && ls -la .env* 2>/dev/null; head -3 tests/fixtures/VOO.csv; wc -l tests/fixtures/*.csv, cut -d= -f1 .env && source .venv/bin/activate && python -m pytest -q 2>&1 | tail -5, source .venv/bin/activate && python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -15, source .venv/bin/activate && python -c " import duckdb from datetime import datetime, timezone c = duckdb.connect(':memory:') c.execute('CREATE TABLE t (ts TIMESTAMP)') c.execute('INSERT INTO t VALUES (?)', [datetime(2026,7,10,12,0,0,tzinfo=timezone.utc)]) print(c.execute('SELECT ts FROM t').fetchone()) print('tz:', datetime.now().astimezone().tzinfo) ", python - <<'EOF' import re p = 'src/research_data/brain/store.py' s = open(p).read() subs = [ ("citation.retrieved_at,", "_to_db_ts(citation.retrieved_at),"), ("citation.created_at,", "_to_db_ts(citation.created_at),"), ("spec.created_at,\n spec.approved_by,\n spec.approved_at,", "_to_db_ts(spec.created_at),\n spec.approved_by,\n _to_db_ts(spec.approved_at),"), ("[SpecStatus.APPROVED.value, approved_by, approved_at, spec_id],", "[SpecStatus.APPROVED.value, approved_by, _to_db_ts(approved_at), spec_id],"), ("run.as_of,\n run.created_at,", "run.as_of,\n _to_db_ts(run.created_at),"), ("decision.decided_by,\n decision.created_at,", "decision.decided_by,\n _to_db_ts(decision.created_at),"), ("link.relation, link.created_at]", "link.relation, _to_db_ts(link.created_at)]"), ] for old, new in subs: assert old in s, old s = s.replace(old, new) open(p, 'w').write(s) print("ok") EOF source .venv/bin/activate && python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -3, source .venv/bin/activate && python - <<'EOF' p = 'src/research_data/brain/store.py' s = open(p).read() subs = [ ("citation.retrieved_at,", "_to_db_ts(citation.retrieved_at),"), ("citation.created_at,", "_to_db_ts(citation.created_at),"), ("spec.created_at,\n spec.approved_by,\n spec.approved_at,", "_to_db_ts(spec.created_at),\n spec.approved_by,\n _to_db_ts(spec.approved_at),"), ("[SpecStatus.APPROVED.value, approved_by, approved_at, spec_id],", "[SpecStatus.APPROVED.value, approved_by, _to_db_ts(approved_at), spec_id],"), ("run.as_of,\n run.created_at,", "run.as_of,\n _to_db_ts(run.created_at),"), ("decision.decided_by,\n decision.created_at,", "decision.decided_by,\n _to_db_ts(decision.created_at),"), ("link.relation, link.created_at]", "link.relation, _to_db_ts(link.created_at)]"), ] for old, new in subs: assert old in s, old s = s.replace(old, new) open(p, 'w').write(s) print("ok") EOF python -m pytest tests/test_brain_store.py tests/test_brain_loop.py -q 2>&1 | tail -3, source .venv/bin/activate && python -m pytest tests/test_factors_math.py tests/test_factors_engine.py -q 2>&1 | tail -8, source .venv/bin/activate && python - <<'EOF' from datetime import date from tests.synthetic import make_price_records from research_data.factors.momentum import twelve_minus_one_return AS_OF = date(2026, 6, 30) for sym, drift, vol in [("VOO",0.0004,0.008),("AAPL",0.0020,0.012),("MSFT",0.0002,0.004),("TSLA",-0.0010,0.035)]: recs = make_price_records(sym, end=AS_OF, sessions=320, base_price=100.0, daily_drift=drift, daily_vol=vol, asset_type="etf" if sym=="VOO" else "equity", exchange="NYSE") closes = [r.adjusted_close for r in recs] print(sym, round(twelve_minus_one_return(closes), 4)) EOF, source .venv/bin/activate && python - <<'EOF' from datetime import date from tests.synthetic import make_price_records from research_data.factors.momentum import twelve_minus_one_return from research_data.factors.safety import realized_volatility_annualized AS_OF = date(2026, 6, 30) for seed in range(3, 15): recs = make_price_records("TSLA", end=AS_OF, sessions=320, base_price=200.0, daily_drift=-0.0010, daily_vol=0.035, seed=seed) closes = [r.adjusted_close for r in recs] print(seed, round(twelve_minus_one_return(closes),4), round(realized_volatility_annualized(closes),3)) EOF, source .venv/bin/activate && python -m pytest tests/test_factors_math.py tests/test_factors_engine.py -q 2>&1 | tail -3, cat >> config/assets.toml <<'EOF' [assets.BRKB] # Canonical symbol is letters-only (BRKB); provider clients map to their own # punctuation (Polygon "BRK.B", SEC "BRK-B"). symbol = "BRKB" asset_type = "equity" name = "Berkshire Hathaway Inc. Class B (BRK.B)" exchange = "NYSE" currency = "USD" benchmark_symbol = "VOO" [assets.JPM] symbol = "JPM" asset_type = "equity" name = "JPMorgan Chase & Co." exchange = "NYSE" currency = "USD" benchmark_symbol = "VOO" [assets.COST] symbol = "COST" asset_type = "equity" name = "Costco Wholesale Corporation" exchange = "NASDAQ" currency = "USD" benchmark_symbol = "VOO" [assets.TSLA] symbol = "TSLA" asset_type = "equity" name = "Tesla, Inc." exchange = "NASDAQ" currency = "USD" benchmark_symbol = "VOO" EOF source .venv/bin/activate && python -c " from research_data.config import load_config c = load_config() assert len(c.universe.symbols) == 14, c.universe.symbols assert set(c.universe.symbols) == set(c.universe.assets), 'symbols/assets mismatch' print('universe ok:', c.universe.symbols) " && python -m pytest tests/test_provider_registry.py tests/test_property_provider_registry.py -q 2>&1 | tail -2, source .venv/bin/activate && python -c " from research_data.config import load_config c = load_config() assert len(c.universe.symbols) == 14, c.universe.symbols assert set(c.universe.symbols) == set(c.universe.assets), 'symbols/assets mismatch' print('universe ok, 14 symbols') " && python -m pytest -q 2>&1 | tail -2, source .venv/bin/activate && python -m pytest tests/test_fundamentals.py -q 2>&1 | tail -3, source .venv/bin/activate && python - <<'EOF' p = 'src/research_data/brain/__init__.py' s = open(p).read() s = s.replace("from research_data.brain.loop import (\n BrainLoopError,\n gate_sequence_passes,", "from research_data.brain.loop import (\n BrainLoopError,\n gate_sequence_passes,\n latest_gate_batch,") s = s.replace(' "gate_sequence_passes",', ' "gate_sequence_passes",\n "latest_gate_batch",') open(p, 'w').write(s) print("ok") EOF python -m pytest tests/test_gates.py -q 2>&1 | tail -5, source .venv/bin/activate && python -m pytest tests/test_paper.py -q 2>&1 | tail -6, source .venv/bin/activate && python -m pytest tests/test_paper.py tests/test_kronos_reserved.py tests/test_closed_loop.py -q 2>&1 | tail -8, grep -n "^#" "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/TradingView/RESEARCH.md" | head -40, source .venv/bin/activate && python -m pytest -q 2>&1 | tail -3, git log --oneline -8 && git status --short | head -20 && ls src/research_data src/research_data/providers && ls tests | head -40, cd /home/anant_gupta/projects/hub/tradingview echo "== execution language in src (BUY/SELL as labels, guaranteed, risk-free) ==" grep -rniE '"(buy|sell)"|'"'"'(buy|sell)'"'"'|\bguaranteed\b|risk[- ]free' src/ --include="*.py" | grep -viv "buy-and-hold\|buy_hold\|buying winners\|selling losers" || echo "CLEAN" echo "== PM / out-of-scope asset classes in src ==" grep -rniE 'kalshi|polymarket|prediction.market|option[s]? chain|futures|crypto|margin|leverage|intraday|tick data' src/ --include="*.py" || echo "CLEAN" echo "== Kronos inference imports ==" grep -rniE 'torch|transformers|huggingface|from_pretrained|onnx' src/ --include="*.py" || echo "CLEAN" echo "== broker SDKs ==" grep -rniE 'alpaca|ibkr|interactive.?brokers|robinhood|ccxt|broker' src/ --include="*.py" || echo "CLEAN" echo "== .env gitignored ==" git check-ignore .env && echo "ignored OK" echo "== potential secrets in tracked+untracked source ==" grep -rniE '(api_key|token|secret)\s*=\s*["'"'"'][A-Za-z0-9]{12,}' src/ tests/ config/ || echo "CLEAN", cd /home/anant_gupta/projects/hub/tradingview for f in evidence.py benchmark.py cli.py __main__.py providers/polygon.py; do echo "== $f =="; head -12 src/research_data/$f | sed -n '1,12p'; done echo "== tasks.md checkbox summary =="; grep -c "\[x\]" .kiro/specs/data-ingestion-foundation/tasks.md; grep -c "\[ \]" .kiro/specs/data-ingestion-foundation/tasks.md || true
- Tool call tally: Bash (27), Edit (17), mcp__jarvis__vault_append (1), mcp__jarvis__vault_patch (6), mcp__jarvis-fs__list_allowed_directories (1), Read (21), TaskCreate (10), TaskUpdate (17), ToolSearch (4), Write (48)

