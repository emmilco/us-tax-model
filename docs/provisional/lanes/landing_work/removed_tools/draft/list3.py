#!/usr/bin/env python3
"""Three-way merge of a file whose lines are items (a profile's list of inputs, a persona's answers): our lines, minus the
lines their side removed, plus the lines their side added, each placed after the line it follows on their side.
usage: list3.py <path> [<theirs-rev> [<ours-rev>]]   (base = merge-base of ours and theirs; theirs defaults to
MERGE_HEAD, ours to HEAD; after a merge is committed: list3.py <path> HEAD^2 HEAD^1)
Writes the file. Exits 1, naming them, when a key (the text before ':') is left with two different lines: both sides
changed one answer, which is for a person to settle. Refuses a file with repeated lines other than blank ones."""
import subprocess, sys

def show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], capture_output=True, text=True)
    return r.stdout.split('\n') if r.returncode == 0 else []

def main():
    path = sys.argv[1]; theirs_rev = sys.argv[2] if len(sys.argv) > 2 else 'MERGE_HEAD'
    ours_rev = sys.argv[3] if len(sys.argv) > 3 else 'HEAD'
    base_rev = subprocess.run(['git', 'merge-base', ours_rev, theirs_rev], capture_output=True, text=True).stdout.strip()
    base, ours, theirs = show(base_rev, path), show(ours_rev, path), show(theirs_rev, path)
    for name, lines in (('ours', ours), ('theirs', theirs)):
        solid = [l for l in lines if l.strip()]
        if len(set(solid)) != len(solid):
            dup = sorted({l for l in solid if solid.count(l) > 1})
            print(f'{path}: repeated lines in {name}, not merged: {dup[:5]}'); sys.exit(2)
    bs, ts, os_ = set(base), set(theirs), set(ours)
    out = [l for l in ours if not (l in bs and l not in ts and l.strip())]
    for i, l in enumerate(theirs):
        if not l.strip() or l in bs or l in os_: continue
        prev = next((p for p in reversed(theirs[:i]) if p.strip() and p in out), None)
        out.insert(out.index(prev) + 1 if prev is not None else len(out), l)
    open(path, 'w').write('\n'.join(out))
    keys = {}
    for l in out:
        if ':' in l and l.strip() and not l.lstrip().startswith(('#', '- ')):
            keys.setdefault(l.split(':')[0].strip(), []).append(l)
    twice = {k: v for k, v in keys.items() if len(v) > 1}
    if twice:
        print(f'{path}: {len(twice)} key(s) changed by both sides:'); [print('   ', v) for v in twice.values()]
        sys.exit(1)
    print(f'{path}: merged by line ({len(out) - len(ours):+d} lines against ours)')
main()
