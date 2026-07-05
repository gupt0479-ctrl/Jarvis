#!/usr/bin/env python3
"""Export one Cursor composer (chat/agent conversation) to a Jarvis raw archive note.

Primary source: the Windows Cursor SQLite store
(%APPDATA%\\Cursor\\User\\globalStorage\\state.vscdb), table cursorDiskKV,
keys composerData:<id> + bubbleId:<id>:<bubbleId>. Falls back to the partial
agent-transcripts JSONL mirror under ~/.cursor/projects/*/agent-transcripts/
when a composer has no SQLite row (deleted/rotated) or the DB is locked.

Verified against this machine 2026-07-05: 183 composers in the
composer.composerHeaders index (122 vscode-remote / 32 file / 29 without a
workspace URI), 224 composerData:* rows in cursorDiskKV (the ~41 extra rows
are composers that fell out of the header index but still have raw data -
this script reads cursorDiskKV directly so it can still find them), one
composerData row observed with a NULL value (tombstone - skipped, not an
error).

Deliberate safety choice, matching export-claude-session.ps1: only
natural-language `text` fields are ever emitted. toolResults, attachedCodeChunks,
codeBlockData, diffs, and images are never written to the exported note, and
text still passes through redact_secrets() since a user can paste a literal
key/token into a chat message.

Tool-name limitation: unlike the Claude Code JSONL schema, no bubble in the
sampled composers on this machine had a populated toolResults array, and
there is no other documented field with a clean tool name at the bubble
level. grouping.capabilityType is a numeric enum with no public mapping.
Rather than fabricate tool names, this script emits a generic
"*Tool activity (details omitted)*" marker when a type-2 bubble has empty
text but grouping metadata indicating tool/capability use.
"""
import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from redact_secrets import redact_secrets

DEFAULT_DB = Path(os.environ.get("APPDATA", "")) / "Cursor" / "User" / "globalStorage" / "state.vscdb"
CURSOR_PROJECTS = Path.home() / ".cursor" / "projects"


def open_db_ro(db_path: Path) -> sqlite3.Connection:
    uri = f"file:{db_path.as_posix()}?mode=ro"
    try:
        return sqlite3.connect(uri, uri=True)
    except sqlite3.OperationalError as e:
        print(f"Could not open {db_path} read-only ({e}). "
              f"Cursor may be running with an exclusive lock - try again, "
              f"or close Cursor and retry.", file=sys.stderr)
        sys.exit(1)


def load_composer_index(con: sqlite3.Connection) -> dict:
    """composer.composerHeaders -> {composerId: header dict}, keyed for workspace lookup."""
    row = con.execute("SELECT value FROM ItemTable WHERE key = 'composer.composerHeaders'").fetchone()
    if not row or not row[0]:
        return {}
    data = json.loads(row[0])
    return {c["composerId"]: c for c in data.get("allComposers", []) if c.get("composerId")}


def workspace_env_from_uri(uri: dict | None) -> str:
    if not uri:
        return "unknown"
    scheme = uri.get("scheme", "")
    if scheme == "vscode-remote":
        return "wsl"
    if scheme == "file":
        return "windows"
    return "unknown"


def load_composer_data(con: sqlite3.Connection, composer_id: str) -> dict | None:
    row = con.execute(
        "SELECT value FROM cursorDiskKV WHERE key = ?", (f"composerData:{composer_id}",)
    ).fetchone()
    if not row or row[0] is None:
        return None
    return json.loads(row[0])


def load_bubble(con: sqlite3.Connection, composer_id: str, bubble_id: str) -> dict | None:
    row = con.execute(
        "SELECT value FROM cursorDiskKV WHERE key = ?",
        (f"bubbleId:{composer_id}:{bubble_id}",),
    ).fetchone()
    if not row or row[0] is None:
        return None
    return json.loads(row[0])


def has_tool_activity(bubble: dict) -> bool:
    grouping = bubble.get("grouping") or {}
    if grouping.get("capabilityType") and not grouping.get("hasThinking"):
        return True
    for key in ("toolResults", "diffsForCompressingFiles", "assistantSuggestedDiffs"):
        if bubble.get(key):
            return True
    return False


def turns_from_sqlite(con: sqlite3.Connection, composer_id: str, headers: list) -> list:
    turns = []
    for h in headers:
        bubble_id = h.get("bubbleId")
        if not bubble_id:
            continue
        bubble = load_bubble(con, composer_id, bubble_id)
        if bubble is None:
            continue
        role = "user" if bubble.get("type") == 1 else "assistant"
        text = (bubble.get("text") or "").strip()
        tool_activity = has_tool_activity(bubble)
        if not text and not tool_activity:
            continue
        turns.append({"role": role, "text": text, "tool_activity": tool_activity})
    return turns


def find_agent_transcript(composer_id: str) -> Path | None:
    if not CURSOR_PROJECTS.exists():
        return None
    matches = list(CURSOR_PROJECTS.glob(f"*/agent-transcripts/{composer_id}/{composer_id}.jsonl"))
    return matches[0] if matches else None


def turns_from_jsonl(path: Path) -> list:
    turns = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") == "user" and obj.get("message"):
                content = obj["message"].get("content")
                if isinstance(content, str) and content.strip():
                    turns.append({"role": "user", "text": content.strip(), "tool_activity": False})
            elif obj.get("type") == "assistant" and obj.get("message"):
                text_parts = []
                tool_activity = False
                for block in obj["message"].get("content") or []:
                    if block.get("type") == "text" and block.get("text", "").strip():
                        text_parts.append(block["text"].strip())
                    elif block.get("type") == "tool_use":
                        tool_activity = True
                if text_parts or tool_activity:
                    turns.append({
                        "role": "assistant",
                        "text": "\n\n".join(text_parts),
                        "tool_activity": tool_activity,
                    })
    return turns


def slugify(text: str, max_len: int = 60) -> str:
    if not text:
        return ""
    first_line = text.split("\n", 1)[0]
    first_sentence = re.split(r"(?<=[.!?])\s", first_line)[0]
    clean = re.sub(r'[<>:"/\\|?*`]', "", first_sentence)
    clean = re.sub(r"\s+", " ", clean).strip()
    if len(clean) > max_len:
        truncated = clean[:max_len]
        last_space = truncated.rfind(" ")
        if last_space > 20:
            truncated = truncated[:last_space]
        clean = truncated.strip()
    return clean


def ms_to_iso(ms) -> str:
    if not ms:
        return ""
    try:
        return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    except (ValueError, OSError):
        return ""


def build_note(composer_id: str, data: dict | None, header: dict | None, turns: list, title_override: str | None) -> tuple[str, str, str]:
    """Returns (markdown, created_date_MM-DD, slug)."""
    name = (data or {}).get("name") or (header or {}).get("name") or ""
    first_user_turn = next((t for t in turns if t["role"] == "user"), None)
    auto_slug = slugify(name) or slugify(first_user_turn["text"] if first_user_turn else "")
    if not auto_slug:
        auto_slug = f"Composer {composer_id[:8]}"
    title = title_override or auto_slug

    created_ms = (data or {}).get("createdAt") or (header or {}).get("createdAt")
    updated_ms = (data or {}).get("lastUpdatedAt") or (header or {}).get("lastUpdatedAt")
    started_at = ms_to_iso(created_ms)
    ended_at = ms_to_iso(updated_ms)
    created_date = datetime.fromtimestamp(int(created_ms) / 1000, tz=timezone.utc) if created_ms else datetime.now(timezone.utc)
    mmdd = created_date.strftime("%m-%d")

    uri = (header or {}).get("workspaceIdentifier", {}).get("uri") or {}
    workspace_uri = uri.get("external", "")
    workspace_env = workspace_env_from_uri(uri)

    lines = []
    lines.append("---")
    lines.append("type: input")
    lines.append("input_kind: ai-conversation")
    lines.append("source_app: cursor")
    lines.append(f'title: "{title}"')
    lines.append(f"started_at: {started_at}")
    lines.append(f"ended_at: {ended_at}")
    lines.append("status: raw")
    lines.append(f"composer_id: {composer_id}")
    if workspace_uri:
        lines.append(f"workspace_uri: '{workspace_uri}'")
    lines.append(f"workspace_env: {workspace_env}")
    lines.append("tags:")
    lines.append("  - input")
    lines.append("  - ai-conversation")
    lines.append("  - cursor")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")

    for turn in turns:
        if turn["role"] == "user":
            lines.append("## You")
            lines.append("")
            lines.append(redact_secrets(turn["text"]))
            lines.append("")
        else:
            lines.append("## Cursor")
            lines.append("")
            if turn["text"]:
                lines.append(redact_secrets(turn["text"]))
                lines.append("")
            if turn["tool_activity"]:
                lines.append("*Tool activity (details omitted)*")
                lines.append("")

    return "\n".join(lines), mmdd, auto_slug


def resolve_output_path(output: str | None, output_dir: str | None, mmdd: str, slug: str) -> Path:
    if output:
        return Path(output)
    base_name = f"{mmdd} Cursor - {slug}"
    candidate = Path(output_dir) / f"{base_name}.md"
    n = 2
    while candidate.exists():
        candidate = Path(output_dir) / f"{base_name}-{n}.md"
        n += 1
    return candidate


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--composer-id", required=True)
    ap.add_argument("--output", help="Exact output file path")
    ap.add_argument("--output-dir", help="Output directory; filename is derived (MM-DD Cursor - slug.md)")
    ap.add_argument("--title", help="Override the auto-derived title")
    ap.add_argument("--db", default=str(DEFAULT_DB), help="Path to Cursor's state.vscdb")
    args = ap.parse_args()

    if not args.output and not args.output_dir:
        print("Pass either --output or --output-dir.", file=sys.stderr)
        sys.exit(1)

    db_path = Path(args.db)
    turns, data, header = [], None, None

    if db_path.exists():
        con = open_db_ro(db_path)
        header_index = load_composer_index(con)
        header = header_index.get(args.composer_id)
        data = load_composer_data(con, args.composer_id)
        if data is not None:
            turns = turns_from_sqlite(con, args.composer_id, data.get("fullConversationHeadersOnly", []))
        con.close()

    if not turns:
        jsonl_path = find_agent_transcript(args.composer_id)
        if jsonl_path:
            turns = turns_from_jsonl(jsonl_path)

    if not turns:
        print("No human-readable turns found for this composer (tool-only, empty, "
              "or not found in SQLite or agent-transcripts) - nothing written.")
        sys.exit(0)

    note, mmdd, slug = build_note(args.composer_id, data, header, turns, args.title)
    out_path = resolve_output_path(args.output, args.output_dir, mmdd, slug)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(note, encoding="utf-8")
    print(f"Wrote {out_path} ({len(turns)} turns)")
    print(f"WROTE_PATH:{out_path}")


if __name__ == "__main__":
    main()
