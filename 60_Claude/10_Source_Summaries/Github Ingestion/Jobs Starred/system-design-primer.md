---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - interview-prep
  - system-design
source_url: https://github.com/donnemartin/system-design-primer
notes:
  - "[[40_Resources/CS/Repos]]"
---
# System Design Primer

**GitHub:** [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | **Stars:** 355k | **Updated:** Mar 19, 2026

## What it is
A guide to large-scale system design for interview purposes — covers scalability, availability, consistency, CAP theorem, DNS, CDNs, load balancers, caching (Redis), databases (SQL vs NoSQL, sharding), message queues, and distributed systems concepts. Includes worked design examples (URL shortener, Twitter feed, etc.) and an Anki flashcard deck in the `resources/` folder.

## How Anant uses it
System design rounds typically appear at new-grad and senior-level interviews, not at sophomore internship OAs. So this is a **prep-ahead resource**, not an immediate priority. Specific use:

- **Vocabulary building now:** Read the "Performance vs scalability" and "Latency vs throughput" sections once. When you see terms like "horizontal scaling" or "sharding" in tech blogs or project descriptions, you'll know what they mean. This matters more for AI/ML roles where you might discuss inference infrastructure.
- **Pre-interview for backend/infra internships:** If you apply to roles explicitly labeled "Backend" or "Infrastructure" at mid-size companies, read the "How to approach a system design interview" section and one or two example designs (URL shortener is the canonical starter) the week before.
- **Anki deck for passive review:** The `resources/` folder has a system design Anki deck. Import it to your Anki and add it to a low-priority review deck. You'll absorb the vocabulary over time without active study.

For a sophomore targeting SWE/AI internships at companies like Dropbox, Ramp, or Jane Street, system design questions will not appear in interviews. Deprioritize this until junior year unless a specific role asks for it.

## How to install / run it (Windows)
Read the README.md directly on GitHub (donnemartin/system-design-primer). For the Anki deck: download `system_design.apkg` from the `resources/` folder, open Anki on Windows, File → Import.

## Caveats / current state
- Minor maintenance updates (link fixes, translation corrections) happen occasionally — last content-meaningful update is effectively 2020–2021. The core concepts haven't changed so this is fine.
- The worked examples (design Pastebin, design Amazon's sales rank) reflect pre-LLM architecture; modern ML-serving infrastructure isn't covered.
- Not opinionated about cloud-provider specifics (AWS/GCP) — you'll need to supplement with provider docs when working on actual projects.
- Also relevant to Learning track in this vault — cross-listed because the concepts appear in both interview prep and distributed systems coursework.

## Connects to
[[40_Resources/CS/Repos]]
