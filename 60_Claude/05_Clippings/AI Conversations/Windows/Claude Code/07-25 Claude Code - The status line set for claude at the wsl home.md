---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "The status line set for claude at the wsl home"
started_at: 2026-07-25T19:02:35
ended_at: 2026-07-25T20:40:42
project: Jarvis
status: raw
session_id: d8bb2e2e-53d1-4b26-ab93-c763ddbb1315
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
tags:
  - input
  - ai-conversation
  - claude-code
---

# The status line set for claude at the wsl home

## You

The status line set for claude at the wsl home directory(`\\wsl$\Ubuntu\home\anant_gupta`) needs to be mimicked in a manner that we improve the current code. The improvements to the status line should be a live usage counter for each and every session working all the time. There is no time listed for the weekly limit to get over either. There should be time with hour and minutes. This should be the latest usage count that appears on the claude app usage counter. There should be absolutely no difference between these two. The one in wsl currently is not exactly always correct. Rest everything works. Fix the existing status line, improve it further and add a rolling timeline for the 5 hour session.

## Claude

I'll start by locating the existing status line configuration in the WSL home directory.

Found `statusline.sh`. Let me read it and the settings.json to understand current setup.

Now I have the full schema. The core bug: the script never reads `rate_limits.five_hour` at all — it only shows context-window usage and the weekly bar, with no reset times anywhere. Let me test executing the WSL bash directly so I can verify the rewritten script actually runs correctly inside Ubuntu.

Good, I can test directly in the Ubuntu environment. Now let me write the improved script.

The script behaves correctly across normal usage, high/red thresholds, and missing-data fallbacks — including the rolling timeline marker sliding toward the end as the window closes. Now deploying it to the real file and enabling live ticking via `refreshInterval`.

Now updating settings.json to add `refreshInterval` so the countdowns and timeline keep ticking even when the session is idle (otherwise they'd only update on new messages/compaction, which is why time data felt stale/"not always correct").

Good catch — the Write tool had reset the exec bit; now restored. Let me do one final end-to-end sanity check running the deployed file in place with `bash` (as settings.json invokes it) plus validate settings.json is valid JSON.

Deployed and verified working correctly. Cleaning up the scratch test fixtures.

## Summary

The old status line's core bug: it never read `rate_limits.five_hour` at all — it only showed context-window usage and a bare weekly percentage, with no reset times anywhere. That's why the 5-hour session usage felt invisible and the weekly reset had no clock on it.

Rewrote `~/.claude/statusline.sh` (WSL) to output 4 lines:
1. `folder | branch | model | ctx bar` (unchanged)
2. `5h [bar] NN% resets in Xh Ym (H:MM AM/PM)` — the session usage number, read straight from `rate_limits.five_hour.used_percentage`/`resets_at` with no client-side recalculation, so it can't drift from the Claude app's own usage page
3. A rolling timeline bar — a `>` marker sliding across a 20-cell bar showing exactly where "now" sits inside the current 5-hour rolling window (derived from `resets_at - 5h` as the window start), with "Xh Ym in / Xh Ym left of 5h"
4. `7d [bar] NN% resets in Xd Xh (Day H:MM AM/PM)` — same fix applied to the weekly limit

Also added `"refreshInterval": 30` to `settings.json`'s `statusLine` config — previously the line only redrew on new messages/compaction/mode changes, so countdowns went stale whenever Claude was idle. Now it ticks every 30s regardless.

Tested against fixtures in WSL directly (mid-window, near-reset/red-threshold, and missing-data/free-tier cases) — bars, colors, countdowns, and the timeline marker all render correctly, and it falls back to clear placeholder text ("warming up…", "no weekly limit data") instead of going blank when `rate_limits` isn't populated yet.

*Tools used: Bash, Read, ToolSearch, WebSearch, WebFetch, Write, Edit*

## You

```────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  internship-research-loop | master | Sonnet 5 | ctx [----------] 8%
  5h  [----------] 2% resets in 2h 9m (8:20 PM)
     [===========>........] 2h 50m in / 2h 9m left of 5h
  7d  [----------] 0% resets in 6d 6h (Sat 1:00 AM)```. Is what currently renders in wsl. I want the time bar to be next to the 5 hour window time line. There should not be a new line for this time bar. Each of the bars and percentage should be live with the actual claude app. There should be absolute no difference in both of these. The new context bar should be the most accurate part about the session, make sure that it updates per prompt or token burnt. Next to the context bar should be the tokens for each model that I run. The limit changes for each model that's run and this is right next to the context bar - displaying the tokens totally burnt throughout the session. After you make sure that these changes are reflected and working perfectly. Copy that same status line file into the windows home directory. Both these status lines should be perfect and working.

## Claude

There's already a `statusline-command.sh` here — let me check it and the Windows settings.json before overwriting anything.

The pain point was `wsl.exe -c "...;..."` losing shell semantics through Windows argv reconstruction — writing an actual script file and invoking it works reliably (as `GOT2:hello` just proved). Switching to that approach for all further testing.

Now writing the final combined script: merged 5h+timeline line, and per-model cumulative token tracking (cached against transcript mtime) next to the context bar.

Now let's build a realistic fixture using the real transcript and test full script behavior, including the cache.

That looks like stdout/stderr interleaving from `time` in my test harness, not a real bug. Let me re-run cleanly without `time` to confirm.

Good, both runs are consistent. Let me tighten the token-list separator slightly for readability, then re-verify the edge cases (missing rate_limits/transcript, high/red thresholds).

Now testing the missing-data and high/red-threshold edge cases against the updated script.

Good, this matches what tested. Now deploying to both the WSL and Windows `.claude` directories.

Now the same file into the Windows home `.claude` directory, plus fixing the settings.json pointer there (it currently references a broken `/mnt/c/...` path from a Windows-side Git Bash, which won't resolve).

Now fixing the Windows `settings.json` `statusLine` block — the old command pointed at a WSL-style `/mnt/c/...` path that Git Bash on Windows can't resolve.

Now validating the Windows settings.json is still valid JSON, setting exec bit, and doing a final live test on the Windows side directly (native Git Bash, no WSL detour).

That's this very conversation's own transcript — perfect for a fully real end-to-end test on the Windows side.

Found it — the native Windows `jq.exe` (WinGet build) emits CRLF line endings, so the cache file had a trailing `\r` corrupting the token number. Fixing by stripping `\r` when writing the cache.

Let me apply this fix to the scratch master copy first, retest, then propagate to both deployed files.

Now redeploying the fixed version to both locations and re-testing.

Now deploying the fixed version to the Windows `.claude` directory and re-testing, then re-testing WSL too (since the same jq-CRLF risk could theoretically occur there if WSL's jq ever writes CRLF, though it shouldn't — the fix is harmless either way).

Now updating the WSL copy with the same CRLF-safety fix (harmless there, but keeps both copies identical and robust).

Good, this is already the fixed version (my `cp` deployed it, and the harness's earlier note was just reporting that same content). Copying it to the WSL path now.

Now restoring the exec bit on WSL (Write always resets it) and doing a final clean end-to-end verification on both sides.

Both deployments verified working with the CRLF fix, merged 5h+timeline line, and per-model token totals. Cleaning up scratch test files.

## Summary

**Merged the timeline into the 5h line** — the quota bar, rolling-window timeline, and reset countdown now render on one line instead of two.

**Added per-model token totals next to the context bar.** Claude Code's `context_window` only reports the *live* window snapshot (not a cumulative total, and the limit differs per model), so there's no API field for "tokens burnt this session per model." I parse it out of the session's own transcript JSONL (`transcript_path`, given to the script), summing `input+output+cache_creation+cache_read` tokens grouped by `.message.model`. This is cached per `session_id` and only re-parsed when the transcript's mtime moves forward, so idle `refreshInterval` ticks don't re-read a multi-MB file for nothing.

**Bug caught during testing:** the Windows-native `jq.exe` (WinGet build) emits CRLF line endings, so the cached token numbers had a trailing `\r` baked in, which corrupted the arithmetic (`18366837\r` isn't a valid integer to bash). Fixed by stripping `\r` at both the write and read side — cheap, and a no-op on WSL where `jq` already emits LF-only.

**Context bar accuracy:** no logic change needed — Claude Code already re-invokes the statusline after every new assistant message with the live token count, so it was already "per prompt." Confirmed this holds structurally.

**Rate-limit numbers matching the app:** unchanged from before — both percentages are `rate_limits.*.used_percentage` displayed with no client-side recalculation, so they can't drift from what the app shows.

**Deployed identically to both machines:**
- WSL: `~/.claude/statusline.sh` (exec bit restored after each `Write`, since it resets NTFS permissions)
- Windows: `C:\Users\Anant Gupta\.claude\statusline.sh` — also fixed `settings.json`'s `statusLine.command`, which pointed at a broken `/mnt/c/...` WSL-style path that native Git Bash can't resolve (leftover from `statusline-command.sh`, which is no longer referenced but left on disk untouched). Both now use `bash ~/.claude/statusline.sh` with `refreshInterval: 30`.

Verified end-to-end on both sides using real transcripts (including this very conversation's own transcript on the Windows side) — cold-cache and warm-cache runs, high/red-threshold and missing-data fallback cases, and the CRLF fix, all confirmed correct.

*Tools used: Bash, Read, Write, Edit*

## You

```  Jarvis | master | Sonnet 5 | ctx [##--------] 23% | Sonnet 5 23.9M
  5h [######----] 64% [=========>....] 3h 26m/5h resets 1h 33m (9:50 PM)
  7d [----------] 7% resets in 6d 6h (Sat 2:30 AM)```. The existing status line needs to further improved: "Sonnet 5" is repeated twice, we only need the sonner 5 before ctx window - no model name right side of the ctx bar. The 23.9M is the total tokens that were used in the session? Let that be as it is but I want a rolling token usage per session in paranthesis brackets (). Example a model can only hold 1M context/tokens, then as the session moves we write: "23.9M (235.6K/1M) tokens". No model name only knowledge about the session that is updated per movement/update/run of the terminal. I also want a memory bar or file mention in status line but am not really sure how memory works and how it can be tracked. Let's dig into how we can showcase the memory for each session and what it holds. Do these changes across both wsl and windows both have the same status line now. Make these additions correctly and carefully, so far it works perfectly only needs updates. We need this bar to be working at all times and correctly synced with the claude app. Make sure that this is reflected on both wsl and windows. Do the task at hand correctly and finish it at once.

## Claude

Let me look at the two things needed: (1) how the model's max context size is exposed, and (2) what this "memory" directory actually contains on disk, before touching the script.

Now I understand both pieces. Let me rewrite the script: strip the duplicate model label, combine cumulative + live/max context tokens into one string, and add a memory-directory summary line (this "memory" is Claude Code's per-project memory store at `<project>/memory/` next to the transcripts — the same one this very session uses).

Now let's build a realistic fixture using this session's actual transcript and memory directory, and test end to end.

Matches exactly, and matches the real memory directory's file count and byte size. Now let's verify edge cases still degrade gracefully (no memory dir, no rate_limits).

Real bug caught — when `mem_str` is empty, the trailing `[ -n "$mem_str" ] && printf ...` short-circuits and the script's own exit code becomes 1. Per the docs, a non-zero exit blanks the entire status line in Claude Code, so this would silently break the whole feature whenever memory data is absent. Fixing with an explicit `exit 0`.

Both exit 0 now. Let's also test high/red thresholds and confirm robustness there, then deploy to both machines.

All correct — 200K-context model shows `188K/200K` cleanly. Now deploying the fixed version to both machines.

This is the final version. Deploying to both Windows and WSL.

Restoring exec bit on WSL and doing a final live verification against the real WSL project's transcript+memory data.

Both platforms confirmed working, exit 0, singular/plural handled correctly ("1 note" vs "14 notes"). Cleaning up test artifacts.

## Summary

**Removed the duplicate model name** — the tokens segment no longer labels itself with the model; it's just the numbers now.

**Token display upgraded to your format:** `26.6M (235.6K/1M) tokens`
- `26.6M` — cumulative tokens burnt this session (unchanged mechanism, still parsed from the transcript and cached against its mtime)
- `(235.6K/1M)` — the **live** context window's absolute token count against that model's actual ceiling, read straight from `context_window.total_input_tokens` / `context_window.context_window_size` — the exact numbers Claude Code itself divides to produce the ctx-bar percentage, so it updates every single prompt/response and can never disagree with either the ctx bar or the app.
- Number formatting standardized to uppercase `K`/`M` with no trailing `.0` on round numbers (`1M`, `200K`, `23.9M`).

**Added the memory line.** Claude Code keeps a persistent per-*project* memory store at `<project-dir>/memory/` — a sibling folder to the session transcripts, holding `MEMORY.md` plus individual note files (this is literally the memory system underpinning this conversation). It's shared by every session opened in that project, not scoped to one conversation. The new line reports it live:
```
mem 14 notes · 61.4KB · updated 16d 23h ago
```
counting files, summing bytes, and tracking the most recently touched file's age — verified against the real directory (14 files, 61.4KB summed and hand-checked).

**Bug caught during testing:** the new trailing `[ -n "$mem_str" ] && printf ...` line meant that whenever there was no memory folder, the script's own exit code became `1` — and per Claude Code's docs, a non-zero exit blanks the *entire* status line. Added an explicit `exit 0` at the end so this can never happen regardless of which optional line is present.

Verified end-to-end on both platforms against real transcripts and real memory folders (mid-usage, 200K vs 1M context ceilings, red/high thresholds, and the empty-data fallback), then deployed identical copies to `~/.claude/statusline.sh` (WSL) and `C:\Users\Anant Gupta\.claude\statusline.sh` (Windows) — both confirmed byte-identical and exit 0 in every case.

*Tools used: Bash, Write, Read, Edit*


