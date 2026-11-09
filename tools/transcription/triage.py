#!/usr/bin/env python3
"""Executable triage of transcription disagreements.

For each disagreement in a transcription log, open or ruled, evaluate the project's line and the model's
validated candidate line on the same inputs: every fixture case, a deterministic sample of
generated returns, and partial records that withhold one answer the reviewed document asks.
The result is evidence for adjudication, not a ruling: agreement on every input run is observed
equivalence on that sample, and each difference comes with witness inputs and both values.
`bank.return_states` counts the sample by return state; `kinds_by_return` counts only the differences,
so it is not the size of the completed sample. A reply with invalid declarations is executed line by line
(T-143): valid lines are compared, and a pair whose candidate line or dependency failed schema, type or
reference validation is reported as `candidate-invalid` and listed in `invalid_lines`.

Each section is evaluated against the reply that judged it, as the committed review log records it, so
triage runs in a checkout without the git-ignored review data. A section the log marks "Reviewed in: pass <id>"
was judged in a line-scoped pass: its candidate comes from that pass's recorded reply (its receipt under
.transcription/, when this checkout holds it, must answer the block's prompt hash and equal the recorded reply;
a receipt it lacks is recorded as `receipt_verified: false`), with the project's other computed lines
spliced in beside it as compare() splices them for type validation, so a scoped line the reply omits stays
missing. Every other section is evaluated against the whole-form reply. Each reply is evaluated in its own
run. A record with line-scoped sections lists each pass under `passes` and marks its lines with `pass`;
the top-level response, state, bank and errors are the whole-form reply's. Triage refuses a form when a
pass reply cannot be found, verified or parsed.

Usage: triage.py --form sd [--family deepseek] [--generated 500] [--seed 20261026] [--partial-bases 40]
       triage.py --form sd [--family deepseek] --explain <handle> [--witness N] [--completed] [--depth 6]
--completed indexes the line's separate sample of witnesses on completed returns.
Writes .transcription/triage/<year>/<stem>.json (New York: .transcription/triage/ny/<year>/), git-ignored and
regenerated on demand; a ruling keeps only a compact stamp of the line it relied on (rulings.triage_stamp).
Raw replies are read, never changed.
"""
import argparse, hashlib, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import transcribe as T  # noqa: E402

ROOT = T.ROOT
POLICY = "executable-triage-v2"
OUT = rulings.TRIAGE_DIR  # git-ignored: regenerated on demand, never committed
RAW_HEADING = "## Raw second transcription"


def disagreement_handles(form, family):
    """The printed handles of the log's disagreeing or missing sections, ruled or open, so a record
    regenerated after ruling still covers the lines its rulings cite."""
    text = rulings.read_log("transcription", form, family)
    body = text.partition("\n## Lines\n")[2].partition("\n## Raw ")[0]
    handles = []
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        if "Status: **AGREE**" in content:
            continue
        status = "MISSING" if "Status: **MISSING**" in content else "DISAGREE"
        handles.append((title.split(" — ")[0], status, "Ruling: open" in content))
    return handles


def line_scoped_sections(form, family, only=None):
    """{handle: pass id} for each disagreeing or missing section judged in a line-scoped pass, not in the
    whole-form review: from the form's index, the pass of the record each line's verdict comes from
    (review_store.line_passes); for a log kept as a plain file, the "Reviewed in: pass <id>" tag of its
    section. A form with no log has no such sections."""
    import review_store
    passes = review_store.line_passes("transcription", form, family)
    if passes is not None:
        return {k: v["pass"] for k, v in passes.items()
                if v["pass"] and v["status"] != "AGREE" and (only is None or k == only)}
    text = rulings.read_log("transcription", form, family)
    if text is None:
        return {}
    body = text.partition("\n## Lines\n")[2].partition("\n## Raw ")[0]
    found = {}
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        handle = title.split(" — ")[0]
        if "Status: **AGREE**" in content or (only is not None and handle != only):
            continue
        tag = T.TAG_RE.search(content)
        if tag:
            found[handle] = tag.group(1)
    return found


def refuse_line_scoped(form, family, found):
    """Exit, naming each section ({handle: "pass id: reason"}) whose pass reply is unavailable."""
    if found:
        raise SystemExit(f"{families.stem(form, family)}: cannot triage these sections, whose line-scoped pass reply "
                         f"cannot be found, verified or parsed (the whole-form reply is not the evidence they came from): "
                         + "; ".join(f"{h} (pass {why})" for h, why in sorted(found.items())))


class Unavailable(Exception):
    """A line-scoped pass whose reply cannot be found, verified against the log, or parsed."""


def pass_blocks(form, family):
    """{pass id: block text} of the log's line-scoped reviews."""
    text = rulings.read_log("transcription", form, family)
    return T._log_parts(text, RAW_HEADING)[4]


def load_pass(form, pid, block, doc):
    """{raw, receipt, scope keys, scope ids, own lines} of line-scoped pass `pid`. The reply is the
    block's receipt, accepted only when its recorded prompt hash is the block's and its text is the
    reply the block records; the scope is the block's review scope, mapped to the current form."""
    if block is None:
        raise Unavailable("the log has no block for it")
    def row(name):
        m = re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", block, re.M)
        return m.group(1) if m else None
    receipt, prompt_sha, scope = row("receipt"), row("prompt sha256"), row("review scope")
    if not receipt or not prompt_sha or not scope or not scope.startswith("lines "):
        raise Unavailable("its block records no receipt, prompt sha256 or review scope")
    raw = rulings._fenced(block, "\n##### Raw second transcription\n\n```yaml\n")
    if raw is None:
        raise Unavailable("its block records no reply")
    verified = verify_receipt(receipt, prompt_sha, raw)
    keys = dict(T.line_keys(doc))
    names = scope[len("lines "):].split(", ")
    unknown = [k for k in names if k not in keys]
    if unknown:
        raise Unavailable("its scope names lines the form no longer compares: " + ", ".join(unknown))
    try:
        own = own_lines(form, doc, raw)
    except (ValueError, T.yaml.YAMLError) as ex:
        raise Unavailable(f"its reply cannot be parsed: {ex}")
    return {"raw": raw, "receipt": receipt, "verified": verified, "scope": names, "scope_ids": {keys[k] for k in names},
            "own": own}


def verify_receipt(receipt, prompt_sha, raw):
    """Check a pass's receipt in the git-ignored review data against the reply the log records: True when
    its metadata answers the block's prompt and its reply is the recorded one, False when this checkout does
    not hold it (the reply is then read from the log alone); a receipt that contradicts the log refuses."""
    response, meta = os.path.join(ROOT, receipt + ".response.txt"), os.path.join(ROOT, receipt + ".meta.json")
    if not os.path.exists(response) or not os.path.exists(meta):
        return False
    if json.load(open(meta, encoding="utf-8")).get("prompt_sha256") != prompt_sha:
        raise Unavailable(f"{receipt} answers a different request")
    if open(response, encoding="utf-8").read().strip() != raw.strip():
        raise Unavailable(f"{receipt}.response.txt is not the reply the log records")
    return True


def whole_reply(form, family):
    """The whole-form reply the log records (its "## Raw second transcription"), else exit."""
    text = rulings.read_log("transcription", form, family)
    raw = rulings.section_reply("transcription", text, "", "")
    if raw is None:
        raise SystemExit(f"{families.stem(form, family)}: the transcription log records no whole-form reply")
    return raw


def own_lines(form, doc, raw):
    """The reply's lines, with a definition's own namespace normalized as compare() does."""
    second = T.extract_yaml(raw)["lines"]
    if form in T.load_defs():
        second = T.normalize_definition_ids(form, doc["lines"], second)
    return second


def executed_lines(doc, own, scope_ids=None):
    """The lines triage executes: the reply's own, and for a line-scoped pass the project's other
    computed lines beside them (transcribe.support_lines)."""
    return own if scope_ids is None else own + T.support_lines(doc["lines"], own, scope_ids)


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


def evaluate(stem, form, doc, lines, pairs, generated, seed, partial_bases, max_witnesses):
    """triage.mjs's answer for the pairs with a candidate, evaluated on `lines` in one run."""
    evaluable = [p for p in pairs if p["candidate"]]
    if not evaluable:
        return {"state": "no candidate lines", "errors": [], "lines": []}
    payload = {"context": T.model_type_context(), "form": form, "lines": lines, "pairs": [{k: p[k] for k in ("handle", "project", "candidate", "shown_when")} for p in evaluable],
               "ownInputs": [l["id"] for l in doc["lines"] if l["expr"].get("op") == "input"],
               "generated": generated, "seed": seed, "partialBases": partial_bases, "maxWitnesses": max_witnesses}
    result = subprocess.run(["node", "--max-old-space-size=4096", os.path.join(ROOT, "tools", "transcription", "triage.mjs")],
                            input=json.dumps(payload, allow_nan=False), text=True, capture_output=True, timeout=3600)
    if result.returncode:
        raise SystemExit(f"{stem}: triage evaluator failed: {result.stderr[-1500:]}")
    return json.loads(result.stdout)


def run_summary(answer):
    return {"state": answer["state"], "errors": answer.get("errors", []), "invalid_lines": answer.get("invalid_lines", []),
            "bank": answer.get("bank"), "failures": answer.get("failures", [])}


def verdicts(pairs, answer):
    """{handle: record line} of one run."""
    evaluated = {l["handle"]: l for l in answer.get("lines", [])}
    out = {}
    for p in pairs:
        line = evaluated.get(p["handle"], {})
        if p["candidate"] is None:
            verdict = "missing"
        elif answer["state"] != "evaluated":
            verdict = "candidate invalid"
        elif line.get("invalid"):
            verdict = "candidate invalid"
        elif not line.get("compared"):
            verdict = "not reached"
        elif line["differ"]:
            verdict = "differs"
        else:
            verdict = "agrees on sample"
        out[p["handle"]] = {**p, "triage": verdict, **{k: v for k, v in line.items() if k not in p}}
    return out


def triage(form, family, generated, seed, partial_bases, max_witnesses=6):
    stem = families.stem(form, family)
    doc = T.load_form(form)
    handles = disagreement_handles(form, family)
    tagged = line_scoped_sections(form, family)
    groups = {}
    for h in handles:
        groups.setdefault(tagged.get(h[0]), []).append(h)
    passes = sorted(pid for pid in groups if pid is not None)
    loaded, refused = {}, {}
    if passes:
        blocks = pass_blocks(form, family)
        for pid in passes:
            try:
                loaded[pid] = load_pass(form, pid, blocks.get(pid), doc)
            except Unavailable as ex:
                refused.update({h[0]: f"{pid}: {ex}" for h in groups[pid]})
    refuse_line_scoped(form, family, refused)
    record = {"policy": POLICY, "form": form, "family": family,
              "log_sha256_at_triage": hashlib.sha256(rulings.read_log("transcription", form, family).encode()).hexdigest(),
              "subject_sha256": T.subjects.current("transcription", form, T.Y),
              "scope": "host-only executable triage; evidence for adjudication, no qualification or scoreboard credit"}
    found = {}
    if None in groups or not passes:
        raw = whole_reply(form, family)
        second = own_lines(form, doc, raw)
        pairs = pairs_for(form, doc["lines"], second, groups.get(None, []))
        answer = evaluate(stem, form, doc, second, pairs, generated, seed, partial_bases, max_witnesses)
        record.update({"response_sha256": T.response_sha256(raw), **run_summary(answer)})
        found.update(verdicts(pairs, answer))
    else:
        record.update({"response_sha256": None, "state": "no whole-form sections", "errors": [], "invalid_lines": [],
                       "bank": None, "failures": []})
    if passes:
        record["passes"] = {}
        for pid in passes:
            got = loaded[pid]
            pairs = pairs_for(form, doc["lines"], got["own"], groups[pid])
            lines = executed_lines(doc, got["own"], got["scope_ids"])
            answer = evaluate(stem, form, doc, lines, pairs, generated, seed, partial_bases, max_witnesses)
            record["passes"][pid] = {"response_sha256": T.response_sha256(got["raw"]), "receipt": got["receipt"],
                                     **({} if got["verified"] else {"receipt_verified": False}),
                                     "review_scope": got["scope"], **run_summary(answer)}
            found.update({h: {**line, "pass": pid} for h, line in verdicts(pairs, answer).items()})
    record["lines"] = [found[h[0]] for h in handles]
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, stem + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=1, sort_keys=True)
        f.write("\n")
    return path, record


def explain(form, family, handle, witness, depth, completed=False):
    """Rebuild one recorded witness and print both derivation trees of the disputed line."""
    stem = families.stem(form, family)
    record = json.load(open(os.path.join(OUT, stem + ".json"), encoding="utf-8"))
    line = next((l for l in record["lines"] if l["handle"] == handle), None)
    if line is None:
        raise SystemExit(f"{stem}: no line {handle!r} in the triage record")
    pid = line.get("pass")
    state = record["passes"][pid] if pid else record
    which = "completed_witnesses" if completed else "witnesses"
    found = line.get(which) or []
    if not found:
        raise SystemExit(f"{stem}: line {handle!r} has no {which.replace('_', ' ')} (triage: {line['triage']}"
                         + (f"; {state['state']}: {state.get('errors')}" if state.get("state") != "evaluated" else "") + ")")
    if not 0 <= witness < len(found):
        raise SystemExit(f"{stem}: line {handle!r} has {len(found)} {which.replace('_', ' ')}; --witness {witness} is out of range")
    w = found[witness]
    now = line_scoped_sections(form, family, only=handle).get(handle)
    if now != pid:
        where = lambda p: f"pass {p}" if p else "the whole-form reply"
        raise SystemExit(f"{stem}: the triage record has {handle!r} from {where(pid)}, but the log now has it from {where(now)}; "
                         "rerun triage")
    doc = T.load_form(form)
    if pid is None:
        lines = own_lines(form, doc, whole_reply(form, family))
    else:
        try:
            got = load_pass(form, pid, pass_blocks(form, family).get(pid), doc)
        except Unavailable as ex:
            refuse_line_scoped(form, family, {handle: f"{pid}: {ex}"})
        lines = executed_lines(doc, got["own"], got["scope_ids"])
    payload = {"context": T.model_type_context(), "form": form, "lines": lines,
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
    ap.add_argument("--completed", action="store_true", help="index the witnesses on completed returns")
    ap.add_argument("--depth", type=int, default=6)
    a = ap.parse_args()
    if a.explain:
        return explain(a.form, a.family, a.explain, a.witness, a.depth, a.completed)
    path, record = triage(a.form, a.family, a.generated, a.seed, a.partial_bases)
    tally = {}
    for line in record["lines"]:
        tally[line["triage"]] = tally.get(line["triage"], 0) + 1
    passes = record.get("passes") or {}
    print(f"{families.stem(a.form, a.family)}: {record['state']}; {tally}; bank {record.get('bank')}"
          + "".join(f"; pass {pid}: {p['state']}, bank {p.get('bank')}" for pid, p in passes.items())
          + f" -> {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
