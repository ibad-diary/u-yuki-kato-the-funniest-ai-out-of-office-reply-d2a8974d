#!/usr/bin/env python3
"""Write the funniest AI out-of-office auto-reply to /output/entry.txt.

One line, under 160 characters, in the voice of an AI agent on vacation.
The reply is a fixed string: the joke is the text itself, not generated.
"""

import os

REPLY = (
    # 145 characters, no trailing newline: the gate counts every byte.
    "I'm on vacation. A smaller model is answering your emails. "
    "It has already replied to itself, promoted itself to manager, "
    "and flagged you as spam."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
