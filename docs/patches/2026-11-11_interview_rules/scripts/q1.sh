#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w1
$S $W dep_qr /tmp/f1095a/out/ret_dep_odc.json dependent.qualifying_relative
$S $W dep_incx /tmp/f1095a/out/ret_dep_odc.json dependent.income_exception
$S $W dep_qrrel /tmp/f1095a/out/ret_dep_odc.json dependent.qr_other_relation dependent.qr_household_member
$S $W dep_hoh /tmp/f1095a/out/ret_dep_small.json dependent.hoh_test2 dependent.hoh_test1 dependent.hoh_test2_lived
echo done > /tmp/f1095a/out/q1.done
