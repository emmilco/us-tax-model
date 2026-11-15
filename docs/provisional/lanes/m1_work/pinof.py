# Print, for a pinned argument id, its premises, digest, and the premise diff since the commit that recorded the digest.
import sys,re,json,subprocess
W='/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1'
src=open(W+'/engine/src/mutate.ts').read().split('\n')
for mid in sys.argv[1:]:
    i=[n for n,l in enumerate(src) if l.strip().startswith('"'+mid+'"')]
    if not i: print(mid,'no entry'); continue
    nxt=src[i[0]+1].strip()
    prem=json.loads(nxt[:nxt.index(']')+1])
    dg=re.search(r'"([0-9a-f]{16})"',nxt).group(1)
    c=subprocess.check_output(['git','-C',W,'log','-1','--format=%h','-S',dg,'--','engine/src/mutate.ts']).decode().strip()
    print('==',mid,dg,'recorded at',c)
    sys.stdout.flush()
    subprocess.run(['python3',__import__('os').path.join(__import__('os').path.dirname(__file__),'pindiff.py'),c,','.join(prem)])
