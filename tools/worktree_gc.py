#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""The linked worktrees of this clone, sorted by what may be done with them, and their removal.

    worktree_gc.py [list]                 every linked worktree with its class and why
    worktree_gc.py remove [--dry-run]     remove every `removable` worktree
    worktree_gc.py archive NAME... [--dry-run] [--force-data REASON]
                                          save each named worktree's uncommitted state, then remove it
    worktree_gc.py check [--fail]         list what needs action; with --fail exit 1 when anything does
    worktree_gc.py --self-test

Classes (the main worktree and the check-all worktree under the git dir are never listed):
- `keep`: locked with a reason starting "keep" (`git worktree lock --reason "keep: <why>" <path>`).
- `removable`: no uncommitted or untracked files, HEAD contained in main, and no review data the worktree added
  since its clone (tools/worktree_data.py carry-back --dry-run reports nothing to carry, .DS_Store aside). Removing
  it loses nothing that is not in git or in the main worktree.
- `active`: anything else used in the last STALE_DAYS days (its HEAD moved or a changed file was written).
- `stale`: anything else. Its work is either landed by another route or abandoned; decide which, then `archive` it
  (or `keep` it, with the reason).

`archive` writes .claude/worktree-archive/<date>/<name>/: head.txt (commit and branch), tracked.patch (`git diff
HEAD --binary`), untracked.tar (untracked files git does not ignore) and data/ (the review files carry-back would
copy, when the worktree has a clone base; data.txt says which), then removes the worktree. A locked worktree is
refused, and so is one whose review data cannot be compared with the main worktree's (no clone base, or a carry-back
dry run that refuses): it could hold the only copy of review results. `--force-data REASON` archives it anyway,
recording the reason in data.txt, once the operator has saved or ruled out that data. `check --fail` is the release gate (tools/release_prep.sh); check-all prints `check` without failing.
"""
import datetime
import os
import shutil
import subprocess
import sys
import tarfile
import time

STALE_DAYS = 7
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*args, cwd=None, check=True):
    r = subprocess.run(["git", *args], cwd=cwd or ROOT, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r


def common_dir(root):
    return os.path.realpath(os.path.join(root, git("rev-parse", "--git-common-dir", cwd=root).stdout.strip()))


def main_worktree(root):
    return os.path.dirname(common_dir(root))


def worktrees(root):
    """[{path, head, branch, locked}] of the linked worktrees, the main one and those under the git dir left out."""
    out, cur = [], {}
    for line in git("worktree", "list", "--porcelain", cwd=root).stdout.splitlines() + [""]:
        if not line:
            if cur:
                out.append(cur)
            cur = {}
            continue
        key, _, val = line.partition(" ")
        if key == "worktree":
            cur = {"path": val, "head": "", "branch": "", "locked": None, "prunable": False}
        elif key == "HEAD":
            cur["head"] = val
        elif key == "branch":
            cur["branch"] = val.removeprefix("refs/heads/")
        elif key == "locked":
            cur["locked"] = val
        elif key == "prunable":
            cur["prunable"] = True
    gd = common_dir(root)
    mainp = os.path.realpath(main_worktree(root))
    return [w for w in out if os.path.realpath(w["path"]) != mainp and not os.path.realpath(w["path"]).startswith(gd + os.sep)]


def admin_dir(root, path):
    return os.path.realpath(os.path.join(path, git("rev-parse", "--git-dir", cwd=path).stdout.strip()))


def uncommitted(path):
    return [l for l in git("status", "--porcelain", cwd=path, check=False).stdout.splitlines() if l]


def on_main(root, head):
    return git("merge-base", "--is-ancestor", head, "main", cwd=root, check=False).returncode == 0


def data_to_carry(root, path):
    """(files, note): the review files carry-back would bring from the worktree (.DS_Store aside), or None with a note
    when it cannot tell (no clone base)."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "worktree_data.py"), "carry-back", path,
                        "--main", main_worktree(root), "--dry-run"], capture_output=True, text=True)
    text = r.stdout + r.stderr
    if "no clone base" in text:
        return None, "no clone base: its review data cannot be compared"
    files = [l.split("worktree_data: ", 1)[1].rsplit(": ", 1)[0] for l in text.splitlines()
             if l.startswith("worktree_data: ") and (": would " in l or "conflict" in l) and ".DS_Store" not in l]
    if r.returncode and not files:
        return None, "carry-back --dry-run failed: " + text.strip().splitlines()[-1] if text.strip() else "failed"
    return files, ""


def age_days(root, path, dirty=()):
    """Days since the worktree was last used: its HEAD moved (logs/HEAD) or one of its changed files was written.
    (The index is not a signal: `git status` rewrites it.)"""
    times = []
    try:
        adm = admin_dir(root, path)
        for f in ("logs/HEAD", "HEAD"):
            if os.path.exists(os.path.join(adm, f)):
                times.append(os.path.getmtime(os.path.join(adm, f)))
                break
    except RuntimeError:
        pass
    for line in list(dirty)[:500]:
        f = os.path.join(path, line[3:].split(" -> ")[-1].strip('"'))
        if os.path.exists(f):
            times.append(os.path.getmtime(f))
    return (time.time() - max(times)) / 86400 if times else float("inf")


def classify(root, w, data=data_to_carry):
    """(class, why) of one worktree."""
    if w["prunable"] or not os.path.isdir(w["path"]):
        return "removable", "its directory is gone (git worktree prune)"
    if w["locked"] is not None and w["locked"].lower().startswith("keep"):
        return "keep", w["locked"]
    dirty = uncommitted(w["path"])
    merged = on_main(root, w["head"])
    if not dirty and merged:
        files, note = data(root, w["path"])
        if files == []:
            return "removable", "clean, HEAD on main, no review data to carry back"
        why = note or f"{len(files)} review file(s) not carried back, e.g. {files[0]}"
    else:
        why = ", ".join(p for p in [f"{len(dirty)} uncommitted file(s)" if dirty else "",
                                    "HEAD not on main" if not merged else ""] if p)
    days = age_days(root, w["path"], dirty)
    if days < STALE_DAYS:
        return "active", f"{why}; used {days:.0f} day(s) ago"
    return "stale", f"{why}; unused for {days:.0f} days"


def survey(root, data=data_to_carry):
    return [(w, *classify(root, w, data)) for w in worktrees(root)]


def remove(root, w):
    if w["prunable"] or not os.path.isdir(w["path"]):
        git("worktree", "prune", cwd=root)
        return
    if w["locked"] is not None:
        git("worktree", "unlock", w["path"], cwd=root)
    git("worktree", "remove", "--force", w["path"], cwd=root)


class DataUnknown(Exception):
    """The worktree's review data cannot be compared with the main worktree's."""


def archive(root, w, dest, data=data_to_carry, force_data=None):
    """Save the worktree's uncommitted state under dest, then remove it. Refused (DataUnknown, before anything is
    written) when its review data cannot be compared, unless force_data gives the reason to go on."""
    path = w["path"]
    files, note = data(root, path)
    if files is None and not force_data:
        raise DataUnknown(note)
    os.makedirs(dest, exist_ok=False)
    with open(os.path.join(dest, "head.txt"), "w") as f:
        f.write(f"{w['head']} {w['branch'] or '(detached)'} {path}\n")
    with open(os.path.join(dest, "tracked.patch"), "w") as f:
        f.write(git("diff", "HEAD", "--binary", cwd=path).stdout)
    untracked = git("ls-files", "--others", "--exclude-standard", "-z", cwd=path).stdout.split("\0")
    with tarfile.open(os.path.join(dest, "untracked.tar"), "w") as t:
        for rel in filter(None, untracked):
            t.add(os.path.join(path, rel), arcname=rel, recursive=False)
    with open(os.path.join(dest, "data.txt"), "w") as f:
        f.write((note or f"{len(files)} review file(s) carry-back would copy, saved under data/") + "\n")
        if files is None:
            f.write(f"archived anyway (--force-data): {force_data}\n")
    for rel in files or []:
        src = os.path.join(path, rel)
        if os.path.isfile(src):
            os.makedirs(os.path.dirname(os.path.join(dest, "data", rel)), exist_ok=True)
            shutil.copy2(src, os.path.join(dest, "data", rel))
    remove(root, w)


def report(rows, only_action=False):
    for w, cls, why in sorted(rows, key=lambda r: (r[1], r[0]["path"])):
        if only_action and cls in ("keep", "active"):
            continue
        print(f"  {cls:9} {os.path.relpath(w['path'], main_worktree(ROOT))}: {why}")
    counts = {}
    for _, cls, _ in rows:
        counts[cls] = counts.get(cls, 0) + 1
    print("worktrees: " + (", ".join(f"{n} {c}" for c, n in sorted(counts.items())) or "none linked"))
    return counts


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    dry = "--dry-run" in argv
    cmd = args[0] if args else "list"
    if cmd == "list":
        report(survey(ROOT))
        return 0
    if cmd == "check":
        counts = report(survey(ROOT), only_action=True)
        need = counts.get("removable", 0) + counts.get("stale", 0)
        if need:
            print(f"worktree_gc: {need} worktree(s) need action: `tools/worktree_gc.py remove` for the removable, "
                  "`archive NAME` or `git worktree lock --reason \"keep: <why>\"` for the stale")
        return 1 if need and "--fail" in argv else 0
    if cmd == "remove":
        for w, cls, why in survey(ROOT):
            if cls == "removable":
                print(f"{'would remove' if dry else 'removed'} {w['path']} ({why})")
                if not dry:
                    remove(ROOT, w)
        return 0
    if cmd == "archive":
        force = argv[argv.index("--force-data") + 1] if "--force-data" in argv[:-1] else None
        names = [a for a in args[1:] if a != force]
        if not names:
            sys.exit("worktree_gc: archive NAME... (the worktree's directory name or path)")
        byname = {os.path.basename(w["path"]): w for w in worktrees(ROOT)}
        byname.update({os.path.realpath(w["path"]): w for w in worktrees(ROOT)})
        base = os.path.join(main_worktree(ROOT), ".claude", "worktree-archive", datetime.date.today().isoformat())
        status = 0
        for n in names:
            w = byname.get(n) or byname.get(os.path.realpath(n))
            if not w:
                print(f"worktree_gc: no linked worktree {n}"); status = 1; continue
            if w["locked"] is not None:
                print(f"worktree_gc: {n} is locked ({w['locked']}); unlock it first"); status = 1; continue
            dest = os.path.join(base, os.path.basename(w["path"]))
            print(f"{'would archive' if dry else 'archived'} {w['path']} -> {dest}")
            if not dry:
                try:
                    archive(ROOT, w, dest, force_data=force)
                except DataUnknown as e:
                    print(f"worktree_gc: {n} kept: its review data cannot be compared ({e}); save it, then pass "
                          "--force-data REASON"); status = 1
        return status
    sys.exit(f"worktree_gc: unknown command {cmd!r}")


def self_test():
    import tempfile
    tmp = tempfile.mkdtemp()
    try:
        r = os.path.join(tmp, "repo")
        os.makedirs(r)
        g = lambda *a, cwd=r: git(*a, cwd=cwd)
        g("init", "-q", "-b", "main"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
        open(os.path.join(r, "a"), "w").write("a\n"); g("add", "a"); g("commit", "-qm", "a")
        for n in ("clean", "dirty", "kept", "lane", "old"):
            g("worktree", "add", "-q", "--detach", os.path.join(tmp, n))
        open(os.path.join(tmp, "dirty", "a"), "w").write("b\n")
        g("commit", "-q", "--allow-empty", "-m", "lane", cwd=os.path.join(tmp, "lane"))
        g("worktree", "lock", "--reason", "keep: owner", os.path.join(tmp, "kept"))
        open(os.path.join(tmp, "old", "new.txt"), "w").write("x\n")
        then = (time.time() - 30 * 86400,) * 2
        adm = admin_dir(r, os.path.join(tmp, "old"))
        for f in (os.path.join(adm, "logs", "HEAD"), os.path.join(adm, "HEAD"), os.path.join(tmp, "old", "new.txt")):
            if os.path.exists(f):
                os.utime(f, then)
        no_data = lambda root, path: ([], "")
        got = {os.path.basename(w["path"]): cls for w, cls, _ in survey(r, no_data)}
        want = {"clean": "removable", "dirty": "active", "kept": "keep", "lane": "active", "old": "stale"}
        ok = got == want
        some_data = lambda root, path: ([".transcription/x"], "")
        ok &= {os.path.basename(w["path"]): c for w, c, _ in survey(r, some_data)}["clean"] == "active"
        w = next(w for w in worktrees(r) if w["path"].endswith("old"))
        dest = os.path.join(tmp, "arch", "old")
        archive(r, w, dest, no_data)
        ok &= not os.path.isdir(os.path.join(tmp, "old"))
        ok &= tarfile.open(os.path.join(dest, "untracked.tar")).getnames() == ["new.txt"]
        unknown = lambda root, path: (None, "no clone base")
        w2 = next(w for w in worktrees(r) if w["path"].endswith("dirty"))
        try:
            archive(r, w2, os.path.join(tmp, "arch", "dirty"), unknown); ok = False
        except DataUnknown:
            ok &= os.path.isdir(os.path.join(tmp, "dirty")) and not os.path.exists(os.path.join(tmp, "arch", "dirty"))
        archive(r, w2, os.path.join(tmp, "arch", "dirty2"), unknown, force_data="checked by hand")
        ok &= "checked by hand" in open(os.path.join(tmp, "arch", "dirty2", "data.txt")).read()
        print("worktree_gc self-test: " + ("ok" if ok else f"FAILED: {got}"))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv[1:]))
