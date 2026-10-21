#!/usr/bin/env bash
# The steps of check-all, in order, for one tax year: pass --year N to check a
# year other than the default (the newest adopted year in years.json); every
# step receives the same arguments. tools/check_all.sh runs this and guards it.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
node=(node engine/dist/main.js)

python3 tools/fetch_sources.py "$@"
python3 tools/check_extraction.py "$@"
python3 tools/check_macrs_tables.py "$@"
python3 tools/check_auto_limits.py "$@"
python3 tools/check_bug_inventory.py
python3 tools/transcription/check_logs.py "$@"
python3 tools/transcription/check_table_logs.py "$@"
python3 tools/citations.py "$@"
python3 tools/citations.py --self-test "$@"
npm run compile --silent
"${node[@]}" build "$@"
"${node[@]}" render "$@"
"${node[@]}" conjecture "$@"
"${node[@]}" test-fixtures "$@"
"${node[@]}" test-integration "$@"
"${node[@]}" coverage "$@"
"${node[@]}" evidence "$@"
"${node[@]}" properties "$@"
"${node[@]}" differential "$@"
tools/engines/run.sh "$@"
"${node[@]}" mutate "$@"
(cd lean && lake build taxeval >/dev/null 2>&1)
"${node[@]}" compare "$@"
"${node[@]}" review-stage2 "$@"
"${node[@]}" review-stage3 "$@"
"${node[@]}" review-stage4 "$@"
"${node[@]}" review-stage5 "$@"
