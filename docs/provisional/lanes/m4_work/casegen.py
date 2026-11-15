# Lane m4: shared machinery for writing mutation fixture cases from a table.
# A table row names a base case (an existing case of the same file, whose inputs state every input), the input
# changes (None = leave the input unanswered), and the predicted values: an int (cents), True/False, or
# ("refusal", gate) / ("unknown", input) for a refusal or unknown whose full record is then taken from the evaluator
# after checking it is the gate or input predicted. The script stops on any prediction the evaluator does not give.
import json, subprocess, sys, os

ROOT = __file__.rsplit('/docs/', 1)[0]
EV = os.path.join(ROOT, 'docs/provisional/lanes/m4_work/ev.mjs')


def load(path):
    return json.load(open(os.path.join(ROOT, path)))


def base_inputs(data, case_id):
    for c in data['cases']:
        if c['id'] == case_id:
            return dict(c['inputs'])
    raise KeyError(case_id)


def apply(inputs, changes):
    out = dict(inputs)
    for k, v in changes.items():
        if v is None:
            out.pop(k, None)
        else:
            out[k] = v
    return out


def evaluate(cases, ny=False):
    tmp = '/tmp/m4/eval_in.json'
    os.makedirs('/tmp/m4', exist_ok=True)
    json.dump({c['id']: {'inputs': c['inputs'], 'targets': list(c['predict'])} for c in cases}, open(tmp, 'w'))
    out = subprocess.run(['node', EV, tmp] + (['--ny'] if ny else []), capture_output=True, text=True, cwd=ROOT)
    if out.returncode != 0:
        sys.exit(out.stderr)
    return {r['id']: r['values'] for r in map(json.loads, out.stdout.splitlines())}


def record(pred, got, where):
    if isinstance(pred, bool):
        want = {'kind': 'bool', 'value': pred}
        if got != want:
            sys.exit(f'{where}: predicted {pred}, evaluator gives {json.dumps(got)}')
        return got
    if isinstance(pred, int):
        want = {'kind': 'money', 'cents': pred}
        if got != want:
            sys.exit(f'{where}: predicted {pred} cents, evaluator gives {json.dumps(got)}')
        return got
    kind, ref = pred
    if got is None or got.get('kind') != kind or (got.get('gate') if kind == 'refusal' else got.get('input')) != ref:
        sys.exit(f'{where}: predicted {kind} on {ref}, evaluator gives {json.dumps(got)}')
    return got


def build(cases, ny=False):
    values = evaluate(cases, ny)
    out = []
    for c in cases:
        expect = {t: record(p, values[c['id']].get(t), f"{c['id']} {t}") for t, p in c['predict'].items()}
        out.append({'id': c['id'], 'covers': c['covers'], 'evidence': 'synthetic regression (not class B)',
                    'evidence_note': c['note'], 'inputs': c['inputs'], 'expect': expect})
    return out


def write(path, new_cases, prefix):
    full = os.path.join(ROOT, path)
    data = json.load(open(full))
    # The prefix's cases are replaced where the first of them stood (at the end when there are none yet).
    at = next((i for i, c in enumerate(data['cases']) if c['id'].startswith(prefix)), len(data['cases']))
    before = [c for c in data['cases'][:at] if not c['id'].startswith(prefix)]
    after = [c for c in data['cases'][at:] if not c['id'].startswith(prefix)]
    data['cases'] = before + new_cases + after
    open(full, 'w').write(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print(f'{path}: {len(new_cases)} cases under {prefix}, {len(data["cases"])} in all')
