"""Model change: person.simple_age derived from the birth year; the plain question asked only of a person born in 1962
or 1966; a person born in 1976 answers person.age50_at_year_end (the IRA's question of the same fact). Run once."""
P = 'forms/2025/person.yaml'
t = open(P).read()
CITE = '''      cite:
        doc: p560
        locator: p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which
          they attain age 60, 61, 62, or 63"
'''


def band(lo, hi):
    return f"""op: test
            all:
            - op: test
              ge:
              - person.birth_year
              - const: {lo}
                type: Count
            - op: test
              le:
              - person.birth_year
              - const: {hi}
                type: Count"""


old_line = '''    - id: person.simple_age
      printed: (helper)
      label: Catch-up eligibility
      type: Enum(catchup_age)
      expr:
        op: input
        source: 'Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50),
          or 60, 61, 62 or 63 (age60_63)'
''' + CITE
assert t.count(old_line) == 1


def guard(test, then):
    return f"""        - guard:
            {test}
          then: {then}
"""


def one(op, y):
    return f"""op: test
            {op}:
            - person.birth_year
            - const: {y}
              type: Count"""


def eqg(y): return band(y, y)  # the guard analyser reads intervals, not equality with a number


def leg(y): return one('le', y)


def geg(y): return one('ge', y)


new = '''    - id: person.simple_age
      printed: (helper)
      label: 'Catch-up eligibility from the year of birth: 64 or older (born 1961 or earlier) and 50 to 59 (born 1967 to 1975)
        age50; 60 to 63 (born 1963 to 1965) age60_63; under 50 (born 1977 or later) under50; for a person born in 1962, 1966 or
        1976, as that person states'
      type: Enum(catchup_age)
      expr:
        op: choose
        alternatives:
''' + guard(leg(1961), 'person.catchup_age50') + guard(eqg(1962), 'person.simple_age_if_open_year') \
    + guard(band(1963, 1965), 'person.catchup_age60_63') + guard(eqg(1966), 'person.simple_age_if_open_year') \
    + guard(band(1967, 1975), 'person.catchup_age50') + guard(eqg(1976), 'person.simple_age_1976') \
    + guard(geg(1977), 'person.catchup_under50') + CITE + '''    - id: person.simple_open_year
      printed: (helper)
      type: Bool
      label: Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)
      expr:
        op: test
        any:
        - op: test
          eq:
          - person.birth_year
          - const: 1962
            type: Count
        - op: test
          eq:
          - person.birth_year
          - const: 1966
            type: Count
''' + CITE + '''    - id: person.simple_age_at_year_end
      printed: (helper)
      label: Catch-up eligibility, as stated by a person born in 1962 or 1966
      type: Enum(catchup_age)
      gated_by: person.simple_age_if_open_year
      expr:
        op: input
        source: 'Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50),
          or 60, 61, 62 or 63 (age60_63)'
''' + CITE + '''    - id: person.simple_age_if_open_year
      printed: (gate)
      type: Enum(catchup_age)
      label: Catch-up eligibility as stated by a person born in 1962 or 1966 (otherwise 50 to 59 or 64 and over; read only for
        those years)
      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - person.simple_open_year
            - const: true
          then: person.simple_age_at_year_end
        - guard:
            op: test
            eq:
            - person.simple_open_year
            - const: false
          then: person.catchup_age50
''' + CITE + '''    - id: person.simple_age_1976
      printed: (helper)
      type: Enum(catchup_age)
      label: Catch-up eligibility of a person born in 1976 (50 or over at the end of 2025 as that person states, otherwise under 50)
      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - person.age50_at_year_end_if_born_1976
            - const: true
          then: person.catchup_age50
        - guard:
            op: test
            eq:
            - person.age50_at_year_end_if_born_1976
            - const: false
          then: person.catchup_under50
''' + CITE + '''      ambiguity: amb.2025.ira_age50
'''
for v, name in (('under50', 'ret.catchup_under50'), ('age50', 'ret.catchup_age50'), ('age60_63', 'ret.catchup_age60_63')):
    new += f'''    - id: person.catchup_{v}
      printed: (helper)
      type: Enum(catchup_age)
      label: Year parameter {name} ({v})
      expr:
        op: param
        ref: {name}
''' + CITE
t = t.replace(old_line, new)
open(P, 'w').write(t)

Q = 'params/2025.yaml'
q = open(Q).read()
anchor = '''    ret.simple_limit:
      type: NonNegDollars
      value: 1650000
'''
assert q.count(anchor) == 1
add = ''
for v, what in (('under50', 'under 50 at the end of the year: no catch-up contributions'),
                ('age50', 'age 50 or over at the end of the year and not attaining age 60, 61, 62 or 63 in it: the general catch-up limit'),
                ('age60_63', 'attaining age 60, 61, 62 or 63 in the year: the higher catch-up limit')):
    add += f'''    ret.catchup_{v}:
      type: Enum(catchup_age)
      value: {v}
      cite:
        doc: p560
        locator: 'chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which
          they attain age 60, 61, 62, or 63": {what}'
'''
q = q.replace(anchor, add + anchor)
open(Q, 'w').write(q)
print('ok')
