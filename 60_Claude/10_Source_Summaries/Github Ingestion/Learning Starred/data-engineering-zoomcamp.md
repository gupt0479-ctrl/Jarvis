---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/DataTalksClub/data-engineering-zoomcamp
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Data Engineering Zoomcamp

**GitHub:** [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | **Stars:** 42.8k | **Updated:** June 2026

## What it is
A free 9-week course (DataTalksClub) covering the production data pipeline stack end-to-end: Docker + Terraform → workflow orchestration (Kestra) → data warehousing (BigQuery) → analytics engineering (dbt) → batch processing (Spark) → streaming (Kafka/Flink). All materials run on cloud free tiers. Active through June 2026 (1,237 commits).

## How Anant uses it
Not an active focus — this is background knowledge, not a near-term priority. The one scenario where this becomes directly relevant: if TradingAgents or Kronos needs to ingest streaming market data at scale with reliability guarantees. At that point:
- **Module 1 (Docker + Terraform)**: prerequisites already partially covered through ML Zoomcamp and MLOps Zoomcamp.
- **Module 6 (Kafka/Flink streaming)**: the entry point for reliable real-time market data ingestion — relevant when Polymarket MCP or TradingView MCP feeds need to be archived and replayed.

Otherwise, skip until the trading AI's data volume or reliability requirements justify the overhead.

## How to install / run it (Windows)
Self-paced at any time via GitHub + YouTube playlist. 2026 cohort schedule not confirmed. Free; minimal cloud costs ($0–5 for exercises using free tier GCP/AWS).

## Caveats / current state
Prerequisites are steeper than other Zoomcamps: assumes comfort with SQL, Python, and command line. The cloud tools (BigQuery, GCS, AWS) require account setup. Kafka module requires some infrastructure work. This is the most operationally complex of the DataTalksClub courses and takes more than 9 weeks for most self-paced learners.

## Connects to
[[40_Resources/CS/Repos]]
