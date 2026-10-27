#!/usr/bin/env python3
"""Executable triage of transcription disagreements.

For each disagreement in a transcription log, open or ruled, evaluate the project's line and the model's
validated candidate line on the same inputs: every fixture case, a deterministic sample of
generated returns, and partial records that withhold one answer the reviewed document asks.
The result is evidence for adjudication, not a ruling: agreement on every input run is observed
equivalence on that sample, and each difference comes with witness inputs and both values.

Usage: triage.py --form sd [--family deepseek] [--generated 500] [--seed 20261026] [--partial-bases 40]
       triage.py --form sd [--family deepseek] --explain <handle> [--witness N] [--depth 6]
Writes reviews/<year>/transcription/triage/<stem>.json. Raw replies are read, never changed.
"""
import argparse, hashlib, json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import transcribe as T  # noqa: E402

ROOT = T.ROOT
POLICY = "executable-triage-v2"
OUT = os.path.join(ROOT, "reviews", T.Y, "transcription", "triage")


def disagreement_handles(form, family):
    """The printed handles of the log's disagreeing or missing sections, ruled or open, so a record
    regenerated after ruling still covers the lines its rulings cite."""
    text = open(rulings.log_path("transcription", form, family), encoding="utf-8").read()
    body = text.partition("\n## Lines\n")[2].partition("\n## Raw ")[0]
    handles = []
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        if "Status: **AGREE**" in content:
            continue
        status = "MISSING" if "Status: **MISSING**" in content else "DISAGREE"
        handles.append((title.split(" — ")[0], status, "Ruling: open" in content))
    return handles


def pairs_for(form, project_lines, second_lines, handles):
    """Map each handle to the project's line id and the candidate's line id, as compare() keys them."""
    exported = {l["id"] for l in T.exported_lines({"id": form, "lines": project_lines})}
    inputs = {l["id"]: l for l in project_lines if l["expr"].get("op") == "input"}
    pkeys = T.marker_keys(project_lines)
    skeys = {**{i: pkeys[i] for i in inputs}, **T.marker_keys(second_lines)}
    by_id = {l["id"]: l for l in second_lines}
    by_printed = {skeys[l["id"]]: l for l in second_lines if l["printed"] not in T.HELPER_PRINTED}
    shown = {l["id"]: l.get("shown_when") for l in project_lines}
    by_handle = {pkeys[l["id"]]: l["id"] for l in project_lines
                 if l["printed"] not in T.HELPER_PRINTED and l["expr"].get("op") != "input"}
    out = []
    for handle, status, is_open in handles:
        if handle in exported:
            project, second = handle, by_id.get(handle)
        else:
            project, second = by_handle.get(handle), by_printed.get(handle)
        if project is None:
            raise SystemExit(f"{form}: cannot map open section {handle!r} to a project line")
        out.append({"handle": handle, "status": status, "open_at_triage": is_open, "project": project,
                    "candidate": second["id"] if second else None, "shown_when": shown.get(project)})
    return out


def triage(form, family, generated, seed, partial_bases, max_witnesses=6):
    stem = families.stem(form, family)
    raw_path = os.path.join(ROOT, ".transcription", stem + ".response.txt")
    raw = open(raw_path, encoding="utf-8").read()
    doc = T.load_form(form)
    second = T.extract_yaml(raw)["lines"]
    if form in T.load_defs():
        second = T.normalize_definition_ids(form, doc["lines"], second)
    handles = disagreement_handles(form, family)
    pairs = pairs_for(form, doc["lines"], second, handles)
    record = {"policy": POLICY, "form": form, "family": family,
              "response_sha256": hashlib.sha256(raw.encode()).hexdigest(),
              "log_sha256_at_triage": hashlib.sha256(open(rulings.log_path("transcription", form, family), "rb").read()).hexdigest(),
              "subject_sha256": T.subjects.current("transcription", form, T.Y),
              "scope": "host-only executable triage; evidence for adjudication, no qualification or scoreboard credit"}
    evaluable = [p for p in pairs if p["candidate"]]
    if evaluable:
        payload = {"context": T.model_type_context(), "form": form, "lines": second, "pairs": [{k: p[k] for k in ("handle", "project", "candidate", "shown_when")} for p in evaluable],
                   "ownInputs": [l["id"] for l in doc["lines"] if l["expr"].get("op") == "input"],
                   "generated": generated, "seed": seed, "partialBases": partial_bases, "maxWitnesses": max_witnesses}
        result = subprocess.run(["node", "--max-old-space-size=4096", os.path.join(ROOT, "tools", "transcription", "triage.mjs")],
                                input=json.dumps(payload, allow_nan=False), text=True, capture_output=True, timeout=3600)
        if result.returncode:
            raise SystemExit(f"{stem}: triage evaluator failed: {result.stderr[-1500:]}")
        answer = json.loads(result.stdout)
    else:
        answer = {"state": "no candidate lines", "errors": [], "lines": []}
    evaluated = {l["handle"]: l for l in answer.get("lines", [])}
    record.update({"state": answer["state"], "errors": answer.get("errors", []), "bank": answer.get("bank"),
                   "failures": answer.get("failures", []), "lines": []})
    for p in pairs:
        line = evaluated.get(p["handle"], {})
        if p["candidate"] is None:
            verdict = "missing"
        elif answer["state"] != "evaluated":
            verdict = "candidate invalid"
        elif not line.get("compared"):
            verdict = "not reached"
        elif line["differ"]:
            verdict = "differs"
        else:
            verdict = "agrees on sample"
        record["lines"].append({**p, "triage": verdict, **{k: v for k, v in line.items() if k not in p}})
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, stem + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=1, sort_keys=True)
        f.write("\n")
    return path, record


def explain(form, family, handle, witness, depth):
    """Rebuild one recorded witness and print both derivation trees of the disputed line."""
    stem = families.stem(form, family)
    record = json.load(open(os.path.join(OUT, stem + ".json"), encoding="utf-8"))
    line = next(l for l in record["lines"] if l["handle"] == handle)
    w = line["witnesses"][witness]
    raw = open(os.path.join(ROOT, ".transcription", stem + ".response.txt"), encoding="utf-8").read()
    doc = T.load_form(form)
    second = T.extract_yaml(raw)["lines"]
    if form in T.load_defs():
        second = T.normalize_definition_ids(form, doc["lines"], second)
    payload = {"context": T.model_type_context(), "form": form, "lines": second,
               "pairs": [{"handle": handle, "project": line["project"], "candidate": line["candidate"]}],
               "ownInputs": [], "generated": 0, "seed": 0, "partialBases": 0, "maxWitnesses": 0,
               "explain": {"handle": handle, "source": w["source"], "instance": w["instance"], "depth": depth}}
    result = subprocess.run(["node", "--max-old-space-size=4096", os.path.join(ROOT, "tools", "transcription", "triage.mjs")],
                            input=json.dumps(payload, allow_nan=False), text=True, capture_output=True, timeout=600)
    if result.returncode:
        raise SystemExit(result.stderr[-1500:])
    print(json.dumps({"kind": w["kind"], **json.loads(result.stdout)}, indent=1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--family", default=families.DEFAULT)
    ap.add_argument("--generated", type=int, default=500)
    ap.add_argument("--seed", type=int, default=20261026)
    ap.add_argument("--partial-bases", type=int, default=40)
    ap.add_argument("--explain", metavar="HANDLE", help="print both derivation trees for one recorded witness")
    ap.add_argument("--witness", type=int, default=0, help="index of the witness to explain")
    ap.add_argument("--depth", type=int, default=6)
    a = ap.parse_args()
    if a.explain:
        return explain(a.form, a.family, a.explain, a.witness, a.depth)
    path, record = triage(a.form, a.family, a.generated, a.seed, a.partial_bases)
    tally = {}
    for line in record["lines"]:
        tally[line["triage"]] = tally.get(line["triage"], 0) + 1
    print(f"{families.stem(a.form, a.family)}: {record['state']}; {tally}; bank {record.get('bank')} -> {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
