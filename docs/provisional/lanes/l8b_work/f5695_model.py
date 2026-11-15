"""Lane 8b scratch: the model change of Form 5695 (forms/2025/f5695.yaml), applied once to the file as it stood at
100b132c. One plain parent (f5695.any), a yes or no question per kind of improvement, and each cost asked only for a
kind answered Yes. f5695.part1_any and f5695.part2_any stay as derived lines, so no other form is edited.
Run from the worktree root: python3 docs/provisional/lanes/l8b_work/f5695_model.py"""
import json
import re
from pathlib import Path

P = Path('forms/2025/f5695.yaml')
text = P.read_text()
assert 'f5695.any' not in text, 'already applied'
head, *bl = re.split(r'(?m)^(?=  - id: )', text)
ids = [re.match(r'  - id: (\S+)', b).group(1) for b in bl]
B = dict(zip(ids, bl))

def cite_of(i):
    b = B[i]; a = b.index('    cite:\n'); m = re.search(r'(?m)^    (?!cite:| )', b[a + 1:])
    return b[a:a + 1 + m.start()] if m else b[a:].rstrip('\n') + '\n'

def test(ref, value='true'):
    return f"""      - op: test
        eq:
        - {ref}
        - const: {value}
"""

def choose_expr(guard, then, other):
    return f"""    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - {guard}
          - const: true
        then: {then}
      - guard:
          op: test
          eq:
          - {guard}
          - const: false
        then: {other}
"""

def any_expr(refs):
    return "    expr:\n      op: test\n      any:\n" + ''.join(test(r) for r in refs)

def line(i, label, typ, expr, cite, printed='(helper)', gated_by=None):
    g = f"    gated_by: {gated_by}\n" if gated_by else ''
    return f"  - id: {i}\n    printed: {printed}\n    label: {json.dumps(label, ensure_ascii=False)}\n    type: {typ}\n{g}{expr}{cite}\n"

def ask(i, label, source, cite, gated_by):
    return line(i, label, 'Bool', f"    expr:\n      op: input\n      source: {json.dumps(source, ensure_ascii=False)}\n", cite, gated_by=gated_by)

def set_expr(i, expr):
    b = B[i]; a = b.index('    expr:\n'); c = b.index('    cite:\n')
    B[i] = b[:a] + expr + b[c:]

def mark(i, gate):
    b = B[i]; assert 'gated_by' not in b, i
    B[i] = re.sub(r'(?m)^(    type: .*\n)', lambda m: m.group(1) + f"    gated_by: {gate}\n", b, count=1)

C1, C2 = cite_of('f5695.part1_any'), cite_of('f5695.part2_any')
NO, ZERO = 'f5695.no', 'f5695.zero'

# 1. The parent and the kinds. (id, label, question, cite source, the cost inputs it gates)
KINDS = [
 ('solar', 'Solar electric property was installed', 'Did that include solar panels that make electricity?', C1, ['line1']),
 ('solar_water', 'Solar water heating property was installed', 'Did that include a solar water heater?', C1, ['line2']),
 ('wind', 'Small wind energy property was installed', 'Did that include a wind turbine?', C1, ['line3']),
 ('geothermal', 'Geothermal heat pump property was installed', 'Did that include a geothermal (ground-source) heat pump?', C1, ['line4']),
 ('insulation', 'Insulation or air sealing material or systems were installed', 'Did that include insulation or air sealing?', C2, ['line18a']),
 ('doors', 'Exterior doors were installed', 'Did that include exterior doors?', C2, ['line19a', 'line19d_i', 'line19d_ii', 'line19e']),
 ('windows', 'Exterior windows or skylights were installed', 'Did that include exterior windows or skylights?', C2,
  ['line20a_i', 'line20a_ii', 'line20a_iii', 'line20a_iv', 'line20b']),
 ('panel', 'Panelboards, subpanelboards, branch circuits or feeders were improved or replaced',
  'Did that include a new or upgraded electrical panel, circuits or wiring?', C2, []),
 ('audit', 'A home energy audit was paid for in 2025', 'In 2025, did you (or, on a joint return, your spouse) pay for a home energy audit?', C2, []),
 ('heat_pump', 'An electric or natural gas heat pump was installed',
  'Did that include a heat pump for heating or cooling, electric or gas (other than a geothermal one)?', C2, ['line29a', 'line29b']),
 ('hp_water_heater', 'An electric or natural gas heat pump water heater was installed', 'Did that include a heat pump water heater?', C2,
  ['line29c', 'line29d']),
 ('central_ac', 'A central air conditioner was installed', 'Did that include a central air conditioner?', C2, ['line22a', 'line22b']),
 ('water_heater', 'A natural gas, propane or oil water heater was installed',
  'Did that include a water heater that runs on natural gas, propane or oil?', C2, ['line23a_i', 'line23a_ii', 'line23b']),
 ('furnace', 'A natural gas, propane or oil furnace or hot water boiler was installed',
  'Did that include a furnace or hot water boiler that runs on natural gas, propane or oil?', C2, ['line24a', 'line24b']),
 ('biomass', 'A biomass stove or biomass boiler was installed', 'Did that include a stove or boiler that burns wood, pellets or other plant fuel (a biomass stove or boiler)?', C2,
  ['line29e', 'line29f']),
]
new_head = line('f5695.any', 'Anything was installed in 2025 at a home to save or make energy, or a home energy audit was paid for', 'Bool',
    "    expr:\n      op: input\n      source: " + json.dumps('In 2025, did you (or, on a joint return, your spouse) have anything installed at home that saves or makes energy: solar panels, a battery, insulation, windows, doors, or heating, cooling or hot-water equipment?') + "\n", C1)
gates = {}   # gated input -> gate line
for k, label, q, cite, costs in KINDS:
    kid, gid = f'f5695.{k}', f'f5695.{k}_if_any'
    new_head += ask(kid, label, q, cite, gid)
    new_head += line(gid, f'{label}, asked only when something was installed or an audit paid for (false otherwise)', 'Bool',
                     choose_expr('f5695.any', kid, NO), cite, printed='(gate)')
    for c in costs: gates[f'f5695.{c}'] = (f'f5695.{c}_if_{k}', gid, ZERO, 'NonNegDollars')
# existing yes or no questions that become kinds or conditions of a kind
gates['f5695.line5a'] = ('f5695.line5a_if_any', 'f5695.any', NO, 'Bool')
gates['f5695.line25a'] = ('f5695.line25a_if_panel', 'f5695.panel_if_any', NO, 'Bool')
gates['f5695.line26a'] = ('f5695.line26a_if_audit', 'f5695.audit_if_any', NO, 'Bool')
gates['f5695.line12'] = ('f5695.line12_if_carry', 'f5695.carry_if_prior', ZERO, 'NonNegDollars')
C12 = cite_of('f5695.line12')
new_head += line('f5695.line7a_if_any', 'Qualified fuel cell property was installed, asked only when something was installed (false otherwise); the refusal on line 11 reads the answer itself',
                 'Bool', choose_expr('f5695.any', 'f5695.line7a', NO), cite_of('f5695.line7a'), printed='(gate)')
new_head += ask('f5695.carry', 'A residential clean energy credit carryforward from 2024 (an amount on line 16 of a 2024 Form 5695)',
                "Does that 2024 return include Form 5695 (Residential Energy Credits) with an amount on line 16?", C12, 'f5695.carry_if_prior')
new_head += line('f5695.carry_if_prior', 'A residential clean energy credit carryforward from 2024, asked only when the 2024 return includes a form besides Form 1040 and its schedules (false otherwise: the carryforward is line 16 of the 2024 Form 5695)',
                 'Bool', choose_expr('s3.prior_other_forms', 'f5695.carry', NO), C12, printed='(gate)')
PART1 = ['solar_if_any', 'solar_water_if_any', 'wind_if_any', 'geothermal_if_any', 'line5a_if_any', 'line7a_if_any', 'carry_if_prior']
SEC_A = ['insulation_if_any', 'doors_if_any', 'windows_if_any']
SEC_B = ['heat_pump_if_any', 'hp_water_heater_if_any', 'central_ac_if_any', 'water_heater_if_any', 'furnace_if_any', 'biomass_if_any', 'panel_if_any']
new_head += line('f5695.sec_a_kinds', 'Insulation, exterior doors or exterior windows or skylights were installed', 'Bool', any_expr(['f5695.' + x for x in SEC_A]), C2)
new_head += line('f5695.sec_b_kinds', 'Residential energy property or enabling property was installed', 'Bool', any_expr(['f5695.' + x for x in SEC_B]), C2)

def derived(i, label, refs):
    b = B[i]
    B[i] = line(i, label, 'Bool', any_expr(refs), cite_of(i))
derived('f5695.part1_any', 'Part I is completed: residential clean energy property was installed in 2025 (counted when the original installation is completed, or for a constructed or reconstructed home when its original use begins), or there is a carryforward from 2024',
        ['f5695.' + x for x in PART1])
derived('f5695.part2_any', 'Part II is completed: an energy efficiency improvement or residential energy property was installed in 2025, or a home energy audit was paid for',
        ['f5695.sec_a_kinds', 'f5695.sec_b_kinds', 'f5695.audit_if_any'])

# 2. A gate line after each gated input, and every other reader moved to the gate line.
for inp, (gid, guard, other, typ) in gates.items():
    mark(inp, gid)
order = list(ids)
for inp, (gid, guard, other, typ) in gates.items():
    short = inp.split('.')[1]
    for i in order:
        if i == inp: continue
        B[i] = re.sub(r'(?<![\w.])' + re.escape(inp) + r'(?!\w)', gid, B[i])
    what = 'false' if typ == 'Bool' else 'zero'
    B[gid] = line(gid, f'The answer to {short}, asked only in its case ({what} otherwise)', typ, choose_expr(guard, inp, other), cite_of(inp), printed='(gate)')
    order.insert(order.index(inp) + 1, gid)

# 3. Conditions asked one after another, and only for a kind that was installed.
B['f5695.sec_a_home'] = line('f5695.sec_a_home', 'Lines 17a, 17b and 17c are all Yes', 'Bool', choose_expr('f5695.line17a', 'f5695.sec_a_original', NO), cite_of('f5695.sec_a_claimed'))
B['f5695.sec_a_original'] = line('f5695.sec_a_original', 'Lines 17b and 17c are both Yes', 'Bool', choose_expr('f5695.line17b', 'f5695.line17c', NO), cite_of('f5695.sec_a_claimed'))
set_expr('f5695.sec_a_claimed', choose_expr('f5695.sec_a_kinds', 'f5695.sec_a_home', NO))
order[order.index('f5695.sec_a_claimed'):order.index('f5695.sec_a_claimed')] = ['f5695.sec_a_home', 'f5695.sec_a_original']
set_expr('f5695.sec_a_new_home', choose_expr('f5695.sec_a_claimed', 'f5695.line17e', NO))
B['f5695.sec_b_home'] = line('f5695.sec_b_home', 'Lines 21a and 21b are both Yes', 'Bool', choose_expr('f5695.line21a', 'f5695.line21b', NO), cite_of('f5695.sec_b_claimed'))
set_expr('f5695.sec_b_claimed', choose_expr('f5695.sec_b_kinds', 'f5695.sec_b_home', NO))
order.insert(order.index('f5695.sec_b_claimed'), 'f5695.sec_b_home')
set_expr('f5695.sec_b_new_home', choose_expr('f5695.sec_b_claimed', 'f5695.b_new_home', NO))
set_expr('f5695.enabling_claimed', choose_expr('f5695.sec_b_claimed', 'f5695.line25a_if_panel', NO))
# a QMID is asked only once a cost of its category is entered (as lines 23, 24 and 29 already do)
for cat, cost in [('doors', 'f5695.doors_cost'), ('windows', 'f5695.line20c'), ('ac', 'f5695.line22c'), ('enabling', 'f5695.line25c')]:
    nq = f'f5695.{cat}_no_qmid'; c = cite_of(nq)
    B[f'f5695.{cat}_costs'] = line(f'f5695.{cat}_costs', f'A cost is entered in this category ({cat})', 'Bool',
        f"    expr:\n      op: test\n      gt:\n      - {cost}\n      - param: sales.zero\n", c)
    B[f'f5695.{cat}_qmid_missing'] = line(f'f5695.{cat}_qmid_missing', f'No valid QMID for an item of this category ({cat})', 'Bool',
        f"    expr:\n      op: test\n      eq:\n      - f5695.qmid_{cat}\n      - const: false\n", c)
    set_expr(nq, choose_expr(f'f5695.{cat}_costs', f'f5695.{cat}_qmid_missing', NO))
    order[order.index(nq):order.index(nq)] = [f'f5695.{cat}_costs', f'f5695.{cat}_qmid_missing']
# spouses with separate main homes: asked only on a joint return
alts = ''.join(f"""      - guard:
          op: test
          eq:
          - f1040.status
          - const: {s}
        then: {'f5695.separate_homes' if s == 'mfj' else NO}
""" for s in ['single', 'mfj', 'mfs', 'hoh', 'qss'])
set_expr('f5695.separate_homes_joint', "    expr:\n      op: choose\n      alternatives:\n" + alts)

i0 = order.index('f5695.part1_any')
body = ''.join(B[i] for i in order[:i0]) + new_head + ''.join(B[i] for i in order[i0:])
head = head.replace("Each part is figured only when its screen question is\n    answered Yes; otherwise its Schedule 3 line is zero.",
                    "Each kind of property is asked\n    by a yes or no question beneath one opening question, and a part is figured only when one of its kinds was installed.")
P.write_text(head + body)
import yaml
d = yaml.safe_load(P.read_text())
seen = [l['id'] for l in d['form']['lines']]
assert len(seen) == len(set(seen)), 'duplicate ids'
print('lines:', len(seen), 'gated:', sum(1 for l in d['form']['lines'] if l.get('gated_by')))
