#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w4; R=/tmp/f1095a/out
$S $W dep_hoh1 $R/ret_dep_small.json dependent.hoh_test1
$S $W dep_hoh2 $R/ret_dep_small.json dependent.hoh_test2
$S $W dep_hoh2lived $R/ret_dep_small.json dependent.hoh_test2_lived
echo done > $R/q8.done
