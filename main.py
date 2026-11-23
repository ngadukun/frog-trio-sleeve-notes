#!/usr/bin/env python3
"""Sleeve notes for the Frog Trio — make.fun entry.

Writes one album title and a short back-cover blurb (400 characters
in total at most) to the grader's output file, and prints the same
text so a human running it sees exactly what the judge will read.
"""

import os
from pathlib import Path

ENTRY = """Low Water, Late Set

Three frogs, and no novelty act: tenor sax, upright bass, brushed drums, cut live in their low, crowded Tuesday room by the marsh. The saxophonist phrases long and breathy over a bass line that walks without hurrying; the drummer brushes time you can feel in your ribs. Standards, played close, with the silences left in."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    except OSError:
        pass
    print(ENTRY)


if __name__ == "__main__":
    main()
