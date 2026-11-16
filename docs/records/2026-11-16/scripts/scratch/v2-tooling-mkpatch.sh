#!/bin/bash
# usage: v2-tooling-mkpatch.sh N  (scratch dir v2-tooling-N -> patches/v2/tooling-N.patch)
cd /tmp/nightplan/scratch/v2-tooling-$1 || exit 1
git diff --no-index a b | sed -e 's#^diff --git a/[ab]/\(.*\) b/b/\(.*\)$#diff --git a/\1 b/\2#' -e 's#^--- a/a/#--- a/#' -e 's#^+++ b/b/#+++ b/#' > /tmp/nightplan/patches/v2/tooling-$1.patch
grep -c '^diff --git' /tmp/nightplan/patches/v2/tooling-$1.patch
cd /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint && git apply --check /tmp/nightplan/patches/v2/tooling-$1.patch && echo "tooling-$1 APPLIES"
