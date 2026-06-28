---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/DataTalksClub/machine-learning-zoomcamp
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Machine Learning Zoomcamp

**GitHub:** [DataTalksClub/machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) | **Stars:** 13.4k | **Updated:** June 2026

## What it is
A free ~4-month course (DataTalksClub) that teaches ML engineering rather than ML theory: regression and classification with scikit-learn → model evaluation → deployment with Flask in Docker → decision trees and ensemble methods → neural networks (TensorFlow/Keras) → model serving with Kubernetes and TF-Serving → serverless deployment (AWS Lambda). The emphasis throughout is on shipping a model as an endpoint, not on the math.

## How Anant uses it
The deployment modules are the most immediately applicable for TradingAgents/Kronos:
- **Module 5 (Flask + Docker deployment)**: the first step to exposing a trained trading model as a prediction API that Kronos can call. Do this module when you have a trained model and need to wrap it in an API.
- **Module 9 (Kubernetes + TF-Serving)**: relevant if the trading model needs to scale or handle concurrent requests from multiple agents.
- **Module 10 (Serverless with Lambda)**: worth reading if you want low-cost inference on AWS without managing a server.

The scikit-learn modules (regression, classification, evaluation) are worth doing if you haven't trained models with Python before — they cover the practical workflow that MLOps Zoomcamp assumes you already know.

## How to install / run it (Windows)
Self-paced at any time. The 2025 cohort ran September–December 2025; 2026 cohort schedule not confirmed. All exercises run locally or on small cloud instances. ML Zoomcamp is listed as a prerequisite for MLOps Zoomcamp.

## Caveats / current state
Actively maintained (updated June 25 2026). The course is designed for engineers, not researchers — it does not cover deep learning theory or research models. If you need to understand transformer internals or training dynamics, LLM Zoomcamp or a separate resource is more appropriate. This course is specifically about the engineering workflow: train, evaluate, deploy, monitor.

## Connects to
[[40_Resources/CS/Repos]]
