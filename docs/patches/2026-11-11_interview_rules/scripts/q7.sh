#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w2; R=/tmp/f1095a/out
until [ -f $R/q6.done ]; do sleep 15; done
node /tmp/f1095a/scripts/measure.mjs /tmp/f1095a/base $R/ret_sav.json $R/base_measure_sav.json > $R/base_measure_sav.txt 2>&1
$S $W sav $R/ret_sav.json person.sav_ineligible
node /tmp/f1095a/scripts/minimal.mjs $W $R/min_dec_only.json > $R/fam_sav/min_dec_only.txt 2>&1
echo done > $R/q7.done
