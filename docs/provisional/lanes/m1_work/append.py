# append.py SPECS.json NOTES.json INPUTS.json : append cases to fixtures/2025/mutation.json (ids must be new).
import json,sys
W='/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/fixtures/2025/mutation.json'
specs=json.load(open(sys.argv[1])); notes=json.load(open(sys.argv[2])); inputs={r['id']:r['inputs'] for r in json.load(open(sys.argv[3]))}
d=json.load(open(W))
have={c['id'] for c in d['cases']}
for s in specs:
    assert s['id'] not in have, s['id']
    cov,note=notes[s['id']]
    covers=[cov] if isinstance(cov,str) else cov
    d['cases'].append({"id":s['id'],"covers":covers,"evidence":s.get('evidence',"synthetic regression (not class B)"),"evidence_note":note,"inputs":inputs[s['id']],"expect":s['expect']})
open(W,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print('appended',len(specs),'total',len(d['cases']))
