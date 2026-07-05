#!/usr/bin/env python3
"""Run a cursor-workflow script; on WSL /mnt/c SQLite disk I/O error, retry via Windows Python.

Cursor holds a lock on state.vscdb while running. Reading that file from WSL
through /mnt/c often raises sqlite3.OperationalError: disk I/O error. This
wrapper tries the local interpreter first, then re-invokes the same script with
Windows paths when that specific failure is detected on WSL.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path, PureWindowsPath


def is_wsl() -> bool:
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except OSError:
        return False


def wsl_path_to_windows(path: str) -> str:
    if not path.startswith("/mnt/"):
        return path
    if len(path) < 7 or path[6] != "/":
        return path
    drive = path[5].upper()
    rest = path[7:].replace("/", "\\")
    return f"{drive}:\\{rest}"


def windows_python_candidates() -> list[str]:
    candidates = [
        os.environ.get("CURSOR_WINDOWS_PYTHON", ""),
        r"C:\Python313\python.exe",
        r"C:\Users\Anant Gupta\AppData\Local\Programs\Python\Python313\python.exe",
        r"C:\Users\Anant Gupta\AppData\Local\Microsoft\WindowsApps\python.exe",
    ]
    seen: set[str] = set()
    out: list[str] = []
    for c in candidates:
        if not c or c in seen:
            continue
        seen.add(c)
        win = wsl_path_to_windows(c) if c.startswith("/mnt/") else c
        if Path(win).exists() or win.endswith("python.exe"):
            out.append(win)
    return out


def translate_args_for_windows(args: list[str]) -> list[str]:
    return [wsl_path_to_windows(a) if a.startswith("/mnt/") else a for a in args]


def run_script(exe: str, script: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [exe, str(script), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def emit_result(result: subprocess.CompletedProcess[str]) -> int:
    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)
    return result.returncode


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: cursor-db-run.py <script.py> [script args...]\n"
            "Example: cursor-db-run.py list-cursor-composers.py --jarvis-only --limit 5 "
            "--db '/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/state.vscdb'",
            file=sys.stderr,
        )
        sys.exit(1)

    script = Path(sys.argv[1]).resolve()
    args = sys.argv[2:]

    if not script.exists():
        print(f"Script not found: {script}", file=sys.stderr)
        sys.exit(1)

    result = run_script(sys.executable, script, args)
    combined = (result.stdout or "") + (result.stderr or "")
    if result.returncode == 0 or not is_wsl() or "disk I/O error" not in combined:
        sys.exit(emit_result(result))

    win_script = wsl_path_to_windows(str(script))
    win_args = translate_args_for_windows(args)

    for win_python in windows_python_candidates():
        print(
            f"WSL /mnt/c SQLite lock detected; retrying via Windows Python ({win_python})...",
            file=sys.stderr,
        )
        fallback = run_script(win_python, Path(win_script), win_args)
        if fallback.returncode == 0:
            sys.exit(emit_result(fallback))
        fb_combined = (fallback.stdout or "") + (fallback.stderr or "")
        if "disk I/O error" not in fb_combined and fallback.returncode != 0:
            sys.exit(emit_result(fallback))

    print(
        "disk I/O error persisted after Windows fallback. Close Cursor and retry, "
        "or run the script from Windows PowerShell.",
        file=sys.stderr,
    )
    sys.exit(emit_result(result))


if __name__ == "__main__":
    main()
