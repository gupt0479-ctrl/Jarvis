# Anant Gupta Portfolio

Dark cosmic command-center portfolio built with Next.js, React, Tailwind CSS v4, Sanity, Clerk, Three.js, and a deterministic Portfolio Lab sidebar.

## Stack

- Next.js 16.1.1 App Router
- React 19.2.3
- TypeScript
- Tailwind CSS v4
- shadcn/ui + Radix UI
- Three.js / React Three Fiber
- Sanity v4 with `next-sanity` live content
- Clerk auth for protected routes and Studio access
- Vitest + Testing Library
- Biome for linting and formatting

## Setup

Install dependencies:

```bash
pnpm install
```

Create `.env.local` with the required public Sanity values and private tokens:

```bash
NEXT_PUBLIC_SANITY_PROJECT_ID=...
NEXT_PUBLIC_SANITY_DATASET=...
NEXT_PUBLIC_SANITY_API_VERSION=...
SANITY_API_TOKEN=...

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=...
CLERK_SECRET_KEY=...
```

Do not commit `.env.local`, `.mcp.json`, or local MCP tokens.

### Chat and edge protection

The application currently uses Cloudflare Turnstile directly from the Next.js server route:

1. `ChatTokenInit` loads the public Turnstile widget.
2. `/api/chat-token` verifies the response with Cloudflare Siteverify.
3. The server issues the short-lived HttpOnly `chat_token` cookie.
4. `/api/chat` and `/api/orby-comment` validate the cookie and apply Upstash rate limits.

Required server-only variables are `TURNSTILE_SECRET_KEY`, `CHAT_TOKEN_SECRET`,
`UPSTASH_REDIS_REST_URL`, and `UPSTASH_REDIS_REST_TOKEN`. Provider keys used by
the model router must also be configured in the deployment environment. The
public variable `NEXT_PUBLIC_TURNSTILE_SITE_KEY` must match the Turnstile widget.
Set server-only values as encrypted Vercel variables; never print or commit them.

The Cloudflare Worker named `turnstile-siteverify-portfolio` is retained in the
Cloudflare account but is not in the current runtime path. Do not point the app
at it without first hardening its origin policy, defining an explicit route or
custom domain, and updating this application and deployment configuration
atomically. Cloudflare proxies `anantgupta.dev` and `www.anantgupta.dev` to the
Vercel origin; Vercel Preview URLs remain direct preview environments.

In local development, a missing Turnstile secret is permitted so the UI can be
worked on without external verification. Preview and production fail closed if
`TURNSTILE_SECRET_KEY` is missing.

## Development

```bash
pnpm dev
```

The app runs at `http://localhost:3000`.

In development, `sanityFetch` prefers local NDJSON content from `Data/` unless `PORTFOLIO_CONTENT_SOURCE=sanity` is set. This keeps most UI work unblocked when Sanity is unavailable.

## Content

Primary content lives in Sanity schemas under `src/sanity/schemaTypes/`.

Local fallback content lives in `Data/*.ndjson` and is normalized by `src/lib/localContent.ts`.

After schema changes:

```bash
pnpm typegen
pnpm typecheck
```

Never edit `src/sanity/types/index.ts` by hand.

## Verification

```bash
pnpm test
pnpm typecheck
pnpm build
```

`pnpm lint` runs Biome. If Sanity CLI cannot write to `~/.config/sanity` during `pnpm build` in a sandbox, rerun the build with permission outside the sandbox.

## Deployment

The site deploys to Vercel. Push to the main branch to trigger a production build. Ensure all required environment variables are configured in the Vercel project settings.

Required environment variables for production:
- `NEXT_PUBLIC_SANITY_PROJECT_ID`
- `NEXT_PUBLIC_SANITY_DATASET` (`develop` for the current content)
- `NEXT_PUBLIC_SANITY_API_VERSION`
- `SANITY_API_TOKEN`
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
- `CLERK_SECRET_KEY`
- `NEXT_PUBLIC_SITE_URL`
- `NEXT_PUBLIC_TURNSTILE_SITE_KEY`
- `TURNSTILE_SECRET_KEY`
- `CHAT_TOKEN_SECRET`
- `UPSTASH_REDIS_REST_URL`
- `UPSTASH_REDIS_REST_TOKEN`
- The configured provider API keys used by `src/lib/model-router.ts`
- `CLERK_SECRET_KEY`
