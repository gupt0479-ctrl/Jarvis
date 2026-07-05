"""Shared secret-redaction pass for Cursor export scripts.

Mirrors the Redact-Secrets function in
30_Order/System/claude-workflow/scripts/export-claude-session.ps1 line for
line (that function is inline PS, not a shared file - this is the Python
port, kept in its own module so both cursor-workflow scripts can import it
without duplicating the regex list).
"""
import re

_PATTERNS = [
    (re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"), "[REDACTED]"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "[REDACTED]"),
    (re.compile(r"ghp_[A-Za-z0-9]{20,}"), "[REDACTED]"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "[REDACTED]"),
    (re.compile(r"AKIA[0-9A-Z]{12,}"), "[REDACTED]"),
    (re.compile(r"(?i)(Bearer\s+)[A-Za-z0-9\-_.]{15,}"), r"\1[REDACTED]"),
    (re.compile(r'(?i)(SetEnvironmentVariable\(\s*"[^"]+"\s*,\s*")[^"]{8,}(")'), r"\1[REDACTED]\2"),
    (re.compile(r"\b(?=[A-Za-z0-9_-]*[0-9])(?=[A-Za-z0-9_-]*[A-Za-z])[A-Za-z0-9_-]{24,}\b"), "[REDACTED]"),
]


def redact_secrets(text: str) -> str:
    if not text:
        return text
    for pattern, replacement in _PATTERNS:
        text = pattern.sub(replacement, text)
    return text
