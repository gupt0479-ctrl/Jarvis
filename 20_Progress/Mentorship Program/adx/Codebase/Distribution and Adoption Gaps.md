---
type: input
status: sprout
created: 2026-08-07
updated: 2026-08-07
tags:
  - summary
notes:
  - "[[Codebase Deep Read]]"
  - "[[Source Claims]]"
  - "[[Recommended Fixes]]"
source_url: https://github.com/ahnafyy/adx
input_kind: github
track: ai
---
# adx — Distribution and Adoption Gaps
**Source:** `npm view adx` and a real `npm install adx` in a clean, isolated directory (not the sandbox clone, not the throwaway repo); every `package.json` in `sandbox/adx`; root directory listing for `LICENSE`
**Verified:** 2026-08-07
**Scope:** package distribution and legal/adoption surface — not the code's behavior, whether anyone can reach it in the first place
## Source
Everything else written this session assumes someone already has the code running. This note checks the layer before that: can a new user actually get adx onto their machine by following the docs, and would a team doing real due diligence stop before they even try. Both checks came from a lead flagged mid-review, verified independently here, not taken on report.
## Key Claims
- **The npm package name `adx` is already taken by an unrelated party.** `npm install -g adx` — literally the first command in the getting-started docs — installs a different, dead package, silently, with no error.
- **This isn't a docs typo for a correctly-scoped name.** Every package in the monorepo uses the bare, unscoped name (`adx-cli/package.json`'s real `name` is `"adx"`); `.changeset/config.json` links release versioning around that same bare name. The intent was always the unscoped name.
- **The package is currently unpublishable to npm as configured**, independent of the docs — npm doesn't allow publishing over an existing unscoped name under a different owner.
- **No LICENSE file exists anywhere in the repository**, and no package.json across all 8 packages declares a `license` field either.
- **adx's own "7–8% fewer tokens, 34% fewer file revisits" claim has no citation anywhere** — not in the repo, not on the docs site, not as a linked study.
## Full Content
### `npm install -g adx` installs the wrong package, with zero error
==Verified two independent ways: `npm view adx` against the real registry, and an actual `npm install` in a clean directory — both confirm a real, unrelated, essentially-empty package with no functioning CLI at all.==
```
$ npm view adx
adx@0.0.0 | MIT | deps: none | versions: 1
maintainers: youlingred <30897863@qq.com>
published over a year ago
created: 2019-05-28
```
Installed fresh in an isolated directory (not the sandbox clone, not the throwaway repo):
```json
{
  "name": "adx",
  "version": "0.0.0",
  "description": "",
  "main": "index.js",
  "author": "xiehui <30897863@qq.com>",
  "license": "MIT"
}
```
No `index.js` file actually shipped in the tarball — `find` on the installed package returned only `package.json`. No `.bin` entry was created. This package predates Ahnaf's project by seven years and has nothing to do with it. A user who runs the exact first command on `ahnafyy.github.io/adx/getting-started/` gets a silent, successful install of an empty package with no `adx` command afterward — not an error, not a wrong-version warning, nothing that would tell them something's off.
### This was never a scoping mistake — the bare name was always the intent
==Every one of the 8 packages uses an unscoped name; the changeset release config groups them by that same bare `"adx"` string. This is a genuine collision, not a docs command that forgot a `@scope/`.==
```
packages/adx-cli/package.json:      "name": "adx",
packages/adx-sweep/package.json:    "name": "adx-sweep",
packages/adx-vscode/package.json:   "name": "adx-vscode",
... (all 8 packages, all unscoped)
```
`.changeset/config.json`: `"linked": [["adx", "adx-core", "adx-shape", "adx-gate", "adx-sweep", "adx-maintain"]]` — the release-versioning group is built around the literal string `"adx"`. No `publishConfig` field anywhere in any package.json, no `.npmrc`, no registry override in `pnpm-workspace.yaml`. Nothing in the repository suggests a scoped name (`@ahnafyy/adx` or similar) was ever the plan.

This makes it worse than a documentation bug: even if `getting-started.md` were rewritten today with the correct install command, there isn't a correct command to write, because **`npm publish` on the current package as configured will fail outright** — npm requires unscoped package names to be globally unique, and this one belongs to someone else. The only real fixes are renaming the package (to a scoped name, e.g. `@ahnafyy/adx`) or acquiring the existing name from its current maintainer. Both are bigger changes than a docs edit.
### No LICENSE — not the file, not even the metadata field
==Checked both: no `LICENSE` file at the repository root, and no `package.json` across all 8 packages declares a `license` field at all.==
```
$ ls | grep -i licen
(no output)
$ grep -H '"license"' packages/*/package.json
(no output)
```
The unrelated squatted npm package at least declares `"license": "MIT"` in its metadata — Ahnaf's own packages don't, anywhere. For a team doing real adoption due diligence on a dependency, an npm registry page (if this were ever published) showing "License: not specified" is itself a stop-and-ask-legal moment, separate from and prior to any question about whether the tool works.
### The tool's own precision claim has no source
==`abstraction.ts`'s comment states specific numbers — "7–8% fewer tokens," "34% fewer file revisits" — as empirical fact. No benchmark file, dataset, citation, or methodology note exists anywhere in the repository or docs site.==
```
// Empirically, clean code with a high signal-to-noise ratio costs 7–8% fewer
// tokens for agents to process and requires 34% fewer file revisits during
// investigation.
```
The same numbers get restated as flat claims in two separate `README.md` files (`adx-gate/README.md` and `adx-shape/README.md`) — and in the second one, "34%" is repurposed for a conceptually different claim ("agents spend 34% of their session re-reading files they've already seen") rather than the file-revisit-count framing used everywhere else. Searched the full repo and docs site for any benchmark file, dataset, results directory, or the words "study"/"whitepaper"/"benchmark"/"citation" anywhere near these numbers: nothing. See [[Competitive Positioning]] for how this compares to Factory AI's own published methodology, which turned out to have a real but different gap.
## Why It Matters
Every other note in this folder assumes a reader already has adx installed and running. This is the layer before that, and it's currently broken in a way the other findings aren't: silent, not loud. A crashing `init` command at least tells you something's wrong. A wrong package installing cleanly under the right name doesn't — a new user just gets confused later, with no error message pointing back here.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[Competitive Positioning]] — the citation-gap finding here has a direct, sourced parallel in how Factory AI's own scoring methodology turned out to be disclosed
- [[Source Claims]] — captured the getting-started page's exact install sequence (`npm install -g adx && adx init` etc.) this note checks the first step of
- [[Recommended Fixes]] — none of its existing items cover distribution; this is new ground
## Open Questions
- [ ] Is renaming to a scoped package (`@ahnafyy/adx`) or negotiating for the existing name the right call? Scoped names are free and immediate; acquiring an inactive name from its owner is unpredictable and can take a long time.
- [ ] Does Ahnaf know the package has never actually been published to npm under any name — or was this assumed working because `npm install -g adx` "looks like" a normal, working instruction?
