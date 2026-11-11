#!/bin/bash
# usage: sweep.sh <profile> <n> <first seed> <last seed> <parallel>
cd /tmp/f1095a
start=$(date +%s)
seq "$3" "$4" | xargs -P "$5" -I{} sh -c "node scripts/seeds.mjs /tmp/f1095a/repo $1 {} $2 > out/sweep_$1_{}.jsonl 2> out/sweep_$1_{}.err"
echo "sweep $1 n=$2 seeds $3..$4 parallel $5: $(( $(date +%s) - start )) s wall" > out/sweep_$1.time
