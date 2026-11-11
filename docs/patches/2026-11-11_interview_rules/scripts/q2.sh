#!/bin/bash
S=/tmp/f1095a/scripts/fam.sh; W=/tmp/f1095a/w2
$S $W dep_edutin /tmp/f1095a/out/ret_dep_small.json dependent.edu_llc_tin_refused
$S $W f8962_bzero /tmp/f1095a/out/ret_f8962.json f8962.b_zero
$S $W f8962_applicable /tmp/f1095a/out/ret_f8962.json f8962.applicable f8962.alien_branch
$S $W f8889 /tmp/f1095a/out/ret_f8889.json f8889.excess f8889.married_family
echo done > /tmp/f1095a/out/q2.done
