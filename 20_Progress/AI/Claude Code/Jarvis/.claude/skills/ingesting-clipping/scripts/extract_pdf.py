#!/usr/bin/env python3
"""
Jarvis PDF extractor for ingesting-clipping.
Usage: python extract_pdf.py "<windows_path_to_pdf>"

Tries pypdf text extraction first.
If output is sparse (< 200 chars/page average), prints a warning and exits with
code 2 to signal the caller to fall back to Claude's multimodal Read tool.

Exit codes:
  0 - extraction succeeded; per-page text printed to stdout
  1 - file not found or pypdf not installed
  2 - sparse output; PDF is scanned/image-based, use multimodal Read instead
"""
import sys
import pathlib


def extract(pdf_path: str) -> None:
    path = pathlib.Path(pdf_path)
    if not path.exists():
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    try:
        import pypdf
    except ImportError:
        print(
            "ERROR: pypdf not installed. Run: pip install pypdf --break-system-packages",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    reader = pypdf.PdfReader(str(path))
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    total_chars = 0
    page_texts = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        page_texts.append((i + 1, text))
        total_chars += len(text.strip())

    avg_chars = total_chars / total_pages if total_pages > 0 else 0

    if avg_chars < 200:
        print(
            f"\nWARNING: Average {avg_chars:.0f} chars/page — likely a scanned/image-based PDF.\n"
            "ACTION REQUIRED: Use Claude's multimodal Read tool instead of pypdf.\n"
            "Pass the PDF file path to the Read tool. Claude will see each page as an image.\n"
            "Do NOT continue with pypdf output — it is not reliable for this file.\n"
        )
        sys.exit(2)  # Exit code 2 = fallback needed

    for page_num, text in page_texts:
        print(f"\n=== Page {page_num} ===")
        print(text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <path_to_pdf>", file=sys.stderr)
        sys.exit(1)
    extract(sys.argv[1])
