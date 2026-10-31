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
import argparse, datetime, hashlib, json, os, re, subprocess, sys
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
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402
SOURCES = os.path.join(ROOT, "sources", Y)
FORMS = os.path.join(ROOT, "forms", Y)
LOGS = os.path.join(ROOT, "reviews", Y, "transcription")
RAW = os.path.join(ROOT, ".transcription")
WHOLE_DOC_MAX_PAGES = 6
HELPER_PRINTED = {"(helper)", "(gate)", "(computed helper)"}
PROMPT_POLICY = "source-only-computation-v2"
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
    m = json.load(open(os.path.join(SOURCES, "manifest.json")))
    docs = m["documents"] if isinstance(m, dict) else m
    return {d["id"]: d for d in docs}


def doc_pages(doc, key="text_file"):
    text = archive_text.read(SOURCES, doc, key)
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
    params_doc = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
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


def collection_notes(reviewed=None):
    """Published collection interfaces; own computed fields are not supplied facts."""
    out = []
    for f in sorted(os.listdir(FORMS)):
        if not f.endswith(".yaml"):
            continue
        d = project_yaml(os.path.join(FORMS, f))
        doc = d.get("form")
        if not doc or not doc.get("collection"):
            continue
        parent = doc["collection"].get("parent")
        fields = "; ".join(reference_note(doc, l) for l in doc["lines"]
                           if doc['id'] != reviewed or l['expr'].get('op') == 'input')
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
    path = os.path.join(ROOT, "tables", str(Y))
    return [project_yaml(os.path.join(path, name))["table"] for name in sorted(os.listdir(path)) if name.endswith(".yaml")]


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


def reference_note(doc, line):
    """Shared interface metadata, without project-written computed labels or expressions."""
    text = f"{line['id']} (form {doc['id']}; printed {str(line['printed'])!r}; type {line['type']})"
    if line["expr"].get("op") == "input":
        text += ": input " + " ".join(line["expr"].get("source", "").split())
    return text


def screen_notes():
    """Every Bool input that some line names as a refusal gate, with the question it asks."""
    lines = load_all_lines()
    gates = {r["when"] for _, l in lines.values() for r in (l.get("refuses") or [])}
    out = []
    for g in sorted(gates):
        hit = lines.get(g)
        if hit and hit[1]["expr"].get("op") == "input":
            out.append(f"  - {g}: {' '.join(hit[1]['expr'].get('source', '').split())}")
    return "\n".join(out)


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
    params_doc = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
    enums = (params_doc.get("params") or params_doc).get("enums", {})
    return "\n".join(f"  - Enum({name}): " + ", ".join(f'"{v}"' for v in e["values"]) for name, e in enums.items())


SHARED_NOTE = """A marker shown with a line id in parentheses is printed on more than one of the worksheets in this
document. For such a line write `printed` exactly as shown, marker and id together, give the line that id, and
reference it from other lines by that id.
"""


def build_prompt(form_doc, excerpt, params, other_lines, param_types=None):
    lines = form_doc["lines"]
    inputs = [l for l in lines if l["expr"].get("op") == "input"]
    targets = [l for l in lines if l["printed"] not in HELPER_PRINTED and l["expr"].get("op") != "input"]
    keys = marker_keys(lines)
    shared = any(keys[l["id"]] != str(l["printed"]) for l in lines)
    tgt = "\n".join(f"  - printed {keys[l['id']]!r} (id {l['id']}; type {l['type']})" for l in targets)
    exported = exported_lines(form_doc)
    exp = "\n".join(f"  - id {l['id']} ({l['type']})" for l in exported)
    inp = "\n".join(f"  - {l['id']} (printed {keys[l['id']]!r}, type {l['type']}): {l['expr'].get('source','')}" for l in inputs)
    prm = "\n".join(f"  - {k} ({(param_types or {}).get(k, 'type supplied by the interface')}): {v}" for k, v in params.items())
    oth = "\n".join(f"  - {k}: {v}" for k, v in other_lines.items())
    spec = open(os.path.join(ROOT, "spec", "spec.md"), encoding="utf-8").read()
    atoms = spec[spec.index("### 4.1 Values and types"):spec.index("### 4.4 Collections")]
    contract_block = input_contracts.public_prompt(input_contracts.load(form_doc['id'], Y))
    if contract_block:
        contract_block += "\n\n"
    return f"""You are producing an independent transcription of the IRS worksheet or form below into a
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
{SHARED_NOTE if shared else ''}
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
{collection_notes(form_doc['id'])}

The computed fields of the document under review are not supplied facts. Define every computed
helper of this document that you reference in your own reply, even if a familiar name occurs
elsewhere in the catalog. Fields of another form or collection that the catalog lists are
referenced by their ids (a collection's fields through sum_over); do not redefine them. Only the
listed input lines are already provided locally. A foreign collection field cannot be
used as a return-level refusal gate without an explicitly defined, correctly bound aggregate.

Screening inputs (answered yes, the tool refuses the lines that list them under `refuses`):
{screen_notes()}

Lines on other forms you may reference by id (only where the IRS text says the value comes from
there). The catalog gives ids, printed markers and types, not their project-written computations:
{oth}

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
  - ...

plus any helper lines you need (printed: "(helper)", ids "{form_doc['id']}.h_<name>"). No prose before
or after the YAML. Where the IRS text leaves a point genuinely open, choose a reading and add a
`note:` field on that line saying what was open and what you chose.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
"""


# ---------- comparison ----------

def load_form(form_id):
    d = project_yaml(os.path.join(FORMS, form_id + ".yaml"))
    return d.get("form") or d.get("def")


def norm_ref(ref):
    if isinstance(ref, dict) and "def" in ref:
        return {"def": ref["def"], "line": ref.get("line"), "bind": {k: v for k, v in sorted(ref.get("bind", {}).items())}}
    return ref


def load_defs():
    defs = {}
    for f in os.listdir(FORMS):
        if f.endswith(".yaml"):
            d = project_yaml(os.path.join(FORMS, f))
            if "def" in d:
                defs[d["def"]["id"]] = d["def"]
    return defs


def load_all_lines():
    """Every line of every form, for expanding helper lines referenced across forms."""
    out = {}
    for f in os.listdir(FORMS):
        if f.endswith(".yaml"):
            d = project_yaml(os.path.join(FORMS, f))
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
    docs = [load_form(path[:-5]) for path in sorted(os.listdir(FORMS)) if path.endswith(".yaml")]
    tables = load_tables()
    params = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
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


def compare(form_id, project_lines, second_lines):
    defs = load_defs()
    if form_id in defs:
        second_lines = normalize_definition_ids(form_id, project_lines, second_lines)
    type_errors = validate_model_types(form_id, second_lines)
    params_doc = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
    parameter_rows = (params_doc.get("params") or params_doc)["values"]
    pvals = {k: v["value"] for k, v in parameter_rows.items()}
    ptypes = {k: v["type"] for k, v in parameter_rows.items()}
    inputs = {l["id"]: l for l in project_lines if l["expr"].get("op") == "input"}
    pkeys = marker_keys(project_lines)
    skeys = {**{i: pkeys[i] for i in inputs}, **marker_keys(second_lines)}
    a = Expander(form_id, project_lines, defs, inputs=inputs, params=pvals, keys=pkeys, param_types=ptypes)
    b = Expander(form_id, second_lines, defs, inputs=inputs, params=pvals, keys=skeys, param_types=ptypes)
    results = ComparedLines(type_errors)
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
        sb = checked_second(sb, type_errors, s["id"], second_by_id)
        results.append(gate_check({"printed": l["id"], "label": l["label"], "status": "AGREE" if pa == sb else "DISAGREE",
                        "project": pa, "second": sb, "note": s.get("note")}, l["id"], s, second_by_id))
    second_by_printed = {skeys[l["id"]]: l for l in second_lines if l["printed"] not in HELPER_PRINTED}
    is_def = form_id in defs
    for l in project_lines:
        if l["printed"] in HELPER_PRINTED or l["expr"].get("op") == "input" or is_def:
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

TRANSCRIBE_SYSTEM = ("You transcribe IRS worksheets into a formal data model from the text given to you. "
                     "You have no tools and no other sources. Output only the YAML requested.")


DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_KEYCHAIN = ("deepseek-api", "elliotmilco")   # macOS keychain service and account
DEEPSEEK_MAX_TOKENS = 65536
DEEPSEEK_RETRIES = 3


class MissingCredential(RuntimeError):
    """The keychain holds no API key for the hosted transport."""


def call_model(prompt, model, timeout=900, system=TRANSCRIBE_SYSTEM, reasoning_effort=None, max_output_tokens=None):
    """One fixed-prompt call; returns (text, meta). The transport follows the model name:
    `claude*` runs `claude -p` in print mode with no tools; `deepseek*` posts to DeepSeek's
    hosted OpenAI-compatible endpoint. meta carries model_reported (a list), usage and cost_usd."""
    families.require_selected_model(model)
    if not model.startswith("deepseek") and (reasoning_effort is not None or max_output_tokens is not None):
        raise ValueError("reasoning/output-budget options are supported only by the DeepSeek transport")
    if model.startswith("claude"):
        return _call_claude(prompt, model, timeout, system)
    if model.startswith("deepseek"):
        return _call_deepseek(prompt, model, timeout, system, reasoning_effort, max_output_tokens)
    raise ValueError(f"no transport for model {model!r}: a model name begins with 'claude' or 'deepseek'")


def _call_claude(prompt, model, timeout, system):
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


def review_response(prompt, model, base, policy, from_response=False, system=TRANSCRIBE_SYSTEM, reasoning_effort=None, max_output_tokens=None):
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
    text, meta = call_model(prompt, model, timeout=900 * budget_scale, system=system, reasoning_effort=reasoning_effort, max_output_tokens=max_output_tokens)
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

def write_log(form_doc, model, prompt, used, results, extra, raw_text, meta, dry_run=False, replay_receipt=None):
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    family = families.family_of(model)
    counts = {k: sum(1 for r in results if r["status"] == k) for k in ("AGREE", "DISAGREE", "MISSING")}
    type_errors = getattr(results, "validation_errors", None)
    validation = "unrecorded" if type_errors is None else "fail" if type_errors else "pass"
    second = extract_yaml(raw_text)["lines"]
    interfaces = input_context.assess(form_doc, second, model_type_context(), prompt) if "lines" in form_doc else None
    contract = input_contracts.assess(fid, Y, second, model_type_context(), prompt) if input_contracts.load(fid, Y) else None
    if isinstance(results, ComparedLines):
        results.contract_check = contract
        results.interface_check = interfaces
    out = [f"# Transcription agreement — {fid}", "",
           f"Second transcription of `{form_doc['title']}` by an isolated model (spec 6.5), compared line by line with `forms/{Y}/{fid}.yaml`.", "",
           "| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
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
           f"| printed lines compared | {len(results)} |",
           f"| agree / disagree / missing | {counts['AGREE']} / {counts['DISAGREE']} / {counts['MISSING']} |",
           f"| extra printed lines in second | {', '.join(extra) if extra else 'none'} |", "",
           "## Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    if type_errors:
        out += ["", "## Host-side model expression type checks", "",
                "The build's reference/type checker rejected these model expressions; none were executed."]
        out.extend("- " + error["message"].replace("\n", " ") for error in type_errors)
    if contract:
        out += ["", "## Source-based partial-input checks", "",
                "A fixed interpreter evaluates validated declarative IR on synthetic facts; no model-generated code or commands run. These checks earn no numeric evidence credit.",
                "", "| case | target | expected | observed | result |", "| --- | --- | --- | --- | --- |"]
        for test in contract.get("cases", []):
            for output in test["outputs"]:
                expected = json.dumps(output["expected"], sort_keys=True).replace("|", "\\|")
                actual = json.dumps(output["actual"], sort_keys=True).replace("|", "\\|")
                out.append(f"| {test['id']} | {output['target']} | {expected} | {actual} | {'MATCH' if output['pass'] else 'MISMATCH'} |")
        for error in contract.get("errors", []):
            out += ["", "Not evaluated: " + error["message"].replace("\n", " ")]
    out += ["", "## Lines", ""]
    kept = rulings.kept("transcription", fid, family, context=rulings.review_context("transcription", "\n".join(out)))
    for r in results:
        out.append(f"### {r['printed']} — {r['label'][:90].rstrip()}")
        out.append(f"Status: **{r['status']}**")
        if r["status"] != "AGREE":
            out += ["", "Project:", "", "```json", r["project"], "```", "", "Second:", "", "```json", str(r["second"]), "```"]
            if r.get("note"):
                out += ["", f"Second transcription's note: {r['note']}"]
            ruling = kept.get((r["printed"], r["project"], str(r["second"])), "Ruling: open")
            out += ["", ruling, ""]
        else:
            out.append("")
    gated = [r for r in results if r.get("gates")]
    if gated:
        out += ["## Refusal gates listed by the second transcription", "",
                "Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.", "",
                "| line | gates listed | not read by the project's line |", "| --- | --- | --- |"]
        for r in gated:
            out.append(f"| {r['printed']} | {', '.join(r['gates']['second'])} | {', '.join(r['gates']['not_in_project_line']) or '-'} |")
        out.append("")
    out += ["## Raw second transcription", "", "```yaml", raw_text.strip(), "```", ""]
    path = rulings.log_path("transcription", fid, family)
    if not dry_run:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int, help="DeepSeek output budget, including reasoning (default 65536)")
    ap.add_argument("--dry-run", action="store_true", help="build the prompt and excerpt; call no model")
    ap.add_argument("--from-response", action="store_true", help="re-compare the saved response; call no model")
    a = ap.parse_args()
    mani = manifest()
    form_doc = load_form(a.form)
    excerpt, used = excerpt_for(form_doc, mani)
    params_doc = project_yaml(os.path.join(ROOT, "params", f"{Y}.yaml"))
    values = (params_doc.get("params") or params_doc)["values"]
    params = {k: v["value"] for k, v in values.items()}
    other = {}
    for f in sorted(os.listdir(FORMS)):
        if f.endswith(".yaml") and f[:-5] != a.form:
            d = load_form(f[:-5])
            if d.get("collection"):
                continue   # listed with the collections instead
            for l in d["lines"]:
                other[l["id"]] = reference_note(d, l)
    prompt = build_prompt(form_doc, excerpt, params, other, {k: v["type"] for k, v in values.items()})
    source_targets = exported_lines(form_doc) + [line for line in form_doc["lines"]
        if line["printed"] not in HELPER_PRINTED and line["expr"].get("op") != "input"]
    if not source_targets and adapter_contracts.excluded_ids(a.form, Y):
        print(f"{a.form}: no source-defined computed targets; adapter contract is checked separately; no model call or review assertion")
        return
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, families.stem(a.form, families.family_of(a.model)))
    print(f"{a.form}: excerpt {len(excerpt):,} chars from " + "; ".join(f"{u['doc']} pages {u['pages']} ({u['how']})" for u in used))
    print(f"prompt {len(prompt):,} chars -> {os.path.relpath(base, ROOT)}{'.preview' if a.dry_run else ''}.prompt.txt")
    if a.dry_run:
        with open(base + ".preview.prompt.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        return
    text, meta = review_response(prompt, a.model, base, PROMPT_POLICY, a.from_response, reasoning_effort=a.reasoning_effort, max_output_tokens=a.max_output_tokens)
    replay_receipt = None
    if a.from_response:
        import audit_transcription
        from pathlib import Path
        replay_receipt = audit_transcription.prepare_replay(
            Path(rulings.log_path('transcription', a.form, families.family_of(a.model))),
            prompt, text, meta, subjects.current('transcription', a.form, Y))
    second = extract_yaml(text)
    results, extra = compare(a.form, form_doc["lines"], second["lines"])
    path, counts = write_log(form_doc, a.model, prompt, used, results, extra, text, meta, replay_receipt=replay_receipt)
    print(f"{a.form}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, missing {counts['MISSING']}, extra {len(extra)}; cost {meta.get('cost_usd')} -> {os.path.relpath(path, ROOT)}")
    contract_ok = not results.contract_check or (results.contract_check["state"] == "pass" and results.contract_check["request_context"] == "included")
    interfaces_ok = bool(results.interface_check and results.interface_check["state"] == "pass")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 and not results.validation_errors and contract_ok and interfaces_ok else 3)


if __name__ == "__main__":
    main()
