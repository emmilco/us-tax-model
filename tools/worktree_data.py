#!/usr/bin/env python3
"""The git-ignored data of a checkout: check that the review data the logs reference is here, clone it
into a linked worktree (an agent's) from the main worktree, and carry back what the worktree added.

    worktree_data.py check [--list]
        exit 1, naming what is missing and how to clone it in, when a raw review file the review logs
        reference is missing from this checkout (--list: print every referenced path and exit 0).
        tools/check_all.sh and tools/check_all_bg.sh run it before anything else
    worktree_data.py clone <worktree> [--main DIR]
        replace the worktree's copies of the review data (DATA) and the installs (INSTALLS) with complete
        copy-on-write clones of the main worktree's (cp -cR; never links), and write the clone's base:
        the hash of every untracked review-data file as cloned, and each ledger's length and hash.
        Refused when a tracked file under DATA has uncommitted changes in the worktree
    worktree_data.py carry-back <worktree> [--main DIR] [--dry-run] [--prefer-worktree PATH...]
        bring back into the main worktree what the worktree changed since its clone:
          ledgers (costs.jsonl): the rows the worktree appended after the clone point are appended to the
            main ledger. Refused unless the worktree's ledger and the main one both still begin with the
            ledger as cloned (an edited or truncated ledger is not appended to)
          other review files: a file the worktree changed or added since the base is copied into the main
            worktree when the main copy is still the base's (or absent in both base and main) or already
            equal to the worktree's; a file both changed differently is a conflict, and any conflict refuses
            the whole carry-back before anything is written. A file the worktree deleted is reported, not
            deleted. Files git tracks travel with the worktree's commits and are left out
        --prefer-worktree PATH...: repo-relative paths (globs the shell expands are fine). Each named
          non-ledger file that is a both-changed conflict is copied from the worktree over main's instead
          of refusing, and reported as such; a named file not in conflict is reported and handled as
          usual; a ledger path is an error. Every other conflict still refuses
        The base then moves to what was carried, so a second carry-back brings only what came after.
    worktree_data.py fill <worktree> [--main DIR] [--dry-run]
        copy into the worktree each untracked review file the main worktree has and the worktree lacks.
        Add-only: an existing worktree file is never overwritten or deleted, ledgers (costs.jsonl) are
        never touched, and uncommitted tracked files do not matter. Each filled file is recorded in the
        base at the hash of main's copy, so a later carry-back treats it as unchanged unless the worktree
        edits it. Without a base the files are copied and nothing is recorded (carry-back is refused
        for such a worktree anyway)
    worktree_data.py --self-test

Why the check: the review logs (tracked, under reviews/) name the raw model requests and replies they
rest on, which are git-ignored (.transcription/, .classm/): a transcription or render log's own request,
reply and metadata (.transcription/<stem>.{prompt.txt,response.txt,meta.json}, with <stem>.render for a
render log), and every receipt or class M request a log or rulings file names by path. The review checks
(compare_families.py, check_logs.py) treat a missing one as a review not yet verified rather than as an
error, so a checkout holding only part of the data (a linked worktree gets the tracked files and none of
the ignored ones) would write different reports and still pass. Adjudication notes and findings files are
prose and are not held to this.

The base lives in the worktree's git directory (`git rev-parse --git-path data-clone-base.json`), outside
every data folder. The main worktree is the clone's first (`git worktree list`). clone writes only the
worktree; carry-back writes only the main worktree's data folders and the base.
"""
import argparse
import contextlib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = (".transcription", ".classm", ".human-review", ".extraction-review", ".direct-file")
INSTALLS = ("node_modules", ".engines", "lean/.lake")
LEDGER = "costs.jsonl"
REF = re.compile(r"(\.(?:transcription|classm)/[A-Za-z0-9_./-]+)")
SUFFIXES = (".prompt.txt", ".response.txt", ".meta.json")


# --- check -------------------------------------------------------------------------------------------

def review_files(root):
    """The review logs and rulings files that hold machine-checked references (relative paths)."""
    out = []
    for dirpath, dirnames, filenames in os.walk(root / "reviews"):
        dirnames[:] = [d for d in dirnames if d != "adjudication"]
        if os.path.basename(dirpath) not in ("transcription", "render", "classm"):
            continue
        for f in filenames:
            if (f.endswith(".md") or f.endswith(".json")) and not f.endswith(".findings.md"):
                out.append(os.path.relpath(os.path.join(dirpath, f), root))
    return sorted(out)


def referenced(root=ROOT):
    """path (relative: a file, or a receipt base taking SUFFIXES) -> the first review file naming it."""
    refs = {}
    for f in review_files(root):
        text = (root / f).read_text(encoding="utf-8", errors="replace")
        for m in REF.findall(text):
            refs.setdefault(m.rstrip("."), f)
        parts = f.split("/")
        if f.endswith(".md") and parts[-2] in ("transcription", "render"):
            stem = parts[-1][:-3]
            refs.setdefault(f".transcription/{stem}" + (".render" if parts[-2] == "render" else ""), f)
    return refs


def present(root, ref):
    p = root / ref
    return p.exists() or all(Path(str(p) + s).is_file() for s in SUFFIXES)


def missing(root=ROOT):
    return {r: f for r, f in referenced(root).items() if not present(root, r)}


def check(root=ROOT, main=None, out=sys.stderr):
    gone = missing(root)
    if not gone:
        return 0
    print(f"check-all: {len(gone)} git-ignored review file(s) the review logs reference are missing here, so the "
          "review checks would pass on partial data; not running. For example:", file=out)
    for r, f in sorted(gone.items())[:5]:
        print(f"  {r} (named by {f})", file=out)
    if main is not None and main.resolve() != root.resolve():
        print("Clone the data in from the main worktree (copy-on-write clones replacing the partial copies; the "
              "clone's base is recorded so that `tools/worktree_data.py carry-back` can bring new reviews and cost "
              "rows back):", file=out)
        print(f"  python3 '{root / 'tools/worktree_data.py'}' clone '{root}'", file=out)
    else:
        print("Restore .transcription/ and .classm/ (the raw reviews are kept only locally; they are not in git). "
              "In a linked worktree, `tools/worktree_data.py clone <worktree>` clones them in from the main one.",
              file=out)
    return 1


# --- clone and carry-back ------------------------------------------------------------------------------

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tracked(root):
    """Paths git tracks under DATA in root (empty outside a git checkout)."""
    r = subprocess.run(["git", "ls-files", "-z", "--", *DATA], cwd=root, capture_output=True)
    if r.returncode != 0:
        return set()
    return {p for p in r.stdout.decode("utf-8", "surrogateescape").split("\0") if p}


def files(root, skip=frozenset()):
    """Relative path -> absolute path of every regular file under root's review data folders, but `skip`."""
    out = {}
    for d in DATA:
        base = root / d
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            for f in filenames:
                p = Path(dirpath) / f
                rel = str(p.relative_to(root))
                if rel not in skip and p.is_file() and not p.is_symlink():
                    out[rel] = p
    return out


def is_ledger(rel):
    return os.path.basename(rel) == LEDGER


def prefix(data):
    return {"length": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def base_of(worktree, main, skip):
    """The base record: the hash of each untracked review file of the worktree, and for each ledger the
    prefix carried so far in the worktree's copy and the prefix the main copy must still begin with."""
    out = {"files": {}, "ledgers": {}}
    mn = files(main, skip)
    for rel, p in files(worktree, skip).items():
        if is_ledger(rel):
            out["ledgers"][rel] = {"worktree": prefix(p.read_bytes()),
                                   "main": prefix(mn[rel].read_bytes() if rel in mn else b"")}
        else:
            out["files"][rel] = sha(p)
    return out


def begins(data, p):
    return len(data) >= p["length"] and hashlib.sha256(data[: p["length"]]).hexdigest() == p["sha256"]


def dirty_tracked(worktree):
    """Tracked files under DATA with uncommitted changes in the worktree (a clone would replace them)."""
    r = subprocess.run(["git", "status", "--porcelain", "-z", "--", *DATA], cwd=worktree, capture_output=True)
    if r.returncode != 0:
        return []
    return [e[3:] for e in r.stdout.decode("utf-8", "surrogateescape").split("\0") if e[:2].strip() and e[:2] != "??"]


def clone(main, worktree, manifest, run=subprocess.run):
    if main.resolve() == worktree.resolve():
        raise SystemExit("worktree_data: the worktree is the main worktree")
    dirty = dirty_tracked(worktree)
    if dirty:
        raise SystemExit("worktree_data: tracked files under the data folders have uncommitted changes in the "
                         "worktree, which a clone would replace; commit or restore them first:\n  " + "\n  ".join(dirty))
    for d in DATA + INSTALLS:
        src, dst = main / d, worktree / d
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        elif dst.exists():
            shutil.rmtree(dst)
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            run(["cp", "-cR", str(src), str(dst)], check=True)
    skip = tracked(worktree) | tracked(main)
    manifest.write_text(json.dumps(base_of(worktree, main, skip), indent=0, sort_keys=True))
    print(f"worktree_data: cloned {', '.join(d for d in DATA + INSTALLS if (main / d).exists())} into {worktree}; "
          f"base in {manifest}")
    changed = dirty_tracked(worktree)
    if changed:
        print("worktree_data: tracked files under the data folders now differ from the worktree's HEAD (the main "
              "worktree's copies differ from them):\n  " + "\n  ".join(changed))


def plan(main, worktree, base, skip):
    """(ledger appends {rel: bytes}, copies [rel], conflicts [str], deleted [rel])."""
    appends, copies, conflicts = {}, [], []
    wt, mn = files(worktree, skip), files(main, skip)
    for rel, b in base["ledgers"].items():
        if rel not in wt:
            conflicts.append(f"{rel}: the worktree's ledger is gone")
            continue
        w = wt[rel].read_bytes()
        m = mn[rel].read_bytes() if rel in mn else b""
        if not begins(w, b["worktree"]):
            conflicts.append(f"{rel}: the worktree's ledger no longer begins with the ledger as cloned or last carried")
            continue
        if not begins(m, b["main"]):
            conflicts.append(f"{rel}: the main ledger no longer begins with the ledger as cloned or last carried")
            continue
        added = w[b["worktree"]["length"]:]
        if added:
            if not added.endswith(b"\n"):
                conflicts.append(f"{rel}: the worktree's ledger does not end with a newline (a row is half written)")
                continue
            if m and not m.endswith(b"\n"):
                conflicts.append(f"{rel}: the main ledger does not end with a newline")
                continue
            appends[rel] = added
    for rel, p in sorted(wt.items()):
        if is_ledger(rel):
            if rel not in base["ledgers"]:
                if rel in mn:
                    conflicts.append(f"{rel}: a new ledger in the worktree, and the main worktree has one too")
                else:
                    copies.append(rel)
            continue
        w = sha(p)
        b = base["files"].get(rel)
        if w == b:
            continue
        m = sha(mn[rel]) if rel in mn else None
        if m == w:
            continue
        if m == b:
            copies.append(rel)
        else:
            conflicts.append(f"{rel}: changed in both the worktree and the main worktree since the clone")
    deleted = sorted(rel for rel in base["files"] if rel not in wt)
    return appends, copies, conflicts, deleted


def carry_back(main, worktree, manifest, dry_run=False, skip=None, prefer=()):
    if not manifest.is_file():
        raise SystemExit(f"worktree_data: no clone base for {worktree} ({manifest}); a worktree whose data was not "
                         "cloned with `worktree_data.py clone` cannot be carried back exactly")
    prefer = [os.path.normpath(x) for x in prefer]
    for rel in prefer:
        if is_ledger(rel):
            raise SystemExit(f"worktree_data: --prefer-worktree does not apply to a ledger: {rel}")
    if skip is None:
        skip = tracked(worktree) | tracked(main)
    base = json.loads(manifest.read_text())
    appends, copies, conflicts, deleted = plan(main, worktree, base, skip)
    for rel in dict.fromkeys(prefer):
        both = f"{rel}: changed in both the worktree and the main worktree since the clone"
        if both in conflicts:
            conflicts.remove(both)
            copies.append(rel)
            print(f"worktree_data: {rel}: changed in both; worktree copy kept (--prefer-worktree)")
        else:
            print(f"worktree_data: {rel}: not in conflict; --prefer-worktree has no effect on it")
    for rel in deleted:
        print(f"worktree_data: {rel} was deleted in the worktree; left in the main worktree")
    if conflicts:
        print("worktree_data: refused; nothing written:", file=sys.stderr)
        for c in conflicts:
            print(f"  {c}", file=sys.stderr)
        return 1
    for rel, added in sorted(appends.items()):
        rows = added.count(b"\n")
        print(f"worktree_data: {rel}: {'would append' if dry_run else 'appended'} {rows} row(s)")
        if not dry_run:
            with open(main / rel, "ab") as f:
                f.write(added)
    for rel in copies:
        print(f"worktree_data: {rel}: {'would copy' if dry_run else 'copied'}")
        if not dry_run:
            (main / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(worktree / rel, main / rel)
    if not dry_run:
        manifest.write_text(json.dumps(base_of(worktree, main, skip), indent=0, sort_keys=True))
    print(f"worktree_data: {len(appends)} ledger(s), {len(copies)} file(s), {len(deleted)} deleted in the worktree"
          f"{' (dry run; nothing written)' if dry_run else ''}")
    return 0


def fill(main, worktree, manifest, dry_run=False, skip=None):
    """Copy each untracked, non-ledger review file main has and the worktree lacks; record it in the base."""
    if main.resolve() == worktree.resolve():
        raise SystemExit("worktree_data: the worktree is the main worktree")
    if skip is None:
        skip = tracked(worktree) | tracked(main)
    copies = [rel for rel in sorted(files(main, skip))
              if not is_ledger(rel) and not os.path.lexists(worktree / rel)]
    base = json.loads(manifest.read_text()) if manifest.is_file() else None
    for rel in copies:
        print(f"worktree_data: {rel}: {'would copy' if dry_run else 'filled'}")
        if not dry_run:
            (worktree / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(main / rel, worktree / rel)
            if base is not None:
                base["files"][rel] = sha(worktree / rel)
    if base is not None and copies and not dry_run:
        manifest.write_text(json.dumps(base, indent=0, sort_keys=True))
    print(f"worktree_data: {len(copies)} file(s) {'to fill' if dry_run else 'filled'}"
          f"{' (dry run; nothing written)' if dry_run else ''}"
          f"{'' if base is not None else '; no clone base, so none recorded'}")
    return 0


def git(args, cwd):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"worktree_data: git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def main_worktree(root):
    """The clone's main worktree (the first `git worktree list` names), or None."""
    r = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=root, capture_output=True, text=True)
    for line in r.stdout.splitlines():
        if line.startswith("worktree "):
            return Path(line[len("worktree "):])
    return None


def locate(worktree, main):
    wt = Path(git(["rev-parse", "--show-toplevel"], worktree))
    main = Path(main) if main is not None else main_worktree(wt)
    if main is None:
        raise SystemExit("worktree_data: cannot find the main worktree (git worktree list)")
    manifest = Path(git(["rev-parse", "--path-format=absolute", "--git-path", "data-clone-base.json"], wt))
    return wt, main, manifest


# --- self-test -----------------------------------------------------------------------------------------

def self_test():
    with open(os.devnull, "w") as quiet, contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
        _self_test()
    print("worktree_data self-test: check (present, a receipt missing a file, prose left out), clone, carry-back "
          "(ledger rows with rows on both sides, changed files, tracked files left out, both-changed refusal, "
          "rewritten ledgers, repeated carry, no base, --prefer-worktree), fill (adds missing, never overwrites, skips ledgers, "
          "dry run, carry-back after) ok")
    return 0


def _self_test():
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        # check: a log names its own receipt and a class M request; both present, then one missing.
        root = t / "repo"
        (root / "reviews" / "2025" / "transcription").mkdir(parents=True)
        (root / "reviews" / "2025" / "transcription" / "adjudication").mkdir()
        (root / "reviews" / "2025" / "transcription" / "f1.md").write_text("See .classm/classm.f1.1.prompt.txt.\n")
        (root / "reviews" / "2025" / "transcription" / "adjudication" / "f1.md").write_text(".transcription/prose.txt\n")
        (root / ".transcription").mkdir()
        (root / ".classm").mkdir()
        for s in SUFFIXES:
            (root / ".transcription" / ("f1" + s)).write_text("x")
        (root / ".classm" / "classm.f1.1.prompt.txt").write_text("x")
        sink = open(os.devnull, "w")
        assert set(referenced(root)) == {".transcription/f1", ".classm/classm.f1.1.prompt.txt"}, referenced(root)
        assert check(root, out=sink) == 0
        (root / ".transcription" / "f1.response.txt").unlink()
        assert set(missing(root)) == {".transcription/f1"}, "a receipt base missing one of its three files is missing"
        assert check(root, out=sink) == 1

        main, wt, manifest = t / "main", t / "wt", t / "base.json"
        (main / ".transcription").mkdir(parents=True)
        (main / ".classm").mkdir()
        (main / "node_modules").mkdir()
        (main / ".transcription" / "a.prompt.txt").write_text("a")
        (main / ".transcription" / "b.prompt.txt").write_text("b")
        (main / ".transcription" / "t.prompt.txt").write_text("tracked")
        (main / ".transcription" / LEDGER).write_text('{"n": 1}\n')
        (main / ".classm" / "c.txt").write_text("c")
        wt.mkdir()
        (wt / ".transcription").mkdir()
        (wt / ".transcription" / "partial.txt").write_text("partial")
        clone(main, wt, manifest, run=lambda argv, check: shutil.copytree(argv[2], argv[3]))
        assert not (wt / ".transcription" / "partial.txt").exists(), "clone replaces the partial copy"
        assert (wt / "node_modules").is_dir()
        skip = {".transcription/t.prompt.txt"}
        manifest.write_text(json.dumps(base_of(wt, main, skip)))
        # Work in both: the worktree reviews a, adds d and two ledger rows and changes a tracked file;
        # main adds a row and changes b.
        (wt / ".transcription" / "a.prompt.txt").write_text("a2")
        (wt / ".transcription" / "d.prompt.txt").write_text("d")
        (wt / ".transcription" / "t.prompt.txt").write_text("tracked2")
        with open(wt / ".transcription" / LEDGER, "a") as f:
            f.write('{"n": "w1"}\n{"n": "w2"}\n')
        with open(main / ".transcription" / LEDGER, "a") as f:
            f.write('{"n": "m1"}\n')
        (main / ".transcription" / "b.prompt.txt").write_text("b-main")
        assert carry_back(main, wt, manifest, dry_run=True, skip=skip) == 0
        assert (main / ".transcription" / "a.prompt.txt").read_text() == "a", "a dry run writes nothing"
        assert (main / ".transcription" / LEDGER).read_text() == '{"n": 1}\n{"n": "m1"}\n', "a dry run appends nothing"
        assert carry_back(main, wt, manifest, skip=skip) == 0
        assert (main / ".transcription" / "a.prompt.txt").read_text() == "a2"
        assert (main / ".transcription" / "d.prompt.txt").read_text() == "d"
        assert (main / ".transcription" / "b.prompt.txt").read_text() == "b-main", "a file only main changed is kept"
        assert (main / ".transcription" / "t.prompt.txt").read_text() == "tracked", "a tracked file is not carried"
        assert (main / ".transcription" / LEDGER).read_text() == '{"n": 1}\n{"n": "m1"}\n{"n": "w1"}\n{"n": "w2"}\n'
        # Carried again with nothing new: nothing appended twice.
        assert carry_back(main, wt, manifest, skip=skip) == 0
        assert (main / ".transcription" / LEDGER).read_text().count("w1") == 1
        # A file changed on both sides refuses everything, ledger included.
        (wt / ".transcription" / "a.prompt.txt").write_text("a3")
        (main / ".transcription" / "a.prompt.txt").write_text("a-other")
        with open(wt / ".transcription" / LEDGER, "a") as f:
            f.write('{"n": "w3"}\n')
        before = (main / ".transcription" / LEDGER).read_text()
        assert carry_back(main, wt, manifest, skip=skip) == 1
        assert (main / ".transcription" / LEDGER).read_text() == before
        assert (main / ".transcription" / "a.prompt.txt").read_text() == "a-other"
        # --prefer-worktree: a named conflicting file is taken from the worktree; unnamed conflicts still
        # refuse; a ledger name is rejected; a dry run writes nothing.
        (main / ".transcription" / "b.prompt.txt").write_text("b-main2")
        (wt / ".transcription" / "b.prompt.txt").write_text("b-wt")
        a_rel, b_rel = ".transcription/a.prompt.txt", ".transcription/b.prompt.txt"
        (main / a_rel).write_text("a-other")
        assert carry_back(main, wt, manifest, skip=skip, prefer=[b_rel]) == 1, "an unnamed conflict still refuses"
        assert (main / b_rel).read_text() == "b-main2"
        try:
            carry_back(main, wt, manifest, skip=skip, prefer=[b_rel, ".transcription/" + LEDGER])
            raise AssertionError("a ledger was accepted")
        except SystemExit:
            pass
        assert carry_back(main, wt, manifest, dry_run=True, skip=skip, prefer=[a_rel, b_rel]) == 0
        assert (main / a_rel).read_text() == "a-other" and (main / b_rel).read_text() == "b-main2", "dry run writes nothing"
        assert carry_back(main, wt, manifest, skip=skip, prefer=["./" + a_rel, b_rel]) == 0
        assert (main / a_rel).read_text() == "a3" and (main / b_rel).read_text() == "b-wt", "preferred files are copied"
        assert carry_back(main, wt, manifest, skip=skip) == 0, "a preferred file is recorded as carried"
        (main / a_rel).write_text("a3")
        # A rewritten worktree ledger is refused; so is a rewritten main ledger.
        (main / ".transcription" / "a.prompt.txt").write_text("a3")
        good = (wt / ".transcription" / LEDGER).read_text()
        (wt / ".transcription" / LEDGER).write_text('{"n": "rewritten"}\n')
        assert carry_back(main, wt, manifest, skip=skip) == 1
        (wt / ".transcription" / LEDGER).write_text(good)
        (main / ".transcription" / LEDGER).write_text('{"n": "main rewritten"}\n')
        assert carry_back(main, wt, manifest, skip=skip) == 1
        # A worktree that was never cloned with a base is refused.
        try:
            carry_back(main, wt, t / "missing.json", skip=skip)
            raise AssertionError("carried back without a base")
        except SystemExit:
            pass
        # fill: adds a missing file, never overwrites a differing one, skips ledgers, and leaves
        # carry-back with nothing to bring back for an untouched filled file.
        fm, fw, fb = t / "fmain", t / "fwt", t / "fbase.json"
        (fm / ".transcription").mkdir(parents=True)
        (fw / ".transcription").mkdir(parents=True)
        for name, text in (("keep", "main-keep"), ("new", "new"), ("new2", "new2")):
            (fm / ".transcription" / (name + ".txt")).write_text(text)
        (fm / ".transcription" / LEDGER).write_text('{"n": 1}\n')
        (fw / ".transcription" / "keep.txt").write_text("worktree-keep")
        fb.write_text(json.dumps(base_of(fw, fm, frozenset())))
        assert fill(fm, fw, fb, dry_run=True, skip=frozenset()) == 0
        assert not (fw / ".transcription" / "new.txt").exists(), "a dry run fills nothing"
        assert fill(fm, fw, fb, skip=frozenset()) == 0
        assert (fw / ".transcription" / "new.txt").read_text() == "new"
        assert (fw / ".transcription" / "new2.txt").read_text() == "new2"
        assert (fw / ".transcription" / "keep.txt").read_text() == "worktree-keep", "an existing file is not overwritten"
        assert not (fw / ".transcription" / LEDGER).exists(), "a ledger is not filled"
        assert json.loads(fb.read_text())["files"][".transcription/new.txt"] == sha(fm / ".transcription" / "new.txt")
        appends, copies, conflicts, deleted = plan(fm, fw, json.loads(fb.read_text()), frozenset())
        assert not (appends or copies or conflicts or deleted), "an untouched filled file is not carried back"
        (fw / ".transcription" / "new2.txt").write_text("new2-edited")
        appends, copies, conflicts, deleted = plan(fm, fw, json.loads(fb.read_text()), frozenset())
        assert copies == [".transcription/new2.txt"] and not (appends or conflicts or deleted), copies
        sink.close()


def main(argv):
    if argv[:1] == ["--self-test"]:
        return self_test()
    if argv[:1] == ["check"]:
        if argv[1:] == ["--list"]:
            for r in sorted(referenced()):
                print(r)
            return 0
        if argv[1:]:
            raise SystemExit("usage: worktree_data.py check [--list]")
        return check(ROOT, main_worktree(ROOT))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=("clone", "carry-back", "fill"))
    ap.add_argument("worktree")
    ap.add_argument("--main", help="the main worktree (default: the clone's first worktree)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--prefer-worktree", nargs="+", metavar="PATH", default=[],
                    help="carry-back: take the worktree's copy of these both-changed files")
    a = ap.parse_args(argv)
    if a.prefer_worktree and a.command != "carry-back":
        ap.error("--prefer-worktree applies to carry-back")
    wt, main_wt, manifest = locate(Path(a.worktree), a.main)
    if a.command == "clone":
        if a.dry_run:
            ap.error("--dry-run applies to carry-back and fill")
        clone(main_wt, wt, manifest)
        return 0
    if a.command == "fill":
        return fill(main_wt, wt, manifest, a.dry_run)
    return carry_back(main_wt, wt, manifest, a.dry_run, prefer=a.prefer_worktree)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
