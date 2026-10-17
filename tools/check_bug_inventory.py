#!/usr/bin/env python3
"""Fail unless BUG_INVENTORY.md is an append-only extension of its committed version.

The committed content (git HEAD) must be a byte-for-byte prefix of the working
file, and entry ids must be sequential from BUG-0001 with no gaps or repeats.
"""
import re, subprocess, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
path = root / "BUG_INVENTORY.md"
current = path.read_text(encoding="utf-8")

head = subprocess.run(["git", "show", "HEAD:BUG_INVENTORY.md"], cwd=root, capture_output=True, text=True)
if head.returncode == 0 and not current.startswith(head.stdout):
    print("BUG_INVENTORY.md: committed content was modified; the file is append-only", file=sys.stderr)
    sys.exit(1)

ids = [int(m) for m in re.findall(r"^## BUG-(\d{4}) ", current, flags=re.M)]
if ids != list(range(1, len(ids) + 1)):
    print(f"BUG_INVENTORY.md: entry ids must run BUG-0001.. without gaps; found {ids}", file=sys.stderr)
    sys.exit(1)
print(f"bug inventory OK ({len(ids)} entries, append-only)")
