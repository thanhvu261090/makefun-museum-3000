#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes one museum label, the label a museum in the year 3000 puts
beside an ordinary object from today, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "CAPTCHA, c. 2024. Citizens proved they were human by identifying traffic lights. The robots passed on the first try."
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be one line"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, over {MAX_CHARS}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
