# Usage: repin.py MUTANT_ID [ADD_PREMISE,...]  -- adds premises to the pinned argument's list and records the current digest.
import sys,re,json,subprocess
W='/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1'
P=W+'/engine/src/mutate.ts'
mid=sys.argv[1]; add=[a for a in (sys.argv[2].split(',') if len(sys.argv)>2 and sys.argv[2] else [])]
src=open(P).read().split('\n')
i=[n for n,l in enumerate(src) if l.strip().startswith('"'+mid+'"')]
assert len(i)==1,(mid,i)
n=i[0]+1; line=src[n]
m=re.match(r'^(\s*)(\[.*?\]), "([0-9a-f]{16})"(.*)$',line)
assert m,line
prem=json.loads(m.group(2))
for a in add:
    if a not in prem: prem.append(a)
dg=subprocess.check_output(['node',__import__('os').path.join(__import__('os').path.dirname(__file__),'digest.mjs'),','.join(prem)]).decode().split()[0]
src[n]=f'{m.group(1)}{json.dumps(prem)}, "{dg}"{m.group(4)}'
open(P,'w').write('\n'.join(src))
print(mid,m.group(3),'->',dg,len(prem),'premises')
