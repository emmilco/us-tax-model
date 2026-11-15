"""Lane 8b scratch: this lane's questions in a persona's walk transcript: how many, their prompt and help words.
Usage: python3 docs/provisional/lanes/l8b_work/topic_words.py <transcript.md>..."""
import re, sys
MINE = re.compile(r'^(f5695\.|f8863\.|sli\.|person\[\w+\]\.edu(_|$)|dependent\[\w+\]\.edu(_|$))')
for f in sys.argv[1:]:
    t = open(f).read()
    rows = re.findall(r'(?ms)^### (\d+)\. `([^`]+)`.*?^- Words: prompt (\d+), help (\d+)', t)
    groups = {'home energy': r'^f5695\.', 'education': r'^(f8863\.|person|dependent)', 'student loans': r'^sli\.'}
    out = []
    for name, pat in groups.items():
        m = [(int(n), i, int(p), int(h)) for n, i, p, h in rows if MINE.match(i) and re.match(pat, i)]
        out.append(f"{name}: {len(m)} q, {sum(x[2] for x in m)} prompt w, {sum(x[3] for x in m)} help w, at {m[0][0]}–{m[-1][0]}" if m else f"{name}: 0")
    m = [(int(p), int(h)) for n, i, p, h in rows if MINE.match(i)]
    print(f.split('/')[-1], '|', f"all: {len(m)} q, {sum(x[0] for x in m)} prompt w, {sum(x[1] for x in m)} help w", '|', ' | '.join(out))
