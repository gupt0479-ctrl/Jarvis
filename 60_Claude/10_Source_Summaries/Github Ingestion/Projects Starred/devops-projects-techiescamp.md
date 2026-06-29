---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - devops
  - learning
source_url: https://github.com/techiescamp/devops-projects
notes:
  - "[[40_Resources/CS/Repos]]"
---
# DevOps Projects (techiescamp)

**GitHub:** [techiescamp/devops-projects](https://github.com/techiescamp/devops-projects) | **Stars:** 2.1k | **Updated:** May 2026 (active)

## What it is
10 step-by-step AWS DevOps projects from beginner to advanced, each with full Terraform/Ansible/Packer automation scripts. Projects: Jenkins HA on AWS, Consul service discovery, scalable Java app deployment, Prometheus observability stack, AWS VPC automation, AWS Client VPN, Fargate app deployment, GitHub Actions OIDC AWS integration, Route53 private hosted zones.

The key difference from NotHarshhaa: these have working automation scripts (HCL/Jinja/Shell) that provision real AWS infrastructure, not just instructional writeups.

## How Anant uses it
Lower priority than NotHarshhaa for now — the projects are AWS-heavy and Java-focused, neither of which matches current projects (Python-based trading/Jarvis). The Prometheus observability stack (project 04) and GitHub Actions OIDC AWS (project 09) are the most transferable to Python agent deployments.

Use if a project needs to be deployed to AWS and the pattern is covered here.

## How to install / run it (Windows)
WSL2 required for Terraform/Packer. AWS free-tier credits cover most projects (destroy after practicing to avoid costs). The GitHub Actions OIDC project (09) can be run entirely in CI without local setup.

## Caveats / current state
10 projects only (much smaller than NotHarshhaa). Infrastructure code is 3 years old in some projects — Terraform syntax and AWS resource APIs may have changed. Kubernetes certifications promotion in the README is just monetization; ignore it.

**Verdict: partial** — Prometheus stack (04) and GitHub Actions OIDC (09) are worth reading. Otherwise defer to NotHarshhaa for breadth.

## Connects to
- [[40_Resources/CS/Repos]]
- [[60_Claude/10_Source_Summaries/Github Ingestion/Projects Starred/devops-projects-notharshha]]
