---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/07 Bots-Hub]]"
  - "[[Per Header/01 Dashboard]]"
tags:
  - trading
  - frontend
  - ui
  - settings
track:
  - trading
  - ui
next: "This closes the loop — Per Header/01 Dashboard.md is where the desk begins again"
---
# Settings
==The one page that was never designed in conversation and had to be imagined whole — the desk's own vital signs, kept honest and small, for a product with exactly one person ever meant to open it.==
## A note on how this note came to exist
Every other page in this set traces back to something Anant actually said during planning. Settings doesn't — it was named as a nav slot and never once discussed. Rather than leave it thin, this note commits to a real, coherent vision for it, built from first principles that already govern the rest of the desk: single user, no auth theater, radical honesty about system health, nothing here that isn't either true right now or clearly marked as not yet built. If any of this reads wrong once Settings actually gets discussed properly, it's the easiest page on the desk to revise — nothing else depends on it the way Dashboard's next-steps or My Stocks' pending banner depend on data flowing correctly from elsewhere.
## The first look
Settings reads less like a page and more like a short, calm inspection — five sections stacked vertically, each one a graphite card, no tabs, no sidebar, nothing to navigate because there's nothing here worth hiding behind a click. It's the quietest page on the entire desk, deliberately, because a settings page that tries to be interesting is usually a settings page hiding something it shouldn't.
## The five sections
**Account** states, plainly, that this desk has exactly one identity — `anant`, the only human the brain's own approval logic will ever recognize — and says so without apology: "This is locked for V1. Multi-user auth deferred." No login form, no password field, nothing performing security theater for an audience of one.
**UI Preferences** holds the only genuinely interactive controls on the page: a dark-mode toggle (on by default, because a desk built around royal blue on void black was never really meant to be seen any other way, but the toggle exists for daylight use), three refresh-interval choices matching the three speeds already established across the desk — live panels, AI-generated content, and static/manual-only content — and two small sidebar-behavior preferences, default collapsed-or-expanded state and whether the desk remembers your last choice between sessions.
**API & Secrets** is the page's most consequential section in practice, even though it's visually no louder than any other: a status line per provider — Polygon, Tiingo, FMP, and the LLM keys (Gemini primary, Groq fallback) — each with a clear valid/invalid badge and a last-checked timestamp, a secrets-redaction status confirming nothing sensitive is leaking into logs, and a single honest warning permanently visible near the bottom: key validity is checked on page load, and an invalid key doesn't halt the desk with a loud error — it fails quietly, and shows up as a red mark in Bots-Hub's ingestion log instead. Telling the user this plainly, rather than letting them discover it the hard way, is the entire point of this section existing.
**System Health** reports the desk's own physical facts without embellishment: database connected, its size, how much price history it holds; backend responsive, with real latency in milliseconds; which LLM provider is currently primary and which is standing by; free disk space. A "Run diagnostics" button kicks off a real check rather than a canned animation, results cached for an hour so repeated visits don't re-trigger work needlessly. When something's actually wrong — low disk, a slow backend, an offline LLM provider — the relevant warning surfaces at the very top of this section, not buried at the bottom where a real problem could go unnoticed.
**About** closes the page with the desk's own self-description, stated the way Anant would want anyone who ever saw this screen to understand it immediately: version, a one-line description, who built it, a link to the repository and docs, and two disclaimers that exist specifically to keep this project honest about its own scope — "Not affiliated with TradingView.com" and "Not financial advice; for research and learning only." These two lines are not legal boilerplate copied out of habit; they're the same non-negotiable boundary the whole desk is built around, restated once, plainly, where anyone landing here for the first time will actually see it.
## Color, motion, and the royal-blue instrumentation, specifically here
Settings is the calmest page on the desk by design — no pulsing, no glow, nothing running. The only color beyond graphite-and-silver is status badges (the same green/amber/red language used everywhere else) and the dark-mode toggle itself, which gets a small satisfying royal-blue fill when active, the one moment of tactile feedback this page allows itself.
## How it behaves
Nothing here auto-refreshes. The page loads once, checks are cached, and every check — API keys, diagnostics — happens only when explicitly asked for, because a settings page that silently re-validates itself in the background is a settings page quietly doing work nobody asked it to do. Dark mode is the one instant exception: toggling it changes the whole desk's theme immediately, no save button, no page reload, because a preference that requires a save-and-reload round trip stops feeling like a preference and starts feeling like a form.
## What it's built on
API key status reads the same validation the backend already performs on startup and periodically thereafter. System health numbers are real — actual DuckDB file size, actual backend response latency — not decorative placeholders. The prototype phase is honest about which of these have real teeth yet (API status, most system health numbers) versus which are UI-only for now (saved preferences, in the prototype, live in the browser rather than a real backend record).
## When things aren't perfect
An API key that's actually invalid: the badge turns red, and the message names the real problem plainly — "Polygon API key not authorized. Check .env file" — never a vague "something went wrong." Disk space genuinely low: a warning appears with an actual next step attached, "Only 5 GB free. Archiving old data recommended," not just a number and a shrug. An LLM provider down: the desk says so and names its fallback explicitly — "Gemini offline. Using Groq fallback" — so a degraded state never masquerades as a healthy one.
## What's deferred to production
Saved preferences actually persisting to a backend record rather than browser storage. Any real "danger zone" actions (resetting the local database, clearing cached fixtures) that a single-user desktop tool would eventually want, once there's something real to reset.
## Open threads for the build phase
This entire page is the open thread — it deserves its own short planning pass with Anant once the other seven pages are settled, specifically to confirm whether this imagined version actually matches what he wants a settings page on his own desk to feel like, or whether it needs trimming, expanding, or reshaping entirely. Treat everything above as a strong, coherent first draft, not a locked decision the way the other seven pages are.
