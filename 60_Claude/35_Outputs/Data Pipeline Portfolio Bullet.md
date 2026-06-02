---
type: output
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - output
track:
  - systems
  - career
output_kind: portfolio-bullet
source_concepts:
  - "[[MongoDB Data Model and Filters]]"
  - "[[60_Claude/20_Distilled_Notes/Portfolio Strategy]]"
---

# Data Pipeline Portfolio Bullet

## Portfolio Bullet

**Data Pipeline & Storage Design (MongoDB + Kafka)**

Designed and worked with a document-oriented storage layer for astronomical alert data, where query patterns drove schema decisions rather than code structure. Implemented filter evaluation on enriched records using cross-match data, derived quantities, and classifier outputs — demonstrating that post-enrichment filtering is significantly more powerful than raw-data filtering.

**Stack**: MongoDB, Kafka, Rust (serde/BSON), Docker

## Quantified Impact

- Worked with 5+ entity types (alerts, objects, images, filters, catalogs) in a document database
- Filter versioning enabled reproducible scientific results across pipeline changes
- Architecture pattern transfers directly to feature stores and ML experiment tracking
