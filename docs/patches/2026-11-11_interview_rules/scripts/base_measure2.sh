#!/bin/bash
cd /tmp/f1095a
for fam in carloan eic_step3 f2441 sa eic_age f8962b dep_odc2; do node scripts/measure.mjs /tmp/f1095a/base out/ret_$fam.json out/base_measure_$fam.json > out/base_measure_$fam.txt 2>&1; done
echo done > out/base_measure2.done
