#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes a single joke about Monday mornings (at most 200 characters)
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

JOKE = "Monday morning is proof my weekend was a free trial: great features, and now it wants my card."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
