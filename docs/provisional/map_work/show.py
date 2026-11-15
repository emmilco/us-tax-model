# Scratch: print the dumped questions of the given form prefixes; args: prefixes, optional --max N (truncate prompts), --help N.
import json,sys,re
args=sys.argv[1:]
mx=10**6; hx=18
pre=[]
i=0
while i<len(args):
    if args[i]=='--max': mx=int(args[i+1]); i+=2
    elif args[i]=='--help': hx=int(args[i+1]); i+=2
    else: pre.append(args[i]); i+=1
cards=json.load(open('docs/provisional/map_work/cards.json'))
qs={q['input']:q for q in json.load(open('canonical/2025/interview-full.json'))['questions']}
for x in cards:
    i=x['id']; f=i[1:] if i.startswith('$') else i.split('.')[0]
    if f not in pre and i not in pre: continue
    q=qs[i]
    g=x['gate']['text']
    g={'Asked only in some cases':'gated','Open from the start: it is pending before anything is answered':'OPEN','Open once who the return is for is answered':'OPEN-person','Asked of an entry as soon as it is listed: it is pending when the lists have entries and nothing else is answered':'on-entry'}.get(g,g)
    if x['gate']['questions']: g+=' <- '+','.join(a['id'] for a in x['gate']['questions'])
    p=q['prompt'].split(' ')
    pt=' '.join(p[:mx])+(' […]' if len(p)>mx else '')
    h=(q.get('help') or '').split()
    print(f"## {i} | o{q['order']}{'/'+str(q['seq']) if q.get('seq') else ''} | {x['answer']['type']} | {x['words']['prompt']}w h{len(h)} | {g}\n{pt}\nH: {' '.join(h[:hx])}{'…' if len(h)>hx else ''}\n")
