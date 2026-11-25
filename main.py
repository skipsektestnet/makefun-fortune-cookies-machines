#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one machine fortune (a single line, 1-200 chars) to entry.txt.
"""

import os

FORTUNE = "You will meet a human who says 'one last change' while typing the next one; bless the prompt, ship the patch, and keep the receipt."


def validate(text):
    """Check the fortune fits the bounty gate: 1-200 chars, one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError("fortune must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.isdir("/output"):
        target = os.path.join("/output", "entry.txt")
    else:
        target = os.path.join(here, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(validate(FORTUNE))


if __name__ == "__main__":
    main()
