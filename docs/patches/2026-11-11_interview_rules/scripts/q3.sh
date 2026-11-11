#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w3
$S $W scveh /tmp/f1095a/out/ret_scveh.json scveh.is_actual_owned scveh.is_actual_leased
$S $W retirement /tmp/f1095a/out/ret_retirement.json retirement.has_exception retirement.is_e05 retirement.is_e09 retirement.is_e19 retirement.is_e22 retirement.is_e23 retirement.wrong_kind
$S $W ssb /tmp/f1095a/out/ret_ssb.json ssb.mfs_together f1040.line6d
$S $W asset /tmp/f1095a/out/ret_asset.json asset.s179_bad
echo done > /tmp/f1095a/out/q3.done
