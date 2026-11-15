import yaml,sys
bank=yaml.safe_load(open('interview/2025/questions.yaml'))['bank']
place={q['input']:(q['order'],q.get('seq',9999)) for q in bank['questions']}
for f in sys.argv[1:]:
    d=yaml.safe_load(open(f'forms/2025/{f}.yaml')); d=d.get('form') or d.get('def') or d
    lines={l['id']:l for l in d['lines']}
    def reads(e,acc,seen):
        if isinstance(e,dict):
            for k,v in e.items(): reads(v,acc,seen)
        elif isinstance(e,list):
            for v in e: reads(v,acc,seen)
        elif isinstance(e,str) and e in place: acc.add(e)
        elif isinstance(e,str) and e in lines and e not in seen:
            seen.add(e); reads(lines[e].get('expr'),acc,seen)
    for l in d['lines']:
        r=l.get('refuses') or []
        if len(r)<2: continue
        out=[]
        for x in r:
            seen=set(); acc=set(); w=x['when']
            if w in place: acc.add(w)
            elif w in lines: seen.add(w); reads(lines[w].get('expr'),acc,seen)
            ps=sorted(place[a] for a in acc)
            out.append((w, ps[-1] if ps else None))
        last=None; bad=False
        for w,p in out:
            if p and last and p<last: bad=True
            if p: last=max(last,p) if last else p
        if bad: print(l['id'], [(w.split('.',1)[-1],'%d/%d'%p if p else None) for w,p in out])
