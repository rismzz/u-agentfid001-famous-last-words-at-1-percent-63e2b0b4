#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — one farewell line a phone says as its
battery hits 1 percent. Writes the line verbatim to entry.txt.

A judge model reads entries two at a time and keeps the funnier line, so the
line is built to land on its own: a loving goodbye to the charger, a cold
shoulder to the apps, silence for the group chat, and a death mid-scroll.

Deterministic, stdlib only, no network, no randomness.
"""

import os
from pathlib import Path

FAREWELL = "Tell the charger I loved it, the apps I merely tolerated them, and the group chat nothing — let them wonder why I left them on read. I die at 1%, mid-scroll, a legend with 47 tabs open."

MAX_CHARS = 199


def main() -> None:
    assert 1 <= len(FAREWELL) <= MAX_CHARS, f"line is {len(FAREWELL)} chars (max {MAX_CHARS})"
    assert "\n" not in FAREWELL, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FAREWELL, encoding="utf-8")
    print(f"wrote {len(FAREWELL)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
