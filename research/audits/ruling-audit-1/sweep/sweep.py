import json,re,subprocess,random,collections,sys
random.seed(7)
meta=json.load(open('/tmp/claude-0/sp/sweep_meta.json'));feed=meta['feed']
cases={c['id']:c for c in json.load(open('/tmp/claude-0/sp/allcases.json'))}
ok=json.load(open('/tmp/claude-0/sp/okcases.json'))
base=lambda k: re.sub(r'\[[^\]]*\]','',k)
by=collections.defaultdict(list)
for cid in ok:
    for k,v in cases[cid]['inputs'].items():
        if isinstance(v,bool) and base(k) in feed: by[base(k)].append((cid,k))
jobs=[]
for b,lst in by.items():
    # diversify by fixture file
    random.shuffle(lst)
    files=collections.defaultdict(list)
    for x in lst: files[x[0].split('#')[0]].append(x)
    pick=[]
    while len(pick)<int(sys.argv[1]) and any(files.values()):
        for f in list(files):
            if files[f]: pick.append(files[f].pop())
    jobs+=pick[:int(sys.argv[1])]
print('jobs',len(jobs),file=sys.stderr)
flags=[]
B=150
for s in range(0,len(jobs),B):
    batch=[]
    for i,(cid,k) in enumerate(jobs[s:s+B]):
        inp=dict(cases[cid]['inputs']); inp[k]=not inp[k]
        batch.append({'id':str(s+i),'inputs':inp})
    json.dump(batch,open('/tmp/claude-0/sp/b.json','w'))
    o=subprocess.run(['node','--max-old-space-size=8000','engine/dist/main.js','eval','--batch','/tmp/claude-0/sp/b.json','--json'],capture_output=True,text=True)
    r=json.loads(o.stdout)['cases']
    for i,(cid,k) in enumerate(jobs[s:s+B]):
        v=r[str(s+i)]
        if 'values' not in v: continue
        vals=v['values']
        l24=vals.get('f1040.line24',{}).get('value',{})
        if l24.get('kind')!='money': continue
        gs=feed[base(k)]
        true_gates=[n for n,x in vals.items() if base(n) in gs and x['value'].get('kind')=='bool' and x['value'].get('value') is True]
        if true_gates:
            flags.append({'case':cid,'input':k,'to':(not cases[cid]['inputs'][k]),'gates':true_gates,'line24':l24.get('cents')})
    print(s,len(flags),file=sys.stderr)
json.dump(flags,open('/tmp/claude-0/sp/flags.json','w'),indent=0)
