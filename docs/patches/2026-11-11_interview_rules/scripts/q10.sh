#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w3; R=/tmp/f1095a/out
until [ -f $R/q4.done ]; do sleep 15; done
node /tmp/f1095a/scripts/measure.mjs /tmp/f1095a/base $R/ret_f8889c.json $R/base_measure_f8889c.json > $R/base_measure_f8889c.txt 2>&1
$S $W f8889 $R/ret_f8889c.json f8889.excess f8889.married_family f8889.split
echo done > $R/q10.done
