#!/usr/bin/env python3
"""Which tier of check-all a commit needs, from the paths it changes.

    tier_paths.py required <tree> [<parent commit> ...]
        print "<tier>\\t<reason>": docs, fast or full, the least tier whose green record
        tools/green.sh must hold for <tree> to be committed on those parents
    tier_paths.py --self-test

The rule, for a tree and its parents:
  - full when there is no parent, when a parent lacks tools/full_paths.txt, or when a path changed
    against any parent matches a pattern in tools/full_paths.txt (the parents' lists and the tree's own);
  - docs when there is exactly one parent and every changed path matches tools/docs_paths.txt as the
    parent has it (a commit cannot widen the list it is judged by: the list is not on itself);
  - fast otherwise.
A path is compared with `git diff-tree -r --no-renames`, so a rename counts its old and its new path.

The docs tier is sound only if no check-all step outside it reads an allowlisted path. The self-test
checks that on the code check-all runs: every tracked file under tools/, engine/ and lean/, and the
root package.json and tsconfig.json. Every reference in that code to an allowlisted path (its file
stem, its directory prefix, or its first directory as a quoted path component) and every idiom that
enumerates files beyond a named directory must be listed below, in READERS or WALKERS; an unlisted
one fails, and so does a listed one that is gone. A reader is listed with the check-all steps that
read the path: each must be in the docs tier, or be one of the steps the fast tier skips. The data
directories (forms/, tables/, reviews/, fixtures/, sources/, reports/ ...) mention allowlisted paths
only in prose; they are read through this code, which opens no path taken from them into the allowlist.
The scan finds literal names, not paths assembled from fragments; such a path would not be caught.
"""
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = "tools/docs_paths.txt"
FULL = "tools/full_paths.txt"
STEPS = ROOT / "tools" / "check_all_steps.sh"
TIERS = ("docs", "fast", "full")

# (file, allowlist pattern) -> ("docs", [steps that read it]) when a step reads the path,
# ("slow", [steps]) when only steps the fast tier skips read it, or ("none", reason) when the
# reference is not a read by any check-all step.
_COMMENT = ("none", "a comment or docstring citing the document")
_KEY = ("none", "a dictionary key named docs, not a path")
READERS = {
    ("tools/extract_ny_household_tables.py", "docs/*"): ("none", "a table header it writes names docs/ny/DECISIONS.md; the file is not read"),
    ("tools/check_bug_inventory.py", "BUG_INVENTORY.md"): ("docs", ["check_bug_inventory"]),
    ("tools/check_bug_inventory.py", "bug_pending/*"): ("docs", ["check_bug_inventory"]),
    ("tools/new_bug.py", "bug_pending/*"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/test_bookkeeping_tools.py", "bug_pending/*"): ("none", "writes the path in a temporary repository"),
    ("tools/check_docs_conventions.py", "HANDOFF-NEXT-SESSION.md"): ("docs", ["check_docs_conventions"]),
    ("tools/check_docs_conventions.py", "docs/*"): ("docs", ["check_docs_conventions"]),
    ("tools/check_docs_conventions.py", "handoffs/*"): ("none", "named in its messages; it reads HANDOFF-NEXT-SESSION.md, not handoffs/"),
    # --check and --self-test both validate the real inventory's Siblings checked fields.
    ("tools/siblings.py", "BUG_INVENTORY.md"): ("docs", ["siblings_check", "bookkeeping_self_tests"]),
    ("tools/siblings.py", "bug_pending/*"): ("docs", ["siblings_check", "bookkeeping_self_tests"]),
    # The tests copy the real registers and run the tools on the copies (--file).
    ("tools/test_bookkeeping_tools.py", "BUG_INVENTORY.md"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/test_bookkeeping_tools.py", "TASKS.md"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/test_bookkeeping_tools.py", "TASKS-DONE.md"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/new_bug.py", "BUG_INVENTORY.md"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/task_row.py", "TASKS.md"): ("docs", ["bookkeeping_self_tests"]),
    ("tools/task_row.py", "TASKS-DONE.md"): ("docs", ["bookkeeping_self_tests"]),
    # --check compares docs/COVERAGE.md with the page it generates from canonical/.
    ("tools/coverage/tree.py", "docs/*"): ("docs", ["coverage_tree"]),
    # Validates research/costs/agent_runs.jsonl; the quoted component "research" also names research/audits.
    ("tools/check_agent_runs.py", "research/costs/*"): ("docs", ["check_agent_runs", "bookkeeping_self_tests"]),
    ("tools/check_agent_runs.py", "research/audits/*"): ("none", "the quoted component is research/costs"),
    # The hook writes the agent-run ledger outside check-all; its self-test writes a temporary one.
    ("tools/claude_hooks/agents.py", "research/costs/*"): ("none", "a Claude Code hook writes the ledger; its self-test uses a temporary directory"),
    ("tools/claude_hooks/agents.py", "research/audits/*"): ("none", "the quoted component is research/costs"),
    # Pinned open-defect survivors must name an open entry.
    ("engine/src/mutate.ts", "BUG_INVENTORY.md"): ("slow", ["mutate", "ny_mutate"]),
    ("tools/coverage/roadmap.py", "TASKS.md"): ("none", "roadmap.py is run by hand, by no check-all step"),
    ("tools/transcription/review_yield.py", "BUG_INVENTORY.md"):
        ("none", "review_yield.py runs from costs.py --yield; its test (self_tests review_yield_tests) uses a temporary tree"),
    ("tools/transcription/review_yield.py", "research/costs/*"): ("none", "as above"),
    ("tools/transcription/review_yield.py", "research/audits/*"): ("none", "the quoted component is research/costs"),
    ("tools/transcription/test_review_yield.py", "BUG_INVENTORY.md"): ("none", "writes its own inventory in a temporary tree"),
    ("engine/src/fixtures.ts", "BUG_INVENTORY.md"): ("none", "text of a fixture note"),
    ("tools/transcription/compare_families.py", "BUG_INVENTORY.md"): ("none", "text of the report it writes"),
    ("tools/coverage/tree.json", "docs/*"): ("none", "the description field names the page tree.py writes"),
    ("tools/transcription/prices.json", "docs/*"): ("none", "a vendor URL"),
    ("tools/hooks/test_green.sh", "docs/*"): ("none", "writes the path in a temporary repository"),
    ("tools/hooks/test_green.sh", "BUG_INVENTORY.md"): ("none", "writes the path in a temporary repository"),
    ("tools/hooks/test_pre_push.sh", "docs/*"): ("none", "writes the path in a temporary repository"),
    ("tools/year_diff.py", "docs/*"): _KEY,
    ("tools/transcription/test_ny_review.py", "docs/*"): _KEY,
    **{(f, "docs/*"): _COMMENT for f in [
        "engine/src/year.ts", "lean/Main.lean", "tools/check_all_steps.sh", "tools/check_consumers.py",
        "tools/check_instruction_cites.py", "tools/check_limits.py", "tools/check_operands.py", "tools/check_signs.py",
        "tools/citations.py", "tools/fixtures_year.py", "tools/jurisdiction.py",
        "tools/transcription/question_review.py", "tools/transcription/screen_review.py"]},
}

# (file, idiom) -> why the enumeration stays inside named, non-allowlisted directories.
WALKERS = {
    ("tools/engines/engine_cache.py", ".rglob("): "hashes tools/engines, the installed engines under .engines/ and its own cache; reads no docs-tier path",
    ("tools/transcription/rename_carry.py", "os.walk("): "puts ids back in a scratch copy of forms/, rendered/, canonical/, interview/ and ambiguities/; run by hand, not a check-all step",
    ("tools/transcription/rename_carry.py", "ls-tree"): "lists sources/ at the --from revision; run by hand",
    ("tools/transcription/rename_carry.py", "--name-only"): "the ls-tree listing above",
    ("tools/transcription/rename_carry.py", '"archive"'): "git archive of the --from revision into a scratch directory; run by hand",
    ("tools/transcription/test_rename_carry.py", "os.walk("): "walks reviews/ of a temporary tree of its own",
    ("tools/archive_text.py", 'glob("tools/**'): "its self-test scans tools/**/*.py",
    ("tools/check_all.sh", "--name-only"): "the run's guard: paths changed during the run, not an input of a step",
    ("tools/commit_tested.sh", "--name-only"): "commits a tested tree; not a check-all step",
    ("tools/claims.py", "--name-only"): "pre-commit: the forms a commit changes; its self-test uses a temporary repository",
    ("tools/claims.py", "ls-tree"): "pre-commit, root commit only: the forms of the first tree; not a check-all step",
    ("tools/build_fresh.py", ".rglob("): "the model sources and canonical/ by modification time; reads no docs-tier path",
    ("tools/check_bug_inventory.py", '"grep"'): "git grep for placeholders over every tracked file; a docs-tier step",
    ("tools/check_bug_inventory.py", "git grep"): "as above (named in its docstring)",
    ("tools/check_bug_inventory.py", "ls-tree"): "lists bug_pending/ at a revision",
    ("tools/check_bug_inventory.py", "--name-only"): "the ls-tree listing above",
    ("tools/new_bug.py", '"grep"'): "--assign: the tracked files citing a placeholder; not a check-all step",
    ("tools/siblings.py", '"grep"'): "git grep over forms/<year> only",
    ("tools/siblings.py", "--name-only"): "git diff over reviews/<year> logs; the unscoped one serves --reviews-since, not a step",
    ("tools/siblings.py", ".rglob("): "the --input ripple over its listed source directories; not a step",
    ("tools/year_changes.py", ".rglob("): "the files of interview/<year> only",
    ("tools/transcription/carry.py", "ls-tree"): "lists forms/ and tables/ directories at a revision",
    ("tools/transcription/carry.py", "--name-only"): "the ls-tree listings above",
    ("tools/fetch_sources.py", '"archive"'): "a dictionary key for sources/<year>",
    ("tools/transcription/audit_skipped.py", '"archive"'): "the path .classm/archive/...",
    ("tools/transcription/audit_transcription.py", "'archive'"): "the path .transcription/archive/...",
    ("tools/transcription/test_review_tools.py", "'archive'"): "a temporary directory",
    ("tools/worktree_data.py", "os.walk("): "walks reviews/ and the git-ignored data folders (.transcription/ and the rest)",
    ("tools/worktree_data.py", "ls-files"): "lists the tracked files under the git-ignored data folders",
    ("tools/defaults_guard.mjs", "ls-files"): "lists the staged fixture files in the commit-msg hook; its self-test (the check-all step) lists none",
}

# The classifier, its lists and its tests name the allowlisted paths without reading them.
SCAN_EXCLUDED = {"tools/tier_paths.py", DOCS, FULL}
SCAN_SUFFIXES = {".py", ".ts", ".mjs", ".js", ".cjs", ".sh", ".lean", ".json", ".toml", ".yaml", ".yml", ".txt"}
WALK_RE = re.compile(r"ls-files|ls-tree|os\.walk\(|\.rglob\(|glob\(\s*[\"'][^\"']*\*\*|recursive\s*=\s*True"
                     r"|git grep|[\"']grep[\"']|--name-only|git archive|[\"']archive[\"']")


def parse(text):
    """The patterns of a list file: one per line, blank lines and # comments ignored."""
    return [s for s in (line.strip() for line in text.splitlines()) if s and not s.startswith("#")]


def matches(path, patterns):
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"tier_paths: git {' '.join(args)}: {r.stderr.strip()}")
    return r


def list_at(rev, name):
    """The patterns of list file `name` in commit or tree `rev`, or None when it has none."""
    r = git("show", f"{rev}:{name}", check=False)
    return parse(r.stdout) if r.returncode == 0 else None


def changed(old, new):
    out = git("diff-tree", "-r", "--no-renames", "--name-only", old, new).stdout
    return [p for p in out.splitlines() if p]


def decide(parents, docs, triggers, changes):
    """The tier and its reason. `docs` is the first parent's allowlist (None if it has none),
    `triggers` the full-tier patterns or None, `changes` the changed paths per parent."""
    if not parents:
        return "full", "a commit with no parent needs the full tier"
    if triggers is None:
        return "full", f"a parent has no {FULL}"
    for parent, paths in zip(parents, changes):
        hit = [p for p in paths if matches(p, triggers)]
        if hit:
            return "full", f"{hit[0]} changed (against {parent[:12]}) is a full-tier path ({FULL})"
    if len(parents) > 1:
        return "fast", "a merge needs at least the fast tier"
    if docs is None:
        return "fast", f"the parent has no {DOCS}"
    outside = [p for p in changes[0] if not matches(p, docs)]
    if outside:
        return "fast", f"{outside[0]} changed and is not a docs-tier path ({DOCS})"
    return "docs", f"every changed path is a docs-tier path ({DOCS})"


def required(tree, parents):
    triggers = list_at(tree, FULL) or []
    for parent in parents:
        t = list_at(parent, FULL)
        if t is None:
            triggers = None
            break
        triggers += t
    docs = list_at(parents[0], DOCS) if parents else None
    return decide(parents, docs, triggers, [changed(p, tree) for p in parents])


# --- self-test ----------------------------------------------------------------------------------

def tier_steps():
    """(steps the fast tier skips, steps the docs tier runs), as check_all_steps.sh declares them."""
    text = STEPS.read_text(encoding="utf-8")
    found = {}
    for name in ("slow_steps", "docs_steps"):
        m = re.search(rf'^{name}=" ([a-z0-9_ ]+) "$', text, re.M)
        if not m:
            raise AssertionError(f"check_all_steps.sh declares no {name}")
        found[name] = set(m.group(1).split())
    declared = set(re.findall(r"\bstep ([a-z0-9_]+) ", text))
    for name in re.findall(r"\bjstep ([a-z0-9_]+) ", text):
        declared |= {name, f"ny_{name}"}
    for name, steps in found.items():
        unknown = steps - declared
        if unknown:
            raise AssertionError(f"check_all_steps.sh: {name} names no step {', '.join(sorted(unknown))}")
    return found["slow_steps"], found["docs_steps"]


def reference_res(pattern):
    """Regexes that find a reference to an allowlisted path in code."""
    if pattern.endswith("/*"):
        d = pattern[:-2]
        first = d.split("/")[0]
        return [re.compile(rf"(?<![\w.-]){re.escape(d)}(/|[\"'`])"), re.compile(rf"[\"']{re.escape(first)}[\"']")]
    stem = Path(pattern).stem
    return [re.compile(rf"(?<![A-Za-z0-9_]){re.escape(stem)}(?![A-Za-z0-9_])")]


def surface():
    files = git("ls-files", "tools", "engine", "lean", "package.json", "tsconfig.json").stdout.splitlines()
    out = []
    for f in files:
        if f in SCAN_EXCLUDED:
            continue
        p = Path(f)
        if p.suffix in SCAN_SUFFIXES or (p.parent.as_posix() == "tools/hooks" and not p.suffix):
            out.append(f)
    return out


def scan(files, allow, read=lambda f: (ROOT / f).read_text(encoding="utf-8", errors="ignore")):
    refs, walks = {}, {}
    for f in files:
        text = read(f)
        for pattern in allow:
            n = sum(len(r.findall(text)) for r in reference_res(pattern))
            if n:
                refs[(f, pattern)] = n
        for m in WALK_RE.findall(text):
            walks[(f, m)] = walks.get((f, m), 0) + 1
    return refs, walks


def check_ledgers(refs, walks, slow, docs_tier):
    problems = []
    for key in sorted(set(refs) - set(READERS)):
        problems.append(f"{key[0]} refers to the docs-tier path {key[1]} ({refs[key]}x) and is not in READERS")
    for key in sorted(set(READERS) - set(refs)):
        problems.append(f"READERS lists {key[0]} for {key[1]}, which it no longer refers to")
    for key, (kind, what) in sorted(READERS.items()):
        if kind == "docs":
            missing = [s for s in what if s not in docs_tier]
            if missing:
                problems.append(f"{key[0]} reads {key[1]} in step(s) {', '.join(missing)}, not in the docs tier")
        elif kind == "slow":
            missing = [s for s in what if s not in slow]
            if missing:
                problems.append(f"{key[0]} reads {key[1]} in step(s) {', '.join(missing)}, which the fast tier runs")
        elif kind != "none":
            problems.append(f"READERS: {key}: unknown kind {kind}")
    for key in sorted(set(walks) - set(WALKERS)):
        problems.append(f"{key[0]} enumerates files with {key[1]!r} and is not in WALKERS")
    for key in sorted(set(WALKERS) - set(walks)):
        problems.append(f"WALKERS lists {key[0]} for {key[1]!r}, which it no longer uses")
    return problems


def check_lists(allow, triggers, tracked):
    problems = []
    for p in allow:
        body = p[:-2] if p.endswith("/*") else p
        if any(c in body for c in "*?[") or not body or body.startswith("/"):
            problems.append(f"{DOCS}: {p!r} is neither an exact file nor a whole directory (dir/*)")
        if matches(DOCS, [p]) or matches(FULL, [p]) or any(matches(f, [p]) for f in SCAN_EXCLUDED):
            problems.append(f"{DOCS}: {p!r} covers the classifier or its lists")
        hit = [f for f in surface_like(tracked) if matches(f, [p])]
        if hit:
            problems.append(f"{DOCS}: {p!r} covers code check-all runs ({hit[0]})")
    for p in triggers:
        if not any(matches(f, [p]) for f in tracked):
            problems.append(f"{FULL}: {p!r} matches no tracked file")
    both = [f for f in tracked if matches(f, allow) and matches(f, triggers)]
    if both:
        problems.append(f"{both[0]} is both a docs-tier and a full-tier path")
    for t in triggers:
        if matches(t.replace("*", "x"), allow):
            problems.append(f"{FULL}: {t!r} lies inside the docs-tier paths")
    return problems


def surface_like(tracked):
    return [f for f in tracked if f.split("/")[0] in ("tools", "engine", "lean") or f in ("package.json", "tsconfig.json")]


# Paths whose tier under the real tools/full_paths.txt is fixed: True for full, False for not full.
FULL_EXAMPLES = {
    "tools/engines/engine_cache.py": True,
    "tools/human_review/logs.py": False,
    "tools/human_review/README.md": False,
    "engine/src/mutate.ts": True,
}


def check_examples(triggers):
    return [f"{FULL}: {path} {'should' if want else 'should not'} need the full tier"
            for path, want in FULL_EXAMPLES.items() if matches(path, triggers) != want]


def unit_tests():
    allow = ["BUG_INVENTORY.md", "docs/*"]
    trig = ["engine/src/mutate*.ts", "lean/*"]
    cases = [
        (["p"], [["docs/a.md", "BUG_INVENTORY.md"]], "docs"),
        (["p"], [[]], "docs"),
        (["p"], [["docs/a.md", "README.md"]], "fast"),
        (["p"], [["docs.md"]], "fast"),
        (["p"], [["xdocs/a.md"]], "fast"),
        (["p"], [["engine/src/mutate-worker.ts"]], "full"),
        (["p"], [["lean/TaxFormalization/X.lean", "docs/a.md"]], "full"),
        (["p", "q"], [["docs/a.md"], ["docs/a.md"]], "fast"),
        (["p", "q"], [["docs/a.md"], ["lean/x"]], "full"),
        ([], [], "full"),
    ]
    for parents, changes, want in cases:
        got = decide(parents, allow, trig, changes)[0]
        assert got == want, (parents, changes, got, want)
    assert decide(["p"], allow, None, [["docs/a.md"]])[0] == "full"
    assert decide(["p"], None, trig, [["docs/a.md"]])[0] == "fast"
    assert parse("# c\n\n a \nb/*\n") == ["a", "b/*"]
    # The scan finds each form of reference and each enumeration idiom, and the ledgers catch both ways.
    text = {"t/a.py": 'x = ROOT / "docs" / "COVERAGE.md"\n', "t/b.ts": 'readFileSync(join(ROOT, "BUG_INVENTORY.md"))\n',
            "t/c.py": "# see docs/ny/X.md\n", "t/d.py": "for p in ROOT.rglob('*'):\n", "t/e.py": "x = 'research'\n"}
    refs, walks = scan(sorted(text), ["docs/*", "BUG_INVENTORY.md", "research/costs/*"], read=text.__getitem__)
    assert set(refs) == {("t/a.py", "docs/*"), ("t/b.ts", "BUG_INVENTORY.md"), ("t/c.py", "docs/*"),
                         ("t/e.py", "research/costs/*")}, refs
    assert set(walks) == {("t/d.py", ".rglob(")}, walks
    global READERS, WALKERS
    saved = READERS, WALKERS
    try:
        READERS = {("t/a.py", "docs/*"): ("docs", ["coverage_tree"]), ("t/b.ts", "BUG_INVENTORY.md"): ("docs", ["mutate"]),
                   ("t/c.py", "docs/*"): ("none", "comment"), ("t/e.py", "research/costs/*"): ("slow", ["siblings_check"]),
                   ("t/z.py", "docs/*"): ("none", "gone")}
        WALKERS = {}
        problems = check_ledgers(refs, walks, {"mutate"}, {"coverage_tree", "siblings_check"})
        want = ["not in WALKERS", "no longer refers", "t/b.ts reads BUG_INVENTORY.md in step(s) mutate, not in the docs tier",
                "t/e.py reads research/costs/* in step(s) siblings_check, which the fast tier runs"]
        for w in want:
            assert any(w in p for p in problems), (w, problems)
        assert len(problems) == len(want), problems
    finally:
        READERS, WALKERS = saved
    assert check_lists(["docs/*", "tools/x/*", "a*.md"], ["lean/*", "docs/x"], ["docs/a", "lean/b", "tools/x/y.py"])
    assert not check_lists(["docs/*"], ["lean/*"], ["docs/a", "lean/b"])
    assert check_examples(["tools/human_review/*"]) == [f"{FULL}: tools/engines/engine_cache.py should need the full tier",
                                                         f"{FULL}: tools/human_review/logs.py should not need the full tier",
                                                         f"{FULL}: tools/human_review/README.md should not need the full tier",
                                                         f"{FULL}: engine/src/mutate.ts should need the full tier"]


def self_test():
    unit_tests()
    tracked = git("ls-files").stdout.splitlines()
    allow = parse((ROOT / DOCS).read_text(encoding="utf-8"))
    triggers = parse((ROOT / FULL).read_text(encoding="utf-8"))
    slow, docs_tier = tier_steps()
    problems = check_lists(allow, triggers, tracked) + check_examples(triggers)
    files = surface()
    refs, walks = scan(files, allow)
    problems += check_ledgers(refs, walks, slow, docs_tier)
    if problems:
        print("tier paths self-test: FAILED", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    print(f"tier paths self-test: ok ({len(allow)} docs-tier patterns, {len(triggers)} full-tier patterns, "
          f"{len(files)} code files scanned, {len(READERS)} references and {len(WALKERS)} enumerations accounted for)")
    return 0


def main(argv):
    if argv[:1] == ["--self-test"]:
        return self_test()
    if len(argv) >= 2 and argv[0] == "required":
        tier, reason = required(argv[1], argv[2:])
        print(f"{tier}\t{reason}")
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
