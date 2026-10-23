# SPDX-License-Identifier: Apache-2.0
"""A worked example per printed line, from the fixtures and the engine.

The candidates are the fixture cases (fixtures/<year>/*.json) whose `expect` asserts the
line; they are evaluated in one `eval --batch` run and the case whose reading shows the most
nonzero values is shown: the line's value, then the value of every line its reading names.
"""
import glob
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

from reading import STATUS_WORDS, dollars  # noqa: E402

FIXTURES = ROOT / "fixtures" / Y
ENGINE = ROOT / "engine" / "dist" / "main.js"


def cases():
    out = []
    for f in sorted(glob.glob(str(FIXTURES / "*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for c in d.get("cases", []):
            if "inputs" in c and "expect" in c:
                out.append(c)
    return out


def value_text(v):
    if v is None:
        return "unknown"
    k = v.get("kind")
    if k == "money":
        return dollars(v["cents"])
    if k == "bool":
        return "yes" if v["value"] else "no"
    if k == "count":
        return str(v["value"])
    if k == "enum":
        return STATUS_WORDS.get(v["value"], str(v["value"]))
    if k == "refusal":
        return f"refused (gate {v.get('gate')})"
    if k == "rate":
        return str(v.get("value"))
    return json.dumps(v)


def nonzero(v):
    if not v:
        return False
    k = v.get("kind")
    return (k == "money" and v["cents"] != 0) or (k in ("bool", "count") and bool(v["value"]))


def values_of(values, lid):
    """[(entry label or "", value)] for a line id: the line itself, or its per-entry instances."""
    if lid in values:
        return [("", values[lid]["value"])]
    form, _, rest = lid.partition(".")
    out = []
    for k, v in values.items():
        if k.startswith(form + "[") and k.endswith("." + rest) and k.count(".") == lid.count("."):
            out.append((k[len(form) + 1:k.index("]")], v["value"]))
    return out


def batch_eval(case_list, targets):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([{"id": c["id"], "inputs": c["inputs"]} for c in case_list], f)
        path = f.name
    out = subprocess.run(["node", str(ENGINE), "eval", "--batch", path, "--target", ",".join(targets)],
                         capture_output=True, text=True, cwd=ROOT)
    Path(path).unlink()
    if out.returncode:
        raise RuntimeError(out.stderr.strip() or "eval failed")
    return json.loads(out.stdout)["cases"]


def example(canon, reading, names):
    """{"case", "value", "reads": [(name, text)]} for the best fixture case, or {"none": reason}.
    `names` maps a line id to the phrase the reading uses for it."""
    lid = reading.root
    cands = [c for c in cases() if lid in c["expect"]]
    if not cands:
        return {"none": f"no fixture case asserts {lid}"}
    nz = [c for c in cands if nonzero(c["expect"][lid])]
    pool = nz or cands
    results = batch_eval(pool, [lid])
    best, score = None, -1
    for c in pool:
        r = results.get(c["id"], {})
        if "error" in r or "values" not in r:
            continue
        vals = r["values"]
        s = sum(1 for x in reading.helpers + reading.leaves for _, v in values_of(vals, x) if nonzero(v))
        if s > score:
            best, score = (c, vals), s
    if best is None:
        return {"none": f"the fixture cases asserting {lid} could not be evaluated"}
    c, vals = best
    reads = []
    for x in reading.helpers + reading.leaves:
        if x in names and names[x].startswith("parameter ") and canon.params["values"].get(
                canon.lines[x]["expr"].get("ref"), {}).get("value") == 1:
            continue  # a count of one per entry says nothing in an example
        inst = values_of(vals, x)
        if not inst:
            reads.append((names.get(x, x), "not reached on this return"))
        elif len(inst) == 1 and not inst[0][0]:
            reads.append((names.get(x, x), value_text(inst[0][1])))
        else:
            reads.append((names.get(x, x), "; ".join(f"{who}: {value_text(v)}" for who, v in inst)))
    top = values_of(vals, lid)
    return {"case": c["id"], "value": value_text(top[0][1]) if top else "not evaluated", "reads": reads,
            "expected": value_text(c["expect"][lid])}
