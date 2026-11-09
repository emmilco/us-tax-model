#!/usr/bin/env python3
"""Compare two model families' review logs of the same form and write reports/<year>/second_family.md.

For every form that has both a Claude log and a second family's log of a kind (transcription,
render, class M; families.py), the lines judged in both logs are read and three things reported:

  noise rate         second-family disputes ruled model error / lines it judged, at most 10%
  raw agreement      diagnostic only; a correct objection never counts as model noise
  independence yield the lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where
                     the Claude log agreed or matched, each with the second family's reason
  both disputed      the lines both families disputed

A line one log judged and the other did not (MISSING, or absent from one log) is left out of the
floor and counted. A log whose subject hash is no longer current is marked stale in the table.
The report's "Summary:" line is also printed when the report is written.

While every second family is inactive (families.json `active`) the report is not rewritten: the last one
written stays as the record of the families' historical logs, and the run says so. Reactivating a family
resumes the comparison on the next run.

    python3 tools/transcription/compare_families.py
"""
import datetime, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402
import transcribe  # noqa: E402
import input_contracts  # noqa: E402
import adapter_contracts  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: reviews/ny/<year>/, reports/ny/<year>/)

REPORT = str(jurisdiction.ypath("reports", Y, "second_family.md"))
KINDS = ("transcription", "render", "classm")
AGREE = {"transcription": "AGREE", "render": "MATCH", "classm": "AGREE"}
TITLE = {"transcription": "Transcription agreement", "render": "Render comparison", "classm": "Class M hand-work"}


PASS_FIELDS = {"model": "model requested", "reported": "model reported", "policy": "prompt policy",
               "comparison_policy": "comparison policy", "type_policy": "type validation policy",
               "model_types": "model type validation", "input_context_policy": "input context policy",
               "complete_inputs": "complete input context", "input_context_sha256": "required input context sha256"}


def parse_log(kind, path):
    """The log's header fields and, per judged line, its status and the model's stated reason. A path that
    is a form's log (rulings.log_path) is read as the review store assembles it (rulings.read_log)."""
    form, family = families.split_stem(os.path.basename(path)[:-3])
    if os.path.abspath(path) == os.path.abspath(rulings.log_path(kind, form, family)):
        text = rulings.read_log(kind, form, family)
        if text is not None:
            return parse_log_text(kind, text)
    with open(path, encoding="utf-8") as f:
        return parse_log_text(kind, f.read())


def parse_log_text(kind, text):
    """parse_log of a log's text. `passes` holds, for each line-scoped review the log holds, the same
    header fields from that review's own record."""
    field = lambda name: (re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", text, flags=re.M) or [None, ""])[1]
    passes = {pid: {k: (re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", block, flags=re.M) or [None, ""])[1]
                    for k, name in PASS_FIELDS.items()}
              for pid, block in rulings.pass_blocks(text).items()}
    _, _, rest = text.partition("\n## Lines\n")
    body = re.split(r"\n## ", rest)[0]
    lines, duplicates = {}, []
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        parts = title.split(" — ")
        if kind == "classm":
            if title.startswith("case ") or len(parts) < 3:
                continue
            key = f"{parts[0]} — {parts[1]}"
        else:
            key = parts[0]
        m = re.search(r"^Status: \*\*(\w+)\*\*", content, flags=re.M)
        if not m:
            continue
        if kind == "transcription":
            note = re.search(r"^Second transcription's note: (.*)$", content, flags=re.M)
            reason = note.group(1) if note else ""
        elif kind == "render":
            note = re.search(r"^Model: (.*)$", content, flags=re.M)
            reason = note.group(1) if note else ""
        else:
            value = re.search(r"^Model: (.*)$", content, flags=re.M)
            work = re.search(r"^Work: (.*)$", content, flags=re.M)
            reason = (f"model gave {value.group(1)}" if value else "") + (f"; work: {work.group(1)}" if work else "")
        ruling = re.search(r"^Ruling: (.*)$", content, flags=re.M)
        if key in lines:
            duplicates.append(key)
        lines[key] = {"status": m.group(1), "reason": reason.strip(),
                      "ruling": ruling.group(1).strip() if ruling else ""}
    return {"model": field("model requested"), "reported": field("model reported"), "date": field("date"),
            "subject": field("subject sha256"), "policy": field("prompt policy"),
            "comparison_policy": field("comparison policy"), "lines": lines, "duplicates": duplicates,
            "type_policy": field("type validation policy"), "model_types": field("model type validation"),
            "input_context_policy": field("input context policy"), "complete_inputs": field("complete input context"),
            "input_context_sha256": field("required input context sha256"),
            "partial_policy": field("partial-input policy"), "partial_bank": field("partial-input bank sha256"),
            "partial_context": field("partial-input request context"), "partial_result": field("partial-input result"),
            "passes": passes, "text": text,
            "sources": re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|(?: [^|]* \| ([0-9a-f]{64}|-) \|)?$", text, flags=re.M)}


def ruling_category(ruling):
    """Classify an explicit ruling prefix; unclassified prose cannot silently pass."""
    for category, pattern in (("model_error", r"model[ _-]error\b"),
                              ("interface_gap", r"interface[ _-]gap\b"),
                              ("representation", r"representation\b|equivalent\b"),
                              ("finding", r"finding\b|project[ _-](?:error|corrected)\b|correction\b"),
                              ("scope", r"scope\b"),
                              ("ambiguity", r"ambiguity\b|owner's ruling\b")):
        if re.match(pattern, ruling, re.I):
            return category
    return "open" if not ruling or ruling.lower() == "open" else "unclassified"


def quality(kind, expected, second, stale=()):
    """The owner's decision 12: noise is ruled model error, never disagreement itself.

    Open, missing, malformed and unclassified results remain pending. Empty forms
    have no assertion to credit. The threshold is checked with integer arithmetic.
    """
    agree = AGREE[kind]
    valid = {agree, "DISAGREE" if kind != "render" else "MISMATCH", "MISSING"}
    if kind == "render":
        valid.add("UNCLEAR")
    if kind == "classm":
        valid.add("SKIPPED")
    expected_keys = set(expected["lines"])
    required_keys = {k for k in expected_keys if expected["lines"][k]["status"] != "SKIPPED"}
    unexpected = sorted(set(second["lines"]) - expected_keys)
    judged = {k for k, line in second["lines"].items() if k in expected_keys and line["status"] in valid - {"MISSING", "SKIPPED"}}
    missing = sorted(required_keys - judged)
    invalid = sorted(k for k, line in second["lines"].items() if line["status"] not in valid)
    categories = {k: ruling_category(second["lines"][k].get("ruling", "")) for k in judged
                  if second["lines"][k]["status"] != agree}
    noisy = sorted(k for k, category in categories.items() if category == "model_error")
    pending = sorted(k for k, category in categories.items() if category in ("open", "unclassified", "interface_gap"))
    blockers = []
    if stale:
        blockers.append("stale subject: " + ", ".join(stale))
    if missing:
        blockers.append(f"{len(missing)} missing expected lines")
    if invalid:
        blockers.append(f"{len(invalid)} invalid verdicts")
    if unexpected:
        blockers.append(f"{len(unexpected)} unexpected line keys")
    if second.get("duplicates"):
        blockers.append("duplicate line keys")
    if pending:
        blockers.append(f"{len(pending)} open, unclassified or interface-gap rulings")
    below = len(noisy) * 10 > len(judged)
    if below:
        blockers.append("model-error noise above 10%")
    state = "pending" if blockers else "pass" if judged else "no lines"
    return {"state": state, "judged": len(judged), "model_errors": len(noisy), "categories": categories,
            "missing": missing, "unexpected": unexpected, "pending": pending, "blockers": blockers, "above_limit": below}


def model_blockers(kind, family, log):
    reported = [m.strip() for m in log["reported"].split(",") if m.strip()]
    blockers = []
    if families.family_of(log["model"]) != family or not reported or any(families.family_of(m) != family for m in reported):
        blockers.append("requested/reported model is not the named second family")
    selected = families.selected_model(family, kind)
    if selected and (log["model"] != selected or any(m != selected for m in reported)):
        blockers.append(f"review is not from selected model {selected}")
    return blockers


def pass_blockers(kind, family, p):
    """Why a line-scoped review recorded in a log cannot share the credit of the log's header review:
    the conditions compare() puts on a header, read from the pass's own record. `family` is the
    second family's name, or None for the Claude log (whose model is not checked against a family)."""
    out = []
    if family is not None:
        out += model_blockers(kind, family, p)
    if kind != "transcription":
        return out
    if p["policy"] not in transcribe.INDEPENDENT_LINE_PROMPT_POLICIES:
        out.append("predates the prompt-independence policy")
    if p["comparison_policy"] != transcribe.COMPARISON_POLICY:
        out.append("predates unit-preserving comparison")
    if p["type_policy"] != transcribe.TYPE_VALIDATION_POLICY or p["model_types"] != "pass":
        out.append("no passing current expression type validation")
    if p["input_context_policy"] != transcribe.INPUT_CONTEXT_POLICY or p["complete_inputs"] != "pass":
        out.append("no verified complete input context in the request")
    return out


def compare(kind, form, family):
    a = parse_log(kind, rulings.log_path(kind, form, families.DEFAULT))
    b = parse_log(kind, rulings.log_path(kind, form, family))
    excluded = adapter_contracts.excluded_ids(form, Y) if kind == "transcription" else set()
    if excluded:
        a = adapter_contracts.source_record(form, Y, a)
        b = adapter_contracts.source_record(form, Y, b)
    agree = AGREE[kind]
    shared = sorted(set(a["lines"]) & set(b["lines"]))
    judged = [k for k in shared if a["lines"][k]["status"] not in ("MISSING", "SKIPPED")
              and b["lines"][k]["status"] not in ("MISSING", "SKIPPED")]
    both_agree = [k for k in judged if a["lines"][k]["status"] == agree and b["lines"][k]["status"] == agree]
    yield_ = [k for k in judged if a["lines"][k]["status"] == agree and b["lines"][k]["status"] != agree]
    both_disputed = [k for k in judged if a["lines"][k]["status"] != agree and b["lines"][k]["status"] != agree]
    claude_only = [k for k in judged if a["lines"][k]["status"] != agree and b["lines"][k]["status"] == agree]
    try:
        current = subjects.current(kind, form, Y)
    except FileNotFoundError:
        current = None
    # A log holding line-scoped reviews or a line-subject table is current when every compared line's
    # subject is (the rule check_logs.py applies); its header keeps the subject its first review saw.
    stale = [fam for fam, log in ((families.DEFAULT, a), (family, b))
             if current is None or (subjects.log_state(kind, form, Y, log["text"]) is not None
                                    if log.get("passes") or subjects.recorded(log.get("text") or "") is not None
                                    else log["subject"] != current)]
    q = quality(kind, a, b, stale)
    for fam, record in ((families.DEFAULT, a), (family, b)):
        for pid, p in sorted((record.get("passes") or {}).items()):
            q["blockers"] += [f"pass {pid} of {fam}: {x}" for x in pass_blockers(kind, fam if fam != families.DEFAULT else None, p)]
    if excluded and not judged:
        q["blockers"].append("no source-defined computed targets; internal adapter checks earn no tax-evidence credit")
    if kind == "transcription":
        # BUG-0129's global hold is replaced by the per-form conditions below (owner's decision,
        # 2026-10-27): a log qualifies only under the unit-preserving comparison, passing current
        # type validation, complete input context and a live check of its bound request.
        required_targets=transcribe.required_target_keys(transcribe.load_form(form))
        for fam, record in ((families.DEFAULT,a),(family,b)):
            absent=sorted(required_targets-set(record['lines']))
            if absent:
                q['blockers'].append(f"current source targets not judged by {fam}: "+', '.join(absent))
        legacy = [fam for fam, record in ((families.DEFAULT, a), (family, b))
                  if record.get("comparison_policy") != transcribe.COMPARISON_POLICY]
        if legacy:
            q["blockers"].append("transcription predates unit-preserving comparison; verified re-comparison required: " + ", ".join(legacy))
        unchecked = [fam for fam, record in ((families.DEFAULT, a), (family, b))
                     if record.get("type_policy") != transcribe.TYPE_VALIDATION_POLICY or record.get("model_types") != "pass"]
        if unchecked:
            q["blockers"].append("no passing current expression type validation: " + ", ".join(unchecked))
        incomplete = [fam for fam, record in ((families.DEFAULT, a), (family, b))
                      if record.get("input_context_policy") != transcribe.INPUT_CONTEXT_POLICY or record.get("complete_inputs") != "pass"]
        if incomplete:
            q["blockers"].append("no verified complete input context in the request: " + ", ".join(incomplete))
        # A recorded pass cannot stay current merely because this form's own
        # subject is unchanged: a foreign input/interface may have changed.
        # Recheck the actual bound request/reply, including current types.
        import audit_transcription
        from pathlib import Path
        for fam, record in ((families.DEFAULT, a), (family, b)):
            if record.get("input_context_policy") != transcribe.INPUT_CONTEXT_POLICY or record.get("complete_inputs") != "pass":
                continue
            try:
                replay = audit_transcription.audit(Path(rulings.log_path(kind, form, fam)))
                if replay["request_provenance"] != "bound":
                    raise ValueError("request metadata is legacy-limited")
                if replay["type_errors"]:
                    raise ValueError("current expression/refusal validation fails")
                if replay["input_context"]["state"] != "pass":
                    raise ValueError("required input/interface wording is missing or stale")
                if record.get("input_context_sha256") != replay["input_context"]["required_sha256"]:
                    raise ValueError("required input/interface hash differs")
                # Each line-scoped review the log holds is verified like the header review.
                checked = {r["pass"]: r for r in replay.get("passes", [])}
                for pid, p in sorted((record.get("passes") or {}).items()):
                    r = checked.get(pid)
                    if r is None:
                        raise ValueError(f"pass {pid} was not verified")
                    if r["request_provenance"] != "bound":
                        raise ValueError(f"pass {pid}: request metadata is legacy-limited")
                    if r["type_errors"]:
                        raise ValueError(f"pass {pid}: current expression/refusal validation fails")
                    if r["input_context"]["state"] != "pass":
                        raise ValueError(f"pass {pid}: required input/interface wording is missing or stale")
                    if p.get("input_context_sha256") != r["input_context"]["required_sha256"]:
                        raise ValueError(f"pass {pid}: required input/interface hash differs")
            except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
                q["blockers"].append(f"no verified current request context for {fam}: {exc}")
        bank = input_contracts.load(form, Y)
        if bank:
            untested = [fam for fam, record in ((families.DEFAULT, a), (family, b))
                        if record.get("partial_policy") != input_contracts.POLICY
                        or record.get("partial_bank") != input_contracts.bank_sha(bank)
                        or record.get("partial_context") != "included" or record.get("partial_result") != "pass"]
            if untested:
                q["blockers"].append("no passing current source-based partial-input checks: " + ", ".join(untested))
    if kind == "transcription" and b["policy"] not in transcribe.INDEPENDENT_PROMPT_POLICIES:
        q["blockers"].append("transcription predates the prompt-independence policy")
    q["blockers"].extend(model_blockers(kind, family, b))
    sources = transcribe.manifest()  # in New York mode the New York and the federal documents
    if q["judged"] and not b["sources"]:
        q["blockers"].append("no archived source snapshots recorded")
    for doc, sha, cols_sha in b["sources"]:
        source = sources.get(doc)
        if not source or source["text_sha256"] != sha or (cols_sha and cols_sha != "-" and source.get("cols_sha256") != cols_sha):
            q["blockers"].append(f"stale source snapshot: {doc}")
    if q["blockers"]:
        q["state"] = "pending"
    return {"kind": kind, "form": form, "family": family, "a": a, "b": b, "shared": shared, "judged": judged,
            "both_agree": both_agree, "yield": yield_, "both_disputed": both_disputed, "claude_only": claude_only,
            "unjudged": len(set(a["lines"]) ^ set(b["lines"])) + len(shared) - len(judged),
            "stale": stale, "quality": q, "excluded_adapters": sorted(excluded)}


# The blockers a change since the review causes: its subject or a source snapshot moved on, the form gained
# a target, or a foreign input's wording changed. A rerun of the review clears them; the other blockers say
# the review would not earn credit even if it were current.
CURRENCY = re.compile(r"stale subject: |stale source snapshot: |current source targets not judged by "
                      r"|no verified current request context for .*(required input/interface wording is missing "
                      r"or stale|required input/interface hash differs)")


def eligible_when_current(q):
    """(eligible, blockers) for a compare() quality: whether the second family's log would earn credit if it
    were current, and the blockers other than currency that stop it."""
    other = [b for b in q["blockers"] if not CURRENCY.match(b)]
    return not other, other


def pct(n, d):
    return f"{100 * n / d:.1f}%" if d else "n/a"


def floor_mark(r):
    return r["quality"]["state"]


def pairs():
    out = []
    for kind in KINDS:
        logs = rulings.forms_with_logs(kind)
        claude = {form for form, fam in logs if fam == families.DEFAULT}
        for form, fam in logs:
            if fam != families.DEFAULT and form in claude:
                out.append((kind, form, fam))
    return out


def main():
    known = families.load()
    if not any(on for fam, on in known["active"].items() if fam != families.DEFAULT):
        kept = "is kept as last written" if os.path.exists(REPORT) else "does not exist"
        print(f"second_family: every second family is inactive (tools/transcription/families.json); "
              f"{os.path.relpath(REPORT, ROOT)} {kept} and is not regenerated")
        return
    results = [compare(kind, form, fam) for kind, form, fam in pairs() if families.is_active(fam)]
    fams = sorted({r["family"] for r in results})
    judged = sum(len(r["judged"]) for r in results)
    agreed = sum(len(r["both_agree"]) for r in results)
    yield_n = sum(len(r["yield"]) for r in results)
    both_n = sum(len(r["both_disputed"]) for r in results)
    passing = sum(1 for r in results if floor_mark(r) == "pass")
    pending = sum(1 for r in results if floor_mark(r) == "pending")
    noise_n = sum(r["quality"]["model_errors"] for r in results)
    noise_d = sum(r["quality"]["judged"] for r in results)
    if results:
        summary = (f"{len(results)} form-kind pair(s) with logs from Claude and {', '.join(fams)}; "
                   f"ruled model-error noise {pct(noise_n, noise_d)} ({noise_n}/{noise_d} second-family lines judged; pending reviews are provisional); "
                   f"{passing} eligible, {pending} pending; raw agreement {pct(agreed, judged)} (diagnostic only); "
                   f"current independence yield {yield_n} line(s); both families disputed {both_n}")
    else:
        summary = "no second-family logs yet"
    out = [f"# Second-family review comparison — {Y}{jurisdiction.label()}", "",
           f"Summary: {summary}", "",
           f"Written by `tools/transcription/compare_families.py` on {datetime.date.today().isoformat()} from the review logs under `{jurisdiction.ypath('reviews', Y).relative_to(jurisdiction.ROOT)}/`. "
           "For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.", "",
           "- **Noise rule** (owner's decision 12, integrity plan item 1.3): second-family disputes ruled **model error**, divided by the lines that family judged, must be at most 10% for each form-kind run. Findings, representation differences, scope differences and ambiguities are not model noise. The threshold uses integer arithmetic; 1/10 passes and 1/9 does not. Rates for pending reviews are provisional: an unresolved objection has not yet been classified, and zero ruled model errors does not mean every objection was correct.",
           "- **Eligibility** also requires current subjects/sources, the named second-family model, no missing or invalid verdicts, and no open or unclassified ruling. Empty reviews earn no assertion. Optional-family results can remain pending without becoming evidence.",
           "- **Raw agreement** is retained as a diagnostic only. A correct objection must not disqualify an independent reader.",
           "- **Current independence yield**: lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where the Claude log agreed or matched, with the second family's reason. This describes current logs; findings fixed before a rerun remain in BUG_INVENTORY.md and are not erased by a current yield of zero.",
           "- **Both disputed**: lines both families disputed; **Claude only**: lines only the Claude run disputed.",
           "- **Not judged by both**: lines one log has and the other does not, or that either marked MISSING; left out of the floor.",
           "- **Stale**: a log whose recorded subject hash is not the current subject (subjects.py); its verdicts describe an earlier form or rendering.", ""]
    for kind in KINDS:
        rs = [r for r in results if r["kind"] == kind]
        out += [f"## {TITLE[kind]}", ""]
        if not rs:
            out += ["No form has a second family's log of this kind.", ""]
            continue
        out += ["| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in sorted(rs, key=lambda r: (r["form"], r["family"])):
            out.append(f"| {r['form']} | {r['family']} ({r['b']['model']}) | {len(r['judged'])} | {len(r['both_agree'])} | {pct(len(r['both_agree']), len(r['judged']))} | "
                       f"{r['quality']['model_errors']}/{r['quality']['judged']} ({pct(r['quality']['model_errors'], r['quality']['judged'])}) | {floor_mark(r)} | "
                       f"{len(r['yield'])} | {len(r['both_disputed'])} | {len(r['claude_only'])} | {r['unjudged']} |")
        kj = sum(len(r["judged"]) for r in rs); ka = sum(len(r["both_agree"]) for r in rs)
        out.append(f"| **all** | | {kj} | {ka} | {pct(ka, kj)} | | | {sum(len(r['yield']) for r in rs)} | {sum(len(r['both_disputed']) for r in rs)} | {sum(len(r['claude_only']) for r in rs)} | {sum(r['unjudged'] for r in rs)} |")
        out.append("")
        for r in rs:
            if r["excluded_adapters"]:
                out.append(f"Excluded internal adapters for {r['form']}: " + ", ".join(r["excluded_adapters"]) + ". Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.")
            if r["quality"]["blockers"]:
                out.append(f"Pending {r['form']} [{r['family']}]: " + "; ".join(r["quality"]["blockers"]) + ".")
        out.append("")
        ys = [(r, k) for r in rs for k in r["yield"]]
        out += ["### Independence yield", ""]
        if ys:
            out += ["| form | second family | line | second family's verdict | second family's reason |", "| --- | --- | --- | --- | --- |"]
            for r, k in ys:
                out.append(f"| {r['form']} | {r['family']} | {k} | {r['b']['lines'][k]['status']} | {cell(r['b']['lines'][k]['reason'])} |")
        else:
            out.append("None: every line the second family disputed, the Claude run disputed too.")
        out.append("")
        bs = [(r, k) for r in rs for k in r["both_disputed"]]
        out += ["### Lines both families disputed", ""]
        if bs:
            out += ["| form | second family | line | Claude | second family | second family's reason |", "| --- | --- | --- | --- | --- | --- |"]
            for r, k in bs:
                out.append(f"| {r['form']} | {r['family']} | {k} | {r['a']['lines'][k]['status']} | {r['b']['lines'][k]['status']} | {cell(r['b']['lines'][k]['reason'])} |")
        else:
            out.append("None.")
        out.append("")
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    open(REPORT, "w", encoding="utf-8").write("\n".join(out))
    print(f"second_family: {summary} -> {os.path.relpath(REPORT, ROOT)}")


def cell(text):
    """A table cell: one line, pipes escaped, long reasons cut."""
    t = re.sub(r"\s+", " ", text or "").replace("|", "\\|").strip()
    return (t[:400] + "…") if len(t) > 400 else (t or "(no reason given)")


if __name__ == "__main__":
    main()
