#!/bin/bash
# usage: sweep2.sh <repo> <tag> <n> <first seed> <last seed> <parallel>   (federal; refused returns get the bank-order walk only)
cd /tmp/f1095a
mkdir -p out/$2
start=$(date +%s)
seq "$4" "$5" | SKIP_REFUSED=1 xargs -P "$6" -I{} sh -c "node scripts/seeds.mjs $1 full {} $3 > out/$2/s{}.jsonl 2> out/$2/s{}.err"
echo "sweep $2 n=$3 seeds $4..$5 parallel $6: $(( $(date +%s) - start )) s wall" > out/$2/time.txt
