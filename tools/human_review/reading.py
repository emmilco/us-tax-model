# SPDX-License-Identifier: Apache-2.0
"""Reading English for the packets: what a line computes, said in page terms.

Built from the canonical JSON (canonical/<year>/*.json), one literal template per atom.
Printed lines are named "line N of <form> (“IRS label”)", inputs by their interview
question, parameters by their amount and name; a helper is never named: it is expanded
in place, or, when its expression is compound, given a letter tag "(a)" whose definition
follows under the sentence that uses it. The result of `expand` is a tree of nodes
(text, children) that packet.py renders as nested lists and serve.py flattens for the log.

Also decides what is printed: a line whose `printed` is none of the helper markers.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

CANON = ROOT / "canonical" / Y
NOT_PRINTED = {"(helper)", "(gate)", "(computed helper)", "(screen)", "(question)"}
STATUS_WORDS = {"single": "single", "mfj": "married filing jointly", "mfs": "married filing separately",
                "hoh": "head of household", "qss": "qualifying surviving spouse"}
COMPARE = {"eq": "equals", "ne": "is not", "lt": "is less than", "le": "is at most",
           "gt": "is greater than", "ge": "is at least"}


def without_snapshot(obj):
    if isinstance(obj, dict):
        return {k: ({ck: without_snapshot(cv) for ck, cv in v.items()
                     if ck not in ("snapshot", "revision", "tax_year")} if k == "cite" else without_snapshot(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [without_snapshot(x) for x in obj]
    return obj


def dollars(cents):
    neg = cents < 0
    s = f"${abs(cents) / 100:,.2f}"
    return "-" + s if neg else s


def rate_text(r):
    if isinstance(r, dict) and "num" in r:
        num, den = r["num"], r["den"]
        if den and (10000 * num) % den == 0:
            pct = 100 * num / den
            return f"{pct:g}%"
        return f"{num}/{den}"
    return str(r)


class Node:
    def __init__(self, text, kids=None):
        self.text, self.kids = text, kids or []

    def flat(self):
        """The tree as one line, for the log."""
        out = self.text
        if self.kids:
            out += " [" + " | ".join(k.flat() for k in self.kids) + "]"
        return out


class Canon:
    """The canonical data of the year: lines by id, parameters, question prompts."""

    def __init__(self):
        if not (CANON / "params.json").exists():
            subprocess.run(["node", str(ROOT / "engine" / "dist" / "main.js"), "build"], check=True, cwd=ROOT)
        self.docs, self.lines, self.form_of = {}, {}, {}
        self.prompts, self.frames = {}, {}
        for p in sorted(CANON.glob("*.json")):
            d = json.loads(p.read_text(encoding="utf-8"))
            top = d.get("form") or d.get("def")
            if top:
                source = yaml.safe_load((ROOT / "forms" / Y / f"{top['id']}.yaml").read_text(encoding="utf-8"))
                if without_snapshot(source) != without_snapshot(d):
                    raise ValueError(f"canonical data for {top['id']} is stale; run npm run build before opening a packet")
                self.docs[top["id"]] = top
                for l in top["lines"]:
                    self.lines[l["id"]] = l
                    self.form_of[l["id"]] = top["id"]
            elif "questions" in d:
                for q in d["questions"]:
                    if q.get("prompt") and q["input"] not in self.prompts:
                        self.prompts[q["input"]] = q["prompt"]
        self.params = json.loads((CANON / "params.json").read_text(encoding="utf-8"))["params"]
        source_params = yaml.safe_load((ROOT / "params" / f"{Y}.yaml").read_text(encoding="utf-8"))["params"]
        if without_snapshot(source_params) != without_snapshot(self.params):
            raise ValueError("canonical parameters are stale; run npm run build before opening a packet")
        bank = yaml.safe_load((ROOT / "interview" / f"questions-{Y}.yaml").read_text(encoding="utf-8"))
        self.frames = (bank.get("bank") or {}).get("frames", {})
        self.readers = {}
        for lid, l in self.lines.items():
            for r in refs_in(l.get("expr")):
                r = self.resolve(r, self.form_of[lid])
                if r:
                    self.readers.setdefault(r, []).append(lid)

    def resolve(self, ref, within=None):
        """A line id as written in `within` (a def's bare id, or any qualified id), or None."""
        if isinstance(ref, dict):
            return self.resolve(ref.get("line"), ref.get("def"))
        if ref in self.lines:
            return ref
        if within and f"{within}.{ref}" in self.lines:
            return f"{within}.{ref}"
        return None

    def line(self, lid):
        return self.lines[lid]

    def form_name(self, fid):
        """The form as the reader knows it: the title up to its dash."""
        title = self.docs[fid]["title"]
        return re.split(r"\s+[—–-]\s+|—", title)[0].strip()

    def is_printed(self, lid):
        return str(self.lines[lid].get("printed", "")) not in NOT_PRINTED

    def is_input(self, lid):
        return self.lines[lid]["expr"].get("op") == "input"

    def is_param(self, lid):
        return self.lines[lid]["expr"].get("op") == "param"

    def is_leaf(self, lid):
        return self.is_printed(lid) or self.is_input(lid) or self.is_param(lid)

    def kind(self, lid):
        if self.is_printed(lid):
            return "printed"
        if self.is_input(lid):
            return "input"
        if self.is_param(lid):
            return "param"
        return "helper"

    def question(self, lid, bare=False):
        """The interview wording of an input line; `bare` drops the collection's frame
        ("For this person — ") when the sentence already says which entries are meant."""
        l = self.lines[lid]
        frame = self.frames.get(self.form_of[lid], "")
        text = self.prompts.get(lid) or frame + l["expr"].get("source", l.get("label", lid))
        if bare and frame and text.startswith(frame):
            text = text[len(frame):]
        return text

    def collection_gloss(self, coll):
        """The parenthetical of the collection's interview frame: "you, or your spouse on a joint return"."""
        frame = self.frames.get(coll, "")
        m = re.search(r"\(([^)]*)\)", frame)
        return m.group(1) if m else coll

    def param_text(self, name):
        p = self.params["values"].get(name)
        if p is None:
            return f"parameter {name}"
        v = p["value"]
        t = p.get("type", "")
        if isinstance(v, dict) and "num" in v:
            return rate_text(v)
        if isinstance(v, dict):
            groups = {}
            for status in list(STATUS_WORDS) + sorted(set(v) - set(STATUS_WORDS)):
                if status in v:
                    groups.setdefault(v[status], []).append(STATUS_WORDS.get(status, status))
            parts = [f"{self.amount_text(a, t)} if {' or '.join(s)}" for a, s in groups.items()]
            return "the amount for your filing status (" + "; ".join(parts) + ")"
        return self.amount_text(v, t)

    @staticmethod
    def amount_text(v, t):
        if "Dollars" in t:
            return dollars(v)
        if t == "Rate":
            return rate_text(v)
        return str(v)

    def plain_label(self, lid):
        """A label with line ids turned into words: `sa.line4` is "line 4"."""
        label = str(self.lines[lid].get("label", ""))
        label = re.sub(r"\b[a-z0-9_]+\.line(\d+[a-z]?)\b", r"line \1", label)
        return label

    def line_name(self, lid):
        """How the reading names a printed line."""
        l = self.lines[lid]
        form = self.form_name(self.form_of[lid])
        printed = str(l.get("printed", ""))
        label = self.plain_label(lid)
        if re.match(r"^\d", printed):
            where = f"line {printed} of {form}"
        elif re.match(r"^\(?[a-z]\)?$", printed):
            where = f"column {printed.strip('()')} of {form}"
        else:
            where = f"{form}, {printed.strip('()')}"
        return f"{where} (“{label}”)" if label else where


def refs_in(expr):
    """Every line reference inside an expression, as written."""
    out = []

    def walk(e):
        if isinstance(e, dict):
            if "def" in e and "line" in e:
                out.append(e)
                for v in e.get("bind", {}).values():
                    walk(v)
                return
            for k, v in e.items():
                if k in ("op", "const", "param", "table", "unit", "rule", "places", "collection", "source", "name"):
                    continue
                walk(v)
        elif isinstance(e, list):
            for v in e:
                walk(v)
        elif isinstance(e, str):
            out.append(e)
    walk(expr)
    return out


class Reading:
    """The reading of one printed line: the tree, the helpers folded, the leaves reached."""

    def __init__(self, canon, lid, tag_style="a", stop_at=None):
        self.c = canon
        self.root = lid
        self.stop_at = stop_at or {}
        self.tag_style = tag_style
        self.tags = {}        # helper id -> "(a)"
        self.defs = []        # (tag, helper id, Node), in tag order
        self.leaves = []      # printed / input / param ids reached, in order
        self.helpers = []     # helper ids folded, in order
        self.stack = []
        self.coll = None      # the collection whose entries a sum_over is ranging over
        # a printed line that only copies a helper is read as that helper
        start = lid
        while self.c.lines[start]["expr"].get("op") == "copy":
            nxt = self.c.resolve(self.c.lines[start]["expr"]["from"], self.c.form_of[start])
            if nxt is None or self.c.is_leaf(nxt) or nxt in self.stop_at:
                break
            self._seen(nxt)
            start = nxt
        self.node = self.sentence(start, top=True)

    # -- naming --

    def _seen(self, lid):
        if lid not in self.leaves and lid not in self.helpers:
            (self.helpers if self.c.kind(lid) == "helper" else self.leaves).append(lid)

    def ref(self, r, within):
        """A line reference as an inline phrase (a compound helper becomes its tag)."""
        bound = ""
        if isinstance(r, dict):
            binds = ", ".join(f"{k} = {self.operand(v, within)}" for k, v in r.get("bind", {}).items())
            bound = f" with {binds}" if binds else ""
        lid = self.c.resolve(r, within)
        if lid is None:
            return f"`{r}`"
        if lid in self.stop_at and lid != self.root:
            if lid not in self.leaves:
                self.leaves.append(lid)
            return self.stop_at[lid] + bound
        self._seen(lid)
        k = self.c.kind(lid)
        if k == "printed":
            return self.c.line_name(lid) + bound
        if k == "input":
            return f"your answer to “{self.c.question(lid, bare=self.c.form_of[lid] == self.coll)}”"
        if k == "param":
            return self.c.param_text(self.c.lines[lid]["expr"]["ref"])
        l = self.c.lines[lid]
        op = l["expr"].get("op")
        if op == "copy" or (op == "param"):
            return self.ref(l["expr"]["from"] if op == "copy" else lid, self.c.form_of[lid]) + bound
        if lid in self.tags:
            return self.tags[lid] + bound
        if lid in self.stack:
            return f"(this same amount, {lid}, read again)"
        tag = f"({chr(ord(self.tag_style) + len(self.tags))})"
        self.tags[lid] = tag
        node = self.sentence(lid)
        hint = self.hint(lid)
        node.text = f"{tag} {hint + ': ' if hint else ''}{node.text}"
        self.defs.append((tag, lid, node))
        return tag + bound

    def hint(self, lid):
        label = str(self.c.lines[lid].get("label", ""))
        if re.search(r"\b[a-z0-9_]+\.[a-z0-9_]+", label) or len(label) > 90 or label.startswith("Year parameter"):
            return ""
        return label.rstrip("?.")

    def operand(self, o, within):
        if isinstance(o, dict) and "const" in o:
            v = o["const"]
            if isinstance(v, bool):
                return "yes" if v else "no"
            if isinstance(v, str):
                return STATUS_WORDS.get(v, v)
            if o.get("type") == "Count":
                return str(v)
            return dollars(v) if isinstance(v, int) and abs(v) >= 100 else str(v)
        if isinstance(o, dict) and "param" in o:
            return self.c.param_text(o["param"])
        return self.ref(o, within)

    # -- templates, one per atom --

    def sentence(self, lid, top=False):
        """A node whose text says what `lid` computes, with definitions of its tagged helpers as kids."""
        self.stack.append(lid)
        before = len(self.defs)
        l = self.c.lines[lid]
        within = self.c.form_of[lid]
        expr = l["expr"]
        branches = []
        if expr.get("op") == "choose":
            alts = expr["alternatives"]
            if len(alts) == 2 and complementary(alts[0]["guard"], alts[1]["guard"]):
                condition = self.condition_node(alts[0]["guard"], within)
                branches = [Node(f"Use {self.ref(alts[0]['then'], within)} when:", [condition]),
                            Node(f"Otherwise, use {self.ref(alts[1]['then'], within)}.")]
            else:
                branches = [Node(f"Use {self.ref(a['then'], within)} when:",
                                 [self.condition_node(a["guard"], within)]) for a in alts]
                branches.append(Node("If no condition applies, this line is unknown."))
            text = "Choose the amount as follows:"
        else:
            text = self.atom(expr, within, l)
        kids = [n for _, _, n in self.defs[before:]]
        del self.defs[before:]
        self.stack.pop()
        return Node(text, branches + kids)

    def condition_node(self, test, within):
        for key, text in (("all", "All of the following are true:"), ("any", "At least one of the following is true:")):
            if key in test:
                return Node(text, [self.condition_node(t, within) for t in test[key]])
        if "not" in test:
            return Node("The following is false:", [self.condition_node(test["not"], within)])
        for key in ("eq", "ne"):
            if key in test:
                a, b = test[key]
                if isinstance(b, dict) and isinstance(b.get("const"), bool) and isinstance(a, str):
                    lid = self.c.resolve(a, within)
                    if lid and lid not in self.stop_at and not self.c.is_leaf(lid) and self.c.lines[lid]["expr"].get("op") == "test":
                        self._seen(lid)
                        nested = self.condition_node(self.c.lines[lid]["expr"], self.c.form_of[lid])
                        return nested if b["const"] == (key == "eq") else Node("The following is false:", [nested])
        return Node(self.test(test, within))

    def atom(self, e, w, line=None):
        op = e.get("op")
        P = lambda r: self.ref(r, w)  # noqa: E731
        O = lambda o: self.operand(o, w)  # noqa: E731
        if op == "input":
            return f"your answer to “{self.c.question(line['id'])}”" if line else f"an answer to “{e['source']}”"
        if op == "param":
            return self.c.param_text(e["ref"])
        if op == "copy":
            return P(e["from"])
        if op == "sum":
            return "the sum of " + join_and([P(r) for r in e["of"]])
        if op == "subtract":
            return f"{P(e['from'])} minus {O(e['take'])}"
        if op == "subtract_floor0":
            return f"{P(e['from'])} minus {O(e['take'])}, but not less than zero"
        if op == "smaller_of":
            items = [P(r) for r in e["of"]]
            return ("the smaller of " if len(items) == 2 else "the smallest of ") + join_and(items)
        if op == "larger_of":
            items = [P(r) for r in e["of"]]
            return ("the larger of " if len(items) == 2 else "the largest of ") + join_and(items)
        if op == "multiply_rate":
            return f"{P(e['amount'])} times {O(e['rate'])}"
        if op == "multiply_count":
            return f"{P(e['amount'])} times {P(e['count'])}"
        if op == "round":
            unit = e.get("unit", 1)
            return f"{P(e['of'])} rounded {e.get('rule', '')} to the nearest {dollars(unit) if unit >= 100 else unit}"
        if op == "prorate":
            return (f"{P(e['amount'])} times ({P(e['part'])} divided by {O(e['whole'])}, as a decimal rounded to "
                    f"{e.get('places')} places)")
        if op == "table_lookup":
            return f"the amount in the {e['table']} table at {P(e['key'])}, in the column for {P(e['status'])}"
        if op == "bracket_schedule":
            return f"the tax on {P(e['key'])} from the {e['table']} schedule for {P(e['status'])}"
        if op == "keyed_lookup":
            return f"the value in the {e['table']} table for " + join_and([P(k) for k in e["keys"]])
        if op == "rate_lookup":
            s = f" and {P(e['status'])}" if e.get("status") else ""
            return f"the rate in the {e['table']} table for {P(e['key'])}{s}"
        if op == "sum_over":
            coll = self.c.collection_gloss(e["collection"])
            field = self.c.resolve(e["field"], w)
            fx = self.c.lines[field]["expr"] if field else {}
            count = fx.get("op") == "param" and self.c.params["values"].get(fx["ref"], {}).get("value") == 1
            outer, self.coll = self.coll, e["collection"]
            cond = f" for which {self.test(e['where'], w)}" if e.get("where") else ""
            body = P(e["field"]) if not count else ""
            self.coll = outer
            if count:
                self._seen(field)
                return f"the number of {e['collection']} entries ({coll}){cond}"
            return f"the sum over every {e['collection']} entry ({coll}) of {body}{cond}"
        if op == "choose":
            alts = e["alternatives"]
            if len(alts) == 2 and complementary(alts[0]["guard"], alts[1]["guard"]):
                return f"if {self.test(alts[0]['guard'], w)}, then {P(alts[0]['then'])}; otherwise {P(alts[1]['then'])}"
            parts = [f"if {self.test(a['guard'], w)}, then {P(a['then'])}" for a in alts]
            return "; otherwise, ".join(parts) + "; otherwise no alternative applies and the line is unknown"
        if op == "test":
            return "yes when " + self.test(e, w) + ", otherwise no"
        if op == "opaque":
            return f"an opaque computation named {e.get('name')}"
        return f"an expression of kind {op} (no template)"

    def test(self, t, w, nested=False):
        """A condition as a clause; a compound inside another is parenthesized."""
        O = lambda o: self.operand(o, w)  # noqa: E731
        for key, word, head in (("all", "and", "all of these hold"), ("any", "or", "any of these holds")):
            if key in t:
                parts = [self.test(x, w, nested=True) for x in t[key]]
                if len(parts) == 2:
                    text = f" {word} ".join(parts)
                else:
                    text = f"{head}: " + ", ".join(f"({i + 1}) {p}" for i, p in enumerate(parts))
                return f"({text})" if nested else text
        if "not" in t:
            return "it is not the case that " + self.test(t["not"], w, nested=True)
        for k, word in COMPARE.items():
            if k in t:
                a, b = t[k]
                if k in ("eq", "ne") and isinstance(b, dict) and isinstance(b.get("const"), bool):
                    want = b["const"] if k == "eq" else not b["const"]
                    return self.condition(a, w, want)
                if k == "eq" and isinstance(b, dict) and isinstance(b.get("const"), str):
                    return f"{self.status_phrase(a, w)} is {O(b)}"
                return f"{O(a)} {word} {O(b)}"
        return "a condition with no template"

    def status_phrase(self, a, w):
        lid = self.c.resolve(a, w) if isinstance(a, str) else None
        if lid and self.c.is_printed(lid):
            self._seen(lid)
            return "your " + str(self.c.lines[lid].get("printed", "")).lower() + f" ({self.c.form_name(self.c.form_of[lid])})"
        return self.operand(a, w)

    def condition(self, a, w, want):
        """A Bool operand asserted (want=True) or denied."""
        lid = self.c.resolve(a, w) if isinstance(a, str) else None
        if lid in self.stop_at:
            return f"{self.ref(a, w)} is {'yes' if want else 'no'}"
        if lid and self.c.is_input(lid):
            self._seen(lid)
            q = self.c.question(lid, bare=self.c.form_of[lid] == self.coll)
            return f"you answered {'yes' if want else 'no'} to “{q}”"
        if lid and not self.c.is_leaf(lid):
            l = self.c.lines[lid]
            if l["expr"].get("op") == "test" and lid not in self.tags and lid not in self.stack:
                self.stack.append(lid)
                self._seen(lid)
                clause = self.test(l["expr"], self.c.form_of[lid], nested=True)
                self.stack.pop()
                return clause if want else f"it is not the case that {clause}"
        phrase = self.operand(a, w)
        return f"{phrase} is {'yes' if want else 'no'}"

    # -- the whole line --

    def closure(self):
        """Every line the reading reaches: the helpers folded and the leaves named."""
        return set(self.helpers) | set(self.leaves)


def complementary(g1, g2):
    """Two guards that are the same operand tested true and false."""
    for k in ("eq",):
        if k in g1 and k in g2 and g1[k][0] == g2[k][0]:
            a, b = g1[k][1], g2[k][1]
            if isinstance(a, dict) and isinstance(b, dict) and isinstance(a.get("const"), bool) \
                    and isinstance(b.get("const"), bool) and a["const"] != b["const"]:
                return True
    return False


def join_and(items):
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def refusals(canon, reading):
    """(where, Node, remedy, cite) for the refusal gates on the printed line and its folded helpers;
    the node's text is the sentence, its kids the definitions of the gate's tagged helpers."""
    out = []
    for lid in [reading.root] + reading.helpers:
        for r in canon.lines[lid].get("refuses", []):
            gate = canon.resolve(r["when"], canon.form_of[lid])
            kids = []
            if gate and canon.is_input(gate):
                wording = f"you answer yes to “{canon.question(gate)}”"
            elif gate:
                sub = Reading(canon, gate, tag_style="A")
                wording = sub.node.text
                if wording.startswith("yes when "):
                    wording = wording[len("yes when "):]
                    if wording.endswith(", otherwise no"):
                        wording = wording[:-len(", otherwise no")]
                if sub.node.kids or len(wording) > 400:
                    # a gate with helpers of its own is a line in its own right; name it, do not unfold it
                    wording = f"“{canon.lines[gate].get('label', gate)}” holds (gate {gate}, a computed condition read as its own line)"
                else:
                    wording += f" (gate {gate})"
            else:
                wording = r["when"]
            where = "This line" if lid == reading.root else f"Its folded helper {lid}"
            out.append((where, Node(f"{where} is refused when {wording}.", kids), r.get("remedy", ""), r.get("cite", {})))
    return out


def printed_readers(canon, lid):
    """The nearest printed lines that read `lid`, directly or through helpers (breadth first)."""
    seen, frontier, found = {lid}, [lid], []
    while frontier and not found:
        nxt = []
        for x in frontier:
            for r in canon.readers.get(x, []):
                if r in seen:
                    continue
                seen.add(r)
                if canon.is_printed(r):
                    found.append(r)
                else:
                    nxt.append(r)
        frontier = nxt
    return sorted(found)


def plan(canon, refs, docs=()):
    """What the packet judges for a reading-list item: the printed lines listed, plus, for a
    listed helper none of them reads, the nearest printed line that reads it, chosen by (1) how
    many of the item's lines its reading covers, (2) whether its own citation is in one of the
    item's documents `docs`, (3) how few lines outside the item it drags in; then the listed
    helpers no chosen printed line reads. Returns ([(printed id, Reading, how reached)], orphans)."""
    listed = []
    for r in refs:
        lid = canon.resolve(r) or canon.resolve(r.partition(".")[2], r.partition(".")[0])
        if lid:
            listed.append(lid)
    printed = [l for l in listed if canon.is_printed(l)]
    readings = {p: Reading(canon, p) for p in printed}
    reached = {p: "listed" for p in printed}
    cache = {}

    def covered():
        return set(readings) | (set().union(*(rd.closure() for rd in readings.values())) if readings else set())
    for h in listed:
        if h in covered():
            continue
        best = None
        for p in printed_readers(canon, h):
            rd = cache.setdefault(p, Reading(canon, p))
            reach = rd.closure() | {p}
            key = (-len(reach & set(listed)), 0 if canon.lines[p].get("cite", {}).get("doc") in docs else 1,
                   len(reach - set(listed)), p)
            if best is None or key < best[0]:
                best = (key, p, rd)
        if best:
            _, p, rd = best
            readings[p] = rd
            reached[p] = f"reached from the listed helper {h}"
    done = covered()
    orphans = [h for h in listed if not canon.is_printed(h) and h not in done]
    return [(p, readings[p], reached[p]) for p in readings], orphans
