---
type: project
status: in-progress
created: 2026-06-15
tags:
  - portfolio
  - security
  - sanity
  - backend
---

# Phase 2 — Sanity Backend Lockdown

> Goal: No visitor can mutate Sanity data. Read-only for the world; writes only via authenticated Studio.

→ All prompts for this phase: [[claude-code-prompts#phase-2]]
→ Manual steps: [[manual-actions#phase-2]]

---

## What Claude Code found in the actual codebase

**SANITY_API_TOKEN reaches the browser.** In `src/sanity/lib/live.ts`, next-sanity's Live SSE connection passes the token as `browserToken`. This is expected behaviour for Sanity Live — but it means the token **must** be a Viewer (read-only) token. If it's an Editor or higher, any user who opens DevTools can extract it and mutate your content.

**Open redirect in draft-mode endpoint.** The handler reads `request.nextUrl.searchParams.get("redirect")` and uses it without validation. Low severity because the endpoint requires `SANITY_REVALIDATE_SECRET`, but still worth patching.

**Env var name correction.** The actual env var is `SANITY_REVALIDATE_SECRET`, not `SANITY_PREVIEW_SECRET`. The old notes had the wrong name.

**CSP is Report-Only.** There is a TODO comment in `next.config.ts` noting that the header is `Content-Security-Policy-Report-Only`, not `Content-Security-Policy`. It reports violations but does not block anything. Enforcement is done in Phase 4.

---

## Step 1 — Verify SANITY_API_TOKEN is a Viewer-scoped token

`SANITY_API_TOKEN` is used in two places:
1. Server-side in `src/sanity/lib/server-client.ts` (safe — never reaches browser)
2. As `browserToken` in `src/sanity/lib/live.ts` for the Live SSE connection (reaches the browser intentionally)

Because it reaches the browser, the token's permissions are the ceiling on what an attacker can do with it. A Viewer token can only read published documents — exactly what the public portfolio needs.

**Check in Sanity dashboard:** `sanity.io/manage` → project → API → Tokens. Find the token currently set as `SANITY_API_TOKEN`. Its role must be **Viewer**. If it's Editor, Deploy Studio, or Administrator — rotate it immediately with a new Viewer token.

If you need to create a new Viewer token:
1. Sanity Manage → API → Tokens → Add API Token
2. Name: `portfolio-viewer-prod`
3. Permissions: **Viewer**
4. Copy the token, update `.env.local`, update Vercel env vars, redeploy

---

## Step 2 — Patch the open redirect in draft-mode

**File:** `src/app/api/draft-mode/enable/route.ts` (or wherever draft mode is enabled)

Current vulnerable pattern:
```typescript
const redirect = request.nextUrl.searchParams.get("redirect");
// used directly with no validation ← open redirect
```

Fix — restrict redirect to same-origin paths only:
```typescript
const redirectParam = request.nextUrl.searchParams.get("redirect") ?? "/";
// Strip any protocol/host — only allow same-origin relative paths
const safePath = redirectParam.startsWith("/") && !redirectParam.startsWith("//")
  ? redirectParam
  : "/";
return NextResponse.redirect(new URL(safePath, request.url));
```

This prevents an attacker from crafting a link like:
`/api/draft-mode/enable?secret=X&redirect=https://evil.com`

---

## Step 3 — Confirm no mutation calls in Next.js server code

The golden rule: Next.js server code reads; Studio writes. Scan for any violations:

```bash
grep -rn "\.create(\|\.patch(\|\.delete(\|\.mutate(\|\.transaction(" src/ \
  --include="*.ts" --include="*.tsx"
```

Expected results:
- Contact form Server Action: acceptable if it writes only to a `contact` document type
- Any other result: investigate immediately

If the contact form does write to Sanity, confirm:
1. It uses a separate write token with minimum scope (not the browserToken)
2. That write token is only in a server-side environment variable (never `NEXT_PUBLIC_`)

---

## Step 4 — Studio route has no content flash

**Files:** `middleware.ts` and `src/app/studio/layout.tsx`

See [[phase-1-auth-clerk#step-3]] — the layout guard is shared between phases. `/studio` must redirect before rendering. The middleware catches the route first; the layout is a second layer of defence.

---

## Step 5 — Verify CORS via Sanity dashboard

Sanity CORS must list only known origins. Wildcards are not acceptable.

Go to `sanity.io/manage` → project → API → CORS Origins. The list should include only:
- `http://localhost:3000` (development)
- `https://[your-vercel-domain].vercel.app` (production)
- `https://[your-custom-domain]` (if using one)

Remove any `*` or unknown entries. "Allow credentials" must be **Yes** for your own origins.

---

## Step 6 — SANITY_REVALIDATE_SECRET is set and used

The correct env var name (from the actual codebase) is `SANITY_REVALIDATE_SECRET`.

Confirm it exists in `.env.local`:
```bash
grep "SANITY_REVALIDATE_SECRET" .env.local
```

If missing, generate one and add it:
```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Add to `.env.local` and to Vercel env vars. Confirm `next.config.ts` or the revalidate route reads this variable by this exact name.

---

## Acceptance criteria

- [x] Open redirect in draft-mode endpoint patched (relative paths only) — `src/app/api/draft-mode/enable/route.ts`
- [x] Zero mutation calls in Next.js server code (grep clean) — only `Map.delete()` in space-float-ticker.ts
- [x] `SANITY_REVALIDATE_SECRET` present in `.env.local` — confirm it's also in Vercel env vars (manual)
- [x] `/studio` redirects without content flash — `auth.protect()` is first logic in layout
- [x] CSP `connect-src` covers `https://*.sanity.io` and `https://*.api.sanity.io` for Live SSE
- [ ] `SANITY_API_TOKEN` confirmed as **Viewer** role in Sanity dashboard (MANUAL — sanity.io/manage → API → Tokens)
- [ ] Sanity CORS list contains only known origins, no wildcards (MANUAL — sanity.io/manage → API → CORS Origins)
- [ ] `SANITY_REVALIDATE_SECRET` added to Vercel env vars (MANUAL)
