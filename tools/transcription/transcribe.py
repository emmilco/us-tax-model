#!/usr/bin/env python3
"""Second, isolated transcription of a worksheet, compared structurally with the data.

For one form: cut the cited pages from the archived IRS text, hand them with the
data model to a language model that sees nothing else (print mode, no tools, no
settings, no project files), parse the YAML it returns, expand every printed
line of both transcriptions into a tree over inputs, parameters and cross-form
references, and write a log with every agreement and disagreement. Rulings on
disagreements are written into the log by a person reading the source page;
nothing here writes to forms/.

Usage: transcribe.py --form qdcg [--model claude-opus-5-5] [--dry-run]
"""
import argparse, datetime, hashlib, json, os, re, subprocess, sys
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rulings  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCES = os.path.join(ROOT, "sources", "2025")
FORMS = os.path.join(ROOT, "forms", "2025")
LOGS = os.path.join(ROOT, "reviews", "2025", "transcription")
RAW = os.path.join(ROOT, ".transcription")
WHOLE_DOC_MAX_PAGES = 6
HELPER_PRINTED = {"(helper)", "(gate)", "(computed helper)"}


# ---------- sources ----------

def manifest():
    m = json.load(open(os.path.join(SOURCES, "manifest.json")))
    docs = m["documents"] if isinstance(m, dict) else m
    return {d["id"]: d for d in docs}


def doc_pages(doc, key="text_file"):
    text = open(os.path.join(SOURCES, doc[key]), encoding="utf-8").read()
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def page_kinds(doc):
    """The per-page classification of the reading-order extraction, or None."""
    if "pages_file" not in doc:
        return None
    return json.load(open(os.path.join(SOURCES, doc["pages_file"]), encoding="utf-8"))["pages"]


def locator_pages(locator):
    """Page numbers named in a locator such as 'pp. 34–35, line 12e' or 'p. 11, ...'."""
    out = set()
    for m in re.finditer(r"\bpp?\.\s*([0-9][0-9,\s–—-]*)", locator):
        for part in re.split(r",\s*", m.group(1).strip()):
            part = part.strip()
            r = re.match(r"^(\d+)\s*[–—-]\s*(\d+)$", part)
            if r:
                out.update(range(int(r.group(1)), int(r.group(2)) + 1))
            elif part.isdigit():
                out.add(int(part))
    return out


WORKSHEETS = {
    "Tax Computation Worksheet": ("TCW",),
    "Qualified Dividends and Capital Gain Tax Worksheet": ("QDCGT", "QDCG"),
    "Schedule D Tax Worksheet": ("SDTW",),
    "28% Rate Gain Worksheet": (),
    "Unrecaptured Section 1250 Gain Worksheet": (),
    "Standard Deduction Chart": (),
    "State and Local Tax Deduction Worksheet": (),
    "Capital Loss Carryover Worksheet": (),
}


def heading_pages(pages, locator):
    """Pages carrying the heading a locator names: a worksheet whose title starts a
    line (optionally prefixed by the year), or otherwise an instruction heading 'Line N'."""
    found = set()
    low = locator.lower()
    for phrase, abbrs in WORKSHEETS.items():
        if phrase.lower() in low or any(re.search(r"\b" + a + r"\b", locator) for a in abbrs):
            pat = re.compile(r"(?m)^\s*(?:\d{4}\s+)?" + re.escape(phrase) + r"(?:\u2014|-|\s{2,}|$)")
            found.update(i + 1 for i, p in enumerate(pages) if pat.search(p))
    if found:
        return found
    m = re.search(r"\bline\s+(\d+[a-z]?)\b", locator, re.I)
    if m:
        pat = re.compile(r"(?m)^\s*Line\s+" + re.escape(m.group(1)) + r"\b")
        found.update(i + 1 for i, p in enumerate(pages) if pat.search(p))
    return found


def secondary_pages(locator, mani, primary):
    """Pages of other archived documents a locator names inline, such as
    'i8995 pp. 3-4' in a form citation; returns {doc_id: pages} and the locator
    with those mentions removed so they are not read as pages of the primary document."""
    out = {}
    def take(m):
        doc_id = m.group(1)
        if doc_id in mani and doc_id != primary:
            out.setdefault(doc_id, set()).update(locator_pages(m.group(0)))
            return ""
        return m.group(0)
    rest = re.sub(r"\b([a-z][a-z0-9]*)\s+(pp?\.\s*[0-9][0-9,\s\u2013\u2014-]*)", take, locator)
    return out, rest


def param_cites(form_doc):
    """Citations of the year parameters a form's lines reference."""
    names = set()
    for line in form_doc["lines"]:
        text = json.dumps(line.get("expr", {}))
        names.update(re.findall(r'"param": "([a-z0-9_.]+)"', text))
        if line.get("expr", {}).get("op") == "param":
            names.add(line["expr"]["ref"])
    params_doc = yaml.safe_load(open(os.path.join(ROOT, "params", "2025.yaml"), encoding="utf-8"))
    values = (params_doc.get("params") or params_doc)["values"]
    # Structural constants (a zero amount, a count of one) cite the pages that
    # justify their use, not a figure to check; they are left out.
    return [values[n]["cite"] for n in sorted(names)
            if n in values and "cite" in values[n] and values[n].get("value") not in (0, 1)]


def excerpt_for(form_doc, mani):
    """The cited pages of every cited document, with what was used and why. A locator
    that names pages of another archived document gives those pages too, and so do
    the citations of the year parameters the form references."""
    cites, extra = {}, {}
    for line in form_doc["lines"] + [{"cite": c} for c in param_cites(form_doc)]:
      for c in [line["cite"]] + [r["cite"] for r in line.get("refuses", [])]:
        more, rest = secondary_pages(c["locator"], mani, c["doc"])
        cites.setdefault(c["doc"], set()).add(rest)
        for doc_id, pages in more.items():
            extra.setdefault(doc_id, set()).update(pages)
    excerpt, used = [], []
    for doc_id in list(cites) + [d for d in extra if d not in cites]:
        locators = cites.get(doc_id, set())
        doc = mani[doc_id]
        pages = doc_pages(doc)
        if len(pages) <= WHOLE_DOC_MAX_PAGES:
            chosen = set(range(1, len(pages) + 1)); how = "whole document"
        else:
            chosen = set(extra.get(doc_id, set()))
            for loc in locators:
                chosen |= locator_pages(loc)
                if not locator_pages(loc):
                    chosen |= heading_pages(pages, loc)
            how = "cited pages" if locators else "pages named by another document's citation"
        chosen = sorted(p for p in chosen if 1 <= p <= len(pages))
        # A page classified as columnar prose is given in reading order (tools/extract_text.py);
        # worksheets, tables and single-column pages keep the layout text.
        kinds = page_kinds(doc)
        cols = doc_pages(doc, "cols_file") if kinds else None
        cols_pages = [p for p in chosen if kinds and kinds[p - 1] == "prose"]
        used.append({"doc": doc_id, "revision": doc.get("revision", ""), "text_sha256": doc["text_sha256"],
                     "pages": chosen, "how": how, "locators": sorted(locators),
                     "cols_pages": cols_pages, "cols_sha256": doc.get("cols_sha256", "-")})
        for p in chosen:
            if p in cols_pages:
                excerpt.append(f"===== {doc_id} ({doc.get('revision','')}) page {p} of {len(pages)}, in reading order =====\n{cols[p - 1]}")
            else:
                excerpt.append(f"===== {doc_id} ({doc.get('revision','')}) page {p} of {len(pages)}, as laid out =====\n{pages[p - 1]}")
    return "\n\n".join(excerpt), used


# ---------- exported lines ----------

def operand_refs(node):
    """Every line id an expression reads, walking operand positions only (a definition
    reference's `line` names a line inside that definition, not here)."""
    out = set()
    def ref(r):
        if isinstance(r, str):
            out.add(r)
        elif isinstance(r, dict) and "def" in r:
            for v in r.get("bind", {}).values():
                ref(v)
    def walk(e):
        if not isinstance(e, dict):
            return
        for k in ("from", "take", "amount", "key", "status", "then", "rate"):
            if k in e:
                ref(e[k])
        for k in ("of",):
            for x in e.get(k, []):
                ref(x)
        for k in ("eq", "ne", "lt", "le", "gt", "ge"):
            if k in e:
                for x in e[k]:
                    ref(x)
        for k in ("all", "any"):
            for x in e.get(k, []):
                walk(x)
        if "not" in e:
            walk(e["not"])
        if "where" in e and e["where"]:
            walk(e["where"])
        for alt in e.get("alternatives", []):
            walk(alt.get("guard")); ref(alt.get("then"))
    walk(node)
    return out


def exported_lines(form_doc):
    """Computed helper lines other forms depend on (for a form), or the result lines
    nothing else in the definition reads (for a def). These carry logic that no
    printed line exposes, so they are transcribed and compared by id."""
    global ALL_LINES
    if ALL_LINES is None:
        ALL_LINES = load_all_lines()
    fid = form_doc["id"]
    computed = [l for l in form_doc["lines"] if l["expr"].get("op") != "input"]
    helpers = [l for l in computed if l["printed"] in HELPER_PRINTED]
    if fid in load_defs():
        referenced = set()
        for l in form_doc["lines"]:
            referenced |= operand_refs(l["expr"])
        return [l for l in computed if l["id"] not in referenced]
    refs = set()
    for other_id, (other_fid, line) in ALL_LINES.items():
        if other_fid != fid:
            refs.update(re.findall(r'"(' + re.escape(fid) + r'\.[a-z0-9_.]+)"', json.dumps(line["expr"])))
    return [l for l in helpers if l["id"] in refs]


# ---------- prompt ----------

GRAMMAR = """Expression grammar (YAML). Exactly one atom per line. Operands written as a line reference
(a string id of a line in this worksheet or another form), a constant ({const: 0} for money cents,
{const: true}, {const: "single"}), or a parameter ({param: name}).

  {op: input, source: "<the box or question this value comes from>"}
  {op: copy, from: <ref>}                      # <ref> is a line id string, or for a parameterised
                                               # worksheet {def: tax_on_amount, bind: {amount: <ref>, status: <ref>}, line: tax}
  {op: param, ref: <parameter name>}
  {op: sum, of: [<ref>, ...]}
  {op: subtract, from: <ref>, take: <operand>}
  {op: subtract_floor0, from: <ref>, take: <operand>}     # if zero or less, enter -0-
  {op: smaller_of, of: [<ref>, <ref>]}
  {op: larger_of, of: [<ref>, <ref>]}
  {op: multiply_rate, amount: <ref>, rate: {param: name}}  # rate is a parameter
  {op: round, of: <ref>, unit: <integer cents>, rule: half_up | up | down}  # e.g. up to the next $1,000: unit 100000, rule up
  {op: table_lookup, table: tax_table, key: <ref>, status: <ref>}
  {op: sum_over, collection: <collection id>, field: <line id within the entry>, where: <test>}  # where optional
  {op: test, eq: [<operand>, <operand>]}        # also ne, lt, le, gt, ge; or {op: test, all: [<test>, ...]},
                                               # {op: test, any: [...]}, {op: test, not: <test>}
  {op: choose, alternatives: [{guard: <test>, then: <ref>}, ...]}   # guards exhaustive and disjoint

Money is integer cents. Rates are parameters. There are no loops, strings, functions or arithmetic
beyond these atoms; a line that needs more than one atom is written as several lines, the extra ones
being helper lines (printed: "(helper)") with ids of your own choosing."""


def collection_notes():
    """Collections (keyed entry forms) and their entry fields, for cross-form references."""
    out = []
    for f in sorted(os.listdir(FORMS)):
        if not f.endswith(".yaml"):
            continue
        d = yaml.safe_load(open(os.path.join(FORMS, f), encoding="utf-8"))
        doc = d.get("form")
        if not doc or not doc.get("collection"):
            continue
        parent = doc["collection"].get("parent")
        fields = "; ".join(f"{l['id']} ({l['type']}: {l['label'][:60]})" for l in doc["lines"])
        out.append(f"  - collection `{doc['id']}`" + (f" nested in each `{parent}` entry" if parent else "") +
                   f" — one entry per {doc['title'][:70]}; entry fields: {fields}")
    return "\n".join(out)


def enum_notes():
    params_doc = yaml.safe_load(open(os.path.join(ROOT, "params", "2025.yaml"), encoding="utf-8"))
    enums = (params_doc.get("params") or params_doc).get("enums", {})
    return "\n".join(f"  - Enum({name}): " + ", ".join(f'"{v}"' for v in e["values"]) for name, e in enums.items())


def build_prompt(form_doc, excerpt, params, other_lines):
    lines = form_doc["lines"]
    inputs = [l for l in lines if l["expr"].get("op") == "input"]
    targets = [l for l in lines if l["printed"] not in HELPER_PRINTED and l["expr"].get("op") != "input"]
    tgt = "\n".join(f"  - printed {l['printed']!r}: {l['label']}" for l in targets)
    exported = exported_lines(form_doc)
    exp = "\n".join(f"  - id {l['id']} ({l['type']}): {l['label']}" for l in exported)
    inp = "\n".join(f"  - {l['id']} (printed {l['printed']!r}, type {l['type']}): {l['expr'].get('source','')[:160]}" for l in inputs)
    prm = "\n".join(f"  - {k}: {v}" for k, v in params.items())
    oth = "\n".join(f"  - {k}: {v}" for k, v in other_lines.items())
    spec = open(os.path.join(ROOT, "spec", "spec.md"), encoding="utf-8").read()
    atoms = spec[spec.index("### 4.1 Values and types"):spec.index("### 4.4 Collections")]
    return f"""You are producing an independent transcription of the IRS worksheet or form below into a
formal data model, working ONLY from the IRS text provided here. Do not rely on memory of the tax law
or of any software; if the text does not say it, do not encode it.

# Data model (from the project specification)

{atoms}

{GRAMMAR}

# The worksheet to transcribe

Form id: {form_doc['id']}
Title: {form_doc['title']}
Tax year: {form_doc['tax_year']}

Transcribe these printed lines, each as one line record with id "{form_doc['id']}.line<printed>"
(for example {form_doc['id']}.line{targets[0]['printed'] if targets else '1'}), in this order:
{tgt}

Also produce these intermediate values, which other forms depend on, each as a line with EXACTLY
this id (printed "(helper)"); they may reference the printed lines above and the inputs below:
{exp if exp else '  (none)'}

These input lines already exist and must be referenced by these exact ids (do not redefine them):
{inp if inp else '  (none)'}

Year parameters you may reference with {{param: name}} (values shown for recognition; cents or integer pairs):
{prm}

Enumerations and their only permitted values (compare with {{const: "value"}}):
{enum_notes()}

Keyed collections (Form W-2s, payers, sales, gifts): a total over entries is written
{{op: sum_over, collection: <id>, field: <entry field id>, where: <test over entry fields>}}; a nested
collection is summed within each parent entry, and the parent's per-entry totals summed again:
{collection_notes()}

Lines on other forms you may reference by id (only where the IRS text says the value comes from
there; "(helper)" lines are that form's intermediate values):
{oth}

# Output

Return ONLY a YAML document of the form

lines:
  - id: {form_doc['id']}.line<printed>
    printed: "<printed>"
    label: "<the IRS wording>"
    type: <Dollars | NonNegDollars | Rate | Count | Bool | Enum(name)>
    expr: <one atom>
  - ...

plus any helper lines you need (printed: "(helper)", ids "{form_doc['id']}.h_<name>"). No prose before
or after the YAML. Where the IRS text leaves a point genuinely open, choose a reading and add a
`note:` field on that line saying what was open and what you chose.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
"""


# ---------- comparison ----------

def load_form(form_id):
    d = yaml.safe_load(open(os.path.join(FORMS, form_id + ".yaml"), encoding="utf-8"))
    return d.get("form") or d.get("def")


def norm_ref(ref):
    if isinstance(ref, dict) and "def" in ref:
        return {"def": ref["def"], "line": ref.get("line"), "bind": {k: v for k, v in sorted(ref.get("bind", {}).items())}}
    return ref


def load_defs():
    defs = {}
    for f in os.listdir(FORMS):
        if f.endswith(".yaml"):
            d = yaml.safe_load(open(os.path.join(FORMS, f), encoding="utf-8"))
            if "def" in d:
                defs[d["def"]["id"]] = d["def"]
    return defs


def load_all_lines():
    """Every line of every form, for expanding helper lines referenced across forms."""
    out = {}
    for f in os.listdir(FORMS):
        if f.endswith(".yaml"):
            d = yaml.safe_load(open(os.path.join(FORMS, f), encoding="utf-8"))
            doc = d.get("form") or d.get("def")
            for l in doc["lines"]:
                out[l["id"]] = (doc["id"], l)
    return out


ALL_LINES = None


class Expander:
    """Expands a line's expression into a tree over inputs, params, constants and
    references outside the form, so helper naming on either side does not matter.
    Shared parameterised definitions are inlined with their bindings substituted,
    and Boolean guards are normalised (eq-to-true, not-of-comparison)."""

    def __init__(self, form_id, lines, defs=None, bound=None, foreign=False, inputs=None, params=None):
        self.form_id = form_id
        self.by_id = {l["id"]: l for l in lines}
        self.printed = {l["id"]: l["printed"] for l in lines}
        self.defs = defs if defs is not None else load_defs()
        self.bound = bound or {}
        self.foreign = foreign   # expanding another form's helper: its printed lines stay qualified references
        self.inputs = inputs or {}   # the project's input lines of this form, shared by both sides
        self.params = params or {}   # parameter values, so literal-valued parameters compare as constants

    def inline_def(self, r, depth):
        d = self.defs.get(r["def"])
        if d is None or depth > 40:
            return {"def": r["def"], "line": r["line"], "bind": {k: self.operand(v, depth) for k, v in r["bind"].items()}}
        bound = {k: self.operand(v, depth) for k, v in r["bind"].items()}
        sub = Expander(d["id"], d["lines"], self.defs, bound)
        target = sub.by_id.get(r["line"]) or sub.by_id.get(d["id"] + "." + str(r["line"]))
        if target is None:
            return {"unknown": f"def line {r['line']}"}
        return sub.expr(target["expr"], depth + 1)

    def ref(self, r, depth):
        r = norm_ref(r)
        if isinstance(r, dict):
            if "def" in r:
                return self.inline_def(r, depth)
            if "const" in r:
                return {"const": r["const"]}
            if "param" in r:
                return self.param(r["param"])
            return {"unknown": json.dumps(r, sort_keys=True)}

        if isinstance(r, str):
            if r in self.bound:
                return self.bound[r]
            if r in self.inputs and r not in self.by_id:
                line = self.inputs[r]
                if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                    return {"line": line["printed"]}
                return {"input": r}
            if r in self.by_id:
                line = self.by_id[r]
                if line["expr"].get("op") == "input" or depth > 40:
                    if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                        return {"ref": r} if self.foreign else {"line": line["printed"]}
                    return {"input": r}
                # A printed line of this form is referenced by its number; helpers and
                # definition-internal lines are expanded in place.
                if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                    return {"ref": r} if self.foreign else {"line": line["printed"]}
                return self.expr(line["expr"], depth + 1)
            if r.startswith(self.form_id + ".line"):
                return {"line": r[len(self.form_id) + 5:]}
            # A helper line on another form is expanded in place, so that a value the
            # project routes through a named helper compares with the same expression
            # written inline; printed lines and inputs elsewhere stay as references.
            global ALL_LINES
            if ALL_LINES is None:
                ALL_LINES = load_all_lines()
            other = ALL_LINES.get(r)
            if other and other[1]["printed"] in HELPER_PRINTED and other[1]["expr"].get("op") != "input" and depth <= 40:
                sub = Expander(other[0], [l for (fid, l) in ALL_LINES.values() if fid == other[0]], self.defs, foreign=True)
                return sub.expr(other[1]["expr"], depth + 1)
            return {"ref": r}
        return {"const": r}

    def param(self, name):
        """A parameter whose value is the literal 0 or 1 compares as that constant."""
        v = self.params.get(name)
        if v in (0, 1) and not isinstance(v, bool):
            return {"const": v}
        return {"param": name}

    def operand(self, o, depth):
        return self.ref(o, depth)

    NEGATE = {"lt": "ge", "ge": "lt", "le": "gt", "gt": "le", "eq": "ne", "ne": "eq"}

    def orient(self, k, x, y):
        if k in ("gt", "ge"):
            k, x, y = {"gt": "lt", "ge": "le"}[k], y, x
        # Against zero, a non-negative line: "is zero" is "at most zero", "is not zero" is "above zero".
        zero = {"const": 0}
        if k in ("eq", "ne"):
            for a_, b_ in ((x, y), (y, x)):
                if a_ == zero and self.nonneg(b_):
                    return {"test": "le", "args": [b_, zero]} if k == "eq" else {"test": "lt", "args": [zero, b_]}
            return {"test": k, "args": sorted([x, y], key=json.dumps)}
        return {"test": k, "args": [x, y]}

    def negate(self, tree):
        if isinstance(tree, dict) and tree.get("test") in self.NEGATE:
            return self.orient(self.NEGATE[tree["test"]], tree["args"][0], tree["args"][1])
        if isinstance(tree, dict) and tree.get("test") == "not":
            return tree["args"][0]
        if isinstance(tree, dict) and tree.get("test") in ("all", "any"):
            return {"test": "any" if tree["test"] == "all" else "all",
                    "args": sorted((self.negate(x) for x in tree["args"]), key=json.dumps)}
        return {"test": "not", "args": [tree]}

    def nonneg(self, tree):
        """Whether a tree is a line known to be non-negative (Count or NonNegDollars)."""
        global ALL_LINES
        if ALL_LINES is None:
            ALL_LINES = load_all_lines()
        if isinstance(tree, dict):
            if "ref" in tree and tree["ref"] in ALL_LINES:
                return ALL_LINES[tree["ref"]][1]["type"] in ("Count", "NonNegDollars")
            if "line" in tree:
                for l in self.by_id.values():
                    if l["printed"] == tree["line"]:
                        return l["type"] in ("Count", "NonNegDollars")
                for l in self.inputs.values():
                    if l["printed"] == tree["line"]:
                        return l["type"] in ("Count", "NonNegDollars")
            if tree.get("op") == "sum_over":
                return True
        return False

    def test(self, t, depth):
        if isinstance(t, str):   # a guard written as a reference to a Boolean line
            return self.ref(t, depth)
        for k in ("eq", "ne", "lt", "le", "gt", "ge"):
            if k in t:
                x, y = self.operand(t[k][0], depth), self.operand(t[k][1], depth)
                # `X == true` is X; `X == false` is not X, when X is itself a test.
                for a_, b_ in ((x, y), (y, x)):
                    if isinstance(b_, dict) and b_.get("const") in (True, False) and isinstance(a_, dict) and "test" in a_:
                        if k == "eq":
                            return a_ if b_["const"] else self.negate(a_)
                        if k == "ne":
                            return self.negate(a_) if b_["const"] else a_
                return self.orient(k, x, y)
        if "all" in t:
            return {"test": "all", "args": sorted((self.test(x, depth) for x in t["all"]), key=json.dumps)}
        if "any" in t:
            return {"test": "any", "args": sorted((self.test(x, depth) for x in t["any"]), key=json.dumps)}
        if "not" in t:
            return self.negate(self.test(t["not"], depth))
        return {"unknown": json.dumps(t, sort_keys=True)}

    def expr(self, e, depth=0):
        op = e.get("op")
        if op == "input":
            return {"input": e.get("source", "")[:60]}
        if op == "copy":
            return self.ref(e["from"], depth)
        if op == "param":
            return self.param(e["ref"])
        if op in ("sum", "smaller_of", "larger_of"):
            parts = [self.ref(x, depth) for x in e["of"]]
            if op == "sum":   # zero terms carry nothing: scope placeholders and screens
                parts = [t for t in parts if t != {"const": 0}] or [{"const": 0}]
                if len(parts) == 1:
                    return parts[0]
            return {"op": op, "of": sorted(parts, key=json.dumps)}
        if op in ("subtract", "subtract_floor0"):
            return {"op": op, "from": self.ref(e["from"], depth), "take": self.operand(e["take"], depth)}
        if op == "multiply_rate":
            return {"op": op, "amount": self.ref(e["amount"], depth), "rate": self.operand(e["rate"], depth)}
        if op == "round":
            return {"op": op, "of": self.ref(e["of"], depth), "unit": e.get("unit"), "rule": e.get("rule")}
        if op == "table_lookup":
            return {"op": op, "table": e.get("table"), "key": self.ref(e["key"], depth), "status": self.ref(e["status"], depth)}
        if op == "sum_over":
            w = self.test(e["where"], depth) if e.get("where") else None
            return {"op": op, "collection": e.get("collection"), "field": e.get("field"), "where": w}
        if op == "test":
            return self.test(e, depth)
        if op == "choose":
            alts = [{"guard": self.test(a["guard"], depth), "then": self.ref(a["then"], depth)} for a in e["alternatives"]]
            # Alternatives that select the same target are one case: merge their guards with `any`.
            by_then = {}
            for alt in alts:
                by_then.setdefault(json.dumps(alt["then"], sort_keys=True), []).append(alt)
            merged = []
            for group in by_then.values():
                if len(group) == 1:
                    merged.append(group[0])
                else:
                    merged.append({"guard": {"test": "any", "args": sorted((g["guard"] for g in group), key=json.dumps)}, "then": group[0]["then"]})
            return {"op": op, "alternatives": sorted(merged, key=json.dumps)}
        return {"unknown": json.dumps(e, sort_keys=True)}


def canonical(tree):
    return json.dumps(tree, sort_keys=True, ensure_ascii=False)


def compare(form_id, project_lines, second_lines):
    defs = load_defs()
    params_doc = yaml.safe_load(open(os.path.join(ROOT, "params", "2025.yaml"), encoding="utf-8"))
    pvals = {k: v["value"] for k, v in (params_doc.get("params") or params_doc)["values"].items()}
    inputs = {l["id"]: l for l in project_lines if l["expr"].get("op") == "input"}
    a = Expander(form_id, project_lines, defs, inputs=inputs, params=pvals)
    b = Expander(form_id, second_lines, defs, inputs=inputs, params=pvals)
    results = []
    second_by_id = {l["id"]: l for l in second_lines}
    for l in exported_lines({"id": form_id, "lines": project_lines}):
        pa = canonical(a.expr(l["expr"]))
        s = second_by_id.get(l["id"])
        if s is None:
            results.append({"printed": l["id"], "label": l["label"], "status": "MISSING", "project": pa, "second": None, "note": None})
            continue
        try:
            sb = canonical(b.expr(s["expr"]))
        except Exception as ex:
            sb = f"<unparseable: {ex}>"
        results.append({"printed": l["id"], "label": l["label"], "status": "AGREE" if pa == sb else "DISAGREE",
                        "project": pa, "second": sb, "note": s.get("note")})
    second_by_printed = {l["printed"]: l for l in second_lines if l["printed"] not in HELPER_PRINTED}
    is_def = form_id in defs
    for l in project_lines:
        if l["printed"] in HELPER_PRINTED or l["expr"].get("op") == "input" or is_def:
            continue
        s = second_by_printed.get(l["printed"])
        pa = canonical(a.expr(l["expr"]))
        if s is None:
            results.append({"printed": l["printed"], "label": l["label"], "status": "MISSING", "project": pa, "second": None, "note": None})
            continue
        try:
            sb = canonical(b.expr(s["expr"]))
        except Exception as ex:  # malformed second transcription
            sb = f"<unparseable: {ex}>"
        results.append({"printed": l["printed"], "label": l["label"], "status": "AGREE" if pa == sb else "DISAGREE",
                        "project": pa, "second": sb, "note": s.get("note")})
    extra = [p for p in second_by_printed if p not in {l["printed"] for l in project_lines}]
    return results, extra


# ---------- model call ----------

TRANSCRIBE_SYSTEM = ("You transcribe IRS worksheets into a formal data model from the text given to you. "
                     "You have no tools and no other sources. Output only the YAML requested.")


def call_model(prompt, model, timeout=900, system=TRANSCRIBE_SYSTEM):
    cmd = ["claude", "-p", "--no-session-persistence", "--setting-sources", "", "--tools", "",
           "--permission-prompts", "none", "--output-format", "json", "--model", model,
           "--system-prompt", system]
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode}: {proc.stderr[:400]}")
    events = json.loads(proc.stdout)
    events = events if isinstance(events, list) else [events]
    result = next((e for e in events if e.get("type") == "result"), None)
    if result is None or result.get("subtype") != "success":
        raise RuntimeError(f"no successful result: {json.dumps(events)[:400]}")
    usage = result.get("modelUsage") or {}
    return result.get("result", ""), {"model_reported": list(usage.keys()), "usage": usage, "cost_usd": result.get("total_cost_usd")}


def extract_yaml(text):
    # A response may hold an abandoned draft block before the finished one; the answer is the last block.
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    m = blocks[-1] if blocks else None
    body = m if m is not None else text
    doc = yaml.safe_load(body)
    if not isinstance(doc, dict) or "lines" not in doc:
        raise ValueError("second transcription has no `lines`")
    for l in doc["lines"]:
        l["printed"] = str(l.get("printed", ""))
        l.setdefault("expr", {})
    return doc


# ---------- log ----------

def write_log(form_doc, model, prompt, used, results, extra, raw_text, meta, dry_run=False):
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    kept = rulings.kept("transcription", fid)
    counts = {k: sum(1 for r in results if r["status"] == k) for k in ("AGREE", "DISAGREE", "MISSING")}
    out = [f"# Transcription agreement — {fid}", "",
           f"Second transcription of `{form_doc['title']}` by an isolated model (spec 6.5), compared line by line with `forms/2025/{fid}.yaml`.", "",
           "| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
           f"| model requested | {model} |",
           f"| model reported | {', '.join(meta.get('model_reported', [])) or '-'} |",
           f"| prompt sha256 | {hashlib.sha256(prompt.encode()).hexdigest()} |",
           f"| printed lines compared | {len(results)} |",
           f"| agree / disagree / missing | {counts['AGREE']} / {counts['DISAGREE']} / {counts['MISSING']} |",
           f"| extra printed lines in second | {', '.join(extra) if extra else 'none'} |", "",
           "## Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    out += ["", "## Lines", ""]
    for r in results:
        out.append(f"### {r['printed']} — {r['label'][:90]}")
        out.append(f"Status: **{r['status']}**")
        if r["status"] != "AGREE":
            out += ["", "Project:", "", "```json", r["project"], "```", "", "Second:", "", "```json", str(r["second"]), "```"]
            if r.get("note"):
                out += ["", f"Second transcription's note: {r['note']}"]
            ruling = kept.get((r["printed"], r["project"], str(r["second"])), "Ruling: open")
            out += ["", ruling, ""]
        else:
            out.append("")
    out += ["## Raw second transcription", "", "```yaml", raw_text.strip(), "```", ""]
    path = os.path.join(LOGS, fid + ".md")
    if not dry_run:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--dry-run", action="store_true", help="build the prompt and excerpt; call no model")
    ap.add_argument("--from-response", action="store_true", help="re-compare the saved response; call no model")
    a = ap.parse_args()
    mani = manifest()
    form_doc = load_form(a.form)
    excerpt, used = excerpt_for(form_doc, mani)
    params_doc = yaml.safe_load(open(os.path.join(ROOT, "params", "2025.yaml"), encoding="utf-8"))
    values = (params_doc.get("params") or params_doc)["values"]
    params = {k: v["value"] for k, v in values.items()}
    other = {}
    for f in sorted(os.listdir(FORMS)):
        if f.endswith(".yaml") and f[:-5] != a.form:
            d = load_form(f[:-5])
            if d.get("collection"):
                continue   # listed with the collections instead
            for l in d["lines"]:
                tag = "" if l["printed"] not in HELPER_PRINTED else " (helper)"
                other[l["id"]] = l["label"][:70] + tag
    prompt = build_prompt(form_doc, excerpt, params, other)
    os.makedirs(RAW, exist_ok=True)
    open(os.path.join(RAW, a.form + ".prompt.txt"), "w", encoding="utf-8").write(prompt)
    print(f"{a.form}: excerpt {len(excerpt):,} chars from " + "; ".join(f"{u['doc']} pages {u['pages']} ({u['how']})" for u in used))
    print(f"prompt {len(prompt):,} chars -> .transcription/{a.form}.prompt.txt")
    if a.dry_run:
        return
    if a.from_response:
        text = open(os.path.join(RAW, a.form + ".response.txt"), encoding="utf-8").read()
        meta = json.load(open(os.path.join(RAW, a.form + ".meta.json"))) if os.path.exists(os.path.join(RAW, a.form + ".meta.json")) else {}
    else:
        text, meta = call_model(prompt, a.model)
        open(os.path.join(RAW, a.form + ".response.txt"), "w", encoding="utf-8").write(text)
        json.dump(meta, open(os.path.join(RAW, a.form + ".meta.json"), "w"))
    second = extract_yaml(text)
    results, extra = compare(a.form, form_doc["lines"], second["lines"])
    path, counts = write_log(form_doc, a.model, prompt, used, results, extra, text, meta)
    print(f"{a.form}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, missing {counts['MISSING']}, extra {len(extra)}; cost {meta.get('cost_usd')} -> {os.path.relpath(path, ROOT)}")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 else 3)


if __name__ == "__main__":
    main()
