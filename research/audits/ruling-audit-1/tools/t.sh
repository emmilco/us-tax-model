#!/bin/bash
# t.sh name fixture caseid "targets" overrides...
n=$1; f=$2; c=$3; t=$4; shift 4
W=research/audits/ruling-audit-1/witnesses/$n.json
python3 research/audits/ruling-audit-1/tools/mk.py fixtures/2025/$f.json $c $W "$@"
echo "### $n  base=$f#$c  overrides: $*" | tee -a research/audits/ruling-audit-1/runlog.txt
python3 research/audits/ruling-audit-1/tools/ev.py $W $t 2>&1 | grep -v '^  ' | tee -a research/audits/ruling-audit-1/runlog.txt
