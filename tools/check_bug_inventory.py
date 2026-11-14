#!/usr/bin/env python3
"""Fail unless BUG_INVENTORY.md and its pending entries keep the inventory's rule.

The inventory is append-only: the committed content (git HEAD) must be a byte-for-byte prefix of
the working file, and entry ids run from BUG-0001 with no gaps or repeats. A branch records a new
defect as a pending entry, one file `bug_pending/<name>.md` holding one entry headed
`## BUG-NEW-<name> — <title>`, and cites it elsewhere as `BUG-NEW-<name>`. Pending entries get their
ids in the merge that brings them onto main (`tools/new_bug.py --assign`): appended to the
inventory in name order, the placeholders rewritten to the ids in every tracked file, the files
deleted. So lanes working at once never write the inventory and never collide.

    check_bug_inventory.py                       the working tree against HEAD: the inventory extends HEAD's
                                                 and is gapless; every pending file is well formed; every
                                                 pending file committed at HEAD is present and unchanged;
                                                 every BUG-NEW placeholder in a tracked file names a pending file
    check_bug_inventory.py --merge TREE PARENT...  pre-commit, concluding a merge: every parent's inventory is
                                                 a prefix of TREE's; what TREE appends after the longest of them
                                                 is exactly the parents' pending entries TREE no longer has, as
                                                 new_bug.py --assign appends them; every pending file TREE keeps
                                                 is a parent's, with only assigned placeholders rewritten
    check_bug_inventory.py --self-test
"""
import pathlib
import re
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent.parent
INVENTORY = "BUG_INVENTORY.md"
PENDING_DIR = "bug_pending"
path = root / INVENTORY
HEADING = re.compile(r"^## BUG-\d{4} .*$", re.M)
ID = re.compile(r"^## BUG-(\d{4}) ", re.M)
NAME = r"[a-z0-9]+(?:-[a-z0-9]+)*"
NAME_RE = re.compile(rf"^{NAME}$")
PLACEHOLDER = re.compile(rf"BUG-NEW-({NAME})")
PLACEHOLDER_ERE = "BUG-NEW-[a-z0-9]+(-[a-z0-9]+)*"  # the same, for git grep -E
PENDING_HEAD = re.compile(rf"\A## BUG-NEW-({NAME}) — (\S.*)\n")


def natural_key(name):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", name)]


def ids_of(text):
    return [int(m) for m in ID.findall(text)]


def substitute(text, mapping):
    """`text` with each placeholder BUG-NEW-<name> whose name is in `mapping` replaced by its id."""
    return PLACEHOLDER.sub(lambda m: mapping.get(m.group(1), m.group(0)), text)


def pending_problems(pending):
    """Problems with the pending files {name: text}: each holds one entry headed by its own name."""
    out = []
    for name, text in sorted(pending.items()):
        m = PENDING_HEAD.match(text)
        if not NAME_RE.match(name):
            out.append(f"{PENDING_DIR}/{name}.md: the name must be lower-case letters and digits joined by '-'")
        elif not m or m.group(1) != name:
            out.append(f"{PENDING_DIR}/{name}.md: must begin with the line '## BUG-NEW-{name} — <title>'")
        elif re.search(r"^## ", text[m.end():], re.M):
            out.append(f"{PENDING_DIR}/{name}.md: holds more than one '## ' heading; one entry per file")
        elif not text.endswith("\n"):
            out.append(f"{PENDING_DIR}/{name}.md: does not end with a newline")
    return out


def assign(inventory, pending):
    """The inventory with the pending entries {name: text} appended in name order, and {name: id}.

    Each entry gets the next id; every assigned placeholder in the appended entries becomes its id."""
    n = len(ids_of(inventory))
    names = sorted(pending, key=natural_key)
    mapping = {name: f"BUG-{n + k:04d}" for k, name in enumerate(names, 1)}
    tail = "".join("\n" + substitute(pending[name], mapping) for name in names)
    return inventory + tail, mapping


def working_problems(head_inv, head_pending, inv, pending, placeholders):
    """Problems of a working tree (inventory text, pending {name: text}, placeholder names found in
    tracked files) against HEAD's inventory and pending files."""
    out = []
    if head_inv is not None and not inv.startswith(head_inv):
        out.append(f"{INVENTORY}: committed content was modified or removed; the file is append-only")
    ids = ids_of(inv)
    if ids != list(range(1, len(ids) + 1)):
        out.append(f"{INVENTORY}: entry ids must run BUG-0001.. without gaps or repeats; found {ids}")
    out += pending_problems(pending)
    for name, text in sorted(head_pending.items()):
        if pending.get(name) != text:
            out.append(f"{PENDING_DIR}/{name}.md: a committed pending entry was changed or removed; it is "
                       "replaced only by its assignment in a merge (tools/new_bug.py --assign)")
    for name in sorted(set(placeholders) - set(pending)):
        out.append(f"BUG-NEW-{name} is cited ({', '.join(sorted(placeholders[name])[:3])}) but no pending "
                   f"file {PENDING_DIR}/{name}.md exists")
    return out


def merge_problems(result_inv, result_pending, parents):
    """Problems of a merge's result against its parents, each (inventory text, pending {name: text})."""
    out = []
    for k, (inv, _) in enumerate(parents, 1):
        if not result_inv.startswith(inv):
            new = [h for h in HEADING.findall(result_inv) if h not in HEADING.findall(inv)]
            out.append(f"{INVENTORY}: parent {k}'s inventory is not a prefix of the merge's; the merge rewrites, "
                       "drops or renumbers its entries" + (f" (first differing: {new[0][3:60]})" if new else ""))
    if out:
        return out
    longest = max((inv for inv, _ in parents), key=len)
    offered = {}
    for _, pending in parents:
        for name, text in pending.items():
            if offered.setdefault(name, text) != text:
                out.append(f"{PENDING_DIR}/{name}.md: two parents hold different entries under one name")
    if out:
        return out
    assigned = {n: t for n, t in offered.items() if n not in result_pending}
    want, mapping = assign(longest, assigned)
    if result_inv != want:
        extra = [h for h in HEADING.findall(result_inv[len(longest):])]
        out.append(f"{INVENTORY}: what the merge appends is not the parents' pending entries it removes "
                   f"({', '.join(sorted(assigned, key=natural_key)) or 'none'}), appended by tools/new_bug.py "
                   "--assign" + (f"; it appends {'; '.join(h[3:60] for h in extra[:3])}" if extra else ""))
    for name, text in sorted(result_pending.items()):
        if name not in offered:
            out.append(f"{PENDING_DIR}/{name}.md: the merge creates a pending entry; record it on a branch")
        elif substitute(offered[name], mapping) != text:
            out.append(f"{PENDING_DIR}/{name}.md: the merge changes a pending entry it does not assign")
    return out


def git(*args, cwd=root):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def state_at(tree, cwd=root):
    """(inventory text or None, pending {name: text}) of a commit or tree."""
    r = git("show", f"{tree}:{INVENTORY}", cwd=cwd)
    inv = r.stdout if r.returncode == 0 else None
    pending = {}
    names = git("ls-tree", "--name-only", f"{tree}:{PENDING_DIR}", cwd=cwd)
    for f in names.stdout.splitlines() if names.returncode == 0 else []:
        if f.endswith(".md"):
            pending[f[:-3]] = git("show", f"{tree}:{PENDING_DIR}/{f}", cwd=cwd).stdout
    return inv, pending


def working_pending():
    d = root / PENDING_DIR
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))} if d.is_dir() else {}


def placeholders_in_tracked():
    """{name: [files]} for every BUG-NEW placeholder in the tracked files of the working tree."""
    out = {}
    r = git("grep", "-I", "-o", "-E", PLACEHOLDER_ERE)
    for line in r.stdout.splitlines():
        f, _, token = line.partition(":")
        out.setdefault(PLACEHOLDER.match(token).group(1), []).append(f)
    return out


def check_working():
    head_inv, head_pending = state_at("HEAD")
    inv = path.read_text(encoding="utf-8")
    pending = working_pending()
    problems = working_problems(head_inv, head_pending, inv, pending, placeholders_in_tracked())
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        return 1
    print(f"bug inventory OK ({len(ids_of(inv))} entries, append-only; {len(pending)} pending)")
    return 0


def check_merge(tree, parents, cwd=root):
    result_inv, result_pending = state_at(tree, cwd)
    states = [state_at(p, cwd) for p in parents]
    problems = merge_problems(result_inv or "", result_pending, [(inv or "", pend) for inv, pend in states])
    for p in problems:
        print(f"pre-commit: {p}", file=sys.stderr)
    return 1 if problems else 0


def self_test():
    N = "BUG-" + "NEW-"  # built, so that this file cites no placeholder
    head = "# Bug inventory\n\n---\n\n## BUG-0001 — one\n\n- **Fix:** x\n"
    main = head + "\n## BUG-0002 — two\n\n- **Fix:** y\n"
    a = {"lane-a-01": f"## {N}lane-a-01 — from a\n\n- **Symptom:** see {N}lane-a-02\n",
         "lane-a-02": f"## {N}lane-a-02 — also from a\n\n- **Symptom:** s\n"}
    b = {"lane-b-01": f"## {N}lane-b-01 — from b\n\n- **Symptom:** s\n"}
    cases = []

    def case(label, got, want_substr):
        ok = (not got) if want_substr is None else any(want_substr in g for g in got)
        cases.append((label, ok, got))

    # The working tree against HEAD.
    case("append", working_problems(head, {}, main, {}, {}), None)
    case("rewritten entry", working_problems(main, {}, main.replace("two", "TWO"), {}, {}), "append-only")
    case("dropped entry", working_problems(main, {}, head, {}, {}), "append-only")
    case("reused id", working_problems(head, {}, main + "\n## BUG-0002 — again\n", {}, {}), "without gaps")
    case("pending added", working_problems(main, {}, main, a, {"lane-a-02": ["x"]}), None)
    case("pending changed", working_problems(main, a, main, {**a, "lane-a-01": a["lane-a-02"]}, {}), f"{N}lane-a-01 — <title>")
    case("pending edited", working_problems(main, a, main, {**a, "lane-a-02": a["lane-a-02"] + "more\n"}, {}),
         "committed pending entry was changed")
    case("pending dropped", working_problems(main, a, main, {"lane-a-01": a["lane-a-01"]}, {}),
         "committed pending entry was changed or removed")
    case("pending numbered", working_problems(main, {}, main, {"x-1": "## BUG-0003 — t\n"}, {}), "must begin")
    case("pending two entries", working_problems(main, {}, main, {"x-1": f"## {N}x-1 — t\n\n## B\n"}, {}),
         "more than one")
    case("dangling placeholder", working_problems(main, {}, main, {}, {"gone-1": ["notes.txt"]}), f"{N}gone-1 is cited")

    # Merges: main has moved on (BUG-0002) since lanes a and b were cut from `head`.
    after_a, map_a = assign(main, a)
    case("lane a merged", merge_problems(after_a, {}, [(main, {}), (head, a)]), None)
    case("lane a cross-reference rewritten", [] if "see BUG-0004" in after_a and map_a["lane-a-02"] == "BUG-0004"
         else ["not rewritten"], None)
    after_ab, _ = assign(after_a, b)
    case("then lane b", merge_problems(after_ab, {}, [(after_a, {}), (head, b)]), None)
    after_b, _ = assign(main, b)
    after_ba, _ = assign(after_b, a)
    case("lane b first", merge_problems(after_b, {}, [(main, {}), (head, b)]), None)
    case("then lane a", merge_problems(after_ba, {}, [(after_b, {}), (head, a)]), None)
    both = [h for h in HEADING.findall(after_ab)][2:]
    case("both orders keep every entry once", [] if len(both) == 3 and set(h[13:] for h in both)
         == set(h[13:] for h in HEADING.findall(after_ba)[2:]) and ids_of(after_ab) == [1, 2, 3, 4, 5]
         and ids_of(after_ba) == [1, 2, 3, 4, 5] else ["entries differ"], None)
    case("assigned at merge rewritten", merge_problems(after_a.replace("from a", "From a"), {}, [(main, {}), (head, a)]),
         "not the parents' pending entries")
    case("pending dropped at merge", merge_problems(main, {}, [(main, {}), (head, a)]), "not the parents' pending")
    case("pending kept at merge", merge_problems(main, a, [(main, {}), (head, a)]), None)
    case("partly assigned", merge_problems(assign(main, {"lane-a-01": a["lane-a-01"]})[0],
                                           {"lane-a-02": a["lane-a-02"]}, [(main, {}), (head, a)]), None)
    case("reused id at merge", merge_problems(head + "\n## BUG-0002 — from b\n", {}, [(main, {}), (head, b)]),
         "parent 1's inventory is not a prefix")
    case("renumbered branch entry", merge_problems(main + "\n## BUG-0003 — mine\n", {},
                                                   [(main, {}), (head + "\n## BUG-0002 — mine\n", {})]),
         "parent 2's inventory is not a prefix")
    case("old-style branch append", merge_problems(main + "\n## BUG-0003 — c\n", {},
                                                   [(main, {}), (main + "\n## BUG-0003 — c\n", {})]), None)
    case("created at merge", merge_problems(main + "\n## BUG-0003 — new\n", {}, [(main, {}), (head, {})]),
         "not the parents' pending")
    case("pending created at merge", merge_problems(main, b, [(main, {}), (head, {})]), "creates a pending entry")
    case("same name, two entries", merge_problems(main, {}, [(main, {"x-1": f"## {N}x-1 — p\n"}),
                                                             (head, {"x-1": f"## {N}x-1 — q\n"})]),
         "two parents hold different entries")
    bad = [(label, got) for label, ok, got in cases if not ok]
    print("bug inventory self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--self-test"]:
        sys.exit(self_test())
    if sys.argv[1:2] == ["--merge"]:
        sys.exit(check_merge(sys.argv[2], sys.argv[3:]))
    sys.exit(check_working())
