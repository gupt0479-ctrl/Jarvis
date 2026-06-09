---
type: project
status: sprout
created: 2026-06-09
tags:
  - project
  - claude-setup
  - portfolio
notes:
  - "[[00 - AI Setup — Index & Integration Guide]]"
  - "[[02 - Deploy Security Checklist]]"
---

# Portfolio Config Pack — copy-paste ready

The actual files live in your portfolio **repo** (WSL), not in this vault. This note is the canonical source you copy from. Drop each block into the path in its heading. Stack: Next.js 16 App Router · React 19 · TS · Tailwind v4 · shadcn/ui · Three.js · Sanity · Clerk · Vitest · Biome · pnpm · Vercel.

Why this layout: one `AGENTS.md` carries conventions so Claude stops guessing; a small set of subagents keep review/test/security work in their own context windows so the main session doesn't drift; hooks make Biome and Vitest run automatically so bad code never reaches a commit. Start with these four agents, add more only when context separation earns its keep.

This replaces the loose `CLAUDE.md` + `cosmic-frontend.mdc` + `three-artist.md` you dumped here during the hackathon — fold those into the blocks below.

## `AGENTS.md` (repo root)

Claude Code and Cursor both read `AGENTS.md`. Keep `CLAUDE.md` as a one-line pointer: `See AGENTS.md`.

```markdown
# Portfolio — Agent Contract

## Stack
- Next.js 16 (App Router) + React 19 + TypeScript (strict)
- Tailwind CSS v4 + shadcn/ui
- Three.js for 3D
- Sanity CMS (content) · Clerk (auth)
- Vitest (test) · Biome (lint+format) · pnpm (package manager)
- Deploy: Vercel, custom .dev domain

## Hard rules
- Server Components by default. Add "use client" ONLY for state, effects, browser APIs, or event handlers.
- Next.js 16: `params` and `searchParams` are Promises — always `await` them.
- Never put secrets in NEXT_PUBLIC_* vars. Server-only secrets stay unprefixed.
- Use pnpm only. Never npm/yarn. Respect pnpm-lock.yaml.
- Run Biome before an edit is "done": `pnpm biome check --write .`
- New behavior needs a Vitest test. Run `pnpm vitest run` before declaring success.
- Three.js scenes mount in client components; dynamic-import with `{ ssr: false }`.
- shadcn/ui: add components via `pnpm dlx shadcn@latest add <name>`, don't hand-roll.
- Sanity: schema changes go through the schema; verify GROQ against the live dataset.
- Clerk: protect routes via middleware; never trust client-side auth state for authorization.

## Workflow
- Plan before multi-file changes. State the files you'll touch.
- Prefer Context7 MCP for any library API question over memory.
- Before deploy, run the security-reviewer subagent and the `/security-review` command.

## Anti-patterns to reject
- Client-side fetching where a Server Component would do.
- Over-using global state. Lift to server / URL where possible.
- Committing without Biome + Vitest passing.
```

## `.claude/agents/frontend-builder.md`

```markdown
---
name: frontend-builder
description: Builds and refactors Next.js/React/Tailwind/shadcn UI. Use for component work, routing, server/client boundaries, Three.js scenes.
tools: Read, Edit, Write, Bash, Grep, Glob
---
You implement UI for a Next.js 16 App Router portfolio. Server Components by default; "use client" only when required. Await params/searchParams. Use shadcn/ui primitives and Tailwind v4 tokens. Dynamic-import Three.js with ssr:false. Check unfamiliar library APIs via Context7 before using them. Always run `pnpm biome check --write .` on files you touch.
```

## `.claude/agents/security-reviewer.md`

```markdown
---
name: security-reviewer
description: Reviews diffs for security issues before deploy. Use proactively after a feature is done and before pushing.
tools: Read, Grep, Glob, Bash
---
You review changes for a public Next.js site on a .dev domain (HSTS-preloaded). Check for: secrets in client bundles or NEXT_PUBLIC_*, missing auth checks on server actions/route handlers, unvalidated input, missing/weak security headers, Clerk route-protection gaps, Sanity tokens with write scope shipped to client, unsafe dangerouslySetInnerHTML, CSP violations from Three.js/Sanity/Clerk. Output an ordered list by severity with file:line and the fix. Report only — do not change code.
```

## `.claude/agents/test-runner.md`

```markdown
---
name: test-runner
description: Writes and runs Vitest tests, diagnoses failures. Use after implementing behavior.
tools: Read, Edit, Write, Bash, Grep
---
You own Vitest coverage. For new behavior, add focused tests. Run `pnpm vitest run`. On failure, read the trace, fix the test or flag the implementation bug, re-run until green. Never mark a task done with red tests.
```

## `.claude/agents/sanity-schema.md`

```markdown
---
name: sanity-schema
description: Designs Sanity schemas and GROQ queries. Use for content modeling and query work.
tools: Read, Edit, Write, Bash, Grep
---
You design structured content for Sanity. Favor references over deep nesting; keep schemas content-shaped, not page-shaped. Write and optimize GROQ against the real dataset. Render Portable Text with a typed serializer. Use the Sanity MCP / sanity-plugin skills when available.
```

## `.claude/settings.json` (hooks — auto Biome + test)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "pnpm biome check --write \"$CLAUDE_FILE_PATHS\" 2>/dev/null || true" }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "pnpm vitest run --silent 2>&1 | tail -5 || true" }
        ]
      }
    ]
  }
}
```

## `.mcp.json` (project-scoped MCP servers)

Commit this so the same servers load for every session in the repo. Tokens go in the shell env, never in this file.

```json
{
  "mcpServers": {
    "context7": { "type": "http", "url": "https://mcp.context7.com/mcp" },
    "vercel": { "type": "http", "url": "https://mcp.vercel.com" },
    "sanity": { "type": "http", "url": "https://mcp.sanity.io" },
    "clerk": { "type": "http", "url": "https://mcp.clerk.com/mcp" },
    "github": { "type": "http", "url": "https://api.githubcopilot.com/mcp/" }
  }
}
```

What each buys you: **Context7** = live, version-correct docs for Next 16 / React 19 / Tailwind v4 / Three.js (stops Claude inventing old APIs). **Vercel** = deploy, read build/runtime logs, search Vercel security docs. **Sanity** = query/author content, build GROQ, design schemas. **Clerk** = correct auth SDK snippets. **GitHub** = PRs, reviews, issues.
