#!/usr/bin/env python3
# mk.py fixturefile caseid out.json key=jsonvalue ...
import json,sys
d=json.load(open(sys.argv[1]))
c=[x for x in d['cases'] if x['id']==sys.argv[2]][0]
inp=dict(c['inputs'])
for kv in sys.argv[4:]:
    k,v=kv.split('=',1)
    if k=='CLONE':  # CLONE=frompfx|topfx|collkey|name
        a,b,coll,name=v.split('|')
        for kk,vv in list(inp.items()):
            if kk.startswith(a): inp[b+kk[len(a):]]=vv
            if kk.startswith('$') and a in kk:  # nested collections
                inp[kk.replace(a,b)]=vv
        inp[coll]=inp[coll]+[name]
    elif v=='DEL': inp.pop(k,None)
    else: inp[k]=json.loads(v)
json.dump({'base':sys.argv[1]+'#'+sys.argv[2],'overrides':sys.argv[4:]} and inp,open(sys.argv[3],'w'),indent=1,sort_keys=True)
