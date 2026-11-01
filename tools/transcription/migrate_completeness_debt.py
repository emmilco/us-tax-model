#!/usr/bin/env python3
"""Explicit one-time migration from an independently built historical checkout.

Usage: migrate_completeness_debt.py CHECKOUT COMMIT
The caller exports COMMIT and builds it with npm run build before invoking this tool.
"""
import json
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import baseline_check
import completeness_review as review
import completeness_debt as debt


def main():
    origin, commit = Path(sys.argv[1]), sys.argv[2]
    commit = subprocess.check_output(['git', 'rev-parse', commit], text=True).strip()
    # Verify the historical inputs against Git, including every authored form.
    paths = ['tools/transcription/completeness_review.py', 'sources/' + review.Y + '/manifest.json']
    paths += [str(p.relative_to(origin)) for p in (origin / 'forms' / review.Y).glob('*.yaml')]
    for path in paths:
        expected = subprocess.check_output(['git', 'show', commit + ':' + path])
        if (origin / path).read_bytes() != expected:
            raise ValueError('historical checkout differs from commit: ' + path)
    for path in paths[:2]:
        if (Path(review.ROOT) / path).read_bytes() != (origin / path).read_bytes():
            raise ValueError('migration requires unchanged review policy/source manifest: ' + path)
    target = Path(review.OUT) / 'rulings.json'
    data = json.loads(target.read_text())
    historical = json.loads(subprocess.check_output(['git', 'show', commit + ':reviews/' + review.Y + '/completeness/rulings.json']))
    if data['baseline'] != historical['baseline']:
        raise ValueError('baseline differs from historical commit')
    records = {r['form']: r for r in json.loads((Path(review.OUT) / 'completeness.json').read_text())}
    forms = baseline_check.load_forms(origin / 'canonical' / review.Y)
    if not forms:
        raise ValueError('build the historical checkout first')
    entries = debt.migrate(origin, commit, forms, review.manifest(), records, data['baseline'], review)
    data['deferred_debt'] = entries
    target.write_text(json.dumps(data, indent=1) + '\n')
    print('Verified and migrated', len(entries), 'never-reviewed baseline entries from', commit)


if __name__ == '__main__':
    main()
