---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, deployment, vercel, headers]
---

# Phase 4 — Pre-Deployment Hardening

> Run every step before pushing to `main`. None of these are optional.

→ All prompts for this phase: [[claude-code-prompts#phase-4]]
→ Manual steps: [[manual-actions#phase-4]]

---

## Step 1 — Flip CSP from Report-Only to enforced

**File:** `next.config.ts`

Claude Code found a TODO comment: the CSP header is currently `Content-Security-Policy-Report-Only`. It reports violations to the browser console but blocks nothing. Before deploy, flip it to enforcement.

Locate the header key in the `headers()` function and change:
```typescript
// Before (report-only — does not block anything)
{ key: 'Content-Security-Policy-Report-Only', value: cspString }

// After (enforced)
{ key: 'Content-Security-Policy', value: cspString }
```

**Before flipping, verify the CSP string doesn't break the site.** Run `pnpm dev`, open the portfolio, and check the browser console for any CSP violation messages. Fix all violations before switching to enforcement — a too-strict CSP will break Three.js, Clerk, Sanity Live, and font loading.

Required CSP sources for this stack:
- `script-src`: `'self' 'unsafe-eval'` (Three.js/WebGL requires `unsafe-eval`)
- `style-src`: `'self' 'unsafe-inline'` (Tailwind requires `unsafe-inline`)
- `img-src`: `'self' data: blob: https://cdn.sanity.io https://images.clerk.dev`
- `connect-src`: `'self' https://*.sanity.io wss://*.sanity.io https://*.clerk.com https://api.groq.com https://*.cerebras.ai https://*.mistral.ai https://*.upstash.io`
- `font-src`: `'self' https://fonts.gstatic.com`
- `frame-src`: `'none'`
- `object-src`: `'none'`

Note: `wss://*.sanity.io` is required for Sanity Live SSE connection.

---

## Step 2 — Full environment variable audit

Run this in the project root before deploying:

```bash
# Find every env var referenced in source
grep -rn "process\.env\." src/ next.config.ts --include="*.ts" --include="*.tsx" \
  | grep -oP "process\.env\.\K\w+" | sort -u
```

Compare the output to `.env.local`. Every variable referenced in code must exist. Missing variables will cause silent failures or 500 errors in production.

**Must be server-only (no `NEXT_PUBLIC_` prefix):**
- `CEREBRAS_API_KEY` (or whatever the actual primary model key is)
- `GROQ_API_KEY`
- `MISTRAL_API_KEY` (or third fallback key)
- `CHAT_TOKEN_SECRET`
- `UPSTASH_REDIS_REST_TOKEN`
- `SANITY_API_TOKEN`
- `SANITY_REVALIDATE_SECRET`
- `CLERK_SECRET_KEY`

**Safe as `NEXT_PUBLIC_` (non-secret):**
- `NEXT_PUBLIC_SANITY_PROJECT_ID`
- `NEXT_PUBLIC_SANITY_DATASET`
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
- `NEXT_PUBLIC_SITE_URL`

If any secret has `NEXT_PUBLIC_` prefix: rename it, update all references, rebuild.

---

## Step 3 — Security headers audit

**File:** `next.config.ts`

After fixing CSP (Step 1), confirm all these headers are present in the `headers()` function:

```typescript
const securityHeaders = [
  { key: 'X-DNS-Prefetch-Control',      value: 'on' },
  { key: 'X-Frame-Options',             value: 'SAMEORIGIN' },
  { key: 'X-Content-Type-Options',      value: 'nosniff' },
  { key: 'Referrer-Policy',             value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy',          value: 'camera=(), microphone=(), geolocation=()' },
  { key: 'Strict-Transport-Security',   value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'Content-Security-Policy',     value: cspString },  // enforced, not report-only
];
```

Verify headers are present after running `pnpm build && pnpm start`:
```bash
curl -I http://localhost:3000 | grep -E "x-frame|x-content|strict-transport|content-security"
```

---

## Step 4 — Secrets scan before committing

```bash
# Confirm .env.local is gitignored
cat .gitignore | grep "\.env"

# Check if .env.local was ever committed
git log --all --full-history -- .env.local

# Scan staged files for common key prefixes
git diff HEAD | grep -E "sk_live|sk_test|ghp_|AKIA|AIza|gsk_|Bearer [A-Za-z0-9+/]{20}"

# Find any console.log leaking env vars
grep -rn "console\.log.*process\.env\|console\.log.*API_KEY\|console\.log.*SECRET\|console\.log.*TOKEN" \
  src/ --include="*.ts" --include="*.tsx"
```

If `.env.local` has ever been committed: rotate every key in it immediately. Treat all values as compromised — even if the commit is old, git history is permanent unless you rewrite it.

---

## Step 5 — Dependency audit

```bash
pnpm audit --prod
```

The `--prod` flag limits to production dependencies (excludes devDependencies). For any HIGH or CRITICAL findings:
1. Check if a fix is available: `pnpm update <package>`
2. If no fix: read the CVE. If the vulnerable code path is not reachable in this app, document it with a comment in `package.json` under a `"securityNotes"` key
3. Never ship with a HIGH/CRITICAL vulnerability in a code path that handles user input or network requests

---

## Step 6 — Full build pipeline must be clean

Run in order — do not skip any step:
```bash
pnpm typegen      # regenerate Sanity TypeScript types
pnpm typecheck    # zero TypeScript errors
pnpm lint         # zero Biome errors
pnpm test         # all Vitest tests pass
pnpm build        # production build succeeds
pnpm start        # start prod build and smoke-test manually
```

Fix every error before deploying. Do not use `@ts-ignore` or `// eslint-disable` to silence errors — fix the underlying issue.

---

## Step 7 — Production smoke tests (local)

After `pnpm start` (production build running locally):

```bash
# 1. Homepage returns 200
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000
# Expected: 200

# 2. Studio redirects (302 or 307) without content
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/studio
# Expected: 302 or 307 (never 200)

# 3. Chat without HMAC returns 401
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"messages":[{"role":"user","content":"hi"}]}'
# Expected: 401

# 4. Bad origin returns 403
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat \
  -H "Origin: https://evil.com" \
  -d '{}'
# Expected: 403

# 5. Health endpoint (after Phase 5 fix — see manual-actions#phase-5)
curl -s http://localhost:3000/api/health
# Expected: {"status":"ok","checks":{...}}
```

All five must pass before deploying to Vercel.

---

## Acceptance criteria

- [ ] CSP header is `Content-Security-Policy` (enforced), not `Content-Security-Policy-Report-Only`
- [ ] No CSP violations in browser console when navigating the full portfolio
- [ ] All secret env vars confirmed server-only
- [ ] All security headers present in response (`curl -I`)
- [ ] `pnpm audit --prod` clean of HIGH/CRITICAL
- [ ] `pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build` all pass
- [ ] All 5 smoke tests return correct status codes
