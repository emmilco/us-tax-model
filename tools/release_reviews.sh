#!/usr/bin/env bash
# The release gate of the sampled reviews (tools/transcription/samples.py): on a fresh build of the working tree,
# no form may be due, short of the milestone's samples, or hold an unruled finding. Called by tools/release.sh.
# It leaves the working tree's tracked files as they are (the --release checks write no report).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
npm run -s compile >/dev/null
node engine/dist/main.js build >/dev/null
node engine/dist/main.js render >/dev/null
node engine/dist/main.js render --ny >/dev/null
python3 tools/transcription/check_completeness.py --release
python3 tools/transcription/check_completeness.py --release --jurisdiction ny
python3 tools/transcription/check_screens.py --release
python3 tools/transcription/check_screens.py --release --jurisdiction ny
