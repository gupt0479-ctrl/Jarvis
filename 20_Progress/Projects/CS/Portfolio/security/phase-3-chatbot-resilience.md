---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, chatbot, orby, rate-limiting]
---

# Phase 3 — Chatbot Resilience & Security

> Goal: Orby must not break under load, abuse, or model failure. API keys must never leak.

→ All prompts for this phase: [[claude-code-prompts#phase-3]]
→ Manual steps: [[manual-actions#phase-3]]

---

## Corrected ground truth (from actual codebase)

**Model chain is NOT Gemini → Groq → degraded.**
Actual chain (budget-tiered): **Cerebras → Groq → Mistral → degraded text**

**Env var is NOT `GEMINI_API_KEY`.** Verify the actual primary key name:
```bash
grep -n "process.env" src/lib/model-router.ts
```
Use whatever that file actually reads — do not assume.

**Burst limit window is 60 seconds**, not 10 seconds. Exact config from code:
```typescript
burstLimit: Ratelimit.slidingWindow(N, '60 s')
```
Confirm `N` (the request count) by reading `src/app/api/chat/route.ts`.

**Content limit is shorter than 2000 chars.** Read the actual validation in route.ts — the old notes had the wrong number. Use whatever is in the code.

**Upstash downtime = 500 error.** When Redis is unreachable, the rate-limit check currently throws an unhandled error and the chat endpoint returns 500. This needs a try/catch around the Upstash calls.

---

## Step 1 — Audit all AI API keys are server-only

```bash
grep -rn "process\.env\." src/lib/model-router.ts
grep -rn "CEREBRAS\|GROQ\|MISTRAL\|GEMINI\|OPENAI" src/ --include="*.ts" --include="*.tsx"
```

For every key found:
1. The variable name must NOT start with `NEXT_PUBLIC_`
2. The file using it must NOT have `'use client'` at the top
3. The file must be an API route, Server Component, Server Action, or server lib

If any key appears in a client file: move the call to a Server Action immediately. Keys like these authorize spend on external APIs — exposure means anyone can run up your bill.

---

## Step 2 — Confirm HMAC gate returns 401 without a token

Run this from a terminal (not the browser):
```bash
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"messages":[{"role":"user","content":"test"}]}'
```

Expected output: `401`

If it returns `200` or any chat response, the HMAC gate is not enforcing. Open `src/app/api/chat/route.ts`, find the HMAC verification block, and confirm it actually returns early on failure rather than falling through.

---

## Step 3 — Fix Upstash 500 on Redis downtime

**File:** `src/app/api/chat/route.ts`

Current problem: if Upstash is unreachable, the rate-limit `.limit()` call throws and the whole endpoint returns 500.

Fix — wrap both rate-limit checks in try/catch and degrade gracefully:
```typescript
async function checkRateLimit(identifier: string): Promise<{ allowed: boolean; reason?: string }> {
  try {
    const burst = await burstLimit.limit(identifier);
    if (!burst.success) return { allowed: false, reason: 'burst' };

    const daily = await dailyLimit.limit(identifier);
    if (!daily.success) return { allowed: false, reason: 'daily' };

    return { allowed: true };
  } catch (err) {
    // Redis unavailable — log and allow the request rather than blocking users
    console.warn('[chat] Upstash unreachable — rate limiting skipped', err);
    return { allowed: true };
  }
}
```

This ensures a Redis outage causes degraded rate limiting (not enforcement), not a 500 error visible to users.

---

## Step 4 — Confirm model fallback chain catches all errors

**File:** `src/lib/model-router.ts`

The chain is Cerebras → Groq → Mistral → degraded. Verify each handoff:

1. Cerebras quota/error → catches and tries Groq (not throws)
2. Groq quota/error → catches and tries Mistral (not throws)
3. Mistral error → catches and calls `getDegradedText()` (not throws)
4. `getDegradedText()` returns a static string — it cannot fail

Also verify: if the stream breaks mid-response, the error is caught and the client receives a clean `{ error: "..." }` JSON response, not a broken stream that hangs the UI.

---

## Step 5 — Input validation on the POST body

**File:** `src/app/api/chat/route.ts`

Read the existing validation to find the actual limits, then confirm these rules are enforced:

1. `messages` must be an array — 400 if not
2. `messages.length` must not exceed the limit in the code (confirm the actual number)
3. Each `message.content` must not exceed the character limit in the code (confirm the actual number)
4. `persona` must be one of the valid personas — default to `'recruiter'` if invalid, do not error
5. HTML is stripped from message content before it reaches the AI layer

If any of these checks are missing, add them with a comment: `// Input validation — sanitize before AI layer`

---

## Step 6 — React error boundary on chat UI

**Files:** somewhere in `src/components/chat/` or `src/components/PortfolioLab.tsx`

Verify an error boundary wraps the entire chat component tree. If one doesn't exist, create `src/components/chat/ChatErrorBoundary.tsx`:

```tsx
'use client';
import { Component, type ReactNode } from 'react';

interface State { hasError: boolean }

export class ChatErrorBoundary extends Component<{ children: ReactNode }, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError() { return { hasError: true }; }

  componentDidCatch(error: Error) {
    console.error('[Orby] UI crash:', error.message);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex flex-col items-center justify-center h-full gap-3 text-slate-400 text-sm">
          <p>Orby hit an error. Refresh to try again.</p>
          <button onClick={() => this.setState({ hasError: false })} className="text-violet-400 underline">
            Retry
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}
```

Wrap the chat UI at the highest level that makes sense — typically inside `PortfolioLab` or `AppSidebar`.

---

## Step 7 — Origin allowlist includes production domain

**File:** Wherever `isAllowedOrigin()` is defined (likely `src/app/api/chat/route.ts`)

Before deploying, the production URL must be in the allowlist. If the URL is not yet known, use an env var:

```typescript
const ALLOWED_ORIGINS = [
  'http://localhost:3000',
  process.env.NEXT_PUBLIC_SITE_URL,       // set this in Vercel env vars
].filter(Boolean) as string[];
```

Do not add wildcards or `.vercel.app` subdomains broadly.

---

## Acceptance criteria

- [ ] All AI API keys confirmed server-only (grep shows no client-side usage, no `NEXT_PUBLIC_` prefix)
- [ ] `curl` to `/api/chat` without HMAC cookie returns `401`
- [ ] Upstash downtime degrades gracefully (logs warning, allows request) — not a 500
- [ ] Fallback chain: Cerebras → Groq → Mistral → degraded — no unhandled exceptions at any step
- [ ] Input validation present and correct (array check, length limits, HTML strip)
- [ ] Chat UI wrapped in error boundary — Orby crash does not crash the portfolio page
- [ ] Origin allowlist updated to include production domain before deploy
- [ ] `pnpm build` passes
