"""Lane 8b scratch: rewrite this lane's entries of the question bank and the twins' declared prompt differences.
Run from the worktree root: python3 docs/provisional/lanes/l8b_work/bank.py <wording module>...
A wording module (a .py file beside this one) defines ENTRIES: {input id: {order, seq, prompt?, help?, ...}};
TWINS: {local id: {seq, prompt, help?}} written to person.<id> (with the frame) and dependent.<id>; REMOVE: [ids];
INSERT_AFTER: {new id: existing id it follows}."""
import json, re, sys, runpy, yaml
from pathlib import Path
BANK = Path('interview/2025/questions.yaml')
FRAME = 'For this person (you, or your spouse on a joint return) — '
PER_SEQ = lambda k: 10 * k
DEP_SEQ = lambda k: 200 + 10 * k

class Lit(str): pass
def _lit(d, s): return d.represent_scalar('tag:yaml.org,2002:str', s, style='|')
yaml.SafeDumper.add_representer(Lit, _lit)

def render(entry):
    e = {k: (Lit(v) if isinstance(v, str) and '\n' in v else v) for k, v in entry.items()}
    out = yaml.safe_dump([e], width=118, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return ''.join('  ' + l + '\n' for l in out.splitlines())

def blocks(text):
    head, *rest = re.split(r'(?m)^(?=  - input: )', text)
    return head, rest

def main(mods):
    text = BANK.read_text()
    head, bl = blocks(text)
    ids = [re.match(r'  - input: (\S+)', b).group(1) for b in bl]
    for m in mods:
        ns = runpy.run_path(m)
        entries = dict(ns.get('ENTRIES', {}))
        for local, t in ns.get('TWINS', {}).items():
            # One order number may not hold two questions with the same seq (the order contract, 1.5), so the two
            # sides run in the same sequence, a person's questions first: seq 10k and 200 + 10k.
            base = {'order': t['order']}
            if t.get('help'): base['help'] = t['help']
            if local not in ns.get('PERSON_ONLY', []):
                entries['dependent.' + local] = {**base, 'seq': DEP_SEQ(t['seq']), **({'prompt': t['prompt']} if t.get('prompt') else {})}
            if local not in ns.get('DEPENDENT_ONLY', []):
                entries['person.' + local] = {**base, 'seq': PER_SEQ(t['seq']), **({'prompt': FRAME + t['prompt']} if t.get('prompt') else {})}
        for rid in ns.get('REMOVE', []):
            if rid not in ids: continue
            i = ids.index(rid); del ids[i]; del bl[i]
        for new, after in ns.get('INSERT_AFTER', {}).items():
            if new in ids: continue
            i = ids.index(after) + 1; ids.insert(i, new); bl.insert(i, '')
        for qid, fields in entries.items():
            i = ids.index(qid)
            old = yaml.safe_load(bl[i])[0] if bl[i] else {}
            keep = {k: v for k, v in old.items() if k not in ('input', 'order', 'seq', 'help', 'prompt')}
            e = {'input': qid, 'order': fields['order'], 'seq': fields['seq']}
            if fields.get('help'): e['help'] = fields['help']
            if fields.get('prompt'): e['prompt'] = fields['prompt']
            e.update(keep); e.update({k: v for k, v in fields.items() if k not in e and k not in ('help', 'prompt')})
            bl[i] = render(e)
        tw = ns.get('TWINS')
        if tw:
            p = Path('reviews/2025/twins.json'); d = json.loads(p.read_text())
            d['differences'] = [x for x in d['differences'] if x['field'] not in ('interview.prompt', 'interview.seq')]
            for local, t in tw.items():
                if local in ns.get('PERSON_ONLY', []) or local in ns.get('DEPENDENT_ONLY', []): continue
                d['differences'].append({'pair': local, 'field': 'interview.seq', 'person': PER_SEQ(t['seq']), 'dependent': DEP_SEQ(t['seq']),
                    'reason': 'One order number may not hold two questions with the same place. The two sides are asked in the same sequence, a person on the return first: the dependent side is the person side plus 200.',
                    'source': 'docs/provisional/lanes/order.md (branch lane/order), section 1.5, "two questions of one `order` state the same `seq`"'})
                if not t.get('prompt'): continue
                d['differences'].append({'pair': local, 'field': 'interview.prompt', 'person': FRAME + t['prompt'], 'dependent': t['prompt'],
                    'reason': 'The same words on both sides; the person side begins with the per-person frame, which the interview shows by the entry\'s role (interview/README.md, "The per-person frame as shown").',
                    'source': 'interview/README.md, "The per-person frame as shown"'})
            p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    BANK.write_text(head + ''.join(bl))
    yaml.safe_load(BANK.read_text())

if __name__ == '__main__': main(sys.argv[1:])
