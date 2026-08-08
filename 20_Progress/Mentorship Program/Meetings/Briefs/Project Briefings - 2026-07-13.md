---
type: input
status: sprout
input_kind: transcript
created: 2026-07-14
updated: 2026-08-08
source_note: "Mentor Meeting Transcript.md"
tags:
  - mentorship
  - brief
related_progress:
  - "[[Mentor Meeting Playbook]]"
  - "[[2026-07-14 Mentor Meeting — Actions]]"
  - "[[adx]]"
  - "[[Codebase Deep Read]]"
  - "[[Mentor Details]]"
next: The full action breakdown already exists at [[2026-07-14 Mentor Meeting — Actions]] — no /note-to-actions pass needed.
---
# 2026-07-14 Mentor Meeting — Brief
**Source:** Ahnaf mentorship call, captured via Cluely
**Transcript:** [[Mentor Meeting Transcript]]
**Date of conversation:** 2026-07-14 (meeting slipped one day from the planned 2026-07-13 slot; this note's filename kept the original date)
## What This Was
A standing bi-weekly mentorship call between Anant and Ahnaf (Senior Engineering Manager, Best Buy). Speaker labels in the raw transcript are unreliable — confirmed by Anant — so this brief is built from substance, not attribution. Most of the call ended up being Ahnaf asking Anant to review his own open-source project, **adx**, rather than following the planned four-goals agenda.
## What Was Decided
- **Cadence locked at bi-weekly (alternate Mondays)**, to be revisited at the start of September when Ahnaf is back in Minneapolis.
- **adx contribution becomes the primary currency of the relationship** between now and September — ahead of the program's original four goals, which stay live but secondary until fall.
- **Startup fundamentals got a concrete first step**: form an LLC (~$500-600, e.g. via ZenBusiness), then open a US Bank business checking account — buildable now, no investors or GitHub org required first.
## Key Threads
### adx — the real center of gravity
Ahnaf asked Anant to review adx, his own Agent Development Kit, specifically because Anant isn't a direct report and can give harsher feedback than Ahnaf's own team. Anant proposed adding a memory layer to adx's evidence bundles — persisting each PR's evidence into a queryable graph rather than flat files under `.evidence/`, which becomes unmanageable past ~200 PRs. Ahnaf connected this to the "context graph" problem and named **OpenHands** as a comparable project using one orchestrator over shared memory instead of duplicated agents. Original ask: feedback by 2026-07-19. Full technical detail on adx itself: [[adx]], [[Source Claims]], [[Claims vs Implementation]]; the much deeper follow-on pass: [[Codebase Deep Read]]. Full action breakdown: [[2026-07-14 Mentor Meeting — Actions]].
### Startup fundamentals
Anant framed his own plan as a 2-year runway with this year devoted to finding a problem statement and building, internship "100%" happening next year. Ahnaf's concrete next step: LLC formation, then a business bank account — see What Was Decided above.
### Professional image
Ahnaf gave two concrete resources: **"Cracking the Coding Interview"** (his stated gold standard) and the **"System Design Interview"** book (Alex Xu). Separately advised 3-4 weeks in the Bay Area for in-person networking — hackathons and meetups outperform LinkedIn cold outreach from the Midwest — and named local Minnesota options (JavaScript Minnesota, Open Source North, Minibar/Minidemo, data & analytics conferences).
### Portfolio and TradingView/CausalOps
TradingView wasn't discussed this call. Portfolio/Orby was barely touched — only that the deploy is confirmed live and Anant wants the site to become a genuine ongoing writing store, not AI-generated content. CausalOps came up once, as a concrete example of the "agents not sharing memory" problem — this is what directly informed the adx memory-layer proposal above, not as its own discussion thread.
## Open Questions
- [ ] The raw transcript is heavily garbled by the Cluely capture (fragmented, word-by-word lines, several passages where the speaker's actual meaning doesn't survive the transcription) — several minutes of the call (roughly the 22:00–30:00 mark, covering a tangent about Ahnaf's own mentor) aren't confidently reconstructable and are omitted from this brief rather than guessed at.
- [ ] Whether the 2026-07-19 feedback deadline mattered to Ahnaf once it passed, given the review grew into a multi-session pass instead — worth asking directly rather than assuming it's forgotten.
- [ ] Whether Ahnaf's "80k" references throughout the transcript (a transcription artifact) are worth a clean pass to confirm every occurrence really means "adx" — spot-checked, not exhaustively verified.
## Follow-Up Actions
- [ ] Raise the adx memory-layer proposal as a real GitHub issue, once [[Codebase Deep Read]]'s review is judged ready — see its own Next Action.
- [ ] Full detail on every thread above, plus items not central enough for this brief (internship outreach system design, portfolio blog prioritization, resource list): [[2026-07-14 Mentor Meeting — Actions]].
## Related Notes
- [[Mentor Meeting Playbook]] — the standing format this call followed, and its Session Log's 2026-07-14 entry
- [[2026-07-14 Mentor Meeting — Actions]] — the full link-dense action breakdown
- [[adx]], [[Codebase Deep Read]] — where the adx thread actually went
- [[Mentor Details]] — the mentor whose program this is
- [[Plan]] — the standing goals document this call's cadence decision updates
