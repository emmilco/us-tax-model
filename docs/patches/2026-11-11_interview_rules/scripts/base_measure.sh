#!/bin/bash
cd /tmp/f1095a
for f in out/ret_*.json; do fam=$(basename $f .json); fam=${fam#ret_}; node scripts/measure.mjs /tmp/f1095a/base $f out/base_measure_$fam.json > out/base_measure_$fam.txt 2>&1; done
echo done > out/base_measure.done
