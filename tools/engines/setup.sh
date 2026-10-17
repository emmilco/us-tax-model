#!/usr/bin/env bash
# One-time, deliberate network step: install the independent engines into a
# git-ignored virtualenv under .engines/. Nothing in the repository imports them;
# they run only in tools/engines/run_engines.py under this interpreter.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.engines/venv"
python3 -m venv "$VENV"
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$ROOT/tools/engines/requirements.txt"
"$VENV/bin/pip" show policyengine-us taxcalc | grep -E '^(Name|Version)'
echo "engines installed in $VENV"
