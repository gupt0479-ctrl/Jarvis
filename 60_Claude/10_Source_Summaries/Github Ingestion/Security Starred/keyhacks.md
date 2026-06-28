---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - cybersecurity
source_url: https://github.com/streaak/keyhacks
notes:
  - "[[40_Resources/CS/Repos]]"
---
# KeyHacks

**GitHub:** [streaak/keyhacks](https://github.com/streaak/keyhacks) | **Stars:** 6.3k | **Updated:** July 2024

## What it is
A single README containing verified `curl` commands to test whether a found API key actually grants access — one entry per service, with example requests, expected responses for valid vs invalid credentials, and regex patterns for detecting key formats in source code.

## How Anant uses it
When auditing a repo for accidentally committed secrets (e.g., scanning git history with `git log -p | grep -E 'sk-ant|fc-|sbp_|AIza'`), look up the detected key prefix in the KeyHacks README to find the verification command. For an Anthropic key (`sk-ant-*`) there's no explicit entry yet (repo predates widespread Claude usage), but for adjacent services that are wired into the Jarvis stack:

- **GitHub token**: `curl -H "Authorization: token TOKEN" https://api.github.com/user`
- **Google Cloud / Firebase**: see Firebase section for the service account check
- **Slack webhook**: `curl -X POST -H "Content-type: application/json" -d '{"text":""}' WEBHOOK_URL` — if it returns `missing_text_or_fallback_or_attachments`, it's valid
- **AWS**: `AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=y aws sts get-caller-identity`

The workflow is: find suspicious string in repo → identify service → run the KeyHacks curl → see if you get a 200 with real data or an auth error.

## How to install / run it (Windows)
No install — it's a reference doc. Open `https://github.com/streaak/keyhacks` and Ctrl+F the service name. The curl commands run in Git Bash or WSL on Windows. AWS check requires `awscli` (`pip install awscli`).

## Caveats / current state
Last updated July 2024 — 2 years old, not actively maintained. Many newer services (Anthropic, Firecrawl, Supabase) are not listed. Some curl endpoints may have changed. The verification commands only check if a key is valid, not what permissions it has — for AWS use `enumerate-iam` from the repo for that. No AGPL concerns — it's just documentation with no license specified.

## Connects to
[[40_Resources/CS/Repos]]
