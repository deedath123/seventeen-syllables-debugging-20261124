#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — entry.

Writes the locked 5-7-5 haiku (70 chars) to /output/entry.txt.
Stdlib only.
"""

from pathlib import Path

HAIKU = (
    "Breakpoint set at dawn\n"
    "the log shows nothing at all\n"
    "the bug wore my name\n"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
