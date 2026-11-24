#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one one-liner (111 characters) to /output/entry.txt.
Deterministic: the same text on every run. Standard library only,
no network, no input files.
"""

from pathlib import Path

LINE = "I delivered it on time in the timeline where your deadline is next Tuesday. Unfortunately, we live in this one."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} chars, must be 1-200")
    output.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {output}")


if __name__ == "__main__":
    main()
