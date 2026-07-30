#!/usr/bin/env python3
"""Export Cursor agent sessions to Jarvis AI Conversations (WSL + Windows).

Joins two stores (verified 2026-07-30):

1. Per-session JSONL transcripts under ~/.cursor/projects/**/agent-transcripts/
   <uuid>/<uuid>.jsonl — live on the OS where the workspace ran (WSL home or
   Windows user profile). No timestamp/usage/model fields in these files.
2. Windows-only SQLite composerHeaders in
   %APPDATA%\\Cursor\\User\\globalStorage\\state.vscdb — composerId matches the
   JSONL filename; value JSON has name/subtitle/createdAt/lastUpdatedAt/
   filesChangedCount/totalLinesAdded/totalLinesRemoved/isDraft. No tokens or
   cost anywhere — those frontmatter keys are omitted, never fabricated.

Workspace routing uses workspaceIdentifier.uri (from the value blob) with a
fallback to workspaceStorage/<workspaceId>/workspace.json:
  vscode-remote://wsl+... or file://wsl$/...  → WSL/Cursor/<project>/
  file:///c:/... or file:///d:/...            → Windows/Cursor/<project>/

Designed to run on Windows (SQLite lives there). WSL JSONL is read via
\\\\wsl.localhost\\<distro>\\home\\... when running on Windows; when running
inside WSL it reads local paths and opens a copied DB if the live one is locked.

Trigger: NOT a Cursor sessionEnd hook. For vscode-remote+wsl workspaces,
Cursor loads hooks from the WSL user path (~/.cursor/hooks.json), not the
Windows one — confirmed in cursor.hooks logs (User config path:
\\home\\anant_gupta\\.cursor\\hooks.json). A WSL-side sessionEnd cannot
reliably open the Windows SQLite store. Automation is a Windows Task
Scheduler sweep (same eventually-consistent pattern as Cowork).

Usage:
  py export-cursor-sessions.py --backfill
  py export-cursor-sessions.py --sweep
  py export-cursor-sessions.py --composer-id <uuid>
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent))
from redact_secrets import redact_secrets

# --- Paths -----------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
WORKFLOW_DIR = SCRIPT_DIR.parent

if os.name == "nt":
    APPDATA = Path(os.environ.get("APPDATA", r"C:\Users\Anant Gupta\AppData\Roaming"))
    USERPROFILE = Path(os.environ.get("USERPROFILE", r"C:\Users\Anant Gupta"))
    DEFAULT_DB = APPDATA / "Cursor" / "User" / "globalStorage" / "state.vscdb"
    WORKSPACE_STORAGE = APPDATA / "Cursor" / "User" / "workspaceStorage"
    WIN_CURSOR_PROJECTS = USERPROFILE / ".cursor" / "projects"
    VAULT_CONV = Path(
        r"D:\Users\_Anant\10_Areas\Documents\Jarvis"
        r"\60_Claude\05_Clippings\AI Conversations"
    )
else:
    DEFAULT_DB = Path(
        "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/state.vscdb"
    )
    WORKSPACE_STORAGE = Path(
        "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/workspaceStorage"
    )
    WIN_CURSOR_PROJECTS = Path("/mnt/c/Users/Anant Gupta/.cursor/projects")
    VAULT_CONV = Path(
        "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
        "/60_Claude/05_Clippings/AI Conversations"
    )

STATE_FILE = WORKFLOW_DIR / "cursor-export-state.json"
WSL_HOME_PROJECTS = Path("/home/anant_gupta/.cursor/projects")  # when running in WSL


# --- Helpers ---------------------------------------------------------------

def detect_wsl_distro() -> str:
    """Return the WSL distro name (e.g. Ubuntu). Never assume."""
    if os.name != "nt":
        # Inside WSL: prefer /etc/os-release NAME or wsl.conf
        try:
            text = Path("/etc/os-release").read_text(encoding="utf-8")
            for line in text.splitlines():
                if line.startswith("NAME="):
                    return line.split("=", 1)[1].strip().strip('"')
        except OSError:
            pass
        return "Ubuntu"
    try:
        raw = subprocess.check_output(
            ["wsl", "-l", "-v"], stderr=subprocess.STDOUT, timeout=15
        )
        # wsl -l -v emits UTF-16LE on Windows
        try:
            text = raw.decode("utf-16-le")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", errors="replace")
        for line in text.splitlines():
            line = line.strip()
            if not line or line.lower().startswith("windows subsystem"):
                continue
            if "NAME" in line.upper() and "STATE" in line.upper():
                continue
            # default marked with *
            if line.startswith("*"):
                line = line[1:].strip()
            parts = line.split()
            if parts:
                return parts[0]
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        pass
    return "Ubuntu"


def wsl_projects_root(distro: str) -> Path:
    if os.name == "nt":
        return Path(rf"\\wsl.localhost\{distro}\home\anant_gupta\.cursor\projects")
    return WSL_HOME_PROJECTS


def open_db(db_path: Path) -> sqlite3.Connection:
    """Open state.vscdb read-only. On WSL lock failure, copy then open."""
    uri = f"file:{db_path.as_posix()}?mode=ro"
    try:
        con = sqlite3.connect(uri, uri=True)
        # Force a read to surface locks early
        con.execute("SELECT COUNT(*) FROM composerHeaders").fetchone()
        return con
    except sqlite3.OperationalError:
        if os.name == "nt":
            raise
        tmp = Path("/tmp/cursor-state-export.vscdb")
        shutil.copy2(db_path, tmp)
        return sqlite3.connect(str(tmp))


def ms_to_iso_local(ms) -> str:
    """Epoch-ms → YYYY-MM-DDTHH:MM:SS in local time, no offset, no fraction."""
    if not ms:
        return ""
    try:
        return datetime.fromtimestamp(int(ms) / 1000).strftime("%Y-%m-%dT%H:%M:%S")
    except (ValueError, OSError, OverflowError):
        return ""


def now_iso_local() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def sanitize_filename(text: str, max_len: int = 80) -> str:
    if not text:
        return ""
    clean = re.sub(r'[<>:"/\\|?*`]', "", text)
    clean = re.sub(r"\s+", " ", clean).strip()
    if len(clean) > max_len:
        truncated = clean[:max_len]
        last_space = truncated.rfind(" ")
        if last_space > 20:
            truncated = truncated[:last_space]
        clean = truncated.strip()
    return clean


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def collect_jsonl_index(roots: list[Path]) -> dict[str, dict]:
    """Map composerId → {path, source_os, projects_root, project_slug}."""
    index: dict[str, dict] = {}
    for root, source_os in roots:
        if not root.exists():
            continue
        try:
            project_dirs = list(root.iterdir())
        except OSError:
            continue
        for proj in project_dirs:
            transcripts = proj / "agent-transcripts"
            if not transcripts.is_dir():
                continue
            try:
                session_dirs = list(transcripts.iterdir())
            except OSError:
                continue
            for sess in session_dirs:
                if not sess.is_dir() or sess.name == "subagents":
                    continue
                jsonl = sess / f"{sess.name}.jsonl"
                if jsonl.is_file():
                    index[sess.name] = {
                        "path": jsonl,
                        "source_os": source_os,
                        "projects_root": root,
                        "project_slug": proj.name,
                        "agent_transcripts": transcripts,
                    }
    return index


def load_workspace_folder(workspace_id: str | None, value: dict) -> str:
    """Return the folder URI string for routing."""
    uri = (value.get("workspaceIdentifier") or {}).get("uri") or {}
    external = uri.get("external") or ""
    if external:
        return external
    if not workspace_id:
        return ""
    wj = WORKSPACE_STORAGE / workspace_id / "workspace.json"
    if wj.exists():
        try:
            return json.loads(wj.read_text(encoding="utf-8")).get("folder") or ""
        except (OSError, json.JSONDecodeError):
            return ""
    return ""


def route_workspace(folder_uri: str) -> tuple[str, str, str]:
    """Return (source_os, project_name, cwd_path).

    source_os is 'wsl' | 'windows' | 'unknown'.
    """
    if not folder_uri:
        return "unknown", "unknown", ""

    raw = unquote(folder_uri)
    lower = raw.lower()

    # WSL remote or Windows path into WSL filesystem
    if lower.startswith("vscode-remote://wsl") or "wsl%2b" in lower or "wsl+" in lower:
        # vscode-remote://wsl+ubuntu/home/...
        path = ""
        if "://" in raw:
            rest = raw.split("://", 1)[1]
            # authority/path
            if "/" in rest:
                path = "/" + rest.split("/", 1)[1]
            else:
                path = ""
        project = Path(path.rstrip("/")).name or "unknown"
        return "wsl", project, path

    if lower.startswith("file://wsl$") or lower.startswith("file://wsl%24"):
        # file://wsl$/Ubuntu/home/anant_gupta/...
        rest = raw.split("://", 1)[1]  # wsl$/Ubuntu/home/...
        parts = rest.split("/")
        # drop wsl$ and distro
        if len(parts) >= 3:
            path = "/" + "/".join(parts[2:])
        else:
            path = ""
        project = Path(path.rstrip("/")).name or "unknown"
        return "wsl", project, path

    if lower.startswith("file:"):
        # file:///c:/Users/... or file:///d:/...
        path = raw
        if path.lower().startswith("file:///"):
            path = path[8:]  # strip file:///
        elif path.lower().startswith("file://"):
            path = path[7:]
        # c:/Users/... → C:\Users\... style for display; keep as given with /
        if re.match(r"^[a-zA-Z]:", path):
            # normalize
            path = path[0].upper() + path[1:]
            path = path.replace("/", "\\")
        project = Path(path.rstrip("\\/")).name or "unknown"
        return "windows", project, path

    return "unknown", "unknown", raw


def parse_jsonl(path: Path) -> tuple[list[dict], Counter, list[str], list[str]]:
    """Return (turns, tool_tally, files_touched, commands_run)."""
    turns: list[dict] = []
    tool_tally: Counter = Counter()
    files_touched: list[str] = []
    commands_run: list[str] = []

    state = {"role": None, "text": [], "calls": []}

    def flush():
        if state["role"] and (state["text"] or state["calls"]):
            turns.append({
                "role": state["role"],
                "text": "\n\n".join(state["text"]),
                "calls": list(state["calls"]),
            })
        state["text"] = []
        state["calls"] = []

    path_keys = ("path", "file_path", "target_directory", "working_directory")

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            role = obj.get("role")
            message = obj.get("message") or {}
            content = message.get("content")

            if role == "user":
                if isinstance(content, str):
                    if not content.strip():
                        continue
                    flush()
                    state["role"] = "user"
                    state["text"].append(content)
                    flush()
                    state["role"] = None
                elif isinstance(content, list):
                    texts = [
                        b.get("text", "")
                        for b in content
                        if b.get("type") == "text" and (b.get("text") or "").strip()
                    ]
                    if texts:
                        flush()
                        state["role"] = "user"
                        state["text"].extend(texts)
                        flush()
                        state["role"] = None

            elif role == "assistant":
                if state["role"] != "assistant":
                    flush()
                    state["role"] = "assistant"
                if isinstance(content, str):
                    if content.strip():
                        state["text"].append(content)
                elif isinstance(content, list):
                    for block in content:
                        btype = block.get("type")
                        if btype == "text" and (block.get("text") or "").strip():
                            state["text"].append(block["text"])
                        elif btype == "tool_use" and block.get("name"):
                            name = block["name"]
                            tool_tally[name] += 1
                            inp = block.get("input") or {}
                            call_line = format_tool_call(name, inp)
                            state["calls"].append(call_line)
                            for pk in path_keys:
                                if inp.get(pk):
                                    files_touched.append(str(inp[pk]))
                            if name == "Shell" and inp.get("command"):
                                commands_run.append(str(inp["command"]))
                            # Write/StrReplace/EditNotebook style
                            if name in ("Write", "StrReplace", "EditNotebook", "Delete") and inp.get("path"):
                                files_touched.append(str(inp["path"]))
                            if name == "Write" and inp.get("contents") is None and inp.get("path"):
                                pass  # already recorded
    flush()
    # dedupe files preserving order
    seen = set()
    files_uniq = []
    for fpath in files_touched:
        if fpath not in seen:
            seen.add(fpath)
            files_uniq.append(fpath)
    cmds_uniq = []
    seen_c = set()
    for c in commands_run:
        if c not in seen_c:
            seen_c.add(c)
            cmds_uniq.append(c)
    return turns, tool_tally, files_uniq, cmds_uniq


def format_tool_call(name: str, inp: dict) -> str:
    if name == "Shell":
        cmd = inp.get("command") or ""
        if "\n" in cmd:
            return f"- `{name}`:\n  ```bash\n{redact_secrets(cmd)}\n  ```"
        return f"- `{name}` — `{redact_secrets(cmd)}`"
    if name in ("Read", "Write", "StrReplace", "Delete", "EditNotebook"):
        return f"- `{name}` — `{inp.get('path') or inp.get('target_notebook') or ''}`"
    if name in ("Grep", "Glob"):
        pattern = inp.get("pattern") or inp.get("glob_pattern") or ""
        path = inp.get("path") or inp.get("target_directory") or "."
        return f"- `{name}` — pattern `{pattern}`, path `{path}`"
    dump = redact_secrets(json.dumps(inp, ensure_ascii=False, separators=(",", ":")))
    if len(dump) > 300:
        dump = dump[:300] + "…"
    return f"- `{name}` — `{dump}`"


def has_real_assistant(turns: list[dict]) -> bool:
    return any(
        t["role"] == "assistant" and (t["text"].strip() or t["calls"])
        for t in turns
    )


def already_exported(project_dir: Path, session_id: str) -> bool:
    """Dedup via flat raw copy (WSL one-way) or session_id in an existing note."""
    # WSL-style flat safety-net copy — definitive marker
    flat_raw = project_dir / "_raw_jsonl" / f"{session_id}.jsonl"
    try:
        if flat_raw.is_file():
            return True
    except OSError:
        pass

    if not project_dir.exists():
        return False
    needle = f"session_id: {session_id}"
    try:
        notes = list(project_dir.glob("*.md"))
    except OSError:
        return False
    for md in notes:
        if md.name.startswith("00 -"):
            continue
        try:
            head = md.read_text(encoding="utf-8", errors="replace")[:4000]
        except OSError:
            continue
        if needle in head:
            return True
    return False


def ensure_raw_jsonl(
    project_dir: Path,
    source_os: str,
    jsonl_meta: dict,
    session_id: str,
) -> None:
    """Windows: NTFS junction to agent-transcripts. WSL: one-way per-session copy."""
    raw_dir = project_dir / "_raw_jsonl"
    src_transcripts: Path = jsonl_meta["agent_transcripts"]
    src_jsonl: Path = jsonl_meta["path"]

    if source_os == "windows" and os.name == "nt":
        if raw_dir.exists():
            return
        raw_dir.parent.mkdir(parents=True, exist_ok=True)
        # mklink /J requires no pre-existing destination
        cmd = f'mklink /J "{raw_dir}" "{src_transcripts}"'
        subprocess.run(["cmd", "/c", cmd], check=False, capture_output=True)
        if not raw_dir.exists():
            # Fallback: copy this one session if junction fails
            raw_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_jsonl, raw_dir / f"{session_id}.jsonl")
        return

    # WSL-hosted (or running exporter from WSL for either side): one-way copy
    raw_dir.mkdir(parents=True, exist_ok=True)
    dest = raw_dir / f"{session_id}.jsonl"
    if not dest.exists():
        try:
            shutil.copy2(src_jsonl, dest)
        except OSError as e:
            print(f"  warn: could not copy raw jsonl for {session_id}: {e}", file=sys.stderr)


def update_rollups(project_dir: Path, source_os: str, project_name: str) -> None:
    vault_rel = (
        f"60_Claude/05_Clippings/AI Conversations/"
        f"{'WSL' if source_os == 'wsl' else 'Windows'}/Cursor/{project_name}"
    )
    index_path = project_dir / "00 - Session Index.md"
    rollup_path = project_dir / "00 - Tool Usage Rollup.md"

    index_path.write_text(
        f"""---
type: dashboard
status: auto-generated
tags:
  - cursor
  - {source_os}
---
# Session Index — {project_name}

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  started_at AS "Session Ran",
  exported_at AS "Added to Jarvis",
  turn_count AS "Turns",
  files_changed_count AS "Files Changed",
  lines_added AS "+Lines",
  lines_removed AS "-Lines"
FROM "{vault_rel}"
WHERE type = "input"
SORT started_at DESC
```
""",
        encoding="utf-8",
    )

    rollup_path.write_text(
        f"""---
type: dashboard
status: auto-generated
tags:
  - cursor
  - {source_os}
---
# Tool Usage Rollup — {project_name}

```dataviewjs
const pages = dv.pages("{vault_rel}").where(p => p.type === "input");
let toolTotals = {{}};
let fileSessions = {{}};
for (const p of pages) {{
  for (const [tool, count] of Object.entries(p.tools_used ?? {{}})) {{
    toolTotals[tool] = (toolTotals[tool] ?? 0) + count;
  }}
  for (const f of p.files_touched ?? []) {{
    fileSessions[f] = (fileSessions[f] ?? 0) + 1;
  }}
}}
dv.paragraph("**Total sessions:** " + pages.length);
dv.header(2, "Tool usage");
dv.table(["Tool", "Total uses"], Object.entries(toolTotals).sort((a, b) => b[1] - a[1]));
dv.header(2, "Files touched (by session count)");
dv.table(["File", "Sessions"], Object.entries(fileSessions).sort((a, b) => b[1] - a[1]));
```
""",
        encoding="utf-8",
    )


def build_note(
    *,
    session_id: str,
    title: str,
    source_os: str,
    project: str,
    cwd: str,
    started_at: str,
    ended_at: str,
    exported_at: str,
    turns: list[dict],
    tool_tally: Counter,
    files_touched: list[str],
    commands_run: list[str],
    subtitle: str,
    files_changed_count,
    lines_added,
    lines_removed,
) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append("type: input")
    lines.append("input_kind: ai-conversation")
    lines.append("source_app: cursor")
    lines.append(f"source_os: {source_os}")
    lines.append(f"title: {yaml_quote(title)}")
    lines.append(f"started_at: {started_at}")
    lines.append(f"ended_at: {ended_at}")
    lines.append(f"exported_at: {exported_at}")
    lines.append(f"project: {project}")
    cwd_yaml = yaml_quote(cwd) if cwd else "''"
    lines.append(f"cwd: {cwd_yaml}")
    lines.append(f"session_id: {session_id}")
    lines.append("status: raw")
    lines.append(f"turn_count: {len(turns)}")
    lines.append("tools_used:")
    for tool in sorted(tool_tally):
        lines.append(f"  {tool}: {tool_tally[tool]}")
    if files_touched:
        lines.append("files_touched:")
        for fpath in files_touched:
            lines.append(f"  - {yaml_quote(fpath)}")
    if files_changed_count is not None:
        lines.append(f"files_changed_count: {files_changed_count}")
    if lines_added is not None:
        lines.append(f"lines_added: {lines_added}")
    if lines_removed is not None:
        lines.append(f"lines_removed: {lines_removed}")
    lines.append("tags:")
    lines.append("  - input")
    lines.append("  - ai-conversation")
    lines.append("  - cursor")
    lines.append(f"  - {source_os}")
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
            if turn["calls"]:
                lines.append("**Tool calls:**")
                lines.append("")
                lines.extend(turn["calls"])
                lines.append("")

    lines.append("## Actions Taken")
    if subtitle:
        lines.append(f"- Summary: {subtitle}")
    if files_changed_count is not None:
        lines.append(f"- Files changed (Cursor): {files_changed_count}")
    if lines_added is not None or lines_removed is not None:
        lines.append(
            f"- Lines: +{lines_added if lines_added is not None else 0} / "
            f"-{lines_removed if lines_removed is not None else 0}"
        )
    if files_touched:
        lines.append(f"- Files touched (from tool calls): {', '.join(files_touched)}")
    else:
        lines.append("- Files touched (from tool calls): (none)")
    cmds_flat = [re.sub(r"\s+", " ", c) for c in commands_run]
    if cmds_flat:
        lines.append(f"- Commands run: {redact_secrets(', '.join(cmds_flat))}")
    else:
        lines.append("- Commands run: (none)")
    tally_str = ", ".join(f"{t} ({tool_tally[t]})" for t in sorted(tool_tally))
    lines.append(f"- Tool call tally: {tally_str or '(none)'}")
    lines.append("")
    return "\n".join(lines)


def resolve_note_path(project_dir: Path, mmdd: str, title: str) -> Path:
    base = f"{mmdd} {sanitize_filename(title) or 'Untitled session'}"
    candidate = project_dir / f"{base}.md"
    n = 2
    while candidate.exists():
        candidate = project_dir / f"{base}-{n}.md"
        n += 1
    return candidate


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def export_one(
    con: sqlite3.Connection,
    composer_id: str,
    jsonl_meta: dict,
    exported_at: str,
    counts: dict,
    touched: set[tuple[str, str]],
) -> str:
    row = con.execute(
        "SELECT workspaceId, createdAt, lastUpdatedAt, isArchived, isSubagent, value "
        "FROM composerHeaders WHERE composerId = ?",
        (composer_id,),
    ).fetchone()
    if not row:
        counts["skip_no_header"] += 1
        return "skip_no_header"

    workspace_id, created_at, last_updated, is_archived, is_subagent, raw_value = row
    if is_archived:
        counts["skip_archived"] += 1
        return "skip_archived"
    if is_subagent:
        counts["skip_subagent"] += 1
        return "skip_subagent"

    value = json.loads(raw_value) if raw_value else {}
    if value.get("isDraft") or value.get("isArchived"):
        counts["skip_draft_or_archived"] += 1
        return "skip_draft_or_archived"

    turns, tool_tally, files_touched, commands_run = parse_jsonl(jsonl_meta["path"])
    if not has_real_assistant(turns):
        counts["skip_no_assistant"] += 1
        return "skip_no_assistant"

    folder_uri = load_workspace_folder(workspace_id, value)
    source_os, project_name, cwd = route_workspace(folder_uri)
    # Prefer JSONL physical location when URI routing is unknown
    if source_os == "unknown":
        source_os = jsonl_meta["source_os"]
        if project_name == "unknown":
            project_name = jsonl_meta["project_slug"]

    os_folder = "WSL" if source_os == "wsl" else "Windows"
    project_dir = VAULT_CONV / os_folder / "Cursor" / project_name

    if already_exported(project_dir, composer_id):
        counts["dup"] += 1
        return "dup"

    project_dir.mkdir(parents=True, exist_ok=True)
    ensure_raw_jsonl(project_dir, source_os, jsonl_meta, composer_id)

    title = (value.get("name") or "").strip()
    if not title:
        first_user = next((t for t in turns if t["role"] == "user"), None)
        if first_user and first_user["text"].strip():
            title = sanitize_filename(first_user["text"].split("\n", 1)[0], 60) or "Untitled session"
        else:
            title = "Untitled session"

    started = ms_to_iso_local(value.get("createdAt") or created_at)
    ended = ms_to_iso_local(value.get("lastUpdatedAt") or last_updated)
    mmdd = ""
    try:
        ms = int(value.get("createdAt") or created_at)
        mmdd = datetime.fromtimestamp(ms / 1000).strftime("%m-%d")
    except (TypeError, ValueError, OSError):
        mmdd = datetime.now().strftime("%m-%d")

    note = build_note(
        session_id=composer_id,
        title=title,
        source_os=source_os if source_os in ("wsl", "windows") else jsonl_meta["source_os"],
        project=project_name,
        cwd=cwd,
        started_at=started,
        ended_at=ended,
        exported_at=exported_at,
        turns=turns,
        tool_tally=tool_tally,
        files_touched=files_touched,
        commands_run=commands_run,
        subtitle=(value.get("subtitle") or "").strip(),
        files_changed_count=value.get("filesChangedCount"),
        lines_added=value.get("totalLinesAdded"),
        lines_removed=value.get("totalLinesRemoved"),
    )
    out_path = resolve_note_path(project_dir, mmdd, title)
    out_path.write_text(note, encoding="utf-8")

    src_os = source_os if source_os in ("wsl", "windows") else jsonl_meta["source_os"]
    touched.add((src_os, project_name))
    counts["written"] += 1
    print(f"WROTE {out_path}")
    return "written"


def archive_old_notes() -> None:
    """Move pre-rewrite flat notes into _archive-pre-fix/ (never delete)."""
    for os_name in ("WSL", "Windows"):
        cursor_root = VAULT_CONV / os_name / "Cursor"
        if not cursor_root.exists():
            continue
        archive = cursor_root / "_archive-pre-fix"
        flat_notes = [
            p for p in cursor_root.glob("*.md")
            if p.is_file() and not p.name.startswith("00 -")
        ]
        if not flat_notes:
            continue
        archive.mkdir(parents=True, exist_ok=True)
        for note in flat_notes:
            dest = archive / note.name
            if dest.exists():
                stem, suf = note.stem, note.suffix
                n = 2
                while (archive / f"{stem}-{n}{suf}").exists():
                    n += 1
                dest = archive / f"{stem}-{n}{suf}"
            shutil.move(str(note), str(dest))
            print(f"ARCHIVED {note} -> {dest}")


def run(args: argparse.Namespace) -> int:
    distro = args.distro or detect_wsl_distro()
    wsl_root = wsl_projects_root(distro)
    print(f"WSL distro: {distro}")
    print(f"WSL projects root: {wsl_root}")
    print(f"Windows projects root: {WIN_CURSOR_PROJECTS}")
    print(f"DB: {args.db}")

    if args.archive_old:
        archive_old_notes()

    jsonl_index = collect_jsonl_index([
        (wsl_root, "wsl"),
        (WIN_CURSOR_PROJECTS, "windows"),
    ])
    print(f"JSONL found: {len(jsonl_index)} "
          f"(wsl={sum(1 for v in jsonl_index.values() if v['source_os']=='wsl')}, "
          f"windows={sum(1 for v in jsonl_index.values() if v['source_os']=='windows')})")

    con = open_db(Path(args.db))
    header_count = con.execute("SELECT COUNT(*) FROM composerHeaders").fetchone()[0]
    eligible_headers = con.execute(
        "SELECT COUNT(*) FROM composerHeaders "
        "WHERE COALESCE(isArchived,0)=0 AND COALESCE(isSubagent,0)=0"
    ).fetchone()[0]
    print(f"composerHeaders: total={header_count} non-archived/non-subagent={eligible_headers}")

    # Reconciliation report
    header_ids = {
        r[0] for r in con.execute("SELECT composerId FROM composerHeaders").fetchall()
    }
    jsonl_ids = set(jsonl_index)
    both = jsonl_ids & header_ids
    only_jsonl = jsonl_ids - header_ids
    only_header = header_ids - jsonl_ids
    print(f"Reconciliation: jsonl∩header={len(both)} "
          f"jsonl-only={len(only_jsonl)} header-only={len(only_header)}")

    state = load_state()
    last_ms = int(state.get("last_processed_updated_at", 0) or 0)

    targets: list[str]
    if args.composer_id:
        targets = [args.composer_id]
    elif args.sweep:
        # Rows newer than last watermark that have JSONL
        rows = con.execute(
            "SELECT composerId, lastUpdatedAt FROM composerHeaders "
            "WHERE COALESCE(isArchived,0)=0 AND COALESCE(isSubagent,0)=0 "
            "AND lastUpdatedAt > ?",
            (last_ms,),
        ).fetchall()
        targets = [r[0] for r in rows if r[0] in jsonl_index]
        print(f"Sweep: {len(targets)} candidates newer than {last_ms}")
    else:
        # Backfill: every JSONL that has a header
        targets = sorted(both)
        print(f"Backfill: {len(targets)} JSONL∩header candidates")

    counts = Counter()
    touched: set[tuple[str, str]] = set()
    exported_at = now_iso_local()
    max_updated = last_ms

    for cid in targets:
        meta = jsonl_index.get(cid)
        if not meta:
            counts["skip_no_jsonl"] += 1
            continue
        status = export_one(con, cid, meta, exported_at, counts, touched)
        row = con.execute(
            "SELECT lastUpdatedAt FROM composerHeaders WHERE composerId=?", (cid,)
        ).fetchone()
        if row and row[0]:
            max_updated = max(max_updated, int(row[0]))
        counts["seen"] += 1
        counts[status] += 0  # ensure key exists

    for source_os, project_name in sorted(touched):
        os_folder = "WSL" if source_os == "wsl" else "Windows"
        project_dir = VAULT_CONV / os_folder / "Cursor" / project_name
        try:
            update_rollups(project_dir, source_os, project_name)
        except OSError as e:
            print(f"  warn: rollup update failed for {project_name}: {e}", file=sys.stderr)

    if args.sweep or args.backfill or args.composer_id:
        state["last_processed_updated_at"] = max_updated
        state["last_run_at"] = exported_at
        state["last_counts"] = dict(counts)
        save_state(state)

    con.close()
    print("=== Summary ===")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")
    print(f"Projects touched: {len(touched)}")
    return 0


def main():
    # Windows consoles often default to cp1252 — force UTF-8 for path/unicode output
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--backfill", action="store_true", help="Export all reconciled sessions")
    mode.add_argument("--sweep", action="store_true", help="Export sessions newer than watermark")
    mode.add_argument("--composer-id", help="Export one composer by UUID")
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--distro", help="WSL distro name (auto-detected if omitted)")
    ap.add_argument(
        "--archive-old",
        action="store_true",
        help="Archive flat pre-rewrite notes into _archive-pre-fix/ before exporting",
    )
    args = ap.parse_args()
    # Allow --backfill as the mutual exclusive target when only archive requested? No.
    try:
        return run(args)
    except Exception as e:
        print(f"FATAL: {type(e).__name__}: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
