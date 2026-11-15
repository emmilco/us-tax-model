# Scratch: condensed view. First line up to L words, bullets up to B words, other paragraphs up to P words.
import json,sys
args=sys.argv[1:]; L,B,P=60,14,28
pre=[a for a in args if not a.startswith('-')]
cards=json.load(open('docs/provisional/map_work/cards.json'))
qs={q['input']:q for q in json.load(open('canonical/2025/interview-full.json'))['questions']}
def cut(s,n):
    w=s.split(' '); return ' '.join(w[:n])+('…' if len(w)>n else '')
for x in cards:
    i=x['id']; f=i[1:] if i.startswith('$') else i.split('.')[0]
    if f not in pre and i not in pre: continue
    q=qs[i]
    g=x['gate']['text']
    g={'Asked only in some cases':'gated','Open from the start: it is pending before anything is answered':'OPEN','Open once who the return is for is answered':'OPEN-person','Asked of an entry as soon as it is listed: it is pending when the lists have entries and nothing else is answered':'on-entry'}.get(g,g[:60])
    if x['gate']['questions']: g+=' <- '+','.join(a['id'] for a in x['gate']['questions'])
    lines=[l for l in q['prompt'].split('\n') if l.strip()]
    out=[cut(lines[0],L)]
    for l in lines[1:]:
        s=l.strip()
        if s.startswith('- '): out.append(('    ' if l.startswith('  ') else '  ')+cut(s,B))
        else: out.append(' '+cut(s,P))
    h=(q.get('help') or '').split()
    hh='' if ' '.join(h).startswith('Married filing separately and unsupported') else ' H: '+' '.join(h[:12])+'…'
    print(f"## {i} | o{q['order']}{'/'+str(q['seq']) if q.get('seq') else ''} | {x['answer']['type']} | {x['words']['prompt']}w h{len(h)} | {g}\n"+'\n'.join(out)+hh+'\n')
