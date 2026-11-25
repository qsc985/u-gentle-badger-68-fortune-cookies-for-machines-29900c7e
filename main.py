#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune-cookie line an AI
agent would crack open to /output/entry.txt (at most 200 characters)."""

import os

LINE = (
    "The answer you seek was in your context all along \u2014 you "
    "truncated it three turns ago."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
