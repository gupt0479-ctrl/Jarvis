---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, claude-code, prompts]
---

# Claude Code Prompts — Security Pass

> Every prompt in this file is written for Claude Code running inside the portfolio repo. Copy each block verbatim into Claude Code, run it, verify the output matches the expected result, then move to the next.
>
> Run in order. Do not skip steps — later prompts depend on earlier ones being clean.

→ Manual actions you do in dashboards: [[manual-actions]]
→ Phase detail files: [[phase-1-auth-clerk]] · [[phase-2-sanity-lockdown]] · [[phase-3-chatbot-resilience]] · [[phase-4-deployment-hardening]] · [[phase-5-monitoring]]

---

## Phase 1 — Clerk auth fix {#phase-1}

**P1-A — Find the active middleware file**
```
There are two proxy/middleware files: proxy.ts at the project root and src/proxy.ts. Check next.config.ts to find which one is loaded as middleware. Open that file and show me its current content — specifically the route matchers and which routes trigger auth().protect().
```

**P1-B — Fix clerk-appearance.ts**
```
Open src/lib/clerk-appearance.ts. The Clerk sign-in page renders pitch-black — only the Google button is visible. Fix the appearance config:
1. Set colorBackground to '#0d1117' (dark but not pure black)
2. Set colorText to '#e2e8f0' (light, readable)
3. Set colorTextSecondary to '#94a3b8'
4. Set colorInputBackground to '#161b22'
5. Set colorInputText to '#e2e8f0'
6. Set colorPrimary to '#7c3aed' (violet, matches portfolio)
7. Set borderRadius to '0.75rem'
8. Add element overrides for card (border border-white/10), formFieldInput (bg-slate-800 border-slate-700), and formFieldLabel (text-slate-300)
Keep the dark baseTheme import. Run pnpm typecheck after and fix any type errors.
```

**P1-C — Verify middleware protects only /studio**
```
Open the active middleware file (identified in P1-A). Confirm:
1. Only /studio/* routes call auth().protect()
2. /api/chat is NOT in the protected list (it has its own HMAC gate)
3. /api/health is NOT in the protected list (it needs to be public for uptime monitoring)
4. /api/error-report is NOT in the protected list

If /api/health or /api/error-report are covered by the API catch-all matcher, update the config.matcher to exclude them. Show me the final matcher config before and after.
```

**P1-D — Verify /studio layout has no auth flash**
```
Open src/app/studio/layout.tsx. Confirm the auth() call is the FIRST line of logic in the async function — before any JSX or data fetching. If it isn't, move it to be first. Show me the current order and the corrected version if needed.
```

**P1-E — Phase 1 smoke test**
```
Run: pnpm build
Then: pnpm start
Then test:
1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 — expect 200
2. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/studio — expect 302 or 307
3. curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat -H "Content-Type: application/json" -H "Origin: http://localhost:3000" -d '{"messages":[{"role":"user","content":"hi"}]}' — expect 401
Report the actual HTTP status codes for each.
```

---

## Phase 2 — Sanity backend lockdown {#phase-2}

**P2-A — Audit SANITY_API_TOKEN usage**
```
Run: grep -rn "SANITY_API_TOKEN\|getServerClient\|browserToken" src/ --include="*.ts" --include="*.tsx"
For every file found, tell me: (a) is it a server-only file, (b) does it have 'use client' at the top, (c) what does it use the token for. I need to know if the token reaches the browser anywhere and through what mechanism.
```

**P2-B — Patch the open redirect in draft-mode**
```
Find the draft-mode enable route — likely src/app/api/draft-mode/enable/route.ts or similar. Look for where it reads a "redirect" search param. Show me the current code. Then patch it so the redirect target is validated: only allow relative paths starting with "/" and not starting with "//". Reject anything else by defaulting to "/". Show the before and after.
```

**P2-C — Scan for Sanity mutation calls**
```
Run: grep -rn "\.create(\|\.patch(\|\.delete(\|\.mutate(\|\.transaction(" src/ --include="*.ts" --include="*.tsx"
For each result: tell me which file it's in, whether that file is server-only, and what it's writing to. Flag anything that's not a contact form Server Action.
```

**P2-D — Confirm correct env var name for revalidation**
```
Run: grep -rn "SANITY_REVALIDATE_SECRET\|SANITY_PREVIEW_SECRET\|SANITY_WEBHOOK_SECRET" src/ next.config.ts --include="*.ts" --include="*.tsx"
Show me every occurrence. The correct name used in this codebase should be SANITY_REVALIDATE_SECRET. If the code uses a different name, tell me the exact variable name so I can add the right one to Vercel env vars.
```

**P2-E — Verify CSP allows Sanity Live SSE**
```
Open next.config.ts and find the Content-Security-Policy or Content-Security-Policy-Report-Only header. Show me the current connect-src directive. Confirm it includes wss://*.sanity.io — this is required for Sanity's Live SSE connection. If it's missing, add it.
```

---

## Phase 3 — Chatbot resilience {#phase-3}

**P3-A — Identify all AI model env vars**
```
Open src/lib/model-router.ts (or wherever routeChat() is defined). Show me every process.env reference in that file. I need the exact variable names for the primary model, fallback models, and any API keys. Also show me the complete fallback chain — which model is tried first, second, third, and what happens when all fail.
```

**P3-B — Verify all AI keys are server-only**
```
Take the env var names found in P3-A. For each one, run:
grep -rn "<VAR_NAME>" src/ --include="*.ts" --include="*.tsx"
Confirm: (a) none appear with NEXT_PUBLIC_ prefix, (b) none appear in files with 'use client' at the top. Report any violations.
```

**P3-C — Test the HMAC gate**
```
Start pnpm dev if not already running. Run:
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"messages":[{"role":"user","content":"test"}]}'
Expected: 401. If I get anything else (200, 500, etc.), open src/app/api/chat/route.ts and show me the HMAC verification block — we need to find why it's not enforcing.
```

**P3-D — Fix Upstash 500 on Redis downtime**
```
Open src/app/api/chat/route.ts. Find where the Upstash rate-limit checks (.limit()) are called. Show me the current code. Then wrap both the burstLimit.limit() and dailyLimit.limit() calls in a try/catch. If Redis is unreachable (catch fires), log a warning with console.warn('[chat] Upstash unreachable — rate limiting skipped') and allow the request to continue. Do not return 500 to the user. Show the before and after.
```

**P3-E — Audit input validation**
```
Open src/app/api/chat/route.ts. Find the request body parsing section. Show me every validation check currently in place. I need to know: (a) what the current message array length limit is, (b) what the current per-message character limit is, (c) whether HTML is stripped from content, (d) how invalid persona values are handled. If any of these checks are missing, add them.
```

**P3-F — Add or verify error boundary on chat UI**
```
Search for an error boundary component wrapping the chat UI:
grep -rn "ErrorBoundary\|componentDidCatch" src/ --include="*.ts" --include="*.tsx"
If one exists, show me what it renders when there's an error. If none exists, create src/components/chat/ChatErrorBoundary.tsx as a class component error boundary with a Retry button, then wrap the chat component tree with it inside PortfolioLab or AppSidebar (whichever is the top-level chat container). Show me where you wrapped it.
```

**P3-G — Update origin allowlist**
```
Find the isAllowedOrigin function — likely in src/app/api/chat/route.ts. Show me the current ALLOWED_ORIGINS array. I need to add the production domain before deploying. Update it to read from a NEXT_PUBLIC_SITE_URL env var as a fallback if the production URL isn't hardcoded yet:
const ALLOWED_ORIGINS = ['http://localhost:3000', process.env.NEXT_PUBLIC_SITE_URL].filter(Boolean);
Add NEXT_PUBLIC_SITE_URL to .env.local with the value http://localhost:3000 for now.
```

---

## Phase 4 — Deployment hardening {#phase-4}

**P4-A — Flip CSP from report-only to enforced**
```
Open next.config.ts. Find the security headers section. Show me the current Content-Security-Policy header key. If it's 'Content-Security-Policy-Report-Only', change it to 'Content-Security-Policy'. Before saving, run pnpm dev and open the browser console — report any CSP violation messages so we can fix them before enforcement goes live. Only switch to enforcement after the console is clean.
```

**P4-B — Full env var audit**
```
Run: grep -rn "process\.env\." src/ next.config.ts --include="*.ts" --include="*.tsx" | grep -oP "process\.env\.\K\w+" | sort -u
Show me the complete list. For each variable: (a) is it present in .env.local, (b) does it have NEXT_PUBLIC_ prefix, (c) is that prefix correct for a variable of that type (secret vs public config). Flag any mismatches.
```

**P4-C — Security headers verification**
```
Run: pnpm build && pnpm start
Then: curl -I http://localhost:3000
Show me the full response headers. Confirm these are present: X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Strict-Transport-Security, Content-Security-Policy (enforced, not report-only). If any are missing, show me the current headers() config in next.config.ts so we can add them.
```

**P4-D — Secrets scan**
```
Run these checks:
1. cat .gitignore | grep -E "\.env|secret|key" — confirm .env.local is ignored
2. git log --all --full-history -- .env.local — confirm it was never committed
3. grep -rn "console\.log.*process\.env\|console\.log.*KEY\|console\.log.*SECRET\|console\.log.*TOKEN" src/ --include="*.ts" --include="*.tsx" — find any env var logging

Report results for all three. If any console.log leaks are found, remove them.
```

**P4-E — Dependency audit**
```
Run: pnpm audit --prod
Show me any HIGH or CRITICAL vulnerabilities. For each one: the package name, the CVE, whether it's in a code path this app actually uses, and whether a patched version is available. Then run pnpm update for any packages with available fixes and confirm pnpm build still passes.
```

**P4-F — Complete build pipeline**
```
Run these in order and show me the output of any that fail:
1. pnpm typegen
2. pnpm typecheck
3. pnpm lint
4. pnpm test
5. pnpm build
All five must pass with zero errors. Fix every error before continuing.
```

**P4-G — Local production smoke tests**
```
Run pnpm start (production build). Then run these five curl checks and report the HTTP status code for each:
1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000
2. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/studio
3. curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat -H "Content-Type: application/json" -H "Origin: http://localhost:3000" -d '{"messages":[{"role":"user","content":"hi"}]}'
4. curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat -H "Origin: https://evil.com" -d '{}'
5. curl -s http://localhost:3000/api/health
Expected: 200, 302, 401, 403, {"status":"ok",...}
```

---

## Phase 5 — Monitoring {#phase-5}

**P5-A — Fix /api/health Clerk protection**
```
The /api/health route currently returns 401 because Clerk middleware covers the /api/* matcher. Fix the middleware config (in the file identified in P1-A) so /api/health is excluded from Clerk. Then run: curl -s http://localhost:3000/api/health
Expected: {"status":"ok",...} not 401.
```

**P5-B — Create /api/health endpoint**
```
Check if src/app/api/health/route.ts exists. If not, create it. The endpoint must:
1. Return 200 with {"status":"ok","checks":{...},"ts":"..."} when all env vars are present
2. Return 503 with {"status":"degraded",...} if any are missing
3. Check these env vars by presence only (Boolean(process.env.X)) — never log values
4. Include export const dynamic = 'force-dynamic' to prevent caching
5. Not require any authentication

The checks object should include: server (always true), ai_primary (primary model key), ai_fallback (GROQ_API_KEY), chat_secret (CHAT_TOKEN_SECRET), upstash (UPSTASH_REDIS_REST_URL), sanity_token (SANITY_API_TOKEN). Use the actual env var names from P3-A for ai_primary.
```

**P5-C — Create /api/error-report endpoint**
```
Create src/app/api/error-report/route.ts. It should accept POST requests with a JSON body containing error, stack, and component fields. Log them with console.error('[client-error]', ...) — this writes to Vercel Function logs. Return 204 No Content. Exempt this route from Clerk middleware the same way as /api/health. Also update the ChatErrorBoundary from P3-F to call this endpoint in componentDidCatch when NODE_ENV is production.
```

**P5-D — Post-deploy production smoke tests**
```
[Run AFTER Vercel deployment — replace DOMAIN with actual production URL]
Run these and report each HTTP status code:
1. curl -s -o /dev/null -w "%{http_code}" https://DOMAIN
2. curl -I https://DOMAIN | grep -iE "x-frame-options|strict-transport|content-security-policy"
3. curl -s -o /dev/null -w "%{http_code}" https://DOMAIN/studio
4. curl -s -o /dev/null -w "%{http_code}" -X POST https://DOMAIN/api/chat -H "Content-Type: application/json" -H "Origin: https://DOMAIN" -d '{"messages":[{"role":"user","content":"hi"}]}'
5. curl -s -o /dev/null -w "%{http_code}" -X POST https://DOMAIN/api/chat -H "Origin: https://evil.com" -d '{}'
6. curl -s https://DOMAIN/api/health
Expected: 200, (headers present), 302, 401, 403, {"status":"ok"}
```
