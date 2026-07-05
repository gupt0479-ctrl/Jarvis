#!/usr/bin/env python3
"""Tier 0 safety net: on-demand, unredacted raw dump of one composer.

Not a standing sync - run by hand (or by the export-cursor-session skill)
right before/after exporting a composer you want a full-fidelity backup of.
Writes composerData:<id> plus every referenced bubbleId:<id>:<bubbleId> blob,
verbatim, to a single JSON file. This WILL contain secrets if any were ever
pasted into the conversation - the destination directory
(AI Conversations/**/_raw_composer/) must stay in .gitignore.
"""
import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path

DEFAULT_DB = Path(os.environ.get("APPDATA", "")) / "Cursor" / "User" / "globalStorage" / "state.vscdb"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--composer-id", required=True)
    ap.add_argument("--output-dir", required=True, help="Should be a _raw_composer/ folder")
    ap.add_argument("--db", default=str(DEFAULT_DB))
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"Database not found: {db_path}", file=sys.stderr)
        sys.exit(1)

    con = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    row = con.execute(
        "SELECT value FROM cursorDiskKV WHERE key = ?",
        (f"composerData:{args.composer_id}",),
    ).fetchone()
    if not row or row[0] is None:
        print(f"No composerData found for {args.composer_id}", file=sys.stderr)
        sys.exit(1)

    composer_data = json.loads(row[0])
    bubbles = {}
    for h in composer_data.get("fullConversationHeadersOnly", []):
        bubble_id = h.get("bubbleId")
        if not bubble_id:
            continue
        brow = con.execute(
            "SELECT value FROM cursorDiskKV WHERE key = ?",
            (f"bubbleId:{args.composer_id}:{bubble_id}",),
        ).fetchone()
        if brow and brow[0] is not None:
            bubbles[bubble_id] = json.loads(brow[0])
    con.close()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.composer_id}.json"
    out_path.write_text(
        json.dumps({"composerData": composer_data, "bubbles": bubbles}, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {out_path} ({len(bubbles)} bubbles, unredacted)")


if __name__ == "__main__":
    main()
