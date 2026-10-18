#!/usr/bin/env bash
# One-time, deliberate network step: download the PolicyEngine-US microdata build
# that policyengine-us pins as its default dataset, into the git-ignored
# .engines/data/, and check it against the pinned hash. Needs tools/engines/setup.sh first.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.engines/venv"
mkdir -p "$ROOT/.engines/data"
"$VENV/bin/python" -I -c "
from huggingface_hub import hf_hub_download
hf_hub_download('policyengine/populace-us', 'populace_us_2024.h5', repo_type='dataset',
                revision='populace-us-2024-spm-20260909', local_dir='$ROOT/.engines/data')"
echo "6496cc4393d4d3c6574f76eca231de5898c803b9067645591fd5c4d3e65aee84  $ROOT/.engines/data/populace_us_2024.h5" | shasum -a 256 -c -
