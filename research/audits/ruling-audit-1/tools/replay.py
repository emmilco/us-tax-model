#!/usr/bin/env python3
# replay.py witness.json : drives the full-profile interview, answering from the witness; reports asked inputs not in witness, final status, and targets
import json,subprocess,sys,os,tempfile
w=json.load(open(sys.argv[1]))
log=tempfile.mktemp(suffix='.jsonl',dir='/tmp/claude-0/sp')
def run(*a):
    o=subprocess.run(['node','engine/dist/main.js','interview',*a,'--log',log],capture_output=True,text=True)
    if o.returncode: print('ERR',o.stderr[:500]); sys.exit(2)
    return json.loads(o.stdout)
d=run('start','--profile','full')
asked=[]
for step in range(3000):
    if d['status']!='incomplete': break
    q=d['question']['input']
    if q not in w:
        print('ASKED BUT NOT IN WITNESS:',q); break
    asked.append(q)
    d=run('answer','--input',q,'--value',json.dumps(w[q]))
print('status:',d['status'],'questions answered:',len(asked))
if d.get('refusal'): print('refusal:',json.dumps(d['refusal'])[:300])
v=d.get('values',{})
for t in sys.argv[2:]:
    x=v.get(t); print(t, json.dumps(x.get('value') if isinstance(x,dict) and 'value' in x else x)[:200])
unused=[k for k in w if k not in asked]
print('witness inputs never asked:',len(unused), unused[:40])
