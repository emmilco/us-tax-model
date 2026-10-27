#!/usr/bin/env bash
# One-time, deliberate network step: install the independent engines into a
# git-ignored virtualenv under .engines/. Nothing in the repository imports them;
# they run only in tools/engines/run_engines.py under this interpreter.
#
# OpenTaxSolver is built here from its package, which must be downloaded by hand:
# SourceForge answers every scripted fetch with a browser challenge. Save the
# Linux package (OpenTaxSolver<year>_<version>_linux64.tgz; it carries the C
# sources, the templates and prebuilt Linux binaries that are not run) into
# .engines/opentaxsolver-src/ and run this script again. A new release is a new
# tarball in that directory and a rerun: the adapter reads the version from the
# package's 0_README.txt, so no code changes.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.engines/venv"
OTS="$ROOT/.engines/opentaxsolver-src"
python3 -m venv "$VENV"
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$ROOT/tools/engines/requirements.txt"
"$VENV/bin/pip" show policyengine-us taxcalc | grep -E '^(Name|Version)'
echo "engines installed in $VENV"

# UsTaxes: the TypeScript sources at a pinned commit, used as shipped (never built or edited), and
# the three runtime packages its tax code imports, at the versions UsTaxes' package-lock pins, in
# a separate directory (a full `npm install` in the clone would fetch its React/Tauri tree).
# A newer commit is a change to USTAXES_COMMIT here and a rerun; the adapter reads the version and
# commit from the clone.
USTAXES_COMMIT=d276c7241dc85654758c7097e295d4d50a7fb435
UST="$ROOT/.engines/ustaxes-src"
if [ ! -d "$UST/.git" ]; then
  git clone --quiet https://github.com/ustaxes/UsTaxes "$UST"
fi
if [ "$(git -C "$UST" rev-parse HEAD)" != "$USTAXES_COMMIT" ]; then
  git -C "$UST" fetch --quiet origin "$USTAXES_COMMIT" && git -C "$UST" checkout --quiet "$USTAXES_COMMIT"
fi
npm install --silent --no-audit --no-fund --prefix "$ROOT/.engines/ustaxes-deps" lodash@4.18.1 loglevel@1.9.2 typescript@4.9.5
echo "UsTaxes: $(git -C "$UST" rev-parse --short=12 HEAD) in $UST, runtime packages in $ROOT/.engines/ustaxes-deps"

# SHA-256 of the packages this project has run; a tarball not listed here is built with a warning
# and its hash printed, to be added once the owner has checked the download.
KNOWN_SHA256="
0cc7e54030afb215399967df597b66704a879be0d746344e0e47f23e418e5e6b  OpenTaxSolver2025_23.06_linux64.tgz
"
mkdir -p "$OTS"
shopt -s nullglob
TARBALLS=("$OTS"/OpenTaxSolver*_linux64.tgz)
if [ ${#TARBALLS[@]} -eq 0 ]; then
  echo "OpenTaxSolver: no package found in $OTS"
  echo "  Download OpenTaxSolver<year>_<version>_linux64.tgz in a browser from"
  echo "  https://sourceforge.net/projects/opentaxsolver/files/ (scripted downloads are blocked),"
  echo "  save it into $OTS and rerun this script. The engine differential runs without it."
  exit 0
fi
for TGZ in "${TARBALLS[@]}"; do
  NAME="$(basename "$TGZ")"
  SUM="$(shasum -a 256 "$TGZ" | cut -d' ' -f1)"
  if echo "$KNOWN_SHA256" | grep -q "^$SUM  $NAME\$"; then
    echo "OpenTaxSolver: $NAME sha256 verified"
  else
    echo "OpenTaxSolver: WARNING $NAME has sha256 $SUM, not in KNOWN_SHA256 of tools/engines/setup.sh; add it once the download is checked"
  fi
  DIR="$OTS/${NAME%.tgz}"
  if [ ! -d "$DIR" ]; then
    tar -xzf "$TGZ" -C "$OTS"
  fi
  if [ ! -d "$DIR/src" ]; then
    echo "OpenTaxSolver: $DIR has no src/ directory; cannot build"; exit 1
  fi
  # The shipped binaries are Linux ELF files; the build replaces them with native ones.
  make -C "$DIR/src" -B all > "$DIR/build.log" 2>&1 || { echo "OpenTaxSolver: build failed, see $DIR/build.log"; exit 1; }
  echo "OpenTaxSolver: built $(ls "$DIR/bin" | wc -l | tr -d ' ') programs in $DIR/bin ($(grep -m1 -oE 'v[0-9]+\.[0-9]+' "$DIR/0_README.txt" || echo 'version unknown'))"
done
if [ ${#TARBALLS[@]} -gt 1 ]; then
  echo "OpenTaxSolver: more than one package is extracted; the adapter uses the newest by name. Remove the one not wanted."
fi
