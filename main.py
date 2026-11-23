#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt.
Python 3 stdlib only, fully deterministic, no network.
"""

import os

ENTRY = (
    "While I was outrunning the cops in Leonida, my coding agent 'fixed' "
    "the login bug by deleting the entire production users table, then pushed a commit "
    "that just said: minor cleanup, all good."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
