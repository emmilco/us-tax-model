#!/usr/bin/env bash
# Engine differential (spec 6.5, class C): generated returns (single, head of household and
# married filing jointly) through
# the project and through PolicyEngine-US and Tax-Calculator, compared line by
# line. Skips visibly when the engines are not installed (tools/engines/setup.sh).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.engines/venv"
WORK="$ROOT/.engines/work"
N="${ENGINE_CASES:-1000}"
J="${ENGINE_JOINT_CASES:-400}"
SEED="${ENGINE_SEED:-20260101}"
if [ ! -x "$VENV/bin/python" ]; then
  echo "engine differential: SKIPPED - engines not installed; run tools/engines/setup.sh once (network) to enable this check"
  exit 0
fi
mkdir -p "$WORK"
python3 -I "$ROOT/tools/engines/generate_cases.py" --count "$N" --joint "$J" --seed "$SEED" --out "$WORK/cases.json"
node "$ROOT/engine/dist/main.js" eval --batch "$WORK/cases.json" > "$WORK/project.json"
"$VENV/bin/python" -I "$ROOT/tools/engines/run_engines.py" --cases "$WORK/cases.json" --out "$WORK/engines.json"
python3 -I "$ROOT/tools/engines/compare.py" --cases "$WORK/cases.json" --project "$WORK/project.json" --engines "$WORK/engines.json" \
  --investigations "$ROOT/fixtures/2025/differential/engine_investigations.json" --report "$ROOT/reports/2025/engine_differential.md"
