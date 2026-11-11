#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w1; R=/tmp/f1095a/out
$S $W f2441 $R/ret_f2441.json f2441.nondependent_gate
$S $W sa $R/ret_sa.json sa.itemizes
$S $W eic_age $R/ret_eic_age.json
echo done > $R/q5.done
