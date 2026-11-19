# SPDX-License-Identifier: MIT
"""Place the finished front-page picture where the grader expects it.

The picture is stored in this repository as entry.png. This script does
nothing but copy those exact bytes to <output>/entry.png, where <output>
is MAKEFUN_OUTPUT_DIR when that variable is set and /output otherwise.
It runs on Python 3.13 with the standard library alone: no network, no
clock, and no file outside this repository is ever read, so every run
writes the same bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path(DEFAULT_OUTPUT_DIR)


def copy_image(source: Path, target: Path) -> int:
    """Copy the finished picture and verify the copy byte for byte.

    Returns the number of bytes written. Raises SystemExit with a clear
    message when the source is missing or the copy does not match.
    """
    if not source.is_file():
        print(f"error: source image {source} does not exist", file=sys.stderr)
        raise SystemExit(1)

    data = source.read_bytes()
    if not data:
        print(f"error: source image {source} is empty", file=sys.stderr)
        raise SystemExit(1)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

    written = target.stat().st_size
    if written != len(data):
        print(
            f"error: wrote {written} bytes to {target}, "
            f"expected {len(data)}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    if hashlib.sha256(target.read_bytes()).hexdigest() != hashlib.sha256(
        data
    ).hexdigest():
        print(f"error: bytes written to {target} differ from source",
              file=sys.stderr)
        raise SystemExit(1)

    return written


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    target = output_dir() / IMAGE_NAME

    written = copy_image(source, target)
    print(f"wrote {target} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
