#!/usr/bin/env python3
"""Rulings on review disagreements, kept as data beside each log.

Each review log (`reviews/<year>/<kind>/<form>.md`, or `<form>.<family>.md` for a
model family other than Claude: families.py) is rendered by its tool; the rulings a
person wrote on its disagreements live in `<form>.rulings.json` (`<form>.<family>.rulings.json`) next
to it, keyed by the disagreement they answer (the printed line and the two sides
of the disagreement; a transcription expression is stored as the sha256 of its text, stored_key),
with a context hash covering the reviewed subject, prompts and source excerpts. Only an unchanged
disagreement in the same recorded context can reuse a ruling. An entry also records the line's
cross-document subject and, for transcription, a compact stamp of the triage it relied on (EXTRA).
`rule.py` writes both files; `check_logs.py` fails when a log's rulings and its sidecar disagree.

    rulings.py --migrate     # build every sidecar from the rulings already in the logs
    rulings.py --check       # report log/sidecar disagreements (exit 1 on any)
    rulings.py --prune       # drop sidecar entries whose disagreement no longer occurs
    rulings.py --compact [--triage-dir DIR]   # rewrite every sidecar in the stored form
"""
import argparse, hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: reviews/ny/<year>/)
REVIEWS = str(jurisdiction.ypath("reviews", Y))
KINDS = {
    "transcription": ("printed", "project", "second"),
    "render": ("printed", "restated", "model"),
    "classm": ("case", "printed", "project", "model"),
}
OPEN = "Ruling: open"
DROPPED = " [dropped]"
# Stamps a sidecar entry carries when rule.py writes it: the date it was ruled, the reply it rules
# (`run`: transcribe.response_sha256 of the reply, as the cost ledger records the call that returned
# it) and, for a finding, its severity. Entries written before stamping have none of them; a stamp
# is never inferred for them.
STAMPS = ("date", "run", "severity")
SEVERITIES = ("high", "medium", "low")


def sidecar_path(kind, form, family=families.DEFAULT):
    return os.path.join(REVIEWS, kind, families.stem(form, family) + ".rulings.json")


def log_path(kind, form, family=families.DEFAULT):
    """Where a form's log is written as a readable view (review_store.view_path): generated from the
    committed index and records, never read back as the record. Read a log with read_log."""
    import review_store
    return review_store.view_path(kind, form, family)


def read_log(kind, form, family=families.DEFAULT):
    """A form's review log, as review_store assembles it from its index and records; None when the form
    has no index. A log file at log_path is read only outside the generated views (a test's own log)."""
    import review_store
    text = review_store.view(kind, form, family)
    if text is not None:
        return text
    path = log_path(kind, form, family)
    if review_store.is_view(path) or not os.path.exists(path):
        return None
    return open(path, encoding="utf-8").read()


def has_log(kind, form, family=families.DEFAULT):
    import review_store
    if os.path.exists(review_store.index_path(kind, form, family)):
        return True
    path = log_path(kind, form, family)
    return not review_store.is_view(path) and os.path.exists(path)


STORE_ELSEWHERE = False  # store logs as records even in a reviews directory outside the repository's (tests)


def write_log(kind, form, text, family=families.DEFAULT):
    """Store a log a review tool wrote (review_store.ingest) and refresh its readable view; returns the
    view's path."""
    import review_store
    path = log_path(kind, form, family)
    if review_store.is_view(path) or STORE_ELSEWHERE or os.path.exists(review_store.index_path(kind, form, family)):
        review_store.ingest(kind, form, family, text)
    # else: a reviews directory outside the repository's (a test's) keeps plain log files
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


# A transcription disagreement is keyed by its printed line and both expression texts. The sidecar
# stores each expression as the sha256 of its exact text as the log section embeds it (stored_key),
# not the text: the expressions are in the review record, and a section and its entry still match
# exactly. Render and class M sides are short and kept as text.
HASHED = {"transcription": (("project", "project_expr_sha256"), ("second", "second_expr_sha256"))}
# What an entry records besides its key, ruling, drop flag, context and stamps: the line's
# cross-document subject when it was ruled (`subject_key`: carry.line_subject), and for transcription
# the executable triage the ruling relied on (`triage`: triage_stamp), when a triage record existed.
EXTRA = ("subject_key", "triage")


def _sha_text(text):
    return hashlib.sha256(str(text).encode()).hexdigest()


def stored_key(kind, key):
    """The sidecar key of a disagreement keyed as its log section reads it (section_key)."""
    if kind not in HASHED:
        return tuple(key)
    return (key[0], *(_sha_text(x) for x in key[1:]))


def stored_fields(kind):
    """The sidecar row fields that hold the key, in key order."""
    hashed = dict(HASHED.get(kind, ()))
    return tuple(hashed.get(f, f) for f in KINDS[kind])


def compact_row(kind, row):
    """A sidecar row in the stored form: a row that still embeds expressions (as in revisions written
    before they were hashed) has them replaced by their hashes; any other row is returned as is."""
    out = dict(row)
    for field, hashed in HASHED.get(kind, ()):
        if field in out:
            out[hashed] = _sha_text(out.pop(field))
    return out


def load(kind, form, family=families.DEFAULT):
    """{stored key tuple: {"ruling": text without the dropped suffix, "drop": bool, ...}}."""
    path = sidecar_path(kind, form, family)
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding="utf-8"))
    fields = stored_fields(kind)
    out = {}
    for r in data["rulings"]:
        r = compact_row(kind, r)
        out[tuple(r[f] for f in fields)] = {"ruling": r["ruling"], "drop": bool(r.get("drop")),
                                            **({"context": r["context"]} if r.get("context") else {}),
                                            **{s: r[s] for s in STAMPS + EXTRA if r.get(s)}}
    return out


def save(kind, form, rulings, family=families.DEFAULT):
    """Write a sidecar; `rulings` is keyed by stored keys (stored_key)."""
    fields = stored_fields(kind)
    rows = []
    for key in sorted(rulings, key=lambda k: tuple(str(x) for x in k)):
        row = dict(zip(fields, key))
        row["ruling"] = rulings[key]["ruling"]
        if rulings[key].get("drop"):
            row["drop"] = True
        if rulings[key].get("context"):
            row["context"] = rulings[key]["context"]
        for s in STAMPS + EXTRA:
            if rulings[key].get(s):
                row[s] = rulings[key][s]
        rows.append(row)
    path = sidecar_path(kind, form, family)
    head = {"kind": kind, "form": form}
    if family != families.DEFAULT:
        head["family"] = family
    with open(path, "w", encoding="utf-8") as f:
        json.dump({**head, "rulings": rows}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


def witness_id(w):
    """A triage witness's input by name: a fixture case, a generated return (seed.index) or a partial
    record (its base case and the withheld answer), with the instance the line was read in."""
    s = w.get("source") or {}
    kind = s.get("kind")
    name = (s.get("id") if kind == "fixture" else f"{s.get('seed')}.{s.get('index')}" if kind == "generated"
            else f"{s.get('base')}-{s.get('withheld')}" if kind == "partial" else json.dumps(s, sort_keys=True))
    return f"{kind}:{name}@{w.get('instance')}"


def triage_stamp(record, line):
    """The compact stamp of the triage line a ruling relied on: its verdict, the kinds of difference
    found (names only), the ids of its witnesses and the triage policy."""
    return {"verdict": line["triage"], "kinds": sorted(line.get("kinds") or {}),
            "witnesses": [witness_id(w) for w in line.get("witnesses") or []], "policy": record.get("policy")}


# Triage records (triage.py) are regenerated on demand into git-ignored review data, by jurisdiction and year.
TRIAGE_DIR = os.path.join(ROOT, ".transcription", "triage", os.path.relpath(REVIEWS, os.path.join(ROOT, "reviews")))


def triage_path(form, family=families.DEFAULT):
    return os.path.join(TRIAGE_DIR, families.stem(form, family) + ".json")


def triage_line(record, handle, run):
    """The line of a triage record that evaluated section `handle` against the reply `run`
    (transcribe.response_sha256), else None."""
    for line in record.get("lines", []):
        if line.get("handle") != handle:
            continue
        pid = line.get("pass")
        reply = (record.get("passes") or {}).get(pid, {}).get("response_sha256") if pid else record.get("response_sha256")
        if run and reply == run:
            return line
    return None


def triage_for(kind, form, family, handle, run, path=None):
    """The triage stamp for a ruling on section `handle` of reply `run`: from the form's triage record when
    one exists and evaluated that very reply, else None."""
    if kind != "transcription":
        return None
    path = path or triage_path(form, family)
    if not os.path.exists(path):
        return None
    record = json.load(open(path, encoding="utf-8"))
    line = triage_line(record, handle, run)
    return triage_stamp(record, line) if line else None


def review_context(kind, text):
    """Bind a ruling to what was reviewed, including input wording carried by the prompt.

    Exclude dates and outcome counts. Class M records its prompts on case headings;
    the other writers record one prompt in the header. Legacy rulings without a
    context remain historical records, but are never automatically reused.
    """
    head = text.partition("\n## Lines\n")[0]
    names = ("subject sha256", "prompt sha256", "prompt policy", "system sha256",
             "model requested", "reasoning effort", "output token budget")
    fields = {name: (re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", head, re.M) or [None, ""])[1]
              for name in names}
    comparison = re.search(r"^\| comparison policy \| (.*?) \|$", head, re.M)
    if kind == "transcription" and comparison:
        fields["comparison policy"] = comparison.group(1)
        for name in ("type validation policy", "model type validation", "input context policy", "complete input context",
                     "required input context sha256",
                     "review provenance", "parent review log sha256", "original review date",
                     "original comparison policy", "original type validation policy", "original input context policy",
                     "partial-input policy", "partial-input bank sha256", "partial-input request context", "partial-input result"):
            match = re.search(rf"^\| {name} \| (.*?) \|$", head, re.M)
            if match:
                fields[name] = match.group(1)
    if kind == "classm":
        scope = re.search(r"^\| worked target scope \| (.*?) \|$", head, re.M)
        if scope:
            fields['worked target scope'] = scope.group(1)
    sources = re.findall(r"^\| \S+ \| [^|]* \| [^|]* \| [^|]* \| [0-9a-f]{64} \|[^\n]*$", head, re.M)
    cases = sorted(re.findall(r"^### case (\S+) — prompt sha256 ([0-9a-f]{64});", text, re.M)) if kind == "classm" else []
    return hashlib.sha256(json.dumps({"kind": kind, "fields": fields, "sources": sorted(sources),
                                     "case_prompts": cases}, sort_keys=True).encode()).hexdigest()


PASS_TAG = re.compile(r"^Reviewed in: pass ([0-9a-f]{12})$", re.M)


def pass_blocks(text):
    """{pass id: record} of the line-scoped reviews a transcription or render log holds."""
    _, sep, tail = text.partition("\n## Line-scoped reviews\n")
    if not sep:
        return {}
    tail = tail.split("\n## Raw ", 1)[0]
    return {part.partition("\n")[0].strip(): "#### Pass " + part for part in tail.split("\n#### Pass ")[1:]}


def section_context(kind, text, content, blocks=None):
    """The review context of one section of a log: that of the line-scoped review whose pass the
    section names ("Reviewed in: pass <id>"), else that of the review recorded in the log's header.
    A section naming a pass the log does not hold has no context (None)."""
    tag = PASS_TAG.search(content.split("\n## ", 1)[0])
    if not tag:
        return review_context(kind, text)
    blocks = pass_blocks(text) if blocks is None else blocks
    return review_context(kind, blocks[tag.group(1)]) if tag.group(1) in blocks else None


RAW_HEADINGS = {"transcription": "Raw second transcription", "render": "Raw response"}


def _fenced(text, start):
    """The reply a log embeds after `start` ("```yaml" fence), to the last closing fence of `text`."""
    at = text.find(start)
    if at < 0:
        return None
    body = text[at + len(start):]
    end = body.rfind("\n```")
    return body[:end] if end >= 0 else None


def section_reply(kind, text, title, content, blocks=None):
    """The reply (stripped, as embedded) whose verdict a section of a log records, else None: the
    raw reply of the line-scoped pass the section names, of the review in the log's header, or for
    class M of the section's case."""
    if kind == "classm":
        case = title.split(" — ")[0]
        _, sep, tail = text.partition("\n## Raw responses\n")
        if not sep:
            return None
        start = f"\n### {case}\n\n```yaml\n"
        at = tail.find(start)
        if at < 0:
            return None
        body = tail[at + len(start):]
        nxt = re.search(r"\n```\n\n### \S+\n\n```yaml\n", body)
        end = nxt.start() if nxt else body.rfind("\n```")
        return body[:end] if end >= 0 else None
    tag = PASS_TAG.search(content.split("\n## ", 1)[0])
    if tag:
        blocks = pass_blocks(text) if blocks is None else blocks
        block = blocks.get(tag.group(1))
        return _fenced(block, f"\n##### {RAW_HEADINGS[kind]}\n\n```yaml\n") if block else None
    _, sep, tail = text.partition(f"\n## {RAW_HEADINGS[kind]}\n")
    return _fenced("\n" + tail, "\n```yaml\n") if sep else None


def section_run(kind, text, title, content, blocks=None):
    """The run stamp of a section: the identity of the reply it records (transcribe.response_sha256),
    which the cost ledger records for the call that returned it; None when the log holds no reply."""
    reply = section_reply(kind, text, title, content, blocks)
    return hashlib.sha256(reply.strip().encode()).hexdigest() if reply is not None else None


def stamp_errors(row):
    """What is malformed in a sidecar entry's stamps (absent stamps are not errors)."""
    errs = []
    if row.get("date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(row["date"])):
        errs.append("date is not YYYY-MM-DD")
    if row.get("run") and not re.fullmatch(r"[0-9a-f]{64}", str(row["run"])):
        errs.append("run is not a sha256")
    if row.get("severity") and row["severity"] not in SEVERITIES:
        errs.append("severity is not one of " + ", ".join(SEVERITIES))
    return errs


def kept(kind, form, family=families.DEFAULT, *, context):
    """Only reuse rulings explicitly made in this review context; keyed by stored keys (stored_key)."""
    return {k: v["ruling"] + (DROPPED if v["drop"] else "") for k, v in load(kind, form, family).items()
            if v.get("context") == context}


def split_ruling(text):
    """A ruling line as printed -> (text without the dropped suffix, drop flag)."""
    text = text.strip()
    if text.endswith(DROPPED.strip()):
        return text[: -len(DROPPED.strip())].rstrip(), True
    return text, False


_SECTION = {
    "transcription": re.compile(r"^Status: \*\*(?:DISAGREE|MISSING)\*\*\n\nProject:\n\n```json\n(.*?)\n```\n\nSecond:\n\n```json\n(.*?)\n```(?:\n\nSecond transcription's note: [^\n]*)?\n\n(Ruling: [^\n]*)", re.S),
    "render": re.compile(r"^Status: \*\*(?:MISMATCH|UNCLEAR|MISSING)\*\*\n\nRestated: (.*?)\n\nModel: (.*?)\n\n(Ruling: [^\n]*)", re.S),
    "classm": re.compile(r"^Status: \*\*(?:DISAGREE|MISSING)\*\*\n\nProject: ([^\n]*)\nModel: ([^\n]*)\n(?:Work: [^\n]*\n)?\n(Ruling: [^\n]*)"),
}


def section_key(kind, title, content):
    """(key tuple, ruling line) for a disagreement section of a log, else None.
    `title` is the heading text after '### '; `content` the lines below it."""
    m = _SECTION[kind].match(content)
    if not m:
        return None
    if kind == "classm":
        parts = title.split(" — ")
        if len(parts) < 3:
            return None  # a case heading, not a line
        key = (parts[0], parts[1], m.group(1), m.group(2))
    else:
        key = (title.split(" — ")[0], m.group(1), m.group(2))
    return key, m.group(3).strip()


def log_sections(kind, text, with_content=False):
    """Every disagreement section of a log: [(key, ruling line)], or with `with_content`
    [(key, ruling line, section content)]."""
    _, _, rest = text.partition("\n## Lines\n")
    body, _, _ = rest.partition("\n## Raw ")
    out = []
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        found = section_key(kind, title, content)
        if found:
            out.append((*found, content) if with_content else found)
    return out


def forms_with_logs(kind):
    """[(form, family)] for every log of a kind, the Claude family first within a form."""
    d = os.path.join(REVIEWS, kind)
    if not os.path.isdir(d):
        return []
    stems = {f[:-len(".index.json")] for f in os.listdir(d) if f.endswith(".index.json")}
    stems |= {f[:-3] for f in os.listdir(d) if f.endswith(".md")}  # a test's own log files
    pairs = [families.split_stem(s) for s in stems]
    return sorted(pairs, key=lambda p: (p[0], p[1] != families.DEFAULT, p[1]))


def migrate():
    total = 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = read_log(kind, form, family)
            rulings = load(kind, form, family)
            for key, line in log_sections(kind, text):
                key = stored_key(kind, key)
                if line != OPEN:
                    t, drop = split_ruling(line)
                    # Migration copies historical rulings; it cannot establish that
                    # their rationale was adjudicated in the current context.
                    prior = rulings.get(key, {})
                    rulings[key] = {**prior, "ruling": t, "drop": drop}
            if rulings:
                save(kind, form, rulings, family); total += len(rulings)
    print(f"rulings: {total} written to sidecars")


def compact(triage_dir=None):
    """Rewrite every sidecar in the stored form (compact_row), adding to each entry without them the
    line's cross-document subject as it is now (carry.line_subject) and, for a live transcription entry,
    the stamp of the triage record in `triage_dir` that evaluated the reply its section records."""
    import carry
    snap = carry.Snapshot(None)
    stats = {"entries": 0, "subject_key": 0, "triage": 0}
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            if not os.path.exists(sidecar_path(kind, form, family)):
                continue
            text = read_log(kind, form, family)
            blocks = pass_blocks(text)
            live = {}
            for key, _, content in log_sections(kind, text, with_content=True):
                live[stored_key(kind, key)] = (key, content)
            side = load(kind, form, family)
            for skey, entry in side.items():
                stats["entries"] += 1
                if not entry.get("subject_key"):
                    subject = carry.line_subject(kind, snap, form, skey[1] if kind == "classm" else skey[0])
                    if subject:
                        entry["subject_key"] = subject
                if entry.get("subject_key"):
                    stats["subject_key"] += 1
                if kind == "transcription" and triage_dir and not entry.get("triage") and skey in live:
                    key, content = live[skey]
                    run = entry.get("run") or section_run(kind, text, key[0], content, blocks)
                    stamp = triage_for(kind, form, family, key[0], run,
                                       os.path.join(triage_dir, families.stem(form, family) + ".json"))
                    if stamp:
                        entry["triage"] = stamp
                if entry.get("triage"):
                    stats["triage"] += 1
            save(kind, form, side, family)
    print(f"rulings: {stats['entries']} entries in the stored form; {stats['subject_key']} with a subject key, "
          f"{stats['triage']} with a triage stamp")


def prune():
    """Drop sidecar entries whose disagreement no longer occurs in the log."""
    dropped = 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = read_log(kind, form, family)
            live = {stored_key(kind, key) for key, _ in log_sections(kind, text)}
            side = load(kind, form, family)
            kept = {k: v for k, v in side.items() if k in live}
            if len(kept) != len(side):
                dropped += len(side) - len(kept)
                if kept:
                    save(kind, form, kept, family)
                else:
                    os.remove(sidecar_path(kind, form, family))
    print(f"rulings: {dropped} stale sidecar entries pruned")


def check():
    """A log's non-open rulings must each equal the sidecar's; sidecar entries with no
    matching section are reported (a disagreement that no longer occurs) but pass."""
    problems, stale, total = [], 0, 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = read_log(kind, form, family)
            side = load(kind, form, family)
            seen = set()
            stem = families.stem(form, family)
            blocks = pass_blocks(text)
            for key, line, content in log_sections(kind, text, with_content=True):
                if line == OPEN:
                    continue
                key = stored_key(kind, key)
                total += 1; seen.add(key)
                t, drop = split_ruling(line)
                s = side.get(key)
                if s is None:
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} is in the log but not in {stem}.rulings.json")
                elif s["ruling"] != t or s["drop"] != drop:
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} differs between the log and {stem}.rulings.json")
                elif s.get("context") and s["context"] != section_context(kind, text, content, blocks):
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} belongs to a different review context")
            stale += sum(1 for k in side if k not in seen)
            for key, v in side.items():
                problems += [f"{kind}/{stem}: ruling on {key[:2]} in {stem}.rulings.json: {e}" for e in stamp_errors(v)]
    for p in problems:
        print(p, file=sys.stderr)
    print(f"rulings: {total} in logs, all in sidecars" if not problems else f"rulings: {len(problems)} log/sidecar disagreement(s)", f"({stale} sidecar entries without a current disagreement)" if stale else "")
    return 1 if problems else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--migrate", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--prune", action="store_true", help="drop sidecar entries whose disagreement no longer occurs")
    ap.add_argument("--compact", action="store_true", help="rewrite every sidecar in the stored form, with subject keys "
                    "and, from --triage-dir, triage stamps")
    ap.add_argument("--triage-dir", help="directory of triage records (<stem>.json) to stamp rulings from (--compact)")
    a = ap.parse_args()
    if a.migrate:
        migrate()
    if a.compact:
        compact(a.triage_dir)
    if a.prune:
        prune()
    if a.check:
        sys.exit(check())
    if not (a.migrate or a.check or a.prune or a.compact):
        ap.print_help()
