---
type: evergreen
status: seedling
created: 2026-07-09
tags:
  - internships
  - career
  - dashboard
  - tracking
  - pipeline
notes:
  - "[[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]"
  - "[[Tracker]]"
  - "[[Weekly Operating System]]"
  - "[[MavGPT AI Resume & Job Search Guide (PDF)]]"
  - "[[LinkedIn Search URL Cheatsheet (PDF)]]"
next: Create internship tracking board in Obsidian
---

# Internship Tracking Dashboard — 2027 Calendar, Programs & Application Pipeline

**Integrated Sources:**
- [[2027 Internship Calendar (web)]] — Wave timing (Quant, Big Tech, Banks)
- [[Fintech Early Programs That Pay — HRT, Capital One, Bloomberg (web)]] — $5,800–$5,000+/wk programs
- [[Underclassmen Internship List (web)]] — Freshman/sophomore-locked programs with short windows

**Status:** Framework defined; Obsidian dashboard ready to build  
**Update Cadence:** Weekly (Friday pipeline check) + Daily (deadline alerts)

---

## Executive Summary: The Three-Wave Strategy

**Wave 1 — Quant Programs (Highest Pay, Earliest Deadline)**
- Hudson River Trading: $5,800/week + housing (sophomores, grad 2028)
- Jane Street FTTP/AMP: $2,500–$4,000/week (freshmen/recent HS)
- Two Sigma First-Year: $2,900/week (1st-year only)
- D.E. Shaw Fellowships: Second-years, resume-screen bypass
- Citadel Launch/Discover: $4,300–$4,800/week (2nd-year, datathon fast-track)
- **Timeline:** Wave 1 opens NOW through fall 2026

**Wave 2 — Big Tech Programs (Mid-pay, Mid-window)**
- Google ASDI (formerly STEP): 1st/2nd-year, 12 weeks, opens ~late Sept/Oct
- Microsoft Explore: 1st/2nd-year, opens ~Aug 2026
- LinkedIn First Play: 1st/2nd-year, infamously short window (late Nov 2026)
- NVIDIA Ignite: 1st/2nd-year, short window
- MLH Fellowship: Any year, 18+, rolling (OPEN NOW)
- **Timeline:** Wave 2 opens Jul–Oct 2026

**Wave 3 — Banks (Lowest Pay, Deadline Closed for 2027)**
- Goldman, JPMorgan, Citi, Morgan Stanley IB: **FILLED Dec 2025–Jan 2026 (closed)**
- Capital One: Rising juniors (grad 2027), opens ~Aug 2026
- **Timeline:** Bank roles CLOSED for summer 2027 (apply now for summer 2028)

**Bottom Line:** For summer 2027, focus Wave 1 + Wave 2 (quant + big tech). Wave 3 (banks) is closed; pivot to Capital One + specialized quant tracks.

---

## Core Framework: The Dashboard Design

### Why a Dashboard is Critical

**Problem with the current approach:**
- Three separate web pages (Notion, GitHub, career sites)
- No unified view of your applications + deadlines + status
- "Applied 3 months ago, forgot to follow up" (common failure)
- No tracking of "which programs applied to" vs. "still eligible" vs. "aged out"

**Solution: Obsidian Dashboard combining**
1. **Calendar view** (deadlines by wave + month)
2. **Application tracker** (program name, status, deadline, eligibility)
3. **Dataview queries** (filter by eligibility, status, pay, deadline)
4. **Follow-up reminder system** (weekly deadlines, application tracking)

---

## The Data Model: What to Track

### Core Fields (Every Internship Program)

| Field | Type | Example | Purpose |
|---|---|---|---|
| `name` | Text | Hudson River Trading Sophomore | Program identifier |
| `company` | Text | Hudson River Trading | Company name (for filtering) |
| `program_type` | Dropdown | Quant / Big Tech / Bank / Fellowship | Wave categorization |
| `eligible_classes` | Multi-select | Sophomore, Junior (grad 2027/2028) | Who can apply |
| `grad_year` | Number | 2027, 2028, 2029 | Your grad year (filter match) |
| `wave` | Dropdown | Wave 1, Wave 2, Wave 3 | Application timing window |
| `opens_date` | Date | 2026-08-15 | Portal opens |
| `deadline_posted` | Date | 2026-10-31 | Official deadline (often fake) |
| `deadline_real` | Date | 2026-10-15 | Real deadline (rolling, first 2 weeks) |
| `pay_per_week` | Number | 5800 | Compensation |
| `pay_currency` | Dropdown | USD | Currency |
| `duration_weeks` | Number | 10 | Internship length |
| `benefits` | Multi-select | Housing, Meals, Perks | Non-salary compensation |
| `application_url` | URL | https://www.hudsonrivertrading.com/student-opportunities/ | Direct apply link |
| `careers_page` | URL | https://www.hudsonrivertrading.com/careers/ | Fallback link |
| `status` | Dropdown | Not Started, Applied, Interview, Offer, Rejected, Closed | Application status |
| `date_applied` | Date | 2026-09-15 | When you applied |
| `notes` | Text | AI tools banned in interviews | Key traps/requirements |
| `tags` | Multi-select | high-pay, hard, quant, AI-focused | Search tags |

---

## Building the Dashboard: Folder Structure + Files

### Recommended Vault Structure

```
10_Areas/
  Career/
    Internships/
      [Main Dashboard]
      📄 Internship Tracker — Dashboard.md
      📄 Internship Application Log.md
      📄 Internship Deadlines (Weekly Review).md
      📄 Internship Resources & Links.md
      
      Programs/
      📄 2026-HRT.md (one file per program)
      📄 2026-CapitalOne.md
      📄 2026-GoogleASID.md
      ... etc
      
      [Reference]
      📄 Wave 1 Programs (Quant).md
      📄 Wave 2 Programs (Big Tech).md
      📄 Wave 3 Programs (Banks).md
      📄 Underclassmen Programs Tracker.md
```

---

## Dashboard: Dataview Queries

### Query 1: All Open Programs (By Wave)

```
## Wave 1 — Quant (Open Now Through Fall 2026)
```dataview
TABLE
  opens_date,
  deadline_real,
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE program_type = "Quant" AND wave = "Wave 1"
SORT opens_date ASC
```

## Wave 2 — Big Tech (Open Jul–Oct 2026)
```dataview
TABLE
  opens_date,
  deadline_real,
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE program_type = "Big Tech" AND wave = "Wave 2"
SORT opens_date ASC
```

### Query 2: Application Status Tracker

```
## 📊 Application Pipeline Status

### Not Started (Ready to Apply)
```dataview
TABLE
  deadline_real,
  pay_per_week,
  eligible_classes
FROM "10_Areas/Career/Internships/Programs"
WHERE status = "Not Started" AND opens_date <= date(today)
SORT deadline_real ASC
```

### Applied (Waiting for Response)
```dataview
TABLE
  date_applied,
  deadline_real,
  days_since_apply = (date(today) - date_applied)
FROM "10_Areas/Career/Internships/Programs"
WHERE status = "Applied"
SORT date_applied DESC
```

### In Interview / Offer / Rejected
```dataview
TABLE
  status,
  date_applied,
  pay_per_week
FROM "10_Areas/Career/Internships/Programs"
WHERE status IN ("Interview", "Offer", "Rejected")
SORT date_applied DESC
```

### Query 3: High-Pay Programs (Filter by Compensation)

```
## 💰 Sorted by Pay (Highest First)
```dataview
TABLE
  company,
  pay_per_week,
  program_type,
  deadline_real,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE pay_per_week >= 2900
SORT pay_per_week DESC
```

### Query 4: Eligibility Filter (By Your Grad Year)

```
## ✅ Programs You Can Still Apply To (Grad 2027)
```dataview
TABLE
  program_type,
  opens_date,
  deadline_real,
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE contains(eligible_classes, "2027") AND status != "Closed"
SORT deadline_real ASC
```

### Query 5: Deadline Alerts (Next 30 Days)

```
## ⏰ Deadlines in Next 30 Days
```dataview
TABLE
  opens_date,
  deadline_real,
  days_until_deadline = (date(deadline_real) - date(today)),
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE deadline_real <= date(today) + dur(30 days) AND status = "Not Started"
SORT deadline_real ASC
```

---

## Program Data: Ready-to-Use Template

### Template: One Program Per File

**File:** `10_Areas/Career/Internships/Programs/2026-HRT.md`

```markdown
---
name: Hudson River Trading Sophomore Internship
company: Hudson River Trading
program_type: Quant
eligible_classes: 
  - Sophomore
grad_year: 2028
wave: Wave 1
opens_date: 2026-08-01
deadline_posted: 2026-10-31
deadline_real: 2026-10-15
pay_per_week: 5800
pay_currency: USD
duration_weeks: 10
benefits:
  - Housing
  - Meals
  - Perks
application_url: https://www.hudsonrivertrading.com/student-opportunities/
careers_page: https://www.hudsonrivertrading.com/careers/
status: Not Started
date_applied: 
notes: |
  - $5,800/week base + housing (NOT the $25k signing bonus, which is for algo-trader role)
  - Rotation through algorithm development (quant research) + software engineering
  - Python OR C++ (pick one at application; you can't apply to both)
  - Only ONE HRT application per cycle allowed
  - AI tools STRICTLY BANNED in interviews and assessments
  - Most hires don't have finance background; training provided
tags:
  - high-pay
  - quant
  - research
  - algo-dev
---

# Hudson River Trading — Sophomore Internship

## Key Info
- **Pay:** $5,800/week + housing/meals/perks
- **Who:** Sophomores graduating 2028 (apply in fall 2026)
- **Skills needed:** Python or C++, stats, numerical work or ML (pandas, numpy, R, MATLAB)
- **Rotation:** Algorithm development + Software engineering (6 weeks each approx)

## Traps to Avoid
1. ❌ Don't apply for the $25k signing bonus role (that's algo-trader for grad hires, different posting)
2. ❌ Don't use AI tools during interviews — instant disqualification possible
3. ❌ Choose Python OR C++ at application; you cannot apply to both in one cycle
4. ❌ Can only apply to ONE HRT posting per cycle

## Scam Check
Real HRT emails ONLY come from @hudson-trading.com domain. Offers never ask for banking info.

## Links
- Apply: [Student Opportunities](https://www.hudsonrivertrading.com/student-opportunities/)
- Careers: [HRT Careers](https://www.hudsonrivertrading.com/careers/)
- Inside HRT track: 3-day immersive for 1st/2nd-year in CS/Math/STEM

## Application Log
- Status: Not Started
- Opens: August 2026
- Real deadline: October 15 (apply in first 2 weeks for best odds)
```

---

## Reference: All Programs + Working Links

### Wave 1 — Quant (Opens Now–Fall 2026)

| Program | Company | Pay/Week | Eligibility | Links |
|---|---|---|---|---|
| **Sophomore Internship** | Hudson River Trading | $5,800 + housing | Sophomores (grad 2028) | [Student Opps](https://www.hudsonrivertrading.com/student-opportunities/) · [Careers](https://www.hudsonrivertrading.com/careers/) |
| **FTTP (First-Year SWE)** | Jane Street | $2,500–$3,000 | 1st-year ONLY (grad 2028) | Search Jane Street careers |
| **AMP (Apprenticeship)** | Jane Street | — | Recent HS only | Search Jane Street careers |
| **First-Year SWE** | Two Sigma | $2,900/week | 1st-year ONLY | [Careers](https://careers.twosigma.com/careers/InternshipsAndEarlyCareers) |
| **Fellowship Programs** | D.E. Shaw | $4,000+/week | 2nd-year, resume bypass | Search D.E. Shaw careers |
| **Launch Intern** | Citadel | $4,300–$4,800/week | 2nd-year (grad 2027) | [Launch Role](https://www.citadel.com/careers/details/launch-intern-us/) |
| **Discover Datathon** | Citadel | — | 1st/2nd-year (1st year fast-track) | Search Citadel careers |

### Wave 2 — Big Tech (Opens Jul–Oct 2026)

| Program | Company | Pay/Week | Eligibility | Links |
|---|---|---|---|---|
| **ASDI (formerly STEP)** | Google | — | 1st/2nd-year (12 weeks) | [Google Careers](https://www.google.com/about/careers/applications/) – search "Associate Software Developer Intern" |
| **Explore** | Microsoft | — | 1st/2nd-year | [Microsoft Explore](https://careers.microsoft.com/v2/global/en/exploremicrosoft) |
| **First Play** | LinkedIn | — | 1st/2nd-year (INFAMOUSLY SHORT WINDOW) | [LinkedIn First Play](https://careers.linkedin.com/pathways-programs/internships/Technical/first-play) |
| **Ignite** | NVIDIA | — | 1st/2nd-year (SHORT WINDOW) | Search NVIDIA careers |
| **Fellowship** | MLH | — | Any year, 18+ (rolling, OPEN NOW) | [MLH Fellowship](https://fellowship.mlh.com/) |
| **NASA OSTEM** | NASA | — | Any year, US citizens (opens fall 2026) | [NASA Internships](https://intern.nasa.gov/) |

### Wave 3 — Banks (Closed for Summer 2027, Open for 2028)

| Program | Company | Status | Next Cycle |
|---|---|---|---|
| **Investment Banking** | Goldman Sachs | ❌ CLOSED (filled Dec 2025–Jan 2026) | Apply Sept 2026 for 2028 |
| **Investment Banking** | JPMorgan | ❌ CLOSED | Apply Sept 2026 for 2028 |
| **Investment Banking** | Citi / Morgan Stanley | ❌ CLOSED | Apply Sept 2026 for 2028 |
| **Point72 Academy** | Point72 | ❌ CLOSED (~50 spots) | Apply Sept 2026 for 2028 |
| **Technology Internship** | Capital One | ✅ OPEN (rising juniors, grad 2027) | [Capital One Early Career](https://www.capitalonecareers.com/get-ahead-with-early-career-programs-for-students) · [Internship Programs](https://www.capitalonecareers.com/internship-programs) |
| **Tech Summit (Pipeline)** | Capital One | ✅ OPEN (freshmen/sophomores) | [Capital One Early Career](https://www.capitalonecareers.com/get-ahead-with-early-career-programs-for-students) |
| **Engineering Accelerator** | Bloomberg | ✅ OPEN (interview fast-track) | [Bloomberg Student Programs](https://www.bloomberg.com/company/early-careers/student-programs/) |

### Specialty Programs (Any Year)

| Program | Company | Eligibility | Links |
|---|---|---|---|
| **Fellowship** | MLH | Any year, 18+ | [MLH Fellowship](https://fellowship.mlh.com/) |
| **NASA OSTEM** | NASA | Any year, US citizens | [NASA Internships](https://intern.nasa.gov/) |

---

## Master Internship Resources & Trackers

| Resource | Type | Last Updated | Purpose |
|---|---|---|---|
| **2027 Internship Calendar** | Notion (collaborative) | June 10, 2026 | Wave timing + per-firm program table | [View](https://burly-handstand-0dc.notion.site/The-2027-Internship-Calendar-Prediction-when-everything-actually-drops-37be3f8633848182be9ae0cd005e175a) |
| **Northwestern Fintech GitHub** | GitHub tracker | Ongoing | 2027 Quant Internships (real-time updates) | [View](https://github.com/northwesternfintech/2027QuantInternships) |
| **Fintech Early Programs** | Notion (curated) | June 7, 2026 | HRT / Capital One / Bloomberg deep-dive | [View](https://burly-handstand-0dc.notion.site/fintech-early-programs-that-actually-pay-not-sm-bs-unpaid-internship-lmao-378e3f863384811485e0eab2449758f2) |
| **Underclassmen List** | Notion (verified) | June 16, 2026 | 1st/2nd-year programs with short windows | [View](https://burly-handstand-0dc.notion.site/the-underclassmen-internship-list-before-u-age-out-381e3f86338481ae8062fa91002db977) |

---

## Critical Timing Insights

### Rule 1: Posted Deadlines Are Theater

**Reality:** Rolling basis means the real deadline is 2 weeks BEFORE the posted one.
- Goldman took 250k+ applications for ~2,900 spots → filled by January
- First 2 weeks of window = 70% of hires
- Months before posted deadline = 0% of hires

**Action:** Apply in the FIRST WEEK the portal opens. Do NOT wait.

### Rule 2: Read Eligibility by Grad Year, Not Class Standing

**Example Trap:**
- "Sophomore program" does NOT mean "current sophomore"
- It means "graduating in 2028"
- If you're a rising junior (graduating 2027), you're ineligible, even though you're technically in your junior year

**Action:** Check the posted grad year (e.g., "graduating 2028"). Filter programs by YOUR grad year.

### Rule 3: Know Which Programs Are Already Closed

**For summer 2027:**
- ❌ Goldman / JPMorgan / Citi / Morgan Stanley IB: CLOSED (filled Dec 2025–Jan 2026)
- ❌ Point72 Academy: CLOSED (50 spots, October fill-up)
- ✅ Quant programs (HRT, Jane Street, Two Sigma): OPEN through fall 2026
- ✅ Big Tech (Google, Microsoft, LinkedIn): OPEN Jul–Oct 2026
- ✅ Capital One / Bloomberg: OPEN (specialized tracks)

**Action:** Don't waste time on closed Wave 3 banks. Focus Wave 1 (quant) + Wave 2 (big tech).

### Rule 4: Infamously Short Windows

These open and close in 2–3 weeks. SET EMAIL ALERTS:
- NVIDIA Ignite (2–3 weeks)
- LinkedIn First Play (2–3 weeks)
- Google ASDI (1–2 weeks)

**Action:** Bookmark the careers page; check weekly; set calendar reminders for late Sept/late Oct 2026.

---

## Weekly Application Pipeline Workflow

### Friday Ritual (30 min): Weekly Deadline Check

**Cadence:** Every Friday of Aug–Nov 2026

**Checklist:**
1. Open this dashboard
2. Run "Deadlines in Next 30 Days" query
3. Check each program:
   - [ ] Are you eligible (grad year match)?
   - [ ] Has the portal opened yet?
   - [ ] If open, have you applied yet?
   - [ ] If applied, any follow-up needed (referral, status check)?
4. Update statuses in tracker
5. Add to calendar: next wave of openings

**Time tracker:** Set a 30-min Pomodoro for this

---

## Integration with Other Systems

- **[[Weekly Operating System]]** → Add Friday 15-min internship check
- **[[Tracker]]** → Link to this dashboard
- **[[MavGPT AI Resume & Job Search Guide (PDF)]]** → Use Prompt 5A (application tracking) for follow-ups
- **[[LinkedIn Search URL Cheatsheet (PDF)]]** → Research recruiters at these firms
- **[[Outreach Automation Manual (PDF)]]** → Reach out to recruiters 1 week before deadline

---

## Anti-Patterns & Traps

| Trap | Why It Fails | What to Do |
|---|---|---|
| Applying to banks (Jan 2027) for 2027 | They closed in Dec 2025; you're wasting time | Pivot to Wave 1 quant + Wave 2 big tech NOW |
| Waiting until "posted deadline" to apply | You're applying in the last week; odds are near zero | Apply in first week portal opens (50% better odds) |
| Reading "sophomore" as "current sophomore" | You're ineligible by grad year; auto-rejection | Check posted grad year (e.g., "graduating 2028") |
| Not tracking "already applied to" | You apply twice by mistake; auto-rejection | Use status tracker religiously |
| Ignoring short-window programs | You miss NVIDIA / LinkedIn by 1 day | Set email alerts on careers pages |
| Using AI tools in HRT assessment | Instant disqualification + possible offer rescind | HRT explicitly bans AI; do it yourself |
| Applying to multiple HRT postings in one cycle | You're violating their rules; auto-rejection | Choose Python OR C++ track; apply once |

---

## Open Questions for Your Dashboard

- [ ] **What is your grad year?** (This filters ~60% of programs)
- [ ] **Which specialization?** (Quant/SWE/Data? Determines wave focus)
- [ ] **Geographic preference?** (East Coast fintech vs. West Coast tech vs. remote?)
- [ ] **Do you want to bulk-create the program files**, or start with top 10 + grow?

---

## Flashcards

#cards/career

**When do you read internship eligibility?**::By **grad year**, not class standing. A "summer 2027 program" applied in fall 2026 requires you to **graduate in 2028** (or the year specified), regardless of your current year.

**What's the real deadline rule for rolling-basis internships?**::Apply in the **first 2 weeks** the portal opens, not the posted deadline. Posted deadlines are theater; rolling basis fills top spots in the first 2 weeks.

**Which wave opens first for 2027 internships?**::**Wave 1 Quant** (HRT, Jane Street, Two Sigma, Citadel) opens first (often months ahead). Then Wave 2 Big Tech (Google, Microsoft, LinkedIn). Wave 3 Banks is already closed.

**What are the three companies with infamously short application windows?**::**NVIDIA Ignite**, **Google ASDI**, and **LinkedIn First Play** — each open for 2–3 weeks only. Set email alerts on their careers pages.

**Why is HRT the highest-paying undergrad internship?**::$5,800/week ($58k base for 10 weeks) + company-paid housing, meals, and perks. Rotation through algorithm development and software engineering for quant exploration.

---

## Version History

| Date | Change |
|---|---|
| 2026-07-09 | Initial dashboard framework created; all programs + links added; dataview queries defined |

**Next:** Set up Obsidian folder structure + create program files + activate weekly ritual

