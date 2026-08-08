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
next: Decide what becomes a GitHub issue. No issues open until that gets a separate go-ahead.
---
# adx — Codebase Deep Read (MOC)
==Nobody can currently install this tool by following its own docs — `npm install -g adx` silently installs an unrelated, dead package from 2019 — and everything else in this folder describes what happens once you get past that, using a build from source instead.==
## Goal
Get past "the code matches the docs, or it doesn't" into "here's what actually happens when this runs, proven by running it" — before any of it becomes a GitHub issue or a document for Ahnaf. This folder is the second code-level pass, two weeks after [[Claims vs Implementation]] and one month after the repository itself last changed.
## What This Pass Covered That the Original Didn't
The July review read every non-test `.ts` file across all 8 packages. This pass:
- Read the test files themselves, the CLI command wrappers, the harness's supporting modules, `adx-vscode`'s webview content, and `adx-intellij` — a Kotlin IntelliJ plugin that existed in the repository the whole time but was never mentioned in the original four notes or, as it turns out, anywhere in adx's own README or docs site.
- Built the CLI from source and ran it directly against a disposable throwaway repo (`~/projects/ai/claude/adx-worktree-throwaway-test/`, kept on disk, not deleted) — `init`, `run --exec`, `gate --ci`, `maintain`, `sweep`, across multiple flag and config combinations.
- Started the MCP server for real and called all 6 tools through an actual client, not just read the handler code.
- Read every substantive commit's diff, not just the current file state — this is how the `adx init` crash got traced to its exact origin, and how the BER-score-jump commit's real mechanism got found.
- Checked the layer before all of that: whether a new user can actually get the tool onto their machine, and whether the license/citation surface would survive real due diligence.
- Confirmed, via `gh api` and `git fetch origin`, that nothing has changed in the real repository since 2026-07-07 — a month of dormancy, not ongoing development.
## Corrections to the Existing Notes
- **[[Claims vs Implementation]]**'s "Repository Reality Check" section states *"`git log --oneline` returns exactly one commit"*. This was a shallow-clone (`--depth 1`) artifact — the real history is 17 commits across a single 3-hour window on 2026-07-06/07. Confirmed directly: nothing was rewritten or force-pushed; the original clone simply never fetched full history. Nothing else in that note changes — the code state it reviewed and the code state reviewed here are identical. Flagged here for a deliberate edit to that note later, not changed in place — see [[Process and CI Gaps]] for the full detail.
## The Five New Notes
- [[Distribution and Adoption Gaps]] — **read this one first.** The npm package name `adx` is already taken by an unrelated, essentially-empty package from 2019; the getting-started docs' first command silently installs the wrong thing. No LICENSE file, no `license` field in any package.json. Adoption-funnel problems, not code bugs — nobody can reach the code the way the docs describe at all.
- [[Safety-Critical Gaps]] — the harness's isolation, verification, and governance mechanisms, tested against the exact conditions (unattended runs, interrupted processes, CI with no human watching) they're built for. Packages: `adx-core`, `adx-gate`, `adx-maintain`.
- [[Process and CI Gaps]] — why the worst code bug found this pass shipped and survived: TypeScript catches it instantly, and nothing in this project's pipeline ever asks TypeScript. Also: a stale self-reported score, and a live-reproduced metric divergence. Packages: `adx-cli`, `adx-core`, `adx-gate`, the root tooling.
- [[Dead-on-Arrival Code]] — commands, config fields, and a whole package (`adx-intellij`) that exist but don't do what they claim, organized by failure shape. Packages: `adx-cli`, `adx-core`, `adx-mcp`, `adx-intellij`, `adx-shape`, `adx-sweep`, `adx-vscode`.
- [[Competitive Positioning]] — real, sourced Factory AI research, done after an earlier version of this note correctly flagged itself as unresearched. The comparison is sharper than the version it replaces, and one part of the original framing didn't survive verification — corrected in place, not quietly dropped.
## The Single Best Insight From This Pass
adx's actual claim to novelty — per [[adx]]'s own Competitive Read — is the three-pillar bundle, and the idea doing the real conceptual work inside it is the Agency Ladder: forcing genuine human accountability instead of rubber-stamping. [[Safety-Critical Gaps]] shows that mechanism is exactly the one currently faked — CI auto-approves Level 6 with a hardcoded `signedBy: 'engineer'`, unaffected by any config. [[Competitive Positioning]] found the sharper version of this point: Factory AI doesn't do accountability better than adx — it doesn't attempt accountability at all, on any of its products. adx is trying to solve a harder, more valuable problem than its nearest competitor even attempts, and the part of adx that tries to solve it doesn't work yet.
## Methodology
Every finding in these five notes is one of four things, and each note says which: read directly in source, reproduced by running the built CLI or MCP server against a throwaway repo, traced through `git show`/`git log` on the actual commit that introduced or broke it, or independently verified against a live external source (npm registry, Factory AI's own docs) rather than taken on report. Nothing here is a single observation standing alone — claims that started as one observation were deliberately re-tested across flag combinations, config variations, repeated runs, or independent sources before being written down.
## Open Questions
- [ ] Which of these findings does Ahnaf already know about? The mentorship framing (per [[Mentor Details]] and the original meeting transcript) is that he wants the harsh read specifically because he can't get it from his own team — worth checking directly rather than assuming any of this is news.
- [ ] Does the npm name collision change the order of operations for raising anything with him — it's arguably more urgent than the `adx init` crash, since it blocks a first-time user one step earlier and with zero error signal.
- [ ] See each individual note's Open Questions for narrower follow-ups.
## Next Action
Decide what becomes a GitHub issue, and how the issue set is split (concrete bug-fix issues, the one Factory-positioning issue already scoped, and now potentially a distribution/naming issue). Per standing instruction, no issues get opened until that decision gets a separate go-ahead.
## Log
- **2026-08-07:** Read every file the July pass hadn't (tests, CLI wrappers, harness internals, `adx-vscode` webview, `adx-intellij`); built and ran the CLI against a throwaway repo; found and root-caused the `adx init` crash; found the `--exec` worktree bypass and proved it with a live file-write probe; found and reproduced mutation-testing crash-corruption; started the MCP server for real and called all 6 tools, surfacing a live BER divergence and a third JSON-schema shape; confirmed via `gh api` that the real repository has had zero commits since 2026-07-07; wrote this note plus [[Safety-Critical Gaps]], [[Process and CI Gaps]], [[Dead-on-Arrival Code]], and a first, deliberately unresearched version of [[Competitive Positioning]].
- **2026-08-07 (same day, second pass):** Verified the npm package-name collision independently (registry query + real clean install); confirmed no LICENSE file or license metadata anywhere; confirmed adx's 7–8%/34% claim has zero citation; wrote [[Distribution and Adoption Gaps]]. Did the real Factory AI research owed from the first pass — found the accountability-comparison framing was directionally right but needed a real correction (Factory doesn't out-perform adx's Agency Ladder, it doesn't attempt that problem at all), and found Factory's own published methodology has an undisclosed-validation gap paralleling adx's uncited numbers. Rewrote [[Competitive Positioning]] in place with sourced findings.
