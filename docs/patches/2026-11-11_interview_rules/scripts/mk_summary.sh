#!/bin/bash
cd /tmp/f1095a
python3 -I scripts/famsummary.py dep_odc:dep_odc dep_qr:dep_odc dep_incx:dep_odc dep_qrrel:dep_odc dep_hoh:dep_small dep_hoh1:dep_small dep_hoh2:dep_small dep_hoh2lived:dep_small dep_edutin:edutin f8962_bzero:f8962b f8962_applicable:f8962 f5695:f5695 f8889:f8889c scveh:scveh retirement:retirement ssb:ssb asset:asset s1a_died:s1a_died carloan:carloan eic_step3:eic_step3 f2441:f2441 sa:sa eic_age:eic_age sav:sav > out/famsummary.json
python3 -I scripts/gen_tables.py > out/catalog_tables.md
python3 -I scripts/gen_families.py > out/catalog_families.md
wc -l out/catalog_tables.md out/catalog_families.md
