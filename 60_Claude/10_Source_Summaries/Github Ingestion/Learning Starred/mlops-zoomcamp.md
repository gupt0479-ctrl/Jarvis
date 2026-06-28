---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/DataTalksClub/mlops-zoomcamp
notes:
  - "[[40_Resources/CS/Repos]]"
---
# MLOps Zoomcamp

**GitHub:** [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | **Stars:** 14.9k | **Updated:** June 2026

## What it is
A free 9-week course (DataTalksClub) on productionizing ML models: intro to MLOps maturity model → experiment tracking with MLflow (model registry, run comparison) → pipeline orchestration → deployment (Flask web service, AWS Kinesis/Lambda for streaming, batch scoring) → monitoring (Prometheus + Evidently + Grafana) → best practices (unit/integration tests, GitHub Actions CI/CD, Terraform). Uses NYC taxi dataset as the running example.

## How Anant uses it
- **Module 2 (MLflow experiment tracking)**: start using this as soon as TradingAgents experiments begin. MLflow gives you a model registry, run comparison, and artifact versioning that prevents "which checkpoint was the good one?" problems. Set this up before you have too many experiments to track manually.
- **Module 4 (deployment)**: the Flask + Docker path maps directly to deploying a trading signal model endpoint. The streaming deployment with Kinesis/Lambda is the pattern for low-latency signal generation if the trading AI needs real-time inference.
- **Module 5 (monitoring with Evidently)**: applies when you need to detect whether a deployed trading model is degrading due to market regime changes — the data drift detection patterns are directly applicable.

Skip Module 3 (orchestration) for now — Kestra is covered in LLM Zoomcamp and Data Engineering Zoomcamp, no need to revisit here.

## How to install / run it (Windows)
Self-paced only in 2026 — no live cohort planned this year. Register at airtable.com/shrCb8y6eTbPKwSTL to be notified if a live cohort runs again. Prerequisites: Python, Docker basics, ML experience (recommend completing ML Zoomcamp first), ~1 year programming experience.

## Caveats / current state
No live cohort in 2026 (confirmed in README: "We don't plan to run a live cohort in 2026"). Self-paced materials are fully available and current (last commit June 2026). The monitoring module uses Evidently and Grafana — both require some Docker setup on Windows (WSL2 recommended for the Grafana/Prometheus stack). The Terraform module in Module 6 is AWS-specific.

## Connects to
[[40_Resources/CS/Repos]]
