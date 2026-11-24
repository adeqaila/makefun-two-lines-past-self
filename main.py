#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry (slot 1).

Writes the tournament-winning two-line warning to /output/entry.txt.
Deterministic, no network, no input, no secrets.

Winner (see candidates.md for the full 16-candidate tournament):
the art-school letter — the tightest cause-and-effect chain in the field,
with a twist that sharpens the moment instead of showing off.
"""

import os

ENTRY = (
    "Open the thin envelope from the art school at the kitchen table, not in the car.\n"
    "You read the rejection in the wrong light and never saw the second page, "
    "the one that offered you a place on the waiting list.\n"
)


def main():
    # Gate self-check (mirror of the sealed scorer): UTF-8 text, 1-280 chars,
    # not only whitespace, exactly two lines, one sentence per line.
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} outside 1-280"
    assert ENTRY.strip(), "entry is only whitespace"
    lines = ENTRY.rstrip("\n").split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip().endswith("."), f"line is not one sentence: {line!r}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
