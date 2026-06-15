---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, monitoring, vercel, observability]
---

# Phase 5 — Runtime Monitoring & Incident Response

> The site is live. These steps ensure you know when something breaks before a recruiter finds it.

→ All prompts for this phase: [[claude-code-prompts#phase-5]]
→ Manual steps: [[manual-actions#phase-5]]

---

## Critical correction: `/api/health` is Clerk-protected

Claude Code found that the existing `/api/health` route (if it exists) returns 401 because Clerk middleware applies to the `/api/(.*)` matcher. An uptime monitor hitting this endpoint will always see 401 and think the site is down.

Two options to fix this — pick one:

**Option A — Exempt `/api/health` from Clerk middleware (recommended)**

In `middleware.ts`:
```typescript
const isProtectedRoute = createRouteMatcher([
  '/studio(.*)',
  // do NOT include /api/health here
]);
```

The middleware matcher in `config.matcher` likely catches all `/api/(.*)`. Add a negative lookahead or explicitly exclude `/api/health`:
```typescript
export const config = {
  matcher: [
    '/((?!_next|api/health|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico)).*)',
    '/(api(?!/health)|trpc)(.*)',
  ],
};
```

**Option B — Move health check to a route Clerk doesn't touch**

Rename to `/api/public/health/route.ts` and update the middleware matcher to exclude `/api/public/(.*)` from Clerk.

---

## Step 1 — Create `/api/health` endpoint

**File:** `src/app/api/health/route.ts`

```typescript
import { NextResponse } from 'next/server';

export async function GET() {
  const checks = {
    server: true,
    // Check env var presence only — never log values
    ai_primary:   Boolean(process.env.CEREBRAS_API_KEY ?? process.env.GEMINI_API_KEY),
    ai_fallback:  Boolean(process.env.GROQ_API_KEY),
    chat_secret:  Boolean(process.env.CHAT_TOKEN_SECRET),
    upstash:      Boolean(process.env.UPSTASH_REDIS_REST_URL),
    sanity_token: Boolean(process.env.SANITY_API_TOKEN),
  };

  const allHealthy = Object.values(checks).every(Boolean);

  return NextResponse.json(
    {
      status: allHealthy ? 'ok' : 'degraded',
      checks,
      ts: new Date().toISOString(),
    },
    { status: allHealthy ? 200 : 503 }
  );
}

// Prevent Next.js from caching this route
export const dynamic = 'force-dynamic';
```

After creating it and fixing the Clerk middleware (above), verify:
```bash
curl http://localhost:3000/api/health
# Expected: {"status":"ok","checks":{"server":true,...},"ts":"..."}
```

---

## Step 2 — Add a client error reporter (optional, useful)

If Orby crashes in the browser, you want to know. Add error reporting to `ChatErrorBoundary` (created in Phase 3):

```typescript
componentDidCatch(error: Error, info: React.ErrorInfo) {
  if (process.env.NODE_ENV === 'production') {
    fetch('/api/error-report', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: error.message,
        stack: error.stack?.slice(0, 500),
        component: info.componentStack?.slice(0, 200),
      }),
    }).catch(() => {}); // fire-and-forget
  }
}
```

**File:** `src/app/api/error-report/route.ts`
```typescript
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    console.error('[client-error]', JSON.stringify({
      error: body.error,
      stack: body.stack,
      component: body.component,
    }));
  } catch {}
  return new NextResponse(null, { status: 204 });
}
```

This logs client crashes to Vercel Function logs without requiring an external service. Exempt `/api/error-report` from Clerk middleware the same way as `/api/health`.

---

## Step 3 — Post-deploy smoke tests

After the first Vercel production deployment:

```bash
DOMAIN="https://your-portfolio.vercel.app"

# Homepage
curl -s -o /dev/null -w "%{http_code}" "$DOMAIN"
# Expected: 200

# Security headers present
curl -I "$DOMAIN" | grep -iE "x-frame-options|strict-transport|content-security-policy"
# Expected: all three present

# Studio redirect
curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/studio"
# Expected: 302 or 307

# Chat without token
curl -s -o /dev/null -w "%{http_code}" -X POST "$DOMAIN/api/chat" \
  -H "Content-Type: application/json" \
  -H "Origin: $DOMAIN" \
  -d '{"messages":[{"role":"user","content":"hi"}]}'
# Expected: 401

# Bad origin
curl -s -o /dev/null -w "%{http_code}" -X POST "$DOMAIN/api/chat" \
  -H "Origin: https://evil.com" -d '{}'
# Expected: 403

# Health
curl -s "$DOMAIN/api/health" | python3 -m json.tool
# Expected: {"status":"ok",...}
```

---

## Incident response playbook

### Site down (5xx or 502 from Vercel)
1. Vercel dashboard → Deployments → find the failed one
2. Rollback: click the last green deployment → "Promote to Production" (takes ~30 seconds)
3. `git log --oneline -5` — identify what changed since the last good deploy
4. Fix in a branch, confirm preview deploy works, then merge to `main`

### Orby returns 500
1. Vercel dashboard → Functions → `api/chat` → Logs
2. Find the exact error and traceback
3. Common causes:
   - Upstash down: should degrade gracefully after Phase 3 fix — if still 500, the fix wasn't applied
   - Cerebras quota hit: Groq fallback should kick in — if not, check model-router.ts
   - `CHAT_TOKEN_SECRET` missing in Vercel env vars: add it and redeploy

### Sanity content blank
1. Check `sanity.io` status page
2. Confirm `SANITY_API_TOKEN` is in Vercel env vars (not just `.env.local`)
3. `sanityFetch()` should fall back to `loadLocalQueryResult()` — if it doesn't, the local fallback data may be stale

### Clerk sign-in broken
1. Check Clerk dashboard → Applications → your app
2. Confirm both `CLERK_SECRET_KEY` and `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` are in Vercel env vars
3. Test vs dev keys: `pk_test_*` only works with `CLERK_SECRET_KEY` starting with `sk_test_*`

### Suspected unauthorized Studio access
1. Clerk dashboard → Users → check recent sign-in activity
2. If unknown sign-ins: select user → Revoke sessions
3. Rotate `CLERK_SECRET_KEY` in Vercel env vars, redeploy
4. Check Sanity History for unauthorized edits: `sanity.io/manage` → project → History

---

## Acceptance criteria

- [ ] `/api/health` returns 200 with `{"status":"ok"}` — not 401
- [ ] Uptime monitor configured and sending alerts to `anantmahi721@gmail.com`
- [ ] Vercel Analytics and Speed Insights enabled
- [ ] All post-deploy smoke tests pass
- [ ] Incident playbook read — you can do a Vercel rollback in under 2 minutes
