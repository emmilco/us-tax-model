"""Source-based partial-input cases; only synthetic facts enter blind requests.

Host checks use the fixed declarative evaluator after schema/type validation in
a separate, bounded process. They never change authored forms, numeric fixtures
or original model receipts, and earn no H/B/M/engine scoreboard assertion.
"""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = Path(__file__).resolve().parent / "input_contracts"
POLICY = "source-partial-inputs-v1"
REQUIRED = {"2025": {"dependent"}}


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def load(form, year):
    path = DIRECTORY / str(year) / f"{form}.json"
    if not path.exists():
        if form in REQUIRED.get(str(year), set()):
            raise FileNotFoundError("required source input-contract bank is missing: " + str(path))
        return None
    bank = json.loads(path.read_text())
    if bank["form"] != form or bank["tax_year"] != int(year) or bank["policy"] != POLICY:
        raise ValueError("input-contract identity mismatch")
    if not bank["cases"] or len(bank["cases"]) > 32:
        raise ValueError("invalid input-contract cases")
    if len({test['id'] for test in bank['cases']}) != len(bank['cases']):
        raise ValueError("duplicate input-contract case id")
    manifest = json.loads((ROOT / 'sources' / str(year) / 'manifest.json').read_text())
    sources = {source['id']: source for source in manifest['documents']}
    if not bank.get('sources') or any(source['text_sha256'] != sources.get(source['doc'], {}).get('text_sha256') for source in bank['sources']):
        raise ValueError("stale input-contract source snapshot")
    return bank


def cases(bank):
    return [{"id": test["id"], "inputs": {**bank["base_inputs"], **test["inputs"]}, "expect": test["expect"]}
            for test in bank["cases"]]


def public_prompt(bank):
    if bank is None:
        return ""
    public = [{"id": test["id"], "inputs": test["inputs"], "targets": sorted(test["expect"])} for test in cases(bank)]
    return ("# Partial-input fact cases (" + POLICY + ")\n\n"
            "These are synthetic facts for the closed input interface, not computed results.\n"
            "An input catalog does not promise that every answer is supplied. An absent answer\n"
            "is unknown, never false or zero. Derive what the IRS text determines from the facts;\n"
            "avoid requiring an unanswered question when other given facts already determine the result.\n"
            "Where the facts genuinely do not determine a result, preserve the missing information.\n"
            "Write expressions that work on these partial records; do not return case answers or\n"
            "invent default answers. No authored formulas or expected results are supplied.\n\n" + encoded(public))


def bank_sha(bank):
    return hashlib.sha256(encoded(bank).encode()).hexdigest() if bank is not None else "-"


def assess(form, year, lines, context, prompt):
    bank = load(form, year)
    if bank is None:
        return {"policy": POLICY, "bank_sha256": "-", "request_context": "not applicable", "state": "not applicable", "cases": []}
    request_context = "included" if public_prompt(bank) in prompt else "absent"
    payload = {"form": form, "lines": lines, "context": context, "cases": cases(bank)}
    result = subprocess.run(["node", "--max-old-space-size=256", str(ROOT / "tools/transcription/check_input_contracts.mjs")],
                            input=json.dumps(payload, allow_nan=False), text=True, capture_output=True, timeout=30)
    if result.returncode:
        raise RuntimeError("partial-input checker failed: " + result.stderr[-500:])
    answer = json.loads(result.stdout)
    return {**answer, "policy": POLICY, "bank_sha256": bank_sha(bank), "request_context": request_context}
