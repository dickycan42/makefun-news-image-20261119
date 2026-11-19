# SPDX-License-Identifier: MIT
"""Place the finished front-page picture where the grader expects it.

The picture is stored in this repository as entry.png. This script does
nothing but copy those exact bytes to <output>/entry.png, where <output>
is MAKEFUN_OUTPUT_DIR when that variable is set and /output otherwise.
It runs on Python 3.13 with the standard library alone: no network, no
clock, and no file outside this repository is ever read, so every run
writes the same bytes.
"""

import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path(DEFAULT_OUTPUT_DIR)


def run() -> int:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print(f"error: {source} is missing", file=sys.stderr)
        return 1

    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME

    data = source.read_bytes()
    target.write_bytes(data)

    written = target.stat().st_size
    if written != len(data):
        print(
            f"error: wrote {written} bytes to {target}, "
            f"expected {len(data)}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {target} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
