import json,glob,re,collections,os
OLD=['age65','born_after_1960','born_before_2001','edu_born_2002','edu_born_2007','sav_born','under16','ira_age50','died_before_65']
def vec(c):
    y,j,u,a,d=c['y'],c.get('j',False),c.get('u'),c.get('a'),c.get('d',False)
    cut=lambda Y: y<Y or (y==Y and j)
    v={'age65':cut(1961),'born_after_1960':y>=1961,'born_before_2001':cut(2001),'edu_born_2002':cut(2002),'edu_born_2007':cut(2007),'sav_born':cut(2008),
       'under16': y>=2011 or (y==2010 and bool(u)), 'ira_age50': y<=1975 or (y==1976 and bool(a)),
       'died_before_65': bool(d) and (y==1960 or (y==1961 and j))}
    return v
CANDS=[{'y':1980},{'y':1970},{'y':1950},{'y':1960,'d':False},{'y':1960,'d':True},{'y':1961,'j':True,'d':False},{'y':1961,'j':True,'d':True},
       {'y':2001,'j':False},{'y':2004},{'y':2007,'j':False},{'y':2009},{'y':2012},
       {'y':2001,'j':True},{'y':2002,'j':True},{'y':2007,'j':True},{'y':2008,'j':True},{'y':1976,'a':True},{'y':1976,'a':False},{'y':2010,'u':True},{'y':2010,'u':False}]
def files():
    return sorted(glob.glob('fixtures/2025/*.json')+glob.glob('fixtures/ny/2025/*.json')+glob.glob('fixtures/2025/differential/*.json'))
def persons(inputs):
    ps=set()
    for k in inputs:
        m=re.match(r'person\[([^\]]+)\]\.(\w+)$',k)
        if m and m.group(2) in OLD: ps.add(m.group(1))
    return ps
def stated(inputs,p):
    return {o:inputs[f'person[{p}].{o}'] for o in OLD if f'person[{p}].{o}' in inputs}
def satisfying(S):
    out=[]
    for c in CANDS:
        v=vec(c)
        if all(v[k]==val for k,val in S.items() if val is not None): out.append(c)
    return out
