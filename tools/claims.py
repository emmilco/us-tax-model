#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Form claims: two lanes (branches, usually in their own worktrees) never edit the same form at once.

A claim names a form id (a file forms/<year>/<id>.yaml or forms/ny/<year>/<id>.yaml) or the key `inputs` (the right to
add new input ids, whose ripple through fixtures, interview and generators one lane owns at a time). Claims are held by
a branch and kept in <git common dir>/claims.json, so every worktree of the clone sees them.

- tools/hooks/pre-commit runs `check`: a commit that changes a form claimed by another branch, or adds an input id
  while another branch holds `inputs`, is refused. A commit on a branch other than main claims the forms it changes
  (and `inputs` when it adds input ids) for its branch. A commit on main claims nothing.
- A merge may change forms claimed by the branch it merges; tools/hooks/post-commit then releases that branch's claims.
- A claim whose branch no longer exists is ignored and pruned.

    claims.py claim KEY... [--reason TEXT]    claim for the current branch before starting work
    claims.py release KEY...                   release claims (any holder's; say why in the commit)
    claims.py list
    claims.py check TREE PARENT...             pre-commit: TREE is the staged tree, PARENTs HEAD and MERGE_HEADs
    claims.py merged                           post-commit: release the claims of branches HEAD merged
    claims.py --self-test
"""
import contextlib
import datetime
import fcntl
import json
import os
import re
import subprocess
import sys
import tempfile

import yaml

FORM = re.compile(r"^forms/(?:ny/)?\d{4}/([^/]+)\.yaml$")
INPUTS = "inputs"
MAIN = "main"


def git(*args, cwd=None):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True, cwd=cwd).stdout.strip()


def store_path(cwd=None):
    return os.path.join(os.path.abspath(os.path.join(cwd or ".", git("rev-parse", "--git-common-dir", cwd=cwd))),
                        "claims.json")


@contextlib.contextmanager
def store(cwd=None):
    """The claims, locked for the duration; written back on exit."""
    path = store_path(cwd)
    with open(path + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        data = json.load(open(path)) if os.path.exists(path) else {}
        before = json.dumps(data, sort_keys=True)
        yield data
        if json.dumps(data, sort_keys=True) != before:
            with open(path + ".tmp", "w") as f:
                json.dump(data, f, indent=1, sort_keys=True)
                f.write("\n")
            os.replace(path + ".tmp", path)


def branch(cwd=None):
    return subprocess.run(["git", "symbolic-ref", "-q", "--short", "HEAD"], capture_output=True, text=True,
                          cwd=cwd).stdout.strip()


def branches(cwd=None):
    return set(git("for-each-ref", "--format=%(refname:short)", "refs/heads", cwd=cwd).split())


def prune(data, cwd=None):
    live = branches(cwd)
    for key in [k for k, c in data.items() if c["branch"] not in live]:
        del data[key]


def input_ids(tree, path, cwd=None):
    """The ids of the input lines of a form file in a tree (empty when the file is absent or unreadable)."""
    try:
        doc = yaml.safe_load(git("show", f"{tree}:{path}", cwd=cwd))
    except (subprocess.CalledProcessError, yaml.YAMLError):
        return set()
    body = (doc or {}).get("form") or (doc or {}).get("def") or {}
    return {l["id"] for l in body.get("lines") or [] if isinstance(l, dict) and (l.get("expr") or {}).get("op") == "input"}


def touched(tree, parent, cwd=None):
    """(forms changed between parent and tree, whether input ids were added)."""
    paths = git("diff-tree", "-r", "--name-only", parent, tree, cwd=cwd).splitlines() if parent else \
        git("ls-tree", "-r", "--name-only", tree, cwd=cwd).splitlines()
    forms, added = set(), False
    for p in paths:
        m = FORM.match(p)
        if m:
            forms.add(m.group(1))
            if input_ids(tree, p, cwd) - (input_ids(parent, p, cwd) if parent else set()):
                added = True
    return forms, added


def check(tree, parents, cwd=None):
    """The refusal (a message) or None. On a branch other than main, claims what the commit changes."""
    me = branch(cwd) or "(detached)"
    head = parents[0] if parents else None
    merged = {b for b in branches(cwd) for p in parents[1:] if git("rev-parse", b, cwd=cwd) == p}
    forms, added = touched(tree, head, cwd)
    keys = forms | ({INPUTS} if added else set())
    with store(cwd) as data:
        prune(data, cwd)
        held = {k: data[k]["branch"] for k in keys if k in data and data[k]["branch"] not in ({me} | merged)}
        if held:
            return ("this commit changes " + ", ".join(f"{k} (claimed by {b})" for k, b in sorted(held.items()))
                    + "; finish or merge that branch first, or release the claim with tools/claims.py release")
        if me not in (MAIN, "(detached)"):
            now = datetime.date.today().isoformat()
            for k in keys - set(data):
                data[k] = {"branch": me, "since": now, "how": "commit"}
    return None


def release_merged(cwd=None):
    """Release the claims of the branches whose tips are HEAD's second and later parents."""
    parents = git("rev-list", "--parents", "-n", "1", "HEAD", cwd=cwd).split()[2:]
    gone = {b for b in branches(cwd) for p in parents if git("rev-parse", b, cwd=cwd) == p}
    with store(cwd) as data:
        for k in [k for k, c in data.items() if c["branch"] in gone]:
            del data[k]
    return gone


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "--self-test":
        return self_test()
    if cmd == "check":
        why = check(rest[0], rest[1:])
        if why:
            print(f"pre-commit: {why}", file=sys.stderr)
            return 1
        return 0
    if cmd == "merged":
        gone = release_merged()
        if gone:
            print(f"claims: released the claims of {', '.join(sorted(gone))} (merged)")
        return 0
    if cmd == "list":
        with store() as data:
            prune(data)
            for k, c in sorted(data.items()):
                print(f"{k:24s} {c['branch']:40s} since {c['since']} ({c['how']}){'  ' + c['reason'] if c.get('reason') else ''}")
        return 0
    if cmd in ("claim", "release"):
        reason = None
        if "--reason" in rest:
            i = rest.index("--reason")
            reason, rest = rest[i + 1], rest[:i] + rest[i + 2:]
        if not rest:
            print(f"claims: {cmd} needs at least one key", file=sys.stderr)
            return 2
        me = branch()
        with store() as data:
            prune(data)
            if cmd == "release":
                for k in rest:
                    data.pop(k, None)
                return 0
            if me in ("", MAIN):
                print("claims: claims are held by a lane's branch, not by main or a detached HEAD", file=sys.stderr)
                return 2
            taken = {k: data[k]["branch"] for k in rest if k in data and data[k]["branch"] != me}
            if taken:
                print("claims: already claimed: " + ", ".join(f"{k} by {b}" for k, b in sorted(taken.items())), file=sys.stderr)
                return 1
            for k in rest:
                data[k] = {"branch": me, "since": datetime.date.today().isoformat(), "how": "explicit",
                           **({"reason": reason} if reason else {})}
        return 0
    print(f"claims: unknown command {cmd}", file=sys.stderr)
    return 2


def self_test():
    """Lanes in a temporary repository: claim on commit, refusal across branches, inputs, release on merge."""
    def run(*a):
        return git(*a, cwd=repo)

    def write(path, inputs):
        os.makedirs(os.path.join(repo, os.path.dirname(path)), exist_ok=True)
        lines = [{"id": i, "expr": {"op": "input"}} for i in inputs] + [{"id": "x.total", "expr": {"op": "add"}}]
        open(os.path.join(repo, path), "w").write(yaml.safe_dump({"form": {"id": "x", "lines": lines}}))

    def commit(msg):
        run("add", "-A")
        tree = run("write-tree")
        parents = [run("rev-parse", "HEAD")]
        mh = os.path.join(repo, ".git", "MERGE_HEAD")
        if os.path.exists(mh):
            parents += open(mh).read().split()
        why = check(tree, parents, repo)
        if why is None:
            run("commit", "-qm", msg)
        return why

    failures = []

    def expect(cond, what):
        if not cond:
            failures.append(what)

    with tempfile.TemporaryDirectory() as repo:
        run("init", "-q", "-b", MAIN)
        run("config", "user.email", "t@example.com"); run("config", "user.name", "t")
        write("forms/2025/a.yaml", ["a.one"]); write("forms/2025/b.yaml", ["b.one"])
        run("add", "-A"); run("commit", "-qm", "base")
        run("checkout", "-qb", "lane1")
        write("forms/2025/a.yaml", ["a.one"])
        open(os.path.join(repo, "forms/2025/a.yaml"), "a").write("# edit\n")
        expect(commit("lane1 edits a") is None, "a lane's first commit of a form is accepted")
        with store(repo) as data:
            expect(data.get("a", {}).get("branch") == "lane1", "the commit claims the form for its branch")
        run("checkout", "-q", MAIN); run("checkout", "-qb", "lane2")
        open(os.path.join(repo, "forms/2025/a.yaml"), "a").write("# other\n")
        why = commit("lane2 edits a")
        expect(why is not None and "a (claimed by lane1)" in why, "another lane's commit of a claimed form is refused")
        run("checkout", "-q", "--", "."); run("reset", "-q", "--hard")
        write("forms/2025/b.yaml", ["b.one", "b.two"])
        expect(commit("lane2 adds an input") is None, "a lane may add an input while no lane holds inputs")
        run("checkout", "-q", "lane1")
        write("forms/2025/a.yaml", ["a.one", "a.two"])
        why = commit("lane1 adds an input")
        expect(why is not None and "inputs (claimed by lane2)" in why, "adding an input while another lane holds inputs is refused")
        run("reset", "-q", "--hard")
        run("checkout", "-q", MAIN)
        open(os.path.join(repo, "forms/2025/a.yaml"), "a").write("# main\n")
        why = commit("main edits a")
        expect(why is not None and "lane1" in why, "main's commit of a lane's form is refused")
        run("reset", "-q", "--hard")
        run("merge", "-q", "--no-commit", "--no-ff", "lane1")
        expect(commit("merge lane1") is None, "a merge may change the merged branch's forms")
        release_merged(repo)
        with store(repo) as data:
            expect("a" not in data and data.get(INPUTS, {}).get("branch") == "lane2",
                   "the merge releases the merged branch's claims only")
        with store(repo) as data:
            expect("a" not in data, "main claims nothing")
        run("branch", "-qD", "lane2")
        with store(repo) as data:
            prune(data, repo)
            expect(not data, "a deleted branch's claims are pruned")
    for f in failures:
        print(f"claims self-test: FAILED: {f}")
    print("claims self-test: " + ("ok" if not failures else f"{len(failures)} failure(s)"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
