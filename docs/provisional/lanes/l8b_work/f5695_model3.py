"""Lane 8b scratch, applied once after f5695_model2.py: all seventeen kinds are asked together, directly after the
opening question. A test of `any` is decided by its first true operand, so after one Yes the other kinds were asked
only later, where a cost line first read them. f5695.kinds_answered needs every kind's answer (each operand is "Yes
or No", unknown until the kind is answered, and `all` asks every undecided operand at once); it is always true once
they are answered, and the two part lines read the kinds only through it.
Run from the worktree root: python3 docs/provisional/lanes/l8b_work/f5695_model3.py"""
import re
from pathlib import Path
P = Path('forms/2025/f5695.yaml'); t = P.read_text()
assert 'f5695.kinds_answered' not in t, 'already applied'
KINDS = ['solar', 'solar_water', 'wind', 'geothermal', 'line5a', 'line7a', 'insulation', 'doors', 'windows', 'panel', 'audit',
         'heat_pump', 'hp_water_heater', 'central_ac', 'water_heater', 'furnace', 'biomass']
def block(i):
    m = re.search(r'(?ms)^  - id: ' + re.escape(i) + r'\n.*?(?=^  - id: )', t); return m.group(0)
answered = "  - id: f5695.kinds_answered\n    printed: (helper)\n    label: Every kind of property has been answered Yes or No\n    type: Bool\n    expr:\n      op: test\n      all:\n"
for k in KINDS:
    g = f'f5695.{k}_if_any'
    answered += f"      - op: test\n        any:\n        - op: test\n          eq:\n          - {g}\n          - const: true\n        - op: test\n          eq:\n          - {g}\n          - const: false\n"
p1 = block('f5695.part1_any')
cite = p1[p1.index('    cite:\n'):]
answered += cite
def choose(i, label, then):
    return f"""  - id: {i}
    printed: (helper)
    label: {label}
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - f5695.kinds_answered
          - const: true
        then: {then}
      - guard:
          op: test
          eq:
          - f5695.kinds_answered
          - const: false
        then: f5695.no
""" + cite
for part in ('part1', 'part2'):
    b = block(f'f5695.{part}_any')
    label = re.search(r'(?m)^    label: (.*)$', b).group(1)
    some = b.replace(f'  - id: f5695.{part}_any\n', f'  - id: f5695.{part}_some\n')
    t = t.replace(b, some + choose(f'f5695.{part}_any', label, f'f5695.{part}_some'))
a = t.index('  - id: f5695.part1_some\n')
t = t[:a] + answered + t[a:]
P.write_text(t)
import yaml; d = yaml.safe_load(t); ids = [l['id'] for l in d['form']['lines']]; assert len(ids) == len(set(ids)); print(len(ids), 'lines')
