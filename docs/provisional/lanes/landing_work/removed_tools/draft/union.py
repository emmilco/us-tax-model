#!/usr/bin/env python3
"""resolve conflict hunks in a YAML list/map file by keeping both sides' lines (dedupe by the text before ':' or the whole line; theirs wins)"""
import re, sys
p = sys.argv[1]; s = open(p).read()
def fn(m):
    o, t = m.group(1).splitlines(), m.group(2).splitlines()
    key = lambda l: l.split(':')[0].strip() if ':' in l else l.strip()
    tk = {key(l) for l in t}
    return ''.join(l + '\n' for l in o if key(l) not in tk) + ''.join(l + '\n' for l in t)
s2, n = re.subn(r'<<<<<<< [^\n]*\n(.*?)(?:\|\|\|\|\|\|\| [^\n]*\n.*?)?=======\n(.*?)>>>>>>> [^\n]*\n', fn, s, flags=re.S)
open(p, 'w').write(s2); print(f'{p}: {n} hunk(s) unioned')
