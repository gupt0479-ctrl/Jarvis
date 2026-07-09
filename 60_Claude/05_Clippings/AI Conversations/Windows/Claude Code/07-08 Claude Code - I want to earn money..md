---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "I want to earn money."
started_at: 2026-07-08T12:44:10
ended_at: 2026-07-08T12:53:36
project: Jarvis
status: raw
session_id: e86b1e5f-f812-449f-9d77-48fadf28bd52
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
tags:
  - input
  - ai-conversation
  - claude-code
---

# I want to earn money.

## You

I want to earn money. There are ways to add extensions/plugins to vs code or claude directly to display ads. We earn money just from seeing these ads. I have found two websites regarding this easy money: "https://www.claudecodeads.com/", "https://kickbacks.ai/". If needed use firecrawl to analyze various other websites. Here is what you have to do now: I want to make the most amount of money through this ads thing. Find the best, most trusted and most profitable(for me) ads displayer out there that brings me the most revenue.

## Claude

I'll look at both sites to see what's actually being offered before making any recommendation.

I'll pull the content of both sites first to see what they actually claim to offer.

Both sites are the same category: a VS Code extension that hijacks Claude Code's "thinking" spinner/status line to show sponsored text, and splits ad revenue with whoever installed it. Let me check trust signals — install counts, reviews, and any scam reports — before recommending one.

Here's what I found after checking both sites, the actual VS Code Marketplace listing, GitHub, and independent user reports.

## What these actually are

Both `claudecodeads.com` (extension: **AdSpin**) and `kickbacks.ai` are the same product category: a VS Code extension that patches Claude Code's `statusLine`/`spinnerVerbs` settings so the "thinking…" text you see while Claude works gets replaced with a paid sponsored line. Advertisers bid per 1,000 impressions; you get a cut.

| | AdSpin (claudecodeads.com) | Kickbacks.ai |
|---|---|---|
| Your cut | 75% | 50% |
| Payout | PayPal, weekly, $10 min | Stripe Connect only, monthly, $10 min — restricted to Stripe-supported countries |
| Transparency | Proprietary, "source-available" | Open source on GitHub, detailed FAQ covering telemetry/fraud rules |
| Real install count | **397 installs, 2 reviews** on the actual VS Code Marketplace listing | Listed separately on Marketplace, no Open VSX support yet |
| Marketing claim | Landing page claims **"44,530+ developers"** | No inflated install claim found |
| Data collection | Claims no code/prompt access, unverified (closed source) | Documented: no code/prompts by default; optional opt-in tier shares an "abstracted interest signal" from your session for higher pay |
| Company | "XYZ AI Inc.", brand-new, v0.1.6 | Individual dev (github.com/andrewmccalip), more mature docs |
| Platform support | VS Code + Open VSX (Cursor/VSCodium) | Windows/Linux good; macOS explicitly unsupported (keychain issues) |

**Red flag on AdSpin:** the landing page's "44,530+ developers" figure doesn't match the Marketplace's actual 397 installs — a 100x discrepancy. That's the kind of number I'd treat as fabricated marketing copy, not a data point.

**Real user sentiment on Kickbacks** (Reddit, r/ClaudeAI): someone running Claude Max 20x + Codex 20x heavy usage called it "a rip-off... they're clipping the ticket hard" — i.e., even heavy personal use produces underwhelming earnings.

## The math that actually matters

Bids start at $1.00 per 1,000 impressions. At 50–75% revenue share, that's **$0.0005–0.00075 per impression** — and an impression only counts if the spinner is visible ≥5 seconds during your own active coding. Even a very heavy personal user (hundreds of Claude Code turns a day) is looking at maybe **$1–5/month**, and that's assuming advertiser demand is actually filling the queue (AdSpin's own live campaign builder showed "no bids yet" when I checked).

This only becomes real money if you have many users running it — i.e., you're distributing the extension to an audience, not using it yourself. For a single developer, neither of these is an income stream; they're a rounding error, in exchange for letting a young, third-party company inject sponsored content into your dev tool and control your Claude Code settings/status line.

## My take

If you're going to try one anyway, **Kickbacks is the more trustworthy of the two** — open source, genuinely documented fraud/privacy rules, no inflated numbers — but it pays less and independent user reports already call the earnings disappointing. AdSpin pays a higher nominal share but has a verifiable inflated marketing claim and a near-zero real install base, which I'd weigh heavily against it.

Given the actual economics, I wouldn't recommend installing either for personal revenue — the money isn't there for individual use, and you'd be handing a brand-new company control over your coding assistant's settings file for a few dollars a month at best. If your real goal is to earn money from this trend, the leverage is in *building* one of these products or distributing it to an audience, not installing it yourself.

*Tools used: ToolSearch, mcp__firecrawl__firecrawl_scrape, mcp__firecrawl__firecrawl_search*

## You

How fast would I make $10 from this when i am on the pro plan (abuse the weekly limit almost every week)? Is this worth installing?

## Claude

Let me work through the actual numbers rather than guess.

**Assumptions (labeled explicitly):**
- Claude Pro's published weekly Claude Code allowance is roughly **40–80 hours** of active Sonnet usage before you hit the weekly cap (Anthropic's own published range for that tier). "Abusing the limit almost every week" puts you at the top of that band — call it ~60–80 hrs/week of Claude Code actually running.
- Of that wall-clock time, only the portion where the **spinner is visible** counts as an ad impression — not tool execution, not streamed output. For a typical mixed coding workflow (edits, bash calls, file reads interleaved with reasoning), that's realistically **15–25%** of total active time. Call it ~10–20 hrs/week of genuine spinner time.
- Payout math from what I read on both sites:
  - **Kickbacks**: 50% share, impression = 5-second view-tick, floor bid $1/1,000 impressions → $0.0005 credited per tick.
  - **AdSpin**: 75% share, impression = 10-second view, floor bid $1/1,000 → $0.00075 credited per view.

**Optimistic ceiling (assumes every single tick has a paying ad ready to serve — 100% fill rate):**

| | Spinner-seconds/week | Impressions/week | $/week | Weeks to $10 |
|---|---|---|---|---|
| Kickbacks | 36,000–72,000s | 7,200–14,400 | $3.60–$7.20 | ~1.5–3 |
| AdSpin | 36,000–72,000s | 3,600–7,200 | $2.70–$5.40 | ~2–3.5 |

**Why the real number is worse than this:**
1. **Fill rate isn't 100%.** When I loaded AdSpin's live campaign builder it showed "no bids yet" — meaning at that moment there was no advertiser to serve you at all. A thin, brand-new ad marketplace means long stretches where the spinner just shows the stock "thinking…" text (or a sign-in nag) and pays nothing.
2. **Both networks explicitly throttle heavy users.** Kickbacks' FAQ states it enforces "per-user spacing rules and hourly/daily caps" specifically so a single account can't harvest disproportionate earnings — i.e., the "abuse the weekly limit" strategy is the exact pattern their fraud system is built to cap.
3. **Real-world report from a heavier user than you'd be:** the Reddit user running Claude Max 20x *and* Codex 20x simultaneously (meaningfully more volume than Pro-at-cap) called Kickbacks "a rip-off... they're clipping the ticket hard" — implying their actual weekly take was well under the optimistic math above.

Realistic estimate: **4–8+ weeks** to hit the $10 threshold at heavy Pro-tier usage, not 1.5–3.

**Is it worth installing?**

No, I wouldn't. Even in the optimistic case you're talking about $10 every few weeks — genuinely a few dollars a month — in exchange for:
- Letting a brand-new, unaudited company (AdSpin: 397 real installs behind a "44,530+" marketing claim I couldn't verify; Kickbacks: a solo dev's project) **patch your Claude Code extension or settings.json**.
- Kickbacks' optional higher-pay tier explicitly trades on an "abstracted interest signal" derived from your coding sessions — that's the one lever that could meaningfully increase your rate, and it's also the one that starts profiling what you work on.
- Ongoing maintenance risk: both note they can break when Claude Code updates, requiring reinstall/reconfig to keep working.

The money doesn't justify the trust you'd be extending. This is a novelty at best, not something worth optimizing your workflow around.


