---
created: 2026-07-09
updated: 2026-07-09
type: dashboard
status: active
tags:
  - internships
  - tracking
  - career
  - wave-1
  - wave-2
  - deadline-driven
---

# 📊 Internship Tracker Dashboard — 2027 Cycle
> **Latest Update:** July 9, 2026 | **Focus:** Wave 1 Quant (NOW) + Wave 2 Big Tech (Jul–Oct 2026)

---
## ⏰ Critical Timing

| Wave | Opens | Closes | Focus | Status |
|---|---|---|---|---|
| **Wave 1 — Quant** | NOW | Fall 2026 | HRT, Jane Street, Two Sigma, Citadel | 🟢 OPEN NOW |
| **Wave 2 — Big Tech** | Jul 2026 | Oct 2026 | Google ASDI, Microsoft Explore, LinkedIn First Play | 🟡 OPENING SOON |
| **Wave 3 — Banks** | Sept 2026 | Jan 2027 (for 2028) | Goldman, JPMorgan, Citi, Morgan Stanley | 🔴 CLOSED FOR 2027 |

**⚠️ KEY RULE:** Real deadlines are 2 weeks BEFORE posted deadlines. Apply in FIRST WEEK portal opens.

---
## 🎯 Applications Due in Next 30 Days

```dataview
TABLE
  opens_date,
  deadline_real as "Real Deadline",
  pay_per_week as "Pay/Week",
  status as "Status",
  eligible_classes as "Eligible"
FROM "10_Areas/Career/Internships/Programs"
WHERE deadline_real <= date(today) + dur(30 days) AND status != "Closed"
SORT deadline_real ASC
```

---
## 📋 Application Status Overview
### 🟢 Not Started — Ready to Apply

```dataview
TABLE WITHOUT ID
  file.link as "Program",
  opens_date as "Opens",
  deadline_real as "Deadline",
  pay_per_week as "Pay/Week"
FROM "10_Areas/Career/Internships/Programs"
WHERE status = "Not Started" AND opens_date <= date(today)
SORT deadline_real ASC
```

### 🟡 Applied — Waiting for Response

```dataview
TABLE WITHOUT ID
  file.link as "Program",
  date_applied as "Applied",
  deadline_real as "Deadline",
  (date(today) - date(date_applied)) as "Days Ago"
FROM "10_Areas/Career/Internships/Programs"
WHERE status = "Applied"
SORT date_applied DESC
```

### 🟠 In Interview

```dataview
TABLE WITHOUT ID
  file.link as "Program",
  status as "Stage",
  date_applied as "Applied"
FROM "10_Areas/Career/Internships/Programs"
WHERE status = "Interview"
```

### 🟢 Offer / ✗ Rejected

```dataview
TABLE WITHOUT ID
  file.link as "Program",
  status as "Result",
  pay_per_week as "Pay/Week"
FROM "10_Areas/Career/Internships/Programs"
WHERE status IN ("Offer", "Rejected")
SORT status DESC
```

---

## 💰 Sorted by Compensation (Highest First)

```dataview
TABLE
  company as "Company",
  program_type as "Type",
  pay_per_week as "Pay/Week",
  benefits as "Benefits",
  deadline_real as "Deadline",
  status as "Status"
FROM "10_Areas/Career/Internships/Programs"
WHERE pay_per_week >= 2500
SORT pay_per_week DESC
```

---

## 🌊 Wave 1 — Quant Programs (Highest Pay, Opens NOW)

```dataview
TABLE
  eligible_classes,
  opens_date,
  deadline_real,
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE program_type = "Quant" AND wave = "Wave 1"
SORT deadline_real ASC
```

**Top Programs:**
- **Hudson River Trading** — $5,800/week + housing (sophomores, grad 2028)
- **Two Sigma First-Year** — $2,900/week (1st-year ONLY)
- **Jane Street FTTP** — $2,500–$3,000/week (1st-year ONLY)
- **Citadel Launch** — $4,300–$4,800/week (2nd-year)

**Action:** Open applications now. First 2 weeks = best odds.

---

## 🌊 Wave 2 — Big Tech Programs (Opens Jul–Oct 2026)

```dataview
TABLE
  eligible_classes,
  opens_date,
  deadline_real,
  pay_per_week,
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE program_type = "Big Tech" AND wave = "Wave 2"
SORT opens_date ASC
```

**Top Programs:**
- **Google ASDI** — 1st/2nd-year, 12 weeks, opens late Sept (SHORT WINDOW)
- **Microsoft Explore** — 1st/2nd-year, opens ~Aug
- **LinkedIn First Play** — 1st/2nd-year (INFAMOUSLY SHORT: 2–3 weeks)
- **NVIDIA Ignite** — 1st/2nd-year (SHORT WINDOW)
- **MLH Fellowship** — Any year, OPEN NOW rolling

---

## ✅ Programs You're Eligible For

**Filter by your grad year (replace with YOUR year):**

```dataview
TABLE
  company,
  program_type,
  eligible_classes,
  opens_date,
  deadline_real as "Deadline",
  pay_per_week as "Pay/Week",
  status
FROM "10_Areas/Career/Internships/Programs"
WHERE contains(eligible_classes, "2027") AND status != "Closed"
SORT deadline_real ASC
```

---

## 📊 Stats & Insights

### Application Funnel

```dataview
TABLE WITHOUT ID
  rows.status as "Status",
  length(rows) as "Count"
FROM "10_Areas/Career/Internships/Programs"
GROUP BY status
```

### Total Opportunities Tracked

**Total Programs:** (auto-count below)

```dataview
LIST
FROM "10_Areas/Career/Internships/Programs"
LIMIT 1
```

---

## 🎯 This Week's Action Items

**[ ] Friday — Weekly Deadline Check (30 min ritual)**
- [ ] Update program statuses
- [ ] Check which portals have opened
- [ ] Apply to any newly-opened programs
- [ ] Check on applications from 1 month ago (follow-up)

**[ ] Set Calendar Reminders**
- [ ] NVIDIA Ignite (watch late Aug)
- [ ] Google ASDI (watch late Sept)
- [ ] LinkedIn First Play (watch late Nov)

**[ ] Reach Out to Recruiters**
- Use [[LinkedIn Search URL Cheatsheet (PDF)]] to find recruiters at HRT/Jane Street/Two Sigma
- Schedule warm outreach for next week

---

## 📚 Resources & Links

**Master Reference:** [[Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline]]

**External Trackers:**
- [2027 Internship Calendar (Notion)](https://burly-handstand-0dc.notion.site/The-2027-Internship-Calendar-Prediction-when-everything-actually-drops-37be3f8633848182be9ae0cd005e175a)
- [Northwestern Fintech GitHub](https://github.com/northwesternfintech/2027QuantInternships)

**Direct Program Links:**
- [Hudson River Trading](https://www.hudsonrivertrading.com/student-opportunities/)
- [Capital One Early Career](https://www.capitalonecareers.com/get-ahead-with-early-career-programs-for-students)
- [Bloomberg Student Programs](https://www.bloomberg.com/company/early-careers/student-programs/)
- [Google Careers](https://www.google.com/about/careers/applications/)
- [Microsoft Explore](https://careers.microsoft.com/v2/global/en/exploremicrosoft)
- [MLH Fellowship](https://fellowship.mlh.com/)
- [NASA Internships](https://intern.nasa.gov/)

---

## 🗂️ Folder Structure

```
10_Areas/
  Career/
    Internships/
      📄 Internship Tracker — Dashboard.md (THIS FILE)
      📄 Internship Resources.md
      📄 2027 Internship Calendar Summary.md
      
      Programs/
      📄 2026-HRT-Sophomore.md
      📄 2026-TwoSigma-FirstYear.md
      📄 2026-JaneStreet-FTTP.md
      📄 2026-Citadel-Launch.md
      📄 2026-GoogleASID.md
      📄 2026-Microsoft-Explore.md
      ... (one file per program)
```

---

## 📅 Last Updated

- **Dashboard:** July 9, 2026
- **Programs:** July 9, 2026
- **Links Verified:** July 9, 2026
- **Next Review:** July 16, 2026 (Friday weekly ritual)

---

**Next Step:** Create program files in the `/Programs` folder using the template below.
