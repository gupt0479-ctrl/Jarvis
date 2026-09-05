---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, portfolio-lab, chat]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 07 — Portfolio Lab (Chat Input & Mobile Layout)

> **Status:** partial (textarea + 3-line cap built; vertical centering open; mobile repro open; break-words already done)
> **Ledger:** [[UI Fixes]] §6 | **Tasks:** 6.3, 7.1, 7.2
> **2026-09-05 correction pass:** re-verified against `ChatInputBar.tsx`, `ChatThread.tsx`, `src/components/ui/sidebar.tsx` on `post-frontend`. One claim was stale — see Task 7.2 below, it's already shipped. Everything else in the old note checked out.

## Purpose

Portfolio Lab input must feel polished: **vertically centered** short text, growable to 3 lines, mobile-safe send button layout, wrapped chat bubbles (already true — see below).

## Current code (re-verified 2026-09-05)

### `src/components/lab/ChatInputBar.tsx` (128 lines)

| Feature | Status |
|---|---|
| `<textarea>` not `<input>`, `rows={1}` | Confirmed |
| `MAX_LEN = 1000`, `MAX_LINES = 3` | Confirmed (lines 13–14) |
| Auto-grow via `scrollHeight`, capped at `lineHeight * MAX_LINES` | Confirmed (`resize`, lines 27–34) |
| Enter submit, Shift+Enter newline | Confirmed (`handleKeyDown`, lines 49–54) |
| Character counter, shows past 80% of `MAX_LEN` | Confirmed (`showCounter`, line 25) |
| `aria-label="Message to Orby"` | Confirmed (line 95) |
| Send button `shrink-0 h-7 w-7`, `aria-label="Send message"` | Confirmed (lines 110–124) |

**Bug — vertical alignment, confirmed real, exact location (lines 80–85):**
```tsx
<div
  className={cn(
    "cosmic-card flex items-end gap-2 px-3 py-2",
    "border-violet-500/20",
  )}
>
  <div className="flex flex-1 flex-col gap-1">
    <textarea ... />
```
`items-end` on the outer flex row pins the whole `flex-col` (textarea + counter span) to the bottom of the card. There is no line-count-based conditional today — it's a single static class. When the counter renders, it's inside the same column, so it also gets pulled down with the text.

### `src/components/lab/ChatThread.tsx` (211 lines)

**Task 7.2 is already done — do not re-implement.** Line 162: the user message bubble already has `break-words` in its class list: `"ml-auto max-w-[80%] rounded-xl px-3 py-2 break-words"`. The old note's claim ("User bubble: may lack break-words — July gap") is stale. No action needed here; keep as a regression check only.

### `src/components/ui/sidebar.tsx` (real path — old note said bare `sidebar.tsx`)

- `SIDEBAR_WIDTH = "25rem"`, `SIDEBAR_WIDTH_MOBILE = "100%"` — confirmed (lines 16–17).
- Whether the send button actually overflows at 320–375px is **not verifiable from source alone** — nothing in `ChatInputBar.tsx`'s markup (flex row, `shrink-0` on the button) obviously breaks at small widths, but real rendering (font metrics, card padding, viewport chrome) can still overflow. **Task 7.1 stays open and unverified** — needs an actual repro (dev server + real viewport or Playwright), not a code read.

## Target behavior

### 1. Textarea vertical centering (Task 6.3)

**When 1 line and no counter showing:**
- Text vertically centered in the input card, left-aligned horizontally.
- Outer wrapper: swap the static `items-end` for a conditional — `items-center` at single line, `items-end` once the textarea grows past one line or the counter is visible (so growth doesn't visually jump — counter appearing is itself a legitimate reason to fall back to bottom-aligned, don't fight it).

**When 2–3 lines:**
- Keep `items-end` (current behavior) — text top-aligns naturally as the textarea's own height grows; at `MAX_LINES` cap, internal scroll already works via the existing `resize()` height cap.

**Implementation pattern (illustrative, not prescriptive — Cursor should match existing code style):**
```tsx
const isSingleLine = !showCounter && lineCount <= 1; // derive lineCount from scrollHeight/lineHeight, same math resize() already uses
<div className={cn(
  "cosmic-card flex gap-2 px-3 py-2",
  isSingleLine ? "items-center" : "items-end",
  "border-violet-500/20",
)}>
```

### 2. Send button
- Already `shrink-0 h-7 w-7` — no change needed. It will naturally re-center with the row when `items-center` applies, and stay bottom-aligned when `items-end` applies. Do not add separate positioning for the button.

### 3. Mobile layout (Task 7.1) — unchanged scope, still needs a real repro first
- Reproduce at 320, 375, 390px widths before touching any code.
- If a real overflow reproduces, fix at the root (likely `ChatInputBar.tsx`'s flex/padding or the sidebar's mobile width interacting with card padding) — not a per-viewport patch.

### 4. Chat bubble wrap (Task 7.2) — already satisfied, verify only
- Confirm long unbroken strings still wrap with the existing `break-words` class; this is a regression check, not new work.

## Files to modify

1. `src/components/lab/ChatInputBar.tsx` — only file needing a real code change (Task 6.3).
2. `src/components/ui/sidebar.tsx` and/or `src/components/lab/ChatInputBar.tsx` — only if Task 7.1 repro confirms a real mobile overflow.
3. `src/components/lab/ChatThread.tsx` — no change expected; touch only if the Task 7.2 regression check somehow fails.

## Do NOT

- Do not re-add `break-words` to `ChatThread.tsx` — it's already there (line 162). Adding a duplicate class is harmless but pointless; don't spend a turn on it.
- Do not restructure `ChatInputBar.tsx` beyond the `items-end`/`items-center` conditional — don't touch `MAX_LEN`, `MAX_LINES`, the resize algorithm, paste handling, or persona detection.
- Do not "fix" Task 7.1 without reproducing it first — there is no code-level evidence of a bug today.
- Do not change `SIDEBAR_WIDTH` or `SIDEBAR_WIDTH_MOBILE` unless the Task 7.1 repro specifically implicates them.

## Accessibility

- Keep `aria-label="Message to Orby"` on the textarea and `aria-label="Send message"` on the button — both already correct, don't remove during the class-conditional refactor.
- Counter `aria-live="polite"` only when visible — already correct (conditional render, not just opacity).

## Acceptance criteria

- [ ] 1 line typed, no counter visible: text and placeholder both vertically centered, left-aligned
- [ ] Counter appears (>800 chars) or text wraps to 2+ lines: falls back to bottom-aligned, no visual jump/flicker
- [ ] 3 lines (cap): top-aligned within textarea, internal scroll, unchanged from today
- [ ] Enter submits, Shift+Enter inserts newline — unchanged
- [ ] Mobile 320/375/390px: send button confirmed on-screen (repro'd, not assumed) — fix only if repro shows a real bug
- [ ] Long unbroken string in a chat bubble still wraps (regression check on existing `break-words`)
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Front-loaded so it needs no follow-up turn.

```
Read ui-fix-07-portfolio-lab.md in full before touching any file. It was re-verified against the live repo on 2026-09-05 — one thing it corrects versus older notes: the chat-bubble break-words fix (old "Task 7.2") is ALREADY IMPLEMENTED in src/components/lab/ChatThread.tsx line 162. Do not re-add it, do not spend time on ChatThread.tsx at all unless your own regression check in step 3 below actually fails.

TASK 1 — Textarea vertical centering (the only confirmed code bug here):
File: src/components/lab/ChatInputBar.tsx, lines 80–85.
Today the outer row is a static `cosmic-card flex items-end gap-2 px-3 py-2` — this bottom-aligns the textarea+counter column at all times, including when there's only one short line of text.
Change: make the alignment conditional — `items-center` when the content is a single line AND the character counter is not showing (showCounter is already computed at line 25), `items-end` otherwise (multi-line growth, or counter visible). Derive "single line" using the same scrollHeight/lineHeight math the existing `resize()` callback (lines 27–34) already uses — do not invent a second measurement approach; reuse or lightly extend what's there. Recompute this alignment decision at the same points `resize()` already runs (on change, on submit, on mount) so it never lags a keystroke behind.
Do not touch MAX_LEN, MAX_LINES, the resize algorithm's height math, paste handling, or persona detection in this file — those are unrelated and already correct.

TASK 2 — Mobile send-button repro (Task 7.1), do this BEFORE editing anything for it:
Run the dev server and check src/components/lab/ChatInputBar.tsx rendered inside the Portfolio Lab sidebar at 320px, 375px, and 390px viewport widths (src/components/ui/sidebar.tsx sets SIDEBAR_WIDTH_MOBILE to 100%, so the card should have the full viewport width to work with).
If the send button overflows, clips, or forces horizontal scroll/zoom at any of those widths: fix the root cause (most likely candidates: the input row's flex sizing, `px-3` card padding leaving too little room, or the button's `shrink-0 h-7 w-7` not actually preventing compression under a real font-rendering width) in ChatInputBar.tsx and/or sidebar.tsx.
If it does NOT reproduce at any of those three widths: state that explicitly in your report and make no changes for this task. Do not "fix" something you couldn't reproduce.

TASK 3 — Regression check only, no code change expected:
Confirm a long unbroken string (e.g. a 200-character token with no spaces) still wraps inside a user chat bubble in ChatThread.tsx (the break-words class is already on line 162). If it somehow doesn't wrap, that's a real bug — report it and fix minimally. If it wraps correctly, just say so; do not touch this file.

VERIFY before reporting done, state each explicitly:
(a) Typing one short word: text and placeholder both sit vertically centered in the input card.
(b) Typing past the counter threshold, or wrapping to 2+ lines: alignment falls back to bottom (items-end) with no visible jump.
(c) Typing to the 3-line cap: unchanged from current behavior (top-aligned, internal scroll).
(d) Enter/Shift+Enter behavior unchanged.
(e) Mobile repro result at 320/375/390px stated explicitly, whether or not a fix was needed.
(f) Long-string wrap regression check result stated explicitly.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- Independent of GSAP/pin work (Phases 3–5).

## Risks

- The single-line/multi-line alignment switch must not visibly "pop" mid-keystroke — tie it to the same measurement `resize()` already performs each frame of input, not a separate debounced check.
- Task 7.1 has no code-level signal either way — resist the urge to preemptively "harden" mobile layout without a confirmed repro; that's speculative work outside this task's scope.
