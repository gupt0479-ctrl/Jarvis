---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - projects
  - reference
source_url: https://github.com/public-apis/public-apis
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Public APIs

**GitHub:** [public-apis/public-apis](https://github.com/public-apis/public-apis) | **Stars:** 437k | **Updated:** actively maintained via community PRs

## What it is
Collective index of free public APIs organized by category (Finance, Science, Weather, Music, Games, Security, etc.). Each entry shows the API name, description, auth method (apiKey / OAuth / None), HTTPS support, and CORS status. ~1,400 APIs listed.

## How Anant uses it
First stop when a project needs external data and building a scraper would be overkill. For the trading project: Finance category covers financial data APIs beyond Yahoo Finance. For Jarvis: News and Weather categories for daily brief enrichment. For interview prep projects: anything in the Games or Open Data categories for building demo apps quickly.

Search with `Ctrl+F` in the README for the domain, check auth method (None = easiest to start), then evaluate the API docs.

## How to install / run it (Windows)
No install — it's a README. Use GitHub's search or `Ctrl+F` in the browser.

## Caveats / current state
Actively maintained. Some listed APIs go offline without warning — always test before building on one. "No Auth" APIs are frequently rate-limited without documentation. The Finance section has solid entries but many require registration even when listed as apiKey (free tier key).

**Verdict: yes** — first stop when a new project needs external data. Saves 30 minutes of searching for an API that may already be catalogued here.

## Connects to
- [[40_Resources/CS/Repos]]
