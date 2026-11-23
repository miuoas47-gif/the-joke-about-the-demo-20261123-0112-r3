"""The joke about the demo.

A tiny, deterministic program: it writes one one-line joke about
working beside AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt
(the grader's output directory, /output by default).

No arguments, no network, no randomness, no clock: every run writes
the exact same bytes, so the output is byte-identical across runs.
"""

import os
import sys

# SPDX-License-Identifier: MIT

JOKE = (
    "My AI coding agent and I make a great team: it writes a thousand "
    "lines before lunch, and I spend the afternoon deleting nine hundred "
    "of them \u2014 with a smile."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
