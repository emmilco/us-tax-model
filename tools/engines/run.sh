#!/usr/bin/env bash
# Engine differential (spec 6.5, class C): generated returns (single, head of household and
# married filing jointly) through the project and through PolicyEngine-US, Tax-Calculator and
# OpenTaxSolver, compared line by line. Skips visibly when the Python engines are not
# installed (tools/engines/setup.sh); run_engines.py leaves OpenTaxSolver out, visibly, when
# its package is not built.
set -euo pipefail
# Arguments (--year N) are passed to every step; the paths below use the year they resolve to.
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.engines/venv"
WORK="$ROOT/.engines/work"
N="${ENGINE_CASES:-1000}"
J="${ENGINE_JOINT_CASES:-400}"
S="${ENGINE_SE_CASES:-300}"
SEED="${ENGINE_SEED:-20260101}"
Y="$(python3 -I -c 'import sys; sys.path.insert(0, sys.argv[1]); sys.argv[1:2] = []; import taxyear; print(taxyear.Y)' "$ROOT/tools" "$@")"
if [ ! -x "$VENV/bin/python" ]; then
  echo "engine differential: SKIPPED - engines not installed; run tools/engines/setup.sh once (network) to enable this check"
  exit 0
fi
mkdir -p "$WORK"
python3 -I "$ROOT/tools/engines/generate_cases.py" "$@" --count "$N" --joint "$J" --se "$S" --seed "$SEED" --out "$WORK/cases.json"
node "$ROOT/engine/dist/main.js" eval "$@" --batch "$WORK/cases.json" > "$WORK/project.json"
"$VENV/bin/python" -I "$ROOT/tools/engines/run_engines.py" "$@" --cases "$WORK/cases.json" --out "$WORK/engines.json"
python3 -I "$ROOT/tools/engines/compare.py" "$@" --cases "$WORK/cases.json" --project "$WORK/project.json" --engines "$WORK/engines.json" \
  --investigations "$ROOT/fixtures/$Y/differential/engine_investigations.json" --report "$ROOT/reports/$Y/engine_differential.md"
