---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - utility
  - jarvis
source_url: https://github.com/yt-dlp/yt-dlp
notes:
  - "[[40_Resources/CS/Repos]]"
---
# yt-dlp

**GitHub:** [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | **Stars:** 104k | **Updated:** actively maintained, ~weekly releases

## What it is
CLI audio/video downloader for 1,800+ sites; fork of youtube-dl with active maintenance and working YouTube support where the original broke.

## How Anant uses it
Already installed. The main pipeline: YouTube technical talk or course lecture → `yt-dlp -x --audio-format mp3 URL` → transcribe with faster-whisper (also installed) → paste transcript into `/ingest-clipping`. This turns any conference talk, interview prep video, or course lecture into a searchable Jarvis vault note without manual transcription.

```bash
# Download audio only (faster-whisper handles mp3 well)
yt-dlp -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID" -o "~/Downloads/%(title)s.%(ext)s"

# Then transcribe
faster-whisper ~/Downloads/video.mp3 --output_format txt --output_dir ~/Downloads/
```

## How to install / run it (Windows)
Already installed. Update: `yt-dlp -U`. If reinstalling: `pip install yt-dlp`.

## Caveats / current state
Actively maintained. No API key needed for most content. YouTube throttling exists but yt-dlp has built-in workarounds. Playlist download: add `--yes-playlist` flag. SponsorBlock integration available via `--sponsorblock-remove all` to strip ads from downloaded audio before transcription.

**Verdict: yes** — already installed, useful specifically as the first step of the YouTube→faster-whisper→vault pipeline.

## Connects to
- [[40_Resources/CS/Repos]]
