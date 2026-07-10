---
created: 2026-07-09
type: setup
---

# 🎯 Internship Tracker Setup Guide

**Status:** Ready to deploy | **Last Updated:** July 9, 2026

---

## What You're Getting

A complete internship tracking system for the **2027 summer cycle** that combines:
- 📅 **Wave timing calendar** (Quant → Big Tech → Banks)
- 📊 **Application dashboard** with live dataview queries
- 📋 **Program tracker** (one file per internship program)
- 🔗 **Working links** to all official career pages
- ⏰ **Deadline automation** (alerts for next 30 days)
- 📈 **Status tracking** (Not Started → Applied → Interview → Offer/Rejected)

---

## Files Created

### Core Files (Read These First)

1. **`Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline.md`**
   - Master reference document
   - All programs listed with descriptions
   - Core framework + dataview queries
   - Workflow instructions
   - **Read first:** This is your bible

2. **`Internship Tracker — Dashboard.md`**
   - Live dashboard with dataview queries
   - Application status overview
   - Deadline alerts (next 30 days)
   - Wave organization (Wave 1 Quant, Wave 2 Big Tech, Wave 3 Banks)
   - **Use daily:** This is your working interface

### Program Files (Templates to Populate)

3. **`Programs/2026-HRT-Sophomore.md`** (Sample/Template)
   - Full example of how to structure program files
   - Use as template for other programs
   - Copy YAML frontmatter + customize

4. **`Programs-to-Create.md`**
   - Quick-reference with all 13 programs ready to copy-paste
   - YAML frontmatter pre-filled
   - Just create files and update company-specific details

### Support Files

5. **`Internship Resources.md`** (TBD — add link summary)
   - Resource links
   - External trackers
   - Recruiter contact templates

---

## Quick Start (30 minutes)

### Step 1: Read the Master Document (10 min)
```
Open: Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline.md
Read: Sections 1–5 (Executive Summary through Core Framework)
```

### Step 2: Open the Dashboard (2 min)
```
Open: Internship Tracker — Dashboard.md
Bookmark this (you'll use it every Friday)
```

### Step 3: Create Program Files (15 min)
```
1. Open: Programs-to-Create.md
2. Create 13 new .md files in Programs/ folder:
   - 2026-HRT-Sophomore.md
   - 2026-TwoSigma-FirstYear.md
   - 2026-JaneStreet-FTTP.md
   ... (list of 13 total)
3. Copy YAML + update company details
4. Leave status = "Not Started" for all
```

### Step 4: Verify Dashboard Updates (3 min)
```
Return to: Internship Tracker — Dashboard.md
Refresh page (Cmd+R or Ctrl+R)
You should see all 13 programs populate in dataview tables
```

---

## File Structure (What to Create)

```
10_Areas/
  Career/
    Internships/
      📄 README.md (THIS FILE)
      📄 Internship Tracker — Dashboard.md (MAIN BOARD)
      📄 Internship Tracking Dashboard — 2027 Calendar... (MASTER REF)
      📄 Programs-to-Create.md (TEMPLATE GUIDE)
      📄 Internship Resources.md (LINKS + EXTERNAL REFS)
      
      Programs/  ← CREATE THIS FOLDER
      📄 2026-HRT-Sophomore.md (TEMPLATE/SAMPLE)
      📄 2026-TwoSigma-FirstYear.md
      📄 2026-JaneStreet-FTTP.md
      📄 2026-Citadel-Launch.md
      📄 2026-DEShaw-Fellowships.md
      📄 2026-Google-ASDI.md
      📄 2026-Microsoft-Explore.md
      📄 2026-LinkedIn-FirstPlay.md
      📄 2026-NVIDIA-Ignite.md
      📄 2026-MLH-Fellowship.md
      📄 2026-CapitalOne-Tech.md
      📄 2026-Bloomberg-Engineering.md
      📄 2026-NASA-OSTEM.md
```

---

## How to Use

### Daily (Takes 2 min)
```
Open: Internship Tracker — Dashboard.md
Scan: "Applications Due in Next 30 Days" section
Action: If any portal has opened → apply immediately
```

### Weekly (Takes 30 min — Friday Ritual)
```
1. Open: Internship Tracker — Dashboard.md
2. Update all program statuses:
   - Check which portals opened this week
   - Mark "Not Started" → "Applied" for any you submitted
   - Check on applications from 1 month ago (follow-up time?)
3. Refresh dataview queries (they auto-update)
4. Log: Add to [[02 - Weekly Operating System]] notes
```

### Monthly (Takes 1 hour)
```
1. Re-read: "Wave 1 — Quant Programs" section (check if windows shifted)
2. Update: deadline_real dates if portals announced changes
3. Refresh: External tracker links (Notion calendar, GitHub)
4. Log: Which programs you applied to + results so far
```

---

## Integration with Your System

### Link to Existing Notes
- **[[02 - Weekly Operating System]]** → Add Friday internship check
- **[[Tracker]]** → Link to this dashboard
- **[[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]** → Portfolio projects + internships are both 20% of interview weight
- **[[MavGPT AI Resume & Job Search Guide (PDF)]]** → Use Prompt 5A (application tracking) for follow-ups
- **[[LinkedIn Search URL Cheatsheet (PDF)]]** → Research recruiters at these firms

### Dataview Dependencies
All queries run on files in `10_Areas/Career/Internships/Programs/` with these frontmatter fields:
```yaml
name:
company:
program_type: (Quant / Big Tech / Bank / Fellowship)
eligible_classes: (Freshman / Sophomore / Junior / Senior)
grad_year: (2027 / 2028 / 2029)
wave: (Wave 1 / Wave 2 / Wave 3)
opens_date:
deadline_real:
pay_per_week:
status: (Not Started / Applied / Interview / Offer / Rejected)
```

---

## Key Timelines

### Right Now (July 2026)
- [ ] Create all 13 program files
- [ ] Verify dashboard shows all programs
- [ ] Read the master reference doc

### August 2026 (Wave 1 Opens)
- [ ] HRT portal opens (~Aug 1)
- [ ] Apply to HRT immediately (first 2 weeks = best odds)
- [ ] Two Sigma, Jane Street, Citadel, D.E. Shaw open
- [ ] Apply to Wave 1 quant programs (HIGHEST PAY)

### September 2026 (Wave 1 Continues + Wave 2 Opens)
- [ ] Continue following up on Wave 1 applications
- [ ] Google ASDI opens (late Sept, 1–2 week window)
- [ ] Microsoft Explore opens (~Aug-Sept)
- [ ] NVIDIA Ignite opens (SHORT WINDOW)
- [ ] Watch for interview requests from Wave 1 firms

### October 2026 (Wave 1 Ends + Wave 2 In Full Swing)
- [ ] Real deadlines for most Wave 1 programs (~Oct 15)
- [ ] Wave 2 programs in full swing
- [ ] ASDI, Explore, Ignite windows closing
- [ ] LinkedIn First Play NOT YET (watch for late November)

### November 2026 (Wave 2 Late + LinkedIn/NASA)
- [ ] LinkedIn First Play opens (late Nov, 2–3 week window) ⏰
- [ ] NASA OSTEM opens (fall 2026)
- [ ] Wave 2 deadlines

### December 2026–January 2027 (Wave 3 Decisions + Planning)
- [ ] Wave 1 offer decisions rolling in
- [ ] Wave 2 interviews happening
- [ ] Wave 3 (banks) starts recruiting for summer 2028
- [ ] Update dashboard with results

---

## All Working Links (Updated July 9, 2026)

### Wave 1 — Quant
- [Hudson River Trading](https://www.hudsonrivertrading.com/student-opportunities/)
- [Two Sigma Careers](https://careers.twosigma.com/careers/InternshipsAndEarlyCareers)
- [Jane Street Careers](https://www.janestreet.com/apply/)
- [Citadel Launch](https://www.citadel.com/careers/details/launch-intern-us/)
- [D.E. Shaw](https://www.deshaw.com/careers)

### Wave 2 — Big Tech
- [Google Careers](https://www.google.com/about/careers/applications/) (search "ASDI")
- [Microsoft Explore](https://careers.microsoft.com/v2/global/en/exploremicrosoft)
- [LinkedIn First Play](https://careers.linkedin.com/pathways-programs/internships/Technical/first-play)
- [NVIDIA Careers](https://www.nvidia.com/careers/)
- [MLH Fellowship](https://fellowship.mlh.com/)

### Wave 3 — Banks & Specialty
- [Capital One](https://www.capitalonecareers.com/get-ahead-with-early-career-programs-for-students)
- [Bloomberg Student Programs](https://www.bloomberg.com/company/early-careers/student-programs/)
- [NASA OSTEM](https://intern.nasa.gov/)

### External Trackers
- [2027 Internship Calendar (Notion)](https://burly-handstand-0dc.notion.site/The-2027-Internship-Calendar-Prediction-when-everything-actually-drops-37be3f8633848182be9ae0cd005e175a)
- [Northwestern Fintech GitHub](https://github.com/northwesternfintech/2027QuantInternships)

---

## Success Metrics

By end of 2026, you should have:
- [ ] Applied to 5+ Wave 1 quant programs (HRT, Two Sigma, Jane Street, Citadel, D.E. Shaw)
- [ ] Applied to 3+ Wave 2 big tech programs (Google ASDI, Microsoft Explore, LinkedIn First Play)
- [ ] Received phone screen invites from 3+ firms
- [ ] Reached on-site interview for 1+ firm
- [ ] Ideally: offer(s) in hand by January 2027

---

## Troubleshooting

### Dataview Queries Not Showing Programs
**Problem:** Dashboard shows "No results" in dataview tables  
**Solution:**
1. Create all program files in `10_Areas/Career/Internships/Programs/` folder
2. Ensure YAML frontmatter has all required fields (name, company, program_type, etc.)
3. Refresh page (Cmd+R or Ctrl+R)
4. Check that file path is exactly `10_Areas/Career/Internships/Programs/*`

### Programs Not Filtering Correctly
**Problem:** Dashboard filters by grad year aren't working  
**Solution:**
1. Check YAML field `grad_year` is filled (e.g., `grad_year: 2028`)
2. Update `eligible_classes` field with multi-select list (not text)
3. Verify dataview query uses correct folder path

### Links Are Broken
**Problem:** Career page links redirect or 404  
**Solution:**
1. Links verified July 9, 2026 (they may shift by fall)
2. Always go to company careers page directly and search
3. Example: search "Associate Software Developer Intern" on Google Careers
4. Update link in program file if it changes

---

## Anti-Patterns to Avoid

1. ❌ **Waiting until "posted deadline"** to apply
   - ✅ Apply in first week portal opens (50% better odds)

2. ❌ **Ignoring short-window programs**
   - ✅ Set email alerts for Google ASDI, LinkedIn First Play, NVIDIA Ignite

3. ❌ **Applying to banks in Dec 2026 for summer 2027**
   - ✅ Banks already closed (filled Dec 2025–Jan 2026); apply Sept 2026 for 2028

4. ❌ **Forgetting to update program files after you apply**
   - ✅ Update status immediately when you submit (dashboard depends on it)

5. ❌ **Not following up on applications from 1+ month ago**
   - ✅ Use [[MavGPT AI Resume & Job Search Guide (PDF)]] Prompt 5A for follow-ups

---

## Next Steps

1. **This Week:**
   - [ ] Read master reference doc (1 hour)
   - [ ] Create `/Programs/` folder structure
   - [ ] Create all 13 program files (using Programs-to-Create.md template)
   - [ ] Bookmark dashboard for daily use

2. **By Aug 1:**
   - [ ] HRT portal opens
   - [ ] Apply to HRT (+ all Wave 1 quant programs if open)
   - [ ] Update dashboard status to "Applied"

3. **Ongoing:**
   - [ ] Friday 30-min ritual: check deadlines + update statuses
   - [ ] Set email alerts on short-window programs
   - [ ] Follow up on applications 1 month after submission

---

## Support & Context

- **Master Reference:** [[Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline]]
- **Weekly Planning:** [[02 - Weekly Operating System]]
- **Career Track:** [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]
- **Resume Tailoring:** [[MavGPT AI Resume & Job Search Guide (PDF)]]
- **Recruiter Outreach:** [[LinkedIn Search URL Cheatsheet (PDF)]], [[Outreach Automation Manual (PDF)]]

---

**Version:** 1.0  
**Status:** Ready to deploy  
**Next Review:** August 1, 2026 (when Wave 1 opens)

🚀 **You're set. Good luck!**
