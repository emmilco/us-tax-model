import json
def fmt(t):
    d=json.loads(t)
    for kw in (dict(indent=2),dict(separators=(',',':')),dict(indent=1)):
        for ea in (False,True):
            for nl in ('','\n'):
                if json.dumps(d,ensure_ascii=ea,**kw)+nl==t: return lambda x: json.dumps(x,ensure_ascii=ea,**kw)+nl
    raise SystemExit('format')
def new_keys(p,c):
    o={f'person[{p}].birth_year':c['y']}
    if c['y'] in (1961,2001,2002,2007,2008): o[f'person[{p}].born_jan1']=c.get('j',False)
    if c['y']==2010: o[f'person[{p}].under16_at_year_end']=c.get('u',True)
    if c['y']==1976: o[f'person[{p}].age50_at_year_end']=c.get('a',False)
    if c['y']==1960 or (c['y']==1961 and c.get('j')): o[f'person[{p}].died_at_64']=c.get('d',False)
    return o
