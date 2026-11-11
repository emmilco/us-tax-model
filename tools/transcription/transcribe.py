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

The log is reviews/<year>/transcription/<form>.md for a Claude model and <form>.<family>.md for
another family (families.py), each with its own rulings sidecar; the raw prompt and response
under .transcription/ take the same stem.
"""
import argparse, bisect, datetime, hashlib, json, os, re, subprocess, sys
from functools import cache
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402
import input_contracts  # noqa: E402
import adapter_contracts  # noqa: E402
import input_context  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y, YEAR  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York documents, sources and logs)
import archive_text  # noqa: E402
from structured_text import indent_rest, inline, summary  # noqa: E402
import citations  # noqa: E402
import html_sections  # noqa: E402  (a web edition cut by the headings its locators name)
SOURCES = str(jurisdiction.ypath("sources", Y))
FORMS = str(jurisdiction.ypath("forms", Y))
LOGS = str(jurisdiction.ypath("reviews", Y, "transcription"))
RAW = os.path.join(ROOT, ".transcription")
WHOLE_DOC_MAX_PAGES = 6
HELPER_PRINTED = {"(helper)", "(gate)", "(computed helper)"}
PROMPT_POLICY = "source-only-computation-v3"
# Prompt policies under which no project-written computation is shown and the other-form catalog
# does not depend on the reviewed form's encoding: v2 listed every other form, v3 a source-chosen
# subset (catalog_selection) and asks for shown_when wherever the IRS text conditions a line.
INDEPENDENT_PROMPT_POLICIES = frozenset({"source-only-computation-v2", PROMPT_POLICY})
PROJECT_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def project_yaml(path):
    """Read local project data with the fast safe loader when LibYAML is installed.

    Model response parsing remains on its existing validation path.
    """
    with open(path, encoding="utf-8") as stream:
        return yaml.load(stream, Loader=PROJECT_YAML_LOADER)


def marker_keys(lines):
    """Each line's comparison key: its printed marker, qualified by the line id when several
    lines of the document share the marker (a form that carries more than one IRS worksheet)."""
    counts = {}
    for l in lines:
        counts[str(l["printed"])] = counts.get(str(l["printed"]), 0) + 1
    plain = lambda m: counts[m] == 1 or m in HELPER_PRINTED or m == "(screen)"
    return {l["id"]: str(l["printed"]) if plain(str(l["printed"])) else f'{l["printed"]} ({l["id"]})' for l in lines}


# ---------- sources ----------

def manifest():
    """The archive's documents by id. In New York mode the federal documents follow the New York
    ones: a New York review cites only New York pages, but the other-form catalog reads the federal
    forms' own pages to choose the federal lines a New York text names."""
    out = {}
    for sources in source_dirs():
        m = json.load(open(os.path.join(sources, "manifest.json")))
        docs = m["documents"] if isinstance(m, dict) else m
        out.update({d["id"]: d for d in docs if d["id"] not in out})
    return out


def source_dirs():
    return [SOURCES] + ([os.path.join(ROOT, "sources", Y)] if jurisdiction.NY else [])


def source_dir(doc_id):
    """The archive directory of a document: sources/ny/<year>/ for a New York document."""
    return SOURCES if jurisdiction.mine(doc_id) else str(jurisdiction.doc_dir("sources", Y, doc_id))


def form_files(sort=True):
    """(file name, path) of every document the jurisdiction reads: federally forms/<year>/ alone
    (listed as before, sorted or in directory order); in New York mode the federal documents, then
    the New York ones, which read federal lines."""
    out = []
    for d in [FORMS] if not jurisdiction.NY else [str(p) for p in jurisdiction.read_dirs("forms", Y)]:
        names = sorted(os.listdir(d)) if sort else os.listdir(d)
        out += [(f, os.path.join(d, f)) for f in names]
    return out


def form_path(form_id):
    d = FORMS if jurisdiction.mine(form_id) else str(jurisdiction.doc_dir("forms", Y, form_id))
    return os.path.join(d, form_id + ".yaml")


def year_params():
    """The year parameters a review reads: params/<year>.yaml; in New York mode merged with
    params/ny/<year>.yaml (names prefixed `ny.`), as the canonical build merges them."""
    doc = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
    if jurisdiction.NY and os.path.exists(jurisdiction.params_file(Y)):
        fed = doc.get("params") or doc
        ny = project_yaml(str(jurisdiction.params_file(Y)))
        ny = ny.get("params") or ny
        doc = {"params": {**fed, "values": {**fed["values"], **ny.get("values", {})},
                          "enums": {**fed.get("enums", {}), **ny.get("enums", {})}}}
    return doc


_PAGES = {}


def doc_pages(doc, key="text_file"):
    memo = (source_dir(doc["id"]), doc["id"], key, doc.get(key), doc.get("text_sha256"), doc.get("cols_sha256"))
    if memo not in _PAGES:
        text = archive_text.read(source_dir(doc["id"]), doc, key)
        pages = text.split("\f")
        if pages and not pages[-1].strip():
            pages = pages[:-1]
        _PAGES[memo] = pages
    return list(_PAGES[memo])


def page_kinds(doc):
    """The per-page classification of the reading-order extraction, or None."""
    if "pages_file" not in doc:
        return None
    return json.load(open(os.path.join(source_dir(doc["id"]), doc["pages_file"]), encoding="utf-8"))["pages"]


PAGE_LIST = re.compile(r"\bpp?\.\s*" + citations.PAGES_RE)
DOC_PAGES = re.compile(r"\b([a-z][a-z0-9-]*)\s+(pp?\.\s*" + citations.PAGES_RE + ")")


def locator_pages(locator):
    """Page numbers named anywhere in a locator ('pp. 34–35, line 12e', 'pp. 17 and 19, ...'),
    read with the page-list grammar of tools/citations.py."""
    out = set()
    for m in PAGE_LIST.finditer(locator):
        out.update(citations.page_list(m.group(1)))
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
    rest = DOC_PAGES.sub(take, locator)
    return out, rest


def param_cites(form_doc):
    """Citations of the year parameters a form's lines reference."""
    names = set()
    for line in form_doc["lines"]:
        text = json.dumps(line.get("expr", {}))
        names.update(re.findall(r'"param": "([a-z0-9_.]+)"', text))
        if line.get("expr", {}).get("op") == "param":
            names.add(line["expr"]["ref"])
    params_doc = year_params()
    values = (params_doc.get("params") or params_doc)["values"]
    # Structural constants (a zero amount, a count of one) cite the pages that
    # justify their use, not a figure to check; they are left out.
    return [values[n]["cite"] for n in sorted(names)
            if n in values and "cite" in values[n] and values[n].get("value") not in (0, 1)]


def excerpt_for(form_doc, mani):
    """The cited pages of every cited document, with what was used and why. A locator
    that names pages of another archived document gives those pages too, and so do
    the citations of the year parameters the form references."""
    excerpt, used = [], []
    for doc_id, chosen, how, locators in excerpt_pages(form_doc, mani):
        doc = mani[doc_id]
        pages = doc_pages(doc)
        # A page classified as columnar prose is given in reading order (tools/extract_text.py);
        # worksheets, tables and single-column pages keep the layout text.
        kinds = page_kinds(doc)
        cols = doc_pages(doc, "cols_file") if kinds else None
        cols_pages = [p for p in chosen if kinds and kinds[p - 1] == "prose"]
        cut = sectioned(doc_id, mani, how, locators)
        if cut:
            used.append({"doc": doc_id, "revision": doc.get("revision", ""), "text_sha256": doc["text_sha256"],
                         "pages": chosen, "how": "cited sections: " + "; ".join(cut[1]), "locators": sorted(locators),
                         "cols_pages": [], "cols_sha256": doc.get("cols_sha256", "-"), "lines": [list(r) for r in cut[2]]})
            excerpt.append(f"===== {doc_id} ({doc.get('revision','')}), the sections cited, of a single web page =====\n{cut[0]}")
            continue
        used.append({"doc": doc_id, "revision": doc.get("revision", ""), "text_sha256": doc["text_sha256"],
                     "pages": chosen, "how": how, "locators": sorted(locators),
                     "cols_pages": cols_pages, "cols_sha256": doc.get("cols_sha256", "-")})
        for p in chosen:
            if p in cols_pages:
                excerpt.append(f"===== {doc_id} ({doc.get('revision','')}) page {p} of {len(pages)}, in reading order =====\n{cols[p - 1]}")
            else:
                excerpt.append(f"===== {doc_id} ({doc.get('revision','')}) page {p} of {len(pages)}, as laid out =====\n{pages[p - 1]}")
    return "\n\n".join(excerpt), used


def sectioned(doc_id, mani, how, locators):
    """A web edition archived as one page and cut by its headings (html_sections.py): (text, section titles,
    line ranges of the sections) of the sections its locators name; None for its whole page (another
    document, or a locator naming no heading)."""
    if doc_id not in html_sections.SECTIONED or how != "whole document":
        return None
    pages = doc_pages(mani[doc_id])
    return html_sections.cut(source_dir(doc_id), mani[doc_id], "\f".join(pages), locators) if len(pages) == 1 else None


def source_units(doc_id, chosen, how, locators, mani):
    """(keys, texts) of one document's chosen pages, as the catalog compares them: (doc, page) keys and the
    page texts; for a web edition cut by headings, (doc, ("line", n)) keys of its cited sections' lines and
    the cut text, so two documents share its page only where they cite the same part of it."""
    cut = sectioned(doc_id, mani, how, locators)
    if cut:
        return {(doc_id, ("line", n)) for a, b in cut[2] for n in range(a, b)}, [cut[0]]
    pages = doc_pages(mani[doc_id])
    return {(doc_id, p) for p in chosen}, [pages[p - 1] for p in chosen]


def excerpt_pages(form_doc, mani):
    """[(doc id, chosen pages, how, locators)] in excerpt order, the page choice of excerpt_for."""
    cites, extra = {}, {}
    for line in form_doc["lines"] + [{"cite": c} for c in param_cites(form_doc)]:
      for c in [line["cite"]] + [r["cite"] for r in line.get("refuses", [])]:
        more, rest = secondary_pages(c["locator"], mani, c["doc"])
        cites.setdefault(c["doc"], set()).add(rest)
        for doc_id, pages in more.items():
            extra.setdefault(doc_id, set()).update(pages)
    out = []
    for doc_id in list(cites) + [d for d in extra if d not in cites]:
        locators = cites.get(doc_id, set())
        pages = doc_pages(mani[doc_id])
        if len(pages) <= WHOLE_DOC_MAX_PAGES:
            chosen = set(range(1, len(pages) + 1)); how = "whole document"
        else:
            chosen = set(extra.get(doc_id, set()))
            for loc in locators:
                chosen |= locator_pages(loc)
                if not locator_pages(loc):
                    chosen |= heading_pages(pages, loc)
            how = "cited pages" if locators else "pages named by another document's citation"
        out.append((doc_id, sorted(p for p in chosen if 1 <= p <= len(pages)), how, locators))
    return out


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
        for k in ("from", "take", "amount", "count", "part", "whole", "key", "status", "then", "rate", "field"):
            if k in e:
                ref(e[k])
        for k in ("of", "keys"):
            values = e.get(k, [])
            for x in ([values] if isinstance(values, str) else values):
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
    excluded = adapter_contracts.excluded_ids(fid, Y)
    helpers = [l for l in computed if l["printed"] in HELPER_PRINTED and l["id"] not in excluded]
    if fid in load_defs():
        referenced = set()
        for l in form_doc["lines"]:
            referenced |= operand_refs(l["expr"])
        return [l for l in computed if l["id"] not in referenced]
    refs = set()
    for other_id, (other_fid, line) in ALL_LINES.items():
        if other_fid != fid:
            refs.update(operand_refs(line['expr']))
            refs.update(r if isinstance(r,str) else r['when'] for r in line.get('refuses',[]))
            if line.get('shown_when'):
                refs.add(line['shown_when'])
    return [l for l in helpers if l["id"] in refs]


def line_keys(form_doc):
    """[(log key, line id)] of the compared lines in log order: the exported lines by id, then
    (for a form) the printed computed lines by marker."""
    out = [(l["id"], l["id"]) for l in exported_lines(form_doc)]
    if form_doc["id"] not in load_defs():
        markers = marker_keys(form_doc["lines"])
        out += [(markers[l["id"]], l["id"]) for l in form_doc["lines"]
                if l["printed"] not in HELPER_PRINTED and l["expr"].get("op") != "input"]
    return out


def required_target_keys(form_doc):
    """Current log keys, including gates that older target discovery omitted."""
    keys={line['id'] for line in exported_lines(form_doc)}
    if form_doc['id'] not in load_defs():
        markers=marker_keys(form_doc['lines'])
        keys.update(markers[line['id']] for line in form_doc['lines']
                    if line['printed'] not in HELPER_PRINTED and line['expr'].get('op')!='input')
    return keys


# ---------- prompt ----------

GRAMMAR = """Expression grammar (YAML). Exactly one atom per line. Operands written as a line reference
(a string id of a line in this worksheet or another form), a constant ({const: 0} for money cents,
{const: n, type: Count} for a nonnegative whole-number count, {const: true}, {const: "single"}),
or a parameter ({param: name}). An untyped numeric constant is money cents, never a Count.
When comparing a Count line with a numeric threshold, mark the constant with type: Count.
Constants belong only in operand positions. A copy source or choose branch must be a line id
or a definition instance, not a constant/parameter object. Use op: param to define a constant helper
from the supplied parameter catalog. choose returns money; it does not select Count, Bool or Enum values.
Every test position (all/any entries, not, a choose guard or sum_over.where) requires a nested
test object. A bare Bool line id is an operand, not a test: wrap it as
{op: test, eq: [<Bool line id>, {const: true}]} (or compare with false).
sum adds money lines only; use sum_over for Count entry fields. A sum_over at return level may
read a root collection. Within a collection entry it may read only that entry's child collection;
it cannot sum another root collection. Use a published return-level aggregate where the IRS calls
for that aggregate. NonNegDollars declarations must be proved nonnegative by the expression types;
copying a Dollars input does not prove that property. Do not silently change a required result type.
subtract accepts money and always produces Dollars; it cannot subtract Counts. To work with
month counts, multiply the money amount by each count separately and subtract those money lines.
larger_of proves NonNegDollars only when every operand is already nonnegative in this checker;
use subtract_floor0 against zero when an IRS zero floor must establish a nonnegative result.

  {op: input, source: "<the box or question this value comes from>"}
  {op: copy, from: <ref>}                      # <ref> is a line id string, or for a parameterised
                                               # worksheet {def: tax_on_amount, bind: {amount: <ref>, status: <ref>}, line: tax}
  {op: param, ref: <parameter name>}
  {op: sum, of: [<ref>, ...]}
  {op: subtract, from: <ref>, take: <operand>}
  {op: subtract_floor0, from: <ref>, take: <operand>}     # if zero or less, enter -0-
  {op: smaller_of, of: [<ref>, <ref>]}
  {op: larger_of, of: [<ref>, <ref>]}
  {op: multiply_rate, amount: <ref>, rate: {param: name}, unit: <integer cents>}  # rate is a parameter; unit optional: the exact product rounded once, half-up, to that unit (100 = to the dollar); without it, half-up to the cent
  {op: multiply_count, amount: <ref>, count: <ref>}         # an amount times a whole number (a Count line), e.g. a monthly amount times months
  {op: prorate, amount: <ref>, part: <ref>, whole: <operand>, places: <int>}  # amount times (part / whole), the ratio rounded half-up to <places> decimal places and kept between 0 and 1
  {op: percent_floor, part: <ref>, whole: <operand>, cap: <int>}  # a whole-number percentage: cap + 1 when part is more than cap% of whole, else 100 x part / whole with the decimals dropped (not below 0)
  {op: keyed_lookup, table: <table id>, keys: [<ref>, ...]}  # the entry of a printed table (a rate, an amount, a number or a category) found by the values of the key lines, in the table's key order
  {op: rate_lookup, table: <table id>, key: <ref>, status: <ref>}  # the rate of a printed "Over / But not over" table for the amount on the key line; status (the filing status line) only when the table has filing-status columns
  {op: round, of: <ref>, unit: <integer cents>, rule: half_up | up | down}  # e.g. up to the next $1,000: unit 100000, rule up
  {op: table_lookup, table: tax_table, key: <ref>, status: <ref>}
  {op: sum_over, collection: <collection id>, field: <line id within the entry>, where: <test>}  # where optional
  {op: test, eq: [<operand>, <operand>]}        # also ne, lt, le, gt, ge; or {op: test, all: [<test>, ...]},
                                               # {op: test, any: [...]}, {op: test, not: <test>}
  {op: choose, alternatives: [{guard: <test>, then: <ref>}, ...]}   # guards exhaustive and disjoint

A line may also carry `refuses: [<id>, ...]`, a list of Bool inputs or lines: when any of them is true
the tool stops at this line and names the form the filer needs instead of computing it. The tool
supports only part of what some lines cover; the screening inputs listed below stand for the
situations it does not compute. Where the IRS text of a line covers such a situation, encode only the
case the tool computes and list the screening input under `refuses`, instead of adding inputs for the
unsupported amounts or writing the unsupported case as a zero.

For a consistency check on supplied figures, a refusal entry may instead be
{when: <Bool line id>, when_known: true}. A known true check still refuses, a refused gate
still propagates its refusal, and a known false check permits the expression. An unknown
consistency check is recorded as unperformed and does not block an independently determined
amount or request its missing figures. The expression must still determine its value;
this never fills an absent input with zero or false. Use ordinary refusal ids for eligibility
and scope questions that must be answered. Infer any consistency check from the source;
the project supplies no placement or formula.

Money is integer cents. Rates are parameters. There are no loops, strings, functions or arithmetic
beyond these atoms; a line that needs more than one atom is written as several lines, the extra ones
being helper lines (printed: "(helper)") with ids of your own choosing."""


def collection_notes(reviewed=None, selected=None):
    """Published collection interfaces; own computed fields are not supplied facts. With
    `selected`, only the reviewed collection and the selected others (catalog_selection)."""
    out = []
    for f, path in form_files():
        if not f.endswith(".yaml"):
            continue
        if selected is not None and f[:-5] != reviewed and f[:-5] not in selected:
            continue
        d = project_yaml(path)
        doc = d.get("form")
        if not doc or not doc.get("collection"):
            continue
        parent = doc["collection"].get("parent")
        only = listed_lines(reviewed, doc["id"], selected) if selected is not None else None
        fields = "; ".join(reference_note(doc, l) for l in doc["lines"]
                           if (doc['id'] != reviewed or l['expr'].get('op') == 'input') and (only is None or l["id"] in only))
        out.append(f"  - collection `{doc['id']}`" + (f" nested in each `{parent}` entry" if parent else "") +
                   f" — one entry per {doc['title'][:70]}; entry fields: {fields}")
    return "\n".join(out)


@cache
def implemented_atoms():
    """Use the same implemented vocabulary as the host checker, excluding reserved atoms."""
    code = 'import { IMPLEMENTED } from "./engine/dist/atoms.js"; process.stdout.write(JSON.stringify([...IMPLEMENTED]));'
    result = subprocess.run(["node", "--input-type=module", "-e", code], cwd=ROOT,
                            capture_output=True, text=True, check=True)
    return frozenset(json.loads(result.stdout))


def expression_schema():
    """Only generic syntax definitions, never authored computations or table cells."""
    schema = json.loads(open(os.path.join(ROOT, "schema", "data.schema.json"), encoding="utf-8").read())
    allowed = implemented_atoms()
    schema["$defs"]["expr"]["oneOf"] = [variant for variant in schema["$defs"]["expr"]["oneOf"]
        if variant.get("properties", {}).get("op", {}).get("const",
            "test" if variant.get("$ref") == "#/$defs/test" else None) in allowed]
    definitions = {}
    pending = ["expr"]
    while pending:
        name = pending.pop()
        if name in definitions:
            continue
        definitions[name] = schema["$defs"][name]
        pending.extend(re.findall(r'"\$ref": "#\/\$defs\/([^"/]+)"', json.dumps(definitions[name])))
    return {"$schema": schema["$schema"], "$defs": definitions, "$ref": "#/$defs/expr"}


def load_tables():
    return [project_yaml(os.path.join(str(path), name))["table"] for path in jurisdiction.read_dirs("tables", Y)
            for name in sorted(os.listdir(path)) if name.endswith(".yaml")]


def table_notes(tables=None):
    """Names and types of available table interfaces; no row data or authored expressions."""
    out = []
    for table in load_tables() if tables is None else tables:
        kind = table["kind"]
        if kind == "bracket_schedule" and kind not in implemented_atoms():
            continue  # A declared reference table does not imply an implemented lookup atom.
        if kind == "keyed":
            args = ", ".join(f"{key['name']}: {key['type']}" for key in table["keys"])
            signature = f"keyed_lookup; keys in order [{args}]; result {table['cell']}"
        elif kind == "rate_bands":
            signature = "rate_lookup; key: money" + ("; status: Enum(filing_status)" if table.get("columns") else "; omit status") + "; result Rate"
        elif kind in ("tax_table", "bracket_schedule"):
            signature = f"{kind if kind == 'bracket_schedule' else 'table_lookup'}; key: money; status: Enum(filing_status); result NonNegDollars"
        else:
            raise ValueError(f"unknown table interface kind: {kind}")
        out.append(f"  - {table['id']}: {signature}; title {table['title']!r}")
    return "\n".join(out)


# Signed Dollars interfaces whose printed line is a loss in parentheses: Schedule D lines 6 and 14
# (f1040sd p. 1) and the worksheet lines that copy line 14 (i1040sd p. 11, 28% Rate Gain Worksheet
# line 5; p. 13, Unrecaptured Section 1250 Gain Worksheet line 16). A reader holding them positive
# disagrees on every line that combines them.
NEGATIVE_INTERFACES = frozenset({"sd.line6", "sd.line14", "g28.line5", "u1250.line16"})
NEGATIVE_NOTE = "a loss carryover printed in parentheses, held as a negative amount"


def sign_note(line_id):
    return f"; {NEGATIVE_NOTE}" if line_id in NEGATIVE_INTERFACES else ""


def reference_note(doc, line):
    """Shared interface metadata, without project-written computed labels or expressions."""
    text = f"{line['id']} (form {doc['id']}; printed {str(line['printed'])!r}; type {line['type']}{sign_note(line['id'])})"
    if line["expr"].get("op") == "input":
        text += ": input " + " ".join(inline(line["expr"].get("source", "")).split())
    return text


def screen_notes():
    """Every Bool input that some line of any form names as a refusal gate, with its interface
    and the question it asks. The list is the same for every reviewed form."""
    lines = load_all_lines()
    gates = {r["when"] for _, l in lines.values() for r in (l.get("refuses") or [])}
    docs = {}
    out = []
    for g in sorted(gates):
        hit = lines.get(g)
        if hit and hit[1]["expr"].get("op") == "input":
            doc = docs.setdefault(hit[0], {"id": hit[0]})
            out.append(f"  - {reference_note(doc, hit[1])}")
    return "\n".join(out)


# ---------- other-form catalog ----------
#
# The catalog of other forms' lines is a subset chosen from the IRS source alone: what the
# excerpt given to the model shows or names, compared with each other form's own source
# pages, IRS documents and IRS title. Nothing here reads the reviewed form's expressions,
# refusal lists or visibility conditions.

# The general instructions name every form of the return: the federal Form 1040 instructions, and in New
# York mode the IT-201 instructions (PDF and web text).
CATALOG_WHOLE_TEXT_EXCLUDED = frozenset({"i1040gi", "ny_it201i", "ny_it201i-html"})
CATALOG_ID = r"(\d{3,4}(?:-[A-Z]{1,3})?|W-2|[1-3](?:-A)?|8812|SE|[A-E])"
CATALOG_NAME = re.compile(r"\b(Form|Schedule)s?\s+" + CATALOG_ID + r"\b")
CATALOG_LINE = re.compile(r"\b(Form|Schedule)\s+" + CATALOG_ID +
                          r"(?:\s+or\s+1040-SR)?(?:\s*\(Form\s+1040(?:\s+or\s+1040-SR)?\))?,?\s+lines?\s+(\d+[a-z]?)\b")
CATALOG_LINE_OF = re.compile(r"\blines?\s+(\d+[a-z]?)\s+of\s+(?:your\s+)?(Form|Schedule)\s+" + CATALOG_ID + r"\b")
CATALOG_PRODUCER = re.compile(r"\b(?:enter|include|report|carry)\w*\b[^.;]{0,100}\b(?:on|to)\s+$", re.I)
CATALOG_TITLE_LINE = re.compile(r"(?:\b(Form|Schedule)\s+" + CATALOG_ID + r",\s*)?\bLines?\s+(\d+[a-z]?)(?:\s+and\s+(\d+[a-z]?))?")


def doc_family(doc_id):
    """The IRS form an archived document belongs to: f8962 and i8962 are both 8962; the
    general Form 1040 instructions (i1040gi) and publications belong to no single form."""
    doc_id = re.sub(r"-html$", "", doc_id)
    if doc_id == "i1040gi":
        return doc_id
    if doc_id[:1] in ("f", "i") and (doc_id[1:2].isdigit() or doc_id[1:2] == "w"):
        return doc_id[1:]
    return doc_id


def named_family(kind, number, mani):
    """The family a printed name such as "Schedule 1" or "Form 8962" refers to, if archived."""
    key = number.lower().replace("-", "")
    doc = ("f" + key) if kind == "Form" else ("f1040s" + key)
    return doc_family(doc) if doc in mani or ("i" + doc[1:]) in mani else None


def named_forms(text, mani):
    return {f for kind, n in CATALOG_NAME.findall(text) if (f := named_family(kind, n, mani))}


def named_lines(text, mani, producers_only=False):
    """(family, printed line) pairs a text names, as in "Form 1040 or 1040-SR, line 2b" or "line 17
    of Schedule 1"; with producers_only, only those it says to enter an amount on."""
    flat = " ".join(text.split())
    out = set()
    for m in CATALOG_LINE.finditer(flat):
        if producers_only and not CATALOG_PRODUCER.search(flat[max(0, m.start() - 120):m.start()]):
            continue
        if (f := named_family(m.group(1), m.group(2), mani)):
            out.add((f, m.group(3)))
    if not producers_only:
        for m in CATALOG_LINE_OF.finditer(flat):
            if (f := named_family(m.group(2), m.group(3), mani)):
                out.add((f, m.group(1)))
    return out


_PROFILES = {}


def source_profile(doc, mani):
    """What the IRS source says of one other form: its source pages (the pages its own review
    would be given), the IRS forms it belongs to, the worksheet its IRS title names, and the
    form lines it feeds (from its title, "...Worksheet—Line 16", and from "enter ... on" text in
    its source pages and its own form documents)."""
    memo = (FORMS, SOURCES, doc["id"])
    if memo in _PROFILES:
        return _PROFILES[memo]
    pages = excerpt_pages(doc, mani)
    cited = {l["cite"]["doc"] for l in doc["lines"]}
    if (doc.get("collection") or {}).get("cite"):
        cited.add(doc["collection"]["cite"]["doc"])
    forms = {d for d in cited if d.startswith("f") and d in mani}
    families = {doc_family(d) for d in (forms or cited)}
    own_forms = {"f" + f for f in families if ("f" + f) in mani}
    units = [source_units(d, chosen, how, locators, mani) for d, chosen, how, locators in pages]
    text = [t for _, texts in units for t in texts]
    text += [page for d in sorted(own_forms) for page in doc_pages(mani[d])]
    head, _, tail = doc["title"].partition("—")
    worksheet = " ".join(head.split()).lower() if "Worksheet" in head else None
    fed = named_lines("\n".join(text), mani, producers_only=True)
    for kind, number, first, second in CATALOG_TITLE_LINE.findall(tail):
        family = named_family(kind, number, mani) if kind else "1040"
        fed |= {(family, n) for n in (first, second) if n}
    profile = {"pages": {k for keys, _ in units for k in keys},
               "families": families, "worksheet": worksheet, "fed": fed}
    _PROFILES[memo] = profile
    return profile


def catalog_selection(form_doc, excerpt, used, mani=None, whole_text=True, cited=None):
    """{document id: reason} for every other form, definition and collection the catalog lists.

    Chosen from the reviewed form's source only: the excerpt given to the model and the whole
    text of the archived documents it is cut from (except the general Form 1040 instructions,
    which name every form of the return):
      definition   a shared definition, always listed;
      shared page  the other form's own source pages include a page of this excerpt;
      named form   that text names an IRS form or schedule the other form belongs to;
      worksheet    that text names the IRS worksheet the other form's title names;
      named line   that text names a form line ("Form 1040, line 2b", "line 17 of Schedule 1")
                   that the other form feeds, by its IRS title or by its source's "enter ... on".
    Refusal-gate inputs are listed for every form in the screening list instead. Without
    `whole_text` (a line-scoped review), "that text" is the excerpt alone: the catalog is chosen
    from the pages given. `cited` (a line-scoped review: the document cut to the scoped lines' reach)
    narrows it as a New York catalog is narrowed, with that document's citations in place of the whole
    form's (federal_whole). Federally, a form the excerpt names only as a form is listed whole only
    where those citations name its IRS form; otherwise its input lines and the lines the excerpt names
    by form and line are listed (NAMED_FORM_INPUTS), and a collection named only as a form only by
    those named lines (NAMED_LINES). Definitions, shared pages, worksheets and named lines are listed
    as without `cited`."""
    mani = manifest() if mani is None else mani
    defs = load_defs()
    mine = {(u["doc"], p) for u in used if "lines" not in u for p in u["pages"]}
    mine |= {(u["doc"], ("line", n)) for u in used for a, b in u.get("lines", []) for n in range(a, b)}
    text = "\n".join([excerpt] + (["\n".join(doc_pages(mani[u["doc"]])) for u in used
                                   if u["doc"] not in CATALOG_WHOLE_TEXT_EXCLUDED and u["doc"] in mani] if whole_text else []))
    names = named_forms(text, mani)
    lines_named = named_lines(text, mani)
    flat = " ".join(text.split()).lower()
    out = {}
    for f, _ in form_files():
        if not f.endswith(".yaml") or f[:-5] == form_doc["id"]:
            continue
        doc = load_form(f[:-5])
        if doc["id"] in defs:
            out[doc["id"]] = "definition"
            continue
        p = source_profile(doc, mani)
        if p["pages"] & mine:
            out[doc["id"]] = "shared page"
        elif p["families"] & names:
            out[doc["id"]] = "named form"
        elif p["worksheet"] and p["worksheet"] in flat:
            out[doc["id"]] = "worksheet"
        elif p["fed"] & lines_named:
            out[doc["id"]] = "named line"
    if jurisdiction.NY or cited is not None:
        whole = federal_whole(form_doc if cited is None else cited, mani)
        inputs = {}
        if jurisdiction.NY:
            out = {d: why for d, why in out.items() if jurisdiction.is_ny(d) or d in whole}
        else:
            # A form named only as a form keeps its input lines, the return's facts the text may rely on
            # without naming a line (filing status); a collection named only as a form is not listed
            # unless a scoped line sums over it, since the model cannot write that sum without its fields.
            summed = collections_read(cited) if cited is not None else set()
            for d in [d for d, why in out.items() if why == "named form" and d not in whole]:
                doc = load_form(d)
                if doc.get("collection") and d in summed:
                    continue
                del out[d]
                if not doc.get("collection"):
                    inputs[d] = {l["id"] for l in doc["lines"] if l["expr"].get("op") == "input"}
            for d in sorted(summed - set(out)):
                if d != form_doc["id"]:
                    out[d] = SUMMED_COLLECTION
        named = federal_named(lines_named, mani)
        if jurisdiction.NY:
            for d, ids in federal_labelled(text, mani).items():
                named.setdefault(d, set()).update(ids)
        for d in sorted(set(named) | set(inputs)):
            ids = named.get(d, set()) | inputs.get(d, set())
            if d != form_doc["id"] and d not in out and ids:
                out[d] = (NAMED_FORM_INPUTS if d in inputs else NAMED_LINES) + ", ".join(sorted(ids))
    return out


# New York mode: the federal part of the catalog. The source rules above, run on New York text, name
# federal forms ("federal Form 1040", "Schedule C") whose lines a New York document does not read. So, from
# the same source text, a federal document is listed whole only where a line of the reviewed document
# states its rule on that document's own pages (cites it) or the document is a federal definition it
# instantiates; otherwise the catalog lists the federal lines the text names, reason NAMED_LINES:
#   by form and line   "federal Form 1040, line 1z" (named_lines, as the federal rule reads it);
#   by printed label   the line's printed IRS label, as a whole phrase, in a passage that names or implies
#                      the line's federal form (federal_labelled).
# A New York form copies most federal amounts by their federal labels ("Wages, salaries, tips",
# "Federal adjusted gross income") without naming the line, so both are needed.
NAMED_LINES = "named lines: "
# A line-scoped federal catalog (catalog_selection with `cited`): of a form the excerpt names only as a form,
# its input lines and the lines the excerpt names by form and line.
NAMED_FORM_INPUTS = "named form, inputs and named lines: "
# A line-scoped federal catalog: a collection a scoped line sums over, listed whole.
SUMMED_COLLECTION = "collection a scoped line sums over"


def collections_read(doc):
    """The collections a document's lines sum over (`sum_over` and other ops naming a `collection`)."""
    out = set()

    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get("collection"), str):
                out.add(x["collection"])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for l in doc.get("lines", []):
        walk(l.get("expr"))
        walk(l.get("shown_when"))
        walk(l.get("refuses"))
    return out


def federal_named(pairs, mani):
    """{federal document id: line ids} of the printed federal lines that (family, printed line) pairs name,
    a document's family being its IRS forms (source_profile)."""
    out = {}
    defs = load_defs()
    for f, _ in form_files():
        if not f.endswith(".yaml") or jurisdiction.is_ny(f[:-5]) or f[:-5] in defs:
            continue
        doc = load_form(f[:-5])
        fams = source_profile(doc, mani)["families"]
        for l in doc["lines"]:
            if l["printed"] not in HELPER_PRINTED and any((fam, str(l["printed"])) in pairs for fam in fams):
                out.setdefault(doc["id"], set()).add(l["id"])
    return out


LABEL_INSTRUCTION = re.compile(r"^(add|subtract|multiply|divide|enter|combine|attach|check|see|if|include|"
                               r"complete|use|amount|list|from)\b")
LABEL_LEAD = re.compile(r"^(this is your|these are your|this is the|these are the)\s+")


def label_norm(text):
    """Text as label matching compares it: lower case, parentheses dropped, every other character that is not a
    letter or digit a space, spaces collapsed; padded with one space each side."""
    t = re.sub(r"[()]", "", str(text).lower())
    return " " + " ".join(re.sub(r"[^a-z0-9]+", " ", t).split()) + " "


def label_phrases(label, form_text):
    """The phrases a printed federal label can be named by, each printed on the federal form's own IRS text:
    its sentences, less a lead such as "This is your" and less instruction sentences ("Add lines 1a
    through 1h", "Attach Schedule C"); a sentence ending in an abbreviation in parentheses ("Earned income
    credit (EIC)") also without it; a two-part label "IRA distributions, taxable amount" (a line and its
    sub-line) also as "taxable amount of IRA distributions". A phrase of fewer than two words is dropped."""
    out = set()
    for raw in re.split(r"[.:](?:\s+|$)", " ".join(str(label or "").split())):
        for sentence in {raw, re.sub(r"\s*\([A-Z]{2,6}\)\s*$", "", raw)}:
            sentence = LABEL_LEAD.sub("", sentence.strip().lower())
            if not sentence or LABEL_INSTRUCTION.match(sentence):
                continue
            parts = [x.strip() for x in sentence.split(",")]
            if not all(label_norm(x) in form_text for x in parts):
                continue                     # not the form's printed wording
            out.add(label_norm(sentence))
            if len(parts) == 2:
                out.add(label_norm(f"{parts[1]} of {parts[0]}"))
    return {x for x in out if len(x.split()) >= 2}


# The federal return a New York passage implies when it says "federal" without naming a form: Form 1040
# and its numbered schedules.
FEDERAL_RETURN = ("f1040", "f1040s1", "f1040s1a", "f1040s2", "f1040s3")
LABEL_WINDOW = 50        # words before a phrase that make up its passage
NEW_YORK_QUALIFIER = re.compile(r" (new york|new york state|new york city|nys|nyc|city|yonkers|state) $")
NORM_NAME = re.compile(r" (form|schedule)s? (\d{3,4}(?: [a-z]{1,3})?|w 2|[1-3](?: a)?|8812|se|[a-e])(?= )")


def passage_families(passage, mani):
    """The IRS forms a normalized passage names ("form 1040", "schedule c") or implies (FEDERAL_RETURN) by
    saying "federal" other than before a form's name ("federal Form W-2" names Form W-2)."""
    out = {f for kind, n in NORM_NAME.findall(passage)
           if (f := named_family(kind.title(), n.upper().replace(" ", "-"), mani))}
    if re.search(r" federal (?!forms? |schedules? )", passage):
        out |= {doc_family(d) for d in FEDERAL_RETURN if d in mani}
    return out


def federal_labelled(text, mani):
    """{federal document id: line ids} of the printed federal lines the text names by printed label.

    Text and labels are compared normalized (label_norm). A line's label phrases (label_phrases) are looked
    for in the text as whole phrases. An occurrence counts only where
      - its passage, the LABEL_WINDOW words before it and the phrase itself, names the line's IRS form or,
        saying "federal", implies the federal return (passage_families): the IRS form the text names or
        implies for that passage;
      - the text does not qualify it as a New York amount ("New York adjusted gross income", "New York
        State earned income credit", "city taxable income"): NEW_YORK_QUALIFIER just before it;
      - it does not lie inside a longer phrase found at the same place ("IRA distributions" inside "taxable
        amount of IRA distributions"); only the longer one counts.
    Federal definitions are not eligible."""
    flat = label_norm(text)
    starts = [m.start() for m in re.finditer(r"\S+", flat)]
    defs = load_defs()
    found = []                           # (start, end, doc id, line id, the IRS forms of the line's document)
    for f, _ in form_files():
        if not f.endswith(".yaml") or jurisdiction.is_ny(f[:-5]) or f[:-5] in defs:
            continue
        doc = load_form(f[:-5])
        fams = source_profile(doc, mani)["families"]
        form_text = label_norm(" ".join(page for fam in sorted(fams) if ("f" + fam) in mani
                                        for page in doc_pages(mani["f" + fam])))
        for l in doc["lines"]:
            if l["printed"] in HELPER_PRINTED:
                continue
            for ph in label_phrases(l.get("label"), form_text):
                start = flat.find(ph)
                while start >= 0:
                    found.append((start, start + len(ph), doc["id"], l["id"], fams))
                    start = flat.find(ph, start + 1)
    out = {}
    for a, b, d, i, fams in found:
        if any(a2 <= a and b <= b2 and b2 - a2 > b - a for a2, b2, *_ in found):
            continue
        if NEW_YORK_QUALIFIER.search(flat[max(0, a - 20):a + 1]):
            continue
        first = starts[max(0, bisect.bisect_left(starts, a + 1) - LABEL_WINDOW)]
        if fams & passage_families(flat[max(0, first - 1):b + 1], mani):
            out.setdefault(d, set()).add(i)
    return out


def federal_reads(form_doc):
    """{federal document id: line ids} of the federal lines a New York document's lines read (copies of
    federal return lines, refusal gates, visibility conditions); federal definitions excluded."""
    lines = load_all_lines()
    refs = set()
    for line in form_doc["lines"]:
        refs |= operand_refs(line.get("expr", {}))
        refs |= {r if isinstance(r, str) else r.get("when") for r in line.get("refuses") or []}
        if line.get("shown_when"):
            refs.add(line["shown_when"])
    defs = load_defs()
    out = {}
    for r in refs:
        if r in lines and not jurisdiction.is_ny(lines[r][0]) and lines[r][0] not in defs:
            out.setdefault(lines[r][0], set()).add(r)
    return out


def definition_refs(form_doc):
    """The definitions a document's lines instantiate ({def: <id>, ...})."""
    out = set()
    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get("def"), str):
                out.add(x["def"])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for line in form_doc["lines"]:
        walk(line.get("expr", {}))
    return out


def federal_whole(form_doc, mani):
    """The federal documents a New York catalog lists whole: those whose IRS forms the reviewed document's
    own citations name (a line's rule stated on the federal document), and the federal definitions it
    instantiates."""
    cited = {c["doc"] for line in form_doc["lines"] + [{"cite": c} for c in param_cites(form_doc)]
             for c in [line["cite"]] + [r["cite"] for r in line.get("refuses") or []]
             if not jurisdiction.is_ny(c["doc"])}
    families = {doc_family(d) for d in cited}
    out = definition_refs(form_doc) - {d for d in load_defs() if jurisdiction.is_ny(d)}
    if families:
        for f, _ in form_files():
            if f.endswith(".yaml") and not jurisdiction.is_ny(f[:-5]):
                doc = load_form(f[:-5])
                if source_profile(doc, mani)["families"] & families:
                    out.add(doc["id"])
    return out


NY_CATALOG_NOTE = """In this New York request the catalog above lists a federal form only by the federal lines the
New York text names, by form and line or by the line's printed label (or whole, where a line of this
document cites that federal form's own pages); a federal form the text names without naming a line,
and the federal definitions, are not listed.
"""


SCOPED_CATALOG_NOTE = """In this line-scoped request the catalog above lists a form the text names only as a form (not
by a line, worksheet or shared page) by its input lines and the lines the text names by form and line,
or whole where a line under review cites that form's own pages; such a collection is listed only by
its named lines.
"""


def ny_catalog_notes(form_doc, scope=None):
    """What build_prompt adds after the catalog: in New York mode NY_CATALOG_NOTE; federally, for a
    line-scoped request (`scope`), SCOPED_CATALOG_NOTE; otherwise ''."""
    if jurisdiction.NY:
        return "\n" + NY_CATALOG_NOTE
    return "\n" + SCOPED_CATALOG_NOTE if scope is not None else ""


def listed_lines(reviewed, doc_id, selected):
    """The lines of `doc_id` a catalog lists: all of them (None), or (NAMED_LINES, NAMED_FORM_INPUTS) only
    those its reason names."""
    why = selected.get(doc_id) or ""
    for prefix in (NAMED_LINES, NAMED_FORM_INPUTS):
        if why.startswith(prefix):
            return set(why[len(prefix):].split(", "))
    return None


def catalog_lines(reviewed, selected):
    """The other-form catalog entries ({line id: note}) of the selected non-collection forms."""
    other = {}
    for f, _ in form_files():
        if f.endswith(".yaml") and f[:-5] != reviewed and f[:-5] in selected:
            d = load_form(f[:-5])
            if d.get("collection"):
                continue   # listed with the collections instead
            only = listed_lines(reviewed, d["id"], selected)
            for l in d["lines"]:
                if only is None:
                    other[l["id"]] = reference_note(d, l)
                elif l["id"] in only:
                    other[l["id"]] = reference_note(d, l)
    return other


INPUT_CONTEXT_POLICY = input_context.POLICY
LEGACY_INPUT_CONTEXT_POLICY = "complete-input-context-v1"


def missing_input_context(prompt):
    """Legacy global-catalog diagnostic, kept separate from required-interface freshness.

    Shared-definition inputs are caller bindings, not filer questions; their bare ids
    may overlap between definitions and are not the catalog of interview inputs.
    """
    supplied = " ".join(prompt.split())
    definitions = load_defs()
    return sorted(line_id for line_id, (doc_id, line) in load_all_lines().items()
                  if doc_id not in definitions and line["expr"].get("op") == "input"
                  and " ".join(line["expr"].get("source", "").split()) not in supplied)


def gate_closure(line_id, lines, seen=None):
    """Every refusal gate that can make a line refuse: its own and those of every line it reads, across forms."""
    seen = set() if seen is None else seen
    if line_id in seen or line_id not in lines:
        return set()
    seen.add(line_id)
    l = lines[line_id][1]
    out = {r["when"] for r in (l.get("refuses") or [])}
    for ref in operand_refs(l.get("expr", {})):
        out |= gate_closure(ref, lines, seen)
    return out


def second_gates(line, by_id, seen=None):
    """Refusal gates a second transcription lists on a line and on the helper lines it reads."""
    seen = set() if seen is None else seen
    if line["id"] in seen:
        return set()
    seen.add(line["id"])
    out = {r if isinstance(r, str) else r["when"] for r in (line.get("refuses") or [])
           if isinstance(r, str) or isinstance(r, dict) and isinstance(r.get("when"), str)}
    for ref in operand_refs(line.get("expr", {})):
        if ref in by_id:
            out |= second_gates(by_id[ref], by_id, seen)
    return out


def enum_notes():
    params_doc = year_params()
    enums = (params_doc.get("params") or params_doc).get("enums", {})
    return "\n".join(f"  - Enum({name}): " + ", ".join(f'"{v}"' for v in e["values"]) for name, e in enums.items())


SHARED_NOTE = """A marker shown with a line id in parentheses is printed on more than one of the worksheets in this
document. For such a line write `printed` exactly as shown, marker and id together, give the line that id, and
reference it from other lines by that id.
"""


SHOWN_WHEN_NOTE = """`shown_when` is required on every printed line whose display the IRS text makes conditional
(the form or worksheet shows the line, or an amount on it, for some returns or entries only): give the
Bool line of this document that is true exactly when the line is shown. Leave it out only on a line
the IRS text always shows. The data-model table above calls the field optional because most lines are
always shown, not because it may be omitted where the text conditions a line."""


SCOPE_NOTE = """This is a line-scoped review: transcribe only the printed lines listed above and the result
interfaces listed below, with any helper lines they need. The document's other printed lines are
reviewed separately and are not to be transcribed here. A listed line marked "shown only when" is
skipped where its condition is false, not zeroed: its amount is still computed. A line you transcribe
that uses it only where it is completed must test that condition itself, by the id shown. Where the IRS
text of a listed line uses one of them, reference it by the id shown:
"""


def build_prompt(form_doc, excerpt, params, other_lines, param_types=None, collections=None, scope=None):
    """The transcription request. With `scope` (line ids), a line-scoped request: only those
    printed lines and result interfaces are asked for, and every other printed computed line of
    the document is listed by id, marker and type for reference."""
    lines = form_doc["lines"]
    inputs = [l for l in lines if l["expr"].get("op") == "input"]
    targets = [l for l in lines if l["printed"] not in HELPER_PRINTED and l["expr"].get("op") != "input"]
    keys = marker_keys(lines)
    shared = any(keys[l["id"]] != str(l["printed"]) for l in lines)
    printed_row = lambda l: f"  - printed {keys[l['id']]!r} (id {l['id']}; type {l['type']}{sign_note(l['id'])})"
    exported = exported_lines(form_doc)
    scope_block = ""
    if scope is not None:
        others = [l for l in targets if l["id"] not in scope]
        targets = [l for l in targets if l["id"] in scope]
        exported = [l for l in exported if l["id"] in scope]
        other_row = lambda l: printed_row(l)[:-1] + (f"; shown only when {l['shown_when']} is true, its amount computed either way)"
                                                     if l.get("shown_when") else ")")
        scope_block = "\n" + SCOPE_NOTE + ("\n".join(other_row(l) for l in others) if others else "  (none)") + "\n"
    tgt = "\n".join(printed_row(l) for l in targets) if targets or scope is None else "  (none)"
    exp = "\n".join(f"  - id {l['id']} ({l['type']})" for l in exported)
    inp = "\n".join(indent_rest(f"  - {l['id']} (printed {keys[l['id']]!r}, type {l['type']}): {l['expr'].get('source','')}", "      ")
                    for l in inputs)
    prm = "\n".join(f"  - {k} ({(param_types or {}).get(k, 'type supplied by the interface')}): {v}" for k, v in params.items())
    oth = "\n".join(f"  - {k}: {v}" for k, v in other_lines.items())
    spec = open(os.path.join(ROOT, "spec", "spec.md"), encoding="utf-8").read()
    atoms = spec[spec.index("### 4.1 Values and types"):spec.index("### 4.4 Collections")]
    contract_block = input_contracts.public_prompt(input_contracts.load(form_doc['id'], Y))
    if contract_block:
        contract_block += "\n\n"
    return jurisdiction.preface(f"""You are producing an independent transcription of the IRS worksheet or form below into a
formal data model, working ONLY from the IRS text provided here. Do not rely on memory of the tax law
or of any software; if the text does not say it, do not encode it.

# Data model (from the project specification)

{atoms}

{GRAMMAR}

Exact JSON Schema for one expression (YAML must parse to this structure):
{json.dumps(expression_schema(), separators=(',', ':'))}

# The worksheet to transcribe

Form id: {form_doc['id']}
Title: {form_doc['title']}
Tax year: {form_doc['tax_year']}

Transcribe these printed lines in this order, using each exact id shown (shared definitions
may use bare ids such as line13; do not add a form prefix to those ids):
{tgt}
{SHARED_NOTE if shared else ''}{scope_block}
The following result interfaces are required by other forms. If one is already a printed line
listed above, supply it once with that exact id and its printed marker. Otherwise supply a helper
with this exact id (printed "(helper)"). These names are not instructions for how to compute them.
Infer their meaning from the IRS pages; if the pages do not determine it, say so in a note rather
than guessing. Project-written labels and expressions are deliberately omitted:
{exp if exp else '  (none)'}

These input lines already exist and must be referenced by these exact ids (do not redefine them):
{inp if inp else '  (none)'}

This is a CLOSED input interface: do not introduce any new `op: input` line, even if the full IRS
form has additional boxes. Sources excluded by the screening questions are outside this slice;
their form lines must be represented within that declared scope, not by inventing extra inputs.
If the supplied text/interface does not determine a requested result, record that limitation in
a note rather than adding an unprovided input. Derive computed questions from the named interfaces.

Year parameters you may reference with {{param: name}} (values shown for recognition; cents or integer pairs):
{prm}

Only names in that year-parameter list may be used with `op: param` or a parameter operand.
An id listed below as a line or result interface is not a parameter; copy that line by its string id.

A parameter whose value is a dictionary keyed by filing status automatically selects the current
return's filing status and returns the amount of the declared type. Read it with `op: param` (or
as a parameter operand); do not invent a table named after the parameter. For a constant-valued
line use a declared parameter of the matching type (for example a zero-valued money parameter).
`expr: {{const: 0}}` is an operand, not a line expression; every line expression needs an `op`.

Available table interfaces (ids, ordered argument types and result types only; no table cells):
{table_notes()}
Use only these table ids. Infer which table applies from the IRS pages; the catalog does not
tell you which result should use a lookup. If no supplied table supports an instruction, note
that limitation instead of inventing a table or a new operation.

If the IRS says to STOP because no tax or credit applies, carry that condition to the requested
tax/credit/deduction result as zero; do not continue the arithmetic past that STOP or leave its
effect only in a note. If the instruction instead says to STOP and use an earlier amount, return
that amount. Derive the stopping condition from the archived text; none is supplied by the project.

Enumerations and their only permitted values (compare with {{const: "value"}}):
{enum_notes()}

Keyed collections (Form W-2s, payers, sales, gifts): a total over entries is written
{{op: sum_over, collection: <id>, field: <entry field id>, where: <test over entry fields>}}; a nested
collection is summed within each parent entry, and the parent's per-entry totals summed again:
{collection_notes(form_doc['id']) if collections is None else collections}

The computed fields of the document under review are not supplied facts. Define every computed
helper of this document that you reference in your own reply, even if a familiar name occurs
elsewhere in the catalog. Fields of another form or collection that the catalog lists are
referenced by their ids (a collection's fields through sum_over); do not redefine them. Only the
listed input lines are already provided locally. A foreign collection field cannot be
used as a return-level refusal gate without an explicitly defined, correctly bound aggregate.

Screening inputs (answered yes, the tool refuses the lines that list them under `refuses`):
{screen_notes()}

Lines on other forms you may reference by id (only where the IRS text says the value comes from
there). The catalog gives ids, printed markers and types, not their project-written computations.
It lists the other forms and collections whose own IRS pages share a page with the text below or
that this text or the IRS documents it comes from name (as a form or schedule, a worksheet, or a
line that form feeds), and every shared definition. The selection is made from the IRS documents
alone, not from this project's encoding, so a listed line is not a hint that it is needed:
{oth if oth else '  (none)'}
{ny_catalog_notes(form_doc, scope)}
{contract_block}# Output

Keep the exact declared type on every requested result id. A mathematically nonnegative result
may still have a published Dollars interface; do not replace it with NonNegDollars. Before
returning, check that each local computed reference is defined in this reply and each foreign
reference is in the supplied catalog. These are syntax/interface requirements, not tax formulas.

Return ONLY a YAML document of the form

lines:
  - id: <exact id from the required-line lists above>
    printed: "<printed>"
    label: "<the IRS wording>"
    type: <Dollars | NonNegDollars | Rate | Count | Bool | Enum(name)>
    expr: <one atom>
    refuses: [<screening input id>, ...]   # optional
    shown_when: <Bool line id of this document>   # required where the IRS text makes the line's display conditional
  - ...

plus any helper lines you need (printed: "(helper)", ids "{form_doc['id']}.h_<name>"). No prose before
or after the YAML. Where the IRS text leaves a point genuinely open, choose a reading and add a
`note:` field on that line saying what was open and what you chose.

{SHOWN_WHEN_NOTE}

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
""")


# ---------- comparison ----------

def load_form(form_id):
    d = project_yaml(form_path(form_id))
    return d.get("form") or d.get("def")


def norm_ref(ref):
    if isinstance(ref, dict) and "def" in ref:
        return {"def": ref["def"], "line": ref.get("line"), "bind": {k: v for k, v in sorted(ref.get("bind", {}).items())}}
    return ref


def load_defs():
    defs = {}
    for f, path in form_files(sort=False):
        if f.endswith(".yaml"):
            d = project_yaml(path)
            if "def" in d:
                defs[d["def"]["id"]] = d["def"]
    return defs


def load_all_lines():
    """Every line of every form, for expanding helper lines referenced across forms."""
    out = {}
    for f, path in form_files(sort=False):
        if f.endswith(".yaml"):
            d = project_yaml(path)
            doc = d.get("form") or d.get("def")
            for l in doc["lines"]:
                out[l["id"]] = (doc["id"], l)
    return out


ALL_LINES = None


COMPARISON_POLICY = "checked-expression-types-v2"
TYPE_VALIDATION_POLICY = "project-expression-types-v3"


@cache
def model_type_context():
    """Live authored interfaces for the host validator, never supplied to the model."""
    docs = [load_form(f[:-5]) for f, _ in form_files() if f.endswith(".yaml")]
    tables = load_tables()
    params = year_params()
    return {"forms": [d for d in docs if d.get("kind") != "def"],
            "defs": [d for d in docs if d.get("kind") == "def"],
            "params": params.get("params", params), "tables": tables, "register": {"entries": []}}


def validate_model_types(form_id, second_lines):
    """Reuse the build's reference/type checker without executing candidate expressions."""
    try:
        payload = json.dumps({"context": model_type_context(), "form": form_id, "lines": second_lines}, allow_nan=False)
    except ValueError:
        return [{"line": None, "message": "model contains a non-finite numeric value"}]
    result = subprocess.run(["node", os.path.join(ROOT, "tools", "transcription", "check_model_types.mjs")],
                            input=payload, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError("model type validator failed to run: " + result.stderr[-500:])
    answer = json.loads(result.stdout)
    if answer.get("policy") != TYPE_VALIDATION_POLICY or not isinstance(answer.get("errors"), list):
        raise RuntimeError("model type validator returned an invalid result")
    return answer["errors"]


def validation_dependencies(line_id, second_by_id):
    seen, remaining = set(), [line_id]
    while remaining:
        current = remaining.pop()
        if current in seen:
            continue
        seen.add(current)
        if current in second_by_id:
            remaining.extend(operand_refs(second_by_id[current]["expr"]) - seen)
    return seen


def checked_second(expression, errors, line_id, second_by_id):
    dependencies = validation_dependencies(line_id, second_by_id)
    relevant = [e for e in errors if e["line"] is None or e["line"] in dependencies]
    if relevant:
        try:
            parsed = json.loads(expression)
        except (ValueError, TypeError):
            parsed = expression
        return canonical({"invalid_model_types": relevant, "expression": parsed})
    return expression


class ComparedLines(list):
    def __init__(self, errors):
        super().__init__()
        self.validation_errors = errors


def money_zero(tree):
    """Only an untyped numeric zero; Bool false and Count zero have different units."""
    return (isinstance(tree, dict) and set(tree) == {"const"}
            and isinstance(tree["const"], (int, float)) and not isinstance(tree["const"], bool)
            and tree["const"] == 0)


class Expander:
    """Expands a line's expression into a tree over inputs, params, constants and
    references outside the form, so helper naming on either side does not matter.
    Shared parameterised definitions are inlined with their bindings substituted,
    and Boolean guards are normalised (eq-to-true, not-of-comparison)."""

    def __init__(self, form_id, lines, defs=None, bound=None, foreign=False, inputs=None, params=None, keys=None, param_types=None):
        self.form_id = form_id
        self.keys = keys or marker_keys(lines)   # line id -> the marker a reference to a printed line compares as
        self.by_id = {l["id"]: l for l in lines}
        self.printed = {l["id"]: l["printed"] for l in lines}
        self.defs = defs if defs is not None else load_defs()
        self.bound = bound or {}
        self.foreign = foreign   # expanding another form's helper: its printed lines stay qualified references
        self.inputs = inputs or {}   # the project's input lines of this form, shared by both sides
        self.params = params or {}   # parameter values, so literal-valued parameters compare as constants
        self.param_types = param_types or {}

    def inline_def(self, r, depth):
        d = self.defs.get(r["def"])
        if d is None or depth > 40:
            return {"def": r["def"], "line": r["line"], "bind": {k: self.operand(v, depth) for k, v in r["bind"].items()}}
        bound = {k: self.operand(v, depth) for k, v in r["bind"].items()}
        sub = Expander(d["id"], d["lines"], self.defs, bound, params=self.params, param_types=self.param_types)
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
                return {"const": r["const"], **({"type": r["type"]} if "type" in r else {})}
            if "param" in r:
                return self.param(r["param"])
            return {"unknown": json.dumps(r, sort_keys=True)}

        if isinstance(r, str):
            if r in self.bound:
                return self.bound[r]
            if r in self.inputs and r not in self.by_id:
                line = self.inputs[r]
                if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                    return {"line": self.keys.get(r, line["printed"])}
                return {"input": r}
            if r in self.by_id:
                line = self.by_id[r]
                if line["expr"].get("op") == "input" or depth > 40:
                    if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                        return {"ref": r} if self.foreign else {"line": self.keys.get(r, line["printed"])}
                    return {"input": r}
                # A printed line of this form is referenced by its number; helpers and
                # definition-internal lines are expanded in place.
                if line["printed"] not in HELPER_PRINTED and self.form_id not in self.defs:
                    return {"ref": r} if self.foreign else {"line": self.keys.get(r, line["printed"])}
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
                sub = Expander(other[0], [l for (fid, l) in ALL_LINES.values() if fid == other[0]], self.defs,
                               foreign=True, params=self.params, param_types=self.param_types)
                return sub.expr(other[1]["expr"], depth + 1)
            return {"ref": r}
        return {"unknown": json.dumps(r, sort_keys=True)}

    def param(self, name):
        """A parameter whose value is the literal 0 or 1 compares as that constant."""
        v = self.params.get(name)
        if v in (0, 1) and not isinstance(v, bool):
            return {"const": v, **({"type": "Count"} if self.param_types.get(name) == "Count" else {})}
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
                if money_zero(a_) and self.nonneg(b_):
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
                    if self.keys.get(l["id"], l["printed"]) == tree["line"]:
                        return l["type"] in ("Count", "NonNegDollars")
                for l in self.inputs.values():
                    if self.keys.get(l["id"], l["printed"]) == tree["line"]:
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
                    if isinstance(b_, dict) and isinstance(b_.get("const"), bool) and isinstance(a_, dict) and "test" in a_:
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
                parts = [t for t in parts if not money_zero(t)] or [{"const": 0}]
                if len(parts) == 1:
                    return parts[0]
            return {"op": op, "of": sorted(parts, key=json.dumps)}
        if op in ("subtract", "subtract_floor0"):
            return {"op": op, "from": self.ref(e["from"], depth), "take": self.operand(e["take"], depth)}
        if op == "multiply_rate":
            out = {"op": op, "amount": self.ref(e["amount"], depth), "rate": self.operand(e["rate"], depth)}
            if e.get("unit") is not None:
                out["unit"] = e.get("unit")
            return out
        if op == "percent_floor":
            return {"op": op, "part": self.ref(e["part"], depth), "whole": self.operand(e["whole"], depth), "cap": e.get("cap")}
        if op == "round":
            return {"op": op, "of": self.ref(e["of"], depth), "unit": e.get("unit"), "rule": e.get("rule")}
        if op == "multiply_count":
            return {"op": op, "amount": self.ref(e["amount"], depth), "count": self.ref(e["count"], depth)}
        if op == "prorate":
            return {"op": op, "amount": self.ref(e["amount"], depth), "part": self.ref(e["part"], depth), "whole": self.operand(e["whole"], depth), "places": e.get("places")}
        if op == "keyed_lookup":
            return {"op": op, "table": e.get("table"), "keys": [self.ref(k, depth) for k in e["keys"]]}
        if op == "rate_lookup":
            out = {"op": op, "table": e.get("table"), "key": self.ref(e["key"], depth)}
            if e.get("status") is not None:
                out["status"] = self.ref(e["status"], depth)
            return out
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


def gate_check(result, project_id, second_line, second_by_id):
    """Refusal gates are reported, not judged: the expressions decide agreement. The project often
    refuses before a worksheet is used (a gate on the line that chooses the worksheet), which no
    per-line comparison can see, so a gate the second lists that the project's line does not read
    is recorded in the log for the reviewer rather than counted as a disagreement."""
    global ALL_LINES
    ALL_LINES = ALL_LINES or load_all_lines()
    listed = sorted(second_gates(second_line, second_by_id))
    if listed:
        unread = [g for g in listed if g not in gate_closure(project_id, ALL_LINES)]
        result["gates"] = {"second": listed, "not_in_project_line": unread}
    return result


def support_lines(project_lines, second_lines, only):
    """The project's computed lines that stand in for the rest of the document beside a line-scoped
    reply (`only`: the scoped line ids): every computed line the reply does not define and that is
    not in scope. A scoped line the reply omits is not supplied, so it stays missing."""
    own = {l["id"] for l in second_lines}
    return [l for l in project_lines if l["id"] not in own and l["id"] not in only and l["expr"].get("op") != "input"]


def compare(form_id, project_lines, second_lines, only=None):
    """Compare every target line, or with `only` (line ids) those of a line-scoped review. In a
    line-scoped review the reply defines only its own lines: the project's other computed lines
    stand in for the rest when its types are checked (errors on them are not the reply's), and the
    other printed lines it references compare as those printed lines."""
    defs = load_defs()
    if form_id in defs:
        second_lines = normalize_definition_ids(form_id, project_lines, second_lines)
    if only is None:
        type_errors = validate_model_types(form_id, second_lines)
    else:
        own = {l["id"] for l in second_lines}
        support = support_lines(project_lines, second_lines, only)
        type_errors = [e for e in validate_model_types(form_id, second_lines + support) if e["line"] is None or e["line"] in own]
    params_doc = year_params()
    parameter_rows = (params_doc.get("params") or params_doc)["values"]
    pvals = {k: v["value"] for k, v in parameter_rows.items()}
    ptypes = {k: v["type"] for k, v in parameter_rows.items()}
    inputs = {l["id"]: l for l in project_lines if l["expr"].get("op") == "input"}
    pkeys = marker_keys(project_lines)
    skeys = {**{i: pkeys[i] for i in inputs}, **marker_keys(second_lines)}
    a = Expander(form_id, project_lines, defs, inputs=inputs, params=pvals, keys=pkeys, param_types=ptypes)
    b_lines = second_lines
    if only is not None and form_id not in defs:
        own = {l["id"] for l in second_lines}
        stubs = [{"id": l["id"], "printed": l["printed"], "type": l["type"], "expr": {"op": "input"}}
                 for l in project_lines if l["id"] not in own and l["id"] not in only
                 and l["printed"] not in HELPER_PRINTED and l["expr"].get("op") != "input"]
        b_lines = second_lines + stubs
        skeys.update({s["id"]: pkeys[s["id"]] for s in stubs})
    b = Expander(form_id, b_lines, defs, inputs=inputs, params=pvals, keys=skeys, param_types=ptypes)
    results = ComparedLines(type_errors)
    second_by_id = {l["id"]: l for l in second_lines}
    for l in exported_lines({"id": form_id, "lines": project_lines}):
        if only is not None and l["id"] not in only:
            continue
        pa = canonical(a.expr(l["expr"]))
        s = second_by_id.get(l["id"])
        if s is None:
            results.append({"printed": l["id"], "label": l["label"], "status": "MISSING", "project": pa, "second": None, "note": None})
            continue
        try:
            sb = canonical(b.expr(s["expr"]))
        except Exception as ex:
            sb = f"<unparseable: {ex}>"
        sb = checked_second(sb, type_errors, s["id"], second_by_id)
        results.append(gate_check({"printed": l["id"], "label": l["label"], "status": "AGREE" if pa == sb else "DISAGREE",
                        "project": pa, "second": sb, "note": s.get("note")}, l["id"], s, second_by_id))
    second_by_printed = {skeys[l["id"]]: l for l in second_lines if l["printed"] not in HELPER_PRINTED}
    is_def = form_id in defs
    for l in project_lines:
        if l["printed"] in HELPER_PRINTED or l["expr"].get("op") == "input" or is_def:
            continue
        if only is not None and l["id"] not in only:
            continue
        s = second_by_printed.get(pkeys[l["id"]])
        pa = canonical(a.expr(l["expr"]))
        if s is None:
            results.append({"printed": pkeys[l["id"]], "label": l["label"], "status": "MISSING", "project": pa, "second": None, "note": None})
            continue
        try:
            sb = canonical(b.expr(s["expr"]))
        except Exception as ex:  # malformed second transcription
            sb = f"<unparseable: {ex}>"
        sb = checked_second(sb, type_errors, s["id"], second_by_id)
        if pa == sb:
            # Equal amounts agree only where both show them: a line the project hides by its
            # shown_when is blank on the form, so a reply that would show the amount there differs.
            # The visibility is added only to such lines, so the key of every other line is unchanged.
            pv = a.ref(l["shown_when"], 0) if l.get("shown_when") else None
            sv = b.ref(s["shown_when"], 0) if s.get("shown_when") else None
            if canonical(pv) != canonical(sv):
                pa = canonical({"shown_when": pv, "value": json.loads(pa)})
                sb = canonical({"shown_when": sv, "value": json.loads(sb)})
        results.append(gate_check({"printed": pkeys[l["id"]], "label": l["label"], "status": "AGREE" if pa == sb else "DISAGREE",
                        "project": pa, "second": sb, "note": s.get("note")}, l["id"], s, second_by_id))
    extra = [p for p in second_by_printed if p not in set(pkeys.values())]
    return results, extra


def normalize_definition_ids(form_id, project_lines, second_lines):
    """A namespace prefix is not a computational disagreement.

    Only exact published definition ids can be unqualified. New helpers keep the
    model's own names, and conflicting definitions are rejected rather than merged.
    The raw response is retained unchanged alongside the comparison log.
    """
    aliases = {f"{form_id}.{l['id']}": l["id"] for l in project_lines if not l["id"].startswith(form_id + ".")}
    def refs(value):
        if isinstance(value, str):
            return aliases.get(value, value)
        if isinstance(value, list):
            return [refs(v) for v in value]
        if isinstance(value, dict):
            return {k: v if k in ("param", "source", "op", "table", "collection") else refs(v) for k, v in value.items()}
        return value
    out = [{**line, "id": aliases.get(line["id"], line["id"]), "expr": refs(line["expr"]),
            **({"refuses": refs(line["refuses"])} if "refuses" in line else {})} for line in second_lines]
    ids = [line["id"] for line in out]
    if len(set(ids)) != len(ids):
        raise ValueError("second transcription has conflicting ids after definition-namespace normalization")
    return out


# ---------- model call ----------

TRANSCRIBE_SYSTEM = jurisdiction.system("You transcribe IRS worksheets into a formal data model from the text given to you. "
                                        "You have no tools and no other sources. Output only the YAML requested.")


DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_KEYCHAIN = ("deepseek-api", os.environ.get("DEEPSEEK_KEYCHAIN_ACCOUNT") or "elliotmilco")   # macOS keychain service and account (DEEPSEEK_KEYCHAIN_ACCOUNT overrides the account)
DEEPSEEK_MAX_TOKENS = 65536
DEEPSEEK_RETRIES = 3


class MissingCredential(RuntimeError):
    """The keychain holds no API key for the hosted transport."""


LEDGER_NAME = "costs.jsonl"
RERUN_REASON_ENV = "REVIEW_RERUN_REASON"  # a forced rerun's reason, recorded in each ledger row it writes
PRICES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prices.json")
TOOL_KINDS = {"transcribe.py": "transcription", "render_compare.py": "render", "classm.py": "classm",
              "completeness_review.py": "completeness", "screen_review.py": "screen", "false_no_review.py": "false_no",
              "question_review.py": "question",
              "transcribe_tables.py": "tables", "transport_check.py": "transport-check"}


def call_model(prompt, model, timeout=900, system=TRANSCRIBE_SYSTEM, reasoning_effort=None, max_output_tokens=None,
               kind=None, subject=None, year=None, jurisdiction_id=None):
    """One fixed-prompt call; returns (text, meta). The transport follows the model name:
    `claude*` runs `claude -p` in print mode with no tools; `deepseek*` posts to DeepSeek's
    hosted OpenAI-compatible endpoint; `gpt*` runs `codex exec` in an empty read-only scratch
    directory. meta carries model_reported (a list), usage and cost_usd.

    Every call that reaches a transport appends one line to the cost ledger
    (.transcription/costs.jsonl), success or failure; the ledger never enters a prompt,
    a receipt or meta. kind and subject name the review (transcription, render, classm,
    completeness, screen, false_no) and its form; kind defaults from the calling script. year and
    jurisdiction_id (us or ny) name the tax year and jurisdiction the call is spent on; they default to
    the run's own (--year, --jurisdiction)."""
    import time
    families.require_active(model)
    families.require_selected_model(model)
    if not model.startswith("deepseek") and (reasoning_effort is not None or max_output_tokens is not None):
        raise ValueError("reasoning/output-budget options are supported only by the DeepSeek transport")
    if model.startswith("claude"):
        transport, call = "claude-print", lambda: _call_claude(prompt, model, timeout, system)
    elif model.startswith("deepseek"):
        transport, call = "deepseek", lambda: _call_deepseek(prompt, model, timeout, system, reasoning_effort, max_output_tokens)
    elif model.startswith("gpt"):
        transport, call = "codex-exec", lambda: _call_codex(prompt, model, timeout, system)
    else:
        raise ValueError(f"no transport for model {model!r}: a model name begins with 'claude', 'deepseek' or 'gpt'")
    started, clock = datetime.datetime.now(datetime.timezone.utc), time.monotonic()
    meta, outcome, text = None, "ok", None
    try:
        text, meta = call()
        if meta.get("finish_reason") == "length":
            outcome = "output-budget-exhausted"
        return text, meta
    except BaseException as ex:
        outcome = f"error: {type(ex).__name__}: {str(ex)[:200]}"
        raise
    finally:
        try:
            record_cost(started, time.monotonic() - clock, model, transport, prompt, system, meta, outcome, kind, subject,
                        response=text, year=year, jurisdiction_id=jurisdiction_id)
        except Exception as ex:  # the ledger must never lose or alter a review result
            print(f"warning: cost ledger not written: {type(ex).__name__}: {ex}", file=sys.stderr)


def load_prices():
    with open(PRICES, encoding="utf-8") as f:
        return json.load(f)


def _deepseek_peak(when, rule):
    """Whether a UTC time falls in DeepSeek's peak hours (weekday hour windows; holidays not modelled)."""
    return when.weekday() < 5 and any(start <= when.hour < end for start, end in rule["peak_hours_utc"])


def estimate_cost(model, usage, reported_cost, when, prices=None):
    """(estimated_cost_usd, price_basis) from the reported usage and prices.json; None where the
    table has no cited price for the model."""
    prices = load_prices() if prices is None else prices
    entry = prices.get("models", {}).get(model) or prices.get("families", {}).get(families.family_of(model))
    if entry is None:
        return None, "no price entry"
    basis = entry.get("basis")
    if basis == "reported":
        return reported_cost, "reported by the transport (" + entry.get("source", "") + ")"
    rates = entry.get("per_million_usd")
    if not rates or any(v is None for v in rates.values()):
        return None, "price not confirmed: " + entry.get("note", "")
    if not usage:
        return None, "no usage reported (a failed call may still have been billed)"
    if basis == "deepseek":
        hit = usage.get("prompt_cache_hit_tokens", 0) or 0
        miss = usage.get("prompt_cache_miss_tokens", (usage.get("prompt_tokens", 0) or 0) - hit) or 0
        out = usage.get("completion_tokens", 0) or 0
        peak = _deepseek_peak(when, entry)
        scale = 1 if peak else entry.get("off_peak_factor", 1)
        cost = (hit * rates["input_cache_hit"] + miss * rates["input_cache_miss"] + out * rates["output"]) * scale / 1e6
        return round(cost, 6), f"{entry['source']} ({'peak' if peak else 'off-peak'} rate)"
    if basis == "openai":
        total = usage.get("input_tokens", 0) or 0
        cached = usage.get("cached_input_tokens", 0) or 0
        out = usage.get("output_tokens", 0) or 0
        long = total > entry.get("long_context_above_input_tokens", float("inf"))
        rates = entry["long_context_per_million_usd"] if long else rates
        cost = ((total - cached) * rates["input"] + cached * rates["cached_input"] + out * rates["output"]) / 1e6
        return round(cost, 6), f"{entry['source']} ({'long' if long else 'short'} context; API list-price equivalent)"
    return None, f"unknown price basis {basis!r}"


def response_sha256(text):
    """The identity of a reply: the hash of the text as a review log embeds it (stripped at its
    edges). The ledger records it for every call that returned text, and a ruling is stamped with
    the identity of the reply it rules (rulings.section_run), which names the call that bought it."""
    return hashlib.sha256(text.strip().encode()).hexdigest()


def record_cost(started, seconds, model, transport, prompt, system, meta, outcome, kind=None, subject=None, response=None,
                year=None, jurisdiction_id=None):
    """Append one JSON line to RAW/costs.jsonl: one write() on an O_APPEND descriptor, so lines from
    concurrent processes do not interleave. The row's year (int) and jurisdiction ("us" or "ny") are
    the arguments, else the run's own: --year (taxyear.YEAR) and --jurisdiction (jurisdiction.J)."""
    year = YEAR if year is None else year
    jurisdiction_id = jurisdiction.J if jurisdiction_id is None else jurisdiction_id
    if not isinstance(year, int) or isinstance(year, bool) or jurisdiction_id not in jurisdiction.JURISDICTIONS:
        raise ValueError(f"cost row needs an integer year and a jurisdiction in {jurisdiction.JURISDICTIONS}: {year!r}, {jurisdiction_id!r}")
    tool = os.path.basename(sys.argv[0]) if sys.argv and sys.argv[0] else "-"
    meta = meta or {}
    usage = meta.get("usage") or {}
    try:
        estimated, basis = estimate_cost(model, usage, meta.get("cost_usd"), started)
    except (OSError, ValueError, KeyError, TypeError) as ex:
        estimated, basis = None, f"price table unreadable: {type(ex).__name__}"
    record = {"timestamp": started.isoformat(timespec="seconds"), "tool": tool,
              "kind": kind or TOOL_KINDS.get(tool, "unknown"), "subject": subject,
              "year": year, "jurisdiction": jurisdiction_id,
              "model_requested": model, "model_reported": meta.get("model_reported"),
              "transport": meta.get("transport", transport), "prompt_chars": len(prompt), "system_chars": len(system),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
              "response_sha256": response_sha256(response) if isinstance(response, str) else None,
              "usage": usage, "cost_usd": meta.get("cost_usd"),
              "estimated_cost_usd": estimated, "price_basis": basis,
              "duration_s": round(seconds, 3), "outcome": outcome}
    if os.environ.get(RERUN_REASON_ENV):
        record["rerun_reason"] = os.environ[RERUN_REASON_ENV]  # rerun_all.py --force-rerun
    granted = families.override()
    if granted and granted[0] == families.family_of(model) and not families.is_active(granted[0]):
        record["inactive_family_override"] = {"family": granted[0], "reason": granted[1]}
    line = (json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    os.makedirs(RAW, exist_ok=True)
    fd = os.open(os.path.join(RAW, LEDGER_NAME), os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        os.write(fd, line)
    finally:
        os.close(fd)


def _call_claude(prompt, model, timeout, system):
    cmd = ["claude", "-p", "--no-session-persistence", "--setting-sources", "", "--tools", "",
           "--permission-prompts", "none", "--output-format", "json", "--model", model,
           "--system-prompt", system]
    # A review call is one-shot: a prompt cache written for it is never read, and writing it costs more than
    # plain input, so caching is off for these calls (the prompt, model and policy are unchanged).
    env = dict(os.environ, DISABLE_PROMPT_CACHING="1")
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode}: {proc.stderr[:400]}")
    events = json.loads(proc.stdout)
    events = events if isinstance(events, list) else [events]
    result = next((e for e in events if e.get("type") == "result"), None)
    if result is None or result.get("subtype") != "success":
        raise RuntimeError(f"no successful result: {json.dumps(events)[:400]}")
    usage = result.get("modelUsage") or {}
    return result.get("result", ""), {"model_reported": list(usage.keys()), "usage": usage, "cost_usd": result.get("total_cost_usd")}


def _deepseek_key():
    """The API key, read from the keychain at call time and held only in memory: never written,
    logged, printed or exported. On failure the message names the entry and nothing else."""
    service, account = DEEPSEEK_KEYCHAIN
    try:
        proc = subprocess.run(["security", "find-generic-password", "-s", service, "-a", account, "-w"],
                              capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        proc = None
    key = proc.stdout.strip() if proc and proc.returncode == 0 else ""
    if not key:
        raise MissingCredential(f"no DeepSeek API key in the macOS keychain (service {service!r}, account {account!r}); "
                                f"add it with: security add-generic-password -s {service} -a {account} -w")
    return key


def _call_codex(prompt, model, timeout, system):
    """Run `codex exec` as a fixed-prompt transport (owner decision 2026-11-01: gpt-6 is an
    optional third family, not a required reviewer).

    Isolation: the agent runs in an empty scratch directory with `--ignore-user-config`,
    `--skip-git-repo-check` and the read-only sandbox, so no project file is in its workspace and
    it cannot write. The system prompt and the review prompt are joined, because codex has no
    separate system-prompt flag; both hashes are bound in the receipt. Codex is an agent harness,
    so the call fails closed if the event stream reports any tool activity (command execution,
    file change, MCP or web search); the reply is accepted only from agent messages. The model the
    run actually used is read from codex's own session rollout, and the rollout is deleted after
    the model is recorded so the only retained copy of the request and reply is the review's own
    raw receipt."""
    import glob, tempfile, shutil
    workdir = tempfile.mkdtemp(prefix="codex-review-")
    cmd = ["codex", "exec", "--skip-git-repo-check", "--ignore-user-config", "-s", "read-only",
           "--json", "--model", model, "-C", workdir, "-"]
    try:
        proc = subprocess.run(cmd, input=system + "\n\n" + prompt, capture_output=True, text=True,
                              timeout=timeout, cwd=workdir)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    if proc.returncode != 0:
        raise RuntimeError(f"codex exited {proc.returncode}: {(proc.stderr or proc.stdout)[:400]}")
    events = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                raise RuntimeError(f"codex emitted a non-JSON event line: {line[:200]}") from None
    thread = next((e.get("thread_id") for e in events if e.get("type") == "thread.started"), None)
    messages, tools_used = [], []
    for event in events:
        kind = event.get("type")
        item = event.get("item") or {}
        if kind in ("thread.started", "turn.started"):
            continue
        if kind == "turn.completed":
            usage = event.get("usage") or {}
            continue
        if kind == "turn.failed":
            raise RuntimeError(f"codex turn failed: {json.dumps(event)[:400]}")
        if kind in ("item.started", "item.completed", "item.updated"):
            itype = item.get("type")
            if itype == "agent_message":
                if kind == "item.completed" and item.get("text"):
                    messages.append(item["text"])
            elif itype in ("reasoning", "todo_list"):
                continue
            else:
                tools_used.append(itype or "unknown")
            continue
        if kind == "error":
            raise RuntimeError(f"codex error: {json.dumps(event)[:400]}")
        tools_used.append(kind or "unknown")
    if tools_used:
        raise RuntimeError("codex used an action outside the fixed prompt (tool events: "
                           + ", ".join(sorted(set(tools_used))) + "); the reply was rejected")
    if not messages:
        raise RuntimeError("codex returned no agent message")
    reported = []
    if thread:
        stamp = datetime.datetime.now(datetime.timezone.utc).astimezone()
        for path in glob.glob(os.path.expanduser(f"~/.codex/sessions/*/*/*/rollout-*-{thread}.jsonl")):
            try:
                found = re.findall(r'"model"\s*:\s*"([^"]+)"', open(path, encoding="utf-8").read())
            except OSError:
                found = []
            if found:
                reported = [found[0]]
            try:
                os.remove(path)
            except OSError:
                pass
    meta = {"model_reported": reported or [f"{model} (requested; codex session did not name the model)"],
            "usage": usage if "usage" in locals() else {}, "cost_usd": None,
            "transport": "codex-exec", "isolation": "empty scratch cwd, read-only sandbox, tool events rejected"}
    return "\n".join(messages), meta


def _call_deepseek(prompt, model, timeout, system, reasoning_effort=None, max_output_tokens=None):
    import time, urllib.error, urllib.request
    budget = DEEPSEEK_MAX_TOKENS if max_output_tokens is None else max_output_tokens
    if not isinstance(budget, int) or not 1 <= budget <= 384000:
        raise ValueError("DeepSeek output budget must be between 1 and 384000 tokens")
    request = {"model": model, "stream": False, "temperature": 0, "max_tokens": budget,
               "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}]}
    if reasoning_effort is not None:
        if reasoning_effort not in ("low", "high", "max"):
            raise ValueError("invalid DeepSeek reasoning effort")
        request["reasoning_effort"] = reasoning_effort
    body = json.dumps(request).encode()
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + _deepseek_key()}
    attempt = 0
    while True:
        try:
            req = urllib.request.Request(DEEPSEEK_URL, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.load(resp)
            break
        except urllib.error.HTTPError as ex:
            detail = ex.read()[:400].decode("utf-8", "replace")
            if not (ex.code == 429 or ex.code >= 500) or attempt >= DEEPSEEK_RETRIES:
                raise RuntimeError(f"deepseek HTTP {ex.code}: {detail}") from None
        except urllib.error.URLError as ex:
            if isinstance(ex.reason, TimeoutError) or attempt >= DEEPSEEK_RETRIES:
                raise RuntimeError(f"deepseek request failed: {ex.reason}") from None
        except ConnectionError as ex:
            # A peer reset can surface directly while reading the response body,
            # rather than being wrapped in URLError by urlopen.
            if attempt >= DEEPSEEK_RETRIES:
                raise RuntimeError(f"deepseek connection failed: {type(ex).__name__}") from None
        attempt += 1
        time.sleep(2 ** attempt)
    choices = data.get("choices") or []
    if not choices or choices[0].get("message", {}).get("content") is None:
        raise RuntimeError(f"deepseek returned no message content: {json.dumps(data)[:400]}")
    usage = data.get("usage") or {}
    meta = {"model_reported": [data.get("model") or model], "usage": usage, "cost_usd": None,
            "transport": "deepseek", "finish_reason": choices[0].get("finish_reason"), "attempts": attempt + 1}
    if reasoning_effort is not None:
        meta["reasoning_effort"] = reasoning_effort
    return choices[0]["message"]["content"], meta


def review_response(prompt, model, base, policy, from_response=False, system=TRANSCRIBE_SYSTEM, reasoning_effort=None, max_output_tokens=None,
                    kind=None, subject=None):
    """Bind a raw response to its actual request; a dry run never overwrites this receipt."""
    receipt = {"prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
               "system_sha256": hashlib.sha256(system.encode()).hexdigest(),
               "prompt_policy": policy, "model_requested": model, "reasoning_effort": reasoning_effort,
               "request_max_tokens": (DEEPSEEK_MAX_TOKENS if max_output_tokens is None else max_output_tokens) if model.startswith("deepseek") else None}
    if from_response:
        with open(base + ".meta.json", encoding="utf-8") as f:
            meta = json.load(f)
        with open(base + ".prompt.txt", encoding="utf-8") as f:
            saved_prompt = f.read()
        recorded = dict(meta)
        # Before this option existed every bound DeepSeek request used the fixed
        # 65536-token limit. Preserve that actual receipt; never relabel it as a
        # larger-budget call. Unbound legacy prompts still fail the other fields.
        recorded.setdefault("request_max_tokens", 65536 if model.startswith("deepseek") else None)
        if saved_prompt != prompt or any(recorded.get(k) != v for k, v in receipt.items()):
            raise ValueError("saved response belongs to a different or unrecorded prompt/model/system; run a fresh review")
        with open(base + ".response.txt", encoding="utf-8") as f:
            text = f.read()
        if meta.get("finish_reason") == "length":
            raise ValueError("saved response exhausted its output budget; run a fresh review with a larger --max-output-tokens")
        return text, meta
    budget_scale = max(1, ((max_output_tokens or DEEPSEEK_MAX_TOKENS) + DEEPSEEK_MAX_TOKENS - 1) // DEEPSEEK_MAX_TOKENS)
    text, meta = call_model(prompt, model, timeout=900 * budget_scale, system=system, reasoning_effort=reasoning_effort,
                            max_output_tokens=max_output_tokens, kind=kind, subject=subject or os.path.basename(base))
    meta = {**meta, **receipt}
    for suffix, value in ((".prompt.txt", prompt), (".response.txt", text),
                          (".meta.json", json.dumps(meta, ensure_ascii=False))):
        with open(base + suffix, "w", encoding="utf-8") as f:
            f.write(value)
    if meta.get("finish_reason") == "length":
        raise ValueError("response exhausted its output budget; raw receipt saved; run a fresh review with a larger --max-output-tokens")
    return text, meta


def extract_yaml(text):
    # A response may hold an abandoned draft block before the finished one; the answer is the last block.
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    m = blocks[-1] if blocks else None
    body = m if m is not None else text
    doc = yaml.safe_load(body)
    if not isinstance(doc, dict) or not isinstance(doc.get("lines"), list):
        raise ValueError("second transcription has no `lines`")
    seen = set()
    for l in doc["lines"]:
        if not isinstance(l, dict) or not isinstance(l.get("id"), str) or not l["id"]:
            raise ValueError("transcribed line must have a nonempty id")
        if l["id"] in seen:
            raise ValueError(f"duplicate transcribed id: {l['id']}")
        seen.add(l["id"])
        l["printed"] = str(l.get("printed", ""))
        l.setdefault("expr", {})
        if not isinstance(l.get("refuses", []), list):
            l["refuses"] = [l["refuses"]]
    return doc




# ---------- log ----------

PASS_HEADING = "## Line-scoped reviews"
# A line-scoped request's policy: lines-v1 chooses its catalog from the excerpt alone; lines-v2 also
# narrows it by the scoped lines' citations (catalog_selection with `cited`); lines-v3 also states the display
# condition of each listed unscoped line that has one. All are chosen from the source.
LINE_PROMPT_POLICY = PROMPT_POLICY + "+lines-v3"
# Line-scoped prompt policies under which a pass is as independent as a whole review under PROMPT_POLICY.
INDEPENDENT_LINE_PROMPT_POLICIES = frozenset({PROMPT_POLICY + "+lines-v1", PROMPT_POLICY + "+lines-v2",
                                                      LINE_PROMPT_POLICY})


def _review_rows(form_doc, model, prompt, used, results, extra, meta, interfaces, contract, replay_receipt=None,
                 catalog=None, h="## ", scope=None, receipt=None):
    """The record of one review: its field table, source pages, catalog, host type checks and
    partial-input checks. `h` is the heading level of its parts; `scope` and `receipt` are recorded
    for a line-scoped review."""
    fid = form_doc["id"]
    counts = {k: sum(1 for r in results if r["status"] == k) for k in ("AGREE", "DISAGREE", "MISSING")}
    type_errors = getattr(results, "validation_errors", None)
    validation = "unrecorded" if type_errors is None else "fail" if type_errors else "pass"
    out = ["| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
           *([f"| review scope | lines {', '.join(scope)} |"] if scope is not None else []),
           *(["| review provenance | verified saved-response replay; no model call |",
              f"| parent review log sha256 | {replay_receipt['parent_sha256']} |",
              f"| original review date | {replay_receipt['original_date']} |",
              f"| original comparison policy | {replay_receipt['original_comparison_policy']} |",
              f"| original type validation policy | {replay_receipt['original_type_policy']} |",
              f"| original input context policy | {replay_receipt['original_input_context_policy']} |"] if replay_receipt else []),
           f"| model requested | {model} |",
           f"| model reported | {', '.join(meta.get('model_reported', [])) or '-'} |",
           f"| prompt sha256 | {hashlib.sha256(prompt.encode()).hexdigest()} |",
           f"| prompt policy | {meta.get('prompt_policy', 'legacy-unrecorded')} |",
           f"| comparison policy | {COMPARISON_POLICY} |",
           f"| input context policy | {INPUT_CONTEXT_POLICY if interfaces else 'unrecorded'} |",
           f"| complete input context | {interfaces['state'] if interfaces else 'unrecorded'} |",
           f"| required input context sha256 | {interfaces['required_sha256'] if interfaces else '-'} |",
           f"| type validation policy | {TYPE_VALIDATION_POLICY if type_errors is not None else 'unrecorded'} |",
           f"| model type validation | {validation} |",
           *([f"| partial-input policy | {contract['policy']} |",
              f"| partial-input bank sha256 | {contract['bank_sha256']} |",
              f"| partial-input request context | {contract['request_context']} |",
              f"| partial-input result | {contract['state']} |"] if contract else []),
           f"| system sha256 | {meta.get('system_sha256', '-')} |",
           f"| reasoning effort | {meta.get('reasoning_effort') or 'provider default'} |",
           f"| output token budget | {meta.get('request_max_tokens') or 'transport default (65536 for DeepSeek)'} |",
           "| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |",
           f"| subject sha256 | {subjects.current('transcription', fid, Y)} |",
           *([f"| receipt | {receipt} |"] if receipt else []),
           f"| printed lines compared | {len(results)} |",
           f"| agree / disagree / missing | {counts['AGREE']} / {counts['DISAGREE']} / {counts['MISSING']} |",
           f"| extra printed lines in second | {', '.join(extra) if extra else 'none'} |", "",
           f"{h}Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    if catalog is not None:
        out += ["", f"{h}Other documents in the catalog", "",
                "Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.", "",
                "| reason | documents |", "| --- | --- |"]
        for reason in sorted(set(catalog.values())):
            out.append(f"| {reason} | {', '.join(sorted(k for k, v in catalog.items() if v == reason))} |")
    if type_errors:
        out += ["", f"{h}Host-side model expression type checks", "",
                "The build's reference/type checker rejected these model expressions; none were executed."]
        out.extend("- " + error["message"].replace("\n", " ") for error in type_errors)
    if contract:
        out += ["", f"{h}Source-based partial-input checks", "",
                "A fixed interpreter evaluates validated declarative IR on synthetic facts; no model-generated code or commands run. These checks earn no numeric evidence credit.",
                "", "| case | target | expected | observed | result |", "| --- | --- | --- | --- | --- |"]
        for test in contract.get("cases", []):
            for output in test["outputs"]:
                expected = json.dumps(output["expected"], sort_keys=True).replace("|", "\\|")
                actual = json.dumps(output["actual"], sort_keys=True).replace("|", "\\|")
                out.append(f"| {test['id']} | {output['target']} | {expected} | {actual} | {'MATCH' if output['pass'] else 'MISMATCH'} |")
        for error in contract.get("errors", []):
            out += ["", "Not evaluated: " + error["message"].replace("\n", " ")]
    return out, counts


def pass_tag(pass_id):
    return f"Reviewed in: pass {pass_id}"


def _sections(results, kept, pass_id=None):
    """The "### " section of each compared line; a line-scoped review tags each with its pass."""
    out = []
    tag = [pass_tag(pass_id)] if pass_id else []
    for r in results:
        out.append(f"### {r['printed']} — {summary(r['label'])[:90].rstrip()}")
        out.append(f"Status: **{r['status']}**")
        if r["status"] != "AGREE":
            out += ["", "Project:", "", "```json", r["project"], "```", "", "Second:", "", "```json", str(r["second"]), "```"]
            if r.get("note"):
                out += ["", f"Second transcription's note: {r['note']}"]
            ruling = kept.get(rulings.stored_key("transcription", (r["printed"], r["project"], str(r["second"]))), "Ruling: open")
            out += ["", ruling, *tag, ""]
        else:
            out += [*tag, ""]
    return out


GATES_HEADING = "## Refusal gates listed by the second transcription"


def _gate_rows(results):
    return [f"| {r['printed']} | {', '.join(r['gates']['second'])} | {', '.join(r['gates']['not_in_project_line']) or '-'} |"
            for r in results if r.get("gates")]


def _gates_section(rows):
    if not rows:
        return []
    return [GATES_HEADING, "",
            "Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.", "",
            "| line | gates listed | not read by the project's line |", "| --- | --- | --- |", *rows, ""]


def write_log(form_doc, model, prompt, used, results, extra, raw_text, meta, dry_run=False, replay_receipt=None, catalog=None):
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    family = families.family_of(model)
    second = extract_yaml(raw_text)["lines"]
    interfaces = input_context.assess(form_doc, second, model_type_context(), prompt) if "lines" in form_doc else None
    contract = input_contracts.assess(fid, Y, second, model_type_context(), prompt) if input_contracts.load(fid, Y) else None
    if isinstance(results, ComparedLines):
        results.contract_check = contract
        results.interface_check = interfaces
    rows, counts = _review_rows(form_doc, model, prompt, used, results, extra, meta, interfaces, contract, replay_receipt, catalog)
    out = [f"# Transcription agreement — {fid}", "",
           f"Second transcription of `{form_doc['title']}` by an isolated model (spec 6.5), compared line by line with `{jurisdiction.doc_dir('forms', Y, fid).relative_to(jurisdiction.ROOT)}/{fid}.yaml`.", "",
           *rows]
    out += ["", "## Lines", ""]
    kept = rulings.kept("transcription", fid, family, context=rulings.review_context("transcription", "\n".join(out)))
    out += _sections(results, kept)
    out += _gates_section(_gate_rows(results))
    out += subjects.table_for("transcription", fid, Y)
    out += ["## Raw second transcription", "", "```yaml", raw_text.strip(), "```", ""]
    path = rulings.log_path("transcription", fid, family)
    if not dry_run:
        rulings.write_log("transcription", fid, "\n".join(out), family)
    return path, counts


# ---------- line-scoped reviews ----------
#
# A line-scoped review asks only for some lines and merges its verdicts into the form's existing
# log. The log's header stays the record of the review it describes (so the rulings bound to that
# review's context keep their context); each line-scoped review adds a block under
# "## Line-scoped reviews" with its own record (date, model, prompt and policy hashes, source
# pages, catalog, checks, raw reply), and every section it judged carries "Reviewed in: pass <id>",
# the first 12 hex digits of its prompt hash. A ruling on such a section is bound to that block's
# context (rulings.section_context). The "## Line subjects" table is rewritten: every compared
# line's subject is then current. A block no section names any longer is dropped.

def scoped_lines(form_doc, names):
    """The line ids a line-scoped review covers: every compared line that is named (by log key or
    id), that reads a named line of the document (an input or helper included), or that reads a
    named line of another document (directly or through its own lines); and the union of the
    in-document lines those read. Raises on an unknown name."""
    global ALL_LINES
    ALL_LINES = ALL_LINES or load_all_lines()
    keys = line_keys(form_doc)
    by_key = dict(keys)
    by_id = {l["id"]: l for l in form_doc["lines"]}
    named, foreign = set(), set()
    for n in names:
        if n in by_key:
            named.add(by_key[n])
        elif n in by_id:
            named.add(n)
        elif n in ALL_LINES:
            foreign.add(n)
        else:
            raise SystemExit(f"{form_doc['id']}: {n!r} is not a line id of any document nor a compared line of the form")
    reaches = {i: subjects.reach(form_doc, i) for _, i in keys}
    reads = lambda m: {s for j in m for s in subjects._strings({k: v for k, v in by_id[j].items() if k != "id"})}
    scope = {i for i, (m, b) in reaches.items() if (m | b) & named or (foreign and reads(m) & foreign)}
    return scope, members_of(form_doc, scope)


def members_of(form_doc, ids):
    """The lines of the document a set of compared lines expand: themselves, their helpers and inputs."""
    return set().union(*(subjects.reach(form_doc, i)[0] for i in ids)) if ids else set()


def git_text(rev, rel):
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{rel}"], capture_output=True, text=True)
    return proc.stdout if proc.returncode == 0 else None


def recorded_line_subjects(kind, fid, text):
    """(({key: subject}, rest), where found) of the version a log reviewed: its line-subject table,
    or, for a log reviewed whole before tables existed, the version of the document (the working
    tree or a committed revision) whose whole subject the log records; (None, None) if neither."""
    rec = subjects.recorded(text)
    if rec is not None:
        return rec, "line-subject table"
    m = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", text, flags=re.M)
    if not m:
        return None, None
    file = subjects.path(kind, fid, Y)
    keys = subjects.target_keys(kind, fid)
    now = open(file, encoding="utf-8").read()
    if subjects.of_text(kind, now) == m.group(1):
        return subjects.line_subjects_of(kind, fid, now, keys), "working tree"
    rel = os.path.relpath(file, ROOT)
    revs = subprocess.run(["git", "-C", ROOT, "log", "--format=%H", "-n", "200", "--", rel],
                          capture_output=True, text=True).stdout.split()
    for rev in revs:
        old = git_text(rev, rel)
        if old is not None and subjects.of_text(kind, old) == m.group(1):
            return subjects.line_subjects_of(kind, fid, old, keys), f"revision {rev[:12]}"
    return None, None


def plan_scope(kind, fid, log_text, names):
    """(scope keys, reach ids or None, stale keys, keys no longer compared) for a line-scoped
    review of a log, or exits with the reason a whole review is needed."""
    rec, where = recorded_line_subjects(kind, fid, log_text)
    if rec is None:
        raise SystemExit(f"{fid}: the {kind} log records no line subjects and its subject matches no version of the "
                         "document in the working tree or recent history; run the whole review")
    rows, rest = rec
    cur, cur_rest = subjects.current_line_subjects(kind, fid, Y)
    if rest != cur_rest:
        raise SystemExit(f"{fid}: the document changed outside every compared line since the {kind} log ({where}); run the whole review")
    stale = [k for k in cur if rows.get(k) != cur[k]]
    if kind == "transcription":
        stale += [k for k in subjects.foreign_stale(fid, Y, log_text) if k not in stale]
    gone = sorted(set(rows) - set(cur))
    keys = subjects.target_keys(kind, fid)
    if names == ["auto"]:
        scope_ids = {i for k, i in keys if k in stale}
        reach = None
    elif kind == "transcription":
        scope_ids, reach = scoped_lines(load_form(fid), names)
    else:
        scope_ids, reach = names, None
    scope_keys = [k for k, i in keys if i in scope_ids]
    missing = [k for k in stale if k not in scope_keys]
    if missing:
        raise SystemExit(f"{fid}: these {kind} lines also changed since the log ({where}) and must be reviewed with it: "
                         + ", ".join(missing) + "; add them or use --lines auto")
    print(f"{fid}: line subjects from the {where}; stale: {', '.join(stale) or 'none'}"
          + (f"; no longer compared: {', '.join(gone)}" if gone else ""))
    return scope_keys, scope_ids, reach, stale, gone


def _log_parts(text, raw_heading):
    """(head, {key: section part}, section order, gate rows, {pass id: block}, raw tail) of a log."""
    head, sep, rest = text.partition("\n## Lines\n")
    if not sep:
        raise ValueError("log has no Lines section")
    at = rest.find("\n" + raw_heading + "\n")
    if at < 0:
        raise ValueError(f"log has no {raw_heading!r} section")
    pre, raw = rest[:at], rest[at:]
    ends = [i for i in (pre.find("\n" + h) for h in (GATES_HEADING, subjects.LINE_SUBJECTS + "\n", PASS_HEADING + "\n")) if i >= 0]
    end = min(ends) if ends else len(pre)
    body, extras = pre[:end], pre[end:]
    sections, order = {}, []
    for part in body.split("\n### ")[1:]:
        key = part.partition("\n")[0].split(" — ")[0]
        sections[key] = part
        order.append(key)
    gate_rows = {}
    g = extras.find("\n" + GATES_HEADING)
    if g >= 0:
        for row in re.split(r"\n## ", extras[g + 1:], maxsplit=1)[0].splitlines():
            if row.startswith("| ") and not row.startswith("| line |") and not row.startswith("| --- |"):
                gate_rows[row[2:].split(" | ")[0]] = row
    blocks = {}
    p = extras.find("\n" + PASS_HEADING + "\n")
    if p >= 0:
        for part in extras[p:].split("\n#### Pass ")[1:]:
            blocks[part.partition("\n")[0].strip()] = "#### Pass " + part.rstrip("\n")
    return head, sections, order, gate_rows, blocks, raw


TAG_RE = re.compile(r"^Reviewed in: pass ([0-9a-f]{12})$", re.M)
PASS_INTRO = ("Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or "
              "render_compare.py --lines). A section marked \"Reviewed in: pass <id>\" was judged in the pass of "
              "that id below; every other section in the review recorded at the top of this log.")


def merge_log(kind, fid, old, raw_heading, fresh, key_order, gone, block, pid, count_rows, gate_rows=None):
    """The log `old` with the sections of `fresh` ({key: section part}) replacing or adding
    those keys, the keys in `gone` dropped, sections in `key_order`, the pass `block` (lines,
    or None) added, unreferenced blocks dropped, line subjects rewritten and the header's
    count rows replaced by `count_rows(statuses)`. Rows of the header that a ruling context
    reads are never changed."""
    head, sections, order, gates, blocks, raw = _log_parts(old, raw_heading)
    sections.update(fresh)
    order = [k for k in key_order if k in sections and k not in gone]   # a line no longer compared is dropped
    sections = {k: sections[k] for k in order}
    if gate_rows is not None:
        gates = {k: v for k, v in gates.items() if k not in fresh and k in sections}
        gates.update(gate_rows)
    if block is not None:
        blocks[pid] = "\n".join(block).rstrip("\n")
    used = {m for part in sections.values() for m in TAG_RE.findall(part.split("\n## ", 1)[0])}
    blocks = {pid: b for pid, b in blocks.items() if pid in used}
    statuses = [re.search(r"^Status: \*\*(\w+)\*\*", sections[k], re.M).group(1) for k in order]
    replace = count_rows(statuses)
    for name, value in replace.items():
        head = re.sub(rf"^\| {re.escape(name)} \| .*? \|$", lambda _: f"| {name} | {value} |", head, count=1, flags=re.M)
    head = re.sub(r"^\| line-scoped reviews \| .*? \|\n", "", head, flags=re.M)
    if blocks:
        dates = sorted(re.search(r"^\| date \| (.*?) \|$", b, re.M).group(1) for b in blocks.values())
        head = re.sub(r"^(\| date \| .*? \|)$", lambda m: m.group(1) + f"\n| line-scoped reviews | {len(blocks)} (latest {dates[-1]}); see Line-scoped reviews |",
                      head, count=1, flags=re.M)
    lines_text = "".join("\n### " + sections[k] for k in order)
    tail = []
    if kind == "transcription":
        tail += _gates_section([gates[k] for k in order if k in gates])
    foreign = None
    if kind == "transcription":
        # Only the lines this review judged were asked with the current foreign interfaces.
        recorded = subjects.recorded_foreign(old) or {}
        now = subjects.current_foreign(fid, Y) if fresh and os.path.exists(subjects.path(kind, fid, Y)) else {}
        foreign = {k: now[k] if k in fresh and k in now else recorded[k] for k in order if (k in fresh and k in now) or k in recorded}
    tail += subjects.table_for(kind, fid, Y, foreign)
    if blocks:
        tail += [PASS_HEADING, "", PASS_INTRO, ""]
        for pid in sorted(blocks, key=lambda p: re.search(r"^\| date \| (.*?) \|$", blocks[p], re.M).group(1) + p):
            tail += [blocks[pid], ""]
    return head + "\n## Lines\n" + lines_text + "\n" + "\n".join(tail).rstrip("\n") + "\n" + raw


def part_of(section_lines):
    """A section as it appears between "\\n### " separators."""
    return "\n".join(section_lines)[len("### "):]


def scoped_main(a, form_doc, mani, params, values):
    """--lines: review only some lines and merge the verdicts into the existing log."""
    fid, family = a.form, families.family_of(a.model)
    path = rulings.log_path("transcription", fid, family)
    if not rulings.has_log("transcription", fid, family):
        raise SystemExit(f"{fid}: no transcription log of the {family} family to merge into; run the whole review")
    if input_contracts.load(fid, Y):
        raise SystemExit(f"{fid}: a form with source partial-input cases is reviewed whole (its cases read every line)")
    old = rulings.read_log("transcription", fid, family)
    names = [n.strip() for n in a.lines.split(",") if n.strip()]
    scope_keys, scope_ids, reach, stale, gone = plan_scope("transcription", fid, old, names)
    if reach is None:
        reach = members_of(form_doc, scope_ids)
    key_order = [k for k, _ in line_keys(form_doc)]
    if not scope_ids:
        if not gone:
            print(f"{fid}: " + ("every compared line is current; nothing to review" if names == ["auto"]
                                else f"no compared line reads {', '.join(names)}; nothing to review"))
            if subjects.recorded(old) is None:
                # Every line's subject and the rest were verified equal to the reviewed version
                # (plan_scope), so the current table records what the log reviewed.
                merged = merge_log("transcription", fid, old, "## Raw second transcription", {}, key_order, [], None, None, _transcription_counts)
                if not a.dry_run:
                    rulings.write_log("transcription", fid, merged, family)
                print(f"{fid}: recorded the line subjects the log reviewed; no model call")
            return
        merged = merge_log("transcription", fid, old, "## Raw second transcription", {}, key_order, gone, None, None,
                           _transcription_counts)
        if not a.dry_run:
            rulings.write_log("transcription", fid, merged, family)
        print(f"{fid}: dropped {', '.join(gone)}; no model call")
        return
    scoped_doc = {**form_doc, "lines": [l for l in form_doc["lines"] if l["id"] in reach]}
    excerpt, used = excerpt_for(scoped_doc, mani)
    selected = catalog_selection(form_doc, excerpt, used, mani, whole_text=False, cited=scoped_doc)
    other = catalog_lines(fid, selected)
    prompt = build_prompt(form_doc, excerpt, params, other, {k: v["type"] for k, v in values.items()},
                          collection_notes(fid, selected), scope=scope_ids)
    os.makedirs(RAW, exist_ok=True)
    tag = hashlib.sha256(",".join(sorted(scope_keys)).encode()).hexdigest()[:12]
    base = os.path.join(RAW, families.stem(fid, family) + ".lines-" + tag)
    print(f"{fid}: line-scoped review of {len(scope_keys)} compared line(s): {', '.join(scope_keys)}")
    print(f"{fid}: excerpt {len(excerpt):,} chars from " + "; ".join(f"{u['doc']} pages {u['pages']} ({u['how']})" for u in used))
    print(f"catalog: {len(selected)} other documents: " + ", ".join(f"{k} ({v})" for k, v in sorted(selected.items())))
    print(f"prompt {len(prompt):,} chars -> {os.path.relpath(base, ROOT)}{'.preview' if a.dry_run else ''}.prompt.txt")
    if a.dry_run:
        with open(base + ".preview.prompt.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        return
    text, meta = review_response(prompt, a.model, base, LINE_PROMPT_POLICY, a.from_response, reasoning_effort=a.reasoning_effort,
                                 max_output_tokens=a.max_output_tokens, kind="transcription", subject=fid)
    second = extract_yaml(text)
    results, extra = compare(fid, form_doc["lines"], second["lines"], only=scope_ids)
    assessed = {**form_doc, "lines": [l for l in form_doc["lines"] if l["id"] in reach or l["expr"].get("op") == "input"]}
    interfaces = input_context.assess(assessed, second["lines"], model_type_context(), prompt)
    results.contract_check, results.interface_check = None, interfaces
    path, counts = write_scoped(form_doc, a.model, prompt, used, results, extra, text, meta, selected, scope_keys, old,
                                key_order, gone, os.path.relpath(base, ROOT), a.from_response)
    print(f"{fid}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, missing {counts['MISSING']}, extra {len(extra)}; cost {meta.get('cost_usd')} -> {os.path.relpath(path, ROOT)}")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 and not results.validation_errors and interfaces["state"] == "pass" else 3)


def _transcription_counts(statuses):
    return {"printed lines compared": len(statuses),
            "agree / disagree / missing": " / ".join(str(statuses.count(s)) for s in ("AGREE", "DISAGREE", "MISSING"))}


def write_scoped(form_doc, model, prompt, used, results, extra, raw_text, meta, catalog, scope_keys, old, key_order, gone,
                 receipt, from_response=False):
    """Merge a line-scoped review into the existing log; returns (path, counts of this pass)."""
    fid = form_doc["id"]
    family = families.family_of(model)
    pid = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    rows, counts = _review_rows(form_doc, model, prompt, used, results, extra, meta, results.interface_check, None,
                                catalog=catalog, h="##### ", scope=scope_keys, receipt=receipt)
    if from_response:
        rows.insert(3, "| request | saved response re-read (--from-response); no model call |")
    block = [f"#### Pass {pid}", "", *rows, "", "##### Raw second transcription", "", "```yaml", raw_text.strip(), "```", ""]
    kept = rulings.kept("transcription", fid, family, context=rulings.review_context("transcription", "\n".join(block)))
    fresh = {}
    for r in results:
        fresh[r["printed"]] = part_of(_sections([r], kept, pid))
    gate_rows = {r[2:].split(" | ")[0]: r for r in _gate_rows(results)}
    merged = merge_log("transcription", fid, old, "## Raw second transcription", fresh, key_order, gone, block, pid,
                       _transcription_counts, gate_rows)
    path = rulings.log_path("transcription", fid, family)
    rulings.write_log("transcription", fid, merged, family)
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int, help="DeepSeek output budget, including reasoning (default 65536)")
    ap.add_argument("--dry-run", action="store_true", help="build the prompt and excerpt; call no model")
    ap.add_argument("--from-response", action="store_true", help="re-compare the saved response; call no model")
    ap.add_argument("--lines", help="line-scoped review merged into the existing log: comma-separated line ids or log keys "
                                    "(each with the compared lines that read it), or 'auto' for the lines whose subject changed")
    families.add_override_args(ap)
    a = ap.parse_args()
    families.apply_override(ap, a)
    mani = manifest()
    form_doc = load_form(a.form)
    params_doc = year_params()
    values = (params_doc.get("params") or params_doc)["values"]
    # The year parameters the request lists: in New York mode the New York ones (`ny.`), all a New York
    # document reads; the federal lines it copies are listed as other forms' lines.
    params = {k: v["value"] for k, v in values.items() if not jurisdiction.NY or k.startswith("ny.")}
    if a.lines:
        return scoped_main(a, form_doc, mani, params, values)
    excerpt, used = excerpt_for(form_doc, mani)
    selected = catalog_selection(form_doc, excerpt, used, mani)
    other = catalog_lines(a.form, selected)
    prompt = build_prompt(form_doc, excerpt, params, other, {k: v["type"] for k, v in values.items()},
                          collection_notes(a.form, selected))
    source_targets = exported_lines(form_doc) + [line for line in form_doc["lines"]
        if line["printed"] not in HELPER_PRINTED and line["expr"].get("op") != "input"]
    if not source_targets and adapter_contracts.excluded_ids(a.form, Y):
        print(f"{a.form}: no source-defined computed targets; adapter contract is checked separately; no model call or review assertion")
        return
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, families.stem(a.form, families.family_of(a.model)))
    print(f"{a.form}: excerpt {len(excerpt):,} chars from " + "; ".join(f"{u['doc']} pages {u['pages']} ({u['how']})" for u in used))
    print(f"catalog: {len(selected)} other documents: " + ", ".join(f"{k} ({v})" for k, v in sorted(selected.items())))
    print(f"prompt {len(prompt):,} chars -> {os.path.relpath(base, ROOT)}{'.preview' if a.dry_run else ''}.prompt.txt")
    if a.dry_run:
        with open(base + ".preview.prompt.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        return
    text, meta = review_response(prompt, a.model, base, PROMPT_POLICY, a.from_response, reasoning_effort=a.reasoning_effort,
                                 max_output_tokens=a.max_output_tokens, kind="transcription", subject=a.form)
    replay_receipt = None
    if a.from_response:
        import audit_transcription
        from pathlib import Path
        replay_receipt = audit_transcription.prepare_replay(
            Path(rulings.log_path('transcription', a.form, families.family_of(a.model))),
            prompt, text, meta, subjects.current('transcription', a.form, Y))
    second = extract_yaml(text)
    results, extra = compare(a.form, form_doc["lines"], second["lines"])
    path, counts = write_log(form_doc, a.model, prompt, used, results, extra, text, meta, replay_receipt=replay_receipt, catalog=selected)
    print(f"{a.form}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, missing {counts['MISSING']}, extra {len(extra)}; cost {meta.get('cost_usd')} -> {os.path.relpath(path, ROOT)}")
    contract_ok = not results.contract_check or (results.contract_check["state"] == "pass" and results.contract_check["request_context"] == "included")
    interfaces_ok = bool(results.interface_check and results.interface_check["state"] == "pass")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 and not results.validation_errors and contract_ok and interfaces_ok else 3)


if __name__ == "__main__":
    main()
