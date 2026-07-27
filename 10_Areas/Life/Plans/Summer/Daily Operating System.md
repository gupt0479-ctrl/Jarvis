---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-07-27
tags:
  - plan
  - summer
  - daily
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[LeetCode & CSCI 4041]]"
  - "[[ML Fundamentals (2033 + 2230)]]"
  - "[[Anti-Drift Rules]]"
  - "[[Final Month Plan (Jul 28 - Sep 1)]]"
next: "[[Weekly Operating System]]"
---

# Daily Operating System

The one checklist `/startday` pastes on top of the day. Every item has a **done definition** and a vault link. If you can only read one note before starting a day, read this one.

Physical/health tracking lives in The Plan now — gym, habits, and body-related logging happen there, not in this checklist.

> [!WARNING]
> This checklist's academic-stack rows had never once been checked all summer as of 2026-07-27 — see [[Final Month Plan (Jul 28 - Sep 1)]]'s Implementation Status table. The rows below are unchanged in mechanism; the four new ones (System Design, Trading Knowledge, AI Knowledge, Certification) come from that plan. Running `/startday` and `/closeday` daily is what closes the gap — not adding more rows.

## The 4 wins (non-negotiable, with MVP for low-energy days)

| # | Win | Full version | MVP (still counts) | Done when |
|---|-----|--------------|--------------------|-----------|
| 1 | **Project** | 1 commit / 1 issue on flagship (Bangalore phase) | Course/hackathon admin step OR skip in Dubai phase | Evidence: commit hash, screenshot, or note path |
| 2 | **Career** | LeetCode ≥5 problems | LeetCode 5 (still required) | Count + topics in Today note → see [[LeetCode & CSCI 4041]] |
| 3 | **Cleanup / admin** | One course assignment OR inbox zero | Smallest admin step (HIST dropbox, 1 WebAssign problem) | Artifact posted/filed |
| 4 | **Review** | Full `/closeday` | 5-min end-of-day note | Today note's review block filled |

> Career win = LeetCode by default. Internship-pipeline work is a **weekly** cadence (see [[Weekly Operating System]]), not a daily minimum.

## Summer academic stack (always visible in the daily checklist)

| Track | Daily minimum | Done when | Plan |
|-------|---------------|-----------|------|
| LeetCode | **≥5 problems** | Count + topics logged; ≥1 tied to a 4041 concept | [[LeetCode & CSCI 4041]] |
| CSCI 4041 review | 25–45 min | One concept section reviewed OR 1 pattern linked to today's LC | [[LeetCode & CSCI 4041]] |
| CSCI 2033 (ML fundamentals) | 30–45 min | One subtopic + vault output (rule, derivation, or 3 practice problems) | [[ML Fundamentals (2033 + 2230)]] |
| MATH 2230 | Complete | Bridge notes still owed — see [[ML Fundamentals (2033 + 2230)]] §5 | [[ML Fundamentals (2033 + 2230)]] |
| HIST 1103 | Complete | No further action | — |
| System Design | 20–30 min | One [[Engineer Edge Roadmap]] step read + one applied question against a real project | [[Final Month Plan (Jul 28 - Sep 1)]] |
| Trading Knowledge | One note-line minimum | Personal mechanics or a [[Fable 5 — Read Order (TradingView folder)]] note read | [[Final Month Plan (Jul 28 - Sep 1)]] |
| AI Knowledge | One item | NVIDIA course, zoomcamp lesson, or a relevant paper/blog | [[Final Month Plan (Jul 28 - Sep 1)]] |
| Certification | Per week's cert in the table | Progress logged against the current cert's hour estimate | [[Final Month Plan (Jul 28 - Sep 1)]] |

## Daily checklist (copy block for Today note)

```markdown
## Summer Ops Checklist — [DATE]

### 4 Wins
- [ ] Project win (commit/issue OR Dubai-phase: course admin)
- [ ] Career win = LeetCode ≥5 ✔ count: __ / topics: __
- [ ] Cleanup/admin win (course assignment / inbox / HIST dropbox)
- [ ] Review win (closeday or 5-min end note)

### Academic Stack (daily minimums)
- [ ] LeetCode ≥5 — topics: __ (≥1 linked to CSCI 4041)
- [ ] CSCI 4041 review 25–45 min — concept: __
- [ ] CSCI 2033 broad-pass unit(s) — see [[ML Fundamentals (2033 + 2230)]]
- [ ] System design — 20–30 min, applied to: __
- [ ] Trading knowledge — one note-line: __
- [ ] AI knowledge — one item: __
- [ ] Certification — this week's cert progress: __

### Done definition met? (for /closeday scorecard)
- [ ] ≥90% of the above checked
```

## Default day shape (Dubai week — adapt to calendar)

Today's calendar drives the *when*; this is the fallback when it's empty. Capacity target: **3–5 h focused**.

| Block | Time (Dubai) | Use |
|-------|--------------|-----|
| Morning launch | 30 min | Open Today note; no phone/doomscroll before first task ([[Anti-Drift Rules]]) |
| Deep work 1 | 60–90 min | Hardest academic track of the day (usually MATH 2230 or 2033) |
| LeetCode | 45–60 min | 5 problems, one topic ([[LeetCode & CSCI 4041]]) |
| Deep work 2 | 45–60 min | CSCI 4041 review OR project (Bangalore phase) |
| Admin | 20–30 min | Course dropbox / WebAssign / inbox |
| Evening close | 15 min | `/closeday` → review win |

## Done definition for the *day*

A day is **green** when ≥90% of the academic-stack rows + all 4 wins (full or MVP) are checked. `/closeday` computes this; if red, it writes **one** friction fix for tomorrow (see [[Anti-Drift Rules]]).
