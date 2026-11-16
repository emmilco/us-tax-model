#!/usr/bin/env python3
"""Each bug entry's status, read from the inventory, its pending entries and the task registers.

    bug_status.py                    the count of entries per status
    bug_status.py BUG-0129 ...       the status of each named entry, with what decided it
    bug_status.py --open             the open entries, one per line, with the open task rows that cover them
    bug_status.py --write            write reports/bug_status.md
    bug_status.py --check            fail when a closure is malformed or names no entry, or when
                                     reports/bug_status.md is not what --write writes (a docs-tier step)
    bug_status.py --self-test

BUG_INVENTORY.md is append-only, so an entry's status is never edited into it. It is derived:

1. From the entry's own fields, the first that applies:
   - `Closure:` makes the entry a closure record (it records the closing of others; it is no defect), and so
     does closing others (step 2) with no `Symptom:`, status or fix field of its own;
   - `Duplicate of:` closes it as a duplicate;
   - `Status:`, `Disposition:` or `Proposed disposition:` beginning "fixed", "closed", "resolved" or "the
     check is fixed": fixed; beginning anything else ("open", a task id, "needs ..."): open;
   - a fix field (`Fix:`, `Fix (owner):`, `Tool change:`, `Wording fix:`, `Changed form lines:`), not empty and
     not beginning "open", "not fixed", "unfixed", "either", "pending", "deferred", "to be fixed" or
     "proposed": fixed;
   - otherwise (no field, an empty or open fix field, or only `Proposed fix:`, `Fix sketch:`, `Possible fix:`,
     `Fix (proposed):`, `Remedy:` or `Resolution:`): open.
2. Then from later entries, in inventory order (pending entries last, in the order --assign numbers them):
   - a `Closes:` field closes the ids it begins with ("BUG-0134", "BUG-0134, BUG-0135 and BUG-0138",
     "BUG-0500, BUG-0522 to BUG-0528"); prose may follow the list. The closure is partial, and the entry stays
     open, when the prose after the list says so ("in part", "partly", "mostly", "stays open", "remains open",
     "the ... part", or begins "for"). Its kind is the closing entry's `Closure:` field: `fixed`, `won't fix`,
     `superseded`, `duplicate`, `not a defect` or `disposed` (default `fixed`);
   - the title conventions of entries written before the field: "BUG-x is fixed: ...", "BUG-x and BUG-y are
     fixed", "BUG-x is settled" / "is closed" / "is resolved", "BUG-x fixed" / "completed", "Fix for BUG-x:",
     "Disposition of BUG-x" (kind disposed), "Closure: BUG-x ... were fixed", "(closes BUG-x)", and "... (BUG-x)
     ... fixed ..." for a round's lows. "is mostly fixed", "is partly fixed", "is fixed for ...", "BUG-x's ...
     is resolved" and "in part" are partial. A title closure also applies beside a `Closes:` field, for the ids
     the field's leading list does not name;
   - a `Reopens:` field reopens the ids it begins with.
   A closing entry may name a pending entry by its placeholder (BUG-NEW-<name>). It may also stand before the
   entry it closes: --assign numbers pending entries in name order, not in the order they were written.
3. An open entry is covered by a task when a row of TASKS.md names it, or when its Status, Disposition or
   fix field names a task id that is a row of TASKS.md. A row of TASKS-DONE.md naming an open entry is
   listed as a hint that a closure entry is due.

To close an entry, record a closure entry (tools/new_bug.py "Closure: BUG-x is fixed" --pending PREFIX
--field "Closes=BUG-x" --field "Closure=fixed" --field "Evidence=..."). reports/bug_status.md lists every
open entry; pending entries are listed under their placeholders after the numbered ones, in the order
--assign numbers them, so the rewriting of placeholders at assignment keeps the report current.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INVENTORY = "BUG_INVENTORY.md"
PENDING_DIR = "bug_pending"
TASKS = "TASKS.md"
TASKS_DONE = "TASKS-DONE.md"
REPORT = "reports/bug_status.md"

ID = r"BUG-(?:\d{4}|NEW-[a-z0-9]+(?:-[a-z0-9]+)*)"
HEAD = re.compile(rf"^## ({ID}) — (.*)$", re.M)
FIELD = re.compile(r"^- \*\*([^*]+?):\*\*[ ]?(.*)$")
# A list of ids: "BUG-0001", "BUG-0001, BUG-0002 and BUG-0003", "BUG-0500, BUG-0522 to BUG-0528".
ID_LIST = rf"{ID}(?:(?:,? and |, | to ){ID})*"
ID_LIST_RE = re.compile(ID_LIST)
ID_RE = re.compile(ID)
TASK_RE = re.compile(r"\bT-\d{3}\b")
RANGE_MAX = 60

STATUS_FIELDS = ("Status", "Disposition", "Proposed disposition")
FIX_FIELDS = ("Fix", "Fix (owner)", "Tool change", "Wording fix", "Changed form lines")
PROPOSAL_FIELDS = ("Fix (proposed)", "Proposed fix", "Fix sketch", "Possible fix", "Remedy", "Resolution")
CLOSURE_KINDS = ("fixed", "won't fix", "superseded", "duplicate", "not a defect", "disposed")
CLOSED_WORD = re.compile(r"^(fixed|closed|resolved|the check is fixed)\b", re.I)
OPEN_FIX = re.compile(r"^(open|not fixed|unfixed|either|pending|deferred|to be fixed|proposed)\b", re.I)
PARTIAL = re.compile(r"\b(in part|partly|mostly|stays? open|remains? open|the [^;.]*\bpart)\b|^\W*for\b", re.I)

# Title conventions for a closure, each (regex, kind); the id list is the group "ids", what follows it "rest".
TITLE_CLOSURES = [
    (re.compile(rf"^(?:The )?(?P<ids>{ID_LIST})(?: [a-z-]+)?(?P<poss>'s [^:]*?)? (?:is|are) (?P<adv>(?:mostly |partly )?)"
                rf"(?:fixed|closed|settled|resolved)\b(?P<rest>.*)$"), "fixed"),
    (re.compile(rf"^(?P<ids>{ID_LIST}) (?:fixed|completed)\b(?P<rest>.*)$"), "fixed"),
    (re.compile(rf"^Fix for (?P<ids>{ID_LIST})\b(?P<rest>.*)$"), "fixed"),
    (re.compile(rf"^Disposition of (?P<ids>{ID_LIST})\b(?P<rest>.*)$"), "disposed"),
    (re.compile(rf"^Closure: (?P<ids>{ID_LIST}) (?:was|were|is|are) fixed\b(?P<rest>.*)$"), "fixed"),
    (re.compile(rf"\(closes (?P<ids>{ID_LIST})\)(?P<rest>)"), "fixed"),
    (re.compile(rf"^[^:]*?\((?P<ids>{ID_LIST})\)[^:]*?\bfixed\b(?P<rest>.*)$"), "fixed"),
]


class Entry:
    def __init__(self, ident, title, fields, pending):
        self.id, self.title, self.fields, self.pending = ident, title, fields, pending
        self.own, self.own_reason = own_status(fields, title)
        self.status, self.reason = self.own, self.own_reason
        self.by = None          # the entry that closed it
        self.kind = None        # the closure's kind
        self.partial = []       # entries that close it in part
        self.tasks = []         # open task rows covering it
        self.done_tasks = []    # done task rows naming it


def parse_entries(text, pending=False):
    """[Entry] of a text holding '## BUG-... — title' headings and '- **Field:** value' bullets."""
    marks = list(HEAD.finditer(text))
    out = []
    for i, m in enumerate(marks):
        body = text[m.end():marks[i + 1].start() if i + 1 < len(marks) else len(text)]
        fields, cur = {}, None
        for line in body.splitlines():
            f = FIELD.match(line)
            if f:
                cur = f.group(1).strip()
                fields[cur] = (fields.get(cur, "") + " " + f.group(2)).strip()
            elif cur and line.strip() and line.strip() != "---":
                fields[cur] += " " + line.strip()
            elif line.strip() == "---":
                cur = None
        out.append(Entry(m.group(1), m.group(2).strip(), fields, pending))
    return out


def own_status(fields, title=""):
    if "Closure" in fields:
        return "record", "a closure record (Closure field)"
    if "Symptom" not in fields and not any(n in fields for n in STATUS_FIELDS + FIX_FIELDS) and (
            "Closes" in fields or any(rx.search(title) for rx, _ in TITLE_CLOSURES)):
        return "record", "a closure record (closes others; no symptom or fix of its own)"
    if "Duplicate of" in fields:
        return "closed", "Duplicate of field"
    for name in STATUS_FIELDS:
        if name in fields:
            value = fields[name]
            return ("fixed" if CLOSED_WORD.match(value) else "open"), f"{name}: {value[:60]}"
    for name in FIX_FIELDS:
        if name in fields:
            value = fields[name].strip()
            if value and not OPEN_FIX.match(value):
                return "fixed", f"{name} field"
            return "open", f"{name}: {value[:60] or '(empty)'}"
    proposed = [n for n in PROPOSAL_FIELDS if n in fields]
    if proposed:
        return "open", f"only a proposal ({proposed[0]} field)"
    return "open", "no fix or status field"


def expand(id_list):
    """The ids of an id list, with 'BUG-x to BUG-y' ranges expanded."""
    toks = re.findall(rf"({ID})|( to )", id_list)
    ids, want_range = [], False
    for ident, to in toks:
        if to:
            want_range = True
            continue
        if want_range and ids and ids[-1][4:].isdigit() and ident[4:].isdigit():
            lo, hi = int(ids[-1][4:]), int(ident[4:])
            if 0 < hi - lo <= RANGE_MAX:
                ids += [f"BUG-{n:04d}" for n in range(lo + 1, hi + 1)]
                want_range = False
                continue
        ids.append(ident)
        want_range = False
    return ids


def leading_ids(value):
    """(ids, rest) of a field beginning with an id list; ([], value) when it does not."""
    m = ID_LIST_RE.match(value.strip())
    if not m:
        return [], value
    return expand(m.group(0)), value.strip()[m.end():]


def closures_of(entry):
    """[(target id, kind, partial, how)] that an entry declares: its Closes and Reopens fields, else its title."""
    out = []
    kind = (entry.fields.get("Closure") or "fixed").strip().rstrip(".").lower()
    kind = next((k for k in CLOSURE_KINDS if kind.startswith(k)), kind)
    if "Closes" in entry.fields:
        ids, rest = leading_ids(entry.fields["Closes"])
        partial = bool(PARTIAL.search(rest))
        out += [(i, kind, partial, "Closes field") for i in ids]
    if "Reopens" in entry.fields:
        ids, _ = leading_ids(entry.fields["Reopens"])
        out += [(i, "reopened", False, "Reopens field") for i in ids]
    named = {t for t, *_ in out}
    for rx, tkind in TITLE_CLOSURES:
        m = rx.search(entry.title)
        if m:
            groups = m.groupdict()
            partial = bool(groups.get("poss") or groups.get("adv") or PARTIAL.search(groups.get("rest") or ""))
            out += [(i, tkind, partial, "title") for i in expand(m.group("ids")) if i not in named]
            break
    if "Duplicate of" in entry.fields:
        ids, _ = leading_ids(entry.fields["Duplicate of"])
        entry.by = ids[0] if ids else None
        entry.kind = "duplicate"
    return out


def task_rows(text):
    """{task id: row text} of a register's table rows."""
    return {m.group(1): m.group(0) for m in re.finditer(r"^\| (T-\d{3}) \|.*$", text, re.M)}


def named_ids(text):
    """The ids a text names, with "BUG-x to BUG-y", "BUG-x to yyyy" and "BUG-x/yyyy/zzzz" expanded."""
    text = re.sub(r"\b(BUG-\d{4}) to (\d{4})\b", r"\1 to BUG-\2", text)
    text = re.sub(r"\b(BUG-\d{4})((?:/\d{4})+)", lambda m: m.group(1) + m.group(2).replace("/", " BUG-"), text)
    return set(expand(" ".join(m.group(0) for m in ID_LIST_RE.finditer(text))))


def derive(inventory, pending, tasks_text, done_text):
    """[Entry] in inventory order (pending last, in --assign's order) with statuses derived, and [problem]."""
    entries = parse_entries(inventory)
    for name in sorted(pending, key=natural_key):
        entries += parse_entries(pending[name], pending=True)
    by_id = {e.id: e for e in entries}
    problems = []
    for e in entries:
        if "Closes" in e.fields and not leading_ids(e.fields["Closes"])[0]:
            problems.append(f"{e.id}: its Closes field does not begin with an entry id")
        if "Closure" in e.fields:
            kind = e.fields["Closure"].strip().rstrip(".").lower()
            if not any(kind.startswith(k) for k in CLOSURE_KINDS):
                problems.append(f"{e.id}: Closure '{e.fields['Closure'][:40]}' is not one of {', '.join(CLOSURE_KINDS)}")
            if "Closes" not in e.fields:
                problems.append(f"{e.id}: a Closure field with no Closes field")
        for target, kind, partial, how in closures_of(e):
            t = by_id.get(target)
            if t is None:
                problems.append(f"{e.id}: its {how} names {target}, which is no entry")
                continue
            if target == e.id:
                problems.append(f"{e.id}: its {how} names the entry itself")
                continue
            if kind == "reopened":
                t.status, t.reason, t.by, t.kind = "open", f"reopened by {e.id}", None, None
            elif partial:
                t.partial.append(e.id)
            elif t.status == "open":
                t.status, t.reason, t.by, t.kind = "closed", f"closed by {e.id} ({how})", e.id, kind
    open_rows, done_rows = task_rows(tasks_text), task_rows(done_text)
    named_open = {t: named_ids(row) for t, row in open_rows.items()}
    named_done = {t: named_ids(row) for t, row in done_rows.items()}
    for e in entries:
        if e.status != "open":
            continue
        own_text = " ".join(e.fields.get(n, "") for n in STATUS_FIELDS + FIX_FIELDS)
        cited = set(TASK_RE.findall(own_text))
        e.tasks = sorted({t for t, ids in named_open.items() if e.id in ids} | (cited & set(open_rows)))
        e.done_tasks = sorted({t for t, ids in named_done.items() if e.id in ids} | (cited & set(done_rows)))
    return entries, problems


def natural_key(name):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", name)]


def report(entries):
    """The text of reports/bug_status.md. Nothing in it depends on whether an entry is pending, so assigning ids
    (which rewrites placeholders in tracked files) keeps it current."""
    opened = [e for e in entries if e.status == "open"]
    covered = [e for e in opened if e.tasks]
    bare = [e for e in opened if not e.tasks]
    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1
    lines = [
        "# Open bug entries",
        "",
        "Generated by `python3 tools/bug_status.py --write` from `BUG_INVENTORY.md`, `bug_pending/`, `TASKS.md`",
        "and `TASKS-DONE.md`; check-all (`bug_status`) fails when it is not current. Do not edit it: close an entry",
        "with a closure entry (see the tool's docstring). The rules that derive a status are in the tool's docstring.",
        "",
        f"Entries: {len(entries)}. " + ", ".join(f"{k}: {counts[k]}" for k in ("open", "fixed", "closed", "record")
                                                 if k in counts) + ".",
        f"Open: {len(opened)}, of which {len(covered)} are covered by a row of `TASKS.md` and {len(bare)} by none.",
        "",
        "## Open, covered by a task row",
        "",
        "| Entry | Title | Task rows | Notes |",
        "| --- | --- | --- | --- |",
    ]
    lines += [row(e, ", ".join(e.tasks)) for e in covered]
    lines += [
        "",
        "## Open, covered by no task row",
        "",
        "| Entry | Title | Task rows | Notes |",
        "| --- | --- | --- | --- |",
    ]
    lines += [row(e, "") for e in bare]
    return "\n".join(lines) + "\n"


def row(e, tasks):
    """One table row. Nothing is cut to a length, so rewriting a placeholder to its id changes only that token."""
    title = e.title.replace("|", "\\|")
    notes = ["open by its " + e.reason.split(":")[0] if ":" in e.reason else e.reason]
    if e.partial:
        notes.append("partly closed by " + ", ".join(e.partial))
    if e.done_tasks:
        notes.append("named by done " + ", ".join(e.done_tasks))
    return f"| {e.id} | {title} | {tasks} | {'; '.join(notes)} |"


def read_tree(root=ROOT):
    inv = (root / INVENTORY).read_text(encoding="utf-8")
    d = root / PENDING_DIR
    pending = {p.stem: p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))} if d.is_dir() else {}
    tasks = (root / TASKS).read_text(encoding="utf-8")
    done = (root / TASKS_DONE).read_text(encoding="utf-8")
    return derive(inv, pending, tasks, done)


def describe(e):
    out = f"{e.id}  {e.status}"
    if e.status == "closed":
        out += f" ({e.kind}, by {e.by})"
    out += f"  [{e.reason}]"
    if e.partial:
        out += f"  partly closed by {', '.join(e.partial)}"
    if e.tasks:
        out += f"  tasks {', '.join(e.tasks)}"
    if e.done_tasks:
        out += f"  done tasks {', '.join(e.done_tasks)}"
    return out + f"\n    {e.title[:120]}"


def self_test():
    N = "BUG-" + "NEW-"  # built, so that this file cites no placeholder
    inv = "\n".join([
        "# Bug inventory", "", "---", "",
        "## BUG-0001 — fixed in place", "", "- **Fix:** the line now reads x.", "", "---", "",
        "## BUG-0002 — no fix field", "", "- **Symptom:** s", "", "---", "",
        "## BUG-0003 — open fix", "", "- **Fix:** open; next batch (T-010).", "", "---", "",
        "## BUG-0004 — status open", "", "- **Status:** open, T-011.", "- **Fix sketch:** do x", "", "---", "",
        "## BUG-0005 — disposition to a task", "", "- **Disposition:** T-012, with the next pass.", "",
        "## BUG-0006 — status fixed", "", "- **Status:** fixed (abc123).", "",
        "## BUG-0007 — proposal only", "", "- **Proposed fix:** do y", "",
        "## BUG-0008 — BUG-0002 is fixed: the line reads y", "", "- **Fix:** z", "",
        "## BUG-0009 — BUG-0003 is mostly fixed: most of it", "", "- **Fix:** z", "",
        "## BUG-0010 — later closer", "", "- **Fix:** z", "- **Closes:** BUG-0004, BUG-0005 (owner's decision).", "",
        "## BUG-0011 — part closer", "", "- **Fix:** z",
        "- **Closes:** BUG-0007, the `a.b` part; the `a.c` part stays open", "",
        "## BUG-0012 — names a later entry", "", "- **Closes:** BUG-0014 in part", "- **Closure:** fixed", "",
        "## BUG-0013 — Fix for BUG-0013: itself", "", "- **Fix:** z", "",
        "## BUG-0014 — either fix", "", "- **Fix:** Either do a or b.", "",
        "## BUG-0015 — range closer", "", "- **Wording fix:** w", "",
        "## BUG-0016 — open a", "", "- **Symptom:** s", "",
        "## BUG-0017 — open b", "", "- **Symptom:** s", "",
        "## BUG-0018 — open c", "", "- **Symptom:** s", "",
        "## BUG-0019 — BUG-0016 to BUG-0018 are fixed: a range", "", "- **Fix:** z", "",
        "## BUG-0020 — The BUG-0014 lows are fixed for asset", "", "- **Fix:** z", "",
        "## BUG-0021 — dup", "", "- **Duplicate of:** BUG-0014 (the same).", "",
        "## BUG-0022 — reopened", "", "- **Reopens:** BUG-0016", "- **Symptom:** the range closure was wrong", "",
        "## BUG-0023 — Disposition of BUG-0014", "", "- **Fix:** recorded as a limit.", "",
        "## BUG-0024 — open d", "", "- **Symptom:** s", "",
        "## BUG-0025 — Disposition of BUG-0002 and BUG-0024", "",
        "- **Closes:** BUG-0002 (fixed with x) and BUG-0024 (fixed with y).", "- **Tags:** disposition", "",
        "## BUG-0026 — names no entry", "", "- **Closes:** BUG-0099", "- **Closure:** fixed", "",
    ]) + "\n"
    pending = {
        "lane-2": f"## {N}lane-2 — open pending\n\n- **Fix:** Not fixed (no tool).\n",
        "lane-10": f"## {N}lane-10 — closure of a pending one\n\n- **Closes:** {N}lane-2\n- **Closure:** won't fix\n"
                   "- **Evidence:** e\n",
        "lane-11": f"## {N}lane-11 — bad closure\n\n- **Closes:** see BUG-0003\n- **Closure:** maybe\n",
        "lane-3": f"## {N}lane-3 — a long open title that cites {N}lane-2 and runs on past any column width a table "
                  "might want to cut it at, so that a cut would move\n\n- **Status:** open, see {N}lane-2 and T-020.\n",
    }
    tasks = "| T-010 | do BUG-0003 | src | due | open |\n| T-011 | x | s | d | open |\n| T-020 | BUG-0017 | s | d | open |\n"
    done = "| T-012 | did BUG-0005 | s | d | done |\n| T-013 | BUG-0007/0016 | s | d | done |\n"
    entries, problems = derive(inv, pending, tasks, done)
    st = {e.id: e for e in entries}
    want = {
        "BUG-0001": ("fixed", None), "BUG-0002": ("closed", "BUG-0008"), "BUG-0003": ("open", None),
        "BUG-0004": ("closed", "BUG-0010"), "BUG-0005": ("closed", "BUG-0010"), "BUG-0006": ("fixed", None),
        "BUG-0007": ("open", None), "BUG-0012": ("record", None), "BUG-0013": ("fixed", None),
        "BUG-0014": ("closed", "BUG-0023"), "BUG-0015": ("fixed", None), "BUG-0016": ("open", None),
        "BUG-0017": ("closed", "BUG-0019"), "BUG-0018": ("closed", "BUG-0019"), "BUG-0021": ("closed", "BUG-0014"),
        "BUG-0024": ("closed", "BUG-0025"), "BUG-0025": ("record", None),
        f"{N}lane-2": ("closed", f"{N}lane-10"), f"{N}lane-10": ("record", None),
    }
    bad = []
    for ident, (status, by) in want.items():
        e = st[ident]
        if (e.status, e.by) != (status, by):
            bad.append(f"{ident}: got {e.status} by {e.by}, want {status} by {by}")
    checks = [
        (st["BUG-0003"].partial == ["BUG-0009"], "BUG-0003 partly closed by BUG-0009"),
        (st["BUG-0007"].partial == ["BUG-0011"], "BUG-0007 partly closed by BUG-0011"),
        (st["BUG-0014"].partial == ["BUG-0012", "BUG-0020"],
         "BUG-0014 partly closed by BUG-0012 (an earlier entry) and BUG-0020 ('is fixed for')"),
        (st["BUG-0014"].kind == "disposed", "a Disposition-of title closes as disposed"),
        (st[f"{N}lane-2"].kind == "won't fix", "the Closure field gives the kind"),
        (st["BUG-0024"].kind == "disposed" and st["BUG-0024"].reason == "closed by BUG-0025 (title)",
         "a title closure adds the ids a Closes field names past its leading list"),
        (st["BUG-0003"].tasks == ["T-010"], "a task row naming the entry and its own fix's task id cover it"),
        (st["BUG-0016"].reason == "reopened by BUG-0022" and st["BUG-0016"].done_tasks == ["T-013"],
         "a Reopens field reopens; a done row's 'BUG-0007/0016' names both"),
        (st["BUG-0007"].done_tasks == ["T-013"], "done rows are hints"),
        (pending and [e.id for e in entries][-4:] == [f"{N}lane-2", f"{N}lane-3", f"{N}lane-10", f"{N}lane-11"],
         "pending entries follow in --assign's order"),
        (any("BUG-0013: its title names the entry itself" in p for p in problems), "a closure of itself is refused"),
        (any("BUG-0026: its Closes field names BUG-0099, which is no entry" in p for p in problems),
         "a closure of no entry is refused"),
        (any(f"{N}lane-11: its Closes field does not begin" in p for p in problems), "a Closes field needs an id"),
        (any(f"{N}lane-11: Closure 'maybe'" in p for p in problems), "an unknown closure kind is refused"),
        (len(problems) == 4, f"exactly the four planted problems: {problems}"),
        (st["BUG-0013"].status == "fixed", "a refused closure leaves its entry's own status"),
        (expand("BUG-0500, BUG-0522 to BUG-0524 and BUG-0530") ==
         ["BUG-0500", "BUG-0522", "BUG-0523", "BUG-0524", "BUG-0530"], "ranges expand"),
    ]
    bad += [label for ok, label in checks if not ok]
    text = report(entries)
    if "| BUG-0003 | open fix | T-010 |" not in text or f"| {N}lane-3 |" not in text:
        bad.append("report rows")
    # Assigning ids (new_bug.py --assign, which rewrites placeholders in tracked files) keeps the report current.
    numbered = inv + "".join("\n" + pending[n] for n in sorted(pending, key=natural_key))
    mapping = {f"{N}{n}": f"BUG-{27 + k:04d}" for k, n in enumerate(sorted(pending, key=natural_key))}
    for old, new in sorted(mapping.items(), key=lambda kv: -len(kv[0])):
        numbered = numbered.replace(old, new)
    rewritten = text
    for old, new in sorted(mapping.items(), key=lambda kv: -len(kv[0])):
        rewritten = rewritten.replace(old, new)
    after, _ = derive(numbered, {}, tasks, done)
    if report(after) != rewritten:
        bad.append("assigning ids makes the report stale")
    print("bug status self-test: " + ("ok" if not bad else "FAILED: " + "; ".join(bad)))
    return 1 if bad else 0


def main(argv):
    if argv[:1] == ["--self-test"]:
        return self_test()
    entries, problems = read_tree()
    if argv[:1] == ["--check"]:
        path = ROOT / REPORT
        want = report(entries)
        if not path.exists() or path.read_text(encoding="utf-8") != want:
            problems.append(f"{REPORT} is not current: run python3 tools/bug_status.py --write")
        for p in problems:
            print(f"bug_status: {p}", file=sys.stderr)
        if problems:
            return 1
        n_open = sum(e.status == "open" for e in entries)
        print(f"bug status OK ({len(entries)} entries, {n_open} open; {REPORT} current)")
        return 0
    for p in problems:
        print(f"bug_status: {p}", file=sys.stderr)
    if argv[:1] == ["--write"]:
        (ROOT / REPORT).write_text(report(entries), encoding="utf-8")
        print(f"wrote {REPORT}")
        return 1 if problems else 0
    if argv[:1] == ["--open"]:
        for e in entries:
            if e.status == "open":
                print(f"{e.id}\t{','.join(e.tasks) or '-'}\t{e.title[:100]}")
        return 0
    if argv:
        by_id = {e.id: e for e in entries}
        for a in argv:
            print(describe(by_id[a]) if a in by_id else f"{a}: no such entry")
        return 0
    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1
    print(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
