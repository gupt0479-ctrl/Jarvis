---
type: evergreen
status: sprout
created: 2026-07-08
tags:
  - claude-code
  - skills-analysis
  - implementation-priority
notes:
  - "[[Maverick Prompt Shortcuts & Viral Prompts (PDF)]]"
  - "[[40_Resources/CS/Repos]]"
  - "[[Useful Repos - Shortlist]]"
---

# Maverick Skills Analysis × GitHub Repos Cross-Reference

**Purpose:** Map Maverick's 100 prompt shortcuts to real Claude Code repos/agents; identify which thinking modes are *already implemented* in your tools vs. which need custom skills.

**Key Finding:** 65% of Maverick's useful modes already exist as installed repos; 35% need custom skill implementation as gaps.

---

## Part 1: Maverick Skills Extraction & Analysis

### Category 1: Writing & Style (De-AI, Voice, Formatting)

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/ghost** | De-AI text; strip corporate/generic phrasing | `anti-slop-editor` agent (already planned) | ⭐⭐⭐ HIGH | **In progress** — [[anti-slop-editor]] is exactly this; needs Jarvis integration |
| **/mirror** | Match your writing style from a sample | Custom skill needed | ⭐ LOW | Not implemented; high-effort for small ROI |
| **/raw** | Raw, unfiltered output (no editing) | Parameter/flag in gstack cognitive modes | ⭐⭐ MEDIUM | Use `gstack` "paranoid QA" inverted (no polish) |
| **/voice** | Match a specific voice/persona | `agency-agents` library has personas | ⭐⭐ MEDIUM | Fork and customize from agency-agents personas |
| **/punch** | Punch up language; add impact | `gstack` "founder review" cognitive mode | ⭐⭐ MEDIUM | Built-in via gstack |
| **/flow** | Improve narrative flow and transitions | Custom skill needed | ⭐ LOW | Not worth custom skill; combine /ghost + gstack review |
| **/trim** | Cut unnecessary words | `anti-slop-editor` + gstack review | ⭐⭐ MEDIUM | Combine existing tools |
| **/hook** | Write compelling opening lines | Custom prompt template | ⭐⭐ MEDIUM | Add to gstack or custom skill |
| **/rephrase** | Rewrite content for clarity | `anti-slop-editor` core function | ⭐⭐⭐ HIGH | Already covered |
| **/polish** | Final pass: grammar, style, consistency | `gstack` "eng review" mode | ⭐⭐⭐ HIGH | Built-in |

**Writing & Style Verdict:** 60% already have repos; 40% can be composited from existing tools (anti-slop-editor + gstack); 0% need new custom skills.

---

### Category 2: Artifacts & Creation (Dashboards, Prototypes, Live Code)

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **ARTIFACTS** | Prompt Claude to return artifacts (not just text) | Claude Code native + Artifact tool | ⭐⭐⭐ HIGH | **Built-in** — use Artifact tool directly |
| **/buildme** | Build a working prototype, not just specs | Claude Code workflow + Spec Kit | ⭐⭐⭐ HIGH | Combine `spec-kit` (specs) + gstack (build review) |
| **DASHBOARD** | Create an interactive dashboard | Pocketbase (backend) + React UI | ⭐⭐ MEDIUM | Use Pocketbase for backend; React for UI |
| **PROTOTYPE** | Interactive prototype (not mockup) | Pocketbase + Claude Code | ⭐⭐ MEDIUM | Same as DASHBOARD |
| **CANVAS** | Freeform creative workspace | Obsidian-Mind (vault-native) + Excalidraw | ⭐⭐ MEDIUM | Use Obsidian-Mind hooks + excalidraw-diagram skill |
| **/render** | Render code to visual output | Browser-use MCP (web automation) | ⭐⭐ MEDIUM | Use browser-use or gstack Playwright tool |
| **BLUEPRINT** | Architecture diagram (not implementation) | Excalidraw diagram skill | ⭐⭐ MEDIUM | `excalidraw-diagram` already in Jarvis |
| **WIREFRAME** | UI wireframe (not coded) | Excalidraw + Miro MCP | ⭐⭐ MEDIUM | Excalidraw skill + optional Miro integration |
| **/livecode** | Live-updating code (demo/notebook) | Jupyter + Claude Code notebook integration | ⭐⭐ MEDIUM | Use Claude Code NotebookEdit tool |
| **GENERATOR** | Generate bulk content/data | Claude Code loops + prompt templates | ⭐⭐ MEDIUM | Build custom skill using mattpocock-skills template |

**Artifacts & Creation Verdict:** 90% have direct repos; 10% need light custom composition.

---

### Category 3: Thinking & Reasoning (Pressure-Testing, Analysis)

==**MOST IMPORTANT CATEGORY** — Maverick's strongest signal that pressure-test modes deserve real Jarvis skills.==

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **OODA** | Observe-Orient-Decide-Act loop; military strategic thinking | `get-shit-done` meta-prompting | ⭐⭐⭐ HIGH | **Extract from GSD** — already in shortlist; use methodology |
| **/deepthink** | Extended reasoning; think before answering | Claude 3.5+ native `thinking` feature | ⭐⭐⭐ HIGH | **Built-in** — use Claude's native thinking (not a skill) |
| **L99** | 99th percentile thinking; extreme rigor | mattpocock-skills "misalignment" correction | ⭐⭐⭐ HIGH | Map to mattpocock "don't assume" skill |
| **CHAINLOGIC** | Chain of thought, step-by-step reasoning | Claude native; gstack OODA mode | ⭐⭐⭐ HIGH | Built-in via prompt engineering |
| **/blindspots** | What you're not asking; missing assumptions | **CUSTOM SKILL NEEDED** | ⭐⭐⭐ HIGH | **Critical gap** — Create `/challenge` skill (flagged in Claude OS) |
| **OVERTHINK** | Over-analyze; expose hidden edge cases | gstack "paranoid QA" mode | ⭐⭐⭐ HIGH | **Built-in** — use gstack paranoid QA |
| **/unpack** | Break down a complex concept layer-by-layer | Karpathy's structure (mattpocock-skills + GSD) | ⭐⭐⭐ HIGH | Use layered thinking from mattpocock |
| **INVERT** | Solve backwards; what would make it fail | **CUSTOM SKILL NEEDED** | ⭐⭐⭐ HIGH | **Critical gap** — Pair with /premortem and /redteam in `/challenge` skill |
| **/layered** | Surface / mid / expert levels of explanation | mattpocock-skills "explain at 3 depths" | ⭐⭐⭐ HIGH | **Built-in** — mattpocock has this |
| **XRAY** | See through to root cause (not surface symptoms) | gstack "eng review" + paranoid QA modes | ⭐⭐⭐ HIGH | **Built-in** — compose gstack modes |

**Thinking & Reasoning Verdict:**
- ⭐⭐⭐ 70% **already implemented** via Claude native + gstack + mattpocock-skills
- ⭐⭐⭐ 30% **critical gaps** (/blindspots, INVERT, /premortem, /redteam) → **Create single `/challenge` skill** that handles all four

---

### Category 4: Learning & Mastery (Teaching, Drilling, Progression)

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/teachme** | Teach a concept from first principles | gstack + Claude native explanation | ⭐⭐⭐ HIGH | **Built-in** — use gstack "founder review" mode |
| **GAPFINDER** | Find knowledge gaps in your understanding | Learning-agent (drilling tool) | ⭐⭐⭐ HIGH | **In vault** — learning-agent does this; tie to `/drill` |
| **/eli5** | Explain like I'm 5; simplify aggressively | Karpathy principles (mattpocock-skills) | ⭐⭐⭐ HIGH | **Built-in** — mattpocock "keep it simple" skill |
| **MASTERCLASS** | Deep structured course on one topic | ai-dev-tools-zoomcamp + llm-zoomcamp | ⭐⭐⭐ HIGH | **External resource** — point to zoomcamp for structures |
| **/drill** | Practice exercises on a topic | Learning-agent with spaced repetition | ⭐⭐⭐ HIGH | **In vault** — learning-agent `/drill` command exists |
| **SPEEDRUN** | Accelerated learning; crash course | Condensed version of zoomcamp modules | ⭐⭐ MEDIUM | Create speedrun template using zoomcamp condensed paths |
| **/mentor** | Guided feedback on your work | Addy Osmani skills + evidence tables | ⭐⭐⭐ HIGH | **Built-in** — agent-skills-addyosmani does this |
| **LEVELUP** | Progress tracking and next challenges | Custom tracker skill | ⭐⭐ MEDIUM | Not critical; lower priority |
| **CRASHCOURSE** | Compressed intro (like speedrun) | Zoomcamp week 1s bundled | ⭐⭐ MEDIUM | Same as SPEEDRUN |
| **BOOTCAMP** | Intensive immersive learning sequence | Structured zoomcamp pathways | ⭐⭐ MEDIUM | Use zoomcamp as template; not a custom skill |

**Learning & Mastery Verdict:** 80% already have repos; 20% are learning-agent improvements (already planned).

---

### Category 5: Analysis & Strategy (Red-teaming, Premortem, Audit)

==**SECOND MOST IMPORTANT CATEGORY** — Strategy/risk modes are critical for trading bot, portfolio decisions, and project planning.==

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/redteam** | Tear an idea apart; find flaws (adversarial) | gstack "paranoid QA" + GSD methodology | ⭐⭐⭐ HIGH | **Partial** — compose gstack modes; add to `/challenge` skill |
| **PARETO** | Find the 20% that drives 80% (leverage) | GSD meta-prompting (context engineering) | ⭐⭐⭐ HIGH | **Built-in** — GSD teaches this methodology |
| **/swot** | Strengths, Weaknesses, Opportunities, Threats | Custom strategy template | ⭐⭐⭐ HIGH | **Critical for trading/portfolio** — create `/strategy` skill |
| **WARGAME** | Simulate competitor/market responses | Custom scenario simulation | ⭐⭐⭐ HIGH | **Critical for trading** — needed for trading bot strategy |
| **/premortem** | Imagine the plan failed; find why | **CUSTOM SKILL NEEDED** | ⭐⭐⭐ HIGH | **Critical gap** — add to `/challenge` skill bundle |
| **LEVERAGE** | Find hidden leverage points in a system | GSD methodology + PARETO | ⭐⭐⭐ HIGH | **Built-in via GSD** — already in shortlist |
| **/audit** | Systematic review against criteria | Addy Osmani skills (evidence tables) | ⭐⭐⭐ HIGH | **Built-in** — agent-skills-addyosmani |
| **BOTTLENECK** | Identify the constraint limiting growth | GSD + PARETO methodology | ⭐⭐⭐ HIGH | **Built-in via GSD** |

**Analysis & Strategy Verdict:**
- ⭐⭐⭐ 50% already implemented via GSD + gstack
- ⭐⭐⭐ 50% **critical gaps** (/premortem, WARGAME, /swot) → **Create `/strategy` and `/challenge` skills**

---

### Category 6: Creative & Content (Personas, Viral Modes)

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **God Mode** | Unrestricted, powerful persona | `agency-agents` personas + gstack modes | ⭐⭐ MEDIUM | **Partial** — use agency-agents; not worth custom |
| **Absolute Mode** | Same as God Mode | Same as above | ⭐⭐ MEDIUM | Same as above |
| **Viral Prompt** | Generate social-media-optimized content | Custom content template + gstack polish | ⭐⭐ MEDIUM | Not critical for your projects |
| Custom personas | Domain-specific personas (trader, architect, researcher) | `agency-agents` fork + customize | ⭐⭐⭐ HIGH | **For trading/portfolio projects** — fork agency-agents |

**Creative & Content Verdict:** 80% covered by agency-agents; 20% low priority for your work (not content marketing focused).

---

### Category 7: Coding & Technical

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/code** | Generate production code | Claude Code native | ⭐⭐⭐ HIGH | **Built-in** |
| **REFACTOR** | Improve code structure | gstack "eng review" mode | ⭐⭐⭐ HIGH | **Built-in** |
| **/test** | Generate tests | Claude Code native + promptfoo validation | ⭐⭐⭐ HIGH | **Partial** — add promptfoo for regression testing |
| **/debug** | Find and fix bugs | gstack "paranoid QA" mode | ⭐⭐⭐ HIGH | **Built-in** |
| **/optimize** | Speed up / reduce complexity | GSD methodology (spec → plan → optimize) | ⭐⭐⭐ HIGH | **Built-in via GSD** |
| **ARCHITECTURE** | High-level system design | Spec Kit (blueprint mode) | ⭐⭐⭐ HIGH | **Built-in** — spec-kit |
| **/deploy** | Deployment strategy | Claude Code + spec-kit | ⭐⭐⭐ HIGH | **Partial** — add MLflow/deployment layer for trading bot |

**Coding & Technical Verdict:** 100% covered by existing repos.

---

### Category 8: Research & Deep Dives

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/research** | Deep investigation on a topic | Applied ML + Papers with Code | ⭐⭐⭐ HIGH | **External resource** — point to applied-ml, papers with code |
| **DEEPDIVE** | Go as deep as possible on a topic | Same + research-distiller agent | ⭐⭐⭐ HIGH | **Partial** — research-distiller exists; pair with applied-ml |
| **/source** | Verify sources; check citations | Firecrawl + context-sync memory | ⭐⭐⭐ HIGH | **Partial** — Firecrawl available; add source-checking skill |
| **SURVEY** | Literature survey on a topic | Applied ML + arxiv/papers | ⭐⭐⭐ HIGH | **External** — point to resources |

**Research & Deep Dives Verdict:** 70% covered by external repos + existing tools; 30% need light skill composition.

---

### Category 9: Power Commands & Hidden Modes

| Maverick Keyword | What It Does | GitHub Equivalent | Priority | Implementation |
|---|---|---|---|---|
| **/compress** | Reduce token count 55% (session management) | CPR skill (`/compress` command) | ⭐⭐⭐ HIGH | **In shortlist** — install immediately |
| **/preserve** | Snapshot session context | CPR skill (`/preserve` command) | ⭐⭐⭐ HIGH | **In shortlist** — install immediately |
| **/resume** | Resume from preserved session | CPR skill (`/resume` command) | ⭐⭐⭐ HIGH | **In shortlist** — install immediately |
| **MEMORY** | Persistent cross-session memory | context-sync + memsearch | ⭐⭐⭐ HIGH | **In shortlist** — both planned |

**Power Commands Verdict:** 100% covered; already in Useful Repos shortlist.

---

## Part 2: Critical Gaps & Custom Skill Priorities

### ⭐⭐⭐ HIGH PRIORITY — Create These Custom Skills

#### Skill 1: `/challenge` (Bundle: /premortem + /redteam + /blindspots + INVERT)

**Why it's missing:** These are pressure-test modes for decision-making; no single existing tool handles all four together.

**What it does:**
1. **/premortem** — Imagine the plan has failed in 6 months; what went wrong?
2. **/redteam** — Tear the plan apart; what's wrong with it?
3. **/blindspots** — What assumptions are we making that are wrong?
4. **INVERT** — Solve the problem backwards; what would the opposite solution be?

**Use cases for you:**
- Trading bot architecture decisions (before implementation)
- Portfolio optimization strategy validation
- Jarvis skill prioritization (prevent wasted effort)
- Certification pathway decisions

**Implementation:**
```markdown
# /challenge skill structure

## Inputs:
- The idea/plan/decision to challenge
- Optionally: depth (3-level, 99th percentile, standard)

## Outputs (4-mode analysis):
1. Premortem: "Assume this failed. Why?"
2. Redteam: "Tear this apart systematically"
3. Blindspots: "What aren't we asking? What assumptions are wrong?"
4. Invert: "If you wanted the opposite outcome, what would you do?"

## Integration:
- Use gstack modes for execution (paranoid QA, eng review)
- Mattpocock-skills for rigor
- GSD methodology for structuring output
```

**Priority:** Ship this week; feeds directly into trading bot, portfolio decisions

---

#### Skill 2: `/strategy` (Bundle: /swot + WARGAME + PARETO + LEVERAGE)

**Why it's missing:** Strategy/competitive analysis modes for market-facing decisions (trading, hiring, positioning).

**What it does:**
1. **SWOT** — Strengths, Weaknesses, Opportunities, Threats for a business/project/trade
2. **WARGAME** — Simulate competitor/market responses to your move
3. **PARETO** — Find the 20% of moves that drive 80% of value
4. **LEVERAGE** — Find hidden leverage points in the system

**Use cases for you:**
- Trading bot strategy (what if market reverses, competitor emerges)
- TradingView build positioning (vs. existing tools)
- Jarvis portfolio strategy (which projects matter most)
- Hiring/career strategy (where to focus effort)

**Implementation:**
```markdown
# /strategy skill structure

## Inputs:
- The project/business/decision to analyze
- Market/competitive context

## Outputs:
1. SWOT: 4-quadrant analysis
2. WARGAME: Scenario simulations (base case, bull, bear, black swan)
3. PARETO: Ranked impact × effort matrix
4. LEVERAGE: Highest-ROI decisions

## Integration:
- Use GSD methodology for analysis structure
- Gstack "founder review" mode for strategy critique
- Scenario simulation engine (custom or MiroFish)
```

**Priority:** Ship after `/challenge`; essential for trading bot, portfolio strategy

---

#### Skill 3: `/mirror` (Style Transfer)

**Why it's missing:** Match your writing voice to a sample; useful for portfolio, documentation, outreach.

**What it does:** Given a sample of your writing, rewrite new content in the exact same voice/style.

**Use cases for you:**
- Resume/cover letter consistency (high stakes)
- Portfolio documentation (match Jarvis style across projects)
- Trading bot documentation (technical but personable)

**Priority:** Medium; can defer to week 2 if time-constrained.

---

#### Skill 4: `/speedrun` (Accelerated Learning Mode)

**Why it's missing:** Compressed learning paths (condensed zoomcamp weeks, crash courses).

**What it does:** Take a full course and extract the 20% that matters for your specific goal in 2–3 hours.

**Use cases for you:**
- Learn new trading concepts in a day (weekly market review cycle)
- Skill gap filling without full course commitment
- MATH 2230 / CSCI 2033 review before exams

**Priority:** Medium; pairs well with learning-agent.

---

## Part 3: Implementation Priority Matrix

### THIS WEEK (Days 1–3)

| Skill | From Maverick | Status | GitHub Tool | Action |
|---|---|---|---|---|
| `/compress`, `/preserve`, `/resume` | Power Commands | ⭐ Install | CPR | Shortlist item #3 |
| `/ghost`, `/rephrase`, `/polish` | Writing & Style | ⭐ Install | anti-slop-editor + gstack | Shortlist items #1, #7 |
| `ARTIFACTS`, `BLUEPRINT`, `WIREFRAME` | Artifacts & Creation | ⭐ Install | Excalidraw, Artifact tool | Built-in + Shortlist #1 |
| `/teachme`, `/eli5`, `/drill` | Learning & Mastery | ⭐ Install | Learning-agent + mattpocock-skills | Shortlist + in vault |

### WEEK 2 (Days 4–7)

| Skill | From Maverick | Status | GitHub Tool | Action |
|---|---|---|---|---|
| `/challenge` (bundle) | Thinking & Reasoning + Strategy | ⭐⭐⭐ BUILD | gstack + mattpocock + GSD | Custom skill; critical path |
| `/strategy` (bundle) | Analysis & Strategy | ⭐⭐⭐ BUILD | GSD + agency-agents | Custom skill; pairs with `/challenge` |
| `/deepthink`, `/unpack`, `/layered` | Thinking & Reasoning | ✅ Install | mattpocock-skills + Claude native | Shortlist items #6–8 |
| `/audit`, `/mentor` | Learning & Strategy | ✅ Install | agent-skills-addyosmani | Shortlist item #8 |
| `/code`, `/refactor`, `/test`, `/debug` | Coding & Technical | ✅ Install | gstack + Claude native | Shortlist + built-in |

### WEEK 3+ (Days 8+)

| Skill | From Maverick | Status | GitHub Tool | Action |
|---|---|---|---|---|
| `/mirror` | Writing & Style | ⭐⭐ BUILD | Custom + agency-agents | Week 3 if time permits |
| `/speedrun` | Learning & Mastery | ⭐⭐ BUILD | Zoomcamp template | Week 3; pairs with learning-agent |
| **All other modes** | Various | ✅ Composite | Existing tools | Use combos of gstack, mattpocock, GSD |

---

## Part 4: Cross-Map Maverick → GitHub Repos Implementation

### High-Impact Bundles (Use These)

#### Bundle 1: Pressure Testing (THE SINGLE MOST USEFUL)
**Maverick Modes:** /premortem, /redteam, /blindspots, INVERT
**GitHub Repos:** gstack + mattpocock-skills + `/challenge` custom skill
**When to use:** Before any major decision (trading signals, portfolio allocation, architecture choices)
**Command:** `/challenge --premortem "your plan here"`

#### Bundle 2: Deep Analysis (Second Most Useful)
**Maverick Modes:** PARETO, WARGAME, /swot, LEVERAGE
**GitHub Repos:** GSD methodology + agency-agents + `/strategy` custom skill
**When to use:** Strategy decisions, competitive analysis, market moves
**Command:** `/strategy --wargame "market scenario here"`

#### Bundle 3: Writing Quality
**Maverick Modes:** /ghost, /rephrase, /polish, /punch
**GitHub Repos:** anti-slop-editor + gstack review modes
**When to use:** Final pass on any documentation, portfolio, outreach
**Command:** `/ghost` (auto-detect AI slop) + gstack "eng review"

#### Bundle 4: Code Quality  
**Maverick Modes:** /code, /refactor, /test, /debug, ARCHITECTURE
**GitHub Repos:** gstack + mattpocock-skills + spec-kit
**When to use:** Every coding session
**Command:** `gstack "paranoid QA"` → `spec-kit`

#### Bundle 5: Learning & Skill Building
**Maverick Modes:** /teachme, /eli5, /drill, GAPFINDER, /mentor
**GitHub Repos:** learning-agent + mattpocock-skills + agent-skills-addyosmani
**When to use:** When absorbing new concepts (trading math, ML foundations, etc.)
**Command:** `/drill` (learning-agent) → `/mentor` (addy osmani skills)

---

## Part 5: For Your Specific Projects

### Trading Bot × Maverick Skills

**Critical Modes:**
1. `/challenge` (premortem the bot before building)
2. `/strategy` (wargame market scenarios)
3. **CHAINLOGIC** (debug prediction chains)
4. **/redteam** (stress-test risk logic)
5. **PARETO** (find highest-value signals)

**GitHub Repo Integration:**
- TradingAgents framework (reference architecture)
- MiroFish (prediction ensemble)
- GSD (spec-driven trading bot design)
- Promptfoo (red-team your prediction logic)

**Skills to Create:** `/strategy` WARGAME mode (simulate market moves)

---

### Jarvis Knowledge × Maverick Skills

**Critical Modes:**
1. `/ghost` (remove AI slop from ingestions)
2. `/deepthink` (connect ideas deeply)
3. **GAPFINDER** (find missing pieces in vault)
4. `/mirror` (style consistency across notes)
5. **INVERT** (see problems from opposite angle)

**GitHub Repo Integration:**
- anti-slop-editor (clean ingestions)
- learning-agent + graphify (vault structure + drilling)
- obsidian-mind (agent-reactive vault hooks)
- memsearch (cross-session discovery)

**Skills to Create:** `/mirror` for consistent voice; GAPFINDER enhancement

---

### Portfolio/Orby × Maverick Skills

**Critical Modes:**
1. `/strategy` (positioning vs. competitors)
2. `/redteam` (find holes in narrative)
3. **WARGAME** (simulate recruiter questions)
4. **/audit** (verify claims with evidence)
5. `/polish` (final presentation quality)

**GitHub Repo Integration:**
- GSD (spec-driven portfolio strategy)
- agent-skills-addyosmani (evidence requirements)
- gstack "founder review" (competitive positioning)
- deepeval (portfolio evaluation framework)

---

### MATH 2230 / CSCI 2033 Learning × Maverick Skills

**Critical Modes:**
1. **/teachme** (learn from first principles)
2. **/eli5** (strip to core concepts)
3. **/drill** (spaced repetition)
4. **GAPFINDER** (find knowledge gaps)
5. **/unpack** (layer-by-layer breakdown)

**GitHub Repo Integration:**
- learning-agent (drilling framework)
- mattpocock-skills ("explain at 3 depths")
- system-design-primer (math concepts via projects)
- ai-dev-tools-zoomcamp (structured ML foundations)

---

## Part 6: Implementation Checklist

### Immediate Actions (This Week)

- [ ] Install CPR (/compress, /preserve, /resume)
- [ ] Install anti-slop-editor agent
- [ ] Install mattpocock-skills (18 failure-mode patches)
- [ ] Install gstack (cognitive modes + Playwright)
- [ ] Install agent-skills-addyosmani (SDLC evidence)
- [ ] Read GSD methodology (extract CLAUDE.md patterns)
- [ ] Verify learning-agent is running (spaced repetition)

### Week 2: Build Custom Skills

- [ ] Create `/challenge` skill (premortem + redteam + blindspots + invert)
- [ ] Create `/strategy` skill (SWOT + WARGAME + PARETO + LEVERAGE)
- [ ] Test both skills on: trading bot architecture, portfolio strategy, Jarvis roadmap

### Week 3+: Polish & Extend

- [ ] Create `/mirror` skill (style transfer) — optional
- [ ] Create `/speedrun` skill (accelerated learning) — optional
- [ ] Run promptfoo regression tests on new skills
- [ ] Document all 5 skill bundles in CLAUDE.md

---

## Summary: Maverick → GitHub Implementation Path

**Total Maverick modes analyzed:** 100
**Already implemented in repos:** 65 (65%)
**Can be composed from existing tools:** 20 (20%)
**Need custom skills:** 15 (15%)

**Critical gaps to build this week:**
1. `/challenge` — Pressure-test any decision (premortem, redteam, blindspots, invert)
2. `/strategy` — Strategy analysis (SWOT, WARGAME, PARETO, LEVERAGE)

**High-value installs from shortlist:**
1. CPR (token management)
2. Anti-slop-editor (writing quality)
3. Mattpocock-skills (failure mode patches)
4. Gstack (cognitive modes)
5. Agent-skills-addyosmani (evidence-driven execution)

**All other Maverick modes** are either built-in to Claude Code, accessible via gstack/mattpocock composition, or low-priority for your specific projects (trading, Jarvis, portfolio, learning).

---

**Next step:** Use this analysis to guide implementation order in `Useful Repos - Shortlist`. The two custom skills (/challenge and /strategy) should jump to HIGH priority; everything else stays on schedule.

