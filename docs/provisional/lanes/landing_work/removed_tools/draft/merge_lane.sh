#!/bin/bash
# merge a lane into the provisional branch: generated files take the lane's side (regenerated later); fixture JSON and the
# question bank are merged structurally; anything else left in conflict stops the merge for a hand resolution
cd "$(dirname "$0")/../.." || exit 2
git merge -q --no-edit "$1" >/dev/null 2>&1
bad=0
for f in $(git diff --name-only --diff-filter=U); do
  case "$f" in
    reports/*|rendered/*|docs/provisional/walks/after/*) git checkout --theirs -- "$f" 2>/dev/null && git add -- "$f" ;;
    *.json|interview/2025/questions.yaml) python3 tools/draft/merge3.py "$f" && git add -- "$f" || bad=1 ;;
    interview/2025/personas/*|interview/2025/stage4.yaml|interview/2025/sales.yaml|interview/2025/social-security.yaml) python3 tools/draft/union.py "$f" && git add -- "$f"; echo "UNIONED (check): $f" ;;
    *) echo "TEXT CONFLICT: $f"; bad=1 ;;
  esac
done
if [ "$bad" = 1 ]; then echo "CONFLICTS in $1 (merge left open)"; git diff --name-only --diff-filter=U; exit 1; fi
if git diff --cached --quiet && [ ! -f .git/MERGE_HEAD ]; then echo "$1: already merged: $(git log --oneline -1)"; exit 0; fi
git commit -q --no-edit && echo "$1 merged: $(git log --oneline -1)"
