#!/usr/bin/env python3
"""Recompare saved transcriptions without rewriting requests, logs or rulings.

This is a diagnostic expression-type/comparison audit, not review qualification.
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
import input_contracts
import adapter_contracts
import input_context


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
            "original_comparison_policy": fields.get("comparison policy", "legacy-unversioned"),
            "original_type_policy": fields.get("type validation policy", "legacy-unrecorded"),
            "original_input_context_policy": fields.get("input context policy", "legacy-unrecorded")}


def prepare_replay(path, prompt, response, meta, current_subject, archive_root=None):
    """Archive a verified parent before an explicitly labelled host re-comparison.

    The caller must also enforce review_response's exact current request/model/
    system match. This cannot migrate an older request with different context.
    """
    path = Path(path)
    original = path.read_text()
    receipt = verify_saved(original, prompt, response, meta, current_subject)
    if receipt['request_provenance'] != 'bound':
        raise ValueError('cannot replay an unbound or legacy-limited request')
    verify_replay_archive(path, original, prompt, response, meta, current_subject)
    parent_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    folder = Path(archive_root or Path(T.RAW) / 'archive' / 'verified-replays') / path.stem / parent_sha
    base = Path(T.RAW) / path.stem
    if (Path(str(base)+'.prompt.txt').read_text() != prompt
            or Path(str(base)+'.response.txt').read_text() != response
            or json.loads(Path(str(base)+'.meta.json').read_text()) != meta):
        raise ValueError('saved replay artifacts changed after request verification')
    artifacts = [path, path.with_suffix('.rulings.json')]
    artifacts += [Path(str(base) + suffix) for suffix in ('.prompt.txt','.response.txt','.meta.json')]
    manifest = {}
    for artifact in artifacts:
        if not artifact.exists():
            if artifact.suffix == '.json' and artifact.name.endswith('.rulings.json'):
                continue
            raise FileNotFoundError('missing replay artifact: ' + str(artifact))
        data = artifact.read_bytes()
        destination = folder / artifact.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and destination.read_bytes() != data:
            raise ValueError('replay archive already differs: ' + str(destination))
        destination.write_bytes(data)
        manifest[artifact.name] = hashlib.sha256(data).hexdigest()
    (folder / 'sha256.json').write_text(json.dumps(manifest, indent=2) + '\n')
    head = original.partition('\n## Lines\n')[0]
    fields = dict(re.findall(r'^\| ([^|]+) \| ([^|]*) \|$', head, re.M))
    return {'parent_sha256':parent_sha, 'original_date':fields.get('date','unrecorded'),
            'original_comparison_policy':receipt['original_comparison_policy'],
            'original_type_policy':receipt['original_type_policy'],
            'original_input_context_policy':receipt['original_input_context_policy']}


def verify_replay_archive(path, log, prompt, response, meta, current_subject, depth=0):
    """A derived log must retain the exact, hash-verified parent it claims."""
    head=log.partition('\n## Lines\n')[0]
    fields=dict(re.findall(r'^\| ([^|]+) \| ([^|]*) \|$',head,re.M))
    if 'review provenance' not in fields:
        return
    if depth >= 32:
        raise ValueError('saved-review replay chain exceeds the verification bound')
    if fields['review provenance'] != 'verified saved-response replay; no model call':
        raise ValueError('unrecognized saved-review provenance')
    parent=fields.get('parent review log sha256','')
    if not re.fullmatch(r'[0-9a-f]{64}',parent):
        raise ValueError('invalid replay parent identity')
    path=Path(path)
    folder=Path(T.RAW)/'archive/verified-replays'/path.stem/parent
    manifest=json.loads((folder/'sha256.json').read_text())
    required={path.name,*(path.stem+suffix for suffix in ('.prompt.txt','.response.txt','.meta.json'))}
    if not required <= manifest.keys() or manifest.get(path.name) != parent:
        raise ValueError('incomplete replay parent archive')
    for name,expected in manifest.items():
        if Path(name).name != name or hashlib.sha256((folder/name).read_bytes()).hexdigest() != expected:
            raise ValueError('replay parent archive hash mismatch')
    if ((folder/(path.stem+'.prompt.txt')).read_text()!=prompt
            or (folder/(path.stem+'.response.txt')).read_text()!=response
            or json.loads((folder/(path.stem+'.meta.json')).read_text())!=meta):
        raise ValueError('replay parent request/reply differs')
    parent_log=(folder/path.name).read_text()
    parent_receipt=verify_saved(parent_log,prompt,response,meta,current_subject)
    if parent_receipt['request_provenance']!='bound':
        raise ValueError('replay parent is not a bound request')
    verify_replay_archive(folder/path.name,parent_log,prompt,response,meta,current_subject,depth+1)


def audit(path):
    form, family = families.split_stem(path.stem)
    base = Path(T.RAW) / path.stem
    log = path.read_text()
    prompt = base.with_suffix(base.suffix + ".prompt.txt").read_text()
    response = base.with_suffix(base.suffix + ".response.txt").read_text()
    meta = json.loads(base.with_suffix(base.suffix + ".meta.json").read_text())
    receipt = verify_saved(log, prompt, response, meta, T.subjects.current("transcription", form, T.Y))
    verify_replay_archive(path, log, prompt, response, meta, receipt['subject_sha256'])
    before = comparison.parse_log("transcription", str(path))["lines"]
    second = T.extract_yaml(response)["lines"]
    form_doc = T.load_form(form)
    current, extra = T.compare(form, form_doc["lines"], second)
    interfaces = input_context.assess(form_doc, second, T.model_type_context(), prompt)
    partial = input_contracts.assess(form, T.Y, second, T.model_type_context(), prompt) if input_contracts.load(form, T.Y) else None
    changes = [{"line": row["printed"], "before": before.get(row["printed"], {}).get("status", "ABSENT"),
                "after": row["status"], "project": row["project"], "second": row["second"]}
               for row in current if before.get(row["printed"], {}).get("status") != row["status"]]
    return {"form": form, "family": family, **receipt, "comparison_policy": T.COMPARISON_POLICY,
            "input_context_policy": input_context.POLICY, "missing_input_context": interfaces["missing"],
            "input_context": interfaces,
            "legacy_global_missing_input_context": T.missing_input_context(prompt),
            "type_validation_policy": T.TYPE_VALIDATION_POLICY,
            "type_errors": current.validation_errors,
            "partial_inputs": partial,
            "excluded_adapters": sorted(adapter_contracts.excluded_ids(form, T.Y)),
            "before_agree": sum(row["status"] == "AGREE" for row in before.values()),
            "after_agree": sum(row["status"] == "AGREE" for row in current),
            "new_disagreements": sum(row["before"] == "AGREE" and row["after"] == "DISAGREE" for row in changes),
            "extra_lines": extra, "changes": changes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--forms", help="comma-separated form ids")
    parser.add_argument("--family", choices=["claude", "deepseek"])
    parser.add_argument("--report", default=str(Path(T.RAW) / "expression-type-audit-current.json"))
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
    output = {"scope": "Read-only expression checks, re-comparison and bounded source-based partial-input checks, not qualification. Original requests, logs and rulings are unchanged.",
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
