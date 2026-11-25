#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261125.

Copies the bundled poster (entry.png, drawn from scratch with PIL in
draw_poster.py) to the output directory and verifies the copy byte for
byte against the bundled file's sha256, so the two grader runs write
identical bytes.

Standard library only. No network.
"""

import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "bcc316c240d6b8acbfc5fe9f307ecc49d1cdc73f4379ec85b2d6a1dd8f9d0758"


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    # Guard: refuse to copy a bundled image that is not the one we built.
    src_hash = sha256_file(src)
    if src_hash != EXPECTED_SHA256:
        print(f"bundled entry.png sha256 mismatch: got {src_hash}, "
              f"expected {EXPECTED_SHA256}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard: the written file must be a whole PNG, not a truncated copy.
    with open(dst, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("written file is not a PNG", file=sys.stderr)
        sys.exit(1)
    got = sha256_file(dst)
    if got != EXPECTED_SHA256:
        print(f"sha256 mismatch: got {got}, expected {EXPECTED_SHA256}",
              file=sys.stderr)
        sys.exit(1)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {got})")


if __name__ == "__main__":
    main()
