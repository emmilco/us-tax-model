#!/bin/bash
# t.sh name fixture caseid "targets" overrides...
n=$1; f=$2; c=$3; t=$4; shift 4
W=research/audits/ruling-audit-1/witnesses/$n.json
python3 /tmp/claude-0/sp/mk.py fixtures/2025/$f.json $c $W "$@"
echo "### $n  base=$f#$c  overrides: $*" | tee -a /tmp/claude-0/sp/runlog.txt
python3 /tmp/claude-0/sp/ev.py $W $t 2>&1 | grep -v '^  ' | tee -a /tmp/claude-0/sp/runlog.txt
