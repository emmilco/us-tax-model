#!/bin/bash
# usage: mkpatch.sh lane
cd /tmp/nightplan/scratch/$1 || exit 1
git diff --no-index a b | sed -e 's#^diff --git a/a/\(.*\) b/b/\(.*\)$#diff --git a/\1 b/\2#' -e 's#^--- a/a/#--- a/#' -e 's#^+++ b/b/#+++ b/#' > /tmp/nightplan/patches/$1.patch
grep -c '^diff --git' /tmp/nightplan/patches/$1.patch
