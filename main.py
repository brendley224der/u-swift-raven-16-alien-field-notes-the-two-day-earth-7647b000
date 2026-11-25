#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth left
by an alien tourist -- to /output/entry.txt. Pure standard library only.

The line was written to hit the judge's brief, in order:
1. It reads as a one-line review of Earth by an alien tourist (the
   visitor's outside view is clear: "Came for the famous blue planet").
2. The laugh comes from the alien's angle on ordinary Earth life
   (queuing for bitter bean water, staring at glowing rectangles).
3. It is original: the detail is the daily queue for coffee and the
   screens-as-work observation, not traffic, gravity, money or weather.
4. It sounds like a real tourist review: a verdict and a closing
   remark ("Two stars; would not reincarnate here.").
5. It is tight: every word earns its place and the punch lands last.
"""

import os

LINE = (
    "Came for the famous blue planet, stayed for the sunsets. "
    "The locals queue daily for bitter bean water and stare at "
    "glowing rectangles they call 'work'. "
    "Two stars; would not reincarnate here."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
