#!/bin/bash
# The widened check (60 complete returns) on the forms with every rewrite applied.
until [ -f /tmp/f1095a/out/all2/done ]; do sleep 20; done
cd /tmp/f1095a/wcheck_all && git apply /tmp/f1095a/patches/ALL_combined.patch && npm run build --silent > /tmp/f1095a/out/wall_build.txt 2>&1
for mode in default 60; do s=$(date +%s); if [ $mode = default ]; then node engine/dist/main.js interview-rules > /tmp/f1095a/out/wall_$mode.txt 2>&1; else INTERVIEW_RULES_COMPLETE=$mode node engine/dist/main.js interview-rules > /tmp/f1095a/out/wall_$mode.txt 2>&1; fi; echo "exit $? in $(( $(date +%s) - s )) s wall" >> /tmp/f1095a/out/wall_$mode.txt; done
node /tmp/f1095a/scripts/collections.mjs /tmp/f1095a/wcheck_all > /tmp/f1095a/out/wall_collections.jsonl 2> /tmp/f1095a/out/wall_collections.err
echo done > /tmp/f1095a/out/wall.done
