#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Refuse to judge a stale build: the review checks and triage read canonical/, which `node engine/dist/main.js build`
writes from the model sources, and engine/dist/, which `npm run compile` writes from engine/src. After a merge or
an edit the outputs can lag the sources and give false findings.

The build rewrites every canonical file of its year, so canonical/<year>/ is stale when a source file of that year
(forms, tables, params and ambiguities, federal and New York, and the shared schema) is newer than its oldest output;
engine/dist is stale when an engine/src file is newer than engine/dist/main.js. The year is taxyear.py's (`--year N`,
else the newest adopted): adopting or editing another year does not make this year's build stale.

The rendered English (rendered/, tracked) is a second output: `node engine/dist/main.js render` writes it from
canonical/, and the build does not. The render, screen, false-no and question reviews send it to the model, and a
render log's subject is its hash, so a review made after an edit and a build but before a render reads the text from
before the edit and its log looks current. rendered/ is stale when a file differs from what canonical/ renders to
(the engine's `render --check`, a comparison of contents; about half a second for both jurisdictions).

    build_fresh.py              exit 1 with the reason when the build is stale
    build_fresh.py --rendered   also exit 1 when rendered/ is not what the build renders to
    build_fresh.py --self-test  (the rendered part needs a compiled engine and a build)

From Python: `build_fresh.require()` exits with the reason; `build_fresh.require(rendered=True)`, for a tool that
reads rendered/, also exits when rendered/ is stale, naming the files and the command that regenerates them.
"""
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED_SOURCES = ("schema",)
FIX = "rebuild: npm run compile && node engine/dist/main.js build"


def _files(path, suffixes=None):
    if path.is_file():
        yield path
    elif path.is_dir():
        for p in path.rglob("*"):
            if p.is_file() and (suffixes is None or p.suffix in suffixes):
                yield p


def year_sources(root, year):
    """The files the build of `year` reads: its directories and files under forms, tables, params and ambiguities
    (federal, and New York under the `ny` folder), and the shared schema."""
    y = str(year)
    for top in ("forms", "tables"):
        yield from _files(root / top / y)
        yield from _files(root / top / "ny" / y)
    for top in ("params", "ambiguities"):
        yield from _files(root / top / f"{y}.yaml")
        yield from _files(root / top / "ny" / f"{y}.yaml")
    for s in SHARED_SOURCES:
        yield from _files(root / s)


def stale(root=ROOT, year=None):
    """The reason the build of `year` (default: taxyear.py's) is stale, or None."""
    if year is None:
        import taxyear
        year = taxyear.YEAR
    outputs = list(_files(root / "canonical" / str(year), {".json"}))
    if not outputs:
        return f"canonical/{year}/ is empty; {FIX} --year {year}"
    oldest = min(p.stat().st_mtime for p in outputs)
    newest_src = max(year_sources(root, year), key=lambda p: p.stat().st_mtime, default=None)
    if newest_src is not None and newest_src.stat().st_mtime > oldest:
        return f"canonical/{year}/ is older than {newest_src.relative_to(root)}; {FIX} --year {year}"
    main = root / "engine" / "dist" / "main.js"
    newest_ts = max(_files(root / "engine" / "src", {".ts"}), key=lambda p: p.stat().st_mtime, default=None)
    if newest_ts is not None and (not main.exists() or newest_ts.stat().st_mtime > main.stat().st_mtime):
        return f"engine/dist is older than {newest_ts.relative_to(root)}; {FIX}"
    return None


def _render_cmd(root, ny, year_args):
    return ["node", str(root / "engine" / "dist" / "main.js"), "render", *(["--ny"] if ny else []), *year_args]


def unrendered(root=ROOT, out=None):
    """The reason rendered/ is not what canonical/ renders to, or None. Both jurisdictions are compared: a New York
    review also reads federal renderings. `out` names a directory whose `federal` and `ny` folders are compared
    instead of rendered/ (the self-test's)."""
    import taxyear
    found, fixes = [], []
    for ny in (False, True):
        if ny and not (root / "forms" / "ny" / taxyear.Y).is_dir():
            continue
        cmd = _render_cmd(root, ny, taxyear.YEAR_ARGS)
        where = ["--out", str(Path(out) / ("ny" if ny else "federal"))] if out else []
        r = subprocess.run([*cmd, "--check", *where], cwd=root, capture_output=True, text=True)
        if r.returncode == 1:
            found += r.stdout.strip().splitlines()
            fixes.append(" ".join(["node", "engine/dist/main.js", *cmd[2:], *where]))
        elif r.returncode != 0:
            return f"rendered/ could not be compared with the build ({(r.stderr.strip().splitlines() or ['no output'])[-1]}); {FIX}"
    if not found:
        return None
    shown = "; ".join(found[:3]) + (f"; and {len(found) - 3} more" if len(found) > 3 else "")
    return (f"{len(found)} rendered file(s) are not what the current build renders to ({shown}), so a review would read "
            f"text from before the last edit; regenerate: {' && '.join(fixes)}")


def rendered_stale(root=ROOT):
    """Why a tool that reads rendered/ must not run, as ("build" | "rendered text", reason), or None."""
    why = stale(root)
    if why:
        return "build", why
    why = unrendered(root)
    return ("rendered text", why) if why else None


def _found(rendered):
    if rendered:
        return rendered_stale()
    why = stale()
    return ("build", why) if why else None


def require(rendered=False):
    """Exit with the reason when the build is stale or, with `rendered`, when rendered/ is."""
    found = _found(rendered)
    if found:
        sys.exit(f"stale {found[0]}: {found[1]}")


def _rendered_self_test(bad):
    """Render into a temporary directory, plant each kind of stale file and check that each is named."""
    import taxyear
    if not (ROOT / "engine" / "dist" / "main.js").exists() or not any(_files(ROOT / "canonical" / taxyear.Y, {".json"})):
        bad.append(f"the rendered part needs a compiled engine and a build ({FIX})")
        return
    with tempfile.TemporaryDirectory() as d:
        out = Path(d)
        for ny in (False, True):
            if ny and not (ROOT / "forms" / "ny" / taxyear.Y).is_dir():
                continue
            subprocess.run([*_render_cmd(ROOT, ny, taxyear.YEAR_ARGS), "--out", str(out / ("ny" if ny else "federal"))],
                           cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        if unrendered(ROOT, out) is not None:
            bad.append(f"a fresh rendering reported stale: {unrendered(ROOT, out)}")
        docs = sorted(p for p in (out / "federal").glob("*.md") if "- **Encoded (" in p.read_text(encoding="utf-8"))
        if len(docs) < 2:
            bad.append("no rendered documents to plant a stale state in")
            return
        # The trap itself: one line's English as it read before an edit.
        edited, removed = docs[0], docs[1]
        edited.write_text(edited.read_text(encoding="utf-8").replace("- **Encoded (", "- **Encoded before the edit (", 1),
                          encoding="utf-8")
        why = unrendered(ROOT, out) or ""
        if f"{edited.name}: differs" not in why or "1 rendered file(s)" not in why:
            bad.append(f"an edited line not detected: {why!r}")
        if "regenerate: node engine/dist/main.js render " not in why or "--ny" in why.split("regenerate:")[-1]:
            bad.append(f"the refusal does not name the federal render command alone: {why!r}")
        removed.unlink()
        (out / "federal" / "left_over.md").write_text("x", encoding="utf-8")
        why = unrendered(ROOT, out) or ""
        for want in (f"{removed.name}: missing", "left_over.md: not part of the rendering", "3 rendered file(s)"):
            if want not in why:
                bad.append(f"{want!r} not in the refusal: {why!r}")


def self_test():
    bad = []
    with tempfile.TemporaryDirectory() as d:
        r = Path(d)
        for p in ("forms/2025/a.yaml", "forms/2026/b.yaml", "engine/src/main.ts"):
            (r / p).parent.mkdir(parents=True, exist_ok=True)
            (r / p).write_text("x")
        if not (stale(r, 2025) or "").startswith("canonical/2025/ is empty"):
            bad.append("empty canonical")
        t = time.time()
        for p in ("forms/2025/a.yaml", "forms/2026/b.yaml", "engine/src/main.ts"):
            os.utime(r / p, (t - 100, t - 100))
        for p in ("canonical/2025/a.json", "engine/dist/main.js"):
            (r / p).parent.mkdir(parents=True, exist_ok=True)
            (r / p).write_text("x")
        if stale(r, 2025) is not None:
            bad.append("fresh build reported stale")
        os.utime(r / "forms/2026/b.yaml", (t + 100, t + 100))
        if stale(r, 2025) is not None:
            bad.append("an edit of another year made this year's build stale")
        if not (stale(r, 2026) or "").startswith("canonical/2026/ is empty"):
            bad.append("a year with no build was not reported empty")
        os.utime(r / "forms/2025/a.yaml", (t + 100, t + 100))
        if "forms/2025/a.yaml" not in (stale(r, 2025) or ""):
            bad.append("edited form not detected")
        os.utime(r / "forms/2025/a.yaml", (t - 100, t - 100)); os.utime(r / "engine/src/main.ts", (t + 100, t + 100))
        if "engine/dist" not in (stale(r, 2025) or ""):
            bad.append("edited engine source not detected")
    _rendered_self_test(bad)
    print("build_fresh self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    found = _found("--rendered" in sys.argv)
    if found:
        print(f"stale {found[0]}: {found[1]}", file=sys.stderr)
        sys.exit(1)
    print("build and rendered text fresh" if "--rendered" in sys.argv else "build fresh")
