#!/usr/bin/env python3
"""List Cursor composers as export candidates, newest first.

Reads composer.composerHeaders (ItemTable) as the primary index - 183
composers on this machine as of 2026-07-05, split 122 vscode-remote (WSL) /
32 file (Windows) / 29 with no workspace URI (multi-root or empty windows).
Also cross-references cursorDiskKV composerData:* rows directly, since ~41
composers on this machine exist in cursorDiskKV but fell out of the header
index (stale index, not missing data) - those are still listed, with
workspace_env "unknown".
"""
import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from composer_index import DEFAULT_INDEX_PATH, load_exported_index

DEFAULT_DB = Path(os.environ.get("APPDATA", "")) / "Cursor" / "User" / "globalStorage" / "state.vscdb"


def workspace_env_from_uri(uri: dict | None) -> str:
    if not uri:
        return "unknown"
    scheme = uri.get("scheme", "")
    if scheme == "vscode-remote":
        return "wsl"
    if scheme == "file":
        return "windows"
    return "unknown"


def workspace_path_from_uri(uri: dict | None) -> str:
    if not uri:
        return ""
    return uri.get("path") or uri.get("fsPath") or ""


def first_user_preview(con: sqlite3.Connection, composer_id: str, headers: list, limit: int = 150) -> str:
    for h in headers:
        if h.get("type") != 1:
            continue
        bubble_id = h.get("bubbleId")
        if not bubble_id:
            continue
        row = con.execute(
            "SELECT value FROM cursorDiskKV WHERE key = ?",
            (f"bubbleId:{composer_id}:{bubble_id}",),
        ).fetchone()
        if row and row[0]:
            text = (json.loads(row[0]).get("text") or "").strip()
            if text:
                return text[:limit]
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--jarvis-only", action="store_true",
                     help="Only list composers whose workspace path contains Documents/Jarvis")
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable text")
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--index", default=str(DEFAULT_INDEX_PATH))
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"Database not found: {db_path}", file=sys.stderr)
        sys.exit(1)

    con = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)

    row = con.execute("SELECT value FROM ItemTable WHERE key = 'composer.composerHeaders'").fetchone()
    header_by_id = {}
    if row and row[0]:
        for c in json.loads(row[0]).get("allComposers", []):
            if c.get("composerId"):
                header_by_id[c["composerId"]] = c

    cur = con.execute("SELECT key, value FROM cursorDiskKV WHERE key LIKE 'composerData:%'")
    all_ids = {}
    for key, value in cur.fetchall():
        if value is None:
            continue
        composer_id = key.split(":", 1)[1]
        all_ids[composer_id] = value

    exported = load_exported_index(Path(args.index))

    candidates = []
    for composer_id, raw_value in all_ids.items():
        if composer_id in exported:
            continue
        header = header_by_id.get(composer_id)
        uri = (header or {}).get("workspaceIdentifier", {}).get("uri")
        env = workspace_env_from_uri(uri)
        path = workspace_path_from_uri(uri)

        if args.jarvis_only and "jarvis" not in path.lower():
            continue

        data = json.loads(raw_value)
        name = data.get("name") or (header or {}).get("name") or ""
        updated_ms = data.get("lastUpdatedAt") or (header or {}).get("lastUpdatedAt") or 0
        headers = data.get("fullConversationHeadersOnly", [])
        preview = first_user_preview(con, composer_id, headers)

        candidates.append({
            "composer_id": composer_id,
            "name": name,
            "workspace_path": path,
            "workspace_env": env,
            "updated_ms": updated_ms,
            "turn_count": len(headers),
            "preview": preview,
        })

    con.close()

    candidates.sort(key=lambda c: c["updated_ms"], reverse=True)
    candidates = candidates[: args.limit]

    if args.json:
        print(json.dumps(candidates, indent=2))
        return

    if not candidates:
        print("No candidates found.")
        return

    for c in candidates:
        from datetime import datetime, timezone
        date_str = (datetime.fromtimestamp(c["updated_ms"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
                    if c["updated_ms"] else "unknown-date")
        title = c["name"] or "(untitled)"
        print(f"[{date_str}] {title}  ({c['workspace_env']}, {c['turn_count']} turns)")
        print(f"    id: {c['composer_id']}")
        print(f"    workspace: {c['workspace_path'] or '(none)'}")
        if c["preview"]:
            print(f"    preview: {c['preview']}")
        print()


if __name__ == "__main__":
    main()
