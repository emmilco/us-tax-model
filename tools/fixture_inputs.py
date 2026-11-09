"""The inputs fixture cases are evaluated on, for Python tools: the engine's own resolver
(engine/src/fixture-inputs.ts, through `node engine/dist/main.js fixture-inputs`) resolves parameter-relative
inputs and applies the test-data defaults (fixtures/<year>/defaults.json, and for New York also
fixtures/ny/<year>/defaults.json). A tool that evaluates or inspects a case's inputs reads them through here,
never from the case file directly: a case states only what differs from the defaults.

Standard library only, so that tools running in other environments (tools/engines/) can import it.
"""

import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODE = ["node", str(ROOT / "engine" / "dist" / "main.js")]


def resolve_cases(cases, year, ny=False, defaults=None):
    """{id: inputs} for fixture cases ({"id", "file", "inputs"} as a fixture file states them, "file" the case file's
    name, which decides whether the case takes the defaults). `defaults`: defaults files to read instead of the
    year's (federal first). Raises ValueError with the engine's message when a case's inputs do not resolve."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([{"id": c["id"], "file": c["file"], "inputs": c["inputs"]} for c in cases], f)
        path = f.name
    args = NODE + ["fixture-inputs", "--cases", path, "--year", str(year)] + (["--ny"] if ny else [])
    for d in defaults or []:
        args += ["--defaults", str(d)]
    try:
        with tempfile.NamedTemporaryFile("w+", suffix=".json") as out:
            r = subprocess.run(args, stdout=out, stderr=subprocess.PIPE, text=True, cwd=ROOT)
            if r.returncode:
                raise ValueError(r.stderr.strip() or "fixture-inputs failed")
            out.seek(0)
            return json.load(out)["cases"]
    finally:
        Path(path).unlink()


def load_cases(year, ny=False):
    """Every case of the year's fixtures (fixtures/<year>/, or fixtures/ny/<year>/), each with "file" and its
    inputs resolved; the defaults table itself is not a case file."""
    d = ROOT / "fixtures" / ("ny" if ny else "") / str(year)
    cases = []
    for path in sorted(d.glob("*.json")):
        if path.name == "defaults.json":
            continue
        for c in json.loads(path.read_text(encoding="utf-8")).get("cases", []):
            cases.append({**c, "file": path.name})
    resolved = resolve_cases(cases, year, ny)
    return [{**c, "inputs": resolved[c["id"]]} for c in cases]
