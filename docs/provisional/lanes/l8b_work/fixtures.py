"""Lane 8b scratch: rewrite fixture inputs for this lane's model changes (inputs only; never an expected value).
Run from the worktree root: python3 docs/provisional/lanes/l8b_work/fixtures.py sli|f5695"""
import glob, json, sys
from pathlib import Path

STYLES = [dict(indent=2, ensure_ascii=False), dict(indent=2), dict(indent=1, ensure_ascii=False), dict(indent=1),
          dict(separators=(',', ':'), ensure_ascii=False), dict(ensure_ascii=False), dict()]
FULL = ('classm', 'mutation')   # files whose cases take no defaults: every input is stated

def style_of(text, data):
    for kw in STYLES:
        for nl in ('\n', ''):
            if json.dumps(data, **kw) + nl == text: return kw, nl
    return None

def after(inputs, anchor_keys, new):
    """inputs with the pairs of `new` inserted after the last present anchor key (at the end when none is present)."""
    keys = list(inputs); pos = max([keys.index(k) for k in anchor_keys if k in inputs], default=len(keys) - 1)
    out = {}
    for i, k in enumerate(keys):
        out[k] = inputs[k]
        if i == pos:
            for nk, nv in new.items():
                if nk not in inputs: out[nk] = nv
    if not keys: out.update(new)
    return out

def sli(inputs, full):
    paid = inputs.get('sli.interest', 0) or 0
    if isinstance(paid, dict): paid = 1   # an amount stated relative to a year parameter: an amount was paid
    new = {}
    if paid > 0 or (full and 'sli.interest' in inputs): new['sli.any'] = paid > 0
    if full and 'sli.interest' in inputs:
        new.update({'sli.unqualified_any': False, 'sli.unqualified': 0, 'sli.assisted_any': False, 'sli.assisted': 0})
    return after(inputs, ['sli.interest'], new) if new else inputs

KIND_COSTS = {
 'solar': ['line1'], 'solar_water': ['line2'], 'wind': ['line3'], 'geothermal': ['line4'],
 'insulation': ['line18a'], 'doors': ['line19a', 'line19d_i', 'line19d_ii', 'line19e'],
 'windows': ['line20a_i', 'line20a_ii', 'line20a_iii', 'line20a_iv', 'line20b'],
 'heat_pump': ['line29a', 'line29b'], 'hp_water_heater': ['line29c', 'line29d'], 'central_ac': ['line22a', 'line22b'],
 'water_heater': ['line23a_i', 'line23a_ii', 'line23b'], 'furnace': ['line24a', 'line24b'], 'biomass': ['line29e', 'line29f'],
}
PART1_KINDS = ['solar', 'solar_water', 'wind', 'geothermal']
SEC_A_KINDS = ['insulation', 'doors', 'windows']
SEC_B_KINDS = ['heat_pump', 'hp_water_heater', 'central_ac', 'water_heater', 'furnace', 'biomass']
NEW_ORDER = ['any'] + PART1_KINDS + SEC_A_KINDS + ['panel', 'audit'] + SEC_B_KINDS + ['carry']

def f5695(inputs, full):
    """The same facts under the new questions. A kind is Yes when its part's old screen was Yes and one of its costs
    is above zero; a part answered Yes with no cost at all is given one kind (solar panels; insulation or a heat pump
    by the section whose first question was Yes), so that its conditions and refusals are still reached."""
    F = 'f5695.'
    if not any(k.startswith(F) for k in inputs) or F + 'any' in inputs: return inputs
    if F + 'part1_any' not in inputs and F + 'part2_any' not in inputs and not full: return inputs
    g = lambda k: inputs.get(F + k)
    pos = lambda k: isinstance(g(k), dict) or (isinstance(g(k), (int, float)) and not isinstance(g(k), bool) and g(k) > 0)
    yes = lambda k: g(k) is True
    p1, p2 = yes('part1_any'), yes('part2_any')
    v = {k: (p1 if k in PART1_KINDS else p2) and any(pos(c) for c in cs) for k, cs in KIND_COSTS.items()}
    battery, fuel = p1 and yes('line5a'), p1 and yes('line7a')
    v['carry'] = p1 and pos('line12')
    v['panel'] = p2 and yes('line25a')
    v['audit'] = p2 and yes('line26a')
    if p1 and not (any(v[k] for k in PART1_KINDS) or battery or fuel or v['carry']): v['solar'] = True
    if p2:
        a, b = any(v[k] for k in SEC_A_KINDS), any(v[k] for k in SEC_B_KINDS) or v['panel']
        if yes('line17a') and not a: v['insulation'] = a = True
        if yes('line21a') and not b: v['heat_pump'] = b = True
        if not (a or b or v['audit']): v['insulation'] = True
    v['any'] = any(v[k] for k in NEW_ORDER if k not in ('any', 'carry')) or battery or fuel
    out = {}
    done = False
    def put():
        for k in NEW_ORDER:
            if full or v[k]: out[F + k] = v[k]
    for k, val in inputs.items():
        if k in (F + 'part1_any', F + 'part2_any'):
            if not done: put(); done = True
            continue
        if k == F + 'line5a' and val is True: val = battery
        if k == F + 'line7a' and val is True: val = fuel
        if k == 's3.prior_other_forms' and v['carry']: val = True
        if k.startswith(F) and not done: put(); done = True
        out[k] = val
    if v['carry'] and 's3.prior_other_forms' not in out: out['s3.prior_other_forms'] = True
    return out

def f5695_full(inputs, full):
    """Second pass, for the files that state every input: the answers a case now reaches and did not state before
    (the battery and fuel cell questions once something was installed; the three questions beneath
    s3.prior_other_forms once the 2024 return is said to include a separate form). Each is the closed answer."""
    if not full: return inputs
    new = {}
    if inputs.get('f5695.any') is True:
        for k in ('f5695.line5a', 'f5695.line7a'):
            if k not in inputs: new[k] = False
    if inputs.get('f5695.carry') is True:
        for k in ('ftc.carryover', 's3.prior_amt', 's3.prior_forms'):   # the questions beneath s3.prior_other_forms
            if k not in inputs: new[k] = False
    return after(inputs, ['f5695.biomass', 'f5695.carry'], new) if new else inputs

def run(fn):
    changed = 0
    for f in sorted(glob.glob('fixtures/2025/*.json') + glob.glob('fixtures/ny/2025/*.json')):
        if f.endswith('defaults.json'): continue
        text = Path(f).read_text(); data = json.loads(text)
        st = style_of(text, data)
        full = any(x in Path(f).name for x in FULL)
        n = 0
        for case in data['cases']:
            for key in ('inputs',):
                if key in case:
                    new = fn(case[key], full)
                    if new != case[key] or list(new) != list(case[key]): case[key] = new; n += 1
        if n:
            if st is None: raise SystemExit(f'{f}: unknown JSON style; not rewritten')
            Path(f).write_text(json.dumps(data, **st[0]) + st[1]); changed += n; print(f, n)
    print('cases changed:', changed)

if __name__ == '__main__':
    run({'sli': sli, 'f5695': f5695, 'f5695_full': f5695_full}[sys.argv[1]])
