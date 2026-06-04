---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - plan
  - summer
  - ml
  - linear-algebra
  - statistics
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[01 - Daily Operating System]]"
  - "[[06a - ML Fundamentals Progress]]"
  - "[[ML_Foundations]]"
  - "[[CSCI 2033 Board]]"
  - "[[MATH 2230 Board]]"
  - "[[04 - Summer Courses Ops]]"
  - "[[03 - Monthly & Phase Map]]"
next: "[[06a - ML Fundamentals Progress]]"
---

# ML Fundamentals (CSCI 2033 + MATH 2230)

## 1. Strategic summary

CSCI 2033 supplies the **linear algebra** of ML; MATH 2230 supplies the **probability & statistics**. Together they are the **math base for an ML-engineer path** — not a full replay of 2033 and not exam cram. The spine is **curated**: only the ML-fundamentals subset of 2033 (sections 1–6 of [[ML_Foundations]]), studied in prerequisite order with no skipped dependencies. PageRank and graph ML (2033's endgame, [[ML_Foundations]] §7) are **deferred to a late-summer deep pass**, not skimmed now. Where 2033 and 2230 topics overlap, one study block covers both.

## 2. Two-track model

| Track | Source | Summer role | Cadence |
|-------|--------|-------------|---------|
| **A — 2033 ML spine** | `Concepts_old/` + [[ML_Foundations]] | Curated, ordered LA→ML sequence | 30–45 min/day |
| **B — 2230 live course** | `MATH 2230 - Calendar` + syllabus | WebAssign/quizzes (grade in [[04 - Summer Courses Ops]]) + **ML bridge notes** | per course week |

**Integration rule:** when a Track B topic aligns with a Track A unit (see the bridge table in §4), the **same study block** covers both. Grade mechanics for 2230 stay in [[04 - Summer Courses Ops]]; this file owns only the ML bridge.

## 3. ML fundamentals spine (2033) — in-scope only

Ordered units, each mapped to a **real `Concepts_old/` filename**. Study in order; prerequisites are explicit. Output and done-definition per unit. Track in [[06a - ML Fundamentals Progress]].

Path prefix: `10_Areas/UMN/Previous Classes/CSCI/CSCI 2033/Concepts_old/`

| # | ML_Foundations § | Primary vault file(s) | Prereq | Active output | Done when | 2230 bridge |
|---|---|---|:---:|---|---|---|
| 1 | §1 | `Vectors, Linear Functions, and the Regression Model.md` | — | 3 problems: dot product, linear function eval | vector ops from memory | Descriptive stats, mean |
| 2 | §1 | `Norms, Distance, Standard Deviation, and Angles.md` | 1 | derive ‖x‖, distance, cosine | compute norm/angle by hand | Variance, std dev |
| 3 | §1–2 | `Linear Independence, Bases, Orthonormality, and Matrices.md` | 1 | check independence; build orthonormal set | explain span/basis | — |
| 4 | §2 | `Geometric Transformations, Graphs, Linear Equations, and the Matrix Class.md` *(LA core only; defer graph subsection → Endgame)* | 3 | matrix as transform; 2 products | matrix-vector by hand | — |
| 5 | §2 | `Linear Systems, Inverses, Pseudo-Inverse, and Polynomial Interpolation.md` | 4 | solve a system; pseudo-inverse meaning | when inverse exists vs pseudo | — |
| 6 | §2 | `Matrix–Matrix Products, QR Factorization, and Householder Reflectors.md` *(QR in-scope; PageRank-as-dynamical-system subsection → defer)* | 5 | Gram–Schmidt QR on 3×3 | QR by hand, why numerically stable | — |
| 7 | §2 | `Vectors, Linear Functions, and the Regression Model.md` + `Least Squares and Feature Engineering.md` | 6 | fit least-squares line; min ‖Aβ−b‖² | regression as projection | **Estimation, MLE** (same week if possible) |
| 8 | §2 | `Least Squares and Feature Engineering.md` | 7 | add polynomial features; show overfit | train vs test U-curve | Bias-variance intuition |
| 9 | §3 | `Least Squares Classifiers, Optimization, and Gradient Descent.md` | 7 | LS classifier, ±1 labels, threshold | decision boundary = hyperplane | **Conditional prob, Bayes** |
| 10 | §5 | `Least Squares Classifiers, Optimization, and Gradient Descent.md` | 9 | code gradient descent on a loss | role of step size; SGD vs GD | **Expectation of loss, variance** (bias-variance week) |
| 11 | §6 | `Singular Value Decomposition and Eigenfaces.md` | 6 | SVD of small matrix; rank-k approx | top-k singular vectors meaning | — (LA-led) |
| 12 | §6 | `Singular Value Decomposition and Eigenfaces.md` + `Matrix_Operations_Reference.md` | 11 | PCA = de-mean + SVD; project to k dims | PC = variance direction | **Joint distributions, covariance matrix** |
| 13 | §4 | `Clustering.md` | 2 | k-means assign→update loop | why it converges | — |
| 14 | §4 | `Clustering, K-n.md` | 2, 13 | k-NN classifier; cosine NN | parametric vs non-parametric | — |

Reference on demand (not sequential): `Matrix_Operations_Reference.md`, plus `Extra notes/` (`Matrix Tools.md`, `Vector Class.md`, `Jacobi Method.md`, `Complexity.md`). Do **not** assign a full reread of any `Week - *.md`.

### Explicitly DEFER — Endgame (late summer, deep pass not skim)

- `Concepts_old/Graphs_and_PageRank.md`
- `Concepts_old/The Google PageRank Algorithm.md`
- Graph/PageRank subsections inside units 4 and 6 above
- [[ML_Foundations]] **§7 (PageRank → Graph ML)**

**Endgame standard (when reached):** implement **PageRank power iteration** from scratch; adjacency-matrix + random-walk drills; column-stochastic / Google matrix $G=\alpha S+\frac{1-\alpha}{n}J$; then link forward to GNN / Node2Vec study. Full detail — this is the one part you learn deeply at the end, not a checkbox. Tracked as a locked queue in [[06a - ML Fundamentals Progress]].

## 4. 2033 ↔ 2230 bridge table (required)

When the 2230 topic lands in its course week (dates from [[MATH 2230 - Calendar]]), pair it with the matching spine unit in one block.

| 2033 / ML unit | MATH 2230 topic (course week) | Combined study action |
|----------------|-------------------------------|------------------------|
| U1–2 Vectors, norms, distance | Descriptive stats, expectation (Ch 1–3, Wk 1–3) | Compute mean/variance as vector operations |
| U10 Gradient descent / loss | Discrete RVs, expectation & variance (Ch 3, Wk 2–3) | Frame loss as an expectation; bias-variance |
| U9 Classification thresholds | Continuous RVs, distributions, Bayes (Ch 4, Wk 3–4) | Gaussian/Bernoulli as label-noise models |
| U11–12 SVD / PCA | Joint distributions, covariance (Ch 5–6, Wk 4–5) | Covariance matrix → principal components |
| U7 Least squares / regression | Estimation, MLE (Ch 7–8, Wk 5–6) | Show MLE under Gaussian noise = least squares |
| (evaluation) | Hypothesis testing, CIs (Ch 9, Wk 7) | Significance of a metric gap between models |
| U7–8 Regression | Linear regression (Ch 12, Wk 7) | 2230 confirms the regression you built in LA |
| U12 PCA / variance | ANOVA / variance decomposition (Ch 14, Wk 8) | Variance explained per component |

## 5. MATH 2230 ML concept notes

Keep the **≥1 note/week** rule. **Chosen path:** `20_Progress/Degree/MATH 2230/Concepts/` (co-located with the course board, per AGENTS routing for course concept notes; the board's `## Concept notes` MOC links them).

Each note, four parts: **definition · ML use · link to the 2033 spine unit · one worked example.** Sync the topic to the current course week in [[MATH 2230 - Calendar]].

## 6. Vault hygiene

- **Primary read:** `Concepts_old/` (human-refined — the study spine above).
- `Concepts_new/` (`Week_1_and_2.md` … `Week_11_to_13.md`): **supplemental only**.
- Do **not** assign reading all `Week - *.md` (timeline only).
- Any concept-note merge/refine follows `.claude/skills/organize-csci2033.md` (never delete; weekly files append-only) and is **out of scope this session**. One optional pilot merge is logged as backlog in [[06a - ML Fundamentals Progress]], not done now.

## 7. Phase timing (high level — see [[03 - Monthly & Phase Map]])

- **Dubai:** complete spine **units 1–12** (LA core through SVD/PCA).
- **Bangalore:** finish **units 13–14** + all 2230 bridge notes as the course runs.
- **Last 2–3 weeks before Sept 1:** **Endgame** — PageRank / graph ML deep pass.

Tracking and the Endgame locked-queue live in [[06a - ML Fundamentals Progress]].
