---
type: input
status: sprout
created: 2026-07-29
tags:
  - github
  - action
  - claude-code
notes:
  - "[[40_Resources/CS/Repos]]"
  - "[[How Anant Uses Each Repo]]"
  - "[[Useful Repos - Shortlist]]"
  - "[[GitHub Ingestion Implementation]]"
  - "[[00_Execution#Github]]"
---
# Immediate Action
What actually got installed, tested, and decided this session — real hands-on work in WSL (`gupta-builds/second-brain-claudekit` at `~/projects/ai/claude/second-brain-claudekit`), not a plan. Every verdict below is from a real clone and a real run, not a repo README. Split into three: **Global** (Jarvis + every project, WSL and Windows), **Project-based** (one repo/project only), **Unsure** (the rest of `40_Resources/CS/Repos.md` that never got a real decision this session — still starred, still undecided).
## Global
### GBrain — INSTALLED, TESTED, WORKING
`bun install` (283 packages) → `bun run src/cli.ts init --pglite --no-embedding` → `doctor` reports **80/100 overall health, 100/100 brain score**, real PGLite database at `~/.gbrain/`. This is a genuine working install, not a plan. The one open decision: it's running keyword/graph-only right now — full semantic search needs one of `OPENAI_API_KEY`, `ZEROENTROPY_API_KEY`, or `VOYAGE_API_KEY`, none of which are set. That's a real recurring cost decision (Voyage and ZeroEntropy both have usable free tiers; OpenAI doesn't) — not yet made. Paired with gstack's `/setup-gbrain` per [[gstack]], this is the centerpiece of the memory-architecture decision from [[00_Execution#Github]] — confirmed for real, not just referenced.
**Next:** pick an embedding provider (Voyage's free tier is the obvious first try), re-run `gbrain init --pglite` with it set, then promote from the sandbox to the real global `~/.claude/` — not done yet, the sandbox install is the only one that exists right now.
### bun — INSTALLED (new dependency)
Wasn't present in WSL at all. Installed via the checksum-documented method from gstack's own setup script (`curl -fsSL https://bun.sh/install`, version-pinned 1.3.10, got 1.3.14). This is now a real, permanent addition to the WSL environment — gstack, gbrain, and any future bun-based tool all depend on it being there. Not reversible without noticing (removing it breaks the above), but low-risk and standard.
### mattpocock-skills — PARTIAL, needs a real decision
Cloned; the interactive installer (`bunx skills@latest add mattpocock/skills` — `npx` routes to Windows npm from inside WSL and fails with `ERR_INVALID_URL`, use `bunx` instead) discovered **41 skills**, not the 18 the vault notes describe. Its interactive picker doesn't complete non-interactively, so instead of fighting it, the `engineering/` category (17 skills — `code-review`, `tdd`, `diagnosing-bugs`, `implement`, `research`, `to-spec`, `to-tickets`, `codebase-design`, `domain-modeling`, `improve-codebase-architecture`, `resolving-merge-conflicts`, `triage`, `wayfinder`, `ask-matt`, `grill-with-docs`, `prototype`, `setup-matt-pocock-skills`) was copied directly into `second-brain-claudekit/tested-skills/mattpocock-engineering/` for real review. **Not promoted to global yet** — read these 17 for real before deciding which subset actually earns a spot in `~/.claude/commands/`, rather than installing all 41 (`personal`, `productivity`, `misc`, `in-progress`, `deprecated` categories exist too and were not reviewed).
## Project-based
### gstack — BLOCKED, real system dependency missing
Cloned, ran the real `./setup` script. It got genuinely far: compiled the browse/design/PDF binaries, generated **55 skills (~893,538 tokens if all loaded at once — that's the actual current size, not "13 skills")**, downloaded Chromium (278MB). It then failed at the final step: **"gstack setup failed: Playwright Chromium could not be launched"** — WSL is missing the shared libraries headless Chromium needs. `sudo` requires an interactive password in this environment, so the fix couldn't be completed here. Nothing got registered (`~/.claude/skills/gstack` and `~/.claude/commands/gstack*` both confirmed absent — the setup aborted before the registration step, not after).
**Fix required, run this yourself in a real WSL terminal:**
```bash
sudo apt-get update && sudo apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2
cd ~/projects/ai/claude/second-brain-claudekit/sandbox/gstack && ./setup
```
Once that succeeds, decide global vs. project-scoped for real (gstack's own setup targets Claude Code, Codex, Factory, and OpenCode skill directories simultaneously — it's designed to be global by default). This is genuinely project-based *for now* only because it's blocked, not by design.
### openbb, tradingview-mcp, polymarket-mcp-server, claude-context
Unchanged from [[00_Execution#Github]] — real, correctly project-scoped to TradingView (openbb, tradingview-mcp, polymarket-mcp-server as architecture reference) and BOOM (claude-context, still blocked on the same Milvus/Docker dependency, not attempted this session).
## Unsure
Everything in `40_Resources/CS/Repos.md` not named above never got a real decision this session — still starred, still exactly where the GitHub pass in [[00_Execution#Github]] left them (Ruflo, Multica, AgentScope, Goose, OpenCode, browser-use, Kronos, Jan, last30days-skill, CL4R1T4S, polymarket-mcp-server's live-mode question, and the whole Learning/Projects/Jobs/Cybersecurity sections). Not touched, not forgotten — just genuinely not this session's scope. See `40_Resources/CS/Repos.md` directly for the full list and its per-repo markers.
