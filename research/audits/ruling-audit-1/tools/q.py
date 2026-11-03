import json,sys
g=json.load(open('/tmp/claude-0/sp/graph.json'))
cmd,x=sys.argv[1],sys.argv[2]
if cmd=='gate': print(x,'refuses on:',g['gates'].get(x))
if cmd=='readers': print(x,'read by:',g['readers'].get(x))
if cmd=='deps': print(x,'reads:',g['deps'].get(x))
if cmd=='gatesof':  # which gates refuse on line x
    print([k for k,v in g['gates'].items() if x in v])
