#!/bin/bash
# The earlier agent's actual new name (eic.died_in_year), applied to the copy already renamed to eic.died, then built.
set -e
cd /tmp/f1095a/repo355_r1
grep -rlE "(^|[^A-Za-z0-9_.])eic\.died([^A-Za-z0-9_]|$)" forms interview fixtures engine/src tools params ambiguities tables lean ui 2>/dev/null | grep -v "tools/year_diff.py" | while read f; do perl -pi -e 's/(?<![A-Za-z0-9_.])\Qeic.died\E(?![A-Za-z0-9_])/eic.died_in_year/g' "$f"; done
npm run build --silent > /tmp/f1095a/out/build355b.txt 2>&1
node engine/dist/main.js interview-rules > /tmp/f1095a/r1b_355_default.txt 2>&1 || true
tail -1 /tmp/f1095a/r1b_355_default.txt
