---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Internship loop review system"
started_at: 2026-08-23T15:58:26
ended_at: 2026-08-23T16:20:58
exported_at: 2026-08-24T01:30:03
duration_minutes: 22.5
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: f44d2a57-b9fe-450a-8fb8-ed5b08d845ca
status: raw
turn_count: 2
tools_used:
  Bash: 18
  Edit: 1
  Grep: 6
  Read: 19
  Write: 6
tokens:
  input: 168
  output: 114887
  cache_creation: 435450
  cache_read: 9774226
  total: 10324731
cost_usd: 4.845851
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\1 - AI & ML\\2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\3 - CyS & Finance\\Quantitative Trading Intern - Virtu.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Programs\\Considering\\Software Engineering Intern - Appian.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\Tracker\\Each One\\Current\\Software Engineering Intern - Appian.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Applying\\Now.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\Source of Truth.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\System - Build Log.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship Loop Review Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship Notes Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\MOC Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Review Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Capability\\AI Tools Monthly Review Template.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Capability\\AI Tools Weekly Review Template.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Career\\Internship Loop Monthly Review Template.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Career\\Internship Loop Weekly Review Template.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Internship - Design Rationale.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Workflows\\Internship Pipeline.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\07_AI_Information\\Jarvis Writing and Formatting.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\50_Reviews Board.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\AI\\Scheduled\\Weekly\\AI Tools Weekly Review — 2026-W34.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Internship Loop Reviews MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Scheduled\\Monthly\\Internship Loop Monthly Review — 2026-08.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\30_Reviews\\Internship Loop\\Scheduled\\Weekly\\Internship Loop Weekly Review — 2026-W34.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\HUMAN_WRITING.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Internship loop review system

## You

Currently in the process of updating the internship-research-loop. There are way too many things that need to be updated over here. But I just noticed that there is no review system built out for this automated process - especially the dossiers. There should be a review system for each step that takes place for an internship application. There are things that need to be established after the notes inside @30_Order\ are updated in a different session. Currently we are lacking concrete definitions for each and every note that is going to be created. Before that session has completed it's work on refining notes - let's establish the review system created over here: `60_Claude/30_Reviews/Internship Loop`.

## Claude

I'll start by mapping the relevant structure: the existing (if any) review system folder, the internship loop automation, and the 30_Order standards that govern dossiers.

Now the two templates.

Now the first real Weekly Discovery Review, using the evidence gathered.

Now let me add the small cross-link from Dossiers MOC to the new Weekly review, and verify all wikilinks in the new files actually resolve.

All files pass formatting rules (exactly 2 `---` markers for frontmatter, zero stray blank lines). The review system is fully established.

## Summary

Built the review system at `60_Claude/30_Reviews/Internship Loop/`:

- **`30_Order/Standards/Internship Loop Review Standard.md`** — new Standard defining two review types split along the pipeline's own automated/manual boundary: a **Weekly Discovery Review** (Step 1 — the automated dossier loop) and a **Monthly Promotion Review** (Steps 2-9 — Program/Contact/Tracker/Applying notes). It explicitly flags that the Monthly review's per-note-type checks are provisional until the parallel `30_Order` note-definition session lands concrete field specs — named as a dependency, not silently ignored.
- Two templates in `30_Order/Templates/Career/` matching that structure.
- An index MOC and `Scheduled/Weekly/`, `Scheduled/Monthly/` folders under `60_Claude/30_Reviews/Internship Loop/`.
- One cross-link added from `Dossiers MOC.md` so the review system isn't a floating note.

I also ran the **first real review of each type** rather than leaving the system untested, and both surfaced genuine defects:

**Weekly Discovery Review** (12-dossier sample + full-corpus greps):
- `notes:` interlink field (spec'd as shipped 2026-07-30) is present on only **11 of 392** live dossiers
- `company/<slug>` tag present on only **69 of 392**
- A real gate-conformance miss: Virtu's "Quantitative Trading Intern" is pure trading-strategy work that Source of Truth's own rule says should be rejected outright
- An exact-URL cross-source duplicate (two Virtu Financial dossiers, same Greenhouse job ID, one day apart)

**Monthly Promotion Review**:
- 4 of 5 `Programs/Serious/` entries (Deepgram, Nuro, Uber, Western Digital) have a Program note but no Contacts or Tracker note, violating the Pipeline's "created together" rule
- HRT-Sophomore has sat in `Serious/` for 5+ weeks despite being withdrawn the same day it was created, per the Build Log
- Appian's Tracker note's "no rush" reasoning cites an August review-start date that has since arrived

No fixes were applied — per the Review Standard's own rule, a review names problems but doesn't self-authorize fixing them.

### Tool Calls

- `Bash` -- `echo "--- 60_Claude/30_Reviews ---"; ls -la "60_Claude/30_Reviews" 2>&1; echo "--- 30_Order/Standards ---"; ls "30_Order/Standards" 2>&1; echo "--- 30_Order/Templates ---"; ls "30_Order/Templates" 2>&1; echo "--- 30_Order/Workflows ---"; ls "30_Order/Workflows" 2>&1; echo "--- Internship related dirs ---"; find "10_Areas/Career/Internships" -maxdepth 2 2>&1`
```
--- 60_Claude/30_Reviews ---
total 57
drwxr-xr-x 1 Anant Gupta 197121     0 Aug 23 15:20 .
drwxr-xr-x 1 Anant Gupta 197121     0 Jun 24 16:46 ..
-rw-r--r-- 1 Anant Gupta 197121   500 May 31 01:11 50_Reviews Board.md
drwxr-xr-x 1 Anant Gupta 197121     0 Aug  9 13:24 AI
drwxr-xr-x 1 Anant Gupta 197121     0 Aug 23 15:20 Internship Loop
-rw-r--r-- 1 Anant Gupta 197121  1728 Aug 10 10:59 Jarvis Enrichment Phase 1 - 2026-04-24.md
drwxr-xr-x 1 Anant Gupta 197121     0 Jun 24 17:34 Monthly
-rw-r--r-- 1 Anant Gupta 197121 10203 Jun 11 18:50 North Star Convergence — Change Report 2026-06-11.md
drwxr-xr-x 1 Anant Gupta 197121     0 Aug 22 14:34 Ops Reports
-rw-r--r-- 1 Anant Gupta 197121  2718 Jul 27 16:09 Today - 2026-06-03.md
-rw-r--r-- 1 Anant Gupta 197121 26000 Jun 24 17:15 Vault-Audit-2026-05-29.md
drwxr-xr-x 1 Anant Gupta 197121     0 May 28 17:34 Weekly Synthesis
--- 30_Order/Standards ---
Action Standard.md
Brief Standard.md
Concept Standard.md
Course Week Standard.md
Daily Workflow Standard.md
Evergreen Standard.md
Internship Notes Standard.md
Log Standard.md
MOC Standard.md
Project Standard.md
Review Standard.md
Source Summary Standard.md
Tracking Standard.md
--- 30_Order/Templates ---
Capability
Career
Classes
Enumerate
Frontmatter
MOC.md
--- 30_Order/Workflows ---
00_Workflows Index.md
Brief to Action.md
Brief to Progress.md
Capture to Summary.md
Conversation Capture.md
Enrichment.md
Internship - Design Rationale.md
Internship Pipeline.md
Output with Provenance.md
Plan Review Cadence.md
Promotion.md
Summary to Distilled.md
Transcript to Brief.md
--- Internship related dirs ---
10_Areas/Career/Internships
10_Areas/Career/Internships/Cheats
10_Areas/Career/Internships/Cheats/LinkedIn Premium.md
10_Areas/Career/Internships/Cheats/Resume Tailoring, LinkedIn Search & Outreach Discovery.md
10_Areas/Career/Internships/Contacts
10_Areas/Career/Internships/Contacts/Contacts MOC.md
10_Areas/Career/Internships/Contacts/Each One
10_Areas/Career/Internships/Contacts/Mimic.md
10_Areas/Career/Internships/Contacts/Networking Strategies.md
10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status.md
10_Areas/Career/Internships/Internships Hub.md
10_Areas/Career/Internships/Links & Interlinks.md
10_Areas/Career/Internships/List
10_Areas/Career/Internships/List/2026-07 Found.md
10_Areas/Career/Internships/List/Dossiers
10_Areas/Career/Internships/List/Dossiers MOC.md
10_Areas/Career/Internships/List/Excluded — Losing The Debate.md
10_Areas/Career/Internships/List/Resources.md
10_Areas/Career/Internships/List/Run Log.md
10_Areas/Career/Internships/Programs
10_Areas/Career/Internships/Programs/Considering
10_Areas/Career/Internships/Programs/Job & Company
10_Areas/Career/Internships/Programs/Programs MOC.md
10_Areas/Career/Internships/Programs/Programs-to-Create.md
10_Areas/Career/Internships/Programs/Serious
10_Areas/Career/Internships/README.md
10_Areas/Career/Internships/Tracker
10_Areas/Career/Internships/Tracker/Application Tracker.md
10_Areas/Career/Internships/Tracker/Each One
10_Areas/Career/Internships/Tracker/Habit Tracker.md
10_Areas/Career/Internships/Tracker/Internship - Dashboard.md
10_Areas/Career/Internships/Tracker/Tracker.md
```
- `Grep` -- pattern `internship` path `.claude`
- `Bash` -- `echo "--- Internship Loop folder contents ---"; find "60_Claude/30_Reviews/Internship Loop" -type f 2>&1; echo "--- Dossiers structure ---"; find "10_Areas/Career/Internships/List/Dossiers" -maxdepth 2 -type d 2>&1; echo "--- sample dossier count ---"; find "10_Areas/Career/Internships/List/Dossiers" -name "*.md" | wc -l`
```
--- Internship Loop folder contents ---
--- Dossiers structure ---
10_Areas/Career/Internships/List/Dossiers
10_Areas/Career/Internships/List/Dossiers/1 - AI & ML
10_Areas/Career/Internships/List/Dossiers/2 - Fullstack
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance
10_Areas/Career/Internships/List/Dossiers/Other
10_Areas/Career/Internships/List/Dossiers/Viewed
--- sample dossier count ---
398
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Review Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Notes Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship Pipeline.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Workflows\Internship - Design Rationale.md`
- `Bash` -- `echo "--- Source of Truth ---"; find . -iname "Source of Truth.md" -path "*Internship*" 2>&1
echo "--- System - Build Log ---"; find . -iname "System - Build Log.md" 2>&1
echo "--- Dossiers-to-Create ---"; find . -iname "Dossiers-to-Create.md" 2>&1
echo "--- sample dossier ---"; find "10_Areas/Career/Internships/List/Dossiers/1 - AI & ML" -name "*.md" | head -1`
```
--- Source of Truth ---
./20_Progress/Internship/Building System/Source of Truth.md
./60_Claude/40_Project_Briefs/Internship/Source Of Truth.md
--- System - Build Log ---
./20_Progress/Internship/Building System/System - Build Log.md
--- Dossiers-to-Create ---
./10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md
--- sample dossier ---
10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md
```
- `Grep` -- pattern `30_Reviews|Review Standard|review system` path `AGENTS.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\50_Reviews Board.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\1 - AI & ML\2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Source of Truth.md`
- `Grep` -- pattern `Write Contract|Where does this note go|30_Reviews` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\AGENTS.md`
- `Grep` -- pattern `30_Reviews|Write Contract" -A 60` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\AGENTS.md`
- `Bash` -- `echo "--- Ops Reports sample ---"; ls "60_Claude/30_Reviews/Ops Reports" | head -5
echo "--- AI reviews structure ---"; find "60_Claude/30_Reviews/AI" -maxdepth 3
echo "--- 00_Workflows Index for review mentions ---"; grep -n -i "review" "30_Order/Workflows/00_Workflows Index.md"`
```
--- Ops Reports sample ---
Jarvis Ops Report - 2026-04-24 20260424-170132.md
--- AI reviews structure ---
60_Claude/30_Reviews/AI
60_Claude/30_Reviews/AI/Conversations
60_Claude/30_Reviews/AI/Scheduled
60_Claude/30_Reviews/AI/Scheduled/Monthly
60_Claude/30_Reviews/AI/Scheduled/Weekly
60_Claude/30_Reviews/AI/Scheduled/Weekly/AI Tools Weekly Review — 2026-W34.md
60_Claude/30_Reviews/AI/Tools
60_Claude/30_Reviews/AI/Tools/Claude Kit
60_Claude/30_Reviews/AI/Tools/Tool log.md
--- 00_Workflows Index for review mentions ---
51:| Create a plan, or keep an existing one wired into daily/weekly execution | [[Plan Review Cadence]] |
```
- `Grep` -- pattern `Write Contract` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\AGENTS.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\AI\Scheduled\Weekly\AI Tools Weekly Review — 2026-W34.md`
- `Grep` -- pattern `## Write Contract` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\AGENTS.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\System - Build Log.md`
- `Bash` -- `echo "--- Templates/Capability ---"; ls "30_Order/Templates/Capability"
echo "--- Templates/Career ---"; ls "30_Order/Templates/Career"
echo "--- AI Tools Weekly Review Template ---"`
```
--- Templates/Capability ---
Action Template.md
AI Tools Monthly Review Template.md
AI Tools Weekly Review Template.md
Brief Template.md
Clipping Distill Template.md
Deep Dive Template.md
Depth Ladder Template.md
Field OS Template.md
MOC Template.md
Monthly Synthesis Template.md
Output Template.md
Question Bank Template.md
Synthesis Template.md
Weekly Synthesis Template.md
--- Templates/Career ---
Applying Template.md
Cheat Template.md
Contact Template.md
Job & Company Template.md
LinkedIn Post Template.md
List Monthly Log Template.md
Plan Template.md
Program Template.md
Tracking Template.md
--- AI Tools Weekly Review Template ---
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Capability\AI Tools Weekly Review Template.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Capability\AI Tools Monthly Review Template.md`
- `Bash` -- `echo "--- dossier counts per bucket (excluding Viewed) ---"
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  c=$(find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | wc -l)
  echo "$d: $c"
done
echo "Viewed: $(find "10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" | wc -l)"
echo "--- total non-Viewed ---"
find "10_Areas/Career/Internships/List/Dossiers" -maxdepth 2 -name "*.md" -not -path "*/Viewed/*" | wc -l
echo "--- how many dossiers HAVE a notes: field ---"
grep -rl "^notes:" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | wc -l
echo "--- how many dossiers have a company/ tag ---"
grep -rl "company/" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | wc -l
echo "--- most recent 5 dossiers by mtime ---"
find "10_Areas/Career/Internships/List/Dossiers" -name "*.md" -not -path "*/Viewed/*" -printf "%T@ %p\n" 2>/dev/null | sort -rn | head -5`
```
--- dossier counts per bucket (excluding Viewed) ---
1 - AI & ML: 146
2 - Fullstack: 43
3 - CyS & Finance: 63
Other: 139
Viewed: 6
--- total non-Viewed ---
392
--- how many dossiers HAVE a notes: field ---
11
--- how many dossiers have a company/ tag ---
69
--- most recent 5 dossiers by mtime ---
1787484602.9852842000 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Graduate Level Co-op – Data Scientist – Plymouth, MN – Summer 2027 - Philips.md
1787484602.7454268000 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Image Processing Co-op - Specter Aerospace.md
1787484601.7626566000 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/GPUAI Application System Software Engineer Intern - ByteDance.md
1787484600.7983955000 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Full Stack Web Development Co-op - Spring 2027 - Draper.md
1787484600.2399028000 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Data Science Intern - Notion.md
```
- `Bash` -- `echo "--- check for local repo clone ---"
find / -maxdepth 6 -iname "internship-research-loop" -type d 2>/dev/null
echo "--- dates on notes:-having dossiers ---"
grep -rl "^notes:" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | xargs -I{} grep -H "date_found:" {} | head -15`
```
--- check for local repo clone ---
--- dates on notes:-having dossiers ---
10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern, AIML & LLM - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern, CoreAI - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineer Intern, Cloud & Distributed Backend - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineer Intern, Fullstack Product (Web + Services) - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/Other/Software Engineer Intern, Data PlatformAnalytics - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/Other/Software Engineer Intern, Security & Identity - Microsoft.md:date_found: '2026-08-21'
10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security Intern - Capital One (2).md:date_found: '2026-08-03'
10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security IT Intern - CNO Financial Group (2).md:date_found: '2026-08-06'
10_Areas/Career/Internships/List/Dossiers/Viewed/Data Internship - Data & AI Program - JP Morgan Chase (2).md:date_found: '2026-08-03'
10_Areas/Career/Internships/List/Dossiers/Viewed/Software Engineer Intern - Capital One (2).md:date_found: '2026-08-03'
```
- `Bash` -- `echo "--- Appian Program note ---"; find "10_Areas/Career/Internships/Programs" -iname "*Appian*"
echo "--- Appian Contact note ---"; find "10_Areas/Career/Internships/Contacts" -iname "*Appian*"
echo "--- Appian Tracker note ---"; find "10_Areas/Career/Internships/Tracker" -iname "*Appian*"
echo "--- Applying folder ---"; find "20_Progress/Internship/Applying" -maxdepth 2
echo "--- date command check ---"; date -d 2026-08-23 +%G-W%V 2>&1 || python3 -c "import datetime; print(datetime.date(2026,8,23).isocalendar())"`
```
--- Appian Program note ---
10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md
--- Appian Contact note ---
10_Areas/Career/Internships/Contacts/Each One/Ongoing/Software Engineering Intern - Appian.md
--- Appian Tracker note ---
10_Areas/Career/Internships/Tracker/Each One/Current/Software Engineering Intern - Appian.md
--- Applying folder ---
20_Progress/Internship/Applying
20_Progress/Internship/Applying/2026-HRT-Sophomore.md
20_Progress/Internship/Applying/AI Applying.md
20_Progress/Internship/Applying/Applications-to-Create.md
20_Progress/Internship/Applying/Applied
20_Progress/Internship/Applying/Now.md
--- date command check ---
2026-W34
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Programs\Considering\Software Engineering Intern - Appian.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\Tracker\Each One\Current\Software Engineering Intern - Appian.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Applying\Now.md`
- `Bash` -- `find "10_Areas/Career/Internships/List/Dossiers" -iname "*Appian*"`
```
10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineering Intern - Appian.md
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Information Security Engineer Intern - Appian.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\HUMAN_WRITING.md`
- `Bash` -- `find . -iname "Jarvis Writing and Formatting*" 2>&1`
```
./60_Claude/07_AI_Information/Jarvis Writing and Formatting.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Jarvis Writing and Formatting.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\MOC Standard.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers MOC.md`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Loop Review Standard.md`
```
---
type: evergreen
status: sprout
created: 2026-08-23
tags:
  - system
  - standards
  - internship
  - review
notes:
  - "[[30_Order/Standards/Review Standard]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
next: "First run of both review types shipped 2026-08-23. Tighten the Monthly review's Note-Shape Conformance section once the parallel 30_Order note-definition session lands concrete field specs for Program/Contact/Tracker/Applying/Job & Company notes — see that section's own warning."
---
# Internship Loop Review Standard
==A review here checks the internship-research-loop's actual output against what it was designed to do — [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s gates and [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]'s content rules — never a summary of dossier counts alone.== This is the content standard for `60_Claude/30_Reviews/Internship Loop/Scheduled/{Weekly,Monthly}/`. It is a sibling of [[30_Order/Standards/Review Standard|Review Standard]], not a replacement — that note's shared rigor rules (cite the actual rows/files read, "nothing to report" is a valid finding, `Decided Fixes` only at 100% clarity, no `---` in the body, zero blank lines except after a callout) apply here unchanged. This note states only what's different for the internship loop: two review types, split by which half of [[30_Order/Workflows/Internship Pipeline|the pipeline]] they cover, because the two halves fail in completely different ways — Step 1 (Find) is automated code that breaks in reproducible, bug-shaped ways; Steps 2-9 are human judgment calls that stall in note-hygiene-shaped ways.
## Why Two Review Types, Not One
[[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] itself splits the system this way: "Discovery is a GitHub Actions workflow... mechanical, unattended, cheap by design. Promotion onward is entirely manual, human-judgment-driven." A single review covering both would either drown the rare, high-stakes promotion decisions in weekly dossier noise, or let the automated half's real, recurring bugs (see [[20_Progress/Internship/Building System/System - Build Log|Build Log]]'s 2026-07-26 and 2026-07-29 entries — Databricks PM misclassification, Mosaic "threat" false-positive, Aquatic/Google cross-source dedup misses, the Google-careers-page extraction bug, all confirmed *recurring* three days after "fixed") go unchecked for a month at a time.
- **Weekly — Discovery Review.** Covers Step 1 (Find) only: `List/Dossiers/`, the hourly loop. Runs weekly because the loop writes hourly and the historical bug list above was only ever found by someone actually reading real dossiers, not by trusting the commit log.
- **Monthly — Promotion Review.** Covers Steps 2-9 (Screen through Close): `Programs/`, `Contacts/`, `Tracker/`, `20_Progress/Internship/Applying/`, `Preperation/`. Runs monthly because this half is still lightly exercised (one real promotion, Appian, as of 2026-08-23 per [[20_Progress/Internship/Building System/System - Build Log|Build Log]]) — a weekly cadence would mostly report "nothing new," which the general Review Standard already treats as padding to avoid.
## A Known Dependency — Read Before Running The Monthly Review
> [!WARNING]
> The Monthly review's **Note-Shape Conformance** section (below) grades Program/Contact/Tracker/Applying/Job & Company notes against what [[30_Order/Templates/Career/Program Template|Program Template]], `Contact Template`, `Tracking Template`, and `Applying Template` plus [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s prose already specify — not against a fixed, field-level standard, because none exists yet for these note types (only dossiers have one, [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]). A separate session is refining concrete definitions for every note type under `30_Order/`. Until that lands, treat this section's findings as provisional and re-derive them once the real standard exists — do not let a stale provisional finding calcify into an assumed rule.
## Maps To
- Templates: [[30_Order/Templates/Career/Internship Loop Weekly Review Template|Internship Loop Weekly Review Template]], [[30_Order/Templates/Career/Internship Loop Monthly Review Template|Internship Loop Monthly Review Template]]
## Used By Workflow
- Manual, human-triggered, same as the general Review Standard — no cron writes a review. Open the relevant template and work it against the real vault state, the same session or shortly after the period it covers.
## Per-Heading Standard — Weekly Discovery Review
### Period Covered
The exact 7-day range.
### Sources Reviewed
Name what was actually opened: the sampled dossier files (exact paths, not "a sample of dossiers"), [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s live capacity table, `Excluded — Losing The Debate.md`, and `logs/runs.jsonl`/`System - Build Log` where a code-level claim needs checking.
### Sample & Method
State the sample size and how it was chosen (e.g., N most-recently-written per bucket, or N random per bucket) — 392 live dossiers (as of 2026-08-23: 146 AI & ML, 43 Fullstack, 63 CyS & Finance, 139 Other) cannot all be read every week, and a review that doesn't say how it sampled can't be checked for selection bias.
### Gate Conformance
Check the sample against [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s four hard gates (timing, US location, OPT, CS/software relevance). A dossier that shouldn't have cleared a gate is a Finding, cited by exact file and which gate it should have failed.
### Standard Conformance
Check the sample against [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]: required frontmatter fields present, `notes:` interlink present and resolving, `company/<slug>` tag present on same-company dossiers, body free of duplicated paragraphs and jammed ATS-chrome run-ons, and — for anything in `Viewed/` — `removed_date`/`removed_reason`/`status: removed` actually set.
> [!WARNING]
> Reporting Standard Conformance from the sample alone. If a compliance question can be answered exactly across the whole corpus with one grep (e.g. "how many dossiers have a `notes:` field"), run it and report the real fraction — sampling is for content-quality checks that need a human read, not for a countable fact a script already answers.
### Priority Classification Accuracy
Spot-check whether the sampled dossier's actual posting content matches the bucket it landed in — this is the exact bug class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] recorded repeatedly (a role matched on an incidental keyword — "threat" in a safety disclaimer, "machine learning" in a list of acceptable majors — not on genuine relevance).
### Resource-Limit Health
Cite the real current bucket counts against the 50-per-bucket notification threshold and the 150/170/190/200 global thresholds ([[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]). Confirm any GitHub issue that should have fired on a crossing actually did (`gh issue list`), not assumed from the threshold math alone.
### Findings
Named, specific, cited by exact file. "Nothing to report" is valid; a missing citation for a claim is not.
### Decided Fixes
Only items with 100% clarity, per the general [[30_Order/Standards/Review Standard|Review Standard]]'s rule. A review surfacing a bug is not itself authorization to patch the loop's code — that's a separate build session.
### Open Questions
Anything short of 100% clarity. Carries forward until resolved.
### Next Period's Watch List
What this review specifically expects to check again next week.
## Per-Heading Standard — Monthly Promotion Review
### Period Covered
The calendar month.
### Sources Reviewed
Name every folder actually opened: `Programs/{Serious,Considering,Job & Company}/`, `Contacts/Each One/{Ongoing,Come Back,Ended}/`, `Tracker/{Each One,Tracker.md,Internship - Dashboard.md}`, `20_Progress/Internship/Applying/{Now.md,Applied/}`, `Preperation/Interviews/`.
### Pipeline Checklist
Grade the month directly against [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s own `Done When` list — it is already a checklist, not prose to re-derive: every program actually pursued has a Program note, a Contacts note, and a Tracker note, all cross-linked; no Applying note has gone more than a week without a Log entry while active; the Dashboard and the Kanban agree on what's in motion; a Program sitting in `Ended/` with no matching Applying note is flagged for discard, per the Pipeline's own rule.
### Per-Program Trace
For every note trio that exists, walk noted → researched → created → applied → result and flag anything stalled beyond what its own `Next Action` field assumed — most concretely, a Tracker note whose stated reasoning cites a date that has since passed (e.g. "no rush, review starts in August" written in July, unrevisited once August arrives).
### Note-Shape Conformance — Provisional
See the dependency warning above. Grade only against what the current templates and Pipeline prose actually say; do not invent stricter rules. Name explicitly which checks are blocked on the pending 30_Order note-definition work rather than skipping them silently.
### Findings
Named, specific, cited by exact file.
### Decided Fixes
Only items with 100% clarity.
### Open Questions
Anything short of 100% clarity, including anything genuinely blocked on the pending note-definition session.
### Next Period's Watch List
What this review specifically expects to check again next month.
## Done Conditions
- Every claim in Gate Conformance, Standard Conformance, and Resource-Limit Health traces to a real file, count, or log row — a fraction stated as "X/392" only when actually counted, not estimated.
- The Weekly review states its sample size and selection method explicitly.
- The Monthly review's Note-Shape Conformance section names what it could not check because the note-definition work is still pending, rather than silently skipping it.
- Decided Fixes contains only items with 100% clarity; anything less stays in Open Questions.
- No `---` in the body; zero blank lines except after a callout; no duplicate frontmatter keys; every `notes:` wikilink resolves.
## Gold Standard Example
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|Internship Loop Weekly Review — 2026-W34]] — the first real review against this Standard, run the same session this Standard was written. Notable for what a full-corpus grep turned up that a sample alone would have missed: the `notes:` interlink field, specified as shipped in [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] since 2026-07-30, is actually present on 11 of 392 live dossiers.

```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship Loop Weekly Review Template.md`
```
---
type: evergreen
status: tree
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - evergreen
  - review
  - template
  - internship
---
# Internship Loop Weekly Review — <% tp.date.now("YYYY") %>-W<% tp.date.now("ww") %>
## Period Covered
<% tp.date.now("YYYY-MM-DD", -6) %> through <% tp.date.now("YYYY-MM-DD") %>
## Sources Reviewed
- [ ] Sampled dossier files (list exact paths in Sample & Method below)
- [ ] [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]] capacity table
- [ ] `Excluded — Losing The Debate.md`
- [ ] `logs/runs.jsonl` / [[20_Progress/Internship/Building System/System - Build Log|System - Build Log]] (only if a code-level claim needs checking)
## Sample & Method
- Sample size: ___
- Selection rule: ___
- Corpus size this period (full-corpus grep, not sampled): AI & ML ___ / Fullstack ___ / CyS & Finance ___ / Other ___ / Viewed ___
## Gate Conformance
_Against [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s four hard gates: timing, US location, OPT, CS/software relevance._
-
## Standard Conformance
_Against [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]: frontmatter fields, `notes:` interlink, `company/<slug>` tag, body dedup/structure, removal fields._
-
## Priority Classification Accuracy
-
## Resource-Limit Health
- Bucket counts vs. 50-per-bucket threshold: ___
- Global total vs. 150/170/190/200 thresholds: ___
- GitHub issues expected vs. actually filed: ___
## Findings
-
## Decided Fixes
_Only items with 100% clarity — see [[30_Order/Standards/Internship Loop Review Standard]]._
-
## Open Questions
-
## Next Period's Watch List
-

```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship Loop Monthly Review Template.md`
```
---
type: evergreen
status: tree
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - evergreen
  - review
  - template
  - internship
---
# Internship Loop Monthly Review — <% tp.date.now("YYYY-MM") %>
## Period Covered
<% tp.date.now("YYYY-MM-01") %> through <% tp.date.now("YYYY-MM-DD") %>
## Sources Reviewed
- [ ] `Programs/{Serious,Considering,Job & Company}/`
- [ ] `Contacts/Each One/{Ongoing,Come Back,Ended}/`
- [ ] `Tracker/{Each One,Tracker.md,Internship - Dashboard.md}`
- [ ] `20_Progress/Internship/Applying/{Now.md,Applied/}`
- [ ] `Preperation/Interviews/`
## Pipeline Checklist
_Direct against [[30_Order/Workflows/Internship Pipeline]]'s own `Done When` list._
- [ ] Every program actually pursued has a Program note, a Contacts note, and a Tracker note, all cross-linked
- [ ] No Applying note has gone more than a week without a Log entry while active
- [ ] The Dashboard and the Kanban agree on what's currently in motion
- [ ] No `Ended/` Program note sits without a matching Applying note (flag for discard if found)
## Per-Program Trace
| Program | Noted | Researched | Created | Applied | Result | Stalled? |
|---|---|---|---|---|---|---|
## Note-Shape Conformance — Provisional
_See [[30_Order/Standards/Internship Loop Review Standard]]'s dependency warning — grade only against current templates/Pipeline prose, name what's blocked on the pending 30_Order note-definition session._
-
## Findings
-
## Decided Fixes
_Only items with 100% clarity._
-
## Open Questions
_Include anything genuinely blocked on the pending note-definition session._
-
## Next Period's Watch List
-

```
- `Bash` -- `for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "=== $d ==="
  files=$(find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | sort | sed -n '1p;15p;30p')
  for f in $files; do
    echo "--- $f ---"
    grep -E "^(company|title|matched_reason|date_found|status):|^notes:|company/" "$f" | head -8
    echo "[NOTE] callout line:"
    grep -m1 "^\> \[!NOTE\]" "$f"
  done
done`
```
Exit code 2
=== 1 - AI & ML ===
--- 10_Areas/Career/Internships/List/Dossiers/1 ---
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
--- - ---
[NOTE] callout line:
--- AI ---
grep: AI: No such file or directory
[NOTE] callout line:
grep: AI: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- ML/2027 ---
grep: ML/2027: No such file or directory
[NOTE] callout line:
grep: ML/2027: No such file or directory
--- Business ---
grep: Business: No such file or directory
[NOTE] callout line:
grep: Business: No such file or directory
--- Technology ---
grep: Technology: No such file or directory
[NOTE] callout line:
grep: Technology: No such file or directory
--- Solutions ---
grep: Solutions: No such file or directory
[NOTE] callout line:
grep: Solutions: No such file or directory
--- Intern ---
grep: Intern: No such file or directory
[NOTE] callout line:
grep: Intern: No such file or directory
--- - ---
[NOTE] callout line:
--- Data ---
grep: Data: No such file or directory
[NOTE] callout line:
grep: Data: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- Software ---
grep: Software: No such file or directory
[NOTE] callout line:
grep: Software: No such file or directory
--- Engineering ---
grep: Engineering: No such file or directory
[NOTE] callout line:
grep: Engineering: No such file or directory
--- (Undergraduate) ---
grep: (Undergraduate): No such file or directory
[NOTE] callout line:
grep: (Undergraduate): No such file or directory
--- - ---
[NOTE] callout line:
--- AbbVie.md ---
grep: AbbVie.md: No such file or directory
[NOTE] callout line:
grep: AbbVie.md: No such file or directory
--- 10_Areas/Career/Internships/List/Dossiers/1 ---
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
--- - ---
[NOTE] callout line:
--- AI ---
grep: AI: No such file or directory
[NOTE] callout line:
grep: AI: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- ML/Applications ---
grep: ML/Applications: No such file or directory
[NOTE] callout line:
grep: ML/Applications: No such file or directory
--- Intern ---
grep: Intern: No such file or directory
[NOTE] callout line:
grep: Intern: No such file or directory
--- - ---
[NOTE] callout line:
--- AI ---
grep: AI: No such file or directory
[NOTE] callout line:
grep: AI: No such file or directory
--- and ---
grep: and: No such file or directory
[NOTE] callout line:
grep: and: No such file or directory
--- Machine ---
grep: Machine: No such file or directory
[NOTE] callout line:
grep: Machine: No such file or directory
--- Learning ---
grep: Learning: No such file or directory
[NOTE] callout line:
grep: Learning: No such file or directory
--- - ---
[NOTE] callout line:
--- TMEIC ---
grep: TMEIC: No such file or directory
[NOTE] callout line:
grep: TMEIC: No such file or directory
--- Corporation ---
grep: Corporation: No such file or directory
[NOTE] callout line:
grep: Corporation: No such file or directory
--- Americas.md ---
grep: Americas.md: No such file or directory
[NOTE] callout line:
grep: Americas.md: No such file or directory
--- 10_Areas/Career/Internships/List/Dossiers/1 ---
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/1: No such file or directory
--- - ---
[NOTE] callout line:
--- AI ---
grep: AI: No such file or directory
[NOTE] callout line:
grep: AI: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- ML/Campus ---
grep: ML/Campus: No such file or directory
[NOTE] callout line:
grep: ML/Campus: No such file or directory
--- Graduate ---
grep: Graduate: No such file or directory
[NOTE] callout line:
grep: Graduate: No such file or directory
--- Masters ---
grep: Masters: No such file or directory
[NOTE] callout line:
grep: Masters: No such file or directory
--- Summer ---
grep: Summer: No such file or directory
[NOTE] callout line:
grep: Summer: No such file or directory
--- Internship ---
grep: Internship: No such file or directory
[NOTE] callout line:
grep: Internship: No such file or directory
--- Program ---
grep: Program: No such file or directory
[NOTE] callout line:
grep: Program: No such file or directory
--- - ---
[NOTE] callout line:
--- 2027 ---
grep: 2027: No such file or directory
[NOTE] callout line:
grep: 2027: No such file or directory
--- AI ---
grep: AI: No such file or directory
[NOTE] callout line:
grep: AI: No such file or directory
--- Engineer, ---
grep: Engineer,: No such file or di

... [7881 characters truncated] ...

ternships/List/Dossiers/3: No such file or directory
--- - ---
[NOTE] callout line:
--- CyS ---
grep: CyS: No such file or directory
[NOTE] callout line:
grep: CyS: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- Finance/Quantitative ---
grep: Finance/Quantitative: No such file or directory
[NOTE] callout line:
grep: Finance/Quantitative: No such file or directory
--- Trading ---
grep: Trading: No such file or directory
[NOTE] callout line:
grep: Trading: No such file or directory
--- Intern ---
grep: Intern: No such file or directory
[NOTE] callout line:
grep: Intern: No such file or directory
--- - ---
[NOTE] callout line:
--- Virtu.md ---
grep: Virtu.md: No such file or directory
[NOTE] callout line:
grep: Virtu.md: No such file or directory
=== Other ===
--- 10_Areas/Career/Internships/List/Dossiers/Other/2026-2027 ---
grep: 10_Areas/Career/Internships/List/Dossiers/Other/2026-2027: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/Other/2026-2027: No such file or directory
--- Information ---
grep: Information: No such file or directory
[NOTE] callout line:
grep: Information: No such file or directory
--- Technology ---
grep: Technology: No such file or directory
[NOTE] callout line:
grep: Technology: No such file or directory
--- - ---
[NOTE] callout line:
--- Software ---
grep: Software: No such file or directory
[NOTE] callout line:
grep: Software: No such file or directory
--- Engineer ---
grep: Engineer: No such file or directory
[NOTE] callout line:
grep: Engineer: No such file or directory
--- - ---
[NOTE] callout line:
--- Intern ---
grep: Intern: No such file or directory
[NOTE] callout line:
grep: Intern: No such file or directory
--- - ---
[NOTE] callout line:
--- Chevron ---
grep: Chevron: No such file or directory
[NOTE] callout line:
grep: Chevron: No such file or directory
--- Corporation.md ---
grep: Corporation.md: No such file or directory
[NOTE] callout line:
grep: Corporation.md: No such file or directory
--- 10_Areas/Career/Internships/List/Dossiers/Other/College ---
grep: 10_Areas/Career/Internships/List/Dossiers/Other/College: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/Other/College: No such file or directory
--- to ---
grep: to: No such file or directory
[NOTE] callout line:
grep: to: No such file or directory
--- Corporate ---
grep: Corporate: No such file or directory
[NOTE] callout line:
grep: Corporate: No such file or directory
--- IT ---
grep: IT: No such file or directory
[NOTE] callout line:
grep: IT: No such file or directory
--- Internship ---
grep: Internship: No such file or directory
[NOTE] callout line:
grep: Internship: No such file or directory
--- - ---
[NOTE] callout line:
--- Data ---
grep: Data: No such file or directory
[NOTE] callout line:
grep: Data: No such file or directory
--- Analyst ---
grep: Analyst: No such file or directory
[NOTE] callout line:
grep: Analyst: No such file or directory
--- (NC) ---
grep: (NC): No such file or directory
[NOTE] callout line:
grep: (NC): No such file or directory
--- - ---
[NOTE] callout line:
--- Vanguard.md ---
grep: Vanguard.md: No such file or directory
[NOTE] callout line:
grep: Vanguard.md: No such file or directory
--- 10_Areas/Career/Internships/List/Dossiers/Other/Data ---
grep: 10_Areas/Career/Internships/List/Dossiers/Other/Data: No such file or directory
[NOTE] callout line:
grep: 10_Areas/Career/Internships/List/Dossiers/Other/Data: No such file or directory
--- Analytics ---
grep: Analytics: No such file or directory
[NOTE] callout line:
grep: Analytics: No such file or directory
--- Intern ---
grep: Intern: No such file or directory
[NOTE] callout line:
grep: Intern: No such file or directory
--- - ---
[NOTE] callout line:
--- Global ---
grep: Global: No such file or directory
[NOTE] callout line:
grep: Global: No such file or directory
--- Servicing ---
grep: Servicing: No such file or directory
[NOTE] callout line:
grep: Servicing: No such file or directory
--- - ---
[NOTE] callout line:
--- Financial ---
grep: Financial: No such file or directory
[NOTE] callout line:
grep: Financial: No such file or directory
--- Crimes ---
grep: Crimes: No such file or directory
[NOTE] callout line:
grep: Crimes: No such file or directory
--- Risk ---
grep: Risk: No such file or directory
[NOTE] callout line:
grep: Risk: No such file or directory
--- & ---
grep: &: No such file or directory
[NOTE] callout line:
grep: &: No such file or directory
--- Controls ---
grep: Controls: No such file or directory
[NOTE] callout line:
grep: Controls: No such file or directory
--- - ---
[NOTE] callout line:
--- American ---
grep: American: No such file or directory
[NOTE] callout line:
grep: American: No such file or directory
--- Express.md ---
grep: Express.md: No such file or directory
[NOTE] callout line:
grep: Express.md: No such file or directory
```
- `Bash` -- `for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "=== $d ==="
  find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | sort | sed -n '1p;15p;30p' > /tmp/filelist.txt
  while IFS= read -r f; do
    echo "--- $f ---"
    grep -E "^(company|title|matched_reason|date_found|status):" "$f"
    grep -c "^notes:" "$f"
    grep -m1 "company/" "$f"
    grep -m1 "^\> \[!NOTE\]" "$f"
  done < /tmp/filelist.txt
done`
```
Exit code 1
=== 1 - AI & ML ===
--- 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md ---
company: AbbVie
title: 2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate)
date_found: '2026-08-20'
matched_reason: matched
status: unreviewed
0
AbbVie's mission is to discover and deliver innovative medicines and solutions that solve serious health issues today and address the medical challenges of tomorrow. We strive to have a remarkable impact on people's lives across several key therapeutic areas including immunology, oncology and neuroscience - and products and services in our Allergan Aesthetics portfolio. For more information about AbbVie, please visit us at [www.abbvie.com](http://www.abbvie.com/). Follow @abbvie on [LinkedIn,](https://www.linkedin.com/company/abbvie/) [Facebook](https://www.facebook.com/AbbVieGlobal/), [Instagram](https://www.instagram.com/abbvie/), [X](https://twitter.com/abbvie) and [YouTube.](https://www.youtube.com/user/AbbVie)
--- 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Applications Intern - AI and Machine Learning - TMEIC Corporation Americas.md ---
company: TMEIC Corporation Americas
title: Applications Intern - AI and Machine Learning
date_found: '2026-08-12'
matched_reason: Summer 2027, AI/ML/Data
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md ---
company: American Express
title: Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise
date_found: '2026-08-17'
matched_reason: matched
status: unreviewed
0
=== 2 - Fullstack ===
--- 10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/2027 North America Software Engineering Internship - The Trade Desk.md ---
company: The Trade Desk
title: 2027 North America Software Engineering Internship
date_found: '2026-07-25'
matched_reason: matched
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Self-Built Engineer Intern - CDN Platform - ByteDance.md ---
company: ByteDance
title: Self-Built Engineer Intern - CDN Platform
date_found: '2026-08-13'
matched_reason: Summer 2027, AI/ML/Data
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineer Intern, Fullstack Product (Web + Services) - Microsoft.md ---
company: Microsoft
title: Software Engineer Intern, Fullstack Product (Web + Services)
date_found: '2026-08-21'
matched_reason: matched
status: unreviewed
1
  - company/microsoft
=== 3 - CyS & Finance ===
--- 10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md ---
company: Virtu Financial
title: 2027 Internship - Frontend & User Experience
date_found: '2026-07-29'
matched_reason: matched
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md ---
company: Virtu Financial
title: Frontend & User Experience Intern
date_found: '2026-07-30'
matched_reason: matched
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md ---
company: Virtu
title: Quantitative Trading Intern
date_found: '2026-07-27'
matched_reason: matched
status: unreviewed
0
=== Other ===
--- 10_Areas/Career/Internships/List/Dossiers/Other/2026-2027 Information Technology - Software Engineer - Intern - Chevron Corporation.md ---
company: Chevron Corporation
title: 2026-2027 Information Technology - Software Engineer - Intern
date_found: '2026-07-25'
matched_reason: matched
status: unreviewed
0
--- 10_Areas/Career/Internships/List/Dossiers/Other/College to Corporate IT Internship - Data Analyst (NC) - Vanguard.md ---
company: Vanguard
title: College to Corporate IT Internship - Data Analyst (NC)
date_found: '2026-08-18'
matched_reason: matched
status: unreviewed
0
- [LinkedIn](https://www.linkedin.com/company/vanguard "LinkedIn")
--- 10_Areas/Career/Internships/List/Dossiers/Other/Data Analytics Intern - Global Servicing - Financial Crimes Risk & Controls - American Express.md ---
company: American Express
title: Data Analytics Intern - Global Servicing - Financial Crimes Risk & Controls
date_found: '2026-08-18'
matched_reason: Summer 2027, AI/ML/Data
status: unreviewed
0
At American Express, our culture is built on a 175-year history of innovation, [shared values](https://www.americanexpress.com/en-us/company/who-we-are/) and Leadership Behaviors, and an unwavering commitment to back our customers, communities, and colleagues. From delivering differentiated products to providing world-class customer service, we operate with a strong risk mindset, ensuring we continue to uphold our brand promise of trust, security, and service.
```
- `Bash` -- `echo "--- Quant Trading Intern - Virtu (frontmatter + first NOTE + first 40 body lines) ---"
sed -n '1,25p' "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md"
echo "..."
grep -n "^##" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md" | head -5
echo "--- Qualifications section ---"
sed -n '/## Qualifications/,/## /p' "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md" | head -30`
```
--- Quant Trading Intern - Virtu (frontmatter + first NOTE + first 40 body lines) ---
---
company: Virtu
title: Quantitative Trading Intern
url: https://job-boards.greenhouse.io/virtu/jobs/8624408002
source: vanshb03
terms:
  - Summer
locations:
  - Austin, TX
  - Chicago, IL
  - New York, NY
target_year: []
date_posted: '2026-07-27'
date_found: '2026-07-27'
matched_reason: matched
status: unreviewed
next:
tags:
  - internship
  - auto-discovered
---
# Quantitative Trading Intern
Found 2026-07-27 via vanshb03.
> [!NOTE] CyS & Finance: matched on "Quantitative Trading".
## Posting (fetched 2026-07-27)
...
25:## Posting (fetched 2026-07-27)
31:## **Quant Trading Internship**
40:### **Requirements**
--- Qualifications section ---
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\3 - CyS & Finance\Quantitative Trading Intern - Virtu.md`
- `Bash` -- `grep -H "^source:" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md"
grep -H "^url:" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md"`
```
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md:source: Greenhouse
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md:source: vanshb03
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md:url: https://job-boards.greenhouse.io/virtu/jobs/8657500002
10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md:url: https://job-boards.greenhouse.io/virtu/jobs/8657500002
```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Internship Loop Reviews MOC.md`
```
---
type: index
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - internship
  - moc
  - review
notes:
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
next: "Run the next Weekly Discovery Review around 2026-08-30; run the next Monthly Promotion Review in September once at least one more program has moved past Commit."
---
# Internship Loop Reviews — Map of Content
## Purpose
This folder holds the review layer for `gupta-builds/internship-research-loop` and everything downstream of it in [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]] — the thing that checks whether the loop's actual output matches what [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] and [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] say it should, instead of trusting the commit log or the dossier count alone.
## Map
[[30_Order/Standards/Internship Loop Review Standard|Internship Loop Review Standard]] is the content contract for everything under `Scheduled/` here — read it first, it explains why the folder splits into two review types rather than one. `Scheduled/Weekly/` holds the **Discovery Review**: a weekly check on Step 1 (Find) — the hourly, unattended GitHub Actions loop that writes into `List/Dossiers/`. This is the review that actually catches the loop's real, historical bug class — misclassification on an incidental keyword, cross-source duplicates that share an exact URL, postings that never should have cleared the CS/software-relevance gate — the same class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] records recurring even after being "fixed." `Scheduled/Monthly/` holds the **Promotion Review**: a monthly check on Steps 2-9 (Screen through Close) — Program, Contacts, and Tracker note hygiene, graded directly against [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s own `Done When` checklist. It runs monthly, not weekly, because this half of the pipeline is still lightly exercised (one real promotion, Appian, as of the first review below) and a weekly cadence on it would mostly report nothing new.
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|Internship Loop Weekly Review — 2026-W34]] is the first real review of either kind, run the same session the Standard was written. It found the loop's `notes:` interlink field — specified as shipped 2026-07-30 — present on only 11 of 392 live dossiers, plus a real gate-conformance miss (a pure quant-trading role that should have been rejected outright) and an exact-URL cross-source duplicate. [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08|Internship Loop Monthly Review — 2026-08]] is the first Promotion Review, checked against the one real program that exists (Appian) — its note trio cross-links correctly, but its Tracker note's stated "no rush" reasoning cites a review-start date that has since arrived.
> [!WARNING]
> The Monthly review's note-shape checks are provisional — see the Standard's own dependency warning. A separate session is still defining concrete field-level specs for Program/Contact/Tracker/Applying/Job & Company notes under `30_Order/`. Don't read a provisional finding here as a settled rule until that lands.
## Status
| Review | Period | Status |
|---|---|---|
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34\|Weekly — 2026-W34]] | 2026-08-17 to 2026-08-23 | First run — findings open |
| [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08\|Monthly — 2026-08]] | 2026-08-01 to 2026-08-23 | First run — findings open |
## Dataview
```dataview
TABLE created, status
FROM "60_Claude/30_Reviews/Internship Loop/Scheduled"
SORT file.name DESC
```

```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Weekly\Internship Loop Weekly Review — 2026-W34.md`
```
---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - evergreen
  - review
  - internship
notes:
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
next: "Fix the notes:/company-tag write-time gap and the Virtu exact-URL duplicate at the code level (separate build session) — this review only names them."
---
# Internship Loop Weekly Review — 2026-W34
## Period Covered
2026-08-17 through 2026-08-23. First run of this review — no prior period to compare against.
## Sources Reviewed
- [x] 12 sampled dossier files, listed in Sample & Method
- [x] [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s live capacity table, cross-checked against a direct folder count
- [ ] `Excluded — Losing The Debate.md` — not opened this pass
- [ ] `logs/runs.jsonl` / GitHub issues — not reachable this session (no local clone of `gupta-builds/internship-research-loop`, no `gh` auth); claims below that would need it are flagged, not guessed
## Sample & Method
12 dossiers, 3 per priority bucket, picked at sorted positions 1/15/30 within each bucket folder (alphabetical by filename) — a fixed, repeatable rule, not hand-picked for interesting results. Frontmatter and the classification `[!NOTE]` callout read for all 12; full body read for 2 (AbbVie, Virtu Quantitative Trading) where the callout alone wasn't enough to judge gate/classification fit.
Corpus size this period, counted directly (`find`, not the MOC's cached render): **1 - AI & ML 146, 2 - Fullstack 43, 3 - CyS & Finance 63, Other 139, Viewed 6**. Bucket sum is 391; a separate recursive count of the whole `Dossiers/` tree (excluding `Viewed/`) returned 392 — a real one-file discrepancy, most likely a flat/unsorted note the [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s own "Not Yet Sorted" section exists to catch. Not tracked down further this pass — see Open Questions.
## Gate Conformance
**One real miss, high confidence:** `3 - CyS & Finance/Quantitative Trading Intern - Virtu.md` should not have cleared the CS/software-relevance gate at all. Its own body is explicit — "Our Quantitative Traders are responsible for the design, operation, and improvement of high-performance algorithmic trading strategies," "most of their time solving trading problems as they occur in the markets," programming listed only as "some experience... a plus." [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s own gate description names this exact category — "pure trading-strategy research" — as something that "is rejected outright and does not land anywhere — not even Other." This one landed in a priority bucket.
The other 11 sampled dossiers pass: TMEIC's "Applications Intern - AI and Machine Learning" and American Express's "AI Engineer" role are genuinely AI/ML by title and content; the Fullstack and Other samples (Trade Desk, ByteDance, Microsoft, Chevron, Vanguard, Amex Data Analytics) all show real software/data content matching their bucket.
## Standard Conformance
Checked exactly, by grep across the full 392-dossier corpus, not the 12-dossier sample — this is a countable fact, not a judgment call:
- **`notes:` interlink field: 11/392 (2.8%).** [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] §1 states this field shipped 2026-07-30 and is required on every dossier. Of the 11 that have it, 6 are Microsoft dossiers all dated `date_found: 2026-08-21` and 4 are `Viewed/` removals (which get the field appended at move time by `recheck.py`, per §4) — meaning the *write-time* path for every other source (SimplifyJobs, JGCL, vanshb03, zshah101, Greenhouse outside the one Microsoft batch, Ashby, AIJobs, freehire) is not adding it. The AbbVie dossier sampled below (`date_found: 2026-08-20`, one day before the Microsoft batch) confirms this: no `notes:` field at all.
- **`company/<slug>` tag: 69/392 (17.6%).** Same shape of gap — present on the one Microsoft dossier sampled, absent on the other 11.
- Body dedup/structure: none of the 12 sampled dossiers showed duplicated paragraphs or jammed ATS-chrome run-ons in this pass — the specific defects [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] §2 describes (Conagra's repeated "About Us," `locationsChicago...` run-ons) weren't reproduced in this sample. Not proof they're fixed corpus-wide, just not seen in these 12.
> [!WARNING]
> The `notes:`/tag gap is a real conformance failure, not a documentation lag — the Standard says "shipped," the corpus says otherwise for 97%+ of live dossiers. Whether this is a reverted commit, an unpushed fix, or a fix that only ever touched one source's writer path is a code-side question this review can't answer without repo access — see Open Questions.
## Priority Classification Accuracy
One likely miss, lower confidence than the Gate Conformance finding: `1 - AI & ML/2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md` (`matched_reason: matched`, no specific signal named) is a general Data-Engineering-or-Software-Engineering BTS internship; its only AI/ML-adjacent content is one preferred-qualifications bullet — "ability to apply generative AI to custom software solutions" — among a much longer list of unrelated skills (NodeJS, Vue, Java, SQL, TypeScript). This reads like the same bug class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] recorded for Databricks ("machine learning" in a list of acceptable majors) and Mosaic ("threat" in a safety disclaimer) — an incidental keyword hit, not genuine AI/ML core relevance. Flagged as a Finding, not a Decided Fix, since one example isn't enough to confirm the pattern is systemic versus a single edge case.
The other two `1 - AI & ML` samples (TMEIC, American Express) are correctly classified — the bucket isn't uniformly wrong, this looks like a specific keyword-weighting edge case.
## Resource-Limit Health
Current bucket counts (391 total excl. Viewed) are already past every threshold [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] defines: all four buckets sit above the 50-per-bucket notification line except Fullstack (43, approaching), and the 391 total is past both the 190 and 200 global issue thresholds. Source of Truth records issues #4-8 firing on 2026-08-21 for exactly this kind of crossing. **Not verified this pass:** whether the continued growth since then (391 now vs. 393 on 2026-08-21, per Source of Truth's own note — so actually roughly flat, `recheck.py` moving closed postings to `Viewed/` at close to the same rate new ones arrive) has triggered any further notification, since this session has no `gh` access to the loop's repo. Treat the "flat" reading as provisional — it's one data point compared against a number quoted in a note, not a trend independently confirmed here.
## Findings
1. **Real Gate Conformance miss** — Virtu's "Quantitative Trading Intern" dossier should not exist per Source of Truth's own stated rule for pure trading-strategy roles. (`3 - CyS & Finance/Quantitative Trading Intern - Virtu.md`)
2. **Real, exact-URL cross-source duplicate** — `3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md` (source: Greenhouse, found 2026-07-29) and `3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md` (source: vanshb03, found 2026-07-30) share the identical URL `job-boards.greenhouse.io/virtu/jobs/8657500002` — not a same-company-different-title judgment call like the Aquatic case, an exact string match cross-source dedup should catch deterministically.
3. **`notes:` interlink field compliance: 11/392 (2.8%)** against a Standard that says it shipped 2026-07-30 — the write-time gap spans every discovery source except one Microsoft/Greenhouse batch on 2026-08-21.
4. **`company/<slug>` tag compliance: 69/392 (17.6%)** — same shape of gap.
5. **Likely, lower-confidence classification miss** — AbbVie's BTS dossier in `1 - AI & ML` on an incidental "generative AI" mention, same bug class as prior Databricks/Mosaic misses.
## Decided Fixes
None this pass. Every finding above is a real, cited defect, but fixing any of them means editing `gupta-builds/internship-research-loop`'s code — outside what a vault-side review can do, and the general [[30_Order/Standards/Review Standard|Review Standard]]'s rule is that a review surfacing a problem isn't itself authorization to fix it.
## Open Questions
- Is the `notes:`/company-tag write-time gap a reverted fix, an unpushed fix, or a fix that only ever landed in one source's writer path? Needs a direct repo check (`git log` / `git blame` on `vault_writer/writer.py`), not answerable from the vault side alone.
- Should the two Virtu Frontend duplicates be manually merged/one discarded now, or left for the next `recheck.py` cross-source-dedup fix to catch structurally? Leaving it risks the same pair recurring on the next source pull if the underlying dedup key isn't fixed.
- Does the AbbVie-style incidental-keyword classification miss recur often enough to be systemic, or was this one edge case? One data point isn't enough to decide.
- Untracked one-file discrepancy between the per-bucket sum (391) and the recursive non-Viewed count (392) — likely a flat/unsorted note, not chased down this pass.
## Next Period's Watch List
- Re-run the same 3-per-bucket sample rule next week and check whether the `notes:`/tag gap narrowed (a real fix landing) or stayed flat (confirms it's not being worked).
- Check whether the Virtu duplicate pair is still both present, or whether one got caught by a `recheck.py` run in the interim.
- Pull `logs/runs.jsonl` or `gh issue list` directly next time repo access is available, to replace this pass's "not verified" Resource-Limit Health claim with a real number.

```
- `Bash` -- `echo "--- Programs/Serious ---"; find "10_Areas/Career/Internships/Programs/Serious" -maxdepth 1 -name "*.md"
echo "--- Programs/Considering ---"; find "10_Areas/Career/Internships/Programs/Considering" -maxdepth 1 -name "*.md"
echo "--- Contacts/Each One/Ongoing ---"; find "10_Areas/Career/Internships/Contacts/Each One/Ongoing" -maxdepth 1 -name "*.md" 2>&1
echo "--- Tracker/Each One/Current ---"; find "10_Areas/Career/Internships/Tracker/Each One/Current" -maxdepth 1 -name "*.md" 2>&1
echo "--- Applying/Applied ---"; find "20_Progress/Internship/Applying/Applied" -maxdepth 1 -name "*.md" 2>&1
echo "--- Tracker.md kanban head ---"; sed -n '1,20p' "10_Areas/Career/Internships/Tracker/Tracker.md" 2>&1
echo "--- Dashboard head ---"; sed -n '1,25p' "10_Areas/Career/Internships/Tracker/Internship - Dashboard.md" 2>&1`
```
--- Programs/Serious ---
10_Areas/Career/Internships/Programs/Serious/2026-HRT-Sophomore.md
10_Areas/Career/Internships/Programs/Serious/[REDACTED].md
10_Areas/Career/Internships/Programs/Serious/[REDACTED].md
10_Areas/Career/Internships/Programs/Serious/[REDACTED].md
10_Areas/Career/Internships/Programs/Serious/[REDACTED].md
--- Programs/Considering ---
10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md
--- Contacts/Each One/Ongoing ---
10_Areas/Career/Internships/Contacts/Each One/Ongoing/Software Engineering Intern - Appian.md
--- Tracker/Each One/Current ---
10_Areas/Career/Internships/Tracker/Each One/Current/Software Engineering Intern - Appian.md
--- Applying/Applied ---
--- Tracker.md kanban head ---
---

kanban-plugin: board

---

## Interesting



## To Apply



## Applying Today



## Applied

--- Dashboard head ---
---
created: 2026-07-09
updated: 2026-07-26
type: dashboard
status: active
tags:
  - internships
  - tracking
  - career
  - dashboard
notes:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Source of Truth]]"
---
# 📊 Internship Dashboard — The Whole Process
==Not per-internship — this is the health of the entire loop, one screen.== For one specific internship's detail, go to its Tracker/Each One note. For the kanban glance, see [[Tracker]]. For the raw pipeline status doc, see [[Internships Hub]].
## 🔎 Discovery — Dossier Pipeline Health
```dataview
TABLE WITHOUT ID
  file.folder as "Priority Folder", length(rows) as "Count", "/ 50" as Limit
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE company AND file.folder != "10_Areas/Career/Internships/List/Dossiers"
GROUP BY file.folder
```
```
- `Bash` -- `echo "--- Contacts/Each One (all) ---"; find "10_Areas/Career/Internships/Contacts/Each One" -name "*.md"
echo "--- Tracker/Each One (all) ---"; find "10_Areas/Career/Internships/Tracker/Each One" -name "*.md"
echo "--- Programs/Serious/Ended ---"; find "10_Areas/Career/Internships/Programs/Serious" -type d
echo "--- HRT-Sophomore frontmatter ---"; sed -n '1,15p' "10_Areas/Career/Internships/Programs/Serious/2026-HRT-Sophomore.md"`
```
--- Contacts/Each One (all) ---
10_Areas/Career/Internships/Contacts/Each One/Contacts-to-Create.md
10_Areas/Career/Internships/Contacts/Each One/Ongoing/Software Engineering Intern - Appian.md
--- Tracker/Each One (all) ---
10_Areas/Career/Internships/Tracker/Each One/Current/Software Engineering Intern - Appian.md
10_Areas/Career/Internships/Tracker/Each One/Trackings-to-Create.md
--- Programs/Serious/Ended ---
10_Areas/Career/Internships/Programs/Serious
10_Areas/Career/Internships/Programs/Serious/Ended
--- HRT-Sophomore frontmatter ---
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
```
- `Bash` -- `for f in Deepgram Nuro Uber WesternDigital; do
  echo "--- $f ---"
  file=$(find "10_Areas/Career/Internships/Programs/Serious" -iname "*$f*")
  grep -E "^(created|updated|next):" "$file" 2>&1 | head -5
done`
```
--- Deepgram ---
--- Nuro ---
--- Uber ---
--- WesternDigital ---
```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Monthly\Internship Loop Monthly Review — 2026-08.md`
```
---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - evergreen
  - review
  - internship
notes:
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian]]"
next: "Decide HRT-Sophomore's fate (discard vs. keep as reference) and create the missing Deepgram/Nuro/Uber/WesternDigital Contacts+Tracker notes, or explicitly decide they don't need one yet — don't leave the gap silent."
---
# Internship Loop Monthly Review — 2026-08
## Period Covered
2026-08-01 through 2026-08-23. First run of this review — no prior period to compare against, so this pass also covers everything created before August that's still live in the pipeline.
## Sources Reviewed
- [x] `Programs/Serious/` and `Programs/Considering/` (full listing)
- [x] `Contacts/Each One/` (full listing, all subfolders)
- [x] `Tracker/Each One/` (full listing, all subfolders) and `Tracker/Tracker.md`
- [x] `20_Progress/Internship/Applying/Now.md` and `Applied/`
- [ ] `Preperation/Interviews/` — not opened; nothing in this pass reached that stage
## Pipeline Checklist
_Against [[30_Order/Workflows/Internship Pipeline]]'s own `Done When` list._
- [ ] **Every program actually pursued has a Program note, a Contacts note, and a Tracker note, all cross-linked — FAILS for 4 of 5 `Serious/` programs.** See Per-Program Trace.
- [x] No Applying note has gone more than a week without a Log entry while active — vacuously true, `20_Progress/Internship/Applying/` has no active Applying note yet (only `Applied/` exists, empty, and reference stubs `2026-HRT-Sophomore.md`/`AI Applying.md`/`Applications-to-Create.md`).
- [x] The Dashboard and the Kanban agree on what's currently in motion — both show nothing applied yet; `Tracker/Tracker.md`'s "Applied" lane is empty and `Applying/Now.md`'s dataview query has nothing to return, consistent with each other.
- [x] No `Ended/` Program note sits without a matching Applying note — `Programs/Serious/Ended/` and `Programs/Considering/Ended/` are both empty; nothing to check yet.
## Per-Program Trace
| Program | Noted | Researched | Created | Applied | Result | Stalled? |
|---|---|---|---|---|---|---|
| Appian (Considering) | 2026-07-25 | 2026-07-26 | 2026-07-26 | — | — | Trio complete and cross-linked (Program ↔ Contact ↔ Tracker all resolve). Tracker's `Next Action` says "no rush, applications aren't reviewed until August 2026" — written 2026-07-26, and it is now 2026-08-23. That reasoning is stale on its own terms, not re-checked since. |
| Deepgram (Serious) | — | — | 2026-07-29 (per [[30_Order/Workflows/Internship Pipeline]]'s Step 1 note) | — | — | **No Contacts note, no Tracker note exists anywhere in `Contacts/Each One/` or `Tracker/Each One/`.** Committed via the manual-web-clip rule alongside Uber/Nuro/Western Digital, but only the Program note was actually created. |
| Nuro (Serious) | — | — | 2026-07-29 | — | — | Same gap as Deepgram — Program note only. |
| Uber (Serious) | — | — | 2026-07-29 | — | — | Same gap as Deepgram — Program note only. |
| Western Digital (Serious) | — | — | 2026-07-29 | — | — | Same gap as Deepgram — Program note only. |
| HRT-Sophomore (Serious) | 2026-07-16 | 2026-07-16 | 2026-07-16 | — | — | **Explicitly withdrawn the same day it was created**, per [[20_Progress/Internship/Building System/System - Build Log|Build Log]]'s own 2026-07-16 entry ("Class-year correction... withdrew the HRT worked example"). Still sitting in `Programs/Serious/` more than five weeks later, not moved to `Ended/`, not discarded, no Contacts/Tracker note ever existed for it. |
## Note-Shape Conformance — Provisional
See [[30_Order/Standards/Internship Loop Review Standard]]'s dependency warning — the checks below are graded against current templates/Pipeline prose only.
- Appian's trio uses the field names the current `Program`/`Tracking`/`Contact` templates actually use (`list_origin`, `recruiter_contact`, `applying_note` on the Program; `program`/`contact`/`related_notes` on the Tracker) and every cross-link resolves to a real file — checked directly, not assumed.
- Deepgram/Nuro/Uber/Western Digital's Program notes have no `created`/`updated`/`next` frontmatter fields at all — consistent with the Program Template not using those field names, not itself a defect, but it does mean there's no dated signal inside the note for *when* it last got real attention, which makes a gap like the missing Contacts/Tracker notes harder to notice without a review like this one.
## Findings
1. **Four of five `Serious/` programs (Deepgram, Nuro, Uber, Western Digital) are missing their Contacts and Tracker notes**, violating [[30_Order/Workflows/Internship Pipeline]] Step 3's "created together" rule and the pipeline's own `Done When` checklist. All four were committed the same day (2026-07-29) via the same manual-web-clip backfill described in Pipeline Step 1 — this looks like a one-time batch where only the Program-note half of the three-note commit ritual actually happened.
2. **HRT-Sophomore is a stale orphan** — created and withdrawn the same day (2026-07-16) per the project's own Build Log, still physically present in `Programs/Serious/` five-plus weeks later with no Contacts/Tracker note and no move to `Ended/` or deletion.
3. **Appian's Tracker note carries a time-relative claim that has since expired** — "no rush... reviewed until August 2026," written 2026-07-26, unrevisited as of this review (2026-08-23, inside August).
## Decided Fixes
None this pass — every finding above needs a real decision (create the missing notes now vs. decide these four aren't actually being pursued; discard HRT-Sophomore vs. keep it as a dated reference; re-evaluate Appian's timing now that August has arrived), not a mechanical correction with 100% clarity. Per [[30_Order/Standards/Review Standard]]'s rule, a review naming a problem isn't authorization to resolve it here.
## Open Questions
- Are Deepgram/Nuro/Uber/Western Digital still being actively pursued, or did they quietly stall after the 2026-07-29 backfill? The answer decides whether the missing Contacts/Tracker notes are a real gap to close or a sign these should move toward discard.
- Should HRT-Sophomore be deleted outright (it was withdrawn same-day, never a real candidate) or kept in `Ended/` as a dated record of the class-year-eligibility mistake, the way [[30_Order/Standards/Internship Notes Standard]] argues dossiers should be moved-not-deleted on removal? The Pipeline note doesn't state a rule for this Program-note case specifically.
- Has Appian's application-review timing actually opened now that it's August — worth a direct check against the company's own portal, not assumed from a five-week-old note.
## Next Period's Watch List
- Whether the Deepgram/Nuro/Uber/Western Digital gap closed (real Contacts/Tracker notes created) or was resolved by explicit discard.
- Whether HRT-Sophomore is still sitting in `Serious/` unmoved a second review in a row — a second consecutive sighting is stronger evidence this is a discipline gap, not a one-time oversight.
- Whether Appian moved off "no rush" now that its stated review window has arrived.

```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers MOC.md`
```diff
- notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
  - "[[Source of Truth]]"
---
# Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote.
+ notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
  - "[[Source of Truth]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
---
# Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote. For whether what it wrote is actually correct, see [[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC|Internship Loop Reviews MOC]] — the weekly review sampling this folder for gate/classification/Standard conformance.
```
- `Bash` -- `for f in \
  "30_Order/Standards/Internship Loop Review Standard.md" \
  "30_Order/Templates/Career/Internship Loop Weekly Review Template.md" \
  "30_Order/Templates/Career/Internship Loop Monthly Review Template.md" \
  "60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC.md" \
  "60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34.md" \
  "60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08.md" \
  "10_Areas/Career/Internships/List/Dossiers MOC.md"; do
  echo "=== $f ==="
  echo "dash count: $(grep -c '^---$' "$f")"
  echo "blank lines: $(grep -c '^$' "$f")"
done`
```
=== 30_Order/Standards/Internship Loop Review Standard.md ===
dash count: 2
blank lines: 0
=== 30_Order/Templates/Career/Internship Loop Weekly Review Template.md ===
dash count: 2
blank lines: 0
=== 30_Order/Templates/Career/Internship Loop Monthly Review Template.md ===
dash count: 2
blank lines: 0
=== 60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC.md ===
dash count: 2
blank lines: 0
=== 60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34.md ===
dash count: 2
blank lines: 0
=== 60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08.md ===
dash count: 2
blank lines: 0
=== 10_Areas/Career/Internships/List/Dossiers MOC.md ===
dash count: 2
blank lines: 0
```

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Loop Review Standard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship Loop Monthly Review Template.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Career\Internship Loop Weekly Review Template.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Internship Loop Reviews MOC.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Monthly\Internship Loop Monthly Review — 2026-08.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\30_Reviews\Internship Loop\Scheduled\Weekly\Internship Loop Weekly Review — 2026-W34.md`

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers MOC.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `echo "--- 60_Claude/30_Reviews ---"; ls -la "60_Claude/30_Reviews" 2>&1; echo "--- 30_Order/Standards ---"; ls "30_Order/Standards" 2>&1; echo "--- 30_Order/Templates ---"; ls "30_Order/Templates" 2>&1; echo "--- 30_Order/Workflows ---"; ls "30_Order/Workflows" 2>&1; echo "--- Internship related dirs ---"; find "10_Areas/Career/Internships" -maxdepth 2 2>&1`
- `echo "--- Internship Loop folder contents ---"; find "60_Claude/30_Reviews/Internship Loop" -type f 2>&1; echo "--- Dossiers structure ---"; find "10_Areas/Career/Internships/List/Dossiers" -maxdepth 2 -type d 2>&1; echo "--- sample dossier count ---"; find "10_Areas/Career/Internships/List/Dossiers" -name "*.md" | wc -l`
- `echo "--- Source of Truth ---"; find . -iname "Source of Truth.md" -path "*Internship*" 2>&1
echo "--- System - Build Log ---"; find . -iname "System - Build Log.md" 2>&1
echo "--- Dossiers-to-Create ---"; find . -iname "Dossiers-to-Create.md" 2>&1
echo "--- sample dossier ---"; find "10_Areas/Career/Internships/List/Dossiers/1 - AI & ML" -name "*.md" | head -1`
- `echo "--- Ops Reports sample ---"; ls "60_Claude/30_Reviews/Ops Reports" | head -5
echo "--- AI reviews structure ---"; find "60_Claude/30_Reviews/AI" -maxdepth 3
echo "--- 00_Workflows Index for review mentions ---"; grep -n -i "review" "30_Order/Workflows/00_Workflows Index.md"`
- `echo "--- Templates/Capability ---"; ls "30_Order/Templates/Capability"
echo "--- Templates/Career ---"; ls "30_Order/Templates/Career"
echo "--- AI Tools Weekly Review Template ---"`
- `echo "--- dossier counts per bucket (excluding Viewed) ---"
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  c=$(find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | wc -l)
  echo "$d: $c"
done
echo "Viewed: $(find "10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" | wc -l)"
echo "--- total non-Viewed ---"
find "10_Areas/Career/Internships/List/Dossiers" -maxdepth 2 -name "*.md" -not -path "*/Viewed/*" | wc -l
echo "--- how many dossiers HAVE a notes: field ---"
grep -rl "^notes:" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | wc -l
echo "--- how many dossiers have a company/ tag ---"
grep -rl "company/" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | wc -l
echo "--- most recent 5 dossiers by mtime ---"
find "10_Areas/Career/Internships/List/Dossiers" -name "*.md" -not -path "*/Viewed/*" -printf "%T@ %p\n" 2>/dev/null | sort -rn | head -5`
- `echo "--- check for local repo clone ---"
find / -maxdepth 6 -iname "internship-research-loop" -type d 2>/dev/null
echo "--- dates on notes:-having dossiers ---"
grep -rl "^notes:" "10_Areas/Career/Internships/List/Dossiers" --include="*.md" | xargs -I{} grep -H "date_found:" {} | head -15`
- `echo "--- Appian Program note ---"; find "10_Areas/Career/Internships/Programs" -iname "*Appian*"
echo "--- Appian Contact note ---"; find "10_Areas/Career/Internships/Contacts" -iname "*Appian*"
echo "--- Appian Tracker note ---"; find "10_Areas/Career/Internships/Tracker" -iname "*Appian*"
echo "--- Applying folder ---"; find "20_Progress/Internship/Applying" -maxdepth 2
echo "--- date command check ---"; date -d 2026-08-23 +%G-W%V 2>&1 || python3 -c "import datetime; print(datetime.date(2026,8,23).isocalendar())"`
- `find "10_Areas/Career/Internships/List/Dossiers" -iname "*Appian*"`
- `find . -iname "Jarvis Writing and Formatting*" 2>&1`
- `for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "=== $d ==="
  files=$(find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | sort | sed -n '1p;15p;30p')
  for f in $files; do
    echo "--- $f ---"
    grep -E "^(company|title|matched_reason|date_found|status):|^notes:|company/" "$f" | head -8
    echo "[NOTE] callout line:"
    grep -m1 "^\> \[!NOTE\]" "$f"
  done
done`
- `for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "=== $d ==="
  find "10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -name "*.md" | sort | sed -n '1p;15p;30p' > /tmp/filelist.txt
  while IFS= read -r f; do
    echo "--- $f ---"
    grep -E "^(company|title|matched_reason|date_found|status):" "$f"
    grep -c "^notes:" "$f"
    grep -m1 "company/" "$f"
    grep -m1 "^\> \[!NOTE\]" "$f"
  done < /tmp/filelist.txt
done`
- `echo "--- Quant Trading Intern - Virtu (frontmatter + first NOTE + first 40 body lines) ---"
sed -n '1,25p' "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md"
echo "..."
grep -n "^##" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md" | head -5
echo "--- Qualifications section ---"
sed -n '/## Qualifications/,/## /p' "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quantitative Trading Intern - Virtu.md" | head -30`
- `grep -H "^source:" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md"
grep -H "^url:" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md" "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md"`
- `echo "--- Programs/Serious ---"; find "10_Areas/Career/Internships/Programs/Serious" -maxdepth 1 -name "*.md"
echo "--- Programs/Considering ---"; find "10_Areas/Career/Internships/Programs/Considering" -maxdepth 1 -name "*.md"
echo "--- Contacts/Each One/Ongoing ---"; find "10_Areas/Career/Internships/Contacts/Each One/Ongoing" -maxdepth 1 -name "*.md" 2>&1
echo "--- Tracker/Each One/Current ---"; find "10_Areas/Career/Internships/Tracker/Each One/Current" -maxdepth 1 -name "*.md" 2>&1
echo "--- Applying/Applied ---"; find "20_Progress/Internship/Applying/Applied" -maxdepth 1 -name "*.md" 2>&1
echo "--- Tracker.md kanban head ---"; sed -n '1,20p' "10_Areas/Career/Internships/Tracker/Tracker.md" 2>&1
echo "--- Dashboard head ---"; sed -n '1,25p' "10_Areas/Career/Internships/Tracker/Internship - Dashboard.md" 2>&1`
- `echo "--- Contacts/Each One (all) ---"; find "10_Areas/Career/Internships/Contacts/Each One" -name "*.md"
echo "--- Tracker/Each One (all) ---"; find "10_Areas/Career/Internships/Tracker/Each One" -name "*.md"
echo "--- Programs/Serious/Ended ---"; find "10_Areas/Career/Internships/Programs/Serious" -type d
echo "--- HRT-Sophomore frontmatter ---"; sed -n '1,15p' "10_Areas/Career/Internships/Programs/Serious/2026-HRT-Sophomore.md"`
- `for f in Deepgram Nuro Uber WesternDigital; do
  echo "--- $f ---"
  file=$(find "10_Areas/Career/Internships/Programs/Serious" -iname "*$f*")
  grep -E "^(created|updated|next):" "$file" 2>&1 | head -5
done`
- `for f in \
  "30_Order/Standards/Internship Loop Review Standard.md" \
  "30_Order/Templates/Career/Internship Loop Weekly Review Template.md" \
  "30_Order/Templates/Career/Internship Loop Monthly Review Template.md" \
  "60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC.md" \
  "60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34.md" \
  "60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-08.md" \
  "10_Areas/Career/Internships/List/Dossiers MOC.md"; do
  echo "=== $f ==="
  echo "dash count: $(grep -c '^---$' "$f")"
  echo "blank lines: $(grep -c '^$' "$f")"
done`


