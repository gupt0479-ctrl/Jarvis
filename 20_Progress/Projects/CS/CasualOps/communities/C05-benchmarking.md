# C05 — Benchmarking / Tier Scoring

**Community 5** — 28 nodes, cohesion 0.13

Deterministic quality metrics for each HiveMind agent tier. No LLM — scores are computed from artifact counts and content structure.

## Key Nodes

`score_agent_tiers()`, `Score whether parent agents produced complete child tasks.`, `Score child memo output using bus count and a single memo sample.`, `Score child-agent memo completeness.`

## What This Code Does

`score_agent_tiers()` is called by `engine.run_hivemind()` to produce `agent_tier_metrics` in the frontend artifact. Scores the orchestrator, parent, child, evaluator, and causal tiers based on completeness (did it produce the expected outputs?) and quality (memo length, evidence_needs specificity, etc.).

## Source File

`src/benchmarking.py`

## Related Notes

- [[pipeline/00-overview|Pipeline Overview]] — where tier metrics appear in the artifact
