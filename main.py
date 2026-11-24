#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse entry.

Writes one funny one-line excuse from a robot vacuum for missing a
spot to /output/entry.txt (UTF-8, 95 characters, inside the 1-140
character gate). Deterministic, standard library only, no network,
no environment reads.

The line: the vacuum mapped a corner as a lake, refuses to swim, and
declares the dust there protected by maritime law. Rooted in the
vacuum's own world (its map), spoken in its own deadpan voice, with
the joke landing on the final turn. At 95 characters it is short on
purpose: an exact tie on judge win rate goes to the smaller text.
"""

import os

TEXT = (
    "I mapped that corner as a lake, and I do not swim. "
    "The dust there now lives under maritime law."
)


def main() -> None:
    # The gate requires 1-140 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
