#!/usr/bin/env python3
"""Jarvis memory registry.

The data layer for Jarvis's brain: a SQLite index of every vault note. This
module is intentionally a working skeleton, not the finished engine. It builds
the `notes` table for real (scan -> upsert) and exposes status/search helpers
the MCP server and CLI call. Heavier subsystems from the three-month plan
(chunking, embeddings, semantic search, graph, conversations) get their tables
in schema.sql and their functions stubbed here with clear TODOs, so they grow
without restructuring.

CLI:
    python registry.py index     # (re)build the notes index
    python registry.py status    # summarize the registry
    python registry.py search "query"

The database lives next to this file as registry.sqlite and is gitignored.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import sqlite3
import sys
from pathlib import Path

SKIP_TOP = {".git", ".obsidian", ".claude", ".cursor", ".kiro", ".codex", "50_Archive"}
SCHEMA_FILE = Path(__file__).with_name("schema.sql")
DB_FILE = Path(__file__).with_name("registry.sqlite")


def vault_root() -> Path:
    """Resolve the vault root from env, then by walking up to a known anchor."""
    env = os.environ.get("JARVIS_VAULT_ROOT")
    if env and Path(env).exists():
        return Path(env)
    for parent in Path(__file__).resolve().parents:
        if (parent / "00_Dashboard.md").exists() and (parent / ".obsidian").exists():
            return parent
    return Path.cwd()


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db(con: sqlite3.Connection) -> None:
    con.executescript(SCHEMA_FILE.read_text(encoding="utf-8"))
    con.commit()


def iter_note_paths(root: Path):
    for path in root.rglob("*.md"):
        parts = path.relative_to(root).parts
        if parts and parts[0] in SKIP_TOP:
            continue
        yield path


def extract_frontmatter(text: str) -> dict[str, str]:
    """Minimal scalar frontmatter parser. Lists collapse to first value."""
    if not text.startswith("---"):
        return {}
    match = re.match(r"(?s)^---\s*\r?\n(.*?)\r?\n---", text)
    if not match:
        return {}
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_ -]+):\s*(.*)$", line)
        if kv and kv.group(2).strip():
            value = kv.group(2).strip().strip('"').strip("'")
            meta.setdefault(kv.group(1).strip(), value)
    return meta


def index(root: Path) -> int:
    con = connect()
    init_db(con)
    count = 0
    for path in iter_note_paths(root):
        try:
            text = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        meta = extract_frontmatter(text)
        rel = path.relative_to(root).as_posix()
        digest = hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()
        words = len(re.findall(r"\b\w+\b", text))
        con.execute(
            """
            INSERT INTO notes
                (path, title, type, status, track, enrichment_status,
                 source_status, word_count, hash, updated, indexed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                title=excluded.title, type=excluded.type, status=excluded.status,
                track=excluded.track, enrichment_status=excluded.enrichment_status,
                source_status=excluded.source_status, word_count=excluded.word_count,
                hash=excluded.hash, updated=excluded.updated, indexed_at=excluded.indexed_at
            """,
            (
                rel,
                meta.get("title") or path.stem,
                meta.get("type", ""),
                meta.get("status", ""),
                meta.get("track", ""),
                meta.get("enrichment_status", ""),
                meta.get("source_status", ""),
                words,
                digest,
                meta.get("updated", ""),
                dt.datetime.now().isoformat(timespec="seconds"),
            ),
        )
        count += 1
    con.commit()
    con.close()
    return count


def status_text(root: Path) -> str:
    if not DB_FILE.exists():
        return "Jarvis registry: not built yet. Run `python registry.py index`."
    con = connect()
    init_db(con)
    total = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    by_type = con.execute(
        "SELECT type, COUNT(*) c FROM notes WHERE type <> '' GROUP BY type ORDER BY c DESC"
    ).fetchall()
    by_track = con.execute(
        "SELECT track, COUNT(*) c FROM notes WHERE track <> '' GROUP BY track ORDER BY c DESC"
    ).fetchall()
    convos = con.execute("SELECT COUNT(*) FROM conversations").fetchone()[0]
    undistilled = con.execute(
        "SELECT COUNT(*) FROM conversations WHERE status = 'raw'"
    ).fetchone()[0]
    con.close()

    lines = [
        "# Jarvis Registry Status",
        f"- Notes indexed: {total}",
        f"- Conversations: {convos} ({undistilled} undistilled)",
        "- By type: " + (", ".join(f"{r['type']}={r['c']}" for r in by_type) or "none"),
        "- By track: " + (", ".join(f"{r['track']}={r['c']}" for r in by_track) or "none"),
    ]
    return "\n".join(lines)


def search_text(root: Path, query: str, limit: int = 10) -> str:
    """Keyword search over titles and paths. Semantic search is a TODO:
    add a chunks table populated with embeddings and a hybrid ranker (see
    schema.sql `chunks` and the three-month plan, Week 5)."""
    if not DB_FILE.exists():
        return "Jarvis registry: not built yet. Run `python registry.py index`."
    con = connect()
    like = f"%{query.strip()}%"
    rows = con.execute(
        """
        SELECT path, type, status, track FROM notes
        WHERE title LIKE ? OR path LIKE ?
        ORDER BY (title LIKE ?) DESC, path
        LIMIT ?
        """,
        (like, like, like, limit),
    ).fetchall()
    con.close()
    if not rows:
        return f"No notes matched '{query}'."
    out = [f"Matches for '{query}':"]
    for r in rows:
        meta = " ".join(p for p in (r["type"], r["status"], r["track"]) if p)
        out.append(f"- {r['path']}" + (f"  ({meta})" if meta else ""))
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="jarvis-memory", description="Jarvis note registry.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("index", help="Build or refresh the notes index.")
    sub.add_parser("status", help="Summarize the registry.")
    search = sub.add_parser("search", help="Keyword search over notes.")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)

    root = vault_root()
    if args.command == "index":
        n = index(root)
        print(f"Indexed {n} notes into {DB_FILE.name}.")
    elif args.command == "status":
        print(status_text(root))
    elif args.command == "search":
        print(search_text(root, args.query, args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
