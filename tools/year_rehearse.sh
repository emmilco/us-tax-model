#!/usr/bin/env bash
# year_rehearse.sh: rehearse a year's adoption on the documents archived today (drafts included), in a scratch
# copy of this tree outside the repository, and report each step. Nothing in the repository is written.
#
#     tools/year_rehearse.sh [--from 2025] [--to 2026] [--dest /tmp/year-rehearse-2026] [--origin DIR] [--force]
#                            [--reuse-build] [--stand-in-sources]
#
# The copy is DEST/tree (rsync of this tree without .git, the engine stores, the extraction and human review
# stores, lean/.lake and .claude); logs are DEST/out/NN_<step>.log, one line per step in DEST/out/summary.tsv
# (step, exit status, seconds). --origin is the from-year tree whose reviews the carry reads (default: the copy
# itself, whose from-year reviews are this tree's). --force replaces an existing DEST. --reuse-build refreshes an
# existing DEST/tree from this tree but keeps its canonical/ and skips the from-year build (a build can take an hour
# on a loaded machine); use it only when the from-year definitions have not changed since that build.
#
# --stand-in-sources: a to-year build that fails only because cited documents are not yet in the to-year archive
# (unpublished, or not refetched) is retried with each such document's from-year edition copied into the copy's
# sources/<to>/ (sources_standin; the manifest entry marked stand_in). The steps after the build then measure the
# carry and the review estimate as if those documents were unchanged: a lower bound for the forms that cite them.
#
# In the copy, in order (a step whose prerequisite failed is skipped and said so):
#   compile; build the from-year;
#   year_diff.py --adopt (copies the definitions, carries the review files, relocates, applies changes/<to>/,
#     writes the year-literal list and the shared-refs report);
#   stage research/ty<to>/params-<to>.proposed.yaml as params/<to>.yaml, in the params/<from>.yaml format: staged
#     values (source final, draft, derived) replace the adopted ones with their cites, new parameters are added,
#     a parameter with no to-year value (source none) keeps the adopted from-year value, the `retired` list is
#     removed, and every enum of `enums.changed` takes its staged values and cite; then
#     research/ty<to>/tables-<to>/*.yaml over tables/<to>/;
#   citations.py --strict; build the to-year, rebuild the from-year (build_fresh compares every year), render;
#   fixtures_year.py --no-hand-work (no class M model calls); test-fixtures;
#   year_carry.py without --write, then with --write; review_store.py check; check_logs.py;
#   rerun_all.py --dry-run (the review estimate; no model call: the forms with a to-year log, and those a year carry
#     left with none, reviewed whole);
#   a digest of the reports adoption writes (year literals by class, shared refs, relocation, fixtures).
set -u

FROM=2025; TO=2026; DEST=""; ORIGIN=""; FORCE=0; REUSE=0; STANDIN_SOURCES=0
while [ $# -gt 0 ]; do
  case "$1" in
    --from) FROM="$2"; shift 2 ;;
    --to) TO="$2"; shift 2 ;;
    --dest) DEST="$2"; shift 2 ;;
    --origin) ORIGIN="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --reuse-build) REUSE=1; shift ;;
    --stand-in-sources) STANDIN_SOURCES=1; shift ;;
    -h|--help) sed -n '2,34p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "year_rehearse.sh: unknown argument $1" >&2; exit 2 ;;
  esac
done
case "$FROM$TO" in *[!0-9]*) echo "year_rehearse.sh: --from and --to take four-digit years" >&2; exit 2 ;; esac
[ ${#FROM} -eq 4 ] && [ ${#TO} -eq 4 ] || { echo "year_rehearse.sh: --from and --to take four-digit years" >&2; exit 2; }

SRC=$(cd "$(dirname "$0")/.." && pwd -P)
# The copy lies outside the repository, where pyenv would choose another Python: pin the one this tree runs.
if [ -z "${PYENV_VERSION:-}" ] && command -v pyenv > /dev/null 2>&1; then
  PYENV_VERSION=$(cd "$SRC" && pyenv version-name 2>/dev/null) && export PYENV_VERSION
fi
(cd "$SRC" && python3 -c 'import yaml') 2>/dev/null || { echo "year_rehearse.sh: python3 in $SRC cannot import yaml" >&2; exit 2; }
(cd /tmp && python3 -c 'import yaml') 2>/dev/null || { echo "year_rehearse.sh: python3 outside the repository cannot import yaml (set PYENV_VERSION)" >&2; exit 2; }
[ -n "$DEST" ] || DEST="/tmp/year-rehearse-$TO"
mkdir -p "$(dirname "$DEST")"
DEST="$(cd "$(dirname "$DEST")" && pwd -P)/$(basename "$DEST")"
case "$DEST/" in
  "$SRC"/*) echo "year_rehearse.sh: --dest $DEST is inside the repository ($SRC); the copy must be outside it" >&2; exit 2 ;;
esac
TOP=$(git -C "$SRC" rev-parse --path-format=absolute --git-common-dir 2>/dev/null | sed 's#/\.git$##')
if [ -n "$TOP" ]; then
  case "$DEST/" in "$TOP"/*) echo "year_rehearse.sh: --dest $DEST is inside the repository ($TOP)" >&2; exit 2 ;; esac
fi
# One run per DEST: a second run would rsync over the tree the first is building in.
LOCK="$DEST.lock"
if ! mkdir "$LOCK" 2> /dev/null; then
  echo "year_rehearse.sh: another run holds $LOCK (pid $(cat "$LOCK/pid" 2>/dev/null)); remove it if that run is gone" >&2; exit 2
fi
echo $$ > "$LOCK/pid"
trap 'rm -rf "$LOCK"' EXIT
if [ $REUSE -eq 1 ]; then
  [ -e "$DEST/.year-rehearse" ] && [ -d "$DEST/tree/canonical/$FROM" ] \
    || { echo "year_rehearse.sh: --reuse-build needs a DEST made by this script with tree/canonical/$FROM" >&2; exit 2; }
  rm -rf "$DEST/out"
elif [ -e "$DEST" ]; then
  [ $FORCE -eq 1 ] || { echo "year_rehearse.sh: $DEST exists; pass --force to replace it" >&2; exit 2; }
  [ -e "$DEST/.year-rehearse" ] || { echo "year_rehearse.sh: $DEST was not made by this script; not removing it" >&2; exit 2; }
  rm -rf "$DEST"
fi
STAGED_PARAMS="research/ty$TO/params-$TO.proposed.yaml"
STAGED_TABLES="research/ty$TO/tables-$TO"
TREE="$DEST/tree"; OUT="$DEST/out"
mkdir -p "$TREE" "$OUT"
touch "$DEST/.year-rehearse"
printf 'step\trc\tseconds\n' > "$OUT/summary.tsv"

n=0
FAILED=" "
# run NAME NEEDS CMD...: run CMD in the copy, logging to OUT; NEEDS is a comma list of steps that must have passed.
run() {
  local name="$1" needs="$2"; shift 2; n=$((n + 1))
  local log; log="$OUT/$(printf %02d $n)_$name.log"
  local need
  for need in $(echo "$needs" | tr ',' ' '); do
    case "$FAILED" in *" $need "*)
      echo "skipped: $need failed" > "$log"; FAILED="$FAILED$name "
      printf '%s\tskipped\t0\n' "$name" >> "$OUT/summary.tsv"
      echo "[$n] skipped $name (needs $need)"; return 0 ;;
    esac
  done
  local t0; t0=$(date +%s)
  ( cd "$TREE" && "$@" ) > "$log" 2>&1
  local rc=$?
  local dt=$(( $(date +%s) - t0 ))
  [ $rc -eq 0 ] || FAILED="$FAILED$name "
  printf '%s\t%s\t%s\n' "$name" "$rc" "$dt" >> "$OUT/summary.tsv"
  echo "[$n] rc=$rc ${dt}s $name: $(grep -v '^[[:space:]]*$' "$log" | tail -2 | tr '\n' '|' | cut -c1-300)"
}

echo "year_rehearse: $FROM -> $TO; copy $TREE; logs $OUT"
t0=$(date +%s)
KEEP=""; [ $REUSE -eq 1 ] && KEEP="--exclude /canonical"
rsync -a --delete $KEEP --exclude '/.git' --exclude '/.engines' --exclude '/.direct-file' --exclude '/.extraction-review' \
  --exclude '/.human-review' --exclude '/lean/.lake' --exclude '/.claude' "$SRC/" "$TREE/" > "$OUT/00_copy.log" 2>&1 \
  || { echo "year_rehearse.sh: the copy failed (see $OUT/00_copy.log)" >&2; exit 1; }
echo "[0] copied in $(( $(date +%s) - t0 ))s"
[ -n "$ORIGIN" ] || ORIGIN="$TREE"
[ $REUSE -eq 0 ] || rm -rf "$TREE/canonical/$TO" "$TREE/rendered/$TO"
for p in "forms/$TO" "tables/$TO" "params/$TO.yaml" "fixtures/$TO"; do
  [ ! -e "$TREE/$p" ] || { echo "year_rehearse.sh: $p already exists in this tree: nothing to rehearse" >&2; exit 2; }
done
for p in "$STAGED_PARAMS" "$STAGED_TABLES"; do
  [ -e "$TREE/$p" ] || echo "year_rehearse: no $p: that staging step will fail"
done

# The staging of the proposed parameters, written for this run (the copy's own python, read-only on the repository).
cat > "$DEST/stage_params.py" <<'PY'
"""Stage a proposed parameters file (research/ty<to>/params-<to>.proposed.yaml) as params/<to>.yaml."""
import sys
import yaml

target, staged_path = sys.argv[1], sys.argv[2]
doc = yaml.safe_load(open(target, encoding="utf-8"))
P = doc["params"]
S = yaml.safe_load(open(staged_path, encoding="utf-8"))["params"]
if S.get("tax_year") != P.get("tax_year"):
    sys.exit(f"stage: the staged file is for {S.get('tax_year')}, the adopted parameters for {P.get('tax_year')}")
vals, problems, counts = P["values"], [], {}
bump = lambda k: counts.__setitem__(k, counts.get(k, 0) + 1)
for name in S.get("retired") or {}:
    if name in vals:
        del vals[name]
        bump("retired: removed")
    else:
        problems.append(f"retired {name} is not an adopted parameter")
kept = []
for name, e in (S.get("values") or {}).items():
    src = e.get("source")
    if src == "none" or e.get("value") is None:
        if name in vals:
            kept.append(name)
            bump("no to-year value: the adopted from-year value kept")
        else:
            problems.append(f"{name}: no to-year value and no adopted value")
        continue
    new = {k: e[k] for k in ("type", "value", "cite", "moves_with_year") if k in e}
    if name in vals:
        old = vals[name]
        if old.get("type") != new.get("type"):
            problems.append(f"{name}: type {old.get('type')} adopted, {new.get('type')} staged")
        new.setdefault("cite", old.get("cite"))
        bump(f"source {src}: " + ("value unchanged" if old.get("value") == new.get("value") else "value changed"))
    else:
        bump(f"source {src}: new parameter")
        if "cite" not in new:
            problems.append(f"{name}: a new parameter with no cite")
    vals[name] = new
missing = [n for n in vals if n not in (S.get("values") or {})]
for n in missing:
    problems.append(f"{n}: adopted, neither staged nor retired (kept)")
for name, e in ((S.get("enums") or {}).get("changed") or {}).items():
    old = P["enums"].get(name)
    new = dict(old or {})
    new["values"] = e["values"]
    if "cite" in e:
        new["cite"] = e["cite"]
    if old is None:
        bump("enums: added")
    elif old.get("values") != e["values"]:
        gone = [v for v in old["values"] if v not in e["values"]]
        added = [v for v in e["values"] if v not in old["values"]]
        print(f"stage: enum {name}: + {added} - {gone}")
        bump("enums: values changed")
    else:
        bump("enums: values unchanged (cite restated)")
    P["enums"][name] = new
P["tax_year"] = S["tax_year"]
with open(target, "w", encoding="utf-8") as fh:
    fh.write(f"# Staged by tools/year_rehearse.sh from {staged_path} (a rehearsal copy; not adopted).\n")
    yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True, width=120)
for k in sorted(counts):
    print(f"stage: {counts[k]:4d} {k}")
print(f"stage: kept from {P['tax_year'] - 1} (no to-year source): {', '.join(kept)}")
for p in problems:
    print(f"stage: PROBLEM {p}")
sys.exit(1 if problems else 0)
PY

# sources_standin LOG: the from-year edition of every document LOG says is missing from sources/<to>/.
sources_standin() {
  python3 - "$FROM" "$TO" "$1" <<'PY'
import json, re, shutil, sys
from pathlib import Path
f, t, log = sys.argv[1:4]
missing = sorted(set(re.findall(rf"cite doc '([^']+)' not in sources/{t}/manifest.json", open(log).read())))
mf, mt = Path("sources", f, "manifest.json"), Path("sources", t, "manifest.json")
old = {d["id"]: d for d in json.loads(mf.read_text())["documents"]}
new = json.loads(mt.read_text())
nxt = {d["id"]: d.get("next") for d in json.loads(Path("tools", "sources", f"{f}.json").read_text()) if d.get("next")}
done, absent = [], []
for doc in missing:
    d = old.get(doc)
    if d is None:
        absent.append(doc); continue
    for k, v in d.items():
        if (k == "file" or k.endswith("_file")) and isinstance(v, str) and (Path("sources", f) / v).exists():
            shutil.copyfile(Path("sources", f) / v, Path("sources", t) / v)
    e = dict(d); e["stand_in"] = f"the {f} edition, copied by tools/year_rehearse.sh (not archived for {t})"
    new["documents"].append(e)
    done.append(doc + (f" (its {f} catalog names the successor {nxt[doc]})" if doc in nxt else ""))
mt.write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n")
print(f"stand-in: {len(done)} document(s) copied from sources/{f}: " + ", ".join(done))
if absent:
    print(f"stand-in: not in sources/{f} either: {', '.join(absent)}")
PY
}

stage_tables() {
  local f n=0
  for f in "$STAGED_TABLES"/*.yaml; do
    [ -e "$f" ] || { echo "no staged tables in $STAGED_TABLES"; return 1; }
    if [ -e "tables/$TO/$(basename "$f")" ]; then echo "replaced tables/$TO/$(basename "$f")"; else echo "added tables/$TO/$(basename "$f")"; fi
    cp "$f" "tables/$TO/$(basename "$f")"; n=$((n + 1))
  done
  echo "staged $n table(s) from $STAGED_TABLES"
}

digest() {
  python3 - "$FROM" "$TO" <<'PY'
import collections, json, sys
from pathlib import Path
f, t = sys.argv[1], sys.argv[2]
r = Path("reports") / t
lit = r / f"year_literals_from_{f}.json"
if lit.exists():
    recs = json.loads(lit.read_text())
    by = collections.Counter(c for x in recs for c in x.get("classes", []))
    print(f"year literals: {len(recs)} lines; " + ", ".join(f"{c} {k}" for c, k in by.most_common()))
    files = collections.Counter(x["file"].split("/")[0] + "/" + x["file"].split("/")[1] if "/" in x["file"] else x["file"] for x in recs)
    print("  by directory: " + ", ".join(f"{d} {k}" for d, k in files.most_common()))
    print(f"  with a moved candidate: {sum(1 for x in recs if x.get('moved'))}")
else:
    print(f"year literals: no {lit}")
sr = r / f"shared_refs_from_{f}.json"
if sr.exists():
    refs = json.loads(sr.read_text())
    refs = refs if isinstance(refs, list) else refs.get("references", refs)
    by_file = collections.Counter(x.get("file") for x in refs) if isinstance(refs, list) else {}
    by_kind = collections.Counter(x.get("kind") or x.get("strength") for x in refs) if isinstance(refs, list) else {}
    print(f"shared refs: {len(refs)}; by kind " + ", ".join(f"{k} {v}" for k, v in by_kind.items()))
    for fl, k in sorted(by_file.items(), key=lambda kv: -kv[1]):
        print(f"  {k:5d} {fl}")
else:
    print(f"shared refs: no {sr}")
for name in (f"relocation_from_{f}.md", f"fixtures_from_{f}.md", f"year_diff_from_{f}.md"):
    p = r / name
    if p.exists():
        head = [l for l in p.read_text().splitlines() if l.strip()][:12]
        print(f"--- {p}"); print("\n".join(head))
    else:
        print(f"--- no {p}")
PY
}

run compile "" npm run compile --silent
if [ $REUSE -eq 1 ]; then
  n=$((n + 1)); printf '%s\treused\t0\n' build_from >> "$OUT/summary.tsv"; echo "[$n] reused canonical/$FROM (--reuse-build)"
else
  run build_from compile node engine/dist/main.js build --year "$FROM"
fi
run adopt build_from python3 tools/year_diff.py --from "$FROM" --to "$TO" --adopt
run stage_params adopt python3 "$DEST/stage_params.py" "params/$TO.yaml" "$STAGED_PARAMS"
run stage_tables adopt stage_tables
run citations adopt python3 tools/citations.py --strict --year "$TO"
run build_to adopt node engine/dist/main.js build --year "$TO"
case "$FAILED" in *" build_to "*)
  BUILD_LOG=$(ls "$OUT"/*_build_to.log)
  if [ $STANDIN_SOURCES -eq 1 ] && grep -q "not in sources/$TO/manifest.json" "$BUILD_LOG"; then
    run sources_standin "" sources_standin "$BUILD_LOG"
    run build_to_standin adopt node engine/dist/main.js build --year "$TO"
    case "$FAILED" in *" build_to_standin "*) ;; *) FAILED=$(echo "$FAILED" | sed 's/ build_to / /') ;; esac
  fi ;;
esac
run rebuild_from compile node engine/dist/main.js build --year "$FROM"
run render_to build_to node engine/dist/main.js render --year "$TO"
run fixtures_year build_to python3 tools/fixtures_year.py --from "$FROM" --to "$TO" --no-hand-work
run test_fixtures fixtures_year node engine/dist/main.js test-fixtures --year "$TO"
run carry_dry build_to python3 tools/transcription/year_carry.py --year "$TO" --from "$ORIGIN" --report "$OUT/carry_dry.md" --verbose
run carry_write carry_dry python3 tools/transcription/year_carry.py --year "$TO" --from "$ORIGIN" --report "$OUT/carry_write.md" --verbose --write
run review_store carry_write python3 tools/transcription/review_store.py check --year "$TO"
run check_logs carry_write python3 tools/transcription/check_logs.py --year "$TO"
run rerun_estimate render_to,carry_write python3 tools/transcription/rerun_all.py --year "$TO" --dry-run --summary "$OUT/rerun_estimate.json"
run reports adopt digest

echo "year_rehearse: done; failed or skipped:${FAILED% }"
echo "summary: $OUT/summary.tsv"
case "$FAILED" in " ") exit 0 ;; *) exit 1 ;; esac
