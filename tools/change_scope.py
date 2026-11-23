#!/usr/bin/env python3
"""The forms a change touches, for the interview checks the light tier of check-all scopes (--forms).

    change_scope.py [--year N]     print the scope of the working tree's change against HEAD
    change_scope.py --self-test

The change is every path that differs between HEAD and the working tree, untracked files included (what `git add -A`
would commit on HEAD; in the snapshot worktree of tools/check_all_bg.sh, HEAD is the commit the snapshot was taken on).
It prints one line:

  all          a changed path can change any interview walk: the engine, the interview profiles, the schema, the
               parameters or tables, the year files, or any path not named below
  none         no changed path is read by the interview checks (tools, docs, reports, rendered text, reviews,
               sources, research, the Lean evaluator, the web UI)
  f1,f2,...    the form ids touched: a changed form file (forms/<year>/<form>.yaml, forms/ny/<year>/<form>.yaml)
               names its form; a changed fixture file, coverage row file or question bank (interview/<year>/
               questions.yaml) names the forms of the input keys on its changed lines

A form id is the stem of a form file of the year (federal or New York). An input key names the forms among its
segments (engine/src/form-scope.ts reads keys the same way).
"""
import re
import subprocess
import sys
import tempfile
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from tier_paths import DOCS, matches, parse  # noqa: E402

# Paths the interview checks do not read: these prefixes, the bookkeeping paths of tools/docs_paths.txt, and the
# Markdown and licence files at the root.
IGNORED = ("tools/", "reports/", "rendered/", "reviews/", "sources/", "research/", "lean/", "ui/", "spec/",
           "ambiguities/", ".claude/", ".github/")
IGNORED_FILES = {"LICENSE", "LICENSE-DATA", ".gitignore"}
KEY = re.compile(r"\$?[A-Za-z_][\w$@.\[\]-]*")


def git(*args, env=None):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True, env=env).stdout


def tokens(text):
    """The segments of every key-like word of `text`, as form-scope.ts splits an input key."""
    out = set()
    for word in KEY.findall(text):
        out.update(s for s in re.split(r"[.@]", re.sub(r"\[[^\]]*\]", "", word).lstrip("$")) if s)
    return out


def classify(path, changed_lines, year, forms, bookkeeping=()):
    """'all', None (not read), or the set of form ids `path` touches. `changed_lines` returns its changed lines;
    `bookkeeping` is the patterns of tools/docs_paths.txt."""
    if path in IGNORED_FILES or path.startswith(IGNORED) or matches(path, bookkeeping):
        return None
    m = re.fullmatch(rf"forms/(?:ny/)?{year}/([^/]+)\.yaml", path)
    if m:
        return {m.group(1)}
    if (path.startswith(f"fixtures/{year}/") or path.startswith(f"fixtures/ny/{year}/")
            or path.startswith(f"interview/{year}/coverage/") or path == f"interview/{year}/questions.yaml"):
        return tokens(changed_lines(path)) & forms
    if path.endswith(".md") and "/" not in path:
        return None
    return "all"


def scope(paths, changed_lines, year, forms, bookkeeping=()):
    touched = set()
    for p in paths:
        c = classify(p, changed_lines, year, forms, bookkeeping)
        if c == "all":
            return "all"
        if c:
            touched |= c
    return ",".join(sorted(touched)) or "none"


def form_ids(year):
    out = set()
    for d in (ROOT / "forms" / year, ROOT / "forms" / "ny" / year):
        if d.is_dir():
            out.update(p.stem for p in d.glob("*.yaml"))
    return out


def worktree_change():
    """The changed paths between HEAD and the working tree (untracked included), and a reader of a path's changed lines."""
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(tmp) / "index"))
        git("read-tree", "HEAD", env=env)
        git("add", "-A", env=env)
        tree = git("write-tree", env=env).strip()
    paths = [p for p in git("diff-tree", "-r", "--no-renames", "--name-only", "HEAD", tree).splitlines() if p]

    def changed_lines(path):
        diff = git("diff", "-U0", "--no-renames", "HEAD", tree, "--", path)
        return "\n".join(l[1:] for l in diff.splitlines() if l[:1] in "+-" and not l.startswith(("+++", "---")))
    return paths, changed_lines


def self_test():
    forms = {"f8889", "f1040", "sc", "it201"}
    lines = {"fixtures/2025/returns.json": '"person[taxpayer].f8889[hsa].line9": 0,\n"note": "x"',
             "interview/2025/coverage/hsa.yaml": "      $sc@person[taxpayer]: [a]",
             "fixtures/2025/other.json": '"comment": "nothing of a form"'}
    read = lines.__getitem__
    cases = [
        ([], "none"),
        (["tools/x.py", "notes/a.md", "README.md", "reports/2025/x.md"], "none"),
        (["forms/2025/f8889.yaml"], "f8889"),
        (["forms/ny/2025/it201.yaml", "forms/2025/f1040.yaml", "tools/x.py"], "f1040,it201"),
        (["fixtures/2025/returns.json"], "f8889"),
        (["interview/2025/coverage/hsa.yaml"], "sc"),
        (["fixtures/2025/other.json"], "none"),
        (["forms/2025/f8889.yaml", "engine/src/interview.ts"], "all"),
        (["interview/2025/full.yaml"], "all"),
        (["params/2025/x.yaml"], "all"),
        (["forms/2024/f8889.yaml"], "all"),
    ]
    for paths, want in cases:
        got = scope(paths, read, "2025", forms, ["notes/*"])
        assert got == want, (paths, got, want)
    assert tokens("person[taxpayer].f8889[hsa].line9") == {"person", "f8889", "line9"}
    print(f"change scope self-test: ok ({len(cases)} cases)")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    from taxyear import Y
    paths, changed_lines = worktree_change()
    print(scope(paths, changed_lines, Y, form_ids(Y), parse((ROOT / DOCS).read_text(encoding="utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
