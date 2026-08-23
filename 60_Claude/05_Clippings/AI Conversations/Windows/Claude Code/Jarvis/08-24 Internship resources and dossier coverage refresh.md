---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Internship resources and dossier coverage refresh"
started_at: 2026-08-24T01:17:34
ended_at: 2026-08-24T01:30:02
exported_at: 2026-08-24T01:30:02
duration_minutes: 12.5
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: 5e545ffa-226e-41af-bc97-6be623140b07
status: raw
turn_count: 2
tools_used:
  Bash: 15
  Grep: 4
  Read: 11
tokens:
  input: 100
  output: 28357
  cache_creation: 211946
  cache_read: 3843192
  total: 4083595
cost_usd: 1.900192
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\Cyber Security Intern - Capital One (2).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\Cyber Security IT Intern - CNO Financial Group (2).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\Data Internship - Data & AI Program - JP Morgan Chase (2).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\Removed Dossiers MOC.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\Software Engineer Intern - Capital One (2).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Dossiers\\Viewed\\What was Viewed.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Career\\Internships\\List\\Resources.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Internship\\Building System\\Research Loop - Resources.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\Internship Notes Standard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Standards\\MOC Standard.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Internship resources and dossier coverage refresh

## You

**Prompt 14 (now v2) is running in parallel in a different session — don't describe any specific new source as shipped; if you reference the source-expansion effort at all, say "in progress as of 2026-08-24, see this file's Prompt 14 entry," not a finished state.**

### Task 1 — Refresh `10_Areas/Career/Internships/List/Resources.md`
Stale since 2026-07-26 despite its own instruction to update "whenever a source is checked for exhaustion" and its own callout that a number unrefreshed for two weeks should be treated as stale. Real current per-source numbers (fetched/matched over recent runs, and current live-dossier counts) are already available — pull from `logs/runs.jsonl` via the repo, or ask for them if this session lacks direct repo access: SimplifyJobs 138 live dossiers (1.5% match rate on 290K+ fetched), vanshb03 77 (26.6%), zshah101 68 (12.1%), Greenhouse 16 (53.6%, small pre-curated set), AIJobs 11 (25.6%), Freehire 2 (28.6% but tiny absolute volume — worth noting as a real open question, see Prompt 14's Task 2), Jose-Gael-Cruz-Lopez 0 despite 76 real matches over the last 20 runs (also an open question, Prompt 14's Task 1 — note it as under investigation, not resolved either way yet). Update the table with these real, dated figures.

### Task 2 — Refresh the Named-Program Coverage Check in `Research Loop - Resources.md`
Unchanged from before — still a month stale, real numbers have moved (Jane Street 11, Microsoft 6 as of the last real check). Re-check current real dossier coverage per named company and update.

### Task 3 — Build `Viewed/Removed Dossiers MOC.md` for real
Unchanged — still empty, still required by `Internship Notes Standard.md` §1/§4, still dozens of real dossiers pointing at it.

### Explicitly out of scope
No code changes to `internship-research-loop`. No describing Prompt 14's in-progress source work (including InternDock, Lever, or anything else still being investigated) as finished. No unilateral decisions on anything ambiguous.

### Report back
Task 1/2: what changed, with real numbers cited. Task 3: confirmation the MOC is real and populated.

## Claude

I'll start by locating the relevant files for all three tasks.

Good, frontmatter is consistent. Now let me check the other two files quickly, then move to Task 1 — gathering real dossier counts per source.

All 4 removed dossiers confirmed with consistent frontmatter (removed 2026-08-23, all `active: false upstream`). Now let me get real current dossier counts per source for Task 1.

Now let me check current dossier coverage for all 11 named programs (Task 2).

### Tool Calls

- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships" -iname "*Resources*" -o -iname "*Research Loop*" -o -iname "*Viewed*Removed*" 2>/dev/null`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/Data Analyst Intern - Continental Resources.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Resources.md
```
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*internship-research-loop*" -maxdepth 4 -type d 2>/dev/null`
```
(Bash completed with no output)
```
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*Research Loop*" 2>/dev/null
echo "---"
find "/d/Users/_Anant" -maxdepth 3 -iname "*internship-research-loop*" 2>/dev/null
echo "---searching whole vault for logs/runs.jsonl---"
find "/d/Users/_Anant" -iname "runs.jsonl" 2>/dev/null`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Internship Research Loop — Full Pipeline.excalidraw
/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Research Loop - Implementation Plan.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Research Loop - Improvement Plan.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Research Loop - Resources.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Research Loop - Phase 7 Coverage Expansion.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/07-25 Design internship tracking and research loop system.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-17 Complete research loop Phase 4 end-to-end.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-19 Independent audit of internship research loop.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/07-25 Set up Claude Code tooling for internship research loop.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-17 Complete research loop Phase 4 end-to-end.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-19 Independent audit of internship research loop.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/_archive-pre-fix-2/07-25 Set up Claude Code tooling for internship research loop.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/Internship/Internship Research Loop — PRD.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/Internship/_COMMUNITY_Internship Research Loop — PRD.md
---
---searching whole vault for logs/runs.jsonl---
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Resources.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Research Loop - Resources.md`
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List" -maxdepth 2 -type d`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/2 - Fullstack
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed
```
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*Internship Notes Standard*" -o -iname "*Viewed*Removed*"`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\Internship Notes Standard.md`
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 | sort`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security Intern - Capital One (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security IT Intern - CNO Financial Group (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Data Internship - Data & AI Program - JP Morgan Chase (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Software Engineer Intern - Capital One (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/What was Viewed.md
```
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*MOC*"`
```
(Bash completed with no output)
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\Removed Dossiers MOC.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\What was Viewed.md`
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List" -maxdepth 1 -iname "*MOC*"`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers MOC.md`
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "MOC Standard.md"`
```
/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/MOC Standard.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Standards\MOC Standard.md`
- `Bash` -- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" ! -name "Removed Dossiers MOC.md" ! -name "What was Viewed.md" | wc -l
echo "---"
find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" ! -name "Removed Dossiers MOC.md" ! -name "What was Viewed.md"`
```
4
---
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security Intern - Capital One (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Cyber Security IT Intern - CNO Financial Group (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Data Internship - Data & AI Program - JP Morgan Chase (2).md
/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Software Engineer Intern - Capital One (2).md
```
- `Grep` -- pattern `Removed Dossiers MOC` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\Cyber Security Intern - Capital One (2).md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\Software Engineer Intern - Capital One (2).md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\Cyber Security IT Intern - CNO Financial Group (2).md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers\Viewed\Data Internship - Data & AI Program - JP Morgan Chase (2).md`
- `Bash` -- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for dir in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" "."; do
  echo "=== $dir ==="
  if [ "$dir" = "." ]; then
    find . -maxdepth 1 -name "*.md" | wc -l
  else
    find "$dir" -maxdepth 1 -name "*.md" | wc -l
  fi
done`
```
=== 1 - AI & ML ===
138
=== 2 - Fullstack ===
40
=== 3 - CyS & Finance ===
49
=== Other ===
85
=== . ===
1
```
- `Grep` -- pattern `^source:` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Career\Internships\List\Dossiers`
- `Bash` -- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for f in *.md "1 - AI & ML"/*.md "2 - Fullstack"/*.md "3 - CyS & Finance"/*.md "Other"/*.md; do
  [ -f "$f" ] || continue
  src=$(grep -m1 "^source:" "$f" | sed 's/^source: *//')
  echo "$src"
done | sort | uniq -c | sort -rn`
```
    137 SimplifyJobs
     74 vanshb03
     68 zshah101
     16 Greenhouse
     11 AIJobs
      4 manual
      2 Freehire
      1
```
- `Bash` -- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
grep -rl "^source: Ashby" . --include="*.md" | wc -l
echo "---empty source file---"
for f in *.md "1 - AI & ML"/*.md "2 - Fullstack"/*.md "3 - CyS & Finance"/*.md "Other"/*.md; do
  [ -f "$f" ] || continue
  src=$(grep -m1 "^source:" "$f" | sed 's/^source: *//')
  if [ -z "$src" ]; then echo "$f"; fi
done`
```
0
---empty source file---
Dossiers-to-Create.md
```
- `Grep` -- pattern `Prompt 14` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship`
- `Grep` -- pattern `Prompt 14` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Internship\Building System\Runs\Claude Code Prompts.md`
- `Bash` -- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for company in "Jane Street" "Two Sigma" "D. E. Shaw" "D.E. Shaw" "Citadel" "Google" "Microsoft" "LinkedIn" "MLH" "NASA" "Capital One" "Bloomberg"; do
  count=$(grep -rl "^company: $company$" . --include="*.md" 2>/dev/null | grep -v "^./Viewed/" | wc -l)
  echo "$company: $count"
done`
```
Jane Street: 11
Two Sigma: 1
D. E. Shaw: 0
D.E. Shaw: 0
Citadel: 0
Google: 3
Microsoft: 6
LinkedIn: 0
MLH: 0
NASA: 0
Capital One: 0
Bloomberg: 0
```
- `Bash` -- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
grep -rh "^company:" . --include="*.md" | grep -i "shaw"
echo "---Two Sigma files---"
grep -rl "^company: Two Sigma$" . --include="*.md"
echo "---Capital One (all incl viewed)---"
grep -rl "^company: Capital One$" . --include="*.md"`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships" -iname "*Resources*" -o -iname "*Research Loop*" -o -iname "*Viewed*Removed*" 2>/dev/null`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*internship-research-loop*" -maxdepth 4 -type d 2>/dev/null`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*Research Loop*" 2>/dev/null
echo "---"
find "/d/Users/_Anant" -maxdepth 3 -iname "*internship-research-loop*" 2>/dev/null
echo "---searching whole vault for logs/runs.jsonl---"
find "/d/Users/_Anant" -iname "runs.jsonl" 2>/dev/null`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List" -maxdepth 2 -type d`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "*Internship Notes Standard*" -o -iname "*Viewed*Removed*"`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 | sort`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*MOC*"`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List" -maxdepth 1 -iname "*MOC*"`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis" -iname "MOC Standard.md"`
- `find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" ! -name "Removed Dossiers MOC.md" ! -name "What was Viewed.md" | wc -l
echo "---"
find "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -name "*.md" ! -name "Removed Dossiers MOC.md" ! -name "What was Viewed.md"`
- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for dir in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other" "."; do
  echo "=== $dir ==="
  if [ "$dir" = "." ]; then
    find . -maxdepth 1 -name "*.md" | wc -l
  else
    find "$dir" -maxdepth 1 -name "*.md" | wc -l
  fi
done`
- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for f in *.md "1 - AI & ML"/*.md "2 - Fullstack"/*.md "3 - CyS & Finance"/*.md "Other"/*.md; do
  [ -f "$f" ] || continue
  src=$(grep -m1 "^source:" "$f" | sed 's/^source: *//')
  echo "$src"
done | sort | uniq -c | sort -rn`
- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
grep -rl "^source: Ashby" . --include="*.md" | wc -l
echo "---empty source file---"
for f in *.md "1 - AI & ML"/*.md "2 - Fullstack"/*.md "3 - CyS & Finance"/*.md "Other"/*.md; do
  [ -f "$f" ] || continue
  src=$(grep -m1 "^source:" "$f" | sed 's/^source: *//')
  if [ -z "$src" ]; then echo "$f"; fi
done`
- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
for company in "Jane Street" "Two Sigma" "D. E. Shaw" "D.E. Shaw" "Citadel" "Google" "Microsoft" "LinkedIn" "MLH" "NASA" "Capital One" "Bloomberg"; do
  count=$(grep -rl "^company: $company$" . --include="*.md" 2>/dev/null | grep -v "^./Viewed/" | wc -l)
  echo "$company: $count"
done`
- `cd "/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers"
grep -rh "^company:" . --include="*.md" | grep -i "shaw"
echo "---Two Sigma files---"
grep -rl "^company: Two Sigma$" . --include="*.md"
echo "---Capital One (all incl viewed)---"
grep -rl "^company: Capital One$" . --include="*.md"`


