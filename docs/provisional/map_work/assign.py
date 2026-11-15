# Scratch: the map's assignment of every question to a topic (new order range) and a lane; prints the tables MAP.md quotes.
import json,collections,re,sys
qs=json.load(open('canonical/2025/interview-full.json'))['questions']
W={c['id']:c['words']['prompt'] for c in json.load(open('docs/provisional/map_work/cards.json'))}
def form(i): return i[1:] if i.startswith('$') else i.split('.')[0]
def topic(i):
    f=form(i); n=i.split('.',1)[1] if '.' in i else ''
    if i in('$person','f1040.status'): return 100
    if f=='household': return 310 if n=='credit_disallowed' else 100
    if i in('person.under16','person.age65','person.blind','person.died_before_65','sa.dependent','sa.excluded_income','s3.disability_retired'): return 110
    if i in('person.tin','person.work_ssn','person.itin_applied','person.eic_ssn','person.born_after_1960','person.born_before_2001','dependent.eic_ssn','dependent.us_half','s3.elderly_credit'): return 310
    if f=='dependent':
        if n.startswith('dc_'): return 155
        if n.startswith('edu'): return 240
        if n.startswith('ptc_'): return 195
        return 120
    if i.startswith('s3.adoption'): return 120
    if f=='w2':
        if n.startswith('box10'): return 155
        if n.startswith('box12') or n.startswith('g_'): return 310
        return 140
    if i in('person.rrta','person.educator_expenses','person.eligible_educator','f8959.unsupported'): return 140
    if i in('s1a.tips','s1a.overtime') or f in('tipjob','otjob'): return 150
    if i=='s1a.carloan' or f=='carloan': return 220
    if f in('f2441','dcprov'): return 155
    if f in('s1','oi8z','refund'): return 160
    if f=='retirement': return 310 if n.startswith('sav_') else 170
    if f=='ssb': return 178
    if f=='ira': return 180
    if f=='f8889' or i=='person.x_hsa_value': return 190
    if f in('f1095a','f8962'): return 195
    if f in('sa','gift') or i=='s3.mcc': return 200
    if i.startswith('s3.ev') or i.startswith('s3.kerosene'): return 225
    if f=='f5695': return 230
    if f in('f8863','sli') or i.startswith('person.edu'): return 240
    if f=='person':
        if n.startswith('sav_'): return 180 if n in('sav_trad',) else 310
        if n.startswith('ira_') or n.startswith('x_'): return 180
        return 259
    if f=='sc': return 250
    if f=='scveh': return 255
    if f in('asset','s179'): return 257
    if f in('ltc',) or i in('qbi.unsupported','qbi.carryforward'): return 259
    if f=='interest' or i in('sb.unsupported','f1040.tax_exempt_interest'): return 270
    if f=='div' or i in('sb.ordinary_dividends','f1040.line3a','qbi.dividends','sd.distributions'): return 272
    if f=='sales' or i=='sd.other_forms': return 274
    if i=='sd.carryover' or f in('clcw','clcw26') or i=='f8960.prior_2i': return 276
    if f=='f4952': return 277
    if f=='f8960': return 278
    if f=='ftc' or i in('s3.foreign_any','s3.section960c','s3.section965','s3.virgin_islands'): return 279
    if f=='sb': return 285
    if f=='scope': return 0
    if f=='s2' or f=='s3' and i!='s3.line10': return 290
    if i in('f1040.line25b','f1040.line25c_other','f1040.line26','s3.line10','f1040.line35a','f1040.line36'): return 300
    if f in('eic','s8812'): return 310
    raise SystemExit('unplaced '+i)
FILE={'household':'L1','f1040':'L1','dependent':'L2a','f2441':'L2b','dcprov':'L2b','s8812':'L2b','eic':'L2b','w2':'L3','tipjob':'L3','otjob':'L3','s1a':'L3','carloan':'L3','retirement':'L4a','ssb':'L4a','person':'L4b','ira':'L4b','interest':'L5a','div':'L5a','sb':'L5a','ftc':'L5a','sales':'L5b','sd':'L5b','clcw':'L5b','clcw26':'L5b','f4952':'L5b','f8960':'L5b','sc':'L6a','ltc':'L6a','qbi':'L6a','scveh':'L6b','asset':'L6b','s179':'L6b','sa':'L7a','gift':'L7a','refund':'L7a','s1':'L7b','oi8z':'L7b','f1095a':'L8a','f8962':'L8a','f8889':'L8a','f8863':'L8b','sli':'L8b','f5695':'L8b','scope':'L9','s2':'L7b','f8959':'L7b','s3':'L7b'}
def lane(i):
    f=form(i); n=i.split('.',1)[1] if '.' in i else ''
    if i=='$person': return 'L1'
    if i in('person.under16','person.age65','person.blind','person.died_before_65','sa.dependent','sa.excluded_income'): return 'L1'
    if i.startswith('dependent.dc_') or i.startswith('w2.box10') or i in('household.credit_disallowed','person.tin','person.work_ssn','person.itin_applied','person.eic_ssn','person.born_after_1960','person.born_before_2001'): return 'L2b'
    if i=='person.rrta': return 'L3'
    if i.startswith('person.edu') and not i.startswith('person.educator') or i.startswith('dependent.edu'): return 'L8b'
    if i.startswith('dependent.ptc_'): return 'L8a'
    if f=='person' and (n.startswith('plan') or n.startswith('sep_') or n.startswith('simple_') or n=='se_screen'): return 'L6a'
    if i in('f1040.line3a','f1040.tax_exempt_interest','qbi.dividends'): return 'L5a'
    return FILE[f]
if __name__=='__main__':
    by=collections.defaultdict(list)
    for q in qs: by[(q['order'],form(q['input']))].append(q['input'])
    print('## today order -> topics')
    o2=collections.defaultdict(lambda: collections.defaultdict(list))
    for q in qs: o2[q['order']][topic(q['input'])].append(q['input'])
    def glob(ids):
        g=collections.defaultdict(list)
        for i in ids: g[form(i)].append(i)
        out=[]
        for f,l in sorted(g.items()):
            out.append(l[0] if len(l)==1 else f"{f}.* ({len(l)})" if all(not x.startswith('$') for x in l) else f"${f} and {f}.* ({len(l)})")
        return ', '.join(out)
    for o in sorted(o2):
        print(o, ' | '.join(f"{t}: {glob(l)}" for t,l in sorted(o2[o].items())))
    print('## topics')
    tb=collections.defaultdict(list)
    for q in qs: tb[topic(q['input'])].append(q['input'])
    for t in sorted(tb): print(t,len(tb[t]),sum(W[i] for i in tb[t]),glob(tb[t]))
    print('## lanes')
    lb=collections.defaultdict(list)
    for q in qs: lb[lane(q['input'])].append(q['input'])
    walk=set()
    for l in open('docs/provisional/map_work/minimal_walk.tsv'):
        p=l.split('\t')
        if len(p)>3: walk.add(re.sub(r'\[[^\]]*\]','',p[3]).split('@')[0])
    for l in sorted(lb):
        ids=lb[l]; print(l,len(ids),'q',sum(W[i] for i in ids),'w; over120:',sum(1 for i in ids if W[i]>=120),'; asked of all:',sum(1 for i in ids if i in walk), sum(W[i] for i in ids if i in walk),'w')
        print('   ',glob(ids))
        print('    ALL:',', '.join(f"{i}({W[i]})" for i in ids if i in walk))
