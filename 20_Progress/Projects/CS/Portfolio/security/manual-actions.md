---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, manual, dashboard]
---

# Manual Actions — Security Pass

> Everything in this file requires you to open a dashboard, browser, or terminal — it cannot be done by Claude Code alone. Work through this alongside [[claude-code-prompts]].

→ Phase detail files: [[phase-1-auth-clerk]] · [[phase-2-sanity-lockdown]] · [[phase-3-chatbot-resilience]] · [[phase-4-deployment-hardening]] · [[phase-5-monitoring]]

---

## Phase 1 — Clerk {#phase-1}

### 1A — Verify Clerk app is using the correct environment

URL: `https://dashboard.clerk.com`

1. Open your application → **API Keys** tab
2. Confirm `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` in `.env.local` matches the **Development** key (starts with `pk_test_`)
3. Before deploying to production, switch to the **Production** instance key (starts with `pk_live_`)
4. Both `CLERK_SECRET_KEY` and `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` must be from the **same** environment — mixing test/live keys causes auth failures

### 1B — Check sign-in page appearance manually

1. Run `pnpm dev` in the portfolio repo
2. Navigate to `http://localhost:3000/sign-in` in a browser
3. Visually confirm: all form fields visible, labels readable, Google button not the only visible element
4. Also navigate to `http://localhost:3000/studio` while logged out — confirm immediate redirect to `/sign-in`
5. Sign in with your Google account — confirm `/studio` loads the Sanity Studio after sign-in

---

## Phase 2 — Sanity dashboard {#phase-2}

### 2A — Verify SANITY_API_TOKEN role

URL: `https://www.sanity.io/manage`

1. Open your project → **API** tab → **Tokens** section
2. Find the token currently set as `SANITY_API_TOKEN` in `.env.local`
3. Its **Permissions** column must show **Viewer** — not Editor, Deploy Studio, or Administrator
4. If it shows anything other than Viewer:
   - Click **Add API Token**
   - Name: `portfolio-viewer-prod`
   - Permissions: **Viewer**
   - Copy the new token
   - Update `.env.local`: `SANITY_API_TOKEN=<new-token>`
   - Also update Vercel env vars (see Phase 4 manual steps)
   - Delete the old high-permission token from Sanity dashboard

### 2B — Configure Sanity CORS

URL: `https://www.sanity.io/manage` → project → **API** → **CORS Origins**

The allowed origins list must contain exactly:
- `http://localhost:3000` — Allow credentials: **Yes**
- `https://[your-vercel-domain].vercel.app` — Allow credentials: **Yes**
- `https://[your-custom-domain]` — Allow credentials: **Yes** (only if using one)

Remove any wildcard `*` entries. Click **Save** after changes.

Note: you do not have the production URL yet if you haven't deployed. Add it after the first deployment.

### 2C — Check Sanity history after going live (ongoing)

URL: `https://www.sanity.io/manage` → project → **History** tab

After deploying, periodically check this tab for any document edits you did not make. If you see edits from unknown sessions, immediately:
1. Rotate `SANITY_API_TOKEN` with a new Viewer token
2. Rotate `SANITY_REVALIDATE_SECRET` with a new random value
3. Update both in Vercel env vars and redeploy

---

## Phase 3 — Chatbot (no dashboard actions required) {#phase-3}

All Phase 3 actions are code changes done via Claude Code prompts. See [[claude-code-prompts#phase-3]].

The only manual verification is to run the curl command from P3-C in your own terminal:
```bash
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"messages":[{"role":"user","content":"test"}]}'
```
Expected output: `401`

---

## Phase 4 — Vercel dashboard + pre-deploy {#phase-4}

### 4A — Add all environment variables to Vercel

URL: `https://vercel.com` → your project → **Settings** → **Environment Variables**

Add every variable from `.env.local` to the **Production** environment. Tick "Production" for secrets; tick "Preview" and "Development" only for non-secrets you also want in those environments.

Required variables and their correct names (verify against your actual `.env.local`):

| Variable | Environment | Notes |
|----------|-------------|-------|
| `CEREBRAS_API_KEY` (or actual primary key name) | Production only | Server-only |
| `GROQ_API_KEY` | Production only | Server-only |
| `MISTRAL_API_KEY` (or third fallback name) | Production only | Server-only |
| `CHAT_TOKEN_SECRET` | Production only | Server-only |
| `UPSTASH_REDIS_REST_URL` | Production only | Server-only |
| `UPSTASH_REDIS_REST_TOKEN` | Production only | Server-only |
| `SANITY_API_TOKEN` | Production only | Server-only — must be Viewer role |
| `SANITY_REVALIDATE_SECRET` | Production only | Server-only |
| `CLERK_SECRET_KEY` | Production only | Server-only |
| `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` | Production | Use `pk_live_*` key for production |
| `NEXT_PUBLIC_SANITY_PROJECT_ID` | All | Not a secret |
| `NEXT_PUBLIC_SANITY_DATASET` | All | Not a secret |
| `NEXT_PUBLIC_SITE_URL` | Production | `https://your-portfolio.vercel.app` |

**Important:** After adding all variables, do not deploy yet. Complete all Claude Code prompts through Phase 4 first, then push to `main`.

### 4B — Vercel project settings

URL: `https://vercel.com` → your project → **Settings** → **General**

Confirm:
- Framework Preset: **Next.js** (should auto-detect)
- Build Command: `pnpm build` (or leave blank for auto-detect)
- Install Command: `pnpm install --frozen-lockfile`
- Root Directory: empty (project root)

URL: `https://vercel.com` → your project → **Settings** → **Git**

Confirm:
- Only `main` branch triggers **Production** deployments
- Preview deployments are enabled for pull request branches only

### 4C — Enable Vercel Analytics and Speed Insights

URL: `https://vercel.com` → your project → **Analytics** tab

Toggle on:
- **Web Analytics** (free tier — tracks page views, visitor counts)
- **Speed Insights** (free tier — tracks Core Web Vitals per real visitor)

No code changes needed. These activate via the Vercel platform.

### 4D — First production deployment

After completing all Claude Code prompts (P1-A through P4-F) and all manual steps above:

```bash
git add -A
git commit -m "security: clerk fix, CSP enforcement, health endpoint, error boundary"
git push origin main
```

Watch the Vercel build logs in real time. The build must succeed (green). If it fails, read the error and fix it before pushing again.

---

## Phase 5 — Monitoring setup {#phase-5}

### 5A — Set up UptimeRobot (free)

URL: `https://uptimerobot.com`

1. Create a free account
2. **Add New Monitor**:
   - Monitor Type: **HTTP(s)**
   - Friendly Name: `Portfolio — Homepage`
   - URL: `https://your-portfolio.vercel.app`
   - Monitoring Interval: **5 minutes**
3. **Add second monitor**:
   - Monitor Type: **HTTP(s)**
   - Friendly Name: `Portfolio — Health Check`
   - URL: `https://your-portfolio.vercel.app/api/health`
   - Monitoring Interval: **5 minutes**
4. Go to **My Settings** → **Alert Contacts** → add `anantmahi721@gmail.com`
5. Assign the alert contact to both monitors

You will now receive an email within 5 minutes of downtime.

### 5B — Sanity CORS update (after deploy)

Once the production URL is known (e.g. `https://anant-portfolio.vercel.app`), return to the Sanity CORS settings ([[manual-actions#2b]]) and add the production domain if you haven't already.

### 5C — Know how to rollback a Vercel deployment

Practice this before you need it under pressure:

1. URL: `https://vercel.com` → your project → **Deployments** tab
2. Find the last deployment with a green checkmark (before any incident)
3. Click the three-dot menu → **Promote to Production**
4. Confirm — rollback takes approximately 30 seconds

That's it. You do not need to git revert or redeploy. Vercel keeps all previous builds.

### 5D — Post-deploy manual verification (browser)

After the production deployment is live:

1. Open `https://your-portfolio.vercel.app` in a fresh private/incognito browser window
2. Navigate through the full portfolio — all sections should load with real Sanity content
3. Open the sidebar → Orby should be accessible without login (public route)
4. Navigate to `https://your-portfolio.vercel.app/studio` — should redirect to Clerk sign-in
5. Sign in → Sanity Studio should load
6. Open browser DevTools → Console tab → confirm **zero errors** on page load
7. Open DevTools → Network tab → confirm no failed requests (no red rows)
8. Run `curl https://your-portfolio.vercel.app/api/health` — confirm `{"status":"ok"}`

---

## Summary — what you do vs. what Claude Code does

| Action | Who |
|--------|-----|
| Fix clerk-appearance.ts dark mode | Claude Code (P1-B) |
| Fix middleware route matchers | Claude Code (P1-C) |
| Verify Clerk token environment (test vs live) | **You** (1A) |
| Visual QA of sign-in page | **You** (1B) |
| Check SANITY_API_TOKEN is Viewer role | **You** (2A) |
| Configure Sanity CORS allowed origins | **You** (2B) |
| Patch open redirect in draft-mode | Claude Code (P2-B) |
| Scan for mutation calls in Next.js | Claude Code (P2-C) |
| Add all env vars to Vercel dashboard | **You** (4A) |
| Vercel project settings | **You** (4B) |
| Enable Vercel Analytics | **You** (4C) |
| Push to main / trigger deploy | **You** (4D) |
| Set up UptimeRobot | **You** (5A) |
| Update Sanity CORS with production URL | **You** (5B) |
| Post-deploy browser QA | **You** (5D) |
| Fix /api/health Clerk issue | Claude Code (P5-A) |
| Create /api/health and /api/error-report | Claude Code (P5-B, P5-C) |
| Configure Cloudflare DNS for anantgupta.dev | **You** (6A) |
| Add custom domain in Vercel | **You** (6B) |
| Set SSL mode to Full (strict) | **You** (6C) |
| Add WAF rules in Cloudflare | **You** (6D) |
| Configure Sanity revalidate webhook | **You** (6E) |
| Update UptimeRobot monitors to anantgupta.dev | **You** (6F) |
| Add Turnstile env vars to Vercel | **You** (6G) |
| Set up Turnstile + siteverify Worker | Claude Code (P6-A) |
| Update origin allowlist + site URL | Claude Code (P6-B) |
| Update CSP for Turnstile domains | Claude Code (P6-D) |

---

## Phase 6 — Cloudflare + Custom Domain {#phase-6}

> Context: [[cloudflare-strategy]] has the full architecture decisions. These are the manual steps you do in dashboards.

### 6A — Configure Cloudflare DNS

URL: `https://dash.cloudflare.com` → select your account → **anantgupta.dev** → **DNS** → **Records**

1. Delete any existing A/CNAME records for `@` and `www` that point elsewhere
2. First, get your Vercel CNAME target: Vercel dashboard → your project → **Settings** → **Domains** → **Add Domain** → type `anantgupta.dev` → Vercel will show you the CNAME value (e.g. `cname.vercel-dns.com`)
3. Add these DNS records in Cloudflare:

| Type | Name | Content | Proxy status |
|------|------|---------|-------------|
| CNAME | `@` (or blank) | `cname.vercel-dns.com` | **Proxied** (orange cloud ✅) |
| CNAME | `www` | `cname.vercel-dns.com` | **Proxied** (orange cloud ✅) |

4. Click **Save** for each record

> The orange cloud (Proxied) is essential — it routes traffic through Cloudflare's WAF and DDoS protection. Gray cloud (DNS only) bypasses all of that.

### 6B — Add custom domain in Vercel

URL: `https://vercel.com` → your project → **Settings** → **Domains**

1. Click **Add Domain**
2. Add `anantgupta.dev` → Vercel detects Cloudflare and guides you through verification
3. Add `www.anantgupta.dev` → set it to redirect to `anantgupta.dev` (or the other way — be consistent)
4. Wait for Vercel to show both domains as **Valid Configuration** (green checkmark)
5. This can take up to 10 minutes for DNS propagation

### 6C — Set Cloudflare SSL to Full (strict)

URL: `https://dash.cloudflare.com` → **anantgupta.dev** → **SSL/TLS** → **Overview**

1. Set encryption mode to **Full (strict)**
   - **Full** = Cloudflare encrypts to origin but doesn't verify the cert (vulnerable to MITM)
   - **Full (strict)** = Cloudflare verifies Vercel's cert is valid (Vercel auto-issues one) ✅
   - Never use **Flexible** — that sends traffic from Cloudflare to Vercel unencrypted
2. Go to **Edge Certificates** → enable **Always Use HTTPS** (on)
3. Go to **Edge Certificates** → enable **HTTP Strict Transport Security (HSTS)** with:
   - Max Age: 6 months (or 1 year if you're confident)
   - Include subdomains: on
   - Preload: on (only if you're sure you'll keep HTTPS forever)

### 6D — Add WAF rules

URL: `https://dash.cloudflare.com` → **anantgupta.dev** → **Security** → **WAF**

**Custom Rules tab → Create Rule:**

Rule 1 — Block scanner tools:
- Name: `Block known scanners`
- Expression: `(http.user_agent contains "sqlmap") or (http.user_agent contains "nikto") or (http.user_agent contains "nuclei") or (http.user_agent contains "zgrab") or (http.user_agent contains "masscan")`
- Action: **Block**
- Click **Deploy**

Rule 2 — Block empty User-Agent on API routes:
- Name: `Block empty UA on API`
- Expression: `(starts_with(http.request.uri.path, "/api/")) and (http.user_agent eq "")`
- Action: **Block**
- Click **Deploy**

**Rate Limiting Rules tab → Create Rule:**

Rule 3 — Rate limit the chatbot:
- Name: `Chat API rate limit`
- Expression: `http.request.uri.path eq "/api/chat"`
- Rate: `20` requests per `60` seconds, per IP
- Action: **Block** for 60 seconds
- Click **Deploy**

### 6E — Configure Sanity revalidate webhook

First, run Claude Code prompt **P6-C** to find the exact revalidate route path in the codebase.

URL: `https://www.sanity.io/manage` → your project → **API** → **Webhooks** → **Create webhook**

- Name: `Portfolio revalidate`
- URL: `https://anantgupta.dev/<path-from-P6-C>` (e.g. `https://anantgupta.dev/api/revalidate`)
- Dataset: your dataset (e.g. `production`)
- Trigger on: **Create**, **Update**, **Delete** (check all three)
- Filter: leave empty (triggers for all document types)
- Projection: leave empty
- HTTP method: **POST**
- HTTP Headers: add `Authorization` → `Bearer <your SANITY_REVALIDATE_SECRET value>`
- Click **Save**

To test: publish any document in Sanity Studio and check that the portfolio page updates within a few seconds.

### 6F — Update UptimeRobot monitors

URL: `https://uptimerobot.com` → your monitors

Update both monitors set up in Phase 5:
1. Change URL from `https://your-portfolio.vercel.app` → `https://anantgupta.dev`
2. Change URL from `https://your-portfolio.vercel.app/api/health` → `https://anantgupta.dev/api/health`

Also update Sanity CORS (from [[manual-actions#2b]]) to add `https://anantgupta.dev` and `https://www.anantgupta.dev` as allowed origins.

### 6G — Add Turnstile env vars to Vercel

After Claude Code runs **P6-A** (Turnstile Spin), it will output two values:
- `NEXT_PUBLIC_TURNSTILE_SITE_KEY` — the public site key (safe for browser)
- `TURNSTILE_SECRET_KEY` — the secret key for server-side verification

Add both to Vercel dashboard → **Settings** → **Environment Variables**:
- `NEXT_PUBLIC_TURNSTILE_SITE_KEY` → Production + Preview + Development
- `TURNSTILE_SECRET_KEY` → Production only (server-only secret)

Then redeploy by pushing any commit or triggering a manual redeploy in Vercel.
