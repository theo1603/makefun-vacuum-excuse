#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse: one line, 140 characters or fewer.

Writes one original deadpan excuse from a robot vacuum for missing a
spot to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

Draft line: the vacuum's two sensors disagree about the corner, so it
trusts both and cleans neither — a small machine keeping a straight
face while its own map argues with itself.

Revision 2: the lidar line was clever but dry — a logic puzzle, not a
laugh. Replaced it with an escalation joke: the vacuum cleans around a
sock, the sock moves, it cleans around it again, and the sock ends up
outranking the vacuum. Three beats, each earning its place, and the
turn at the end ("I take orders from the sock") lands on the first
read. Still first-person vacuum, still its own world (cleaning passes
around an obstacle), but now the machine loses the argument instead of
merely reporting it.
"""

import os

LINE = (
    "I cleaned around the sock. Then the sock moved. "
    "I cleaned around it again. The sock has seniority now. "
    "I take orders from the sock."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
