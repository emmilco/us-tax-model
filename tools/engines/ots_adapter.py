#!/usr/bin/env python3
"""OpenTaxSolver (OTS) as an engine for the differential: one text input file per form, filled
from the shipped templates, run through the per-form C programs, and read back from
`<input>_out.txt`.

OTS has no API: `taxsolve_US_1040_<year>` computes Form 1040 with Schedules 1, 1-A, 2, 3, A, B,
D, Form 8949, the Qualified Dividends and Capital Gain Tax Worksheet, the Schedule D Tax
Worksheet, the Social Security Benefits Worksheet and the student loan interest worksheet; the
other forms are separate programs whose results the user carries over by hand. The adapter
does that carrying: it runs the programs in dependency order (Schedule C, Schedule SE, Form
8889, Form 8959, Form 1040, Form 8960, Form 8995, Form 1040 again, Form 2441, Schedule 8812,
Form 1040 a third time) and feeds each program's own output into the next. Every input it
supplies that the project computes rather than receives is declared in OTS_PASS_THROUGH.

The input grammar is positional (each key must appear in template order), so an input is the
template with values substituted by key, never a composed file. Programs run with the working
directory outside the OTS tree, with paths as arguments. Money is read as doubles and printed
to two decimals (`%6.2f`); nothing is rounded unless asked, so the engine's precision is
"decimal2": fractions of a cent carried through the arithmetic and rounded only when printed.
"""
import glob
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OTS_SRC = ROOT / ".engines" / "opentaxsolver-src"
ENGINE_NAME = "OpenTaxSolver"


def cents(x):
    return int(round(float(x) * 100))


def money(c):
    """Integer cents as the decimal string OTS reads (exact: no binary fraction is involved)."""
    sign = "-" if c < 0 else ""
    c = abs(int(c))
    return f"{sign}{c // 100}.{c % 100:02d}"


# ---------------------------------------------------------------------------------------------
# Package discovery and version


def package_dir():
    """The extracted OTS package: the directory under .engines/opentaxsolver-src/ holding bin/
    and tax_form_files/, the newest by name when several are extracted. None when the package
    is not installed or not built."""
    for d in sorted(glob.glob(str(OTS_SRC / "OpenTaxSolver*")), reverse=True):
        p = Path(d)
        if p.is_dir() and (p / "bin").is_dir() and (p / "tax_form_files").is_dir():
            return p
    return None


def package_version(pkg):
    """The package version from 0_README.txt ("... vNN.NN - For Tax-Year YYYY"), and the version
    the Form 1040 program prints about itself, which has lagged the package."""
    readme = (pkg / "0_README.txt").read_text(errors="replace") if (pkg / "0_README.txt").exists() else ""
    m = re.search(r"\bv(\d+\.\d+)\b", readme)
    pkg_version = m.group(1) if m else "unknown"
    try:
        out = subprocess.run([str(pkg / "bin" / f"taxsolve_US_1040_{YEAR_TAG}")], capture_output=True, text=True, cwd="/")
        m = re.search(r"\bv(\d+\.\d+)\b", out.stdout + out.stderr)
        bin_version = m.group(1) if m else "unknown"
    except OSError:
        bin_version = "not runnable"
    return pkg_version, bin_version


def is_available():
    pkg = package_dir()
    return pkg is not None and os.access(pkg / "bin" / f"taxsolve_US_1040_{YEAR_TAG}", os.X_OK)


def available(year):
    """Whether the package is installed and built for this tax year (run.sh's skip check)."""
    configure(year)
    return is_available()


# The tax year the shipped programs are built for is part of their names and titles.
YEAR_TAG = None


def configure(year):
    global YEAR_TAG
    YEAR_TAG = str(year)


# ---------------------------------------------------------------------------------------------
# Template filling

def _strip_comments(line):
    return re.sub(r"\{[^}]*\}?", "", line)


def fill_template(text, values):
    """The template with each key in `values` given its value, every other key left as shipped.

    A key line is the first token of a line (outside comments). A key terminated by `;` on the
    same line, or on the following line(s), is a money key and is written `KEY value ;`; any
    other key (text with a trailing colon, a yes/no answer, a bare word) is written `KEY value`.
    A list value writes one entry per line (Form 8949 rows) before the `;`; None writes the key
    alone, keeping only its comment (for a template line whose own text misleads the program)."""
    lines = text.split("\n")
    out, i = [], 0
    pending = dict(values)
    while i < len(lines):
        raw = lines[i]
        bare = _strip_comments(raw).strip()
        key = bare.split()[0] if bare else None
        if key is None or key not in pending:
            out.append(raw)
            i += 1
            continue
        val = pending.pop(key)
        # Where does this key's value end? On this line if it holds ';'; else on a later line
        # made only of ';' (multi-value keys); else this line alone.
        money_key = ";" in bare
        j = i + 1
        if not money_key:
            k = i + 1
            while k < len(lines) and _strip_comments(lines[k]).strip() == "":
                k += 1
            if k < len(lines) and _strip_comments(lines[k]).strip() == ";":
                money_key = True
                j = k + 1
        # The key line's comment is kept: a brace opened there may close on a later line.
        tail = raw[raw.index("{"):] if "{" in raw else ""
        if val is None:
            out.append(f"{key}\t{tail}")
        elif isinstance(val, list):
            out.append(f"{key}\t{tail}")
            out.extend("\t" + v for v in val)
            out.append("\t;")
        elif money_key:
            out.append(f"{key}\t{val} ;\t{tail}")
        else:
            out.append(f"{key}\t{val}\t{tail}")
        i = j
    if pending:
        raise KeyError(f"keys not in template: {sorted(pending)}")
    return "\n".join(out)


def parse_output(text):
    """Every `LABEL = value` line as {label: cents}, the first occurrence winning (OTS repeats a
    few labels), plus the worksheet lines under synthetic labels: QDCG<N>, SDTW<N>, SSB<N>,
    STTD<N>. Checked answers ("SocSecWorkSheet[7]: Check 'No'") give SSB<N>=0. Non-money
    integers (counts, the Schedule 1-A whole-dollar steps) are kept as cents of whole dollars.
    `prose` holds the lines that are not labels, for the standard deduction and decisions."""
    vals, prose, prev = {}, [], None
    for line in text.split("\n"):
        m = re.match(r"^\s*([A-Za-z][A-Za-z0-9_\-/]*)\s*=\s*(-?\d+(?:\.\d+)?)\b", line)
        if m:
            label, value = m.group(1), cents(m.group(2))
            # Schedule 1 line 21 is echoed as entered (the interest paid) when read and printed again,
            # only when nonzero, as the worksheet result just before line 22 in the summary block.
            if label == "S1_22":
                vals["S1_21_computed"] = prev[1] if prev and prev[0] == "S1_21" else 0
            vals.setdefault(label, value)
            prev = (label, value)
            continue
        m = re.match(r"^\s*Qual\. Div & Gains WorkSheet (\d+):\s*(-?\d+(?:\.\d+)?)", line)
        if m:
            vals.setdefault(f"QDCG{m.group(1)}", cents(m.group(2)))
            continue
        m = re.match(r"^\s*Sched-D tax Worksheet line (\d+) =\s*(-?\d+(?:\.\d+)?)", line)
        if m:
            vals.setdefault(f"SDTW{m.group(1)}", cents(m.group(2)))
            continue
        m = re.match(r"^\s*SocSecWorkSheet\[(\d+)\] =\s*(-?\d+(?:\.\d+)?)", line)
        if m:
            vals.setdefault(f"SSB{m.group(1)}", cents(m.group(2)))
            continue
        m = re.match(r"^\s*SocSecWorkSheet\[(\d+)\]: Check 'No'", line)
        if m:
            vals.setdefault(f"SSB{m.group(1)}", 0)
            vals["SSB_STOP"] = int(m.group(1))
            continue
        m = re.match(r"^\s*Sched-A STTD ws\[(\d+)\] =\s*(-?\d+(?:\.\d+)?)", line)
        if m:
            vals.setdefault(f"STTD{m.group(1)}", cents(m.group(2)))
            continue
        prose.append(line)
    return vals, prose


# ---------------------------------------------------------------------------------------------
# Running a program

class OtsError(Exception):
    pass


def run_program(pkg, program, template_rel, values, workdir, name):
    """Fill the template, run the program from `workdir` (outside the OTS tree), and parse its
    output file. Returns (values, prose, output_path)."""
    template = (pkg / "tax_form_files" / template_rel).read_text(errors="replace")
    inp = workdir / f"{name}.txt"
    inp.write_text(fill_template(template, values))
    binary = pkg / "bin" / program
    r = subprocess.run([str(binary), str(inp)], capture_output=True, text=True, cwd=str(workdir))
    out_path = workdir / f"{name}_out.txt"
    if r.returncode != 0 or not out_path.exists():
        raise OtsError(f"{program} exit {r.returncode}: {(r.stdout + r.stderr)[-600:]}")
    text = out_path.read_text(errors="replace")
    if re.search(r"^ERROR", text, re.M) or "ERROR:" in r.stdout:
        raise OtsError(f"{program}: {[l for l in (text + r.stdout).split(chr(10)) if 'ERROR' in l][:3]}")
    vals, prose = parse_output(text)
    return vals, prose, out_path


STATUS = {"single": "Single", "mfj": "Married/Joint", "hoh": "Head_of_House", "mfs": "Married/Sep", "qss": "Widow(er)"}
TAXPAYER = "person[taxpayer]"
HSA = f"{TAXPAYER}.f8889[hsa]"


def yn(b):
    return "Y" if b else "N"


# A text key with nothing after it on its line makes the parser read the next line as its text,
# so the identity lines the templates leave blank are always given a value.
IDENT = {"YourName:": "Generated Case", "YourSocSec#:": "123-45-6789"}


def w2_sum(inputs, person, box):
    return sum(inputs.get(f"{person}.w2[{k}].{box}", 0) for k in inputs.get(f"$w2@{person}", []))


def net_capital_gain(f):
    """Form 8995 line 12 from the facts: the excess of net long-term gain over net short-term
    loss, not below zero, plus qualified dividends. Supplied, not computed by the engine."""
    lt = f["long_term_gain"] + f["capital_gain_distributions"] - f.get("capital_loss_carryover_lt", 0)
    st = f["short_term_gain"] - f.get("capital_loss_carryover_st", 0)
    ncg = max(0, lt + min(st, 0)) if lt > 0 else 0
    return ncg + f["qualified_dividends"]


def sales_entries(inputs, boxes):
    """Form 8949 rows for the OTS `CapGains-X/Y` key: `basis date proceeds date code amount`,
    with `various-short`/`various-long` as the acquisition date and `~ ~` for no adjustment.
    OTS adds the basis as entered; a wash-sale disallowed loss (code W) is the adjustment."""
    rows = []
    for s in inputs.get("$sales", []):
        key = f"sales[{s}]"
        if inputs[f"{key}.box"] not in boxes:
            continue
        term = "various-short" if inputs[f"{key}.box"] in ("A", "B", "C") else "various-long"
        code, amt = ("W", money(inputs[f"{key}.wash_loss"])) if inputs[f"{key}.code"] == "W" else ("~", "~")
        rows.append(f"-{money(inputs[f'{key}.reported_basis'])} {term}  {money(inputs[f'{key}.proceeds'])} 12-31-{YEAR_TAG}  {code} {amt}")
    return rows


def run_case(pkg, case, workdir):
    """All OTS programs for one generated return. Returns {project line id: cents} and the set of
    engine-side features (facts about this run the comparison needs, such as an AMT computed)."""
    f, inputs = case["facts"], case["inputs"]
    status = inputs["f1040.status"]
    joint = bool(f.get("joint"))
    lines, feats = {}, set()
    children = f.get("children", [])
    out = {}

    # --- Schedule C and Schedule SE (one business, the filer's) ---
    se_income = f.get("self_employment_income", 0)
    sc_out = se_out = None
    if se_income:
        pre = f"{TAXPAYER}.sc[biz]"
        c_vals, _, sc_out = run_program(pkg, f"taxsolve_US_1040_Sched_C_{YEAR_TAG}", f"US_1040_Sched_C/US_1040Sched_C_{YEAR_TAG}_template.txt",
                                        {**IDENT, "PrincipalBus:": "Services", "BusinessName:": "Biz", "Fmethod:": "Cash", "GPartic:": "Yes",
                                         "Hacquired:": "No", "Ireq1099s:": "No", "Jfile1099s:": "n/a",
                                         "L1": money(inputs[f"{pre}.line1"]), "L18": money(inputs[f"{pre}.line18"]), "L32a": "Yes"},
                                        workdir, "sched_c")
        for n in ("7", "28", "29", "31"):
            lines[f"{pre}.line{n}"] = c_vals[f"L{n}"]
        se_vals, _, se_out = run_program(pkg, f"taxsolve_US_1040_Sched_SE_{YEAR_TAG}", "US_1040_Sched_SE/US_1040_Sched_SE_template.txt",
                                         {**IDENT, "L2": money(c_vals["L31"]), "L8a": money(w2_sum(inputs, TAXPAYER, "box3") + w2_sum(inputs, TAXPAYER, "box7"))},
                                         workdir, "sched_se")
        # The program stops before line 4c when net earnings are under $400: those lines are zero.
        for lab, pid in (("L4c", "se_line4c"), ("L6", "se_line6"), ("L12", "se_line12"), ("L13", "se_line13")):
            lines[f"{TAXPAYER}.{pid}"] = se_vals.get(lab, 0)
        se_l6, se_l12, se_l13, se_l3 = se_vals.get("L6", 0), se_vals.get("L12", 0), se_vals.get("L13", 0), se_vals.get("L3", 0)
    else:
        se_l6 = se_l12 = se_l13 = se_l3 = 0

    # --- Form 8889 (the filer's one account; line 3 limit supplied from the coverage facts) ---
    hsa_l13 = 0
    if "hsa" in case["features"]:
        family = inputs.get(f"{HSA}.months_family", 0) == 12
        h_vals, _, _ = run_program(pkg, "taxsolve_HSA_f8889", "HSA_Form_8889/HSA_Form_8889_template.txt",
                                   {**IDENT, "L1:": "Family" if family else "Self-Only", "L2": money(inputs[f"{HSA}.line2"]),
                                    "L3": money(855000 if family else 430000), "L7": money(100000 if inputs.get(f"{HSA}.age55") else 0),
                                    "L9": money(inputs[f"{HSA}.line9"])},
                                   workdir, "f8889")
        hsa_l13 = h_vals["L13"]
        lines[f"{HSA}.line12"] = h_vals["L12"]
        lines[f"{HSA}.line13"] = h_vals["L13"]

    # --- Form 8959 (Medicare wages of both spouses; SE income from Schedule SE line 6) ---
    box6 = w2_sum(inputs, TAXPAYER, "box6") + (w2_sum(inputs, "person[spouse]", "box6") if joint else 0)
    m_vals, _, _ = run_program(pkg, f"taxsolve_f8959_{YEAR_TAG}", "Form_8959/Form_8959_template.txt",
                               {**IDENT, "Status": STATUS[status], "L1": money(f["medicare_wages"]), "L8": money(max(0, se_l6)), "L19": money(box6)},
                               workdir, "f8959")
    for n in ("7", "13", "17", "18", "21", "22", "24"):
        lines[f"f8959.line{n}"] = m_vals[f"L{n}"]
    lines["f8959.tax"] = m_vals["L18"]

    # --- Last year's return for the Capital Loss Carryover Worksheet ---
    # OTS reads the 2024 figures from a prior-year output file named on line D6 and runs the worksheet itself.
    # The file is written with the five figures the worksheet reads; line 15 is the signed amount the worksheet
    # asks for (2024 line 11 less line 14), not the floored line an OTS 2024 output would print.
    prior_file = None
    if f.get("prior_year"):
        py = f["prior_year"]
        prior_file = Path(workdir) / "prior_year_out.txt"
        prior_file.write_text("".join(f"{k} = {money(v)}\n" for k, v in (
            ("L15", py["line15"]), ("D7", py["sd7"]), ("D15", py["sd15"]), ("D16", py["sd7"] + py["sd15"]), ("D21", -py["sd21"]))))
    invest = f["investment_interest"] + f.get("investment_interest_carryover", 0)

    # --- Form 1040, pass 1 ---
    def f1040_values(l13a, l19, l28, s2_12, s3_1, s3_2):
        v = {
            "Status": STATUS[status], "You_65+Over?": yn(inputs.get(f"{TAXPAYER}.age65")), "You_Blind?": "N",
            "Spouse_65+Over?": yn(joint and inputs.get("person[spouse].age65")), "Spouse_Blind?": "N",
            "Dependents": str(len(children)), "CkHomeInUS": "Y", "VirtCurr?": "N",
            "L1a": [money(inputs[f"{TAXPAYER}.w2[{k}].box1"]) for k in inputs.get(f"$w2@{TAXPAYER}", [])]
                   + ([money(inputs[f"person[spouse].w2[{k}].box1"]) for k in inputs.get("$w2@person[spouse]", [])] if joint else []),
            "L2b": [money(inputs[f"interest[{k}].amount"]) for k in inputs.get("$interest", [])],
            "L3a": [money(f["qualified_dividends"])], "L3b": [money(f["ordinary_dividends"])],
            "L6a": money(f.get("ss_benefits", 0)),
            "L13a": money(l13a), "L19": money(l19), "L25a": money(f["withheld"]), "L25c": money(m_vals["L24"]), "L28": money(l28),
            "CapGains-A/D": sales_entries(inputs, ("A", "D")), "CapGains-B/E": sales_entries(inputs, ("B", "E")),
            "D13": money(f["capital_gain_distributions"]), "D19": money(f["unrecaptured_1250"]), "Collectibles": money(f["gain_28pct"]),
            **({"D6": str(prior_file)} if prior_file else {}),
            "S1_3": money(se_income), "S1_7": money(f.get("unemployment", 0)),
            "S1_11": money(f.get("educator_deduction", 0)), "S1_13": money(hsa_l13), "S1_15": money(se_l13),
            "S1_20": money(f.get("ira_contribution", 0)), "S1_21": money(f.get("student_loan_interest", 0)),
            "S1A_4a": money(f.get("tips", 0)), "S1A_14a": money(f.get("overtime", 0)), "S1A_22aiii": money(f.get("car_loan_interest", 0)),
            "A1": money(f["medical"]), "A5a": money(f["salt_income_tax"]), "A5b": money(f["salt_real_estate"]),
            "A8a": money(f["mortgage_interest"]), "A9": money(invest),
            "A11": money(f["cash_gifts"]), "A12": money(f["noncash_gifts"]),
            "S2_4": money(se_l12), "S2_11": money(m_vals["L18"]), "S2_12": money(s2_12),
            "S3_1": money(s3_1), "S3_2": money(s3_2),
        }
        return v

    def f1040_pass(name, **kw):
        vals, prose, path = run_program(pkg, f"taxsolve_US_1040_{YEAR_TAG}", "US_1040/US_1040_template.txt", f1040_values(**kw), workdir, name)
        return vals, prose, path

    p1, prose1, out1 = f1040_pass("f1040_pass1", l13a=0, l19=0, l28=0, s2_12=0, s3_1=0, s3_2=0)
    # The foreign tax credit without Form 1116: the smaller of the creditable tax and the tax on
    # line 16 (adapter arithmetic on the engine's own line 16; declared as a pass-through).
    s3_1 = min(f["foreign_tax"], p1["L16"]) if f["foreign_tax"] else 0
    itemized = any("Itemizing." in l for l in prose1)

    # --- Form 8960 (MAGI and the net gain from the engine's own Form 1040 lines) ---
    n_vals, _, _ = run_program(pkg, f"taxsolve_f8960_{YEAR_TAG}", "Form_8960/Form_8960_template.txt",
                               {**IDENT, "Status": STATUS[status], "Entity": "Individual", "Sec6013g": "No", "Sec6013h": "No", "Sec1141_10g": "No",
                                "L1": money(f["interest"]), "L2": money(f["ordinary_dividends"]), "L5a": money(p1["L7a"]),
                                "L9a": money(invest if itemized else 0), "L13": money(p1["L11a"])},
                               workdir, "f8960")
    for n in ("8", "11", "12", "15", "16", "17"):
        lines[f"f8960.line{n}"] = n_vals[f"L{n}"]
    lines["f8960.tax"] = n_vals["L17"]

    # --- Form 8995 (imports the pass-1 Form 1040 output and the Schedule C output) ---
    l13a = 0
    if se_income or f["section_199a_dividends"]:
        # The shipped template's row iii name line carries a stray ';' that the program reads as a
        # business name, which would auto-calculate the Schedule C income a second time.
        q = {"FileName1040": str(out1), "L6": money(f["section_199a_dividends"]), "L12": money(net_capital_gain(f)), "L1_iii_a:": None}
        if sc_out is not None:
            q.update({"FileNameSchC": str(sc_out), "L1_i_a:": "Biz", "L1_i_c": "0"})
        q_vals, _, _ = run_program(pkg, f"taxsolve_f8995_{YEAR_TAG}", "Form_8995/Form_8995_template.txt", q, workdir, "f8995")
        for n in ("2", "4", "5", "8", "9", "10", "11", "13", "14", "15"):
            lines[f"f8995.line{n}"] = q_vals.get(f"L{n}", 0)
        l13a = q_vals["L15"]
        lines["qbi.deduction"] = l13a
        lines["f1040.line13a"] = l13a

    # --- Form 1040, pass 2: with the QBI deduction, the NIIT and the foreign tax credit ---
    p2, prose2, out2 = f1040_pass("f1040_pass2", l13a=l13a, l19=0, l28=0, s2_12=n_vals["L17"], s3_1=s3_1, s3_2=0)

    # --- Form 2441 (imports the pass-2 Form 1040 output; earned income from Schedule SE by file) ---
    s3_2 = 0
    if "dependent_care" in case["features"]:
        d = {"FileName1040:": str(out2), "CkA": "No", "CkB": "No",
             "L1_a_r1:": "Care Provider", "L1_c_r1:": "11-1111111", "Ck_L1_d_r1": "No", "L1_e_r1": money(inputs["dcprov[p0].paid"])}
        # Every child under 13 is a qualifying person (the $3,000 / $6,000 limit counts persons,
        # not persons with expenses), so each is listed, with or without expenses.
        k = 0
        for i, age in enumerate(children):
            if age < 13 and k < 3:
                k += 1
                d.update({f"CkDep{k}QP": "No", f"Dep{k}FirstName:": f"Child{i + 1}", f"Dep{k}LastName:": "Gen", f"CkDep{k}Disabled": "No",
                          f"Dep{k}QualExp": money(inputs.get(f"dependent[child_{i + 1}].dc_paid", 0))})
        if se_out is not None:
            d["FileSEYours:"] = str(se_out)
        if joint:
            d["SpseEI1040"] = money(f.get("spouse_wages", 0))
        d_vals, _, _ = run_program(pkg, f"taxsolve_f2441_{YEAR_TAG}", "Form_2441/Form_2441_template.txt", d, workdir, "f2441")
        for lab, pid in (("L3", "line3"), ("L4", "line4"), ("L6", "line6"), ("L7", "line7"), ("L9a", "line9a"), ("L9c", "line9c"),
                         ("L10", "line10"), ("L11", "line11")):
            lines[f"f2441.{pid}"] = d_vals.get(lab, 0)
        s3_2 = d_vals.get("L11", 0)
    lines["s3.line2"] = s3_2

    # --- Schedule 8812 (Credit Limit Worksheet A and earned income are adapter arithmetic on
    #     the engine's own outputs; declared as pass-throughs) ---
    l19 = l28 = 0
    if children:
        clw_a = max(0, p2["L18"] - (s3_1 + s3_2))
        earned = max(0, p2["L1z"] + se_l3 - se_l13)
        box4 = w2_sum(inputs, TAXPAYER, "box4") + (w2_sum(inputs, "person[spouse]", "box4") if joint else 0)
        e_vals, _, _ = run_program(pkg, f"taxsolve_f8812_{YEAR_TAG}", "Form_8812/Form_8812_template.txt",
                                   {"Status": STATUS[status], "L1": money(p2["L11a"]), "L4": str(sum(1 for a in children if a < 17)),
                                    "L6": str(sum(1 for a in children if a >= 17)), "L13": money(clw_a), "Amnt19": "0",
                                    "L18a": money(earned), "L21": money(box4 + box6), "L22": money(se_l13), "L24": "0",
                                    "YourName:": IDENT["YourName:"], "SocSec:": IDENT["YourSocSec#:"]},
                                   workdir, "f8812")
        for n in ("5", "7", "8", "10", "11"):
            lines[f"s8812.line{n}"] = e_vals[f"L{n}"]
        # Lines the program leaves unprinted when the credit is phased out or no additional
        # credit is reached are zero on the form.
        for n in ("12", "14", "16a", "17", "27"):
            lines[f"s8812.line{n}"] = e_vals.get(f"L{n}", 0)
        for n in ("16b", "19", "20", "23", "25", "26"):
            if f"L{n}" in e_vals:
                lines[f"s8812.line{n}"] = e_vals[f"L{n}"]
        l19, l28 = e_vals.get("L14", 0), e_vals.get("L27", 0)

    # --- Form 1040, pass 3: final ---
    p3, prose3, _ = f1040_pass("f1040_pass3", l13a=l13a, l19=l19, l28=l28, s2_12=n_vals["L17"], s3_1=s3_1, s3_2=s3_2)
    p = p3
    for lab, pid in F1040_LABELS.items():
        if lab in p:
            lines[pid] = p[lab]
        elif lab in F1040_ZERO_WHEN_UNPRINTED:
            # Schedule A lines print only when positive; line 3 (7.5% of AGI) is negative, not
            # zero, when AGI is negative, so it is left unread there.
            if lab == "A3" and p.get("L11b", 0) < 0:
                continue
            lines[pid] = 0
    lines["f1040.tax_before_credits"] = p["L18"] + p["L23"]
    if children:
        lines["f1040.line19"] = l19
        lines["f1040.line28"] = l28
        lines["s8812.line14"] = l19
    m = next((re.search(r"Std-Deduction[,=]\s*(-?[\d.]+)\s*[<>]?\s*(-?[\d.]+)?", l) for l in prose3 if "Std-Deduction" in l), None)
    if m:
        # "(Itemizations < Std-Deduction, A17 < std)" or "(Itemizations = A17, Std-Deduction = std)"
        std = m.group(2) if m.group(2) is not None else m.group(1)
        lines["sa.standard"] = cents(std)
    lines["sa.deduction"] = p["L12"]
    if p.get("S2_2", 0):
        feats.add("ots_amt")
    # Schedule D lines, when the engine ran Schedule D.
    if "D16" in p:
        d17_yes = any("D17 = yes" in l for l in prose3)
        for lab, pid in SD_LABELS.items():
            if lab in ("D18", "D19") and not d17_yes:
                continue  # lines 18 to 21 are skipped when lines 15 and 16 are not both gains
            lines[pid] = p.get(lab, 0)
        if prior_file:
            lines["sd.line6"] = p.get("D6", 0)
            lines["sd.line14"] = p.get("D14", 0)
    # The Capital Loss Carryover Worksheet lines the engine printed (it prints lines 5 to 8 only when the 2024
    # line 7 is a loss and lines 9 to 13 only when line 15 is, as the worksheet's skip rules say, and nothing
    # when its applicability test finds no carryover).
    if prior_file:
        for n in range(1, 14):
            if f"CarryOverWs{n}" in p:
                lines[f"clcw.line{n}"] = p[f"CarryOverWs{n}"]
        feats.add("ots_carryover_worksheet" if "CarryOverWs1" in p else "ots_no_carryover_found")
    # The worksheets, when the engine ran them.
    if "QDCG1" in p:
        for n in range(1, 26):
            lines[f"qdcg.line{n}"] = p[f"QDCG{n}"]
    if any(f"SDTW{n}" in p for n in range(1, 48)):
        for n in range(1, 48):
            lines[f"sdtw.line{n}"] = p.get(f"SDTW{n}", 0)
    if "SSB1" in p:
        for n in range(1, 7):
            lines[f"ssb.line{n}"] = p[f"SSB{n}"]
        stop = p.get("SSB_STOP")
        for n in range(7, 19):
            if f"SSB{n}" in p:
                lines[f"ssb.line{n}"] = p[f"SSB{n}"]
            elif stop is not None and n in SSB_ZERO_AFTER_STOP:
                lines[f"ssb.line{n}"] = 0
    return lines, feats


# Form 1040 output labels and the project lines they are; labels the program prints only when
# nonzero are zero when absent.
F1040_LABELS = {
    "L1z": "f1040.line1z", "L6b": "f1040.line6b", "L7a": "f1040.line7a", "L8": "f1040.line8", "L9": "f1040.line9",
    "L10": "f1040.line10", "L11b": "f1040.line11b", "L12": "f1040.line12e", "L13b": "f1040.line13b",
    "L14": "f1040.line14", "L15": "f1040.line15", "L16": "f1040.line16", "L17": "f1040.line17", "L18": "f1040.line18",
    "L20": "f1040.line20", "L21": "f1040.line21", "L22": "f1040.line22", "L23": "f1040.line23", "L24": "f1040.line24",
    "L25d": "f1040.line25d", "L32": "f1040.line32", "L33": "f1040.line33", "L34": "f1040.line34", "L37": "f1040.line37",
    "S1_9": "s1.line9", "S1_10": "s1.line10", "S1_21_computed": "s1.line21", "S1_26": "s1.line26",
    "S1A_13": "s1a.line13", "S1A_21": "s1a.line21", "S1A_30": "s1a.line30", "S1A_37": "s1a.line37", "S1A_38": "s1a.line38",
    "S2_21": "s2.line21", "S3_8": "s3.line8",
    "A3": "sa.line3", "A4": "sa.line4", "A5d": "sa.line5d", "A5e": "sa.line5e", "A7": "sa.line7", "A8e": "sa.line8e",
    "A10": "sa.line10", "A14": "sa.line14", "A17": "sa.line17",
}
F1040_ZERO_WHEN_UNPRINTED = {"L25d", "L34", "L37", "S1A_13", "S1A_21", "S1A_30", "S1A_37", "S1A_38", "S2_21", "S3_8",
                             "A3", "A4", "A7", "A10", "A14", "A17"}
SD_LABELS = {
    "D1bd": "sd.line1b.d", "D1be": "sd.line1b.e", "D1bg": "sd.line1b.g", "D1bh": "sd.line1b.h",
    "D2d": "sd.line2.d", "D2e": "sd.line2.e", "D2g": "sd.line2.g", "D2h": "sd.line2.h",
    "D8bd": "sd.line8b.d", "D8be": "sd.line8b.e", "D8bg": "sd.line8b.g", "D8bh": "sd.line8b.h",
    "D9d": "sd.line9.d", "D9e": "sd.line9.e", "D9g": "sd.line9.g", "D9h": "sd.line9.h",
    "D7": "sd.line7", "D13": "sd.line13", "D15": "sd.line15", "D16": "sd.line16", "D18": "sd.line18", "D19": "sd.line19", "D21": "sd.line21",
}
# Social Security Benefits Worksheet lines that are zero on the form once the worksheet has
# answered "No" at line 7 or 9; lines 8, 10 and 17 keep their amounts and are compared only
# when printed.
SSB_ZERO_AFTER_STOP = {7, 9, 11, 12, 13, 14, 15, 16, 18}

OTS_PRECISION = "decimal2"
# How OpenTaxSolver's arithmetic differs from the project's, for the comparison's `unrounded`
# reading (compare.py). Each program computes in doubles and never rounds in cents mode
# (taxsolve_routines.c: Conditional_Round returns its argument unless whole-dollar rounding is
# set), so products and ratios carry their fractions of a cent (the project rounds each to the
# cent, amb.<year>.multiplication_subcent; the Student Loan Interest Deduction Worksheet ratio,
# for one, is ws[6] / 15000.0 unrounded in taxsolve_US_1040_<year>.c). A program prints each line
# with "%6.2f" (showline), and every amount that passes from one program to another (Schedule SE
# lines 6, 12 and 13 into Forms 8959 and 1040, Form 1040 lines 11a, 12, 13b, 16 and 18 into Forms
# 8960, 8995, 2441 and Schedule 8812, their results back into Form 1040) is that printed value,
# read back by the next program or by this adapter.
#   programs  which program computes a project line: the first pattern that matches the line's
#             key; any other line is Form 1040's. A value crossing from one program to another
#             is the printed value.
#   engine_line  where a printed value's tie is resolved, the engine line that shows it.
#   first_pass  a line the adapter figures from the first Form 1040 pass (before the QBI
#             deduction): it is modelled only when the named line is zero (the passes agree)
#             or the line's smaller-of takes its other operand, which is then not above the
#             final pass's value and so not above the first's.
# The amounts the adapter supplies in place of a computation are recorded per case (`supplied`).
OTS_UNROUNDED = {
    "programs": [
        [r"\|inst:se#|^person\[[^\]]+\]\.se_", "Schedule SE"],
        [r"^person\[[^\]]+\]\.sc\[", "Schedule C"],
        [r"^person\[[^\]]+\]\.f8889\[", "Form 8889"],
        [r"^f8959\.", "Form 8959"],
        [r"^f8960\.", "Form 8960"],
        [r"^(f8995|qbi)\.", "Form 8995"],
        [r"^f2441\.", "Form 2441"],
        [r"^s8812\.", "Schedule 8812"],
        [r"^ftc\.", "adapter"],
    ],
    "engine_line": {"f1040.line11a": "f1040.line11b"},
    "first_pass": {"ftc.limited": "f1040.line13a"},
}


def supplied_amounts(case):
    """The amounts the adapter gives the programs in place of a computation the project makes,
    keyed by project line: the comparison models such a line only where the project's value is
    the amount supplied."""
    f = case["facts"]
    out = {"s1.line20": f.get("ira_contribution", 0), "s1.line11": f.get("educator_deduction", 0),
           "sd.line19": f["unrecaptured_1250"], "s3.line4": 0, "s3.line5a": 0, "s3.line5b": 0, "s3.line11": 0,
           "f1040.line27a": 0}
    if f.get("self_employment_income") or f["section_199a_dividends"]:
        out["f8995.line12"] = net_capital_gain(f)
    return out

OTS_PASS_THROUGH = {"lines": [], "components": {
    f"{HSA}.line12": "Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; "
                     "the program does not compute the line 3 limitation chart; it computes lines 5 to 13",
    f"{HSA}.line13": "Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; "
                     "the program computes lines 5 to 13",
    "f1040.line10": "Schedule 1 line 11 (educator expenses after the $300 limit) and line 20 (the IRA deduction) enter as the generator's amounts; "
                    "lines 13 and 15 come from the engine's own Form 8889 and Schedule SE runs; line 21 is the engine's student loan worksheet",
    "f1040.line20": "Schedule 3 line 1 (the foreign tax credit) is the smaller of the creditable foreign tax and the engine's own line 16, figured by the adapter",
    "f8960.line17": "Form 8960 line 13 (modified AGI) and line 5a (net gain) are the engine's own Form 1040 lines 11a and 7a; line 9a is the investment "
                    "interest when the engine itemized; lines 8, 11, 12 and 15 to 17 are the program's",
    "f8995.line15": "Form 8995 line 12 (net capital gain plus qualified dividends) is figured from the facts; line 1 column (c) is the program's own "
                    "Schedule C line 31 less Schedule 1 lines 15 to 17 from its Form 1040 output; line 11 is its Form 1040 lines 11a less 12 less 13b",
    "s8812.line14": "Schedule 8812 line 13 (Credit Limit Worksheet A) is the engine's own Form 1040 line 18 less Schedule 3 lines 1 and 2, figured by the adapter",
    "s8812.line27": "Schedule 8812 line 18a (earned income) is the engine's own Form 1040 line 1z plus Schedule SE line 3 (profit or loss) less line 13, not below zero, and line 13 the "
                    "adapter's Credit Limit Worksheet A; lines 21 (boxes 4 and 6), 22 (Schedule 1 line 15) and 24 (zero: no EIC, no excess social security) are supplied",
    "f2441.line11": "Form 2441 line 4 (earned income) is the engine's own Form 1040 line 1z less the spouse's wages, plus its Schedule SE lines 3 less 13 by file import; "
                    "line 10 is its own Form 1040 line 18 less Schedule 3 line 1",
    "sd.line19": "Schedule D line 19 is supplied as Form 1099-DIV box 2b; the program takes the Unrecaptured Section 1250 Gain Worksheet result as an input",
    "f8959.line18": "Form 8959 line 8 (self-employment income) is the engine's own Schedule SE line 6",
}, "unmapped": {
    "f1040.line27a": "the earned income credit is an input (L27); OTS has no EIC worksheet or table",
    "eic.credit": "the earned income credit is an input (L27); OTS has no EIC worksheet or table",
    "f8880.line10": "the saver's credit is an input (S3_4); OTS does not compute Form 8880",
    "f8880.line12": "the saver's credit is an input (S3_4); OTS does not compute Form 8880",
    "f5695.line13": "the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695",
    "f5695.line15": "the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695",
    "f5695.line30": "the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695",
    "f5695.line32": "the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695",
    "s3.line5a": "the residential energy credits are inputs; the engine's zero would not be a computation",
    "s3.line5b": "the residential energy credits are inputs; the engine's zero would not be a computation",
    "s1.line20": "the IRA deduction is an input (S1_20); OTS does not compute the IRA Deduction Worksheet",
    "s3.line11": "the excess social security withholding credit is an input (S3_11); OTS does not compute it",
    "eic.earned_income": "no EIC computation",
    "eic.line1": "no EIC computation",
    "u1250.line18": "the Unrecaptured Section 1250 Gain Worksheet is not computed; its result is the input D19",
    "f1040.line1z": "mapped (sum of Forms W-2 box 1)",
    "f8863.line19": "OTS does not compute Form 8863; Schedule 3 line 3 and Form 1040 line 29 are entered amounts (limitation education)",
    "f1040.line29": "OTS does not compute Form 8863; Form 1040 line 29 is an entered amount (limitation education)",
}}


# Lines a Form 1095-A moves: Schedule 3 line 9 and Schedule 2 line 1a, and through Form 1040 lines 17, 18 and 31 the tax,
# every credit the tax limits, the payments and the refund. Engines given no Form 1095-A are not compared on them there.
PTC_MOVED = re.compile(r"^(f1040\.line(1[7-9]|2[0-9]|3[0-9]|35a)|f1040\.tax_before_credits|s3\.line(2|3|4|5a|5b|8|9|15)|s2\.line(1a|1z|3|21)"
                       r"|s8812\.|f2441\.line(9c|10|11)|f8863\.line19|f8880\.line(11|12)|f5695\.line(14|15|31|32)|f8962\.)")
PTC_REASON = ("the engine is given no Form 1095-A, so its tax, credits and payments omit the premium tax credit reconciliation "
              "(Form 8962) the project figures on these returns")

# Lines Form 8863 moves: its own lines, Schedule 3 line 3 and Form 1040 line 29, and through them every credit after the
# education credits, the tax after credits, the payments and the refund.
EDU_MOVED = re.compile(r"^(f1040\.line(19|2[0-2]|24|28|29|3[2-7]|35a)|s3\.line(3|4|5a|5b|8|15)|s8812\.(line(14|16a|17|27)|clw)"
                       r"|f8880\.line(11|12)|f5695\.line(14|15|31|32)|f8863\.)")
EDU_REASON = ("OpenTaxSolver does not compute Form 8863: it reads Schedule 3 line 3 and Form 1040 line 29 as entered amounts, and the "
              "engine is given none, so its credits after the education credits, its tax after credits and its payments omit the "
              "education credits the project figures on these returns")


def limitations(pkg_version):
    """The engine's declared limitations, keyed by generator or derived features. Those marked
    with a version are defects of that release and drop away when another release is installed."""
    AGI_LINES = ["f1040.line9", "f1040.line10", "f1040.line11b", "s1.line26", "sa.line3", "sa.line4", "sa.line17", "sa.deduction",
                 "f1040.line12e", "f1040.line13a", "f1040.line13b", "f1040.line14", "f1040.line15", "f1040.line16", "f1040.line17",
                 "f1040.line18", "f1040.line20", "f1040.line21", "f1040.line22", "f1040.line24", "f1040.tax_before_credits",
                 "f1040.line19", "f1040.line28", "f1040.line32", "f1040.line33", "f1040.line34", "f1040.line37",
                 "f8960.line15", "f8960.line16", "f8960.line17", "f8960.tax", "f8995.line11", "f8995.line13", "f8995.line14", "f8995.line15",
                 "qbi.deduction", "s1a.line13", "s1a.line21", "s1a.line30", "s1a.line37", "s1a.line38", "f2441.line7", "f2441.line9a",
                 "f2441.line9c", "f2441.line10", "f2441.line11", "s3.line2", "s3.line8"] \
                + [f"qdcg.line{n}" for n in range(1, 26)] + [f"sdtw.line{n}" for n in range(1, 48)] + [f"ssb.line{n}" for n in range(1, 19)] \
                + ["f1040.line6b"] + [f"s8812.line{n}" for n in ("1", "3", "10", "11", "12", "14", "16a", "17", "19", "20", "26", "27")]
    TAX_LINES = ["f1040.line16", "f1040.line18", "f1040.line20", "f1040.line21", "f1040.line22", "f1040.line24", "f1040.tax_before_credits",
                 "f1040.line19", "f1040.line28", "f1040.line32", "f1040.line33", "f1040.line34", "f1040.line37",
                 "f2441.line10", "f2441.line11", "s3.line2", "s3.line8", "s8812.line14", "s8812.line16a", "s8812.line17", "s8812.line27"]
    AFTER_CREDIT_LINES = ["f1040.line20", "s3.line8", "f1040.line21", "f1040.line22", "f1040.line24", "f1040.line32", "f1040.line33", "f1040.line34",
                          "f1040.line37", "f1040.line19", "f1040.line28", "s8812.line14", "s8812.line16a", "s8812.line17", "s8812.line27"]
    REFUND_LINES = ["f1040.line32", "f1040.line33", "f1040.line34", "f1040.line37", "s8812.line27", "f1040.line28"]
    lims = [
        {"feature": "eic", "lines": REFUND_LINES,
         "reason": "OpenTaxSolver takes the earned income credit as an input (L27) and has no EIC worksheet or table; the credit is supplied as zero, "
                   "so Schedule 8812 line 24 and the payment lines are not compared on returns with an EIC"},
        {"feature": "excess_social_security", "lines": REFUND_LINES,
         "reason": "OpenTaxSolver takes the excess social security withholding credit as an input (S3_11), supplied as zero; it does not compute it from per-employer withholding"},
        {"feature": "savers_credit", "lines": AFTER_CREDIT_LINES,
         "reason": "OpenTaxSolver takes the saver's credit as an input (S3_4) and does not compute Form 8880; the credit is supplied as zero, so the lines after "
                   "the nonrefundable credits, and Schedule 8812 Credit Limit Worksheet A, are not compared on returns with one"},
        {"feature": "residential_clean_energy", "lines": AFTER_CREDIT_LINES,
         "reason": "OpenTaxSolver takes the residential clean energy credit as an input (S3_5a) and does not compute Form 5695; supplied as zero"},
        {"feature": "home_improvement", "lines": AFTER_CREDIT_LINES,
         "reason": "OpenTaxSolver takes the energy efficient home improvement credit as an input (S3_5b) and does not compute Form 5695; supplied as zero"},
        {"feature": "ira_phaseout", "lines": AGI_LINES + ["s1.line21"],
         "reason": "OpenTaxSolver takes the IRA deduction as an input (S1_20), supplied as the contributions; it does not compute the IRA Deduction Worksheet's "
                   "phase-out by modified AGI, so returns whose deduction is less than the contributions are not compared on the lines that follow AGI, "
                   "nor on Schedule 1 line 21, whose student loan interest phase-out reads modified AGI after the IRA deduction"},
        {"feature": "sli_phaseout", "lines": AGI_LINES + ["s1.line21"],
         "reason": "OpenTaxSolver's student loan interest worksheet (Calc_StudentLoan_Sched1L21) uses the exact line 7 ratio; the project rounds it to three places "
                   "(amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars, so returns in the phase-out are not compared on the lines that follow AGI"},
        {"feature": "section_1250_netted", "lines": ["sd.line19", "sd.line20"] + [f"sdtw.line{n}" for n in range(1, 48)] + TAX_LINES,
         "reason": "OpenTaxSolver takes Schedule D line 19 as an input (D19, 'amount from line 18 of the Unrecaptured Section 1250 Gain Worksheet'), supplied as "
                   "Form 1099-DIV box 2b; the worksheet nets the gain against the net short-term loss and the 28% worksheet amounts, which the project does"},
        {"feature": "investment_interest_limited", "lines": ["sa.line9", "sa.line10", "sa.line17", "sa.deduction", "f1040.line12e", "f1040.line13a", "f1040.line14",
                                                             "f1040.line15", "f8995.line11", "f8995.line13", "f8995.line14", "f8995.line15", "qbi.deduction",
                                                             "f8960.line11", "f8960.line12", "f8960.line16", "f8960.line17", "f8960.tax"] + TAX_LINES
                                                            + [f"qdcg.line{n}" for n in range(1, 26)] + [f"sdtw.line{n}" for n in range(1, 48)],
         "reason": "OpenTaxSolver takes Schedule A line 9 as entered (A9) and fixes Schedule D Tax Worksheet lines 3 and 4 at zero; it does not apply the Form 4952 "
                   "net-investment-income limit, and the adapter supplies the investment interest paid"},
        {"feature": "negative_agi", "lines": ["sa.line3", "sa.line4", "sa.line14", "sa.line17", "sa.deduction", "f1040.line12e", "f1040.line14", "f1040.line15", "f8995.line11",
                                              "f8995.line13", "f8995.line14", "f8995.line15", "qbi.deduction", "f1040.line13a",
                                              "f2441.line9a", "f2441.line9c", "f2441.line11", "s3.line2"] + TAX_LINES
                                             + [f"qdcg.line{n}" for n in range(1, 26)] + [f"sdtw.line{n}" for n in range(1, 48)],
         "reason": "OpenTaxSolver figures Schedule A line 3 as 7.5% of a negative adjusted gross income and line 4 as `NotLessThanZero(SchedA[1] - SchedA[3])`, "
                   "adding the negative floor to the medical expenses, where the instructions allow \"only the part of your medical and dental expenses that "
                   "exceeds 7.5% of the amount of your adjusted gross income\" (i1040sca, line 1). It caps lines 11 and 12 at 60% and 30% of adjusted gross income by multiplying the AGI as it stands "
                   "(`if (charityCC > 0.60 * L[11]) charityCC = 0.60 * L[11]`), so a negative AGI turns gifts, even none, into a negative charitable "
                   "deduction on line 14; the project's limit is the sa.charity_limited screen, which the generator answers no. Its Form 2441 "
                   "program's line 8 rate lookup (GetLimit over line_8_rate_table) returns zero for an AGI below the table's first row, where the "
                   "project reads the first row (\"$0—15,000\": 0.35) for any amount not over $15,000"},
        {"feature": "tax_table_band_edge", "lines": TAX_LINES + [f"qdcg.line{n}" for n in (22, 23, 24, 25)] + [f"sdtw.line{n}" for n in (44, 45, 46, 47)],
         "reason": "OpenTaxSolver's TaxRateFunction emulates the Tax Table by quantizing the amount to its band (`k = income / x; x = x * (double)k + dx`) "
                   "on a double built by summing the return's lines; when the project's amount in integer cents is exactly a band boundary, the engine's "
                   "double can land a hair below it (mfj-00061: 107,096.84 + 2,341.61 + 7,689.01 - 277.46 - 31,500 = 85,349.99999999999) and the band "
                   "below is read; the Tax Table reads \"At least\" the boundary"},
        {"feature": "investment_interest", "lines": ["sdtw.line3", "sdtw.line4"],
         "reason": "OpenTaxSolver fixes Schedule D Tax Worksheet lines 3 and 4 at zero (sched_D_tax_worksheet: `ws[3] = 0.0; /* Form 4952, line 4g. */ "
                   "ws[4] = 0.0; /* Form 4952, line 4e. */`); on a return that files Form 4952 the project carries its line 4e there. Line 3 is zero on the "
                   "generated returns (no line 4g election), so lines 5 and 8 and the tax are unmoved"},
        {"feature": "qbi_above_threshold", "lines": ["f8995.line11", "f8995.line13", "f8995.line14", "f8995.line15", "qbi.deduction", "f1040.line13a",
                                                     "f1040.line14", "f1040.line15"] + TAX_LINES + [f"qdcg.line{n}" for n in range(1, 26)] + [f"sdtw.line{n}" for n in range(1, 48)],
         "reason": "OpenTaxSolver has no Form 8995-A; its Form 8995 program computes the simplified deduction above the taxable income threshold, where "
                   "the form sends the filer to Form 8995-A and the project refuses the return"},
        {"feature": "ots_amt", "lines": ["f1040.line17", "f1040.line18", "f1040.tax_before_credits", "s2.line3"] + AFTER_CREDIT_LINES + ["f2441.line10", "f2441.line11", "s3.line2"],
         "reason": "OpenTaxSolver computed an alternative minimum tax (Form 6251, Schedule 2 line 2) on this return; Form 6251 is outside the project's scope "
                   "(the s2.amt screen), so the lines from Schedule 2 line 3 onward are not compared"},
        {"feature": "three_or_more_children", "lines": ["s8812.line27", "f1040.line28", "f1040.line32", "f1040.line33", "f1040.line34", "f1040.line37"],
         "reason": "OpenTaxSolver's Schedule 8812 program takes the Part II-A route (`if (L16b <= 5100.0)`, taxsolve_f8812) when line 16b is exactly $5,100, where the "
                   "form's line 20 asks 'On line 16b, is the amount $5,100 or more?' and sends a Yes to Part II-B when line 20 is less than line 17; with three "
                   "qualifying children the engine skips Part II-B"},
    ]
    for lim in lims:
        if "f8960.tax" in lim["lines"] or "f8959.tax" in lim["lines"]:
            lim["lines"] = list(lim["lines"]) + [l for l in ("s2.line21", "f1040.line23") if l not in lim["lines"]]
    if pkg_version.startswith("23.06"):
        lims += [
            {"feature": "special_gains", "lines": [f"sdtw.line{n}" for n in range(19, 48)] + TAX_LINES, "version": pkg_version,
             "reason": "OpenTaxSolver 23.06's Schedule D Tax Worksheet (sched_D_tax_worksheet) codes the line 19 ceiling for single and married filing separately as "
                       "197,390 (the 2025 worksheet: $197,300) and runs lines 33 to 43 only when lines 1 and 32 are equal (`absolutev(ws[1]-ws[32]) < 0.01`), where "
                       "the worksheet says to skip them when they are equal; the 23.07 revision history reports both fixed"},
            {"feature": "car_loan_interest", "lines": ["s1a.line30", "s1a.line38", "f1040.line13b", "f1040.line14", "f1040.line15", "f8995.line11", "f8995.line13",
                                                      "f8995.line14", "f8995.line15", "qbi.deduction", "f1040.line13a"] + TAX_LINES
                                                      + [f"qdcg.line{n}" for n in range(1, 26)] + [f"sdtw.line{n}" for n in range(1, 48)], "version": pkg_version,
             "reason": "OpenTaxSolver 23.06's Schedule 1-A Part IV (sched_1A) truncates line 28 (`j = sched1A_L[27] / 1000.0`) where the form rounds up to the next "
                       "whole number, and multiplies line 29 by $300 per $1,000 where the form says $200; the 23.07 revision history reports both fixed"},
        ]
    universe = ({*F1040_LABELS.values(), "f1040.tax_before_credits", "f1040.line19", "f1040.line28", "s3.line2", "s3.line4", "s3.line5a",
                 "s3.line5b", "s3.line15", "f2441.line9c", "f2441.line10", "f2441.line11", "f8880.line11", "f8880.line12", "f5695.line14",
                 "f5695.line15", "f5695.line31", "f5695.line32"}
                | {f"s8812.line{n}" for n in ("1", "2a", "2b", "2c", "2d", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                                               "15", "16a", "16b", "17", "18a", "18b", "19", "20", "21", "22", "23", "24", "25", "26", "27")})
    lims.append({"feature": "marketplace", "lines": sorted(l for l in universe if PTC_MOVED.match(l)),
                 "reason": PTC_REASON})
    lims.append({"feature": "education", "lines": sorted(l for l in universe if EDU_MOVED.match(l)), "reason": EDU_REASON})
    return lims


def run_ots(cases, year, work_root):
    """Every case through OTS. Returns the engine record for engines.json, or None when the
    package is not built. Cases a program rejects are reported and left without lines."""
    configure(year)
    pkg = package_dir()
    if pkg is None or not is_available():
        return None
    pkg_version, bin_version = package_version(pkg)
    lines, feats, supplied, failures = {}, {}, {}, []
    for c in cases:
        workdir = Path(work_root) / c["id"]
        workdir.mkdir(parents=True, exist_ok=True)
        try:
            lines[c["id"]], fs = run_case(pkg, c, workdir)
            supplied[c["id"]] = supplied_amounts(c)
            if fs:
                feats[c["id"]] = sorted(fs)
        except (OtsError, KeyError) as e:
            failures.append((c["id"], str(e)[:300]))
    if failures:
        print(f"OpenTaxSolver: {len(failures)} cases rejected by a program, e.g. {failures[:3]}")
    return {"version": f"{pkg_version} (package 0_README.txt; the Form 1040 program reports v{bin_version})", "package_version": pkg_version,
            "precision": OTS_PRECISION, "tax_table": True, "lines": lines, "features": feats,
            "limitations": limitations(pkg_version), "pass_through": OTS_PASS_THROUGH, "unrounded": OTS_UNROUNDED,
            "supplied": supplied, "rejected": [cid for cid, _ in failures]}
