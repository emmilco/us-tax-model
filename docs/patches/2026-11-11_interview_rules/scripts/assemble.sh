#!/bin/bash
cd /tmp/f1095a/out
scripts=/tmp/f1095a/scripts
(cd /tmp/f1095a && $scripts/mk_summary.sh > /dev/null 2>&1; python3 -I $scripts/gen_rank.py > out/catalog_rank.md 2>/dev/null)
{ cat part_summary.md; echo; cat part_method.md; echo; cat part_tables_intro.md; cat catalog_tables.md; cat part_tables_after.md; echo; cat part_families_intro.md; cat catalog_families.md; cat part_rank_intro.md; cat catalog_rank.md | grep -v "^Unattributed\|^No cause line"; cat part_rank_after.md; echo; cat part_check.md; echo; cat part_end.md; } > /tmp/f1095a/catalog.md
wc -l -c /tmp/f1095a/catalog.md
