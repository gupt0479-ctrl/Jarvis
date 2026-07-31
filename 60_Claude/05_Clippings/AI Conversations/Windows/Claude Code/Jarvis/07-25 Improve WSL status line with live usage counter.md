---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Improve WSL status line with live usage counter"
started_at: 2026-07-25T19:02:35
ended_at: 2026-07-25T20:40:42
exported_at: 2026-07-31T21:03:25
duration_minutes: 98.1
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: d8bb2e2e-53d1-4b26-ab93-c763ddbb1315
status: raw
turn_count: 6
tools_used:
  Bash: 56
  Edit: 6
  Read: 12
  ToolSearch: 1
  WebFetch: 1
  WebSearch: 2
  Write: 23
tokens:
  input: 390
  output: 288354
  cache_creation: 570051
  cache_read: 32880377
  total: 33739172
cost_usd: 11.740599
model:
  - "claude-sonnet-5"
files_touched:
  - "//wsl$/Ubuntu/home/anant_gupta/.claude/settings.json"
  - "//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh"
  - "C:\\Users\\Anant Gupta\\.claude\\projects\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\tool-results\\toolu_01TPkJ9Z8w1WcW7LNZagX2fv.txt"
  - "C:\\Users\\Anant Gupta\\.claude\\settings.json"
  - "C:\\Users\\Anant Gupta\\.claude\\statusline.sh"
  - "C:\\Users\\Anant Gupta\\.claude\\statusline-command.sh"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_nodata.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_nometa.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_real.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_red.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_win.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_win_red.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_win2.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case_wsl2.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case1.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case2.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\case3.json"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\run_edge.sh"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\run_real.sh"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\run_real2.sh"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\statusline.sh"
  - "C:\\Users\\ANANTG~1\\AppData\\Local\\Temp\\claude\\D--Users--Anant-10-Areas-Documents-Jarvis\\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\\scratchpad\\test_tokens.sh"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Improve WSL status line with live usage counter

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

### Tool Calls

- `Bash` -- `ls -la "//wsl$/Ubuntu/home/anant_gupta/" 2>&1 | head -50`
```
ls: cannot access '//wsl$/Ubuntu/home/anant_gupta/.aws': Input/output error
ls: cannot access '//wsl$/Ubuntu/home/anant_gupta/.azure': Input/output error
total 228
drwxr-xr-x 34 Anant Gupta 197121      0 Jul 25 18:47 .
drwxr-xr-x  3 Anant Gupta 197121      0 Sep  3  2025 ..
drwxr-xr-x  3 Anant Gupta 197121      0 May  9 09:06 .agents
-?????????  ? ?           ?           ?            ? .aws
-?????????  ? ?           ?           ?            ? .azure
-rw-r--r--  1 Anant Gupta 197121 106852 Jul 25 02:24 .bash_history
-rw-r--r--  1 Anant Gupta 197121    220 Sep  3  2025 .bash_logout
-rw-r--r--  1 Anant Gupta 197121   4897 Jul 18 16:38 .bashrc
-rw-r--r--  1 Anant Gupta 197121   4341 Jun  7 20:31 .bashrc.bak.20260607-190106
drwxr-xr-x 21 Anant Gupta 197121      0 Jul 23 17:21 .cache
drwxr-xr-x  5 Anant Gupta 197121      0 Apr  7 08:56 .cargo
drwxr-xr-x 24 Anant Gupta 197121      0 Jul 25 18:44 .claude
-rw-r--r--  1 Anant Gupta 197121  77261 Jul 25 18:47 .claude.json
drwxr-xr-x 13 Anant Gupta 197121      0 Jul 25 19:00 .codex
drwxr-xr-x 19 Anant Gupta 197121      0 Jul 13 22:20 .config
drwxr-xr-x  4 Anant Gupta 197121      0 Jun 16 17:24 .copilot
drwxr-xr-x 10 Anant Gupta 197121      0 Jul  9 11:37 .cursor
drwxr-xr-x  5 Anant Gupta 197121      0 Jul 25 00:31 .cursor-server
drwxr-xr-x  6 Anant Gupta 197121      0 Jul  8 20:35 .docker
drwxr-xr-x  3 Anant Gupta 197121      0 Nov 16  2025 .dotnet
drwxr-xr-x  3 Anant Gupta 197121      0 Jun 16 17:24 .gemini
-rw-r--r--  1 Anant Gupta 197121    366 Jun  7 20:30 .gitconfig
drwxr-xr-x  3 Anant Gupta 197121      0 Sep  5  2025 .gnupg
drwxr-xr-x  4 Anant Gupta 197121      0 Jun 16 17:24 .kiro
drwxr-xr-x  2 Anant Gupta 197121      0 Oct 10  2025 .landscape
-rw-r--r--  1 Anant Gupta 197121    712 Jul 25 02:23 .lesshst
drwxr-xr-x  6 Anant Gupta 197121      0 May 22 10:23 .local
-rw-r--r--  1 Anant Gupta 197121   1117 Jul  5 19:17 .mcp.json
-rw-r--r--  1 Anant Gupta 197121      0 Jul 25 01:55 .motd_shown
-rw-r--r--  1 Anant Gupta 197121      0 Mar 21 05:22 .node_repl_history
drwxr-xr-x  6 Anant Gupta 197121      0 Jun  8 03:50 .npm
drwxr-xr-x  8 Anant Gupta 197121      0 Apr 11 08:12 .nvm
drwxr-xr-x  2 Anant Gupta 197121      0 May  9 21:16 .ollama
drwxr-xr-x  7 Anant Gupta 197121      0 Jul  9 12:49 .pencil
-rw-r--r--  1 Anant Gupta 197121    854 Mar  7 12:59 .profile
drwxr-xr-x  4 Anant Gupta 197121      0 Jun 11 23:10 .promptfoo
drwxr-xr-x  6 Anant Gupta 197121      0 Oct  7  2025 .rustup
drwxr-xr-x  2 Anant Gupta 197121      0 Jun  8 03:48 .ssh
-rw-r--r--  1 Anant Gupta 197121      0 Oct  7  2025 .sudo_as_admin_successful
drwxr-xr-x  3 Anant Gupta 197121      0 May 22 10:27 .supabase
drwxr-xr-x  4 Anant Gupta 197121      0 Sep  5  2025 .vscode-remote-containers
drwxr-xr-x  5 Anant Gupta 197121      0 Nov 16  2025 .vscode-server
-rw-r--r--  1 Anant Gupta 197121    183 Jul 23 16:37 .wget-hsts
-rw-r--r--  1 Anant Gupta 197121    340 Jun 13 13:07 .zshrc
drwxr-xr-x  2 Anant Gupta 197121      0 Jun  7 20:30 dotfiles
drwxr-xr-x  2 Anant Gupta 197121      0 Jun 12 00:13 Downloads
drwxr-xr-x  3 Anant Gupta 197121      0 Jul  9 12:49 Library
```
- `Bash` -- `ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/" 2>&1`
```
total 520
drwxr-xr-x 24 Anant Gupta 197121      0 Jul 25 18:44 .
drwxr-xr-x 34 Anant Gupta 197121      0 Jul 25 18:47 ..
-rw-r--r--  1 Anant Gupta 197121   2520 Jul 25 11:58 .credentials.json
-rw-r--r--  1 Anant Gupta 197121     24 Jul 25 12:19 .last-cleanup
-rw-r--r--  1 Anant Gupta 197121    161 Jul 25 11:58 .last-update-result.json
-rw-r--r--  1 Anant Gupta 197121   1074 Jun  4 15:44 .mcp.json
-rw-r--r--  1 Anant Gupta 197121      4 Jul 25 16:04 .ponytail-active
drwxr-xr-x  2 Anant Gupta 197121      0 Jun 10 19:09 agents
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 18:47 backups
-rw-r--r--  1 Anant Gupta 197121  35162 Jun 10 00:42 bash-commands.log
drwxr-xr-x  2 Anant Gupta 197121      0 Mar 24 00:20 cache
-rw-r--r--  1 Anant Gupta 197121    226 May  9 09:05 CLAUDE.md
drwxr-xr-x  2 Anant Gupta 197121      0 Jun 10 19:09 commands
-rw-r--r--  1 Anant Gupta 197121  38906 Jun 10 00:42 cost-tracker.log
drwxr-xr-x  2 Anant Gupta 197121      0 May 27 12:08 debug
drwxr-xr-x  2 Anant Gupta 197121      0 Mar 24 00:20 downloads
drwxr-xr-x 31 Anant Gupta 197121      0 Jul 25 12:18 file-history
-rw-r--r--  1 Anant Gupta 197121 378769 Jul 25 18:44 history.jsonl
drwxr-xr-x  3 Anant Gupta 197121      0 Jun 10 00:45 homunculus
drwxr-xr-x  2 Anant Gupta 197121      0 Jun 10 19:01 hooks
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 11:49 ide
-rw-r--r--  1 Anant Gupta 197121   5912 Jun 13 15:05 keybindings.json
-rw-r--r--  1 Anant Gupta 197121    371 Apr  4 04:04 mcp-health-cache.json
-rw-r--r--  1 Anant Gupta 197121     86 Jul 23 17:35 mcp-needs-auth-cache.json
drwxr-xr-x  2 Anant Gupta 197121      0 Apr  3 11:28 metrics
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 18:44 paste-cache
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 02:09 plans
drwxr-xr-x  5 Anant Gupta 197121      0 Jul 25 12:09 plugins
drwxr-xr-x  9 Anant Gupta 197121      0 Jul 16 23:17 projects
drwxr-xr-x  2 Anant Gupta 197121      0 Jun 10 01:35 session-data
drwxr-xr-x 75 Anant Gupta 197121      0 Jul 25 12:18 session-env
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 01:53 session-logs
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 11:59 sessions
-rw-r--r--  1 Anant Gupta 197121   1606 Jul 25 00:32 settings.json
-rw-r--r--  1 Anant Gupta 197121     71 Jun 11 21:59 settings.local.json
drwxr-xr-x  2 Anant Gupta 197121      0 Jul 25 18:44 shell-snapshots
drwxr-xr-x 15 Anant Gupta 197121      0 Jun 16 17:24 skills
-rw-r--r--  1 Anant Gupta 197121   6217 Jun 11 22:12 stats-cache.json
-rwxr-xr-x  1 Anant Gupta 197121   3457 Jul 10 17:51 statusline.sh
drwxr-xr-x 12 Anant Gupta 197121      0 Jul 25 12:18 tasks
```
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
- `Read` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/settings.json`
- `Bash` -- `ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/debug/" 2>&1
echo "---"
ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/session-data/" 2>&1
echo "---metrics---"
ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/metrics/" 2>&1`
```
ls: cannot access '//wsl$/Ubuntu/home/anant_gupta/.claude/debug/latest': Input/output error
total 0
drwxr-xr-x  2 Anant Gupta 197121 0 May 27 12:08 .
drwxr-xr-x 24 Anant Gupta 197121 0 Jul 25 18:44 ..
-?????????  ? ?           ?      ?            ? latest
---
total 36
drwxr-xr-x  2 Anant Gupta 197121    0 Jun 10 01:35 .
drwxr-xr-x 24 Anant Gupta 197121    0 Jul 25 18:44 ..
-rw-r--r--  1 Anant Gupta 197121 2670 Apr  5 00:34 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121  647 Apr  5 03:34 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121  923 Apr  7 10:39 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121  791 Apr 29 03:35 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121  846 Jun  6 06:34 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121 2065 Jun  6 15:04 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121 1116 Jun 10 00:45 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121 1582 Jun 10 02:35 [REDACTED].tmp
-rw-r--r--  1 Anant Gupta 197121  357 Jun  9 02:49 compaction-log.txt
---metrics---
total 12
drwxr-xr-x  2 Anant Gupta 197121    0 Apr  3 11:28 .
drwxr-xr-x 24 Anant Gupta 197121    0 Jul 25 18:44 ..
-rw-r--r--  1 Anant Gupta 197121 9419 Jun 10 02:35 costs.jsonl
```
- `ToolSearch` -- `{"query":"WebSearch WebFetch","max_results":5}`
- `WebSearch` -- `{"query":"Claude Code statusLine JSON schema rate_limits five_hour reset_at session"}`
- `WebSearch` -- `{"query":"Claude Code statusline input fields context_window rate_limits documentation"}`
- `WebFetch` -- `{"url":"https://code.claude.com/docs/en/statusline","prompt":"Give me the full JSON schema of the input passed to a statusLine command script, especially the rate_limits object (five_hour, seven_day) and context_window object. Include field names exactly as documented, and any example JSON."}`
- `Read` -- `C:\Users\Anant Gupta\.claude\projects\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\tool-results\toolu_01TPkJ9Z8w1WcW7LNZagX2fv.txt`
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c 'echo ok && which jq && date' 2>&1`
```
ok
/usr/bin/jq
Sat Jul 25 17:39:48 +04 2026
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context usage
# plus live 5-hour session usage/timeline and 7-day weekly usage, both with
# reset countdowns. Reads session JSON from stdin (see Claude Code statusLine
# docs). Dependency: jq. All time math uses rate_limits.*.resets_at (unix
# epoch seconds), the same numbers the Claude app's own usage page reads, so
# the percentages shown here always match the app - no separate calculation.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "$cwd")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

now=$(date +%s)

# --- context usage progress bar ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- 5-hour session usage bar (this is the number the Claude app calls
# "current session" on the usage page - rate_limits.five_hour.used_percentage,
# displayed unmodified so it can never drift from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET}  ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets in ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets in ${countdown}${RESET}"
    fi

    # --- rolling timeline: where "now" sits inside the current 5h window ---
    # the window is exactly 5h wide and always ends at five_reset_i, so its
    # start is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=20
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" "." )
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    # splice a ">" marker at the current position so the bar reads as a clock hand
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"

    elapsed_str=$(fmt_duration "$elapsed")
    remaining_str=$(fmt_duration "$((window_secs - elapsed))")
    timeline_str="${GRAY}   ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str} in / ${remaining_str} left of 5h${RESET}"
  else
    timeline_str="${GRAY}   [rolling timeline unavailable]${RESET}"
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
  timeline_str=""
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET}  ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
[ -n "$timeline_str" ] && printf '%s\n' "$timeline_str"
printf '%s\n' "$week_str"

```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "test -f '/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh' && echo FOUND || echo NOTFOUND"`
```
FOUND
```
- `Bash` -- `SCRIPT="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"
wsl.exe -d Ubuntu -- bash -c "chmod +x '$SCRIPT'"

echo "=== Case 1: normal mid-window, moderate usage ==="
wsl.exe -d Ubuntu -- bash -c '
now=$(date +%s)
five_reset=$((now + 2*3600 + 14*60))       # 2h14m from now -> window started 2h46m ago
week_reset=$((now + 3*86400 + 4*3600))     # 3d4h from now
json=$(jq -n --arg cwd "/home/anant_gupta/project" --argjson ctx 42 --argjson five 55.4 --argjson fr "$five_reset" --argjson week 23.1 --argjson wr "$week_reset" '"'"'
{cwd:$cwd, model:{display_name:"Sonnet 5"}, workspace:{current_dir:$cwd}, context_window:{used_percentage:$ctx}, rate_limits:{five_hour:{used_percentage:$five, resets_at:$fr}, seven_day:{used_percentage:$week, resets_at:$wr}}}
'"'"')
echo "$json" | bash '"$SCRIPT"'
' 2>&1`
```
=== Case 1: normal mid-window, moderate usage ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34munknown[0m [90m|[0m [90mctx [no data yet][0m
[90m5h [warming up - appears after first message][0m
[90m7d [no weekly limit data][0m
used_percentage:$ctx}, rate_limits:{five_hour:{used_percentage:$five, resets_at:$fr}, seven_day:{used_percentage:$week, resets_at:$wr}}}                               
jq: 1 compile error
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c 'date +%s'`
```
1784986890
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case1.json`
```
{"cwd":"/home/anant_gupta/project","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"/home/anant_gupta/project"},"context_window":{"used_percentage":42},"rate_limits":{"five_hour":{"used_percentage":55.4,"resets_at":1784994930},"seven_day":{"used_percentage":23.1,"resets_at":1785260490}}}

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case2.json`
```
{"cwd":"/home/anant_gupta/project","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"/home/anant_gupta/project"},"context_window":{"used_percentage":null}}

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case3.json`
```
{"cwd":"/home/anant_gupta/project","model":{"display_name":"Opus"},"workspace":{"current_dir":"/home/anant_gupta/project"},"context_window":{"used_percentage":91},"rate_limits":{"five_hour":{"used_percentage":92.7,"resets_at":1784987490},"seven_day":{"used_percentage":81.0,"resets_at":1785008490}}}

```
- `Bash` -- `DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
SCRIPT="$DIR/statusline.sh"
for c in case1 case2 case3; do
  echo "=== $c ==="
  wsl.exe -d Ubuntu -- bash -c "bash '$SCRIPT' < '$DIR/$c.json'"
  echo
done`
```
=== case1 ===
[36mproject[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [33m[####------] 42%[0m
[90m5h[0m  [33m[#####-----] 55%[0m [90mresets in 2h 13m (7:55 PM)[0m
[90m   [36m[===========>........][0m [90m2h 46m in / 2h 13m left of 5h[0m
[90m7d[0m  [32m[##--------] 23%[0m [90mresets in 3d 3h (Tue 9:41 PM)[0m

=== case2 ===
[36mproject[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx [no data yet][0m
[90m5h [warming up - appears after first message][0m
[90m7d [no weekly limit data][0m

=== case3 ===
[36mproject[0m [90m|[0m [34mOpus[0m [90m|[0m [90mctx[0m [31m[#########-] 91%[0m [31m[1m![0m
[90m5h[0m  [31m[#########-] 93%[0m [31m[1m![0m [90mresets in 9m (5:51 PM)[0m
[90m   [36m[===================>][0m [90m4h 50m in / 9m left of 5h[0m
[90m7d[0m  [31m[########--] 81%[0m [31m[1m![0m [90mresets in 5h 59m (Sat 11:41 PM)[0m
```
- `Write` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context usage
# plus live 5-hour session usage/timeline and 7-day weekly usage, both with
# reset countdowns. Reads session JSON from stdin (see Claude Code statusLine
# docs). Dependency: jq. All time math uses rate_limits.*.resets_at (unix
# epoch seconds), the same numbers the Claude app's own usage page reads, so
# the percentages shown here always match the app - no separate calculation.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "$cwd")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

now=$(date +%s)

# --- context usage progress bar ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- 5-hour session usage bar (this is the number the Claude app calls
# "current session" on the usage page - rate_limits.five_hour.used_percentage,
# displayed unmodified so it can never drift from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET}  ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets in ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets in ${countdown}${RESET}"
    fi

    # --- rolling timeline: where "now" sits inside the current 5h window ---
    # the window is exactly 5h wide and always ends at five_reset_i, so its
    # start is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=20
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" "." )
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    # splice a ">" marker at the current position so the bar reads as a clock hand
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"

    elapsed_str=$(fmt_duration "$elapsed")
    remaining_str=$(fmt_duration "$((window_secs - elapsed))")
    timeline_str="${GRAY}   ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str} in / ${remaining_str} left of 5h${RESET}"
  else
    timeline_str="${GRAY}   [rolling timeline unavailable]${RESET}"
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
  timeline_str=""
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET}  ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
[ -n "$timeline_str" ] && printf '%s\n' "$timeline_str"
printf '%s\n' "$week_str"

```
- `Edit` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/settings.json`
```diff
-   "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline.sh",
    "padding": 0
  },
+   "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline.sh",
    "padding": 0,
    "refreshInterval": 30
  },
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/statusline.sh && chmod +x ~/.claude/statusline.sh && ls -la ~/.claude/statusline.sh"`
```
-rw-r--r-- 1 anant_gupta anant_gupta 7522 Jul 25 17:43 /home/anant_gupta/.claude/statusline.sh
-rwxr-xr-x 1 anant_gupta anant_gupta 7522 Jul 25 17:43 /home/anant_gupta/.claude/statusline.sh
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c '
jq . ~/.claude/settings.json > /dev/null && echo "settings.json: valid JSON"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "--- deployed script, case1 fixture ---"
bash ~/.claude/statusline.sh < "$DIR/case1.json"
'`
```
Exit code 1
bash: line 5: /case1.json: No such file or directory
fixture ---
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "jq . ~/.claude/settings.json > /dev/null && echo 'settings.json: valid JSON'"`
```
settings.json: valid JSON
```
- `Bash` -- `DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case1.json'"
echo "--- case3 (high usage, near reset) ---"
wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case3.json'"`
```
[36mproject[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [33m[####------] 42%[0m
[90m5h[0m  [33m[#####-----] 55%[0m [90mresets in 2h 10m (7:55 PM)[0m
[90m   [36m[===========>........][0m [90m2h 49m in / 2h 10m left of 5h[0m
[90m7d[0m  [32m[##--------] 23%[0m [90mresets in 3d 3h (Tue 9:41 PM)[0m
--- case3 (high usage, near reset) ---
[36mproject[0m [90m|[0m [34mOpus[0m [90m|[0m [90mctx[0m [31m[#########-] 91%[0m [31m[1m![0m
[90m5h[0m  [31m[#########-] 93%[0m [31m[1m![0m [90mresets in 6m (5:51 PM)[0m
[90m   [36m[===================>][0m [90m4h 53m in / 6m left of 5h[0m
[90m7d[0m  [31m[########--] 81%[0m [31m[1m![0m [90mresets in 5h 56m (Sat 11:41 PM)[0m
```
- `Bash` -- `rm -f "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case1.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case2.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case3.json" 2>&1
echo done`
```
done
```

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

### Tool Calls

- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/ | head -20"`
```
total 44
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul  8 12:46 -home-anant-gupta
drwx------  8 anant_gupta anant_gupta  4096 Jul  9 11:28 -home-anant-gupta-projects-hub-CausalOps
drwx------  8 anant_gupta anant_gupta 12288 Jul 25 00:27 -home-anant-gupta-projects-hub-portfolio
drwxr-xr-x  9 anant_gupta anant_gupta  4096 Jul 21 19:06 -home-anant-gupta-projects-hub-tradingview
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul  1 19:55 -home-anant-gupta-projects-work-gupta-builds
drwxr-xr-x  5 anant_gupta anant_gupta  4096 Jul 25 10:30 -home-anant-gupta-projects-work-internship-research-loop
drwxr-xr-x  9 anant_gupta anant_gupta  4096 Jul 16 21:47 .
drwxr-xr-x 24 anant_gupta anant_gupta  4096 Jul 25 17:43 ..
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Apr  4 02:30 template
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/ | tail -20"`
```
total 8208
drwxr-xr-x 5 anant_gupta anant_gupta    4096 Jul 25 10:30 .
drwxr-xr-x 9 anant_gupta anant_gupta    4096 Jul 16 21:47 ..
-rw------- 1 anant_gupta anant_gupta  267670 Jul 25 17:25 [REDACTED].jsonl
drwxr-xr-x 3 anant_gupta anant_gupta    4096 Jul 19 13:38 [REDACTED]
-rw------- 1 anant_gupta anant_gupta 1584234 Jul 25 17:24 [REDACTED].jsonl
-rw------- 1 anant_gupta anant_gupta 2600046 Jul 19 13:07 [REDACTED].jsonl
-rw------- 1 anant_gupta anant_gupta   13347 Jul 25 14:14 [REDACTED].jsonl
drwxr-xr-x 3 anant_gupta anant_gupta    4096 Jul 17 21:34 [REDACTED]
-rw------- 1 anant_gupta anant_gupta 3892611 Jul 18 18:09 [REDACTED].jsonl
drwxr-xr-x 2 anant_gupta anant_gupta    4096 Jul 18 18:25 memory
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "tail -c 4000 ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | tail -5"`
```
vesting more."}],"stop_reason":"end_turn","stop_sequence":null,"stop_details":null,"usage":{"input_tokens":2,"cache_creation_input_tokens":2174,"cache_read_input_tokens":82169,"output_tokens":982,"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"[REDACTED]":2174,"[REDACTED]":0},"inference_geo":"not_available","iterations":[{"input_tokens":2,"output_tokens":982,"cache_read_input_tokens":82169,"cache_creation_input_tokens":2174,"cache_creation":{"[REDACTED]":0,"[REDACTED]":2174},"type":"message"}],"speed":"standard"},"diagnostics":null},"requestId":"[REDACTED]","type":"assistant","uuid":"[REDACTED]","timestamp":"2026-07-25T11:23:53.945Z","effort":"high","session_id":"[REDACTED]","userType":"external","entrypoint":"cli","cwd":"/home/anant_gupta/projects/work/internship-research-loop","sessionId":"[REDACTED]","version":"2.1.220","gitBranch":"master","slug":"wise-dazzling-beaver"}
{"parentUuid":"[REDACTED]","isSidechain":false,"attachment":{"type":"hook_success","hookName":"Stop","toolUseID":"[REDACTED]","hookEvent":"Stop","content":"[ session ] No log for 2026-07-25 — run /save-session when done.","stdout":"[ session ] No log for 2026-07-25 — run /save-session when done.\n","stderr":"","exitCode":0,"command":"pwsh -ExecutionPolicy Bypass -File /home/anant_gupta/.claude/hooks/session-wrapup.ps1","durationMs":11505},"type":"attachment","uuid":"[REDACTED]","timestamp":"2026-07-25T11:24:05.507Z","session_id":"[REDACTED]","userType":"external","entrypoint":"cli","cwd":"/home/anant_gupta/projects/work/internship-research-loop","sessionId":"[REDACTED]","version":"2.1.220","gitBranch":"master","slug":"wise-dazzling-beaver"}
{"parentUuid":"[REDACTED]","isSidechain":false,"type":"system","subtype":"stop_hook_summary","hookCount":1,"hookInfos":[{"command":"pwsh -ExecutionPolicy Bypass -File /home/anant_gupta/.claude/hooks/session-wrapup.ps1","durationMs":11505}],"hookErrors":[],"hookAdditionalContext":[],"preventedContinuation":false,"stopReason":"","hasOutput":true,"level":"suggestion","timestamp":"2026-07-25T11:24:05.508Z","uuid":"[REDACTED]","toolUseID":"[REDACTED]","session_id":"[REDACTED]","userType":"external","entrypoint":"cli","cwd":"/home/anant_gupta/projects/work/internship-research-loop","sessionId":"[REDACTED]","version":"2.1.220","gitBranch":"master","slug":"wise-dazzling-beaver"}
{"parentUuid":"[REDACTED]","isSidechain":false,"type":"system","subtype":"turn_duration","durationMs":59902,"messageCount":69,"timestamp":"2026-07-25T11:24:05.514Z","uuid":"[REDACTED]","isMeta":false,"userType":"external","entrypoint":"cli","cwd":"/home/anant_gupta/projects/work/internship-research-loop","sessionId":"[REDACTED]","version":"2.1.220","gitBranch":"master","slug":"wise-dazzling-beaver"}
{"parentUuid":"[REDACTED]","isSidechain":false,"type":"system","subtype":"away_summary","content":"Your internship pipeline currently uses two community job lists; we're adding direct company career-page feeds via Greenhouse/Lever/Ashby APIs to catch more postings. Next: send a list of 15-30 target companies so I can wire them in. (disable recaps in /config)","timestamp":"2026-07-25T11:27:03.452Z","uuid":"[REDACTED]","isMeta":false,"userType":"external","entrypoint":"cli","cwd":"/home/anant_gupta/projects/work/internship-research-loop","sessionId":"[REDACTED]","version":"2.1.220","gitBranch":"master","slug":"wise-dazzling-beaver"}
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "grep -o '\"type\":\"assistant\".\{0,50\}' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | head -3
echo '---model field search---'
grep -m1 -o '\"model\":\"[^\"]*\"' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl
echo '---full first assistant line structure (truncated)---'
grep -m1 '\"type\":\"assistant\"' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | head -c 1500"`
```
"type":"assistant","uuid":"[REDACTED]","ti
"type":"assistant","uuid":"[REDACTED]","ti
"type":"assistant","uuid":"[REDACTED]","ti
---model field search---
"model":"[REDACTED]"
---full first assistant line structure (truncated)---
{"parentUuid":"[REDACTED]","isSidechain":false,"message":{"model":"[REDACTED]","id":"[REDACTED]","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"","signature":"Er0ICpMBCA8YAipAH4Ek4zW/[REDACTED]/[REDACTED]+[REDACTED]/[REDACTED]/[REDACTED]/[REDACTED]/[REDACTED]/hk1kIYOOuGJCL+[REDACTED]/[REDACTED]/[REDACTED]/[REDACTED]/lQeO69TnqWuE0bRDO1uJ/4ywxppPJR4DEFN/3p5z/CMNv4r0TJLrAxbF5+[REDACTED]+[REDACTED]+[REDACTED]/6UnahjWLKhHi/RgmYBuDM9/[REDACTED]/A4Icq4LO/+[REDACTED]++8UaYZyZoeJ6Q9Gblgdw/GGgrcwCrWBCSmBOgDDqPk+[REDACTED]+GPYd/[REDACTED]/86WBmTbxUs1FRK16A4/eD48WS/gmDQ5bTgIRPwk0BFwV
```
- `Bash` -- `echo "jq: $(command -v jq || echo MISSING)"
echo "awk: $(command -v awk || echo MISSING)"
echo "stat: $(command -v stat || echo MISSING)"
date -d @1700000000 +'%-I:%M %p' 2>&1
echo "---"
uname -a
echo "---home---"
echo $HOME
ls -la "$HOME/.claude" 2>&1 | head -30`
```
jq: /c/Users/Anant Gupta/AppData/Local/Microsoft/WinGet/Packages/jqlang.jq_Microsoft.Winget.Source_8wekyb3d8bbwe/jq
awk: /usr/bin/awk
stat: /usr/bin/stat
3:43 AM
---
MINGW64_NT-10.0-26200 DESKTOP-3VBG0JH 3.6.5-22c95533.x86_64 2025-10-10 12:02 UTC x86_64 Msys
---home---
/c/Users/Anant Gupta
total 489
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:44 .
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:43 ..
-rw-r--r-- 1 Anant Gupta 197121    723 Jul 25 12:01 .credentials.json
-rw-r--r-- 1 Anant Gupta 197121     24 Jul 25 19:26 .last-cleanup
-rw-r--r-- 1 Anant Gupta 197121    161 Jul 25 18:46 .last-update-result.json
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:43 backups
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 16:01 cache
drwxr-xr-x 1 Anant Gupta 197121      0 Jun  3 03:30 daemon
drwxr-xr-x 1 Anant Gupta 197121      0 May 27 11:05 debug
drwxr-xr-x 1 Anant Gupta 197121      0 Mar 23 23:54 downloads
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:13 file-history
-rw-r--r-- 1 Anant Gupta 197121 269526 Jul 25 19:44 history.jsonl
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 02:23 ide
-rw-r--r-- 1 Anant Gupta 197121  30694 Jul 25 16:04 jarvis-session-activity.jsonl
-rw-r--r-- 1 Anant Gupta 197121     86 Jul 21 20:05 mcp-needs-auth-cache.json
drwxr-xr-x 1 Anant Gupta 197121      0 Jun  2 18:40 memory
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:01 paste-cache
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 13 18:46 plans
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:10 plugins
drwxr-xr-x 1 Anant Gupta 197121      0 Jul  9 11:37 projects
-rw-r--r-- 1 Anant Gupta 197121     91 Jun 20 01:27 scheduled_tasks.lock
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:02 session-env
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:02 sessions
-rw-r--r-- 1 Anant Gupta 197121   5133 Jul 21 21:08 settings.json
-rw-r--r-- 1 Anant Gupta 197121    519 Jun  7 19:40 settings.local.json
drwxr-xr-x 1 Anant Gupta 197121      0 Jul 25 19:06 shell-snapshots
drwxr-xr-x 1 Anant Gupta 197121      0 Jul  5 13:35 skills
-rw-r--r-- 1 Anant Gupta 197121   5790 Apr 26 07:43 stats-cache.json
-rwxr-xr-x 1 Anant Gupta 197121   2184 Jul  6 00:52 statusline-command.sh
```
- `Read` -- `C:\Users\Anant Gupta\.claude\statusline-command.sh`
- `Bash` -- `python3 -c "
import json
d=json.load(open(r'C:\Users\Anant Gupta\.claude\settings.json'))
print(json.dumps(d.get('statusLine'), indent=2))
" 2>&1 || grep -A5 '"statusLine"' "/c/Users/Anant Gupta/.claude/settings.json"`
```
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
  "statusLine": {
    "command": "bash /mnt/c/Users/Anant\\ Gupta/.claude/statusline-command.sh",
    "type": "command"
  }
}
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c '
T=~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl
time jq -r -s "
  map(select(.type==\"assistant\" and .message.usage != null)
      | {model: .message.model,
         tok: ((.message.usage.input_tokens // 0)
             + (.message.usage.output_tokens // 0)
             + (.message.usage.cache_creation_input_tokens // 0)
             + (.message.usage.cache_read_input_tokens // 0))})
  | group_by(.model)
  | map({model: .[0].model, total: (map(.tok) | add)})
  | sort_by(-.total)
  | .[]
  | \"\(.model)\t\(.total)\"
" "$T"
'`
```
Exit code 2
jq: error: Could not open file : No such file or directory

real	0m0.008s
user	0m0.000s
sys	0m0.007s
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c 'T=~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo "[$T]"; ls -la "$T"'`
```
Exit code 2
ls: cannot access '': No such file or directory
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo GOT:\$T; wc -l \"\$T\""`
```
Exit code 1
wc: invalid zero-length file name
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "echo hello; echo HOME_IS:\$HOME"`
```
hello
HOME_IS:/home/anant_gupta
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo GOT:\$T; wc -l \"\$T\""`
```
Exit code 1
wc: invalid zero-length file name
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo GOT:\$T"`
```
GOT:
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/settings.json; echo GOT:\$T"
echo "==="
wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop; echo GOT:\$T"`
```
GOT:
===
GOT:
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=hello; echo GOT:\$T"`
```
GOT:
```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "T=hello && echo GOT:\$T"
echo "---using printf script file---"
printf '%s\n' 'T=hello' 'echo "GOT2:$T"' > /tmp/wsltest.sh
wsl.exe -d Ubuntu -- bash /mnt/c/Users/*/AppData/Local/Temp/wsltest.sh 2>&1 || true
wsl.exe -d Ubuntu -- bash -c "cat /tmp/wsltest.sh 2>&1; bash /tmp/wsltest.sh 2>&1"`
```
Exit code 127
GOT:
---using printf script file---
GOT2:hello
cat: /tmp/wsltest.sh: No such file or directory
bash: /tmp/wsltest.sh: No such file or directory
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\test_tokens.sh`
```
#!/usr/bin/env bash
T="$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl"
echo "path: $T"
ls -la "$T"
time jq -r -s '
  map(select(.type=="assistant" and .message.usage != null)
      | {model: .message.model,
         tok: ((.message.usage.input_tokens // 0)
             + (.message.usage.output_tokens // 0)
             + (.message.usage.cache_creation_input_tokens // 0)
             + (.message.usage.cache_read_input_tokens // 0))})
  | group_by(.model)
  | map({model: .[0].model, total: (map(.tok) | add)})
  | sort_by(-.total)
  | .[]
  | "\(.model)\t\(.total)"
' "$T"

```
- `Bash` -- `wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/test_tokens.sh"`
```
Exit code 127
bash: C:/Program Files/Git/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/[REDACTED]/[REDACTED]/scratchpad/test_tokens.sh: No such file or directory
```
- `Bash` -- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/test_tokens.sh"`
```
real	0m0.006s
user	0m0.000s
sys	0m0.006s
home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl
-rw------- 1 anant_gupta anant_gupta 267670 Jul 25 18:23 /home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl
[REDACTED]	884040
claude-sonnet-5	709057
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | per-model tokens burnt
# then a merged 5-hour usage+rolling-timeline line, then a 7-day weekly line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# Per-model token totals come from parsing transcript_path (the session's own
# JSONL transcript), since Claude Code's context_window object only reports the
# *live* window, not a cumulative session total, and the context limit differs
# per model. The parse result is cached per session_id and only recomputed when
# the transcript file's mtime moves forward, so idle refreshInterval ticks don't
# re-parse a multi-MB file for no reason.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1.2M" / "884.0k" / "42"
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fM", n/1000000}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fk", n/1000}' 2>/dev/null || printf '%dk' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# "[REDACTED]" -> "Haiku 4.5", "claude-sonnet-5" -> "Sonnet 5"
pretty_model() {
  local id=$1
  id=${id#claude-}
  id=$(printf '%s' "$id" | sed -E 's/-[0-9]{8}$//')
  local family=${id%%-*}
  local rest=""
  [ "$family" != "$id" ] && rest=${id#*-}
  family="$(printf '%s' "${family:0:1}" | tr '[:lower:]' '[:upper:]')${family:1}"
  if [ -n "$rest" ]; then
    printf '%s %s' "$family" "$(printf '%s' "$rest" | tr '-' '.')"
  else
    printf '%s' "$family"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- per-model cumulative tokens burnt this session, read from the transcript
# and cached until the transcript file actually grows ---
tokens_str=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.tsv"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      map(select(.type=="assistant" and .message.usage != null)
          | {model: .message.model,
             tok: ((.message.usage.input_tokens // 0)
                 + (.message.usage.output_tokens // 0)
                 + (.message.usage.cache_creation_input_tokens // 0)
                 + (.message.usage.cache_read_input_tokens // 0))})
      | group_by(.model)
      | map({model: .[0].model, total: (map(.tok) | add)})
      | sort_by(-.total)
      | .[]
      | "\(.model)\t\(.total)"
    ' "$transcript_path" 2>/dev/null > "$cache_file"
  fi

  while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
    tokens_str="${tokens_str}${tokens_str:+  }${GRAY}${pretty}${RESET} ${ftot}"
  done < "$cache_file"
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_real.json`
```
{"cwd":"/home/anant_gupta/projects/work/internship-research-loop","session_id":"[REDACTED]","transcript_path":"/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"/home/anant_gupta/projects/work/internship-research-loop"},"context_window":{"used_percentage":8},"rate_limits":{"five_hour":{"used_percentage":2,"resets_at":1784994930},"seven_day":{"used_percentage":0,"resets_at":1785537930}}}

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_real.sh`
```
#!/usr/bin/env bash
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/[REDACTED]/[REDACTED]/scratchpad"
chmod +x "$DIR/statusline.sh"
echo "=== run 1 (cold cache) ==="
time bash "$DIR/statusline.sh" < "$DIR/case_real.json"
echo "=== run 2 (warm cache, should be near-instant) ==="
time bash "$DIR/statusline.sh" < "$DIR/case_real.json"
echo "=== cache file contents ==="
cat "${TMPDIR:-/tmp}/claude-statusline-tokens/[REDACTED].tsv"

```
- `Bash` -- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_real.sh"`
```
real	0m0.412s
user	0m0.093s
sys	0m0.052s

real	0m0.236s
user	0m0.061s
sys	0m0.035s
[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90mHaiku 4.5[0m 884.0k  [90mSonnet 5[0m 709.1k
[90m5h[0m [32m[----------] 2%[0m [36m[=========>....][0m [90m3h 29m/5h[0m [90mresets 1h 30m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 8h (Sat 2:45 AM)[0m
=== run 2 (warm cache, should be near-instant) ===
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90mHaiku 4.5[0m 884.0k  [90mSonnet 5[0m 709.1k
[90m5h[0m [32m[----------] 2%[0m [36m[=========>....][0m [90m3h 29m/5h[0m [90mresets 1h 30m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 8h (Sat 2:45 AM)[0m
=== cache file contents ===
[REDACTED]	884040
claude-sonnet-5	709057
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_real2.sh`
```
#!/usr/bin/env bash
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/[REDACTED]/[REDACTED]/scratchpad"
rm -rf "${TMPDIR:-/tmp}/claude-statusline-tokens"
echo "=== run 1 (cold cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_real.json"
echo "=== run 2 (warm cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_real.json"

```
- `Bash` -- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_real2.sh"`
```
=== run 1 (cold cache) ===
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90mHaiku 4.5[0m 884.0k  [90mSonnet 5[0m 709.1k
[90m5h[0m [32m[----------] 2%[0m [36m[=========>....][0m [90m3h 30m/5h[0m [90mresets 1h 29m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 8h (Sat 2:45 AM)[0m
=== run 2 (warm cache) ===
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90mHaiku 4.5[0m 884.0k  [90mSonnet 5[0m 709.1k
[90m5h[0m [32m[----------] 2%[0m [36m[=========>....][0m [90m3h 30m/5h[0m [90mresets 1h 29m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 8h (Sat 2:45 AM)[0m
```
- `Bash` -- `grep -n 'tokens_str:+' "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"`
```
175:    tokens_str="${tokens_str}${tokens_str:+  }${GRAY}${pretty}${RESET} ${ftot}"
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Edit` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```diff
-     tokens_str="${tokens_str}${tokens_str:+  }${GRAY}${pretty}${RESET} ${ftot}"
+     tokens_str="${tokens_str}${tokens_str:+ ${GRAY}·${RESET} }${GRAY}${pretty}${RESET} ${ftot}"
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_nodata.json`
```
{"cwd":"/home/anant_gupta/projects/work/internship-research-loop","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"/home/anant_gupta/projects/work/internship-research-loop"},"context_window":{"used_percentage":null}}

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_red.json`
```
{"cwd":"/home/anant_gupta/projects/work/internship-research-loop","session_id":"[REDACTED]","transcript_path":"/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl","model":{"display_name":"Opus"},"workspace":{"current_dir":"/home/anant_gupta/projects/work/internship-research-loop"},"context_window":{"used_percentage":91},"rate_limits":{"five_hour":{"used_percentage":92.7,"resets_at":1784987490},"seven_day":{"used_percentage":81.0,"resets_at":1785008490}}}

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_edge.sh`
```
#!/usr/bin/env bash
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/[REDACTED]/[REDACTED]/scratchpad"
echo "=== no rate_limits, null ctx ==="
bash "$DIR/statusline.sh" < "$DIR/case_nodata.json"
echo "=== high usage / red thresholds ==="
bash "$DIR/statusline.sh" < "$DIR/case_red.json"

```
- `Bash` -- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_edge.sh"`
```
=== no rate_limits, null ctx ===
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx [no data yet][0m
[90m5h [warming up - appears after first message][0m
[90m7d [no weekly limit data][0m
=== high usage / red thresholds ===
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mOpus[0m [90m|[0m [90mctx[0m [31m[#########-] 91%[0m [31m[1m![0m [90m|[0m [90mHaiku 4.5[0m 884.0k [90m·[0m [90mSonnet 5[0m 709.1k
[90m5h[0m [31m[#########-] 93%[0m [31m[1m![0m [36m[=============>][0m [90m5h 0m/5h[0m [90mresets 0m (5:51 PM)[0m
[90m7d[0m [31m[########--] 81%[0m [31m[1m![0m [90mresets in 5h 13m (Sat 11:41 PM)[0m
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Write` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | per-model tokens burnt
# then a merged 5-hour usage+rolling-timeline line, then a 7-day weekly line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# Per-model token totals come from parsing transcript_path (the session's own
# JSONL transcript), since Claude Code's context_window object only reports the
# *live* window, not a cumulative session total, and the context limit differs
# per model. The parse result is cached per session_id and only recomputed when
# the transcript file's mtime moves forward, so idle refreshInterval ticks don't
# re-parse a multi-MB file for no reason.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1.2M" / "884.0k" / "42"
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fM", n/1000000}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fk", n/1000}' 2>/dev/null || printf '%dk' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# "[REDACTED]" -> "Haiku 4.5", "claude-sonnet-5" -> "Sonnet 5"
pretty_model() {
  local id=$1
  id=${id#claude-}
  id=$(printf '%s' "$id" | sed -E 's/-[0-9]{8}$//')
  local family=${id%%-*}
  local rest=""
  [ "$family" != "$id" ] && rest=${id#*-}
  family="$(printf '%s' "${family:0:1}" | tr '[:lower:]' '[:upper:]')${family:1}"
  if [ -n "$rest" ]; then
    printf '%s %s' "$family" "$(printf '%s' "$rest" | tr '-' '.')"
  else
    printf '%s' "$family"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- per-model cumulative tokens burnt this session, read from the transcript
# and cached until the transcript file actually grows ---
tokens_str=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.tsv"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      map(select(.type=="assistant" and .message.usage != null)
          | {model: .message.model,
             tok: ((.message.usage.input_tokens // 0)
                 + (.message.usage.output_tokens // 0)
                 + (.message.usage.cache_creation_input_tokens // 0)
                 + (.message.usage.cache_read_input_tokens // 0))})
      | group_by(.model)
      | map({model: .[0].model, total: (map(.tok) | add)})
      | sort_by(-.total)
      | .[]
      | "\(.model)\t\(.total)"
    ' "$transcript_path" 2>/dev/null > "$cache_file"
  fi

  while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
    tokens_str="${tokens_str}${tokens_str:+ ${GRAY}·${RESET} }${GRAY}${pretty}${RESET} ${ftot}"
  done < "$cache_file"
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"

```
- `Write` -- `C:\Users\Anant Gupta\.claude\statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | per-model tokens burnt
# then a merged 5-hour usage+rolling-timeline line, then a 7-day weekly line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# Per-model token totals come from parsing transcript_path (the session's own
# JSONL transcript), since Claude Code's context_window object only reports the
# *live* window, not a cumulative session total, and the context limit differs
# per model. The parse result is cached per session_id and only recomputed when
# the transcript file's mtime moves forward, so idle refreshInterval ticks don't
# re-parse a multi-MB file for no reason.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1.2M" / "884.0k" / "42"
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fM", n/1000000}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fk", n/1000}' 2>/dev/null || printf '%dk' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# "[REDACTED]" -> "Haiku 4.5", "claude-sonnet-5" -> "Sonnet 5"
pretty_model() {
  local id=$1
  id=${id#claude-}
  id=$(printf '%s' "$id" | sed -E 's/-[0-9]{8}$//')
  local family=${id%%-*}
  local rest=""
  [ "$family" != "$id" ] && rest=${id#*-}
  family="$(printf '%s' "${family:0:1}" | tr '[:lower:]' '[:upper:]')${family:1}"
  if [ -n "$rest" ]; then
    printf '%s %s' "$family" "$(printf '%s' "$rest" | tr '-' '.')"
  else
    printf '%s' "$family"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- per-model cumulative tokens burnt this session, read from the transcript
# and cached until the transcript file actually grows ---
tokens_str=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.tsv"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      map(select(.type=="assistant" and .message.usage != null)
          | {model: .message.model,
             tok: ((.message.usage.input_tokens // 0)
                 + (.message.usage.output_tokens // 0)
                 + (.message.usage.cache_creation_input_tokens // 0)
                 + (.message.usage.cache_read_input_tokens // 0))})
      | group_by(.model)
      | map({model: .[0].model, total: (map(.tok) | add)})
      | sort_by(-.total)
      | .[]
      | "\(.model)\t\(.total)"
    ' "$transcript_path" 2>/dev/null > "$cache_file"
  fi

  while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
    tokens_str="${tokens_str}${tokens_str:+ ${GRAY}·${RESET} }${GRAY}${pretty}${RESET} ${ftot}"
  done < "$cache_file"
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"

```
- `Read` -- `C:\Users\Anant Gupta\.claude\settings.json`
- `Edit` -- `C:\Users\Anant Gupta\.claude\settings.json`
```diff
-   "statusLine": {
    "command": "bash /mnt/c/Users/Anant\\ Gupta/.claude/statusline-command.sh",
    "type": "command"
  }
+   "statusLine": {
    "command": "bash ~/.claude/statusline.sh",
    "type": "command",
    "padding": 0,
    "refreshInterval": 30
  }
```
- `Bash` -- `jq empty "/c/Users/Anant Gupta/.claude/settings.json" && echo "settings.json valid"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
ls -la "/c/Users/Anant Gupta/.claude/statusline.sh"`
```
settings.json valid
-rwxr-xr-x 1 Anant Gupta 197121 10494 Jul 25 19:59 /c/Users/Anant Gupta/.claude/statusline.sh
```
- `Bash` -- `ls "/c/Users/Anant Gupta/.claude/projects/" 2>&1 | head -20`
```
C--Users-Anant-Gupta
[REDACTED]
[REDACTED]
```
- `Bash` -- `ls -la "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/" | tail -5`
```
-rw-r--r-- 1 Anant Gupta 197121   327171 Jul  8 12:53 [REDACTED].jsonl
-rw-r--r-- 1 Anant Gupta 197121  3053485 Jul  8 22:26 [REDACTED].jsonl
-rw-r--r-- 1 Anant Gupta 197121   133457 Jul 25 16:01 [REDACTED].jsonl
-rw-r--r-- 1 Anant Gupta 197121   200123 Jul  4 18:48 [REDACTED].jsonl
drwxr-xr-x 1 Anant Gupta 197121        0 Jul  8 21:11 memory
```
- `Bash` -- `ls -lat "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/"*.jsonl | head -3`
```
-rw-r--r-- 1 Anant Gupta 197121   986057 Jul 25 20:02 /c/Users/Anant Gupta/.claude/projects/[REDACTED]/[REDACTED].jsonl
-rw-r--r-- 1 Anant Gupta 197121   556833 Jul 25 20:00 /c/Users/Anant Gupta/.claude/projects/[REDACTED]/[REDACTED].jsonl
-rw-r--r-- 1 Anant Gupta 197121  5004729 Jul 25 19:46 /c/Users/Anant Gupta/.claude/projects/[REDACTED]/[REDACTED].jsonl
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win.json`
```
{"cwd":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis","session_id":"[REDACTED]","transcript_path":"C:\\Users\\Anant Gupta\\.claude\\projects\\[REDACTED]\\[REDACTED].jsonl","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"},"context_window":{"used_percentage":63},"rate_limits":{"five_hour":{"used_percentage":18.4,"resets_at":1784994930},"seven_day":{"used_percentage":6.2,"resets_at":1785537930}}}

```
- `Bash` -- `bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"`
```
/c/Users/Anant Gupta/.claude/statusline.sh: line 98: [: 18366837: integer expression expected
/c/Users/Anant Gupta/.claude/statusline.sh: line 100: [: 18366837: integer expression expected
/c/Users/Anant Gupta/.claude/statusline.sh: line 103: printf: 18366837: invalid number
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [33m[######----] 63%[0m [90m|[0m [90mSonnet 5[0m 18366837
[90m5h[0m [32m[#---------] 18%[0m [36m[==========>...][0m [90m3h 37m/5h[0m [90mresets 1h 22m (9:25 PM)[0m
[90m7d[0m [32m[----------] 6%[0m [90mresets in 6d 8h (Sat 4:15 AM)[0m
```
- `Bash` -- `CACHE="/tmp/claude-statusline-tokens/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315.tsv"
echo "content:"; cat -A "$CACHE" 2>&1 | head -5
echo "---"
echo "TMPDIR is: $TMPDIR"
ls -la /tmp/claude-statusline-tokens/ 2>&1`
```
content:
claude-sonnet-5^I18366837^M$
---
TMPDIR is: 
total 2840
drwxr-xr-x 1 Anant Gupta 197121  0 Jul 25 20:00 .
drwxr-xr-x 1 Anant Gupta 197121  0 Jul 25 20:03 ..
-rw-r--r-- 1 Anant Gupta 197121 42 Jul 25 20:00 [REDACTED].tsv
-rw-r--r-- 1 Anant Gupta 197121 25 Jul 25 20:00 [REDACTED].tsv
-rw-r--r-- 1 Anant Gupta 197121 26 Jul 25 20:00 [REDACTED].tsv
-rw-r--r-- 1 Anant Gupta 197121 26 Jul 25 20:03 [REDACTED].tsv
```
- `Bash` -- `grep -n "> \"\$cache_file\"" "/c/Users/Anant Gupta/.claude/statusline.sh"`
```
168:    ' "$transcript_path" 2>/dev/null > "$cache_file"
```
- `Edit` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```diff
-     ' "$transcript_path" 2>/dev/null > "$cache_file"
+     ' "$transcript_path" 2>/dev/null | tr -d '\r' > "$cache_file"
```
- `Bash` -- `grep -n 'while IFS=\$.\\t.' -A5 "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh" 2>/dev/null
grep -n "while IFS=" "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"`
```
171:  while IFS=$'\t' read -r mdl tot; do
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Edit` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```diff
-   while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
+   while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    tot=${tot%$'\r'}
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Bash` -- `rm -rf /tmp/claude-statusline-tokens
cp "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh" "/c/Users/Anant Gupta/.claude/statusline.sh"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"
echo "=== run 2 (warm cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"`
```
=== run 1 (cold cache) ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [33m[######----] 63%[0m [90m|[0m [90mSonnet 5[0m 21.4M
[90m5h[0m [32m[#---------] 18%[0m [36m[==========>...][0m [90m3h 40m/5h[0m [90mresets 1h 19m (9:25 PM)[0m
[90m7d[0m [32m[----------] 6%[0m [90mresets in 6d 8h (Sat 4:15 AM)[0m
=== run 2 (warm cache) ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [33m[######----] 63%[0m [90m|[0m [90mSonnet 5[0m 21.4M
[90m5h[0m [32m[#---------] 18%[0m [36m[==========>...][0m [90m3h 40m/5h[0m [90mresets 1h 19m (9:25 PM)[0m
[90m7d[0m [32m[----------] 6%[0m [90mresets in 6d 8h (Sat 4:15 AM)[0m
```
- `Read` -- `C:\Users\Anant Gupta\.claude\statusline.sh`
- `Write` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | per-model tokens burnt
# then a merged 5-hour usage+rolling-timeline line, then a 7-day weekly line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# Per-model token totals come from parsing transcript_path (the session's own
# JSONL transcript), since Claude Code's context_window object only reports the
# *live* window, not a cumulative session total, and the context limit differs
# per model. The parse result is cached per session_id and only recomputed when
# the transcript file's mtime moves forward, so idle refreshInterval ticks don't
# re-parse a multi-MB file for no reason.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1.2M" / "884.0k" / "42"
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fM", n/1000000}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{printf "%.1fk", n/1000}' 2>/dev/null || printf '%dk' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# "[REDACTED]" -> "Haiku 4.5", "claude-sonnet-5" -> "Sonnet 5"
pretty_model() {
  local id=$1
  id=${id#claude-}
  id=$(printf '%s' "$id" | sed -E 's/-[0-9]{8}$//')
  local family=${id%%-*}
  local rest=""
  [ "$family" != "$id" ] && rest=${id#*-}
  family="$(printf '%s' "${family:0:1}" | tr '[:lower:]' '[:upper:]')${family:1}"
  if [ -n "$rest" ]; then
    printf '%s %s' "$family" "$(printf '%s' "$rest" | tr '-' '.')"
  else
    printf '%s' "$family"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# --- per-model cumulative tokens burnt this session, read from the transcript
# and cached until the transcript file actually grows ---
tokens_str=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.tsv"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      map(select(.type=="assistant" and .message.usage != null)
          | {model: .message.model,
             tok: ((.message.usage.input_tokens // 0)
                 + (.message.usage.output_tokens // 0)
                 + (.message.usage.cache_creation_input_tokens // 0)
                 + (.message.usage.cache_read_input_tokens // 0))})
      | group_by(.model)
      | map({model: .[0].model, total: (map(.tok) | add)})
      | sort_by(-.total)
      | .[]
      | "\(.model)\t\(.total)"
    ' "$transcript_path" 2>/dev/null | tr -d '\r' > "$cache_file"
  fi

  while IFS=$'\t' read -r mdl tot; do
    [ -z "$mdl" ] && continue
    tot=${tot%$'\r'}
    pretty=$(pretty_model "$mdl")
    ftot=$(fmt_tokens "$tot")
    tokens_str="${tokens_str}${tokens_str:+ ${GRAY}·${RESET} }${GRAY}${pretty}${RESET} ${ftot}"
  done < "$cache_file"
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"

```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "chmod +x ~/.claude/statusline.sh && ls -la ~/.claude/statusline.sh"`
```
-rwxr-xr-x 1 anant_gupta anant_gupta 10528 Jul 25 18:37 /home/anant_gupta/.claude/statusline.sh
```
- `Bash` -- `rm -f "/tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "rm -f /tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv; bash ~/.claude/statusline.sh < '$DIR/case1.json' 2>&1 || echo 'no case1.json (already cleaned) - using case_real.json'; echo ---; bash ~/.claude/statusline.sh < '$DIR/case_real.json'"`
```
no case1.json (already cleaned) - using case_real.json
---
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90mHaiku 4.5[0m 884.0k [90m·[0m [90mSonnet 5[0m 709.1k
[90m5h[0m [32m[----------] 2%[0m [36m[==========>...][0m [90m3h 42m/5h[0m [90mresets 1h 17m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 8h (Sat 2:45 AM)[0m
```
- `Bash` -- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case1.json,case2.json,case3.json,case_real.json,case_nodata.json,case_red.json,case_win.json,test_tokens.sh,run_real.sh,run_real2.sh,run_edge.sh}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`
```
done
```

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

### Tool Calls

- `Bash` -- `echo "=== Windows Jarvis project memory dir ==="
ls -la "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/memory/" 2>&1 | head -30
echo
echo "=== contents of MEMORY.md if present there vs the one referenced in system prompt ==="
find "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/memory/" -maxdepth 1 -type f 2>&1 | head -30`
```
=== Windows Jarvis project memory dir ===
total 140
drwxr-xr-x 1 Anant Gupta 197121    0 Jul  8 21:11 .
drwxr-xr-x 1 Anant Gupta 197121    0 Jul 25 19:07 ..
-rw-r--r-- 1 Anant Gupta 197121 2380 Jul  5 18:23 feedback_permission_classifier_infra_changes.md
-rw-r--r-- 1 Anant Gupta 197121 1570 Jul  5 18:04 feedback_templater_literal_syntax.md
-rw-r--r-- 1 Anant Gupta 197121 4290 Jul  5 18:04 feedback_vault_note_writing.md
-rw-r--r-- 1 Anant Gupta 197121 2312 Jul  5 18:55 feedback_verify_dont_assume_powershell.md
-rw-r--r-- 1 Anant Gupta 197121 5562 Jul  8 21:12 maverick_skills_github_analysis.md
-rw-r--r-- 1 Anant Gupta 197121 1470 Jul  5 18:56 MEMORY.md
-rw-r--r-- 1 Anant Gupta 197121 5723 Jul  5 18:55 project_ai_conversation_archive.md
-rw-r--r-- 1 Anant Gupta 197121 2946 Jul  5 21:09 project_certification_strategy.md
-rw-r--r-- 1 Anant Gupta 197121 5405 Jul  5 23:10 project_deepthinksfinance_proof_testing.md
-rw-r--r-- 1 Anant Gupta 197121 4977 Jul  5 18:04 project_jarvis_dashboard_session.md
-rw-r--r-- 1 Anant Gupta 197121 6525 Jul  5 23:11 project_knowledge_gathering_automation.md
-rw-r--r-- 1 Anant Gupta 197121 6456 Jul  5 22:48 project_model_distillation_research.md
-rw-r--r-- 1 Anant Gupta 197121 5446 Jul  5 23:24 project_skill_implementation_audit.md
-rw-r--r-- 1 Anant Gupta 197121 5452 Jul  5 22:18 project_trading_bot_architecture.md
-rw-r--r-- 1 Anant Gupta 197121 3858 Jul  8 20:48 tool_gitnexus_vs_graphify.md

=== contents of MEMORY.md if present there vs the one referenced in system prompt ===
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/feedback_permission_classifier_infra_changes.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/feedback_templater_literal_syntax.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/feedback_vault_note_writing.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/feedback_verify_dont_assume_powershell.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/maverick_skills_github_analysis.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/MEMORY.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_ai_conversation_archive.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_certification_strategy.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_deepthinksfinance_proof_testing.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_jarvis_dashboard_session.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_knowledge_gathering_automation.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_model_distillation_research.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_skill_implementation_audit.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/project_trading_bot_architecture.md
/c/Users/Anant Gupta/.claude/projects/[REDACTED]/memory/tool_gitnexus_vs_graphify.md
```
- `Bash` -- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/ 2>&1; echo '---jarvis-equivalent (home dir) memory dir if any---'; ls -la ~/.claude/projects/-home-anant-gupta/memory/ 2>&1"`
```
total 16
drwxr-xr-x 2 anant_gupta anant_gupta 4096 Jul 18 18:25 .
drwxr-xr-x 5 anant_gupta anant_gupta 4096 Jul 25 10:30 ..
-rw-r--r-- 1 anant_gupta anant_gupta  170 Jul 18 10:55 MEMORY.md
-rw-r--r-- 1 anant_gupta anant_gupta 3185 Jul 18 18:25 phase4-state-and-gates.md
---jarvis-equivalent (home dir) memory dir if any---
total 32
drwxr-xr-x 2 anant_gupta anant_gupta 4096 May 27 15:49 .
drwxr-xr-x 3 anant_gupta anant_gupta 4096 Jul  8 12:46 ..
-rw-r--r-- 1 anant_gupta anant_gupta  446 May 27 14:45 MEMORY.md
-rw-r--r-- 1 anant_gupta anant_gupta 1058 May 27 14:46 feedback_code_config.md
-rw-r--r-- 1 anant_gupta anant_gupta 1741 May 27 14:46 feedback_working_style.md
-rw-r--r-- 1 anant_gupta anant_gupta 2131 May 27 15:49 project_active.md
-rw-r--r-- 1 anant_gupta anant_gupta 1999 May 27 15:49 reference_tools.md
-rw-r--r-- 1 anant_gupta anant_gupta 1698 May 27 15:48 user_profile.md
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | tokens burnt
# then a merged 5-hour usage+rolling-timeline line, a 7-day weekly line, and a
# per-project memory-store summary line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# The tokens segment shows two numbers: the cumulative total burnt this session
# (summed across every model call in transcript_path, since context_window only
# reports the *live* window, not a running total) and, in parentheses, the live
# context window's absolute token count against its actual per-model ceiling
# (context_window.total_input_tokens / context_window.context_window_size - the
# exact numerator/denominator Claude Code itself divides to get used_percentage,
# so this can't drift from the ctx bar or the app either).
#
# The memory line reads <project-dir>/memory/ (sibling of the transcript files)
# - Claude Code's per-project persistent memory store - and reports how many
# notes it holds, their combined size, and how long ago the most recent one was
# touched. It is per *project*, not per conversation: every session opened in
# this same project directory shares one memory store.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
ctx_live=$(printf '%s' "$input" | jq -r '.context_window.total_input_tokens // empty' 2>/dev/null)
ctx_size=$(printf '%s' "$input" | jq -r '.context_window.context_window_size // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1M" / "23.9M" / "235.6K" / "42" (no trailing .0 on whole units)
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{v=n/1000000; if (v==int(v)) printf "%dM", v; else printf "%.1fM", v}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{v=n/1000; if (v==int(v)) printf "%dK", v; else printf "%.1fK", v}' 2>/dev/null || printf '%dK' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# bytes (int) -> "42.6KB" / "1.2MB" / "512B"
fmt_bytes() {
  local b=$1
  if [ "$b" -ge 1048576 ]; then
    awk -v n="$b" 'BEGIN{v=n/1048576; if (v==int(v)) printf "%dMB", v; else printf "%.1fMB", v}' 2>/dev/null || printf '%dMB' $((b / 1048576))
  elif [ "$b" -ge 1024 ]; then
    awk -v n="$b" 'BEGIN{v=n/1024; if (v==int(v)) printf "%dKB", v; else printf "%.1fKB", v}' 2>/dev/null || printf '%dKB' $((b / 1024))
  else
    printf '%dB' "$b"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# live/max absolute token counts - the same numerator/denominator Claude Code
# itself divides to produce context_window.used_percentage above
live_fmt=""
if [ -n "$ctx_live" ] && [ "$ctx_live" != "null" ] && [ -n "$ctx_size" ] && [ "$ctx_size" != "null" ]; then
  live_fmt=$(fmt_tokens "$(printf '%.0f' "$ctx_live" 2>/dev/null || echo 0)")
  max_fmt=$(fmt_tokens "$(printf '%.0f' "$ctx_size" 2>/dev/null || echo 0)")
fi

# --- cumulative tokens burnt this session (summed across every model call in
# the transcript), cached until the transcript file actually grows ---
cum_total=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.total"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      [ .[] | select(.type=="assistant" and .message.usage != null)
        | ((.message.usage.input_tokens // 0)
         + (.message.usage.output_tokens // 0)
         + (.message.usage.cache_creation_input_tokens // 0)
         + (.message.usage.cache_read_input_tokens // 0)) ]
      | add // 0
    ' "$transcript_path" 2>/dev/null | tr -d '\r' > "$cache_file"
  fi

  cum_total=$(cat "$cache_file" 2>/dev/null)
  cum_total=${cum_total%$'\r'}
fi
[ -z "$cum_total" ] && cum_total=0

tokens_str=""
if [ "$cum_total" != "0" ] || [ -n "$live_fmt" ]; then
  cum_fmt=$(fmt_tokens "$cum_total")
  tokens_str="${GRAY}${cum_fmt}${RESET}"
  [ -n "$live_fmt" ] && tokens_str="${tokens_str} ${GRAY}(${live_fmt}/${max_fmt}) tokens${RESET}"
fi

# --- per-project memory store summary (Claude Code's persistent memory files,
# living at <project-dir>/memory/ next to the session transcripts - shared by
# every session opened in this same project, not scoped to just this one) ---
mem_str=""
if [ -n "$transcript_path" ]; then
  memory_dir="$(dirname "$transcript_path")/memory"
  if [ -d "$memory_dir" ]; then
    mem_count=0
    mem_bytes=0
    mem_latest=0
    for f in "$memory_dir"/*.md; do
      [ -e "$f" ] || continue
      [ "$(basename "$f")" = "MEMORY.md" ] && continue
      mem_count=$((mem_count + 1))
      fsize=$(stat -c %s "$f" 2>/dev/null || stat -f %z "$f" 2>/dev/null || echo 0)
      mem_bytes=$((mem_bytes + fsize))
      fmtime=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null || echo 0)
      [ "$fmtime" -gt "$mem_latest" ] 2>/dev/null && mem_latest=$fmtime
    done

    if [ "$mem_count" -gt 0 ]; then
      mem_size_fmt=$(fmt_bytes "$mem_bytes")
      mem_ago_s=$((now - mem_latest))
      if [ "$mem_ago_s" -lt 60 ]; then
        mem_ago="just now"
      else
        mem_ago="$(fmt_duration "$mem_ago_s") ago"
      fi
      noun="notes"
      [ "$mem_count" -eq 1 ] && noun="note"
      mem_str="${GRAY}mem${RESET} ${mem_count} ${noun} ${GRAY}·${RESET} ${mem_size_fmt} ${GRAY}· updated ${mem_ago}${RESET}"
    fi
  fi
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"
[ -n "$mem_str" ] && printf '%s\n' "$mem_str"

```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win2.json`
```
{"cwd":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis","session_id":"[REDACTED]","transcript_path":"C:\\Users\\Anant Gupta\\.claude\\projects\\[REDACTED]\\[REDACTED].jsonl","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"},"context_window":{"used_percentage":23,"total_input_tokens":235600,"context_window_size":1000000},"rate_limits":{"five_hour":{"used_percentage":64,"resets_at":1785008430},"seven_day":{"used_percentage":7,"resets_at":1785537930}}}

```
- `Bash` -- `rm -rf /tmp/claude-statusline-tokens
DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
chmod +x "$DIR/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"
echo "=== run 2 (warm cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"`
```
=== run 1 (cold cache) ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[##--------] 23%[0m [90m|[0m [90m26.6M[0m [90m(235.6K/1M) tokens[0m
[90m5h[0m [33m[######----] 64%[0m [36m[>.............][0m [90m16m/5h[0m [90mresets 4h 43m (1:10 AM)[0m
[90m7d[0m [32m[----------] 7%[0m [90mresets in 6d 7h (Sat 4:15 AM)[0m
[90mmem[0m 14 notes [90m·[0m 61.4KB [90m· updated 16d 23h ago[0m
=== run 2 (warm cache) ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[##--------] 23%[0m [90m|[0m [90m26.6M[0m [90m(235.6K/1M) tokens[0m
[90m5h[0m [33m[######----] 64%[0m [36m[>.............][0m [90m16m/5h[0m [90mresets 4h 43m (1:10 AM)[0m
[90m7d[0m [32m[----------] 7%[0m [90mresets in 6d 7h (Sat 4:15 AM)[0m
[90mmem[0m 14 notes [90m·[0m 61.4KB [90m· updated 16d 23h ago[0m
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_nometa.json`
```
{"cwd":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"},"context_window":{"used_percentage":null}}

```
- `Bash` -- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "=== no transcript, no rate_limits, null ctx ==="
bash "$DIR/statusline.sh" < "$DIR/case_nometa.json"`
```
Exit code 1
=== no transcript, no rate_limits, null ctx ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx [no data yet][0m
[90m5h [warming up - appears after first message][0m
[90m7d [no weekly limit data][0m
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Edit` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
```diff
- printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"
[ -n "$mem_str" ] && printf '%s\n' "$mem_str"
+ printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"
[ -n "$mem_str" ] && printf '%s\n' "$mem_str"
exit 0
```
- `Bash` -- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "=== no transcript, no rate_limits, null ctx ==="
bash "$DIR/statusline.sh" < "$DIR/case_nometa.json"
echo "exit code: $?"
echo
echo "=== real fixture again (cold cache after clearing) ==="
rm -rf /tmp/claude-statusline-tokens
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"
echo "exit code: $?"`
```
=== no transcript, no rate_limits, null ctx ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx [no data yet][0m
[90m5h [warming up - appears after first message][0m
[90m7d [no weekly limit data][0m
exit code: 0

=== real fixture again (cold cache after clearing) ===
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[##--------] 23%[0m [90m|[0m [90m29.2M[0m [90m(235.6K/1M) tokens[0m
[90m5h[0m [33m[######----] 64%[0m [36m[>.............][0m [90m18m/5h[0m [90mresets 4h 41m (1:10 AM)[0m
[90m7d[0m [32m[----------] 7%[0m [90mresets in 6d 7h (Sat 4:15 AM)[0m
[90mmem[0m 14 notes [90m·[0m 61.4KB [90m· updated 16d 23h ago[0m
exit code: 0
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win_red.json`
```
{"cwd":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis","session_id":"[REDACTED]","transcript_path":"C:\\Users\\Anant Gupta\\.claude\\projects\\[REDACTED]\\[REDACTED].jsonl","model":{"display_name":"Opus"},"workspace":{"current_dir":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"},"context_window":{"used_percentage":94,"total_input_tokens":188000,"context_window_size":200000},"rate_limits":{"five_hour":{"used_percentage":97,"resets_at":1784987490},"seven_day":{"used_percentage":88,"resets_at":1785008490}}}

```
- `Bash` -- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
bash "$DIR/statusline.sh" < "$DIR/case_win_red.json"
echo "exit code: $?"`
```
[36mJarvis[0m [90m|[0m [35mmaster[0m [90m|[0m [34mOpus[0m [90m|[0m [90mctx[0m [31m[#########-] 94%[0m [31m[1m![0m [90m|[0m [90m29.7M[0m [90m(188K/200K) tokens[0m
[90m5h[0m [31m[#########-] 97%[0m [31m[1m![0m [36m[=============>][0m [90m5h 0m/5h[0m [90mresets 0m (7:21 PM)[0m
[90m7d[0m [31m[########--] 88%[0m [31m[1m![0m [90mresets in 4h 42m (Sun 1:11 AM)[0m
[90mmem[0m 14 notes [90m·[0m 61.4KB [90m· updated 16d 23h ago[0m
exit code: 0
```
- `Read` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `Bash` -- `SRC="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"
cp "$SRC" "/c/Users/Anant Gupta/.claude/statusline.sh"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
echo "Windows deployed:"
diff "$SRC" "/c/Users/Anant Gupta/.claude/statusline.sh" && echo "identical"`
```
Windows deployed:
identical
```
- `Write` -- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
```
#!/usr/bin/env bash
# Claude Code status line: folder | git branch | model | context bar | tokens burnt
# then a merged 5-hour usage+rolling-timeline line, a 7-day weekly line, and a
# per-project memory-store summary line.
# Reads session JSON from stdin (see Claude Code statusLine docs). Dependency: jq.
#
# All rate-limit math reads rate_limits.*.used_percentage / resets_at directly -
# the same numbers the Claude app's own usage page reads - with no client-side
# recalculation, so the percentages here can never drift from the app.
#
# The tokens segment shows two numbers: the cumulative total burnt this session
# (summed across every model call in transcript_path, since context_window only
# reports the *live* window, not a running total) and, in parentheses, the live
# context window's absolute token count against its actual per-model ceiling
# (context_window.total_input_tokens / context_window.context_window_size - the
# exact numerator/denominator Claude Code itself divides to get used_percentage,
# so this can't drift from the ctx bar or the app either).
#
# The memory line reads <project-dir>/memory/ (sibling of the transcript files)
# - Claude Code's per-project persistent memory store - and reports how many
# notes it holds, their combined size, and how long ago the most recent one was
# touched. It is per *project*, not per conversation: every session opened in
# this same project directory shares one memory store.

input=$(cat)

# --- colors (raw ANSI escapes, no -e needed) ---
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
BLUE=$'\033[34m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
GRAY=$'\033[90m'

# --- extract fields from stdin JSON ---
cwd=$(printf '%s' "$input" | jq -r '.workspace.current_dir // .cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"
folder=$(basename "${cwd//\\//}")

model=$(printf '%s' "$input" | jq -r '.model.display_name // .model.id // "unknown"' 2>/dev/null)
[ -z "$model" ] && model="unknown"

ctx_pct=$(printf '%s' "$input" | jq -r '.context_window.used_percentage // empty' 2>/dev/null)
ctx_live=$(printf '%s' "$input" | jq -r '.context_window.total_input_tokens // empty' 2>/dev/null)
ctx_size=$(printf '%s' "$input" | jq -r '.context_window.context_window_size // empty' 2>/dev/null)
five_pct=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty' 2>/dev/null)
five_reset=$(printf '%s' "$input" | jq -r '.rate_limits.five_hour.resets_at // empty' 2>/dev/null)
week_pct=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty' 2>/dev/null)
week_reset=$(printf '%s' "$input" | jq -r '.rate_limits.seven_day.resets_at // empty' 2>/dev/null)
session_id=$(printf '%s' "$input" | jq -r '.session_id // empty' 2>/dev/null)
transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)

# --- git branch (fast, never hangs, silent outside a repo) ---
branch=""
if git -C "$cwd" --no-optional-locks rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks branch --show-current 2>/dev/null)
  if [ -z "$branch" ]; then
    branch=$(git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
    [ -n "$branch" ] && branch="detached:${branch}"
  fi
fi

# --- helpers ---
bar_width=10

# builds a two-tone bar: $1 filled count, $2 width, $3 fill-char, $4 empty-char
render_bar() {
  local filled=$1 width=$2 fillchar=$3 emptychar=$4 i bar=""
  [ "$filled" -gt "$width" ] && filled=$width
  [ "$filled" -lt 0 ] && filled=0
  local empty=$((width - filled))
  for ((i = 0; i < filled; i++)); do bar="${bar}${fillchar}"; done
  for ((i = 0; i < empty; i++)); do bar="${bar}${emptychar}"; done
  printf '%s' "$bar"
}

# thresholds shared by ctx/5h/7d usage bars
color_for_pct() {
  local pct=$1
  if [ "$pct" -ge 70 ]; then printf '%s' "$RED"
  elif [ "$pct" -ge 40 ]; then printf '%s' "$YELLOW"
  else printf '%s' "$GREEN"
  fi
}

# seconds -> "Xd Yh" / "Xh Ym" / "Xm" (always hour+minute granularity, never bare seconds)
fmt_duration() {
  local s=$1
  [ "$s" -lt 0 ] && s=0
  local d=$((s / 86400))
  local h=$(((s % 86400) / 3600))
  local m=$(((s % 3600) / 60))
  if [ "$d" -gt 0 ]; then
    printf '%dd %dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then
    printf '%dh %dm' "$h" "$m"
  else
    printf '%dm' "$m"
  fi
}

# tokens (int) -> "1M" / "23.9M" / "235.6K" / "42" (no trailing .0 on whole units)
fmt_tokens() {
  local n=$1
  if [ "$n" -ge 1000000 ]; then
    awk -v n="$n" 'BEGIN{v=n/1000000; if (v==int(v)) printf "%dM", v; else printf "%.1fM", v}' 2>/dev/null || printf '%dM' $((n / 1000000))
  elif [ "$n" -ge 1000 ]; then
    awk -v n="$n" 'BEGIN{v=n/1000; if (v==int(v)) printf "%dK", v; else printf "%.1fK", v}' 2>/dev/null || printf '%dK' $((n / 1000))
  else
    printf '%d' "$n"
  fi
}

# bytes (int) -> "42.6KB" / "1.2MB" / "512B"
fmt_bytes() {
  local b=$1
  if [ "$b" -ge 1048576 ]; then
    awk -v n="$b" 'BEGIN{v=n/1048576; if (v==int(v)) printf "%dMB", v; else printf "%.1fMB", v}' 2>/dev/null || printf '%dMB' $((b / 1048576))
  elif [ "$b" -ge 1024 ]; then
    awk -v n="$b" 'BEGIN{v=n/1024; if (v==int(v)) printf "%dKB", v; else printf "%.1fKB", v}' 2>/dev/null || printf '%dKB' $((b / 1024))
  else
    printf '%dB' "$b"
  fi
}

now=$(date +%s)

# --- context usage progress bar (freshest number in the whole status line:
# Claude Code recomputes context_window from the live token count on every new
# assistant message, so this always reflects the last prompt/response exactly) ---
if [ -n "$ctx_pct" ] && [ "$ctx_pct" != "null" ]; then
  pct_int=$(printf '%.0f' "$ctx_pct" 2>/dev/null || echo 0)
  [ "$pct_int" -lt 0 ] 2>/dev/null && pct_int=0
  [ "$pct_int" -gt 100 ] 2>/dev/null && pct_int=100

  bar_color=$(color_for_pct "$pct_int")
  filled=$((pct_int * bar_width / 100))
  bar=$(render_bar "$filled" "$bar_width" "#" "-")

  ctx_str="${GRAY}ctx${RESET} ${bar_color}[${bar}] ${pct_int}%${RESET}"
  [ "$pct_int" -ge 70 ] && ctx_str="${ctx_str} ${RED}${BOLD}!${RESET}"
else
  ctx_str="${GRAY}ctx [no data yet]${RESET}"
fi

# live/max absolute token counts - the same numerator/denominator Claude Code
# itself divides to produce context_window.used_percentage above
live_fmt=""
if [ -n "$ctx_live" ] && [ "$ctx_live" != "null" ] && [ -n "$ctx_size" ] && [ "$ctx_size" != "null" ]; then
  live_fmt=$(fmt_tokens "$(printf '%.0f' "$ctx_live" 2>/dev/null || echo 0)")
  max_fmt=$(fmt_tokens "$(printf '%.0f' "$ctx_size" 2>/dev/null || echo 0)")
fi

# --- cumulative tokens burnt this session (summed across every model call in
# the transcript), cached until the transcript file actually grows ---
cum_total=""
if [ -n "$transcript_path" ] && [ -f "$transcript_path" ] && [ -n "$session_id" ]; then
  cache_dir="${TMPDIR:-/tmp}/claude-statusline-tokens"
  mkdir -p "$cache_dir" 2>/dev/null
  cache_file="$cache_dir/${session_id}.total"

  src_mtime=$(stat -c %Y "$transcript_path" 2>/dev/null || stat -f %m "$transcript_path" 2>/dev/null || echo 0)
  cache_mtime=0
  [ -f "$cache_file" ] && cache_mtime=$(stat -c %Y "$cache_file" 2>/dev/null || stat -f %m "$cache_file" 2>/dev/null || echo 0)

  if [ "$src_mtime" -gt "$cache_mtime" ] 2>/dev/null || [ ! -s "$cache_file" ]; then
    jq -r -s '
      [ .[] | select(.type=="assistant" and .message.usage != null)
        | ((.message.usage.input_tokens // 0)
         + (.message.usage.output_tokens // 0)
         + (.message.usage.cache_creation_input_tokens // 0)
         + (.message.usage.cache_read_input_tokens // 0)) ]
      | add // 0
    ' "$transcript_path" 2>/dev/null | tr -d '\r' > "$cache_file"
  fi

  cum_total=$(cat "$cache_file" 2>/dev/null)
  cum_total=${cum_total%$'\r'}
fi
[ -z "$cum_total" ] && cum_total=0

tokens_str=""
if [ "$cum_total" != "0" ] || [ -n "$live_fmt" ]; then
  cum_fmt=$(fmt_tokens "$cum_total")
  tokens_str="${GRAY}${cum_fmt}${RESET}"
  [ -n "$live_fmt" ] && tokens_str="${tokens_str} ${GRAY}(${live_fmt}/${max_fmt}) tokens${RESET}"
fi

# --- per-project memory store summary (Claude Code's persistent memory files,
# living at <project-dir>/memory/ next to the session transcripts - shared by
# every session opened in this same project, not scoped to just this one) ---
mem_str=""
if [ -n "$transcript_path" ]; then
  memory_dir="$(dirname "$transcript_path")/memory"
  if [ -d "$memory_dir" ]; then
    mem_count=0
    mem_bytes=0
    mem_latest=0
    for f in "$memory_dir"/*.md; do
      [ -e "$f" ] || continue
      [ "$(basename "$f")" = "MEMORY.md" ] && continue
      mem_count=$((mem_count + 1))
      fsize=$(stat -c %s "$f" 2>/dev/null || stat -f %z "$f" 2>/dev/null || echo 0)
      mem_bytes=$((mem_bytes + fsize))
      fmtime=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null || echo 0)
      [ "$fmtime" -gt "$mem_latest" ] 2>/dev/null && mem_latest=$fmtime
    done

    if [ "$mem_count" -gt 0 ]; then
      mem_size_fmt=$(fmt_bytes "$mem_bytes")
      mem_ago_s=$((now - mem_latest))
      if [ "$mem_ago_s" -lt 60 ]; then
        mem_ago="just now"
      else
        mem_ago="$(fmt_duration "$mem_ago_s") ago"
      fi
      noun="notes"
      [ "$mem_count" -eq 1 ] && noun="note"
      mem_str="${GRAY}mem${RESET} ${mem_count} ${noun} ${GRAY}·${RESET} ${mem_size_fmt} ${GRAY}· updated ${mem_ago}${RESET}"
    fi
  fi
fi

# --- 5-hour session usage + rolling timeline, one line (this is the number the
# Claude app calls "current session" on the usage page -
# rate_limits.five_hour.used_percentage, shown unmodified so it can't drift
# from the app) ---
if [ -n "$five_pct" ] && [ "$five_pct" != "null" ]; then
  fpct_int=$(printf '%.0f' "$five_pct" 2>/dev/null || echo 0)
  [ "$fpct_int" -lt 0 ] 2>/dev/null && fpct_int=0
  [ "$fpct_int" -gt 100 ] 2>/dev/null && fpct_int=100

  five_color=$(color_for_pct "$fpct_int")
  ffilled=$((fpct_int * bar_width / 100))
  fbar=$(render_bar "$ffilled" "$bar_width" "#" "-")

  five_str="${GRAY}5h${RESET} ${five_color}[${fbar}] ${fpct_int}%${RESET}"
  [ "$fpct_int" -ge 70 ] && five_str="${five_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$five_reset" ] && [ "$five_reset" != "null" ]; then
    five_reset_i=$(printf '%.0f' "$five_reset" 2>/dev/null || echo 0)
    remaining=$((five_reset_i - now))
    countdown=$(fmt_duration "$remaining")
    clock=$(date -d "@${five_reset_i}" +'%-I:%M %p' 2>/dev/null)

    # rolling timeline: where "now" sits inside the current 5h window. The
    # window is exactly 5h wide and always ends at five_reset_i, so its start
    # is derivable even though Claude Code doesn't send it directly.
    window_secs=$((5 * 3600))
    window_start=$((five_reset_i - window_secs))
    elapsed=$((now - window_start))
    [ "$elapsed" -lt 0 ] && elapsed=0
    [ "$elapsed" -gt "$window_secs" ] && elapsed=$window_secs

    timeline_width=14
    tfilled=$((elapsed * timeline_width / window_secs))
    tbar=$(render_bar "$tfilled" "$timeline_width" "=" ".")
    marker_pos=$tfilled
    [ "$marker_pos" -ge "$timeline_width" ] && marker_pos=$((timeline_width - 1))
    tbar="${tbar:0:marker_pos}>${tbar:marker_pos+1}"
    elapsed_str=$(fmt_duration "$elapsed")

    five_str="${five_str} ${CYAN}[${tbar}]${RESET} ${GRAY}${elapsed_str}/5h${RESET}"
    if [ -n "$clock" ]; then
      five_str="${five_str} ${GRAY}resets ${countdown} (${clock})${RESET}"
    else
      five_str="${five_str} ${GRAY}resets ${countdown}${RESET}"
    fi
  fi
else
  five_str="${GRAY}5h [warming up - appears after first message]${RESET}"
fi

# --- 7-day weekly usage bar (Pro/Max only; absent otherwise) ---
if [ -n "$week_pct" ] && [ "$week_pct" != "null" ]; then
  wpct_int=$(printf '%.0f' "$week_pct" 2>/dev/null || echo 0)
  [ "$wpct_int" -lt 0 ] 2>/dev/null && wpct_int=0
  [ "$wpct_int" -gt 100 ] 2>/dev/null && wpct_int=100

  week_color=$(color_for_pct "$wpct_int")
  wfilled=$((wpct_int * bar_width / 100))
  wbar=$(render_bar "$wfilled" "$bar_width" "#" "-")

  week_str="${GRAY}7d${RESET} ${week_color}[${wbar}] ${wpct_int}%${RESET}"
  [ "$wpct_int" -ge 70 ] && week_str="${week_str} ${RED}${BOLD}!${RESET}"

  if [ -n "$week_reset" ] && [ "$week_reset" != "null" ]; then
    week_reset_i=$(printf '%.0f' "$week_reset" 2>/dev/null || echo 0)
    wremaining=$((week_reset_i - now))
    wcountdown=$(fmt_duration "$wremaining")
    wclock=$(date -d "@${week_reset_i}" +'%a %-I:%M %p' 2>/dev/null)
    if [ -n "$wclock" ]; then
      week_str="${week_str} ${GRAY}resets in ${wcountdown} (${wclock})${RESET}"
    else
      week_str="${week_str} ${GRAY}resets in ${wcountdown}${RESET}"
    fi
  fi
else
  week_str="${GRAY}7d [no weekly limit data]${RESET}"
fi

# --- assemble output (multi-line) ---
sep=" ${GRAY}|${RESET} "

line1="${CYAN}${folder}${RESET}"
if [ -n "$branch" ]; then
  line1="${line1}${sep}${MAGENTA}${branch}${RESET}"
fi
line1="${line1}${sep}${BLUE}${model}${RESET}${sep}${ctx_str}"
[ -n "$tokens_str" ] && line1="${line1}${sep}${tokens_str}"

printf '%s\n' "$line1"
printf '%s\n' "$five_str"
printf '%s\n' "$week_str"
[ -n "$mem_str" ] && printf '%s\n' "$mem_str"
exit 0

```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "chmod +x ~/.claude/statusline.sh && ls -la ~/.claude/statusline.sh"`
```
-rwxr-xr-x 1 anant_gupta anant_gupta 13023 Jul 25 19:00 /home/anant_gupta/.claude/statusline.sh
```
- `Write` -- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_wsl2.json`
```
{"cwd":"/home/anant_gupta/projects/work/internship-research-loop","session_id":"[REDACTED]","transcript_path":"/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED].jsonl","model":{"display_name":"Sonnet 5"},"workspace":{"current_dir":"/home/anant_gupta/projects/work/internship-research-loop"},"context_window":{"used_percentage":8,"total_input_tokens":15680,"context_window_size":200000},"rate_limits":{"five_hour":{"used_percentage":2,"resets_at":1784994930},"seven_day":{"used_percentage":0,"resets_at":1785537930}}}

```
- `Bash` -- `wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case_wsl2.json'; echo EXIT:\$?"`
```
[[REDACTED][0m [90m|[0m [35mmaster[0m [90m|[0m [34mSonnet 5[0m [90m|[0m [90mctx[0m [32m[----------] 8%[0m [90m|[0m [90m1.6M[0m [90m(15.7K/200K) tokens[0m
[90m5h[0m [32m[----------] 2%[0m [36m[===========>..][0m [90m4h 6m/5h[0m [90mresets 53m (7:55 PM)[0m
[90m7d[0m [32m[----------] 0%[0m [90mresets in 6d 7h (Sat 2:45 AM)[0m
[90mmem[0m 1 note [90m·[0m 3.1KB [90m· updated 7d 0h ago[0m
EXIT:0
```
- `Bash` -- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case_win.json,case_win2.json,case_win_red.json,case_nometa.json,case_nodata.json,case_wsl2.json}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`
```
done
```

## Actions Taken

**Files created:**
- `//wsl$/Ubuntu/home/anant_gupta/.claude/statusline.sh`
- `C:\Users\Anant Gupta\.claude\statusline.sh`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_nodata.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_nometa.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_real.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_red.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win_red.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_win2.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case_wsl2.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case1.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case2.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case3.json`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_edge.sh`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_real.sh`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\run_real2.sh`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh`
- `C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\test_tokens.sh`

**Files modified:**
- `//wsl$/Ubuntu/home/anant_gupta/.claude/settings.json`
- `C:\Users\Anant Gupta\.claude\settings.json`

**Files deleted (heuristic, from Bash commands):**
- `rm -f "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case1.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case2.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case3.json" 2>&1
echo done`
- `rm -rf /tmp/claude-statusline-tokens
cp "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh" "/c/Users/Anant Gupta/.claude/statusline.sh"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"
echo "=== run 2 (warm cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"`
- `rm -f "/tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "rm -f /tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv; bash ~/.claude/statusline.sh < '$DIR/case1.json' 2>&1 || echo 'no case1.json (already cleaned) - using case_real.json'; echo ---; bash ~/.claude/statusline.sh < '$DIR/case_real.json'"`
- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case1.json,case2.json,case3.json,case_real.json,case_nodata.json,case_red.json,case_win.json,test_tokens.sh,run_real.sh,run_real2.sh,run_edge.sh}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`
- `rm -rf /tmp/claude-statusline-tokens
DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
chmod +x "$DIR/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"
echo "=== run 2 (warm cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"`
- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case_win.json,case_win2.json,case_win_red.json,case_nometa.json,case_nodata.json,case_wsl2.json}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`

**Commands run:**
- `ls -la "//wsl$/Ubuntu/home/anant_gupta/" 2>&1 | head -50`
- `ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/" 2>&1`
- `ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/debug/" 2>&1
echo "---"
ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/session-data/" 2>&1
echo "---metrics---"
ls -la "//wsl$/Ubuntu/home/anant_gupta/.claude/metrics/" 2>&1`
- `wsl.exe -d Ubuntu -- bash -c 'echo ok && which jq && date' 2>&1`
- `wsl.exe -d Ubuntu -- bash -c "test -f '/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh' && echo FOUND || echo NOTFOUND"`
- `SCRIPT="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"
wsl.exe -d Ubuntu -- bash -c "chmod +x '$SCRIPT'"

echo "=== Case 1: normal mid-window, moderate usage ==="
wsl.exe -d Ubuntu -- bash -c '
now=$(date +%s)
five_reset=$((now + 2*3600 + 14*60))       # 2h14m from now -> window started 2h46m ago
week_reset=$((now + 3*86400 + 4*3600))     # 3d4h from now
json=$(jq -n --arg cwd "/home/anant_gupta/project" --argjson ctx 42 --argjson five 55.4 --argjson fr "$five_reset" --argjson week 23.1 --argjson wr "$week_reset" '"'"'
{cwd:$cwd, model:{display_name:"Sonnet 5"}, workspace:{current_dir:$cwd}, context_window:{used_percentage:$ctx}, rate_limits:{five_hour:{used_percentage:$five, resets_at:$fr}, seven_day:{used_percentage:$week, resets_at:$wr}}}
'"'"')
echo "$json" | bash '"$SCRIPT"'
' 2>&1`
- `wsl.exe -d Ubuntu -- bash -c 'date +%s'`
- `DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
SCRIPT="$DIR/statusline.sh"
for c in case1 case2 case3; do
  echo "=== $c ==="
  wsl.exe -d Ubuntu -- bash -c "bash '$SCRIPT' < '$DIR/$c.json'"
  echo
done`
- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/statusline.sh && chmod +x ~/.claude/statusline.sh && ls -la ~/.claude/statusline.sh"`
- `wsl.exe -d Ubuntu -- bash -c '
jq . ~/.claude/settings.json > /dev/null && echo "settings.json: valid JSON"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "--- deployed script, case1 fixture ---"
bash ~/.claude/statusline.sh < "$DIR/case1.json"
'`
- `wsl.exe -d Ubuntu -- bash -c "jq . ~/.claude/settings.json > /dev/null && echo 'settings.json: valid JSON'"`
- `DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case1.json'"
echo "--- case3 (high usage, near reset) ---"
wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case3.json'"`
- `rm -f "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case1.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case2.json" "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\case3.json" 2>&1
echo done`
- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/ | head -20"`
- `wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/ | tail -20"`
- `wsl.exe -d Ubuntu -- bash -c "tail -c 4000 ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | tail -5"`
- `wsl.exe -d Ubuntu -- bash -c "grep -o '\"type\":\"assistant\".\{0,50\}' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | head -3
echo '---model field search---'
grep -m1 -o '\"model\":\"[^\"]*\"' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl
echo '---full first assistant line structure (truncated)---'
grep -m1 '\"type\":\"assistant\"' ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl | head -c 1500"`
- `echo "jq: $(command -v jq || echo MISSING)"
echo "awk: $(command -v awk || echo MISSING)"
echo "stat: $(command -v stat || echo MISSING)"
date -d @1700000000 +'%-I:%M %p' 2>&1
echo "---"
uname -a
echo "---home---"
echo $HOME
ls -la "$HOME/.claude" 2>&1 | head -30`
- `python3 -c "
import json
d=json.load(open(r'C:\Users\Anant Gupta\.claude\settings.json'))
print(json.dumps(d.get('statusLine'), indent=2))
" 2>&1 || grep -A5 '"statusLine"' "/c/Users/Anant Gupta/.claude/settings.json"`
- `wsl.exe -d Ubuntu -- bash -c '
T=~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl
time jq -r -s "
  map(select(.type==\"assistant\" and .message.usage != null)
      | {model: .message.model,
         tok: ((.message.usage.input_tokens // 0)
             + (.message.usage.output_tokens // 0)
             + (.message.usage.cache_creation_input_tokens // 0)
             + (.message.usage.cache_read_input_tokens // 0))})
  | group_by(.model)
  | map({model: .[0].model, total: (map(.tok) | add)})
  | sort_by(-.total)
  | .[]
  | \"\(.model)\t\(.total)\"
" "$T"
'`
- `wsl.exe -d Ubuntu -- bash -c 'T=~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo "[$T]"; ls -la "$T"'`
- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo GOT:\$T; wc -l \"\$T\""`
- `wsl.exe -d Ubuntu -- bash -c "echo hello; echo HOME_IS:\$HOME"`
- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/156d5c7d-7e03-456a-8148-6da71f1883c6.jsonl; echo GOT:\$T"`
- `wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/settings.json; echo GOT:\$T"
echo "==="
wsl.exe -d Ubuntu -- bash -c "T=\$HOME/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop; echo GOT:\$T"`
- `wsl.exe -d Ubuntu -- bash -c "T=hello; echo GOT:\$T"`
- `wsl.exe -d Ubuntu -- bash -c "T=hello && echo GOT:\$T"
echo "---using printf script file---"
printf '%s\n' 'T=hello' 'echo "GOT2:$T"' > /tmp/wsltest.sh
wsl.exe -d Ubuntu -- bash /mnt/c/Users/*/AppData/Local/Temp/wsltest.sh 2>&1 || true
wsl.exe -d Ubuntu -- bash -c "cat /tmp/wsltest.sh 2>&1; bash /tmp/wsltest.sh 2>&1"`
- `wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/test_tokens.sh"`
- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/test_tokens.sh"`
- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_real.sh"`
- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_real2.sh"`
- `grep -n 'tokens_str:+' "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"`
- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash "/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/run_edge.sh"`
- `jq empty "/c/Users/Anant Gupta/.claude/settings.json" && echo "settings.json valid"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
ls -la "/c/Users/Anant Gupta/.claude/statusline.sh"`
- `ls "/c/Users/Anant Gupta/.claude/projects/" 2>&1 | head -20`
- `ls -la "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/" | tail -5`
- `ls -lat "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/"*.jsonl | head -3`
- `bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"`
- `CACHE="/tmp/claude-statusline-tokens/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315.tsv"
echo "content:"; cat -A "$CACHE" 2>&1 | head -5
echo "---"
echo "TMPDIR is: $TMPDIR"
ls -la /tmp/claude-statusline-tokens/ 2>&1`
- `grep -n "> \"\$cache_file\"" "/c/Users/Anant Gupta/.claude/statusline.sh"`
- `grep -n 'while IFS=\$.\\t.' -A5 "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\d8bb2e2e-53d1-4b26-ab93-c763ddbb1315\scratchpad\statusline.sh" 2>/dev/null
grep -n "while IFS=" "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"`
- `rm -rf /tmp/claude-statusline-tokens
cp "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh" "/c/Users/Anant Gupta/.claude/statusline.sh"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"
echo "=== run 2 (warm cache) ==="
bash "/c/Users/Anant Gupta/.claude/statusline.sh" < "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/case_win.json"`
- `wsl.exe -d Ubuntu -- bash -c "chmod +x ~/.claude/statusline.sh && ls -la ~/.claude/statusline.sh"`
- `rm -f "/tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "rm -f /tmp/claude-statusline-tokens/156d5c7d-7e03-456a-8148-6da71f1883c6.tsv; bash ~/.claude/statusline.sh < '$DIR/case1.json' 2>&1 || echo 'no case1.json (already cleaned) - using case_real.json'; echo ---; bash ~/.claude/statusline.sh < '$DIR/case_real.json'"`
- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case1.json,case2.json,case3.json,case_real.json,case_nodata.json,case_red.json,case_win.json,test_tokens.sh,run_real.sh,run_real2.sh,run_edge.sh}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`
- `echo "=== Windows Jarvis project memory dir ==="
ls -la "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/memory/" 2>&1 | head -30
echo
echo "=== contents of MEMORY.md if present there vs the one referenced in system prompt ==="
find "/c/Users/Anant Gupta/.claude/projects/D--Users--Anant-10-Areas-Documents-Jarvis/memory/" -maxdepth 1 -type f 2>&1 | head -30`
- `MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "ls -la ~/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/ 2>&1; echo '---jarvis-equivalent (home dir) memory dir if any---'; ls -la ~/.claude/projects/-home-anant-gupta/memory/ 2>&1"`
- `rm -rf /tmp/claude-statusline-tokens
DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
chmod +x "$DIR/statusline.sh"
echo "=== run 1 (cold cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"
echo "=== run 2 (warm cache) ==="
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"`
- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "=== no transcript, no rate_limits, null ctx ==="
bash "$DIR/statusline.sh" < "$DIR/case_nometa.json"`
- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
echo "=== no transcript, no rate_limits, null ctx ==="
bash "$DIR/statusline.sh" < "$DIR/case_nometa.json"
echo "exit code: $?"
echo
echo "=== real fixture again (cold cache after clearing) ==="
rm -rf /tmp/claude-statusline-tokens
bash "$DIR/statusline.sh" < "$DIR/case_win2.json"
echo "exit code: $?"`
- `DIR="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
bash "$DIR/statusline.sh" < "$DIR/case_win_red.json"
echo "exit code: $?"`
- `SRC="/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/statusline.sh"
cp "$SRC" "/c/Users/Anant Gupta/.claude/statusline.sh"
chmod +x "/c/Users/Anant Gupta/.claude/statusline.sh"
echo "Windows deployed:"
diff "$SRC" "/c/Users/Anant Gupta/.claude/statusline.sh" && echo "identical"`
- `wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
DIR="/mnt/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad"
MSYS_NO_PATHCONV=1 wsl.exe -d Ubuntu -- bash -c "bash ~/.claude/statusline.sh < '$DIR/case_wsl2.json'; echo EXIT:\$?"`
- `rm -f "/c/Users/ANANTG~1/AppData/Local/Temp/claude/D--Users--Anant-10-Areas-Documents-Jarvis/d8bb2e2e-53d1-4b26-ab93-c763ddbb1315/scratchpad/"{statusline.sh,case_win.json,case_win2.json,case_win_red.json,case_nometa.json,case_nodata.json,case_wsl2.json}
rm -rf /tmp/claude-statusline-tokens
wsl.exe -d Ubuntu -- bash -c "rm -rf /tmp/claude-statusline-tokens"
echo done`


