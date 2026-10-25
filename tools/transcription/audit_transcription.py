#!/usr/bin/env python3
"""Recompare saved transcriptions without rewriting requests, logs or rulings.

This is a diagnostic audit, not model IR validation or review qualification.
Original log subjects, prompt hashes and embedded replies must match the saved
artifacts. Legacy incomplete request receipts stay explicitly legacy-limited.
Only the requested JSON report is written; no network/model calls are made.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import compare_families as comparison
import families
import transcribe as T


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def verify_saved(log, prompt, response, meta, current_subject):
    head = log.partition("\n## Lines\n")[0]
    fields = dict(re.findall(r"^\| ([^|]+) \| ([^|]*) \|$", head, re.M))
    if fields.get("subject sha256") != current_subject:
        raise ValueError("log subject no longer matches the project definition")
    if fields.get("prompt sha256") != sha(prompt):
        raise ValueError("saved prompt differs from the original log receipt")
    _, separator, tail = log.partition("\n## Raw second transcription\n")
    # The current writer strips the response at its edges when embedding it;
    # legacy writers also embedded the original edge whitespace. Neither permits
    # any change inside the reply. Hash the complete saved response below.
    wrappers = {("```yaml\n" + value + "\n```").strip() for value in (response, response.strip())}
    if not separator or tail.strip() not in wrappers:
        raise ValueError("saved response differs from the reply embedded in the original log")
    for key, field in [("prompt_sha256", "prompt sha256"), ("system_sha256", "system sha256"),
                       ("prompt_policy", "prompt policy"), ("model_requested", "model requested")]:
        if key in meta and meta[key] != fields.get(field):
            raise ValueError(f"saved metadata differs from the log's {field}")
    if meta.get("finish_reason") == "length":
        raise ValueError("response exhausted its output budget")
    bound = all(key in meta for key in ("prompt_sha256", "system_sha256", "prompt_policy", "model_requested"))
    return {"subject_sha256": current_subject, "prompt_sha256": sha(prompt),
            "response_sha256": sha(response), "request_provenance": "bound" if bound else "legacy-limited",
            "original_prompt_policy": fields.get("prompt policy", "legacy-unrecorded"),
            "original_comparison_policy": fields.get("comparison policy", "legacy-unversioned")}


def audit(path):
    form, family = families.split_stem(path.stem)
    base = Path(T.RAW) / path.stem
    log = path.read_text()
    prompt = base.with_suffix(base.suffix + ".prompt.txt").read_text()
    response = base.with_suffix(base.suffix + ".response.txt").read_text()
    meta = json.loads(base.with_suffix(base.suffix + ".meta.json").read_text())
    receipt = verify_saved(log, prompt, response, meta, T.subjects.current("transcription", form, T.Y))
    before = comparison.parse_log("transcription", str(path))["lines"]
    current, extra = T.compare(form, T.load_form(form)["lines"], T.extract_yaml(response)["lines"])
    changes = [{"line": row["printed"], "before": before.get(row["printed"], {}).get("status", "ABSENT"),
                "after": row["status"], "project": row["project"], "second": row["second"]}
               for row in current if before.get(row["printed"], {}).get("status") != row["status"]]
    return {"form": form, "family": family, **receipt, "comparison_policy": T.COMPARISON_POLICY,
            "before_agree": sum(row["status"] == "AGREE" for row in before.values()),
            "after_agree": sum(row["status"] == "AGREE" for row in current),
            "new_disagreements": sum(row["before"] == "AGREE" and row["after"] == "DISAGREE" for row in changes),
            "extra_lines": extra, "changes": changes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--forms", help="comma-separated form ids")
    parser.add_argument("--family", choices=["claude", "deepseek"])
    parser.add_argument("--report", default=str(Path(T.RAW) / "typed-literal-audit.json"))
    args = parser.parse_args()
    selected = set(args.forms.split(",")) if args.forms else None
    results, errors = [], []
    for path in sorted(Path(T.LOGS).glob("*.md")):
        form, family = families.split_stem(path.stem)
        if (selected and form not in selected) or (args.family and family != args.family):
            continue
        try:
            results.append(audit(path))
        except (ValueError, OSError, KeyError, TypeError) as exc:
            errors.append({"log": str(path), "error": str(exc)})
    output = {"scope": "Read-only typed-literal re-comparison, not model IR validation or qualification. Original requests, logs and rulings are unchanged.",
              "comparison_policy": T.COMPARISON_POLICY, "results": results, "errors": errors}
    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"transcription audit: {len(results)} replies verified and recompared; "
          f"{sum(r['new_disagreements'] for r in results)} former agreements become disagreements; "
          f"{sum(r['request_provenance'] == 'legacy-limited' for r in results)} legacy-limited receipts; "
          f"{len(errors)} records could not be verified/recompared; no review logs changed -> {report}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
