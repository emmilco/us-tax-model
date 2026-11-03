import json,subprocess
f=json.load(open('/tmp/claude-0/sp/flags.json'))
cases={c['id']:c for c in json.load(open('/tmp/claude-0/sp/allcases.json'))}
batch=[]
for i,x in enumerate(f):
    inp=dict(cases[x['case']]['inputs']); inp.pop(x['input'])
    batch.append({'id':str(i),'inputs':inp})
json.dump(batch,open('/tmp/claude-0/sp/b2.json','w'))
o=subprocess.run(['node','--max-old-space-size=8000','engine/dist/main.js','eval','--batch','/tmp/claude-0/sp/b2.json','--json','--target','f1040.line24'],capture_output=True,text=True)
r=json.loads(o.stdout)['cases']
out=[]
for i,x in enumerate(f):
    v=r[str(i)]
    k=v.get('values',{}).get('f1040.line24',{}).get('value',{}).get('kind') if 'values' in v else 'error:'+v.get('error','')[:80]
    x['line24_without_input']=k
    if k!='money': out.append(x)
for x in out: print(x['case'],x['input'],x['to'],x['gates'][:2],x['line24_without_input'])
json.dump(out,open('/tmp/claude-0/sp/flags_read.json','w'),indent=0)
