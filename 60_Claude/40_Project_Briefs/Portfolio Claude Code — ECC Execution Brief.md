---
type: project
status: active
created: 2026-06-05
updated: 2026-06-05
tags:
  - claude-code
  - portfolio
  - ecc
  - deployment
  - execution-brief
project: portfolio
notes:
  - "[[60_Claude/40_Project_Briefs/Claude Optimization Master Setup]]"
---

# Portfolio Claude Code — ECC Execution Brief

> **For Claude Cowork.** Read this entire note first. Then execute every phase in order. Do not plan — do. Each step has an exact command or file content. Run it, verify it, move on.

**Project path:** `/home/anant_gupta/projects/hub/portfolio`
**Goal:** Zero build errors. Clean `.claude/` folder. ECC fully wired. Everything committed.

---

## Context — What Was Already Done

A prior session completed the following. Do not redo them:

- Root `CLAUDE.md` → rewritten as comprehensive Claude guide
- `.claude/CLAUDE.md` → rewritten, current architecture, no chatbot
- `.claude/commands/` → created with 5 slash commands (deploy, build-fix, review, sanity-push, add-project)
- `.claude/settings.json` → ECC plugin enabled + 15 Bash/WebSearch permissions
- `MEMORY.md` → updated
- `~/.claude/projects/.../memory/project-setup.md` → created

**What still exists that is wrong:**
- 7 stale dead files in `.claude/` root (cmd-*.md, hook-*.sh, SETUP-INSTRUCTIONS.md)
- `settings.local.json` → needs to be merged into `settings.json` then deleted
- `mcp-settings.json` → wrong name, needs to become `mcp.json`
- `graphify-out/cache/` → not in `.gitignore`, 130+ files should not be committed
- Build pipeline → not yet verified clean

---

## Phase 1 — Read These Files First

Before touching anything, read all of these:

```
/home/anant_gupta/projects/hub/portfolio/.claude/settings.json
/home/anant_gupta/projects/hub/portfolio/.claude/settings.local.json
/home/anant_gupta/projects/hub/portfolio/.claude/mcp-settings.json
/home/anant_gupta/projects/hub/portfolio/.gitignore
/home/anant_gupta/projects/hub/portfolio/package.json
/home/anant_gupta/projects/hub/portfolio/CLAUDE.md
/home/anant_gupta/projects/hub/portfolio/.claude/CLAUDE.md
```

Also run: `find /home/anant_gupta/projects/hub/portfolio/.claude -type f | sort`

This tells you the current state. Now proceed.

---

## Phase 2 — Delete 7 Stale Files

These files do nothing. The `cmd-*.md` files are in the wrong directory (Claude Code only reads commands from `.claude/commands/`). The hook scripts are unregistered. Delete all of them in one command:

```bash
rm \
  /home/anant_gupta/projects/hub/portfolio/.claude/cmd-deploy.md \
  /home/anant_gupta/projects/hub/portfolio/.claude/cmd-add-project.md \
  /home/anant_gupta/projects/hub/portfolio/.claude/cmd-index-docs.md \
  /home/anant_gupta/projects/hub/portfolio/.claude/cmd-sanity-push.md \
  /home/anant_gupta/projects/hub/portfolio/.claude/hook-biome-format.sh \
  /home/anant_gupta/projects/hub/portfolio/.claude/hook-pre-commit-lint.sh \
  /home/anant_gupta/projects/hub/portfolio/.claude/SETUP-INSTRUCTIONS.md
```

Verify: `ls /home/anant_gupta/projects/hub/portfolio/.claude/` — should show only `CLAUDE.md`, `commands/`, `settings.json`, `settings.local.json`, `mcp-settings.json`.

---

## Phase 3 — Overwrite settings.json (Merge + Finalize)

The current `settings.json` is missing `enableAllProjectMcpServers` from `settings.local.json` and the global agent/skill Read permissions. Write this exact content:

**File:** `/home/anant_gupta/projects/hub/portfolio/.claude/settings.json`

```json
{
  "enabledPlugins": {
    "everything-claude-code@everything-claude-code": true
  },
  "enableAllProjectMcpServers": true,
  "permissions": {
    "allow": [
      "Bash(pnpm *)",
      "Bash(npx @biomejs/biome *)",
      "Bash(npx biome *)",
      "Bash(tsc *)",
      "Bash(node *)",
      "Bash(node scripts/*)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git add *)",
      "Bash(git branch *)",
      "Bash(git rev-parse *)",
      "Bash(git show *)",
      "Bash(ls *)",
      "Bash(find . *)",
      "Bash(grep *)",
      "Bash(cat *)",
      "WebSearch",
      "Read(/home/anant_gupta/.claude/commands/**)",
      "Read(/home/anant_gupta/.claude/agents/**)",
      "Read(/home/anant_gupta/.claude/skills/**)"
    ]
  }
}
```

Then delete the now-redundant `settings.local.json`:

```bash
rm /home/anant_gupta/projects/hub/portfolio/.claude/settings.local.json
```

---

## Phase 4 — Rename mcp-settings.json → mcp.json

Delete the old file and write a clean version. The `.claude/` directory is in `.gitignore` so this is safe — real tokens never get committed regardless.

```bash
rm /home/anant_gupta/projects/hub/portfolio/.claude/mcp-settings.json
```

**Create:** `/home/anant_gupta/projects/hub/portfolio/.claude/mcp.json`

```json
{
  "_readme": "Template only. Set real tokens as shell env vars — they are referenced below. Never hardcode.",
  "mcpServers": {
    "sanity": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@sanity/mcp-server@latest"],
      "env": {
        "SANITY_PROJECT_ID": "${NEXT_PUBLIC_SANITY_PROJECT_ID}",
        "SANITY_DATASET": "production",
        "SANITY_API_TOKEN": "${SANITY_API_TOKEN}",
        "SANITY_API_VERSION": "2024-01-01"
      }
    },
    "vercel": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@vercel/mcp-adapter@latest"],
      "env": {
        "VERCEL_TOKEN": "${VERCEL_TOKEN}"
      }
    }
  }
}
```

---

## Phase 5 — Add Two Missing Commands

### 5A — Create `/typecheck` command

**File:** `/home/anant_gupta/projects/hub/portfolio/.claude/commands/typecheck.md`

```markdown
---
description: Sync Sanity types then run TypeScript strict check — fix every error
---

# /typecheck

1. Run `pnpm typegen` — regenerates src/sanity/types/index.ts from schema. Mandatory first.
2. Run `pnpm typecheck 2>&1` — capture all errors at once
3. Fix errors in this order:
   - Sanity type mismatch → re-run typegen, check src/sanity/schemaTypes/
   - Missing import → @/* alias maps to src/*
   - 'use client' violation → add directive or extract to hook
   - Three.js SSR → wrap with next/dynamic({ ssr: false })
   - Clerk auth() in client → move to server component or API route
   - General type error → fix the type; never use `as any` or @ts-ignore
4. Run `pnpm typecheck` again — must reach 0 errors before stopping
```

### 5B — Create `/performance` command

**File:** `/home/anant_gupta/projects/hub/portfolio/.claude/commands/performance.md`

```markdown
---
description: Audit Core Web Vitals, bundle size, Three.js SSR, image optimization
---

# /performance

1. **Three.js SSR** — confirm ObsidianBackground uses next/dynamic with { ssr: false }:
   `grep -r "ObsidianBackground" src/ --include="*.tsx"`

2. **Raw img tags** — find images not using next/image:
   `grep -rn "<img " src/ --include="*.tsx" --include="*.jsx"`

3. **Console.log in production code:**
   `grep -rn "console\." src/ --include="*.tsx" --include="*.ts" | grep -v "__tests__" | grep -v ".test."`

4. **Over-fetching in GROQ queries** — check that sanityFetch() calls project only needed fields,
   not full documents with `{ ... }` or `*`

5. **Client component audit** — list 'use client' components in sections/ that could be server:
   `grep -rn "'use client'" src/components/sections/ src/components/cards/`

6. **Delegate deep analysis** to: `vercel:performance-optimizer` subagent

## ECC Skills
- `vercel:next-cache-components` — ISR / revalidate patterns
- `vercel:performance-optimizer` — Core Web Vitals, bundle, LCP/CLS
- `everything-claude-code:frontend-patterns` — React 19 performance
```

---

## Phase 6 — Fix .gitignore

Read the current `/home/anant_gupta/projects/hub/portfolio/.gitignore` then append these lines to the end. The `graphify-out/cache/` directory has 130+ AST JSON files that must not be committed. The report and graph files are useful and should stay versioned.

Add to the end of `.gitignore`:

```
# graphify — keep report + graph, exclude cache
graphify-out/cache/
graphify-out/manifest.json
```

---

## Phase 7 — Update .claude/CLAUDE.md

Read `/home/anant_gupta/projects/hub/portfolio/.claude/CLAUDE.md` first. Then insert this section **before** the "Common Pitfalls" section:

```markdown
## ECC Skills for This Project

| Skill | Invoke via | Use When |
|-------|-----------|----------|
| `vercel:nextjs` | `/docs nextjs` | App Router patterns, routing, caching |
| `vercel:next-cache-components` | `/performance` | ISR, revalidate, no-store strategy |
| `vercel:performance-optimizer` | `/performance` | Core Web Vitals, LCP, bundle size |
| `vercel:deployment-expert` | `/deploy` | Vercel build config, env vars, failures |
| `vercel:react-best-practices` | `/review` | React 19, Server Components, hydration |
| `everything-claude-code:typescript-reviewer` | `/review` | Type safety, inference, strict patterns |
| `everything-claude-code:build-error-resolver` | `/build-fix` | Minimal-diff TypeScript fixes |
| `everything-claude-code:security-reviewer` | `/review` | Secrets, auth gaps, injection |
| `everything-claude-code:e2e-runner` | `/e2e` | Playwright test generation |

## Session Discipline

- End every session: `/save-session`
- Start next session: `/resume-session`
- Context getting heavy: `/context-budget` then `/aside` for side questions
- Pattern extraction: `/learn-eval` after significant work
```

---

## Phase 8 — Run the Build Pipeline

This is the core deliverable. Run each step, fix all errors before moving to the next.

### 8A — Check environment

```bash
ls /home/anant_gupta/projects/hub/portfolio/.env.local
```

If missing: the project needs at minimum `NEXT_PUBLIC_SANITY_PROJECT_ID`, `NEXT_PUBLIC_SANITY_DATASET`, `SANITY_API_TOKEN`, `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`, `CLERK_SECRET_KEY`. Check what variables exist and report which are missing. Do NOT create the file with fake values.

### 8B — Install dependencies

```bash
cd /home/anant_gupta/projects/hub/portfolio && pnpm install
```

### 8C — Typegen

```bash
pnpm typegen
```

Expected: exits 0, updates `src/sanity/types/index.ts`. If it fails, check `NEXT_PUBLIC_SANITY_PROJECT_ID` is set.

### 8D — Typecheck

```bash
pnpm typecheck 2>&1
```

Expected: 0 errors. If errors exist, fix every single one using the `/typecheck` workflow. Do not proceed to 8E with errors.

### 8E — Lint

```bash
pnpm lint 2>&1
```

If errors: run `pnpm format` first, then `pnpm lint` again. Fix anything format didn't auto-resolve.

### 8F — Full build

```bash
pnpm build 2>&1
```

Expected: Next.js production build exits 0. If it fails, fix the error — check the "Common Pitfalls" section in `.claude/CLAUDE.md` for patterns.

### 8G — Tests

```bash
pnpm test 2>&1
```

Expected: all Vitest tests pass. Fix any failures — do not comment out or skip.

---

## Phase 9 — Verify Final Structure

Run: `find /home/anant_gupta/projects/hub/portfolio/.claude -type f | sort`

Expected output — exactly these files, nothing else:

```
.claude/CLAUDE.md
.claude/commands/add-project.md
.claude/commands/build-fix.md
.claude/commands/deploy.md
.claude/commands/performance.md
.claude/commands/review.md
.claude/commands/sanity-push.md
.claude/commands/typecheck.md
.claude/mcp.json
.claude/settings.json
```

If you see `cmd-*.md`, `hook-*.sh`, `settings.local.json`, or `mcp-settings.json` — they were not deleted in Phase 2/3/4. Delete them now.

---

## Phase 10 — Commit

`.claude/` is in `.gitignore` and will not be committed. That is correct. Commit only the tracked files that changed:

```bash
git status
git diff CLAUDE.md MEMORY.md .gitignore
git add CLAUDE.md MEMORY.md .gitignore
git commit -m "chore: Claude Code source of truth, ECC workflow, gitignore graphify cache"
```

Do not commit: `.env.local`, `node_modules`, `.claude/` contents, or any secret.

---

## Hard Rules — Do Not Violate

| Rule | Why |
|------|-----|
| No ESLint or Prettier | Biome 2.2.0 is the only linter/formatter |
| No `as any` or `@ts-ignore` | Fix the actual type — never suppress |
| No chatbot / AI Twin / ChatKit | Feature was removed, do not add back |
| No manual edits to `src/sanity/types/index.ts` | Generated file — use `pnpm typegen` |
| No modifying `biome.json` or `tsconfig.json` | ECC's config-protection hook will block it |
| No committing `.env.local` | gitignored for a reason |
| Three.js must use `next/dynamic({ ssr: false })` | SSR + Three.js crashes the build |

---

## Success Criteria

- [ ] `pnpm typegen` exits 0
- [ ] `pnpm typecheck` exits 0 — zero errors
- [ ] `pnpm lint` exits 0 — zero errors
- [ ] `pnpm build` exits 0 — production build clean
- [ ] `pnpm test` — all tests pass
- [ ] `.claude/` has exactly 10 files (1 CLAUDE.md + 7 commands + mcp.json + settings.json)
- [ ] `graphify-out/cache/` is in `.gitignore`
- [ ] `CLAUDE.md`, `MEMORY.md`, `.gitignore` committed to `Chatbot` branch
