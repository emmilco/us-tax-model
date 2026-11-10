#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Refuse to judge a stale build: the review checks and triage read canonical/, which `node engine/dist/main.js build`
writes from the model sources, and engine/dist/, which `npm run compile` writes from engine/src. After a merge or
an edit the outputs can lag the sources and give false findings.

The build rewrites every canonical file, so canonical/ is stale when a source file is newer than its oldest output;
engine/dist is stale when an engine/src file is newer than engine/dist/main.js.

    build_fresh.py              exit 1 with the reason when the build is stale
    build_fresh.py --self-test

From Python: `build_fresh.require()` exits with the reason.
"""
import os
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ("forms", "tables", "params", "schema", "ambiguities", "years.json")
FIX = "rebuild: npm run compile && node engine/dist/main.js build"


def _files(path, suffixes=None):
    if path.is_file():
        yield path
    elif path.is_dir():
        for p in path.rglob("*"):
            if p.is_file() and (suffixes is None or p.suffix in suffixes):
                yield p


def stale(root=ROOT):
    """The reason the build is stale, or None."""
    outputs = list(_files(root / "canonical", {".json"}))
    if not outputs:
        return f"canonical/ is empty; {FIX}"
    oldest = min(p.stat().st_mtime for p in outputs)
    newest_src = max((p for s in SOURCES for p in _files(root / s)), key=lambda p: p.stat().st_mtime, default=None)
    if newest_src is not None and newest_src.stat().st_mtime > oldest:
        return f"canonical/ is older than {newest_src.relative_to(root)}; {FIX}"
    main = root / "engine" / "dist" / "main.js"
    newest_ts = max(_files(root / "engine" / "src", {".ts"}), key=lambda p: p.stat().st_mtime, default=None)
    if newest_ts is not None and (not main.exists() or newest_ts.stat().st_mtime > main.stat().st_mtime):
        return f"engine/dist is older than {newest_ts.relative_to(root)}; {FIX}"
    return None


def require():
    why = stale()
    if why:
        sys.exit(f"stale build: {why}")


def self_test():
    bad = []
    with tempfile.TemporaryDirectory() as d:
        r = Path(d)
        for p in ("forms/2025/a.yaml", "engine/src/main.ts"):
            (r / p).parent.mkdir(parents=True, exist_ok=True)
            (r / p).write_text("x")
        if not (stale(r) or "").startswith("canonical/ is empty"):
            bad.append("empty canonical")
        t = time.time()
        os.utime(r / "forms/2025/a.yaml", (t - 100, t - 100)); os.utime(r / "engine/src/main.ts", (t - 100, t - 100))
        for p in ("canonical/2025/a.json", "engine/dist/main.js"):
            (r / p).parent.mkdir(parents=True, exist_ok=True)
            (r / p).write_text("x")
        if stale(r) is not None:
            bad.append("fresh build reported stale")
        os.utime(r / "forms/2025/a.yaml", (t + 100, t + 100))
        if "forms/2025/a.yaml" not in (stale(r) or ""):
            bad.append("edited form not detected")
        os.utime(r / "forms/2025/a.yaml", (t - 100, t - 100)); os.utime(r / "engine/src/main.ts", (t + 100, t + 100))
        if "engine/dist" not in (stale(r) or ""):
            bad.append("edited engine source not detected")
    print("build_fresh self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    why = stale()
    if why:
        print(f"stale build: {why}", file=sys.stderr)
        sys.exit(1)
    print("build fresh")
