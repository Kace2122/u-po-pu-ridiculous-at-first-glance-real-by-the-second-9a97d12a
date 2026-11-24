#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt.
"""

import os

ENTRY = (
    "We sell naming rights to potholes: cities auction each crater to local "
    "businesses, whose logo gets stencilled around it until the road is "
    "fixed, so the worse the road, the higher the bid."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate self-check: one sentence, 1-200 chars, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
