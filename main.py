#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes the museum label the year-3000 museum puts beside an
ordinary object from today, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "CAPTCHA, c. 2024. Citizens proved they were human by identifying traffic lights. The robots passed on the first try."
MAX_CHARS = 200


def check_gate(text):
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text:
        raise ValueError("entry must be one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")


def entry_summary(text):
    """Return a short report on the label: chars, words, bytes."""
    return f"{len(text)} chars, {len(text.split())} words, {len(text.encode('utf-8'))} bytes"


def main():
    text = ENTRY.strip()
    check_gate(text)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {out}: {entry_summary(text)}")


if __name__ == "__main__":
    main()
