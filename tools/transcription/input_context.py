"""Host-side freshness of the input interfaces needed by a source review.

The actual request stays intact. This assessment is not a new model call, an
upgrade of its original prompt policy, or evidence that its tax reading is right.
"""
import hashlib
import json

POLICY = "required-review-interfaces-v2"


def assess(form_doc, second, context, prompt):
    import transcribe as T
    fid = form_doc["id"]
    own_ids = {line["id"] for line in form_doc["lines"]}
    foreign = {line["id"]: (doc, line) for doc in context["forms"]
               if doc["id"] != fid for line in doc["lines"]}
    required = {(fid, line["id"]): (form_doc, line)
                for line in form_doc["lines"] if line["expr"].get("op") == "input"}
    # Include both the submitted and authored form's direct boundary references.
    # A model cannot shrink the required context by omitting a dependency. Do
    # not follow foreign authored arithmetic; these are published boundaries.
    for line in [*form_doc["lines"], *second]:
        refs = T.operand_refs(line.get("expr", {}))
        for refusal in line.get("refuses", []) or []:
            when = refusal if isinstance(refusal, str) else refusal.get("when") if isinstance(refusal, dict) else None
            if isinstance(when, str):
                refs.add(when)
        for name in refs - own_ids:
            # A candidate helper may not shadow a published foreign interface.
            # The type checker rejects that independently; still require it here.
            if name in foreign:
                doc, target = foreign[name]
                required[(doc["id"], name)] = (doc, target)

    supplied = " ".join(prompt.split())
    keys = T.marker_keys(form_doc["lines"])
    records, missing = [], []
    for (doc_id, name), (doc, line) in sorted(required.items()):
        record = {"doc": doc_id, "id": name, "type": line["type"], "printed": str(line["printed"])}
        is_input = line["expr"].get("op") == "input"
        if is_input:
            record["source"] = " ".join(line["expr"].get("source", "").split())
        records.append(record)
        if doc_id == fid:
            expected = f"{name} (printed {keys[name]!r}, type {line['type']}): {record['source']}"
        else:
            expected = T.reference_note(doc, line)
        if " ".join(expected.split()) not in supplied:
            missing.append(f"{doc_id}:{name}")
    fingerprint = hashlib.sha256(json.dumps({"policy": POLICY, "required": records},
        sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return {"policy": POLICY, "required_sha256": fingerprint, "required": records,
            "missing": missing, "state": "fail" if missing else "pass"}
