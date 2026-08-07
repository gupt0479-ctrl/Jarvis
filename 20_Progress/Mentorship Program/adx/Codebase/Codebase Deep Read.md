---
type: project
status: active
created: 2026-08-07
updated: 2026-08-07
deadline:
related_progress:
  - "[[adx]]"
  - "[[Source Claims]]"
  - "[[Claims vs Implementation]]"
  - "[[Recommended Fixes]]"
  - "[[Mentor Details]]"
tags:
  - "#progress"
next: Research the Factory AI comparison for real, then decide what gets opened as GitHub issues.
---
# adx — Codebase Deep Read (MOC)
==Everything the four existing adx notes established from reading code in July, checked again by running the code — plus new ground those notes never covered: adx-intellij, the live MCP server, and the process that let the worst bug found here ship and survive a month unnoticed.==
## Goal
Get past "the code matches the docs, or it doesn't" into "here's what actually happens when this runs, proven by running it" — before any of it becomes a GitHub issue or a document for Ahnaf. This folder is the second code-level pass, two weeks after [[Claims vs Implementation]] and one month after the repository itself last changed.
## What This Pass Covered That the Original Didn't
The July review read every non-test `.ts` file across all 8 packages. This pass:
- Read the test files themselves, the CLI command wrappers, the harness's supporting modules, `adx-vscode`'s webview content, and `adx-intellij` — a Kotlin IntelliJ plugin that existed in the repository the whole time but was never mentioned in the original four notes or, as it turns out, anywhere in adx's own README or docs site.
- Built the CLI from source and ran it directly against a disposable throwaway repo (`~/projects/ai/claude/adx-worktree-throwaway-test/`, kept on disk, not deleted) — `init`, `run --exec`, `gate --ci`, `maintain`, `sweep`, across multiple flag and config combinations.
- Started the MCP server for real and called all 6 tools through an actual client, not just read the handler code.
- Read every substantive commit's diff, not just the current file state — this is how the `adx init` crash got traced to its exact origin, and how the BER-score-jump commit's real mechanism got found.
- Confirmed, via `gh api` and `git fetch origin`, that nothing has changed in the real repository since 2026-07-07 — a month of dormancy, not ongoing development.
## Corrections to the Existing Notes
- **[[Claims vs Implementation]]**'s "Repository Reality Check" section states *"`git log --oneline` returns exactly one commit"*. This was a shallow-clone (`--depth 1`) artifact — the real history is 17 commits across a single 3-hour window on 2026-07-06/07. Confirmed directly: nothing was rewritten or force-pushed; the original clone simply never fetched full history. Nothing else in that note changes — the code state it reviewed and the code state reviewed here are identical. Flagged here for a deliberate edit to that note later, not changed in place — see [[Process and CI Gaps]] for the full detail.
## The Four New Notes
- [[Safety-Critical Gaps]] — the harness's isolation, verification, and governance mechanisms, tested against the exact conditions (unattended runs, interrupted processes, CI with no human watching) they're built for. Packages: `adx-core`, `adx-gate`, `adx-maintain`.
- [[Process and CI Gaps]] — why the worst bug found this pass shipped and survived: TypeScript catches it instantly, and nothing in this project's pipeline ever asks TypeScript. Also: a stale self-reported score, and a live-reproduced metric divergence. Packages: `adx-cli`, `adx-core`, `adx-gate`, the root tooling.
- [[Dead-on-Arrival Code]] — commands, config fields, and a whole package (`adx-intellij`) that exist but don't do what they claim, organized by failure shape. Packages: `adx-cli`, `adx-core`, `adx-mcp`, `adx-intellij`, `adx-shape`, `adx-sweep`, `adx-vscode`.
- [[Competitive Positioning]] — deliberately thin. Records a scoping decision (Factory AI, one dedicated GitHub issue) without fabricating research this pass didn't do.
## The Single Best Insight From This Pass
adx's actual claim to novelty — per [[adx]]'s own Competitive Read — is the three-pillar bundle, and the idea doing the real conceptual work inside it is the Agency Ladder: forcing genuine human accountability instead of rubber-stamping. [[Safety-Critical Gaps]] shows that mechanism is exactly the one currently faked — CI auto-approves Level 6 with a hardcoded `signedBy: 'engineer'`, unaffected by any config. The tool's one real differentiator is the thing that isn't real yet. See [[Competitive Positioning]] for why Factory AI is the sharper comparison to make that point with — that comparison still needs to be researched before it's ready for Ahnaf.
## Methodology
Every finding in these four notes is one of three things, and each note says which: read directly in source, reproduced by running the built CLI or MCP server against a throwaway repo, or traced through `git show`/`git log` on the actual commit that introduced or broke it. Nothing here is a single observation standing alone — claims that started as one observation were deliberately re-tested across flag combinations, config variations, or repeated runs before being written down.
## Open Questions
- [ ] Which of these findings does Ahnaf already know about? The mentorship framing (per [[Mentor Details]] and the original meeting transcript) is that he wants the harsh read specifically because he can't get it from his own team — worth checking directly rather than assuming any of this is news.
- [ ] Does the `adx init` crash change the order of operations for raising anything with him — it may be worth a fast, narrow, separate flag ahead of the fuller issue set, given it blocks every single first-time user.
- [ ] See each individual note's Open Questions for narrower follow-ups.
## Next Action
Research the actual Factory AI comparison (see [[Competitive Positioning]]), then move to deciding what becomes a GitHub issue — per standing instruction, no issues get opened until that decision gets a separate go-ahead.
## Log
- **2026-08-07:** Read every file the July pass hadn't (tests, CLI wrappers, harness internals, `adx-vscode` webview, `adx-intellij`); built and ran the CLI against a throwaway repo; found and root-caused the `adx init` crash; found the `--exec` worktree bypass and proved it with a live file-write probe; found and reproduced mutation-testing crash-corruption; started the MCP server for real and called all 6 tools, surfacing a live BER divergence and a third JSON-schema shape; confirmed via `gh api` that the real repository has had zero commits since 2026-07-07; wrote this note plus [[Safety-Critical Gaps]], [[Process and CI Gaps]], [[Dead-on-Arrival Code]], and [[Competitive Positioning]].
