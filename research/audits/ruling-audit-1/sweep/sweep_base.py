import json,glob,subprocess
cases=[]
for f in sorted(glob.glob('fixtures/2025/stage*.json')):
    d=json.load(open(f))
    for c in d['cases']: cases.append({'id':f.split('/')[-1]+'#'+c['id'],'inputs':c['inputs']})
json.dump(cases,open('/tmp/claude-0/sp/allcases.json','w'))
o=subprocess.run(['node','--max-old-space-size=8000','engine/dist/main.js','eval','--batch','/tmp/claude-0/sp/allcases.json','--json','--target','f1040.line24'],capture_output=True,text=True)
r=json.loads(o.stdout)['cases']
ok=[k for k,v in r.items() if 'values' in v and v['values'].get('f1040.line24',{}).get('value',{}).get('kind')=='money']
print(len(cases),len(ok))
json.dump(ok,open('/tmp/claude-0/sp/okcases.json','w'))
