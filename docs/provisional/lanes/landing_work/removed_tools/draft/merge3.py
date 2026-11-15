#!/usr/bin/env python3
"""Three-way structural merges for the provisional clone: fixture JSON (by key / case id) and the question bank (by entry).
usage: merge3.py <path>   (reads stages 1,2,3 of a conflicted path from git, writes the merged file, exits 1 on a true conflict)"""
import json, subprocess, sys, re

def stage(n, path):
    r = subprocess.run(['git', 'show', f':{n}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

conflicts = []

def keyed(lst):
    if all(isinstance(x, dict) and 'id' in x for x in lst):
        ids = [x['id'] for x in lst]
        if len(set(ids)) == len(ids):
            return 'id'
    if all(isinstance(x, dict) and 'input' in x for x in lst):
        ids = [x['input'] for x in lst]
        if len(set(ids)) == len(ids):
            return 'input'
    return None

MISSING = object()

def m(base, ours, theirs, where):
    if ours == theirs: return ours
    if base == ours: return theirs
    if base == theirs: return ours
    if isinstance(ours, dict) and isinstance(theirs, dict):
        b = base if isinstance(base, dict) else {}
        out = {}
        keys = list(ours.keys()) + [k for k in theirs.keys() if k not in ours]
        # keep theirs' new keys near their predecessor
        if any(k not in ours for k in theirs):
            keys = []
            tk = list(theirs.keys()); seen = set()
            for k in ours.keys():
                keys.append(k); seen.add(k)
            for i, k in enumerate(tk):
                if k in seen: continue
                prev = next((p for p in reversed(tk[:i]) if p in keys), None)
                keys.insert(keys.index(prev) + 1 if prev is not None else 0, k); seen.add(k)
        for k in keys:
            bo, oo, to = b.get(k, MISSING), ours.get(k, MISSING), theirs.get(k, MISSING)
            if oo is MISSING and to is MISSING: continue
            if oo is MISSING:
                if bo is MISSING: out[k] = to
                elif bo == to: pass  # ours deleted
                else: conflicts.append(f'{where}.{k}: deleted by ours, changed by theirs'); out[k] = to
                continue
            if to is MISSING:
                if bo is MISSING: out[k] = oo
                elif bo == oo: pass
                else: conflicts.append(f'{where}.{k}: deleted by theirs, changed by ours'); out[k] = oo
                continue
            out[k] = m(None if bo is MISSING else bo, oo, to, f'{where}.{k}')
        return out
    if isinstance(ours, list) and isinstance(theirs, list):
        b = base if isinstance(base, list) else []
        k = keyed(ours) if keyed(ours) and keyed(ours) == keyed(theirs) and (not b or keyed(b) == keyed(ours)) else None
        if k:
            bd = {x[k]: x for x in b}; od = {x[k]: x for x in ours}; td = {x[k]: x for x in theirs}
            d = m(bd, od, td, where)
            return list(d.values())
        if len(b) == len(ours) == len(theirs):
            return [m(b[i], ours[i], theirs[i], f'{where}[{i}]') for i in range(len(ours))]
        # plain lists of scalars: union of additions, minus removals
        try:
            bs = [json.dumps(x, sort_keys=True) for x in b]; os_ = [json.dumps(x, sort_keys=True) for x in ours]; ts = [json.dumps(x, sort_keys=True) for x in theirs]
            out = [x for x in ours if json.dumps(x, sort_keys=True) not in (set(bs) - set(ts))]
            for i, x in enumerate(theirs):
                s = json.dumps(x, sort_keys=True)
                if s not in bs and s not in os_: out.append(x)
            return out
        except Exception:
            pass
    conflicts.append(f'{where}: both changed')
    return ours

def bank_entries(text):
    """split the bank file into (head, [(key, block)], tail) where a block starts with '  - input: X' under 'questions:'"""
    lines = text.split('\n')
    starts = [i for i, l in enumerate(lines) if re.match(r'^  - input: ', l)]
    if not starts: return text, [], ''
    head = '\n'.join(lines[:starts[0]])
    blocks = []
    for a, b_ in zip(starts, starts[1:] + [len(lines)]):
        key = lines[a][len('  - input: '):].strip()
        blocks.append((key, '\n'.join(lines[a:b_])))
    # the last block may carry the file's trailing newline
    return head, blocks, ''

def merge_bank(path):
    b, o, t = stage(1, path), stage(2, path), stage(3, path)
    hb, eb, _ = bank_entries(b); ho, eo, _ = bank_entries(o); ht, et, _ = bank_entries(t)
    head = ho if hb == ht else (ht if hb == ho else None)
    if head is None:
        # merge the head with git merge-file
        import tempfile, os
        fs = []
        for s in (ho, hb, ht):
            f = tempfile.NamedTemporaryFile('w', delete=False); f.write(s + '\n'); f.close(); fs.append(f.name)
        r = subprocess.run(['git', 'merge-file', '-p'] + fs, capture_output=True, text=True)
        head = r.stdout.rstrip('\n')
        if r.returncode != 0: conflicts.append('bank head (frames/groups): textual conflict')
    def strip(s): return s.rstrip('\n')
    bd = {k: strip(v) for k, v in eb}; od = {k: strip(v) for k, v in eo}; td = {k: strip(v) for k, v in et}
    for name, lst in (('base', eb), ('ours', eo), ('theirs', et)):
        if len({k for k, _ in lst}) != len(lst): conflicts.append(f'bank: duplicate entry keys in {name}')
    order = [k for k, _ in eo]
    tk = [k for k, _ in et]
    for i, k in enumerate(tk):
        if k in od: continue
        if k in bd and bd[k] == td[k]: continue  # ours deleted, theirs unchanged
        prev = next((p for p in reversed(tk[:i]) if p in order), None)
        order.insert(order.index(prev) + 1 if prev is not None else 0, k)
    out = []
    for k in order:
        bo, oo, to = bd.get(k), od.get(k), td.get(k)
        if oo is None: out.append(to); 
        elif to is None:
            if bo is None or bo != oo:
                if bo is not None: conflicts.append(f'bank {k}: deleted by theirs, changed by ours')
                out.append(oo) if bo is None or True else None
            # else deleted by theirs, unchanged by ours: drop
            if bo is not None and bo == oo: out.pop() if False else None
        elif oo == to or bo == to: out.append(oo)
        elif bo == oo: out.append(to)
        else:
            conflicts.append(f'bank {k}: changed by both'); out.append(oo)
    # drop entries deleted by theirs and unchanged by ours
    final = []
    for k, blk in zip(order, out):
        final.append(blk)
    # rebuild honoring theirs-deletions
    final = []
    j = 0
    for k in order:
        bo, oo, to = bd.get(k), od.get(k), td.get(k)
        if to is None and oo is not None and bo is not None and bo == oo:
            continue
        if oo is None: final.append(to)
        elif to is None: final.append(oo)
        elif oo == to or bo == to: final.append(oo)
        elif bo == oo: final.append(to)
        else: final.append(oo)
    open(path, 'w').write(head + '\n' + '\n'.join(final) + '\n')

def main():
    path = sys.argv[1]
    if path.endswith('questions.yaml'):
        merge_bank(path)
    else:
        b, o, t = (stage(n, path) for n in (1, 2, 3))
        out = m(json.loads(b) if b else None, json.loads(o), json.loads(t), '$')
        # write in the file's own format (the one that reproduces our side byte for byte), so the diff shows only the merge
        fmt = next(((i, a) for i in (2, 1) for a in (False, True) if json.dumps(json.loads(o), indent=i, ensure_ascii=a) + '\n' == o), (2, False))
        open(path, 'w').write(json.dumps(out, indent=fmt[0], ensure_ascii=fmt[1]) + '\n')
    if conflicts:
        print(f'{path}: {len(conflicts)} true conflict(s)'); [print('   ', c) for c in conflicts[:25]]
        sys.exit(1)
    print(f'{path}: merged structurally')
main()
