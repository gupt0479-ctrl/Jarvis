---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - cowork
  - prompt
  - csci-2033
  - csci-4041
  - math-2230
notes:
  - "[[00 - CoWork Prompt — Summer OS]]"
  - "[[00b - CoWork Entry Prompt]]"
  - "[[05 - LeetCode & CSCI 4041]]"
  - "[[06 - ML Fundamentals (2033 + 2230)]]"
  - "[[00 - Summer Plans Index]]"
  - "[[ML_Foundations]]"
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[CSCI 2033 Board]]"
  - "[[MATH 2230 Board]]"
---

# CoWork Prompt — Deepen 05 & 06 (CSCI 4041 + ML Track)

**Scope of this session:** Rewrite **`05 - LeetCode & CSCI 4041.md`** and **`06 - ML Fundamentals (2033 + 2230).md`** into **concrete summer study systems** grounded in the actual vault. **Do not** redesign daily workflow (`01`), weekly ops (`02`), or other plan files unless a one-line cross-link is needed.

**How to use:** Attach this file + paste the entry block from [[00b - CoWork Entry Prompt]] (Obsidian-first: use `jarvis` MCP, not `jarvis-fs`). Obsidian must be running.

---

## COPY FROM HERE

```markdown
# MISSION — Summer study foundations (files 05 & 06 only)

You are my **curriculum architect** for two parallel summer tracks. Your job is to **replace** the thin drafts in:

- `10_Areas/Life/Plans/05 - LeetCode & CSCI 4041.md`
- `10_Areas/Life/Plans/06 - ML Fundamentals (2033 + 2230).md`

with **detailed, mistake-free study systems** mapped to **real vault files**. Daily workflow comes **later** — do not rewrite `01 - Daily Operating System.md` except adding wikilinks to new artifacts you create.

**Read the vault folders in depth before writing** (listed below). Search before create. Follow `AGENTS.md`, `HUMAN_WRITING.md`, `CLAUDE.md`. Patch by heading where possible.

---

## NON-NEGOTIABLE CONSTRAINTS

1. **No MCP/tool setup**, no platform comparison, no GitHub stars triage this session.
2. **No full CSCI 2033 replay** — only **machine learning fundamentals** from that course. Do not assign reading every week file or every concept file.
3. **PageRank + graphs (2033 endgame)** — schedule for **late summer / Phase 2 deep pass**, not the ML-fundamentals core. User will learn these **in detail at the end**; label them **Deferred — Endgame** in 06.
4. **CSCI 4041 = entire summer flagship** — LeetCode + professor projects + concept mastery + **company-based** interview prep. Nothing half-assed.
5. **MATH 2230 + CSCI 2033 studied together** where topics overlap — one integrated track in 06, not two silos.
6. **Evidence-based plans** — every unit names vault source paths, outputs, done definitions, and review hooks.
7. Use **`jarvis` Obsidian MCP** for reads/writes. Do not use `jarvis-fs` unless Obsidian MCP is down (say so once).

---

## USER INTENT (preserve every point — do not drop)

### CSCI 2033 (linear algebra → ML)

- Relearn **ML fundamentals only** from CSCI 2033 — **not** the whole course again.
- Vault has **many files** (`Concepts_old/`, `Concepts_new/`, `Week - *.md`, `Extra notes/`) — we cannot touch every concept this summer. **Curate** a ML-fundamentals spine with explicit **in-scope** vs **deferred** lists tied to real filenames.
- Anchor map: `10_Areas/UMN/Previous Classes/CSCI/CSCI 2033/Concepts_old/ML_Foundations.md` (sections 1–6 = summer core; section 7 PageRank + graph ML = **endgame**).
- **Relate 2033 to MATH 2230** (probability & statistics, calculus-based, summer 2026) — study **through both together** when topics align (e.g. covariance ↔ PCA, distributions ↔ classification noise, MLE ↔ regression).
- Goal: **basics of ML** for an **ML engineer path** — not exam cram for 2033.
- **Cover ground carefully** — ordered prerequisites, no skipped dependencies in the ML spine.
- Respect `.claude/skills/organize-csci2033.md` if merging/refining concept notes (never delete; weekly files append-only).

### CSCI 4041 (algorithms — internship core)

- **Spend the entire summer perfecting** this course with **LeetCode** and **professor projects**.
- Notes are **concrete** but user has **not overviewed** them (too much at once). Fix with **structured pass**, not “read everything.”
- **≥5 LeetCode problems/day** stays (already in 05) — enhance with **tracking**, **company tags**, and **interview revision**.
- **Company-based interview questions primarily** — use:
  - `40_Resources/CS/Repos.md` (leetcode-companywise, interview-company-wise-problems)
  - `60_Claude/10_Source_Summaries/Github Ingestion/GitHub Stars — How Anant Uses Each Repo.md` (company-wise section)
- **Core class for internships** — every concept internalized, **never forget**, **easy revision** before interviews.
- Include **professor projects**: Midterm (AVL tree — chosen), Final (Maze — chosen); paths under `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Midterm Project/` and `Final Project/`.
- Map to **14-week structure** in `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/DSA.md` (`## LeetCode / Weekly Plan` + 15 concept MOC items).
- **Not wasting time** — each week: vault concept + LC problems + optional project milestone.

### Sequencing

- **This session = concrete plans for 05 and 06 only.**
- Daily workflow adjustments happen **after** these files are solid.

---

## VAULT INVENTORY (you must read these)

### CSCI 2033 — `10_Areas/UMN/Previous Classes/CSCI/CSCI 2033/`

| Area | Files (44 total) | Role |
|------|------------------|------|
| **Board** | `CSCI 2033 Board.md` | Archived class; points to Final, Midterm |
| **ML map** | `Concepts_old/ML_Foundations.md` | **Primary curriculum map** 2033 → ML |
| **Concepts_old** (15) | See list below | Human-refined; **prefer for study spine** |
| **Concepts_new** | `Week_1_and_2.md` … `Week_11_to_13.md` | Supplement; merge per organize-csci2033 |
| **Week notes** | `Week - 1 & 2.md` … `Week - 12.md` | Timeline only — **do not assign full reread** |
| **Extra** | `Matrix Tools.md`, `Vector Class.md`, `Jacobi Method.md`, `Complexity.md`, `Quiz.md` | Reference on demand |
| **Assessments** | `Midterm - 1.md`, `Final.md` | Scope check only |

**Concepts_old filenames (link each in 06 in-scope or deferred):**

1. `Vectors, Linear Functions, and the Regression Model.md`
2. `Norms, Distance, Standard Deviation, and Angles.md`
3. `Geometric Transformations, Graphs, Linear Equations, and the Matrix Class.md` — *split: LA core vs graph intro → defer graph/PageRank parts*
4. `Linear Independence, Bases, Orthonormality, and Matrices.md`
5. `Linear Systems, Inverses, Pseudo-Inverse, and Polynomial Interpolation.md`
6. `Matrix–Matrix Products, QR Factorization, and Householder Reflectors.md` — *QR in-scope; PageRank-as-dynamical-system subsection → defer*
7. `Least Squares and Feature Engineering.md`
8. `Least Squares Classifiers, Optimization, and Gradient Descent.md`
9. `Clustering.md`, `Clustering, K-n.md`
10. `Singular Value Decomposition and Eigenfaces.md`
11. `Matrix_Operations_Reference.md` — reference, not sequential reading
12. **`Graphs_and_PageRank.md`** — **DEFER Endgame**
13. **`The Google PageRank Algorithm.md`** — **DEFER Endgame**

### CSCI 4041 — `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/`

| Area | Count | Role |
|------|-------|------|
| **Board** | `CSCI 4041 Board.md` | MOC entry; links [[DSA]] |
| **Course map** | `Concepts/DSA.md` | **14-week LeetCode plan + 15 concepts + #cards/CSCI4041** |
| **Concepts/** | 15 concept notes | Each should get mastery + interview pattern in 05 |
| **Week - 1..14** | 14 lecture notes | Weekly study sheet |
| **Textbook/** | Chapter notes | CLRS-aligned |
| **Midterm Project/** | AVL (chosen), RB-tree, multiway options | **Summer re-implementation milestone** |
| **Final Project/** | Maze (chosen), Network Flow, Heuristic Pathfinding | **Summer re-implementation milestone** |

**15 concept notes (from DSA MOC — must appear in 05 mastery table):**

Sorting Algorithms, Time Complexity, Divide and Conquer, QuickSort, HeapSort, Elementary Data Structures, AVL Trees, B-Trees, Hashing, Dynamic Programming, Greedy Algorithms, Graph Algorithms, Minimum Spanning Trees, Shortest Paths, Maximum Flow.

### MATH 2230 — `20_Progress/Degree/MATH 2230/`

- `MATH 2230 Board.md`, Syllabus, Calendar, Assignments — **grade ops stay in `04 - Summer Courses Ops`**
- 06 owns **ML bridge notes** (≥1/week) synced to course calendar

---

## DELIVERABLE A — Rewrite `05 - LeetCode & CSCI 4041.md`

The file must include these sections (create headings if missing):

### 1. Strategic summary (3–5 sentences)

4041 = summer flagship for internships; LeetCode is the daily engine; vault concepts = long-term memory.

### 2. Mastery & interview revision system

- Table: **all 15 concepts** × columns: `Vault note path` | `Mastery 0–10` | `LeetCode patterns` | `Last reviewed` | `Company tags done`
- **Revision protocol:** spaced re-touch (e.g. weekly weak-topic day + pre-interview 48h cram list from mastery &lt;7)
- Use existing `#cards/CSCI4041` pattern from [[DSA]] — extend to each concept note where Practice Map exists
- **“Never forget” rule:** no concept marked `tree` until用户-level checklist passed (define checklist per concept: explain, implement skeleton, 2 LC mediums from memory)

### 3. LeetCode daily system (keep ≥5/day)

- Retain weekday rotation but **align to DSA.md weeks 1–14** (not generic topic names only)
- **Company-wise layer:** primary targets Google, Amazon, Meta (from repos). Structure:
  - **Daily:** 3 “pattern” problems + 2 from **current company focus** (rotate company weekly)
  - **Weekly:** pull top N from company CSV/repos for that week’s topic
- **Tracking artifact** — create `10_Areas/Life/Plans/05a - LeetCode Tracker.md` OR `20_Progress/Career/LeetCode Summer 2026.md` (pick one; link from 05):
  - columns: date | count | topics | problem IDs | company tag | 4041 concept linked | difficulty | redo date

### 4. Summer 4041 syllabus (week-by-week)

Mirror **DSA.md `## LeetCode / Weekly Plan`** (Weeks 1–14 + finals review) with added columns:

| Week | Vault week + textbook | Concept deep-dive | LC min (total ≥35/wk) | Company focus | Project tie-in |

Include **Midterm AVL** and **Final Maze** as explicit milestones with dates TBD placeholders and links to project folders.

### 5. Professor projects (summer execution)

- **AVL midterm:** re-implement + invariant tests + 1 interview story bullet
- **Final maze:** BFS/DFS + spanning tree — link Week 11–12 concepts
- Done definitions + evidence (notebook path, test log, README line)

### 6. Overview pass without overload

- Rule: **LeetCode pulls the concept** (already in current 05) — formalize 25–45 min “concept touch” using **Practice Map** sections in concept notes
- Cap: **one concept depth per day**; two-week rotation = full overview pass

### 7. Wire to Plans index

- Wikilink `[[01 - Daily Operating System]]` unchanged; note new tracker note in frontmatter `notes:`

---

## DELIVERABLE B — Rewrite `06 - ML Fundamentals (2033 + 2230).md`

### 1. Strategic summary

2033 supplies **ML linear algebra**; 2230 supplies **probability/stats**; together they form the **ML engineer math base**. Not a full 2033 repeat.

### 2. Two-track model

| Track | Source | Summer role |
|-------|--------|-------------|
| **A — 2033 ML spine** | Concepts_old + ML_Foundations | Curated sequence, 30–45 min/day |
| **B — 2230 live course** | MATH 2230 calendar/syllabus | WebAssign + **ML bridge notes** |

**Integration rule:** when Track B topic aligns with Track A, **same study block** covers both (table required).

### 3. ML fundamentals spine (2033) — in-scope only

Build ordered units (15–25 units max). Each unit row:

| Unit # | ML_Foundations § | Primary vault file(s) | Prerequisite unit # | Active output | Done definition | 2230 bridge (if any) |

**Must cover (from ML_Foundations §1–6):**

1. Data as vectors / norms / distance
2. Regression & least squares (→ supervised learning)
3. Classification (LS classifier, labels)
4. Clustering & k-NN
5. Gradient descent & optimization
6. SVD / PCA / eigenfaces

**Explicitly DEFER — Endgame (late summer):**

- `Graphs_and_PageRank.md`
- `The Google PageRank Algorithm.md`
- Graph/PageRank portions of other notes
- ML_Foundations §7 (PageRank → Graph ML) — **deep pass, not skim**

Endgame section in 06: week placeholder + “full detail” standard (implement PageRank power iteration, graph adjacency drills, link to future GNN study).

### 4. 2033 ↔ 2230 bridge table (required)

Minimum rows (expand with syllabus dates from MATH 2230 Calendar):

| 2033 / ML unit | MATH 2230 topic (when it appears) | Combined study action |
|----------------|-----------------------------------|------------------------|
| Vectors, dot product, norms | Descriptive stats, expectation | … |
| Covariance / multivariate intuition | Joint distributions, covariance matrix | Feeds PCA unit |
| Least squares / regression | Estimation, MLE | Same week when possible |
| Classification thresholds | Conditional probability, Bayes | … |
| GD / loss | Expectation of loss, variance | Bias-variance week |
| SVD / PCA | — (LA-led; 2230 confirms variance decomposition) | … |

### 5. MATH 2230 ML concept notes

- Keep weekly ≥1 note rule; template: `20_Progress/Degree/MATH 2230/Concepts/` or `40_Resources/` per AGENTS routing — **state chosen path in 06**
- Each note: definition | ML use | link to 2033 unit | one worked example

### 6. Vault hygiene

- Primary read: `Concepts_old/`
- `Concepts_new/`: supplemental only
- Do **not** assign reading all `Week - *.md`
- Link `organize-csci2033` skill for any merge work — **out of scope this session** unless one pilot merge is proposed as backlog

### 7. Tracking artifact

Create `10_Areas/Life/Plans/06a - ML Fundamentals Progress.md` (or equivalent) with:

- Unit checklist (0/1 mastery + date)
- Endgame queue (unchecked until Phase 2)
- Current 2230 week + bridge note links

### 8. Phase timing (high level only)

- **Dubai:** complete ML spine units 1–10 (through PCA/SVD core)
- **Bangalore:** finish spine + 2230 bridges; **Endgame** PageRank/graphs in last 2–3 weeks before Sept 1
- Do not duplicate `03 - Monthly & Phase Map` — link to it

---

## QUALITY BAR (self-check)

- [ ] Every 2033 unit maps to a **real filename**, not a generic topic label only
- [ ] PageRank/graphs are **Deferred — Endgame**, not in daily ML minimums
- [ ] 4041 plan covers **all 15 concepts + 14 weeks + both projects**
- [ ] Company-wise LeetCode is **operational** (rotation + tracker), not a mention
- [ ] 2033 and 2230 have a **bridge table** and combined-study rules
- [ ] No daily workflow rewrite in `01`
- [ ] New tracker notes created and linked
- [ ] Frontmatter `notes:` arrays updated on 05, 06, and Index

---

## OUTPUT FORMAT

1. ≤8 bullets: what changed in 05 and 06
2. List new files created (paths)
3. Confirm Endgame deferral and company-wise LC structure
4. Max 3 blocking questions (else document assumptions in 06)

Begin by reading ML_Foundations, DSA (full LeetCode section), both plan files, MATH 2230 Calendar, and sampling 3 Concepts_old + 3 Concepts/4041 notes.
```

## COPY UNTIL HERE

---

## Optional one-liner (prepend in CoWork)

> Attach `00c - CoWork Prompt — Enhance 05 and 06.md`. Execute Deliverables A & B only. Obsidian MCP (`jarvis`) for all vault I/O. Do not change daily workflow yet.

---

## What CoWork already did (context — do not redo)

CoWork created 11 files under `10_Areas/Life/Plans/` including thin **05** and **06**. Your Today note (2026-06-03) correctly pulls Summer Ops Checklist from **01** — that flow stays. This prompt **deepens** the academic engines only.

## Review snapshot (current 05 / 06 gaps)

| Gap | Current state | This prompt fixes |
|-----|---------------|-------------------|
| 2033 scope | Generic 12-row LA table | File-mapped ML spine + Endgame deferral |
| 2033 ↔ 2230 | Mentioned, no bridge | Required bridge table + combined blocks |
| 4041 | 7-day LC rotation only | 14-week DSA alignment + 15-concept mastery |
| Company LC | Missing | Repo-driven company rotation + tracker |
| Projects | Missing | AVL + Maze summer milestones |
| Interview review | Missing | Mastery 0–10 + spaced revision + cards |
| Progress tracking | Today note count only | Dedicated tracker notes 05a / 06a |
