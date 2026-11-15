"""Model change: one birth year behind the seven birth-date lines of person.yaml (plus age 50, under 16, died before 65)."""
import re
P='forms/2025/person.yaml'
t=open(P).read()
parts=re.split(r'(?m)^(?=    - id: )', t)
head, blocks = parts[0], parts[1:]
ids=[re.match(r'    - id: (\S+)', b).group(1) for b in blocks]
def blk(i): return blocks[ids.index(i)]
def cite_of(i):
    b=blk(i); m=re.search(r'(?ms)^      cite:\n.*?(?=^      [a-z_]+:|\Z)', b); return m.group(0)
def set_expr(i, expr, label=None):
    k=ids.index(i); b=blocks[k]
    m=re.search(r'(?ms)^      expr:\n.*?(?=^      [a-z_]+:|\Z)', b)
    b=b[:m.start()]+expr+b[m.end():]
    if label is not None:
        m=re.search(r'(?ms)^      label: .*?(?=^      [a-z_]+:)', b)
        b=b[:m.start()]+'      label: '+label+'\n'+b[m.end():]
    blocks[k]=b
def add_after(after, text):
    k=ids.index(after); i=re.match(r'    - id: (\S+)', text).group(1)
    assert i not in ids, i
    blocks.insert(k+1, text); ids.insert(k+1, i)
def Y(n): return f"- const: {n}\n            type: Count"
def cut(year, gate='person.born_jan1_if_cut_year'):
    # born before January 2 of `year`: an earlier year, or that year on January 1
    return f"""      expr:
        op: test
        any:
        - op: test
          lt:
          - person.birth_year
          - const: {year}
            type: Count
        - op: test
          all:
          - op: test
            eq:
            - person.birth_year
            - const: {year}
              type: Count
          - op: test
            eq:
            - {gate}
            - const: true
"""
c65=cite_of('person.blind')
# --- new inputs and helper lines, placed after person.one
new = f"""    - id: person.birth_year
      printed: (helper)
      type: Count
      label: The year you were born
      expr:
        op: input
        source: In what year were you born?
{c65}    - id: person.birth_cut_year
      printed: (helper)
      type: Bool
      label: Born in a year in which a birth on January 1 changes an age test of this return (1961, 2001, 2002, 2007 or 2008)
      expr:
        op: test
        any:
""" + ''.join(f"""        - op: test
          eq:
          - person.birth_year
          - const: {y}
            type: Count
""" for y in (1961,2001,2002,2007,2008)) + f"""{c65}    - id: person.born_jan1
      printed: (helper)
      type: Bool
      gated_by: person.born_jan1_if_cut_year
      label: Were you born on January 1?
      expr:
        op: input
        source: Were you born on January 1?
{c65}    - id: person.born_jan1_if_cut_year
      printed: (gate)
      type: Bool
      label: Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)
      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - person.birth_cut_year
            - const: true
          then: person.born_jan1
        - guard:
            op: test
            eq:
            - person.birth_cut_year
            - const: false
          then: person.no
{c65}"""
for text in reversed(re.split(r'(?m)^(?=    - id: )', new)):
    if text: add_after('person.one', text)
set_expr('person.age65', cut(1961), 'Born before January 2, 1961')
set_expr('person.born_before_2001', cut(2001), 'Born before January 2, 2001')
set_expr('person.sav_born', cut(2008), 'Born before January 2, 2008')
set_expr('person.edu_born_2007', cut(2007), 'Born before January 2, 2007')
set_expr('person.edu_born_2002', cut(2002), 'Born before January 2, 2002')
set_expr('person.born_after_1960', """      expr:
        op: test
        ge:
        - person.birth_year
        - const: 1961
          type: Count
""", 'Born after December 31, 1960')
def stated(i, gate, year, yes_test, label, newid, question, born_label, gate_label):
    """Old id `i` becomes a test: settled by the birth year, or (born in `year`) the stated answer `newid` behind `gate`."""
    c=cite_of(i)
    amb=re.search(r'(?m)^      ambiguity: .*\n', blk(i))
    amb=amb.group(0) if amb else ''
    set_expr(i, f"""      expr:
        op: test
        any:
        - op: test
          {yes_test}
        - op: test
          all:
          - op: test
            eq:
            - person.birth_year
            - const: {year}
              type: Count
          - op: test
            eq:
            - {gate}
            - const: true
""", label)
    born=f'person.born_{year}'
    add_after(i, f"""    - id: {born}
      printed: (helper)
      type: Bool
      label: {born_label}
      expr:
        op: test
        eq:
        - person.birth_year
        - const: {year}
          type: Count
{c}    - id: {newid}
      printed: (helper)
      type: Bool
      gated_by: {gate}
      label: {question}
      expr:
        op: input
        source: {question}
{c}{amb}    - id: {gate}
      printed: (gate)
      type: Bool
      label: {gate_label}
      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - {born}
            - const: true
          then: {newid}
        - guard:
            op: test
            eq:
            - {born}
            - const: false
          then: person.no
{c}""")
    # split the inserted text into its three blocks
    k=ids.index(born); three=re.split(r'(?m)^(?=    - id: )', blocks[k]); three=[x for x in three if x]
    blocks[k:k+1]=three; ids[k:k+1]=[re.match(r'    - id: (\S+)', x).group(1) for x in three]
stated('person.under16','person.under16_at_year_end_if_born_2010',2010,
       "ge:\n          - person.birth_year\n          - const: 2011\n            type: Count",
       'Under age 16 at the end of 2025', 'person.under16_at_year_end', 'Were you under age 16 at the end of 2025?',
       'Born in 2010', 'Under age 16 at the end of 2025, as stated by a person born in 2010 (otherwise no)')
stated('person.ira_age50','person.age50_at_year_end_if_born_1976',1976,
       "le:\n          - person.birth_year\n          - const: 1975\n            type: Count",
       'Age 50 or older at the end of 2025', 'person.age50_at_year_end', 'Were you age 50 or older at the end of 2025?',
       'Born in 1976', 'Age 50 or older at the end of 2025, as stated by a person born in 1976 (otherwise no)')
# --- died before 65: asked only of a person who could (born in 1960, or on January 1, 1961)
cd=cite_of('person.died_before_65')
old=blk('person.died_before_65')
src=re.search(r'(?ms)^        source: (.*?)(?=^      cite:)', old).group(1)
set_expr('person.died_before_65', """      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - person.turned_65_in_2025
            - const: true
          then: person.died_at_64
        - guard:
            op: test
            eq:
            - person.turned_65_in_2025
            - const: false
          then: person.no
""", 'The final return of a person who died in 2025 before reaching age 65 (asked only of a person born in 1960, or on January 1, 1961; otherwise no)')
add_after('person.died_before_65', f"""    - id: person.died_at_64
      printed: (helper)
      type: Bool
      gated_by: person.died_before_65
      label: Is this the final return of a person who died in 2025 before reaching age 65?
      expr:
        op: input
        source: Is this the final return of a person who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)
{cd}""")
k=ids.index('person.died_before_65')
tb=f"""    - id: person.turned_65_in_2025
      printed: (helper)
      type: Bool
      label: Born in 1960, or on January 1, 1961 (a person whose 65th birthday, or the day before it, fell in 2025)
      expr:
        op: test
        any:
        - op: test
          eq:
          - person.birth_year
          - const: 1960
            type: Count
        - op: test
          all:
          - op: test
            eq:
            - person.birth_year
            - const: 1961
              type: Count
          - op: test
            eq:
            - person.born_jan1_if_cut_year
            - const: true
{cd}"""
blocks.insert(k, tb); ids.insert(k,'person.turned_65_in_2025')
open(P,'w').write(head+''.join(blocks))
print('ok', len(blocks))
