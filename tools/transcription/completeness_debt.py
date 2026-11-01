#!/usr/bin/env python3
"""Local subjects for never-reviewed completeness debt; actual receipts remain prompt-bound."""
import hashlib
import json
from pathlib import Path

POLICY = 'never-reviewed-completeness-debt-v1'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def subject(form, sections, system):
    # Full canonical data catches computed-expression changes omitted by encoding().
    return digest({'policy': POLICY, 'form': form, 'sections': sections, 'system': system,
                   'reviewer_sha': hashlib.sha256(Path(__file__).with_name('completeness_review.py').read_bytes()).hexdigest()})


def eligible(record, baseline, current_subject, reviewed):
    """Fail closed; an existing receipt can never use a deferred-debt exemption."""
    return (reviewed is None and isinstance(record, dict)
            and record.get('policy') == POLICY
            and isinstance(record.get('origin_commit'), str) and len(record['origin_commit']) == 40
            and isinstance(record.get('prompt_sha'), str) and len(record['prompt_sha']) == 64
            and hashlib.sha256(record['prompt_sha'].encode()).hexdigest()[:16] == baseline
            and record.get('subject') == current_subject)


def migrate(origin, commit, forms, mani, records, baseline, review):
    """Verify each old full-prompt fingerprint before deriving its narrower debt subject.

    origin is an independently built historical checkout; caller supplies its reviewer module.
    No unmatched baseline is migrated and no existing review is exempted.
    """
    result = {}
    for form in forms:
        key = 'stale:' + form['id']
        if key not in baseline or form['id'] in records:
            continue
        prompt = review.prompt_for(form, mani, forms)
        if not prompt or hashlib.sha256(prompt[2].encode()).hexdigest()[:16] != baseline[key]:
            raise ValueError('historical prompt does not reproduce baseline: ' + key)
        secs, _ = review.sections(form, mani)
        result[key] = {'policy': POLICY, 'origin_commit': commit, 'prompt_sha': prompt[2],
                       'subject': subject(form, secs, review.SYSTEM)}
    return result
