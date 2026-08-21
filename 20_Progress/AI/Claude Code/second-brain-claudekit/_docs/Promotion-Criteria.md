# Promotion Criteria — what "cleared the qualification bar" actually means

`_docs/Architecture.md` names four pipeline stages and says a tool moves between them when it "clears the qualification bar." This doc spells out what that bar is. The literal, mechanically-checkable version of this lives in `60_Claude/Qualification-Checklist.md` — this doc is the reasoning behind that checklist, with the three real 2026-07-29 outcomes (gbrain, gstack, mattpocock-skills) as worked examples of the bar actually being applied, not a hypothetical rubric.

## The four questions, in order

Adapted directly from the **Implement > Knowledge** principle already established in the Jarvis vault (`60_Claude/20_Distilled_Notes/Sources - Plan/PDF's Ingestion Implementation.md`) — see `_docs/Design.md` for the full citation. Each question is a hard gate: a "no" stops the tool at its current stage, it doesn't get rounded up to a "maybe."

### 1. Did it actually run without a manual workaround?

Not "does the README claim it works" — did a real command, executed in `sandbox/<repo>/`, actually complete or fail on its own terms?

- **gbrain: yes for the original install** — `bun install` → `bun run src/cli.ts init --pglite --no-embedding` → `doctor` returned real output (80/100 health) against a real database file. No workaround needed. **Update, 2026-08-20:** wiring the OpenAI embedding provider (the decision that had been pending since this Q1 line was written) turned up a real, undocumented gbrain bug — none of `gbrain config set embedding_disabled false`, `gbrain init --embedding-model`, or `gbrain reinit-pglite` (gbrain's own documented switch path) actually clear a stuck `embedding_disabled: true` sentinel in `~/.gbrain/config.json`; only a direct JSON-file edit does. Root-caused by reading `src/commands/init.ts` directly, not guessed. Full account: `tested-tools/mcp-servers/gbrain/VERDICT.md`. Verified working afterward with a real imported+embedded+semantically-searched test page (0.8275 similarity score) — the tool clears Q1 in substance, but not "without a workaround" in the letter, and that distinction is worth keeping visible rather than rounding up to a clean yes.
- **gstack: no.** `./setup` ran real work (compiled binaries, generated 55 skills, downloaded Chromium) but the final Playwright launch check failed on a genuinely missing system dependency. The honest failure is why this tool stays in `sandbox/`, blocked, rather than being marked done because "most of it worked."
- **mattpocock-skills: partial-yes.** The installer ran and discovered 41 real skills; its interactive picker doesn't complete non-interactively, so the workaround (copying `engineering/` by hand) was a deliberate, disclosed scope decision, not a technical failure — this is why it advanced to `tested-tools/` rather than staying in `sandbox/`, but only for the reviewed subset.

### 2. Does it solve a problem nothing else already solves?

Checked against what's already adopted or already decided, not against the tool's own marketing.

- **gbrain: yes**, confirmed by elimination — adopting it made `memsearch` (auto-capture without synthesis) and `context-sync` (thinner SQLite memory) both redundant. Its synthesis + gap-analysis layer, benchmarked +31.4 points over vector-only RAG, is a capability nothing else in the current stack has.
- **gstack: yes, if unblocked** — its `/setup-gbrain` companion command and 55-skill library aren't duplicated elsewhere; the blocker is infrastructure, not redundancy.
- **mattpocock-skills' `engineering/` category: mostly yes, unconfirmed in detail** — `code-review`, `tdd`, `diagnosing-bugs` etc. don't obviously duplicate anything already installed, but this is exactly what the `tested-tools/` second-look stage exists to confirm skill-by-skill before promotion, not something to assume from the category name.

### 3. Is it a duplicate of something already promoted?

The inverse framing of question 2, asked again at the moment of promotion (not just discovery), because the answer can change between when a tool enters `sandbox/` and when it's considered for promotion — something else might get promoted first.

- Before gbrain existed in `sandbox/`, `context-sync` and `memsearch` were both live candidates. Once gbrain cleared the bar, both became duplicates. This is why the qualification pass happens per-decision, not once per tool.

### 4. Can the dependency it claims actually be verified, mechanically, not by re-reading the README?

This is the one question worth a script instead of a judgment call — see `60_Claude/scripts/check_dependency.py`. A tool's own docs claiming "requires bun" or "requires Chromium system libs" is a claim; whether that dependency is actually on `PATH` (or actually installed, actually the right version) in *this* environment is a fact, and facts are cheap to check mechanically before trusting them.

- `bun` — verified on `PATH` after gstack's setup script installed it (checksum-pinned to 1.3.10, resolved to 1.3.14). This is exactly the kind of claim the script formalizes: don't trust "bun is a prerequisite," check that `which bun` actually returns something before believing an install succeeded because of it.
- Chromium's shared library dependencies (`libnss3`, `libatk1.0-0`, etc.) — this is the gstack blocker, and it's exactly the failure mode question 4 exists to catch *before* wasting the setup script's runtime rediscovering it. `60_Claude/scripts/check_dependency.py` includes this exact check as its worked example.

## What "cleared the bar" does NOT mean

- It does not mean "compiles" or "installs without error" alone — question 2 and 3 still have to be answered honestly, not skipped because question 1 was a clean yes.
- It does not mean permanent. A tool can be un-promoted if a later, better-fitting tool makes it redundant (memsearch's fate once gbrain existed) — the bar is evaluated at each promotion decision, not locked in once passed.
- It does not require unanimous confidence. gstack's `engineering/`-style partial promotion (mattpocock-skills) shows the bar can be cleared for a *subset* of a repo while the rest stays unreviewed — "cleared the bar" is a per-decision, not always per-repo, judgment.
