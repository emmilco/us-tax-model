#!/bin/bash
# The earlier agent's one-id rename, applied to a copy of its pristine clone of 355d7302, then built.
set -e
cd /tmp/f1095a
cp -R /tmp/yearfree/repo1 repo355_r1
cd repo355_r1
grep -rlE "(^|[^A-Za-z0-9_.])eic\.died_2025([^A-Za-z0-9_]|$)" forms interview fixtures engine/src tools params ambiguities tables lean ui 2>/dev/null | grep -v "tools/year_diff.py" | while read f; do perl -pi -e 's/(?<![A-Za-z0-9_.])\Qeic.died_2025\E(?![A-Za-z0-9_])/eic.died/g' "$f"; done
npm run build --silent > /tmp/f1095a/out/build355.txt 2>&1
node engine/dist/main.js interview-rules > /tmp/f1095a/r1_355_default.txt 2>&1 || true
tail -1 /tmp/f1095a/r1_355_default.txt
