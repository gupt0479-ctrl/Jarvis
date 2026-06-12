---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - claude-setup
  - frontend
  - security
notes:
  - "[[00 - Frontend Build Kit — Index]]"
---
# Commands, Hooks & CSP Fix
Reuse the chatbot kit's command/hook setup; the only mandatory new work is the **CSP header**, the open item flagged from the last build ("CSP header in `next.config.ts`" — never shipped).

## Commands (reuse, add nothing required)
- `/sanity-push` — push the schema + content from [[09 - Sanity Content Spec]].
- `/typecheck` — gate every phase.
- `/performance` — run after the motion phase; the page is heavy (three.js + many floaters). Watch frame budget.
- `/deploy` — final.

## Hooks
- Keep **Biome-on-edit** (format/lint on save).
- Keep the **typecheck Stop hook**.
- No promptfoo here (that's the chatbot's eval concern, not the visual rebuild).

## The CSP header — the flagged open item
Add a Content-Security-Policy (and companion security headers) in `next.config.ts` via the `headers()` async function. The risk with a portfolio like this is that a too-strict CSP silently breaks three.js, the Sanity image CDN, or the AI agent's API calls — so build it, then verify each subsystem still loads.

### Starting policy (tune domains to the real stack)
```ts
// next.config.ts
const csp = [
  "default-src 'self'",
  // Next.js injects inline/eval in dev; keep 'unsafe-eval' out of prod if possible.
  "script-src 'self' 'unsafe-inline'" + (process.env.NODE_ENV !== "production" ? " 'unsafe-eval'" : ""),
  "style-src 'self' 'unsafe-inline'",                 // Tailwind/styled inline styles
  "img-src 'self' data: blob: https://cdn.sanity.io", // Sanity image CDN
  "font-src 'self' data:",
  "connect-src 'self' https://*.sanity.io https://*.api.sanity.io", // + AI agent endpoints (Gemini/Groq/Upstash) used by Orby
  "frame-ancestors 'none'",
  "base-uri 'self'",
  "form-action 'self'",
  "object-src 'none'",
  "upgrade-insecure-requests",
].join("; ");

async function headers() {
  return [{
    source: "/:path*",
    headers: [
      { key: "Content-Security-Policy", value: csp },
      { key: "X-Frame-Options", value: "DENY" },
      { key: "X-Content-Type-Options", value: "nosniff" },
      { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
      { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
      { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
    ],
  }];
}
```
### Must-verify after adding it
- Background sphere and all three.js render (script/worker/blob not blocked).
- Sanity images load (`cdn.sanity.io` in `img-src`).
- Orby's `/api/chat` and any model/Upstash calls succeed (`connect-src` includes them).
- No CSP violations in the browser console on every section.
- Prefer dropping `'unsafe-eval'` in production; if three.js or a dep needs it, document why. Consider a nonce-based `script-src` if `'unsafe-inline'` proves removable.

Run `security-reviewer` + (chatbot kit's) `/security-review` after, and confirm headers on the deployed `.dev` URL.
