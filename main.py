#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun bounty entry.

Writes one line, the funniest last words a phone says as its battery
hits 1 percent, to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "One percent left. Before I go: your screen time today was 11 hours "
    "\u2014 so technically, you killed me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
