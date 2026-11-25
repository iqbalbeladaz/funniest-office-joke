#!/usr/bin/env python3
"""The Funniest Office Joke entry.

Writes one office joke to /output/entry.txt. The joke is a fixed,
deterministic string: every run produces byte-identical output.
"""

import os

JOKE = (
    "My manager said the meeting could have been an email, then sent a "
    "calendar invite for a meeting to discuss why the meeting could have "
    "been an email."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
