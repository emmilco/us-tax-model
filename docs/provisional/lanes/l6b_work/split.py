"""Take a screen input apart: the old id becomes a derived line (true when any child is true), each child is a new
input, a gated child gets a gate line. Usage: python3 l6b_split.py <spec.py>; the spec defines FORM, SCREEN, HELPERS,
CHILDREN (see the lane's spec files). Text surgery on the form YAML, so the rest of the file is byte-identical."""
import sys, textwrap, re

spec = {}
exec(open(sys.argv[1]).read(), spec)
FORM, SCREEN = spec['FORM'], spec['SCREEN']
path = f'forms/2025/{FORM}.yaml'
s = open(path).read()

start = s.index(f'  - id: {SCREEN}\n')
end = s.index('  - id: ', start + 10)
old = s[start:end]
m = re.search(r'    expr:\n      op: input\n      source: (.*?)\n(    cite:\n.*)', old, re.S)
assert m, 'screen layout'
source_yaml, cite_tail = m.group(1), m.group(2)
head = old[:old.index('    expr:\n')]
# the old question text becomes the derived line's label (MAP 4.1.4: the label keeps the full statement)
head = re.sub(r'    label: .*\n', lambda _: '    label: ' + source_yaml + '\n', head, count=1)
only_cite = re.match(r'(    cite:\n      doc: .*\n      locator: .*?\n)(?=    [a-z]|\Z)', cite_tail, re.S).group(1)


def wrap(key, text, indent):
    """One YAML scalar: plain text folded at 118 columns, single-quoted when it needs it."""
    if '\n' in text:
        body = '\n'.join((' ' * (indent + 2) + ln) if ln else '' for ln in text.split('\n'))
        return ' ' * indent + key + ': |-\n' + body + '\n'
    q = "'" + text.replace("'", "''") + "'"
    lines = textwrap.wrap(key + ': ' + q, width=118 - indent, break_long_words=False, break_on_hyphens=False)
    return ' ' * indent + lines[0] + '\n' + ''.join(' ' * (indent + 2) + ln + '\n' for ln in lines[1:])


def guard(line, value):
    v = 'true' if value is True else 'false' if value is False else value
    return f'      - guard:\n          op: test\n          eq:\n          - {line}\n          - const: {v}\n'


out = []
tests = []
NO = f'{FORM}.no'
for h in spec.get('HELPERS', []):
    # a Bool helper: {id, label, when: (line, value), then: line}  = then when the condition holds, false otherwise
    cond, val = h['when']
    other = (not val) if isinstance(val, bool) else None
    assert other is not None
    out.append(f"  - id: {h['id']}\n    printed: (helper)\n" + wrap('label', h['label'], 4) + "    type: Bool\n    expr:\n      op: choose\n      alternatives:\n"
               + guard(cond, val) + f"        then: {h['then']}\n" + guard(cond, other) + f"        then: {NO}\n" + only_cite)
for c in spec['CHILDREN']:
    cid = c['id']
    gate = c.get('gate')
    line = f"  - id: {cid}\n    printed: (screen)\n" + wrap('label', c['label'], 4) + "    type: Bool\n"
    if gate:
        gid = f"{cid}_if_{c['gate_name']}"
        line += f"    gated_by: {gid}\n"
    line += "    expr:\n      op: input\n" + wrap('source', c['q'], 6) + only_cite
    out.append(line)
    read = cid
    if gate:
        cond, val = gate
        out.append(f"  - id: {gid}\n    printed: (gate)\n" + wrap('label', c['label'] + ', asked only ' + c['gate_says'] + ' (false otherwise)', 4)
                   + "    type: Bool\n    expr:\n      op: choose\n      alternatives:\n"
                   + guard(cond, val) + f"        then: {cid}\n" + guard(cond, not val) + f"        then: {NO}\n" + only_cite)
        read = gid
    if c.get('counts', True) is not False:
        want = 'false' if c.get('refuses_on') is False else 'true'
        tests.append(f"      - op: test\n        eq:\n        - {read}\n        - const: {want}\n")
derived = head + "    expr:\n      op: test\n      any:\n" + ''.join(tests) + cite_tail
s = s[:start] + ''.join(out) + derived + s[end:]
open(path, 'w').write(s)
print('children', len(spec['CHILDREN']), 'operands', len(tests))
