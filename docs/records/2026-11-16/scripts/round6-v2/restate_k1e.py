#!/usr/bin/env python3
"""Mechanical restatement for the scope.k1 split (k1block unit 1, decision D6).

Before the split, "scope.k1": false meant "no Schedule K-1 of any kind". After it, scope.k1 asks about partnerships
and S corporations only and the new scope.k1e about estates and trusts. Every fixture `inputs` object that states
"scope.k1": false and does not state scope.k1e gains "scope.k1e": false right after it, which keeps its meaning.
Fixture files that take defaults.json are unaffected in value (the default is false); class M, mutation and returns
fixtures state every scope answer, so without this they stop at "no input supplied for scope.k1e".
Text-level, so formatting is kept. Idempotent. Usage: restate_k1e.py ROOT [--check]
"""
import json
import re
import sys
from pathlib import Path

LINE = re.compile(r'^(?P<ind>[ \t]*)"scope\.k1": false(?P<comma>,?)[ \t]*$', re.M)


def restate(text):
    out, pos, n = [], 0, 0
    for m in LINE.finditer(text):
        # the next non-blank key in the same object; skip if scope.k1e is already stated in this object
        rest = text[m.end():m.end() + 4000]
        close = rest.find("}")
        if '"scope.k1e"' in rest[:close if close >= 0 else len(rest)]:
            continue
        before = text[max(0, m.start() - 4000):m.start()]
        if '"scope.k1e"' in before[before.rfind("{"):]:
            continue
        ind, comma = m.group("ind"), m.group("comma")
        repl = f'{ind}"scope.k1": false,\n{ind}"scope.k1e": false{comma}'
        out.append(text[pos:m.start()])
        out.append(repl)
        pos = m.end()
        n += 1
    out.append(text[pos:])
    return "".join(out), n


def main():
    root = Path(sys.argv[1])
    check = "--check" in sys.argv
    total = 0
    for d in ("fixtures/2025", "fixtures/ny/2025"):
        for f in sorted((root / d).glob("*.json")):
            text = f.read_text()
            new, n = restate(text)
            if n:
                json.loads(new)
                print(f"{n:5d}  {f.relative_to(root)}")
                total += n
                if not check:
                    f.write_text(new)
    print(f"{total} input object(s){' (check only)' if check else ''}")


if __name__ == "__main__":
    main()
