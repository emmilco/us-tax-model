#!/usr/bin/env python3
"""Carry review verdicts across a proven rename of line ids.

Given a rename map (a JSON object, old line id -> new line id; or {"renames": [{"old", "new"}, ...]}) and the
tree before the rename (--from: a commit, or a directory holding that tree), every review whose subject names a
renamed id is carried to the new names where the rename is proven to have changed nothing but the names, and
listed where it is not. A review unit is a compared line of a transcription or render log, the whole subject of a
log (class M has no other), a question, a screen, a gate (screen and false-no reviews) or a form's completeness
review. Run it from the renamed tree, after its build and rendering (it refuses a stale build).

The proof for a unit has two parts.

A. The subject its review recorded equals the subject the current tree gives once each new id is put back to its
   old id. The current tree is copied (copy-on-write) to a scratch tree; there every new id is replaced by its
   old id, as a whole id, in forms/, rendered/, canonical/, interview/ and ambiguities/ (also in the collection
   form `doc[entry].name`); and every subject is computed in both trees by the review tools' own code
   (subjects.py, question_review, screen_review, gates, completeness_review). So the review judged exactly what
   the tree holds now, but for the names.
B. For transcription, render and class M, the line's year-carry parts (year_carry.parts: its subject with the
   interfaces of the other documents' lines it names, the values of the parameters, enums and tables it reads,
   and the cited source text at anchor-section granularity) are equal at --from and in the scratch tree, and the
   review tools' policy versions at --from are the current ones. So nothing else the verdict rests on changed
   since --from.

A unit is considered only when the rename moves it: its subject differs between the two trees, or its key names
a renamed id. A unit whose proof fails is listed with the reason and nothing of it is carried; its review falls
due as before. The map is refused whole (exit 2, nothing written) when it is stale: an old id that is not a line
at --from or is still a line now, a new id that is a line at --from or is not one now, an id with no document
prefix, or two entries that share an id.

With --write, for each unit carried:
- a transcription or render index line gets the current subject (and foreign interfaces), `subject_key` and
  `carried` {"by": "rename", "map": {old: new, ...}, "from": <commit or tree>, "was": <the subject it was proven
  against>, "keys": {old key: new key} when its log key changed}; a changed key is shown from the record's
  section under the new key (review_store, `section`), and its rulings sidecar entries are re-keyed;
- the rest of a document is carried the same way (`rest_carried`); a whole-form subject (class M, or a log
  without line subjects) as `subject_carried` {"subject", "was", "carried"} (review_store.recorded_subject);
- a question, screen, gate or completeness record is re-keyed to the new id with the current `subject_sha` and
  `carried`; its per-sample rulings (`unruled:<unit>#<k>`) and baseline entries are re-keyed with the new
  `subject_sha`, each ruling marked `carried`; a completeness ruling's `line` and `gate` fields are renamed;
- a consumers.json ruling or baseline entry of a renamed input is re-keyed when the input's question (the
  subject check_consumers.py holds it to) is the same at --from and now.
The map entries a carried unit records are those whose new id its current subject names.

Records (reviews/store/), the verdict and ruling texts and the raw replies are never rewritten: they keep the old
names the reviewer saw.

    rename_carry.py --map MAP.json --from REV|DIR [--write] [--report PATH] [--keep DIR] [--jurisdiction ny]
    rename_carry.py --self-test
"""
import argparse, contextlib, hashlib, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402

KINDS = ("transcription", "render", "classm")
SAMPLED = ("questions", "screens", "false_no", "completeness")
# What the scratch tree holds (copy-on-write clones), and where the old names are put back.
COPY = ("forms", "rendered", "canonical", "params", "tables", "ambiguities", "schema", "interview", "sources", "tools",
        "reviews", "years.json")
RENAMED_IN = ("forms", "rendered", "canonical", "interview", "ambiguities")
TEXT = (".yaml", ".yml", ".json", ".md", ".txt")
ID = r"[A-Za-z0-9_]"


# ---------------------------------------------------------------- substitution

def substituter(mapping):
    """A function replacing each id of `mapping` by its value, as a whole id: not inside a longer id
    (`a.b_if_c`, `x.a.b`), but followed by a sentence's full stop; and in the collection form `doc[entry].name`."""
    if not mapping:
        return lambda text: text
    ids = sorted(mapping, key=len, reverse=True)
    whole = re.compile(r"(?<![A-Za-z0-9_.])(" + "|".join(map(re.escape, ids)) + r")(?!" + ID + r"|\." + ID + ")")
    local = {}
    for old, new in mapping.items():
        doc, _, name = old.partition(".")
        ndoc, _, nname = new.partition(".")
        if doc == ndoc:
            local[(doc, name)] = nname
    inst = re.compile(r"(?<![A-Za-z0-9_.])(" + ID + r"+)(\[[^\]\s]*\])\.(" + ID + r"+)(?!" + ID + ")")

    def sub(text):
        text = whole.sub(lambda m: mapping[m.group(1)], text)
        if local:
            text = inst.sub(lambda m: m.group(1) + m.group(2) + "." + local.get((m.group(1), m.group(3)), m.group(3)), text)
        return text
    return sub


# ---------------------------------------------------------------- the map

def load_map(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict) and "renames" in data:
        data = {r["old"]: r["new"] for r in data["renames"]}
    if not isinstance(data, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in data.items()):
        raise SystemExit(f"{path}: a rename map is a JSON object of old id -> new id")
    return data


def line_ids_at(root):
    """{line id: line} of the documents under a tree's forms/<year>/ and forms/ny/<year>/."""
    import yaml
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    out = {}
    for d in (os.path.join(root, "forms", str(Y)), os.path.join(root, "forms", "ny", str(Y))):
        for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if n.endswith(".yaml"):
                with open(os.path.join(d, n), encoding="utf-8") as f:
                    raw = yaml.load(f, Loader=loader) or {}
                doc = raw.get("form") or raw.get("def") or {}
                for l in doc.get("lines", []):
                    out.setdefault(l["id"], l)
    return out


def plan_consumers(plan, before, now):
    """[(old key, new key)] of reviews/<year>/consumers.json entries (`consumer:<input>@<doc>:p<page>`) whose input
    was renamed and whose question (the subject check_consumers.py holds them to) is the same at --from and now."""
    path = str(jurisdiction.ypath("reviews", Y, "consumers.json"))
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    question = lambda l: (l.get("expr") or {}).get("source", l.get("label", ""))
    out = []
    for k in sorted(set(data.get("rulings", {})) | set(data.get("baseline", {}))):
        iid, at, rest = k[len("consumer:"):].partition("@")
        if not k.startswith("consumer:") or iid not in plan.mapping or not at:
            continue
        new = plan.mapping[iid]
        if new in now and iid in before and question(now[new]) == question(before[iid]):
            out.append((k, f"consumer:{new}@{rest}"))
            plan.carry.append(("consumers", f"{k} -> consumer:{new}@{rest}", "the input's question is unchanged"))
        else:
            plan.refused.append(("consumers", k, "the input's question changed beyond its name"))
    return out


def write_consumers(moves, plan):
    if not moves:
        return []
    path = str(jurisdiction.ypath("reviews", Y, "consumers.json"))
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    to = dict(moves)
    marker = lambda k: {"by": "rename", "map": {k[len("consumer:"):].partition("@")[0]: to[k][len("consumer:"):].partition("@")[0]},
                        "from": plan.rev}
    data["rulings"] = {to.get(k, k): ({**r, "carried": marker(k)} if k in to and isinstance(r, dict) else r)
                       for k, r in data.get("rulings", {}).items()}
    if "baseline" in data:
        data["baseline"] = {to.get(k, k): v for k, v in data["baseline"].items()}
    _json_write(path, data)
    return [path]


def stale(mapping, before, now):
    """Why the map does not describe the rename from `before` ({id: doc} at --from) to `now`: [reason]."""
    out = []
    olds, news = list(mapping), list(mapping.values())
    for old, new in sorted(mapping.items()):
        if "." not in old or "." not in new:
            out.append(f"{old} -> {new}: an id with no document prefix (a definition's local id) is not carried")
        if old == new:
            out.append(f"{old} -> {new}: not a rename")
        if old not in before:
            out.append(f"{old} -> {new}: {old} is not a line at --from")
        if old in now:
            out.append(f"{old} -> {new}: {old} is still a line now")
        if new in before:
            out.append(f"{old} -> {new}: {new} was already a line at --from")
        if new not in now:
            out.append(f"{old} -> {new}: {new} is not a line now")
    dup = sorted({n for n in news if news.count(n) > 1})
    if dup:
        out.append("two old ids renamed to the same new id: " + ", ".join(dup))
    chain = sorted(set(olds) & set(news))
    if chain:
        out.append("ids both renamed and renamed to (apply chained renames one map at a time): " + ", ".join(chain))
    return out


# ---------------------------------------------------------------- the scratch tree

def _clone(src, dst):
    if not os.path.exists(src):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    r = subprocess.run(["cp", "-c", "-R", src, dst], capture_output=True, text=True)
    if r.returncode:
        if os.path.isdir(src):
            shutil.copytree(src, dst, symlinks=True)
        else:
            shutil.copy2(src, dst)


def scratch_tree(root, dest, mapping_back):
    """A copy of `root` under `dest` with each new id put back to its old id (mapping_back: new -> old)."""
    for name in COPY:
        _clone(os.path.join(root, name), os.path.join(dest, name))
    sub = substituter(mapping_back)
    changed = 0
    for top in RENAMED_IN:
        for d, _, files in os.walk(os.path.join(dest, top)):
            for n in files:
                if not n.endswith(TEXT):
                    continue
                p = os.path.join(d, n)
                with open(p, encoding="utf-8") as f:
                    text = f.read()
                new = sub(text)
                if new != text:
                    os.remove(p)  # a clone shares blocks with its source until written: write a new file
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(new)
                    changed += 1
    return changed


# ---------------------------------------------------------------- the subjects of one tree

class _Seen:
    """Records which of `ids` the data hashed with hashlib.sha256 names, while active."""

    def __init__(self, ids):
        self.ids, self.found, self._orig = set(ids), set(), None
        self.pat = re.compile(r"(?<![A-Za-z0-9_.])(" + "|".join(map(re.escape, sorted(self.ids, key=len, reverse=True)))
                              + r")(?!" + ID + r"|\." + ID + ")") if self.ids else None

    def scan(self, data):
        if self.pat is not None and data:
            text = data.decode("utf-8", "replace") if isinstance(data, (bytes, bytearray)) else str(data)
            self.found |= set(self.pat.findall(text))

    @contextlib.contextmanager
    def watching(self):
        orig, seen = hashlib.sha256, self

        class Hash:
            def __init__(self, data=b"", **kw):
                self._h = orig(data, **kw)
                seen.scan(data)

            def update(self, data):
                seen.scan(data)
                self._h.update(data)

            def hexdigest(self):
                return self._h.hexdigest()

            def digest(self):
                return self._h.digest()

        self.found = set()
        hashlib.sha256 = Hash
        try:
            yield self
        finally:
            hashlib.sha256 = orig


def dump(ids):
    """Every review unit's subject in this tree, and the ids of `ids` each names: {kind: {unit: {...}}}."""
    import subjects
    import transcribe as T
    forms_dir = str(jurisdiction.ypath("forms", Y))
    fids = sorted(n[:-5] for n in os.listdir(forms_dir) if n.endswith(".yaml"))
    seen = _Seen(ids)
    out = {k: {} for k in KINDS + ("questions", "gates", "screens", "completeness")}

    def watched(fn, *a):
        with seen.watching():
            value = fn(*a)
        return value, sorted(seen.found)

    index = subjects._all_lines(str(Y))
    for fid in fids:
        doc = T.load_form(fid)
        by_id = {l["id"]: l for l in doc["lines"]}
        keys = subjects.target_keys("transcription", fid)
        per, rest = subjects.current_line_subjects("transcription", fid, str(Y))
        foreign = subjects.current_foreign(fid, str(Y))
        names = {}
        for k, i in keys:
            members, boundary = subjects.reach(doc, i)
            strings = set(members) | set(boundary)
            for m in members:
                strings |= set(subjects._strings(by_id[m]))
            names[k] = sorted(s for s in strings if s in seen.ids and (s in by_id or s in index))
        whole, wn = watched(subjects.current, "transcription", fid, str(Y))
        out["transcription"][fid] = {"keys": keys, "lines": per, "rest": rest, "foreign": foreign, "names": names,
                                     "whole": whole, "whole_names": wn}
        if os.path.exists(subjects.path("render", fid, str(Y))):
            text = open(subjects.path("render", fid, str(Y)), encoding="utf-8").read()
            rkeys = subjects.target_keys("render", fid)
            rper, rrest, rnames = {}, None, {}
            for k, i in rkeys:
                got, n = watched(subjects.render_line_subjects, fid, text, [i])
                if i in got[0]:
                    rper[k], rnames[k] = got[0][i], n
                rrest = got[1]
            if rrest is None:
                rrest = subjects.render_line_subjects(fid, text, [])[1]
            whole, wn = watched(subjects.current, "render", fid, str(Y))
            out["render"][fid] = {"keys": rkeys, "lines": rper, "rest": rrest, "names": rnames, "whole": whole,
                                  "whole_names": wn}
        whole, wn = watched(subjects.current, "classm", fid, str(Y))
        out["classm"][fid] = {"whole": whole, "names": wn}
    import question_review as Q
    ctx = Q.Ctx.load()
    for inp in ctx.units():
        sha, n = watched(ctx.subject, inp)
        out["questions"][inp] = {"sha": sha, "form": ctx.lines[inp][0], "names": n}
    import screen_review as S
    import gates
    lines = S.load_lines()
    mani = T.manifest()
    for screen, gated in S.screens(lines).items():
        sha, n = watched(S.screen_subject, screen, gated, lines, mani)
        out["screens"][screen] = {"sha": sha, "names": n}
    for key, unit in gates.units(lines).items():
        sha, n = watched(gates.subject, unit, lines, S.encoded_english)
        out["gates"][key] = {"sha": sha, "form": gates.unit_form(unit, lines), "names": n}
    import baseline_check
    import completeness_review as C
    for f in baseline_check.load_forms(os.path.join(ROOT, "canonical", str(Y))):
        got = C.prompt_for(f, mani)
        if got is None:
            continue
        with seen.watching():
            seen.scan(got[0])
        out["completeness"][f["id"]] = {"sha": got[2], "names": sorted(seen.found)}
    return out


def dump_tree(root, ids, dest):
    """Run dump() in the tree at `root` (its own copy of the tools), writing JSON to `dest`."""
    cmd = [sys.executable, os.path.join(root, "tools", "transcription", "rename_carry.py"), "--dump", dest,
           "--ids", json.dumps(sorted(ids)), "--year", str(Y), *jurisdiction.J_ARGS]
    r = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"rename_carry: computing the subjects in {root} failed:\n{r.stderr[-3000:]}")
    return json.load(open(dest, encoding="utf-8"))


# ---------------------------------------------------------------- part B: the year-carry parts at --from

def from_tree(origin, work):
    """(directory holding the tree before the rename, its label): a directory as given, or a commit's forms,
    parameters, tables, rendered English, reading-order source texts and review tools written under `work`."""
    if os.path.isdir(origin):
        return os.path.abspath(origin), "tree " + os.path.abspath(origin)
    sha = subprocess.run(["git", "-C", ROOT, "rev-parse", "--verify", origin + "^{commit}"], capture_output=True, text=True)
    if sha.returncode:
        raise SystemExit(f"--from {origin}: neither a directory nor a commit")
    sha = sha.stdout.strip()
    dest = os.path.join(work, "from")
    rev_tree(sha, dest)
    return dest, sha


def rev_tree(rev, dest):
    """The files year_carry.parts reads, as they were at `rev`, under `dest`."""
    os.makedirs(dest, exist_ok=True)
    paths = [p for p in ("forms", "params", "tables", "rendered", "tools/transcription")
             if subprocess.run(["git", "-C", ROOT, "cat-file", "-e", f"{rev}:{p}"], capture_output=True).returncode == 0]
    listed = subprocess.run(["git", "-C", ROOT, "ls-tree", "-r", "--name-only", rev, "--", "sources"],
                            capture_output=True, text=True).stdout.split("\n")
    paths += [p for p in listed if p.endswith((".txt", "manifest.json"))]  # the reading-order texts, not the PDFs
    arch = subprocess.Popen(["git", "-C", ROOT, "archive", rev, "--", *paths], stdout=subprocess.PIPE)
    r = subprocess.run(["tar", "-x", "-C", dest], stdin=arch.stdout, capture_output=True)
    arch.wait()
    if arch.returncode or r.returncode:
        raise SystemExit(f"rename_carry: cannot read the tree of {rev}")


POLICY_RE = {"prompt": ("transcribe.py", "PROMPT_POLICY"), "comparison": ("transcribe.py", "COMPARISON_POLICY"),
             "types": ("transcribe.py", "TYPE_VALIDATION_POLICY"), "inputs": ("input_context.py", "POLICY"),
             "triage": ("triage.py", "POLICY")}


def policies_at(root):
    """The review tools' policy versions as the tools under `root` declare them (year_carry.policies)."""
    out = {}
    for name, (fname, var) in POLICY_RE.items():
        path = os.path.join(root, "tools", "transcription", fname)
        text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        m = re.search(rf'^{var} = "([^"]*)"', text, re.M)
        out[name] = m.group(1) if m else None
    return out


def _jtree_class():
    import year_carry as YC

    class JTree(YC.Tree):
        """year_carry.Tree reading the New York documents beside the federal ones (forms/ny/<year>/,
        rendered/ny/<year>/, sources/ny/<year>/, params/ny/<year>.yaml, tables/ny/<year>/)."""

        def read(self, *parts):
            if len(parts) == 3 and parts[0] in ("forms", "rendered") and parts[2].startswith("ny_"):
                return super().read(parts[0], "ny", parts[1], parts[2])
            if len(parts) == 3 and parts[0] == "tables" and parts[2] in self._c.get("__ny_tables", ()):
                return super().read("tables", "ny", parts[1], parts[2])
            return super().read(*parts)

        def docs(self):
            if "__docs" not in self._c:
                out = {}
                for d in (self.path("forms", self.year), self.path("forms", "ny", self.year)):
                    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                        if name.endswith(".yaml"):
                            raw = YC.yaml.load(open(os.path.join(d, name), encoding="utf-8"), Loader=YC._Loader) or {}
                            doc = raw.get("form") or raw.get("def")
                            if doc:
                                out[doc["id"]] = doc
                self._c["__docs"] = out
            return self._c["__docs"]

        def params(self):
            if "__params" not in self._c:
                values, enums = {}, {}
                for rel in (("params", self.year + ".yaml"), ("params", "ny", self.year + ".yaml")):
                    text = super().read(*rel)
                    raw = (YC.yaml.load(text, Loader=YC._Loader) or {}) if text else {}
                    p = raw.get("params") or raw
                    values.update(p.get("values") or {})
                    enums.update(p.get("enums") or {})
                self._c["__params"] = (values, enums)
            return self._c["__params"]

        def tables(self):
            if "__tables" not in self._c:
                out, ny = {}, set()
                for d, is_ny in ((self.path("tables", self.year), False), (self.path("tables", "ny", self.year), True)):
                    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                        out[n.split(".")[0]] = n
                        if is_ny:
                            ny.add(n)
                self._c["__tables"], self._c["__ny_tables"] = out, ny
            return self._c["__tables"]

        def pages(self, doc):
            key = f"__pages {doc}"
            if key not in self._c:
                sub = ("sources", "ny", self.year) if doc and jurisdiction.is_ny(doc) else ("sources", self.year)
                m = json.loads(super().read(*sub, "manifest.json") or "{}")
                entries = m["documents"] if isinstance(m, dict) else m
                d = next((e for e in entries if e.get("id") == doc), None)
                name = d and (d.get("cols_file") or d.get("text_file"))
                text = super().read(*sub, name) if name else None
                self._c[key] = text.split("\f") if text is not None else None
            return self._c[key]

    return JTree


def proof_b(kind, at_rev, scratch, fid, line_id, rev_policies):
    """(holds, why) of part B for a compared line (or a class M document, line_id None)."""
    import year_carry as YC
    try:
        a = YC.parts(kind, at_rev, fid, line_id)
        b = YC.parts(kind, scratch, fid, line_id)
    except (KeyError, OSError, ValueError, TypeError) as ex:
        return False, f"its year-carry parts cannot be read: {ex}"
    if a is None or b is None:
        return False, f"no {kind} subject at {'--from' if a is None else 'the scratch tree'}"
    a = {**a, "policies": rev_policies}
    ok, why, _, _ = YC.compare_parts(str(Y), a, b)
    return ok, (None if ok else f"at --from: {why}")


# ---------------------------------------------------------------- the plan

def _entries(names, back, mapping):
    """{old: new} of the map entries whose new id `names` (ids of the current tree) holds."""
    return {back[n]: n for n in names if n in back and mapping.get(back[n]) == n}


class Plan:
    def __init__(self, mapping, rev, now, old, rev_root=None, scratch_root=None):
        self.mapping, self.rev, self.now, self.old = mapping, rev, now, old
        self.back = {v: k for k, v in mapping.items()}
        self.fwd = substituter(mapping)
        self.carry, self.refused = [], []  # [(kind, unit, detail)], [(kind, unit, why)]
        self._rev_root, self._scratch_root = rev_root, scratch_root
        self._trees = None

    def trees(self):
        if self._trees is None:
            JTree = _jtree_class()
            self._trees = (JTree(self._rev_root, str(Y)), JTree(self._scratch_root, str(Y)), policies_at(self._rev_root))
        return self._trees

    def marker(self, names, was, keys=None):
        m = {"by": "rename", "map": dict(sorted(_entries(names, self.back, self.mapping).items())), "from": self.rev, "was": was}
        if keys:
            m["keys"] = keys
        return m

    def b(self, kind, fid, line_id):
        if self._rev_root is None:
            return True, None
        at_rev, scratch, pol = self.trees()
        return proof_b(kind, at_rev, scratch, fid, line_id, pol)


def plan_logs(plan, kind, index_of):
    """(form, changes) for each transcription or render index (index_of(kind, form) -> index or None) the rename
    moves. An index with line subjects carries per compared line and its rest; one without (a whole-form review
    of an older form) carries its whole-form subject or nothing."""
    import review_store
    now, old = plan.now[kind], plan.old[kind]
    for fid in sorted(now):
        index = index_of(kind, fid)
        cur, prev = now[fid], old.get(fid)
        if index is None or prev is None:
            continue
        rows, foreign = index.get("subjects"), index.get("foreign") or {}
        if rows is None:
            ch = _whole(plan, kind, fid, index, cur, prev)
            if ch:
                yield fid, {"lines": {}, "whole": ch}
            continue
        old_key = {i: k for k, i in prev["keys"]}
        lines = {l["key"]: l for l in index["lines"]}
        changes = {"lines": {}}
        for k_new, i_new in cur["keys"]:
            i_old = plan.back.get(i_new, i_new)
            k_old = old_key.get(i_old)
            if k_old is None or k_old not in lines:
                continue
            moved = (cur["lines"].get(k_new) != prev["lines"].get(k_old) or k_new != k_old
                     or (kind == "transcription" and cur["foreign"].get(k_new) != prev["foreign"].get(k_old)))
            if not moved or (k_new == k_old and rows.get(k_new) == cur["lines"].get(k_new)
                             and (kind != "transcription" or k_new not in foreign
                                  or foreign[k_new] == cur["foreign"].get(k_new))):
                continue  # not moved by the rename, or already current under its new names
            unit = f"{fid} {k_new}" + (f" (was {k_old})" if k_new != k_old else "")
            if rows.get(k_old) is None or rows.get(k_old) != prev["lines"].get(k_old):
                plan.refused.append((kind, unit, "the log was not current for this line at the old names "
                                     "(its recorded subject is not what the tree gives with the old names put back)"))
                continue
            if kind == "transcription" and k_old in foreign and foreign[k_old] != prev["foreign"].get(k_old):
                plan.refused.append((kind, unit, "the log was not current for the other documents' lines this line "
                                     "names, at the old names"))
                continue
            ok, why = plan.b(kind, fid, i_old)
            if not ok:
                plan.refused.append((kind, unit, why))
                continue
            was = lines[k_old].get("subject_key") or review_store.subject_key(rows.get(k_old), foreign.get(k_old))
            changes["lines"][k_old] = {"key": k_new, "subject": cur["lines"][k_new],
                                       "foreign": cur["foreign"].get(k_new) if kind == "transcription" else None,
                                       "carried": plan.marker(cur["names"].get(k_new, []), was,
                                                              {k_old: k_new} if k_new != k_old else None)}
            plan.carry.append((kind, unit, "line subject"))
        if cur["rest"] != prev["rest"] and index.get("__rest__") != cur["rest"]:
            if index.get("__rest__") == prev["rest"]:
                changes["rest"] = {"subject": cur["rest"],
                                   "carried": plan.marker(cur.get("whole_names", []), index.get("__rest__"))}
                plan.carry.append((kind, f"{fid} (rest of the document)", "rest"))
            else:
                plan.refused.append((kind, f"{fid} (rest of the document)",
                                     "the log was not current for the rest of the document at the old names"))
        if changes["lines"] or changes.get("rest"):
            yield fid, changes


def _whole(plan, kind, fid, index, cur, prev):
    """The carry of an index's whole-form subject (class M, or a log without line subjects), else None."""
    import review_store
    header = review_store.recorded_subject(kind, index)
    if cur["whole"] == prev["whole"] or header == cur["whole"]:
        return None
    if header != prev["whole"]:
        plan.refused.append((kind, f"{fid} (whole)", "the log was not current at the old names"))
        return None
    ids = [None] if kind == "classm" else [plan.back.get(i, i) for _, i in cur["keys"]]
    for i in ids:
        ok, why = plan.b(kind, fid, i)
        if not ok:
            plan.refused.append((kind, f"{fid} (whole)", why if i is None else f"line {i}: {why}"))
            return None
    plan.carry.append((kind, f"{fid} (whole)", "whole-form subject"))
    return {"subject": cur["whole"], "was": header,
            "carried": plan.marker(cur.get("whole_names", cur.get("names", [])), header)}


def plan_classm(plan, index_of):
    for fid in sorted(plan.now["classm"]):
        index = index_of("classm", fid)
        prev = plan.old["classm"].get(fid)
        if index is None or prev is None:
            continue
        ch = _whole(plan, "classm", fid, index, plan.now["classm"][fid], prev)
        if ch:
            yield fid, {"lines": {}, "whole": ch}


def plan_sampled(plan, kind, records):
    """[(old unit, new unit, current subject, marker)] for the records ({unit: record}) of a sampled kind."""
    src = {"questions": "questions", "screens": None, "false_no": "gates", "completeness": "completeness"}[kind]
    out = []
    for unit, rec in sorted(records.items()):
        if kind == "screens":
            table = "gates" if unit.startswith("gate:") else "screens"
        else:
            table = src
        new_unit = plan.fwd(unit)
        old_side, cur = plan.old[table].get(unit), plan.now[table].get(new_unit)
        if cur is None or old_side is None:
            if new_unit != unit:
                plan.refused.append((kind, f"{unit} -> {new_unit}", "no such unit " + ("now" if cur is None else "at the old names")))
            continue
        if cur["sha"] == rec.get("subject_sha") and new_unit == unit:
            continue
        if cur["sha"] == old_side["sha"] and new_unit == unit:
            continue  # the rename does not move it
        label = unit + (f" -> {new_unit}" if new_unit != unit else "")
        if rec.get("subject_sha") != old_side["sha"]:
            plan.refused.append((kind, label, "its record was not current at the old names")); continue
        plan.carry.append((kind, label, "record"))
        out.append((unit, new_unit, cur["sha"], plan.marker(cur["names"], rec["subject_sha"])))
    return out


# ---------------------------------------------------------------- writing

def write_log_index(kind, fid, changes, family=None):
    import families
    import review_store
    import rulings
    family = family or families.DEFAULT
    path = review_store.index_path(kind, fid, family)
    index = json.load(open(path, encoding="utf-8"))
    renamed = {}
    for l in index["lines"]:
        ch = changes["lines"].get(l["key"])
        if ch is None:
            continue
        k_old, k_new = l["key"], ch["key"]
        if k_new != k_old:
            renamed[k_old] = k_new
            l["section"] = l.get("section", k_old)
            l["key"] = k_new
        fo = ch["foreign"] if kind == "transcription" and (index.get("foreign") or {}).get(k_old) is not None else None
        l["subject_key"] = review_store.subject_key(ch["subject"], fo)
        l["carried"] = ch["carried"]
        if l.get("section"):
            l["carried"] = {**l["carried"], "keys": {l["section"]: k_new}}
    if index.get("subjects") is not None:
        index["subjects"] = {renamed.get(k, k): (changes["lines"][k]["subject"] if k in changes["lines"] else v)
                             for k, v in index["subjects"].items()}
    if index.get("foreign"):
        index["foreign"] = {renamed.get(k, k): (changes["lines"][k]["foreign"] if k in changes["lines"] and changes["lines"][k]["foreign"] else v)
                            for k, v in index["foreign"].items()}
    if changes.get("rest"):
        index["__rest__"] = changes["rest"]["subject"]
        index["rest_carried"] = changes["rest"]["carried"]
    if changes.get("whole"):
        index["subject_carried"] = changes["whole"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=1, ensure_ascii=False)
        f.write("\n")
    if renamed and kind in ("transcription", "render"):
        side = rulings.load(kind, fid, family)
        if any(k[0] in renamed for k in side):
            rulings.save(kind, fid, {((renamed.get(k[0], k[0]),) + tuple(k[1:])): v for k, v in side.items()}, family)
    return path


def _json_write(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def rekey_rulings(path, moves, line_ids_fields=False, sub=None):
    """Re-key per-sample rulings and baseline entries of `path` for each (old unit, new unit, subject, marker)."""
    if not os.path.exists(path) or not moves:
        return 0
    data = json.load(open(path, encoding="utf-8"))
    by_old = {m[0]: m for m in moves}
    n = 0
    out = {}
    for k, r in data.get("rulings", {}).items():
        unit = k.split(":", 1)[1].rsplit("#", 1)[0] if k.startswith("unruled:") else None
        m = by_old.get(unit)
        if m is None or not isinstance(r, dict) or r.get("subject_sha") != m[3]["was"]:
            out[k] = r
            continue
        r = {**r, "subject_sha": m[2], "carried": m[3]}
        if line_ids_fields and sub:
            for f in ("line", "gate"):
                if isinstance(r.get(f), str):
                    r[f] = sub(r[f])
        out["unruled:" + m[1] + "#" + k.rsplit("#", 1)[1]] = r
        n += 1
    data["rulings"] = out
    base = {}
    for k, v in (data.get("baseline") or {}).items():
        unit = k.split(":", 1)[1].rsplit("#", 1)[0] if k.startswith("unruled:") else None
        m = by_old.get(unit)
        if m is not None and v == hashlib.sha256(m[3]["was"].encode()).hexdigest()[:16]:
            base["unruled:" + m[1] + "#" + k.rsplit("#", 1)[1]] = hashlib.sha256(m[2].encode()).hexdigest()[:16]
        else:
            base[k] = v
    if "baseline" in data:
        data["baseline"] = base
    _json_write(path, data)
    return n


def write_sampled(kind, moves, sub):
    """Re-key and re-subject the records of a sampled kind; returns the files written."""
    if not moves:
        return []
    top = str(jurisdiction.ypath("reviews", Y, {"questions": "questions", "screens": "screens", "false_no": "false_no",
                                                  "completeness": "completeness"}[kind]))
    by_old = {m[0]: m for m in moves}
    written = []

    def moved(unit, rec):
        m = by_old[unit]
        rec = {**rec, "subject_sha": m[2], "carried": m[3]}
        return m[1], rec

    if kind in ("questions", "false_no"):
        for name in sorted(os.listdir(top)):
            if not name.endswith(".json") or name == "rulings.json":
                continue
            p = os.path.join(top, name)
            log = json.load(open(p, encoding="utf-8"))
            revs = log.get("reviews", {})
            if not any(u in by_old for u in revs):
                continue
            new = {}
            for u, rec in revs.items():
                if u in by_old:
                    nu, rec = moved(u, rec)
                    if kind == "false_no" and rec.get("condition"):
                        rec["condition"] = sub(rec["condition"])
                    new[nu] = rec
                else:
                    new[u] = rec
            log["reviews"] = new
            _json_write(p, log)
            written.append(p)
    elif kind == "screens":
        p = os.path.join(top, "screen_review.json")
        rows = json.load(open(p, encoding="utf-8"))
        out = []
        for r in rows:
            if r.get("screen") in by_old:
                nu, r = moved(r["screen"], r)
                r["screen"] = nu
            out.append(r)
        _json_write(p, out)
        written.append(p)
    else:
        p = os.path.join(top, "completeness.json")
        rows = json.load(open(p, encoding="utf-8"))
        out = []
        for r in rows:
            if r.get("form") in by_old:
                _, r = moved(r["form"], r)
            out.append(r)
        _json_write(p, out)
        written.append(p)
    rp = os.path.join(top, "rulings.json")
    if rekey_rulings(rp, moves, kind == "completeness", sub):
        written.append(rp)
    return written


def sampled_records(kind):
    import question_review as Q
    top = str(jurisdiction.ypath("reviews", Y, kind))
    if kind == "questions":
        return {u: r for u, (_, r) in Q.records().items()}
    if kind == "false_no":
        out = {}
        for name in sorted(os.listdir(top)) if os.path.isdir(top) else []:
            if name.endswith(".json") and name != "rulings.json":
                out.update(json.load(open(os.path.join(top, name), encoding="utf-8")).get("reviews", {}))
        return out
    if kind == "screens":
        p = os.path.join(top, "screen_review.json")
        return {r["screen"]: r for r in json.load(open(p, encoding="utf-8"))} if os.path.exists(p) else {}
    p = os.path.join(top, "completeness.json")
    return {r["form"]: r for r in json.load(open(p, encoding="utf-8"))} if os.path.exists(p) else {}


# ---------------------------------------------------------------- the run

def run(mapping, origin, write=False, report=None, keep=None):
    """Plan (and with `write` apply) the carry; (exit status, Plan or None)."""
    import families
    import review_store
    work = keep or tempfile.mkdtemp(prefix="rename_carry.")
    try:
        at_rev, label = from_tree(origin, work)
        before_lines, now_lines = line_ids_at(at_rev), line_ids_at(ROOT)
        problems = stale(mapping, before_lines, now_lines)
        if problems:
            print("rename_carry: the map does not describe the rename since --from; nothing carried:", file=sys.stderr)
            for p in problems:
                print("  " + p, file=sys.stderr)
            return 2, None
        back = {v: k for k, v in mapping.items()}
        scratch = os.path.join(work, "scratch")
        scratch_tree(ROOT, scratch, back)
        now = dump_tree(ROOT, set(mapping.values()), os.path.join(work, "now.json"))
        old = dump_tree(scratch, set(mapping), os.path.join(work, "old.json"))
        plan = Plan(mapping, label, now, old, at_rev, scratch)
        index_of = lambda kind, fid: review_store.load_index(kind, fid, families.DEFAULT)
        logs = {k: dict(plan_logs(plan, k, index_of)) for k in ("transcription", "render")}
        logs["classm"] = dict(plan_classm(plan, index_of))
        sampled = {k: plan_sampled(plan, k, sampled_records(k)) for k in SAMPLED}
        consumers = plan_consumers(plan, before_lines, now_lines)
        written = []
        if write:
            for kind in KINDS:
                for fid, ch in logs[kind].items():
                    written.append(write_log_index(kind, fid, ch))
            for kind in SAMPLED:
                written += write_sampled(kind, sampled[kind], plan.fwd)
            written += write_consumers(consumers, plan)
        text = render_report(plan, write)
        if report:
            with open(report, "w", encoding="utf-8") as f:
                f.write(text)
        print(text.split("\n\n")[1])
        if write:
            print(f"rename_carry: wrote {len(set(written))} file(s)")
        return 0, plan
    finally:
        if keep is None:
            shutil.rmtree(work, ignore_errors=True)


def render_report(plan, wrote):
    lines = ["# Rename carry", "",
             f"{len(plan.carry)} review unit(s) carried across the rename, {len(plan.refused)} not carried "
             f"(map of {len(plan.mapping)} id(s), from {plan.rev}{'' if wrote else '; dry run, nothing written'}).", ""]
    if plan.carry:
        lines += ["## Carried", ""] + [f"- {k} {u}: {d}" for k, u, d in plan.carry] + [""]
    if plan.refused:
        lines += ["## Not carried (review as usual)", ""] + [f"- {k} {u}: {w}" for k, u, w in plan.refused] + [""]
    lines += ["## Map", ""] + [f"- `{o}` -> `{n}`" for o, n in sorted(plan.mapping.items())]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- self-test

def self_test():
    """test_rename_carry.py: the planted renames on a small tree of its own."""
    import test_rename_carry
    return test_rename_carry.main()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--map", help="the rename map: a JSON object of old line id -> new line id")
    ap.add_argument("--from", dest="rev", help="the commit before the rename, or a directory holding that tree")
    ap.add_argument("--write", action="store_true", help="write the carried entries (default: report only)")
    ap.add_argument("--report", help="write the report (markdown) here")
    ap.add_argument("--keep", help="keep the scratch trees and subject dumps in this directory")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--dump", help=argparse.SUPPRESS)
    ap.add_argument("--ids", help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if a.dump:
        data = dump(set(json.loads(a.ids or "[]")))
        with open(a.dump, "w", encoding="utf-8") as f:
            json.dump(data, f)
        return 0
    if not a.map or not a.rev:
        ap.error("--map and --from are required")
    import build_fresh
    build_fresh.require(rendered=True)
    if a.keep:
        os.makedirs(a.keep, exist_ok=True)
    status, _ = run(load_map(a.map), a.rev, a.write, a.report, a.keep)
    return status


if __name__ == "__main__":
    sys.exit(main())
