#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w2; R=/tmp/f1095a/out
until [ -f $R/q2.done ]; do sleep 15; done
python3 -I -c "import json; json.dump([[6,15],[96,11]], open('$R/ret_f5695.json','w'))"
node /tmp/f1095a/scripts/measure.mjs /tmp/f1095a/base $R/ret_f5695.json $R/base_measure_f5695.json > $R/base_measure_f5695.txt 2>&1
$S $W f5695 $R/ret_f5695.json f5695.sec_a_claimed f5695.sec_a_new_home f5695.sec_b_claimed f5695.sec_b_new_home f5695.enabling_claimed f5695.separate_homes_joint f5695.ac_no_qmid f5695.doors_no_qmid f5695.windows_no_qmid f5695.enabling_no_qmid
echo done > $R/q6.done
