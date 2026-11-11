#!/bin/bash
# usage: fam.sh <work copy> <family> <returns.json> <line id> [<line id> ...]
# Resets the work copy, rewrites the lines (nest.py), builds, runs the fixture suite for both jurisdictions, rechecks
# the family's witness returns and the standard length set, compares values with the base on generated returns,
# counts un-pinned mutation arguments and changed rendered files, and saves the patch.
W=$1; FAM=$2; RET=$3; shift 3
O=/tmp/f1095a/out/fam_$FAM; mkdir -p $O
cd $W || exit 1
git checkout -q . && git clean -qfd forms interview rendered 2>/dev/null
if [ -f /tmp/f1095a/patches_hand/$FAM.sh ]; then bash /tmp/f1095a/patches_hand/$FAM.sh $W > $O/nest.txt 2>&1; else python3 -I /tmp/f1095a/scripts/nest.py $W "$@" > $O/nest.txt 2>&1; fi
git diff -- forms interview > /tmp/f1095a/patches/$FAM.patch
if ! npm run build --silent > $O/build.txt 2>&1; then echo "BUILD FAILED" > $O/done; tail -5 $O/build.txt; exit 1; fi
node engine/dist/main.js test-fixtures > $O/fixtures_fed.txt 2>&1; echo "exit $?" >> $O/fixtures_fed.txt
node engine/dist/main.js test-fixtures --ny > $O/fixtures_ny.txt 2>&1; echo "exit $?" >> $O/fixtures_ny.txt
node /tmp/f1095a/scripts/measure.mjs $W $RET $O/measure.json > $O/measure.txt 2>&1
node /tmp/f1095a/scripts/differential.mjs /tmp/f1095a/base $W 1500 11 > $O/differential.txt 2>&1
node /tmp/f1095a/scripts/pins.mjs /tmp/f1095a/base $W > $O/pins.txt 2>&1
(node engine/dist/main.js render > $O/render.txt 2>&1; node engine/dist/main.js render --ny >> $O/render.txt 2>&1; git status --short rendered | wc -l > $O/rendered_changed.txt; git status --short rendered | head -20 >> $O/rendered_changed.txt)
git diff --stat -- forms > $O/diffstat.txt
echo ok > $O/done
tail -1 $O/fixtures_fed.txt $O/fixtures_ny.txt $O/measure.txt $O/differential.txt $O/pins.txt | cut -c1-300
