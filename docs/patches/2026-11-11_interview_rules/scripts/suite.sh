#!/bin/bash
# usage: suite.sh <repo> <tag>: fixture suite for both jurisdictions and interview-length, outputs under out/<tag>/
cd "$1"
mkdir -p /tmp/f1095a/out/$2
for j in fed ny; do
  s=$(date +%s)
  if [ $j = ny ]; then node engine/dist/main.js test-fixtures --ny > /tmp/f1095a/out/$2/fixtures_$j.txt 2>&1; else node engine/dist/main.js test-fixtures > /tmp/f1095a/out/$2/fixtures_$j.txt 2>&1; fi
  echo "exit $? in $(( $(date +%s) - s )) s" >> /tmp/f1095a/out/$2/fixtures_$j.txt
done
s=$(date +%s)
node engine/dist/main.js interview-length > /tmp/f1095a/out/$2/length.txt 2>&1
echo "exit $? in $(( $(date +%s) - s )) s" >> /tmp/f1095a/out/$2/length.txt
echo done > /tmp/f1095a/out/$2/suite.done
