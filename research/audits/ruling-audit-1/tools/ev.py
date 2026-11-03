#!/usr/bin/env python3
# usage: ev.py inputs.json [lines...]  prints values of lines + all refusals
import json,subprocess,sys
o=subprocess.run(['node','engine/dist/main.js','eval','--inputs',sys.argv[1],'--json'],capture_output=True,text=True)
if o.returncode: print(o.stderr[:2000]); sys.exit(1)
v=json.loads(o.stdout)['values']
def s(x):
    k=x['kind']
    if k=='money': return '$%.2f'%(x['cents']/100)
    if k=='refusal': return 'REFUSAL(%s)'%json.dumps({a:b for a,b in x.items() if a!='kind'})[:300]
    return json.dumps(x)[:200]
for l in sys.argv[2:]:
    print(l,'=',s(v[l]['value']) if l in v else 'ABSENT')
ref=[k for k,x in v.items() if x['value']['kind']=='refusal']
print('refusal-kind values:',len(ref), ref[:15])
for k in ref[:3]: print(' ',k,s(v[k]['value']))
