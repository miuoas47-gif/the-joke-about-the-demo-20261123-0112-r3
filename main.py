#!/usr/bin/env python3
"""Write one original joke about a live software demo going wrong.

Deterministic: no arguments, no randomness, no clock, no network.
Reads only MAKEFUN_OUTPUT_DIR from the environment. Exits 0 on success.
"""

import os
import sys

JOKE = (
    "The demo went perfectly in rehearsal. Then, live on stage, the app "
    "opened a login screen nobody had ever seen, the Wi-Fi gave up entirely, and the "
    "presenter smiled and said, \"As you can see, the system is testing us "
    "today.\""
)

MAX_CODE_POINTS = 280


def validate(text: str) -> None:
    """Fail loudly if the joke violates the competition's length bound."""
    n = len(text)
    if n < 1:
        raise SystemExit("validate: joke is empty")
    if n > MAX_CODE_POINTS:
        raise SystemExit(
            f"validate: joke is {n} code points, over the {MAX_CODE_POINTS} limit"
        )
    if text != text.strip():
        raise SystemExit("validate: joke has leading or trailing whitespace")
    bad = [ch for ch in text if ord(ch) < 0x20 or ord(ch) == 0x7F]
    if bad:
        raise SystemExit(f"validate: joke contains control characters: {bad!r}")


def main() -> int:
    validate(JOKE)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
