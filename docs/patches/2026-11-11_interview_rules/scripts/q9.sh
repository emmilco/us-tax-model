#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w2; R=/tmp/f1095a/out
until [ -f $R/q7.done ]; do sleep 15; done
node /tmp/f1095a/scripts/measure.mjs /tmp/f1095a/base $R/ret_edutin.json $R/base_measure_edutin.json > $R/base_measure_edutin.txt 2>&1
$S $W dep_edutin $R/ret_edutin.json dependent.edu_llc_tin_refused person.edu_llc_tin_refused
echo done > $R/q9.done
