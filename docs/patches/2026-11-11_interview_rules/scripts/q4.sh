#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w3; R=/tmp/f1095a/out
$S $W scveh $R/ret_scveh.json scveh.is_actual_owned scveh.is_actual_leased
$S $W retirement $R/ret_retirement.json retirement.has_exception retirement.is_e05 retirement.is_e09 retirement.is_e19 retirement.is_e22 retirement.is_e23 retirement.wrong_kind!
$S $W asset $R/ret_asset.json asset.s179_bad
$S $W carloan $R/ret_carloan.json carloan.eligible
$S $W eic_step3 $R/ret_eic_step3.json eic.step3_married
$S $W f8962_bzero $R/ret_f8962b.json f8962.b_zero!
echo done > $R/q4.done
