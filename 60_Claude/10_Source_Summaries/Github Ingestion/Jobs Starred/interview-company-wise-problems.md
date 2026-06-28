---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - interview-prep
  - leetcode
source_url: https://github.com/liquidslr/interview-company-wise-problems
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Interview Company-wise Problems

**GitHub:** [liquidslr/interview-company-wise-problems](https://github.com/liquidslr/interview-company-wise-problems) | **Stars:** 25.8k | **Updated:** Jun 25, 2026

## What it is
One folder per company, each containing a CSV of LeetCode problem IDs tagged to that company by LeetCode's own company-tag system. Covers AMD, AQR, Accenture, Accolite, and dozens of others alphabetically — a scraped and cleaned version of what LeetCode Premium shows behind a paywall.

## How Anant uses it
Use this exactly one week before an OA or technical interview at a known company. The workflow:
1. Navigate to the folder for that company (e.g., `/Google`, `/Jane Street`, `/Two Sigma`)
2. Open the CSV — it lists problem slugs or IDs
3. Filter by frequency if the CSV includes it; solve the top 10–15 by frequency
4. This gives you the specific problem surface area for that company vs. grinding random LeetCode

This is most valuable for SWE and quant roles where companies have known patterns (e.g., Jane Street/Citadel lean on DP and combinatorics; FAANG leans on trees/graphs/sliding window).

Do not use this as a primary study resource — it's a final-week targeting tool, not a curriculum.

## How to install / run it (Windows)
No install. On GitHub, navigate to the company folder directly. Download or open the CSV in Excel/Sheets. Sort by frequency column descending. Alternatively, clone the repo locally: `git clone https://github.com/liquidslr/interview-company-wise-problems` and use VS Code to browse folders.

## Caveats / current state
- Actively maintained — last update Jun 25, 2026, only 11 total commits (maintainer does batch updates, not continuous ones).
- The description says "Updated as of 20 June, 2025" but the actual commit is June 2026 — the README description is stale.
- Company tags in LeetCode Premium are crowd-sourced and can be inaccurate; treat the list as signal, not ground truth.
- Companies with fewer interviews in the dataset have noisier tags.
- No difficulty filtering built in — need to cross-reference LeetCode directly to sort by easy/medium/hard.

## Connects to
[[40_Resources/CS/Repos]]
