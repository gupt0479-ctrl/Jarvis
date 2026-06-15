---
type: project
status: sprout
created: 2026-06-15
tags: [portfolio, security, clerk, auth]
---

# Phase 1 — Authentication & Clerk Fix

> **Scope:** Clerk guards `/studio` only. Orby/chat is public — no Clerk needed there. The only problem is the dark-mode rendering of the sign-in page.

→ All prompts for this phase: [[claude-code-prompts#phase-1]]
→ Manual steps: [[manual-actions#phase-1]]

---

## What is actually broken

The Clerk sign-in page (`/sign-in`) renders pitch black. All UI elements are invisible except the Google OAuth button because `src/lib/clerk-appearance.ts` overrides the background to near-black without setting readable foreground colors. This is the only auth bug. The sidebar and Orby chat are public routes — they do not use Clerk.

**What was wrong in the old notes:** The old notes said to put a Clerk `<SignIn />` modal inside the sidebar for Orby. That was incorrect. The chat endpoint uses HMAC + rate limiting, not Clerk. Only `/studio` needs Clerk. Do not add Clerk to the sidebar.

---

## Step 1 — Fix `src/lib/clerk-appearance.ts`

**File:** `src/lib/clerk-appearance.ts`

The `colorBackground` override is too dark, and foreground colors are not set to compensate. Fix:

```typescript
import { dark } from '@clerk/themes';

export const clerkAppearance = {
  baseTheme: dark,
  variables: {
    colorBackground: '#0d1117',       // dark but not black
    colorText: '#e2e8f0',             // light readable text
    colorTextSecondary: '#94a3b8',    // muted secondary text
    colorInputBackground: '#161b22',  // input fields visible
    colorInputText: '#e2e8f0',
    colorPrimary: '#7c3aed',          // violet — matches portfolio
    borderRadius: '0.75rem',
  },
  elements: {
    card: 'shadow-2xl border border-white/10 backdrop-blur-sm',
    socialButtonsBlockButton: 'border border-white/20 hover:border-white/40',
    formButtonPrimary: 'bg-violet-600 hover:bg-violet-700',
    formFieldInput: 'bg-slate-800 border-slate-700 text-slate-100',
    formFieldLabel: 'text-slate-300',
  },
};
```

**Verify:** Navigate to `http://localhost:3000/sign-in` in dev. All form inputs, labels, and both the email/password form and Google button must be visible.

---

## Step 2 — Confirm middleware is correct

**File:** `middleware.ts` at project root (or `src/middleware.ts` — check which `next.config.ts` loads)

The middleware must protect `/studio/*` and leave everything else — including `/api/chat`, `/api/chat-token`, and all portfolio routes — fully public.

```typescript
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isStudioRoute = createRouteMatcher(['/studio(.*)']);

export default clerkMiddleware((auth, req) => {
  if (isStudioRoute(req)) auth().protect();
});

export const config = {
  matcher: ['/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)', '/(api|trpc)(.*)'],
};
```

**Critical:** `/api/chat` must NOT appear in the protected list. It has its own HMAC gate. If Clerk middleware runs on `/api/chat`, it will interfere.

---

## Step 3 — Confirm `/studio` layout guard has no content flash

**File:** `src/app/studio/layout.tsx`

The layout must call `auth()` server-side and redirect before any studio content renders. A common mistake is running the check after the component begins rendering, which causes a brief flash of studio UI.

```typescript
import { auth } from '@clerk/nextjs/server';
import { redirect } from 'next/navigation';

export default async function StudioLayout({ children }: { children: React.ReactNode }) {
  const { userId } = await auth();
  if (!userId) redirect('/sign-in');
  return <>{children}</>;
}
```

The `await auth()` call must be the first line of logic — before any JSX, before any data fetching.

---

## Acceptance criteria

- [ ] `/sign-in` page: all text readable, inputs visible, Google button not the only visible element
- [ ] `/studio` while logged out: redirects immediately to `/sign-in` — no flash of studio content
- [ ] `/studio` while logged in: renders Sanity Studio correctly
- [ ] `http://localhost:3000/` loads with zero auth prompts
- [ ] `POST /api/chat` is not blocked by Clerk middleware (verify via curl — expect 401 from HMAC, not a Clerk redirect)
- [ ] `pnpm build` passes with no type errors
