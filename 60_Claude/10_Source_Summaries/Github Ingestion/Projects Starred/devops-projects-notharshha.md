---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - devops
  - learning
source_url: https://github.com/NotHarshhaa/DevOps-Projects
notes:
  - "[[40_Resources/CS/Repos]]"
---
# DevOps Projects (NotHarshhaa)

**GitHub:** [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | **Stars:** ~50k | **Updated:** actively maintained

## What it is
50+ real-world DevOps project implementations with full solutions across AWS, Docker, Kubernetes, Jenkins, Terraform, and Ansible. Organized by difficulty and technology. Each project includes architecture diagrams, step-by-step instructions, and working code — not just prompts to figure it out.

## How Anant uses it
Reference when the trading project or Jarvis infrastructure needs a deployment pattern (containerization, CI/CD, monitoring). Rather than designing a Docker + GitHub Actions pipeline from scratch, check if an equivalent project already exists here. The AWS + Kubernetes projects are the most directly applicable for productionizing Python agent pipelines.

## How to install / run it (Windows)
No local install — it's a project collection. Each subfolder has its own setup instructions. Most projects assume Linux/cloud environments; WSL2 or a cloud VM is needed for the Kubernetes/Docker projects on Windows.

## Caveats / current state
Actively maintained. Projects are mostly AWS-centric — Azure and GCP coverage is thin. Some solutions are more tutorial than production-grade. The Kubernetes projects require a real cluster (EKS or Minikube + WSL2) to run end-to-end.

**Verdict: yes** — reference when Anant needs to deploy or containerize something. Saves design time on common infrastructure patterns.

## Connects to
- [[40_Resources/CS/Repos]]
