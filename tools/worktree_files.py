#!/usr/bin/env python3
"""The files of the tree a check-all green record names, for the checks that enumerate or search files.

A green record of check-all (tools/green.sh, worktree_tree) holds the tree a full `git add -A` would commit: the
tracked files as they are in the working tree, tracked files deleted from it left out, untracked files included and
ignored files excluded. A check that lists or searches the repository's files must see exactly that set, or a run
made before `git add` records as green a tree whose committed content it never checked. This module gives that set.

    files(*pathspecs, cwd)   the paths of the tree under the pathspecs, sorted
    tree(cwd)                the hash of the tree `git add -A` would commit, the real index untouched
    grep(args, pathspecs, cwd)   `git grep` over those files: the tracked and the untracked, ignored files excluded
    worktree_files.py --self-test
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _git(args, cwd, env=None, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        raise SystemExit(f"worktree_files: git {' '.join(args)}: {r.stderr.strip()}")
    return r


def files(*pathspecs, cwd=ROOT):
    """The repository-relative paths, tracked or untracked and not ignored, that exist in the working tree."""
    spec = ["--", *pathspecs] if pathspecs else []
    listed = _git(["ls-files", "-z", "--cached", "--others", "--exclude-standard", *spec], cwd).stdout.split("\0")
    deleted = set(_git(["ls-files", "-z", "--deleted", *spec], cwd).stdout.split("\0"))
    return sorted({p for p in listed if p and p not in deleted})


def tree(cwd=ROOT):
    """The tree a full `git add -A` would commit, written through a temporary index (as tools/green.sh does)."""
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(tmp) / "index"))
        if _git(["rev-parse", "--verify", "-q", "HEAD"], cwd, check=False).returncode == 0:
            _git(["read-tree", "HEAD"], cwd, env)
        _git(["add", "-A"], cwd, env)
        return _git(["write-tree"], cwd, env).stdout.strip()


def grep(args, pathspecs=(".",), cwd=ROOT):
    """The output of `git grep <args> --untracked -- <pathspecs>`: tracked and untracked files, ignored ones excluded,
    deleted ones absent. Exit status 1 (no match) is not an error."""
    r = _git(["grep", "--untracked", *args, "--", *pathspecs], cwd, check=False)
    if r.returncode not in (0, 1):
        raise SystemExit(f"worktree_files: git grep: {r.stderr.strip()}")
    return r.stdout


def scratch_repo(tmp):
    """A repository in `tmp` with one commit (a.txt, gone.txt, .gitignore ignoring ign.txt), then gone.txt deleted,
    untracked new.txt and ignored ign.txt written. Each file holds the word TOKEN. For the self-tests of the checks."""
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t",
               GIT_COMMITTER_EMAIL="t@t")
    run = lambda *a: subprocess.run(["git", *a], cwd=tmp, env=env, capture_output=True, check=True)  # noqa: E731
    run("init", "-q")
    for name, text in (("a.txt", "TOKEN\n"), ("gone.txt", "TOKEN\n"), (".gitignore", "ign.txt\n")):
        (Path(tmp) / name).write_text(text)
    run("add", "-A")
    run("commit", "-q", "-m", "base")
    (Path(tmp) / "gone.txt").unlink()
    (Path(tmp) / "new.txt").write_text("TOKEN\n")
    (Path(tmp) / "ign.txt").write_text("TOKEN\n")


def self_test():
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        scratch_repo(tmp)
        got = files(cwd=tmp)
        if got != [".gitignore", "a.txt", "new.txt"]:
            bad.append(f"files: {got}, want the tracked, the untracked, not the deleted or the ignored")
        hits = sorted(grep(["-l", "TOKEN"], cwd=tmp).split())
        if hits != ["a.txt", "new.txt"]:
            bad.append(f"grep: {hits}, want a.txt and the untracked new.txt")
        staged = _git(["ls-files", "--stage"], tmp).stdout
        t = tree(cwd=tmp)
        listed = _git(["ls-tree", "-r", "--name-only", t], tmp).stdout.split()
        if listed != got:
            bad.append(f"tree lists {listed}, files lists {got}")
        if _git(["ls-files", "--stage"], tmp).stdout != staged:
            bad.append("tree() changed the real index")
    print("worktree files self-test: " + ("ok" if not bad else "FAILED: " + "; ".join(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sys.exit(self_test())
    print(__doc__, file=sys.stderr)
    sys.exit(2)
