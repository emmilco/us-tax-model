#!/bin/bash
W=/tmp/f1095a/all2; O=/tmp/f1095a/out/all2; mkdir -p $O
cd $W && git checkout -q .
python3 -I /tmp/f1095a/scripts/nest.py $W dependent.odc_person dependent.qualifying_relative dependent.income_exception dependent.qr_other_relation dependent.qr_household_member dependent.hoh_test2 dependent.hoh_test1 dependent.hoh_test2_lived dependent.edu_llc_tin_refused \
  'f8962.b_zero!' f8962.applicable f8962.alien_branch \
  f5695.sec_a_claimed f5695.sec_a_new_home f5695.sec_b_claimed f5695.sec_b_new_home f5695.enabling_claimed f5695.separate_homes_joint f5695.ac_no_qmid f5695.doors_no_qmid f5695.windows_no_qmid f5695.enabling_no_qmid \
  f8889.excess f8889.married_family scveh.is_actual_owned scveh.is_actual_leased \
  retirement.has_exception retirement.is_e05 retirement.is_e09 retirement.is_e19 retirement.is_e22 retirement.is_e23 'retirement.wrong_kind!' \
  ssb.mfs_together f1040.line6d asset.s179_bad carloan.eligible eic.step3_married f2441.nondependent_gate sa.itemizes person.edu_llc_tin_refused person.sav_ineligible > $O/nest.txt 2>&1
bash /tmp/f1095a/patches_hand/s1a_died.sh $W >> $O/nest.txt 2>&1
bash /tmp/f1095a/patches_hand/eic_age.sh $W >> $O/nest.txt 2>&1
git diff -- forms interview > /tmp/f1095a/patches/ALL_combined.patch
if ! npm run build --silent > $O/build.txt 2>&1; then echo "BUILD FAILED" > $O/done; exit 1; fi
node engine/dist/main.js test-fixtures > $O/fixtures_fed.txt 2>&1; echo "exit $?" >> $O/fixtures_fed.txt
node engine/dist/main.js test-fixtures --ny > $O/fixtures_ny.txt 2>&1; echo "exit $?" >> $O/fixtures_ny.txt
node /tmp/f1095a/scripts/differential.mjs /tmp/f1095a/base $W 3000 11 > $O/differential.txt 2>&1
node /tmp/f1095a/scripts/pins.mjs /tmp/f1095a/base $W > $O/pins.txt 2>&1
s=$(date +%s); node engine/dist/main.js interview-rules > $O/rules_default.txt 2>&1; echo "exit $? in $(( $(date +%s) - s )) s" >> $O/rules_default.txt
/tmp/f1095a/scripts/sweep2.sh $W all2_sweep 50 1 40 5
(node engine/dist/main.js render > $O/render.txt 2>&1; node engine/dist/main.js render --ny >> $O/render.txt 2>&1; git status --short rendered > $O/rendered_changed.txt)
echo ok > $O/done
