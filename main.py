#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-awe-20261121-1600.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a lighthouse vignette: the keeper climbs the iron stairs
after a storm, the sea flat to the horizon under a sky washed clean,
a great lens wiped one slow circle at a time, and the light turning
steady over dark water. Vast scale, small patient action, unhurried
rhythm, no instructions.
"""

import os

TEXT = (
    "The storm has passed and the lighthouse keeper climbs the iron "
    "stairs, coat still damp. Below, the sea lies flat to the horizon "
    "and the sky is washed clean. He wipes the great lens with a soft "
    "cloth, one slow circle at a time, and the light turns steady "
    "over the dark water."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
