---
type: project
status: sprout
created: 2026-06-09
tags:
  - project
  - security
  - portfolio
notes:
  - "[[00 - AI Setup — Index & Integration Guide]]"
  - "[[01 - Config Pack (copy-paste ready)]]"
---

# Deploy Security Checklist — .dev on Vercel

A `.dev` TLD sits on the browser **HSTS preload list**: every `.dev` site is forced to HTTPS before the first request even leaves the browser. So TLS isn't optional and you should emit a matching HSTS header. Vercel terminates TLS and gives you HTTPS automatically, but it does **not** add app-level headers (HSTS, CSP, X-Frame-Options) — those are yours to set, and `next.config.ts` is the right place because the config travels with the code.

## 1. Security headers — `next.config.ts`

```ts
const securityHeaders = [
  { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "X-Frame-Options", value: "DENY" },
  { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
];

const nextConfig = {
  async headers() {
    return [{ source: "/:path*", headers: securityHeaders }];
  },
};
export default nextConfig;
```

`includeSubDomains` + `preload` are only safe once **every** subdomain serves HTTPS — true on Vercel. After it's live, submit the apex domain at hstspreload.org.

## 2. Content-Security-Policy (do this deliberately)

CSP is the one header that breaks things if rushed, because Three.js, Sanity, and Clerk each need allowances. Start in **report-only** mode, watch violations, then enforce. Rough starting allowlist:

- `script-src 'self' 'unsafe-inline'` plus Clerk's domains (`*.clerk.accounts.dev`, `clerk.<your-domain>`).
- `connect-src 'self'` plus Sanity (`*.api.sanity.io`, `*.apicdn.sanity.io`) and Clerk.
- `img-src 'self' data: blob:` plus Sanity CDN (`cdn.sanity.io`).
- `worker-src 'self' blob:` (Three.js / WebGL workers).
- `frame-src` for Clerk components if you use hosted flows.

Ask Claude (with Context7 + the Vercel MCP `search_vercel_documentation`) to generate the exact CSP for your installed Clerk/Sanity SDK versions, then run it report-only for a day.

## 3. Clerk auth

- Secret key (`CLERK_SECRET_KEY`) is server-only — never `NEXT_PUBLIC_`.
- Protect routes in `middleware.ts` with `clerkMiddleware` + `createRouteMatcher`; don't gate on client state for authorization.
- Re-check auth inside every Server Action and Route Handler — middleware is not a substitute.
- Use Clerk's webhook signing secret to verify webhook payloads.

## 4. Sanity

- Ship only a **read** token to the client; keep write tokens server-side.
- Verify webhook signatures (`@sanity/webhook`) on revalidation endpoints.
- Guard draft/preview mode with a secret token, not a guessable query param.
- Lock CORS origins to your real domains in the Sanity project settings.

## 5. Secrets & env

- `.env.local` is gitignored; set real values as Vercel Environment Variables, scoped per environment (Production/Preview/Development).
- Only truly public values get `NEXT_PUBLIC_`. Audit the client bundle: `grep -r NEXT_PUBLIC_ .`
- Preview deployments are public URLs — don't point them at production data/secrets.

## 6. Supply chain & gates

- `pnpm audit` in CI; keep `pnpm-lock.yaml` committed.
- Biome + Vitest must pass before deploy (the hooks in the config pack enforce this locally).
- Dependabot/Renovate on the repo for dependency bumps.

## 7. Pre-deploy ritual

1. `security-reviewer` subagent over the diff.
2. Built-in `/security-review` command (ships with Claude Code).
3. Verify headers on the live URL: `curl -sI https://<your-domain>.dev | grep -i -E "strict-transport|content-type-options|frame-options"`.
4. Confirm no secrets in the client bundle.
