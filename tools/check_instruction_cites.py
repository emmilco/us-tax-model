#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Instruction-section citations and supplied-input cross-references (T-084), offline, in check-all.

(a) section: a line printed with a line number ("7", "25c") on a form whose archived instructions have a
    "Line N" section must cite the instruction page that carries that section's heading, so that the
    paragraph governing the line is among the pages its reviews are given.
(b) xref: an input standing for a printed line is checked in its "Line N" section for references
    ("Form 8959, line 24", "Schedule 2, line 11") to lines this project computes; such an input asks
    the filer for an amount the project figures.

A finding is accepted only by a ruling (`rulings`, with a reason) or by the baseline of findings that
existed when the check was introduced (`baseline`), tied to its form's hash and worked off form by form as each
form is next changed (`tools/baseline_check.py`). Rulings and baseline live in
reviews/<year>/instruction_cites.json; the report is reports/<year>/instruction_cites.md.

    check_instruction_cites.py              check (exit 1 on new findings or stale baseline entries)
    check_instruction_cites.py --baseline   rewrite the baseline to the current findings (use once)
    check_instruction_cites.py --self-test
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
from citations import segments  # noqa: E402
import baseline_check  # noqa: E402
import archive_text  # noqa: E402

SOURCES = ROOT / "sources" / Y
CANONICAL = ROOT / "canonical" / Y
RULINGS = ROOT / "reviews" / Y / "instruction_cites.json"
REPORT = ROOT / "reports" / Y / "instruction_cites.md"

PRINTED = re.compile(r"^\d{1,2}[a-z]?$")
# The general instructions cover Form 1040 and Schedules 1, 1-A, 2 and 3, each in its own page range (line numbers
# restart in each part).
INSTRUCTIONS = {"f1040": "i1040gi", "f1040s1": "i1040gi", "f1040s1a": "i1040gi", "f1040s2": "i1040gi", "f1040s3": "i1040gi"}
PARTS = {"f1040": (1, 87), "f1040s1": (88, 100), "f1040s1a": (101, 110), "f1040s2": (111, 114), "f1040s3": (115, 999)}
HEADING = re.compile(r"^Lines? (\d{1,2}[a-z]?(?:(?:,| and| through|,? and| or|–|-)\s*\d{1,2}[a-z]?)*)\b")
REFERENCE = re.compile(r"((?:Form|Schedule) [0-9A-Z]{1,4}(?:-[A-Z]+)?),?\s+(?:\(Form 1040\),?\s+)?lines? (\d{1,2}[a-z]?)")


def instruction_doc(face):
    doc = INSTRUCTIONS.get(face) or ("i" + face[1:] if face.startswith("f") else None)
    return doc if doc and "cols_file" in archive_text.manifest(SOURCES).get(doc, {}) else None


def covers(spec, number):
    """Whether a heading's line list ("25a through 25c", "1 and 2", "8") names `number`."""
    n, letter = re.match(r"(\d+)([a-z]?)", number).groups()
    tokens = re.findall(r"(\d+)([a-z]?)", spec)
    if (n, letter) in tokens or (n, "") in tokens:
        return True
    for (a, _), (b, _) in zip(tokens, tokens[1:]):
        between = spec[spec.find(a):]
        if re.match(rf"{a}[a-z]?\s*(?:through|–|-)\s*{b}", between) and int(a) <= int(n) <= int(b):
            return True
    return False


class Instructions:
    """Pages of one archived instruction document and the "Line N" headings on each."""

    def __init__(self, doc):
        self.pages = archive_text.read(SOURCES, archive_text.manifest(SOURCES)[doc], key="cols_file").split("\f")
        self.headings = []  # (page, line index, spec)
        for p, text in enumerate(self.pages, start=1):
            for i, row in enumerate(text.split("\n")):
                m = HEADING.match(row.strip())
                if m:
                    self.headings.append((p, i, m.group(1)))

    def section_pages(self, number, part=(1, 999)):
        return {p for p, _, spec in self.headings if covers(spec, number) and part[0] <= p <= part[1]}

    def section_text(self, number, part=(1, 999), rows=60):
        """The text under the most specific heading naming `number` ("Line 25c" before "Line 25")."""
        exact = re.match(r"(\d+)([a-z]?)", number).groups()
        ranked = sorted(self.headings, key=lambda h: exact not in re.findall(r"(\d+)([a-z]?)", h[2]))
        for p, i, spec in ranked:
            if covers(spec, number) and part[0] <= p <= part[1]:
                lines = "\n".join(self.pages[p - 1:p + 1]).split("\n")[i + 1:i + 1 + rows]
                out = []
                for row in lines:
                    if HEADING.match(row.strip()):
                        break
                    out.append(row)
                return " ".join(out)
        return None


def cited_pages(cite):
    """{doc: pages} named by a line's citation."""
    out = {}
    for doc, pages, _, _, _ in segments(cite.get("doc", ""), cite.get("locator", "")):
        out.setdefault(doc, set()).update(pages)
    return out


def face_of(form):
    faces = [l.get("cite", {}).get("doc", "") for l in form["lines"]]
    faces = [d for d in faces if re.match(r"^f\d{4}|^f1040", d)]
    return max(set(faces), key=faces.count) if faces else None


def form_names(forms):
    """"Form 8959" / "Schedule 2" -> form id, for the forms whose printed lines this project computes."""
    names = {}
    for form in forms:
        m = re.match(r"((?:Form|Schedule) [0-9A-Z]{1,4}(?:-[A-Z]+)?)\b", form.get("title", ""))
        if m:
            names.setdefault(m.group(1), form["id"])
    return names


def findings(forms):
    docs = {}
    names = form_names(forms)
    computed = {f["id"]: {l["printed"] for l in f["lines"] if PRINTED.match(str(l.get("printed", "")))
                          and l.get("expr", {}).get("op") != "input"} for f in forms}
    out = []
    for form in forms:
        form_face = face_of(form)
        for line in form["lines"]:
            number = str(line.get("printed", ""))
            if not PRINTED.match(number):
                continue
            own = line.get("cite", {}).get("doc", "")
            face = own if re.match(r"^f\d{4}|^f1040", own) else form_face
            idoc = instruction_doc(face) if face else None
            if not idoc:
                continue
            ins = docs.setdefault(idoc, Instructions(idoc))
            part = PARTS.get(face, (1, 999)) if idoc == "i1040gi" else (1, 999)
            pages = ins.section_pages(number, part)
            if not pages:
                continue
            cited = cited_pages(line.get("cite", {})).get(idoc, set())
            if not cited & pages:
                out.append({"kind": "section", "line": line["id"], "form": form["id"],
                            "detail": f"{idoc} p. {', '.join(map(str, sorted(pages)))} has the Line {number} section; "
                                      f"the citation names {', '.join(map(str, sorted(cited))) or 'no page'} of {idoc}"})
            if line.get("expr", {}).get("op") == "input":
                text = ins.section_text(number, part) or ""
                for name, ref in REFERENCE.findall(text):
                    target = names.get(name)
                    if target and target != form["id"] and ref in computed.get(target, ()):
                        out.append({"kind": "xref", "line": line["id"], "form": form["id"],
                                    "detail": f"its {idoc} Line {number} section refers to {name}, line {ref}, "
                                              f"which this project computes ({target})"})
    return out


def check(rebaseline=False):
    forms = baseline_check.load_forms(CANONICAL)
    return baseline_check.run(
        "instruction cites", forms, findings(forms), RULINGS, REPORT,
        "Instruction-section citations and supplied-input cross-references",
        "Generated by `tools/check_instruction_cites.py` (T-084). `section`: a printed line does not cite the instruction "
        "page carrying its \"Line N\" section. `xref`: an input's Line N section refers to a line this project computes.",
        rebaseline)


def self_test():
    assert covers("25a through 25c", "25b") and covers("8", "8z") and covers("1 and 2", "2")
    assert not covers("25a through 25c", "26") and not covers("16", "1")
    assert HEADING.match("Lines 25a through 25c").group(1).startswith("25a")
    assert REFERENCE.findall("enter the amount from Form 8959, line 24.") == [("Form 8959", "24")]
    assert REFERENCE.findall("Schedule 2 (Form 1040), line 11") == [("Schedule 2", "11")]
    print("instruction cites self-test: ok")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(check(rebaseline="--baseline" in sys.argv))
