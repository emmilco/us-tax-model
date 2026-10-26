"""Engineering contracts for internal adapters; never independent tax evidence.

The registry is host-only. Blind requests omit these targets and their behavior.
Historical review logs and rulings remain intact, with excluded rows visible in
comparison reports. Empty source reviews cannot become passing assertions.
"""
import json
from pathlib import Path
import subprocess

DIRECTORY = Path(__file__).resolve().parent / "adapter_contracts"
POLICY = "internal-adapters-v1"
REQUIRED = {"2025": {"div"}}


def load(form, year):
    path = DIRECTORY / str(year) / f"{form}.json"
    if not path.exists():
        if form in REQUIRED.get(str(year), set()):
            raise FileNotFoundError("required adapter contract is missing: " + str(path))
        return None
    bank = json.loads(path.read_text())
    if bank["form"] != form or bank["tax_year"] != int(year) or bank["policy"] != POLICY:
        raise ValueError("adapter-contract identity mismatch")
    if not bank.get("adapters") or not bank.get("cases") or len(bank["cases"]) > 32:
        raise ValueError("empty or oversized adapter contract")
    if len({test["id"] for test in bank["cases"]}) != len(bank["cases"]):
        raise ValueError("duplicate adapter case id")
    if {test["adapter"] for test in bank["cases"]} != set(bank["adapters"]):
        raise ValueError("adapter case coverage mismatch")
    for test in bank["cases"]:
        expected = test["expect"]
        kind = expected.get("kind")
        fields = {"money": {"kind", "cents"}, "refusal": {"kind", "gate"}, "unknown": {"kind", "input"}}
        if kind not in fields or set(expected) != fields[kind]:
            raise ValueError("incomplete adapter reference answer")
        if kind == "money" and (type(expected["cents"]) is not int or expected["cents"] < 0):
            raise ValueError("invalid adapter reference amount")
        if kind != "money":
            field = "gate" if kind == "refusal" else "input"
            if not isinstance(expected[field], str) or not expected[field]:
                raise ValueError("invalid adapter reference gate/input")
    return bank


def excluded_ids(form, year):
    bank = load(form, year)
    return set(bank["adapters"]) if bank else set()


def source_record(form, year, record):
    """A reporting projection only; never rewrite an original log or sidecar."""
    excluded = excluded_ids(form, year)
    return {**record, "lines": {key: row for key, row in record["lines"].items() if key not in excluded}}


def assess(form, year, context):
    bank = load(form, year)
    if bank is None:
        raise ValueError("no adapter contract for " + form)
    docs = {doc["id"]: doc for doc in context["forms"] + context["defs"]}
    lines = {line["id"]: line for doc in docs.values() for line in doc["lines"]}
    for target, contract in bank["adapters"].items():
        line = lines[target]
        if target.split(".")[0] != form or line["printed"] not in ("(helper)", "(gate)", "(computed helper)") or line["expr"]["op"] == "input":
            raise ValueError("only internal computed helpers may be adapter targets")
        if line["type"] != contract["type"]:
            raise ValueError("adapter type changed")
        consumers = {key for key, value in lines.items() if value["expr"] == {"op": "copy", "from": target}}
        if consumers != set(contract["copy_consumers"]):
            raise ValueError("adapter copy-consumer inventory changed")
    cases = [{"id": test["id"], "inputs": {**bank["base_inputs"], **test.get("inputs", {})},
              "expect": {target: test["expect"] for target in
                         [test["adapter"], *bank["adapters"][test["adapter"]]["copy_consumers"]]}}
             for test in bank["cases"]]
    payload = {"context": context, "form": form, "cases": cases}
    result = subprocess.run(["node", "--max-old-space-size=256", str(Path(__file__).with_name("check_adapters.mjs"))],
                            input=json.dumps(payload, allow_nan=False), text=True, capture_output=True, timeout=30)
    if result.returncode:
        raise RuntimeError("adapter checker failed: " + result.stderr[-500:])
    return {**json.loads(result.stdout), "policy": POLICY, "evidence_credit": False}


def main():
    import transcribe as T
    for form in sorted(REQUIRED.get(str(T.Y), set())):
        result = assess(form, T.Y, T.model_type_context())
        if result["state"] != "pass":
            print(json.dumps(result, indent=2))
            raise SystemExit(1)
        print(f"adapter {form}: {len(result['cases'])} engineering cases pass; no tax-evidence credit")


if __name__ == "__main__":
    main()
