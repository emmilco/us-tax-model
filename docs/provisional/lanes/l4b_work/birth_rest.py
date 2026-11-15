import sys,json,re; sys.path.insert(0,'/tmp/l4b')
from bank import Bank
F='For this person (you, or your spouse on a joint return) — '
b=Bank()
b.add_after('person.age65','person.birth_year',order=119,seq=1)
b.add_after('person.birth_year','person.born_jan1',order=119,seq=2,
  help='For several rules of this return a person born on January 1 counts as a year older on the December 31 before.')
b.add_after('person.born_jan1','person.under16_at_year_end',order=119,seq=3,
  help='A return for a person under 16 is outside what this tool prepares; a Yes ends the interview here.')
b.add_after('person.under16_at_year_end','person.died_at_64',order=119,seq=4,
  help='It decides whether the higher standard deduction and the deduction for people 65 or older apply. For a living person the answer is No.')
b.set('person.ira_age50',input='person.age50_at_year_end')
for i in ['person.age65','person.under16','person.sav_born','person.edu_born_2007','person.edu_born_2002','person.born_before_2001','person.born_after_1960','person.died_before_65']:
    b.remove(i)
b.save()
# defaults
p='fixtures/2025/defaults.json'; d=json.load(open(p))
OLD=['age65','born_after_1960','born_before_2001','edu_born_2002','edu_born_2007','sav_born','under16','ira_age50','died_before_65']
olds={'person.'+o for o in OLD}
out=[]; put=False
for e in d['defaults']:
    if e['input'] in olds:
        if not put:
            put=True
            out+= [
             {'input':'person.age50_at_year_end','value':False,'reason':'Closed: asked only of a person born in 1976; the circumstance does not apply unless the scenario says so.'},
             {'input':'person.birth_year','value':1980,'reason':'1980: the ordinary filer is 45 at the end of 2025, a year that settles every age test the ordinary way (not 65 or older, not 50 or older, 25 or older, not under 18) and is on no cut. A scenario about an age states the year.'},
             {'input':'person.born_jan1','value':False,'reason':'Closed: asked only of a person born in 1961, 2001, 2002, 2007 or 2008; a birth on January 1 is the special case.'},
             {'input':'person.died_at_64','value':False,'reason':'Closed: the circumstance this question asks about does not apply unless the scenario says so.'},
             {'input':'person.under16_at_year_end','value':False,'reason':'Closed: asked only of a person born in 2010; the circumstance does not apply unless the scenario says so.'}]
        continue
    out.append(e)
out.sort(key=lambda e:e['input']) if False else None
d['defaults']=out
d['consistency']=[r for r in d['consistency'] if not any(t.get('input') in olds for t in r['never'])]
open(p,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
# profiles
for f in ['stage4','sales','social-security']:
    p=f'interview/2025/{f}.yaml'; t=open(p).read()
    t=t.replace('  - person.age65\n','  - person.birth_year\n  - person.born_jan1\n')
    if '  - person.birth_year\n' in t: t=t.replace('  - person.under16\n','  - person.under16_at_year_end\n')
    else: t=t.replace('  - person.under16\n','  - person.birth_year\n  - person.under16_at_year_end\n')
    t=t.replace('  - person.ira_age50\n','  - person.age50_at_year_end\n').replace('  - person.died_before_65\n','  - person.died_at_64\n')
    open(p,'w').write(t)
# personas: the age in `who` at the end of 2025
ages={'01_single_w2':31,'03_single_parent_child_care':29,'05_self_employed':38,'06_investor_loss_carryover':45,'07_college_student':24,'08_hsa_marketplace':34,'09_tips_overtime':27,'10_homeowner_solar_heat_pump':52}
import glob,os
for p in glob.glob('interview/2025/personas/*.yaml'):
    n=os.path.basename(p)[:-5]; t=open(p).read()
    t=re.sub(r'(?m)^  person\[(taxpayer|spouse)\]\.(age65|under16|sav_born|edu_born_2007|edu_born_2002|born_before_2001|born_after_1960|died_before_65|ira_age50): .*\n','',t)
    add=''
    if n in ages: add=f'  person[taxpayer].birth_year: {2025-ages[n]}\n'
    if n=='07_college_student': add+='  person[taxpayer].born_jan1: false\n'
    if n=='04_retired_couple': add='  person[taxpayer].birth_year: 1954\n  person[spouse].birth_year: 1956\n'
    if add:
        m=re.search(r'(?m)^  f1040\.status: .*\n|^  \$person: .*\n',t)
        # after the $person line (and the status line where one follows it)
        m=re.search(r'(?m)^  \$person: .*\n(  f1040\.status: .*\n)?',t)
        t=t[:m.end()]+add+t[m.end():]
    open(p,'w').write(t)
# coverage row
p='interview/2025/coverage/credits.yaml'; t=open(p).read()
t=t.replace('    person[taxpayer].age65: true\n','    person[taxpayer].birth_year: 1955\n').replace('    person[taxpayer].died_before_65: false\n','')
open(p,'w').write(t)
