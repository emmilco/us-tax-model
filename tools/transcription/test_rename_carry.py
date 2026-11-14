#!/usr/bin/env python3
"""Self-test of rename_carry.py on a small tree of its own, built under a temporary directory.

The tree holds two forms: `t` (an input t.a_2025; line 1 reads it; line 2, t.c_2025, reads line 1; line 3 reads
h.m_2025 of the other form) and `h` (helpers only: an input h.k_2025 and a computed helper h.m_2025 that t reads,
so its transcription log key and its render log keys are ids). Each has transcription and render reviews, `t` a
class M review, and both inputs a question review, recorded through review_store with the subjects the review
tools compute; the render review of `h` holds a ruled disagreement on a line whose key is renamed.

The ids are then renamed (t.a_2025, t.c_2025, h.k_2025, h.m_2025) and line 2's label is changed too. Planted:
- a rename with an unchanged subject (h, and the question of each input): carried, keys and rulings re-keyed;
- a rename with a changed label (line 2): its render review is not carried and stays stale; its transcription
  review, which does not judge labels, is carried;
- a rename of a line other lines read (t.a_2025 read by line 1, h.m_2025 read by line 3): the readers' reviews are
  carried;
- a stale map (an id that is not a line): refused whole, nothing written;
- a --from tree that is not the one the rename was made from (line 1's label differs there): part B refuses the
  render review of line 1 and carries its transcription review (dry run, nothing written);
- a second run: nothing more carried, nothing changed.
Afterwards the currency checks (review_store.state, as check_logs uses it; review_store.check; rulings.check;
the question subjects) accept every carried entry and still report the line whose proof failed.

The steps that need the small tree's own paths run there, in a copy of the tools (--inside STEP).

    test_rename_carry.py
"""
import hashlib, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
MAP = {"t.a_2025": "t.a_now", "t.c_2025": "t.c_now", "h.k_2025": "h.k_now", "h.m_2025": "h.m_now"}
Y = "2025"


def forms(renamed=False):
    """{doc id: document} of the small tree, before or after the rename (and line 2's new label)."""
    n = (lambda i: MAP.get(i, i)) if renamed else (lambda i: i)
    t = {"id": "t", "kind": "form", "title": "Test form", "tax_year": int(Y), "lines": [
        {"id": n("t.a_2025"), "printed": "(helper)", "type": "Dollars", "label": "Amount A",
         "expr": {"op": "input", "source": "Amount A paid"}},
        {"id": "t.b", "printed": "1", "type": "Dollars", "label": "Line one", "expr": {"op": "copy", "from": n("t.a_2025")}},
        {"id": n("t.c_2025"), "printed": "2", "type": "Dollars", "label": "Line two, as renamed" if renamed else "Line two",
         "expr": {"op": "copy", "from": "t.b"}},
        {"id": "t.d", "printed": "3", "type": "Dollars", "label": "Line three", "expr": {"op": "copy", "from": n("h.m_2025")}}]}
    h = {"id": "h", "kind": "form", "title": "Helpers", "tax_year": int(Y), "lines": [
        {"id": n("h.k_2025"), "printed": "(helper)", "type": "Dollars", "label": "Amount K",
         "expr": {"op": "input", "source": "Amount K received"}},
        {"id": n("h.m_2025"), "printed": "(helper)", "type": "Dollars", "label": "Helper M",
         "expr": {"op": "copy", "from": n("h.k_2025")}}]}
    return {"t": t, "h": h}


def rendered(doc):
    """The rendered English of a document, in the engine's section format."""
    out = [f"# {doc['title']}", "", f"- Document: `{doc['id']}` (form, tax year {Y})", ""]
    for l in doc["lines"]:
        helper = str(l["printed"]).startswith("(")
        enc = (f"Input — {l['expr']['source']}" if l["expr"]["op"] == "input" else f"The amount of {l['expr']['from']}")
        out += [f"## {l['printed']} — `{l['id']}`", "",
                f"- **{'Authored helper label' if helper else 'IRS'}:** {l['label']}",
                f"- **Encoded ({l['type']}):** {enc}",
                f"- Expr: `{json.dumps(l['expr'], sort_keys=True)}`", ""]
    return "\n".join(out)


def write_tree(root, docs):
    import yaml
    for fid, doc in docs.items():
        p = os.path.join(root, "forms", Y, fid + ".yaml")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if os.path.exists(p):
            os.remove(p)
        with open(p, "w", encoding="utf-8") as f:
            yaml.safe_dump({"form": doc}, f, sort_keys=False)
        p = os.path.join(root, "rendered", Y, fid + ".md")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if os.path.exists(p):
            os.remove(p)
        with open(p, "w", encoding="utf-8") as f:
            f.write(rendered(doc))
    questions = [{"input": l["id"], "prompt": l["expr"]["source"], "help": ""} for d in docs.values() for l in d["lines"]
                 if l["expr"]["op"] == "input"]
    p = os.path.join(root, "canonical", Y, "interview-full.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p):
        os.remove(p)
    with open(p, "w", encoding="utf-8") as f:
        json.dump({"questions": questions}, f)


def build(root):
    """The small tree: the repository's tools and year list, the forms above, and an empty archive."""
    os.makedirs(root)
    subprocess.run(["cp", "-c", "-R", os.path.join(REPO, "tools"), os.path.join(root, "tools")], check=True)
    shutil.copy(os.path.join(REPO, "years.json"), root)
    for rel, text in ((f"sources/{Y}/manifest.json", '{"documents": []}'), (f"params/{Y}.yaml", "params: {}\n"),
                      (f"tables/{Y}/.keep", "")):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)
    write_tree(root, forms())


def inside(root, step, *args):
    r = subprocess.run([sys.executable, os.path.join(root, "tools", "transcription", "test_rename_carry.py"), "--inside",
                        step, *args], cwd=root, capture_output=True, text=True)
    if r.returncode:
        raise AssertionError(f"step {step} failed:\n{r.stdout[-2000:]}\n{r.stderr[-3000:]}")
    return json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else None


# ---------------------------------------------------------------- steps run inside the small tree

def _log(kind, fid, sections, raw):
    import subjects
    head = (f"# Review — {fid}\n\nintro\n\n| field | value |\n| --- | --- |\n| date | 2026-11-01 |\n"
            f"| prompt sha256 | {'a' * 64} |\n| prompt policy | p-v1 |\n| subject sha256 | {subjects.current(kind, fid, Y)} |\n")
    tail = subjects.table_for(kind, fid, Y) if kind != "classm" else []
    body = "".join("\n### " + s for s in sections)
    return head + "\n## Lines\n" + body + ("\n" + "\n".join(tail).rstrip("\n") + "\n" if tail else "") + raw


def step_setup():
    import review_store, rulings, rule, subjects
    raw = {"transcription": "\n## Raw second transcription\n\n```yaml\nlines: []\n```\n",
           "render": "\n## Raw response\n\n```yaml\nlines: []\n```\n"}
    agree = {"transcription": "Status: **AGREE**\n\n", "render": "Status: **MATCH**\n\nModel: fine\n\n"}
    for kind in ("transcription", "render"):
        for fid in ("t", "h"):
            secs = []
            for key, _ in subjects.target_keys(kind, fid):
                if kind == "render" and key == "k_2025":
                    secs.append("k_2025 — Amount K\nStatus: **MISMATCH**\n\nRestated: Amount K received\n\nModel: unclear\n\n"
                                "Ruling: open\n\n")
                else:
                    secs.append(f"{key} — label\n" + agree[kind])
            rulings.write_log(kind, fid, _log(kind, fid, secs, raw[kind]))
    rule.apply("h", {"k_2025": "Ruling: scope; the amount is asked as the instructions ask it"}, "render")
    pid = "b" * 64
    cm = [f"case classm.t.1 — prompt sha256 {pid}; branches: none\n",
          "classm.t.1 — 1 — Line one\nStatus: **AGREE**\n\nValue: $1.00\n\n",
          "classm.t.1 — 2 — Line two\nStatus: **AGREE**\n\nValue: $1.00\n\n"]
    rulings.write_log("classm", "t", _log("classm", "t", cm, "\n## Raw responses\n\n### classm.t.1\n\n```yaml\nlines: []\n```\n"))
    import question_review as Q
    ctx = Q.Ctx.load()
    for fid, inputs in (("t", ["t.a_2025"]), ("h", ["h.k_2025"])):
        log = {"form": fid, "reviews": {i: {"subject_sha": ctx.subject(i), "samples": [
            {"verdict": "NARROW", "findings": [{"kind": "NARROW", "situation": "s"}], "system_sha": "c" * 64}]} for i in inputs}}
        os.makedirs(Q.OUT, exist_ok=True)
        with open(Q.log_path(fid), "w", encoding="utf-8") as f:
            json.dump(log, f)
    with open(os.path.join(Q.OUT, "rulings.json"), "w", encoding="utf-8") as f:
        json.dump({"rulings": {"unruled:t.a_2025#1": {"subject_sha": ctx.subject("t.a_2025"), "class": "model error"}},
                   "baseline": {}}, f)
    with open(os.path.join(rulings.REVIEWS, "consumers.json"), "w", encoding="utf-8") as f:
        json.dump({"rulings": {"consumer:t.a_2025@d:p1": {"verdict": "same", "question_phrase": "q", "source_phrase": "s",
                                                           "reason": "r"}},
                   "baseline": {"consumer:h.k_2025@d:p2": "0123456789abcdef"}}, f)
    print(json.dumps(state()))


def state():
    """What the currency checks say of the small tree's reviews."""
    import io, contextlib
    import review_store, rulings, families
    import question_review as Q
    out = {}
    for kind in ("transcription", "render", "classm"):
        for fid in ("t", "h"):
            s = review_store.state(kind, fid, families.DEFAULT, Y)
            if s is not review_store.NO_INDEX:
                out[f"{kind} {fid}"] = s
    err = io.StringIO()
    with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
        out["store check"] = review_store.check()
        out["rulings check"] = rulings.check()
    out["store problems"] = err.getvalue()
    ctx = Q.Ctx.load()
    recs = Q.records()
    out["questions"] = {i: (recs.get(i, (None, {}))[1].get("subject_sha") == ctx.subject(i)) for i in ctx.units()}
    data = json.load(open(os.path.join(Q.OUT, "rulings.json"), encoding="utf-8"))
    out["question rulings"] = sorted(data["rulings"])
    unit = lambda k: k.split(":", 1)[1].rsplit("#", 1)[0]
    out["question ruling current"] = [k for k, r in data["rulings"].items()
                                      if unit(k) in ctx.units() and r.get("subject_sha") == ctx.subject(unit(k))]
    consumers = json.load(open(os.path.join(rulings.REVIEWS, "consumers.json"), encoding="utf-8"))
    out["consumers"] = sorted(consumers["rulings"]) + sorted(consumers["baseline"])
    out["render h keys"] = [l["key"] for l in review_store.load_index("render", "h")["lines"]]
    out["render h sidecar"] = sorted(k[0] for k in rulings.load("render", "h"))
    out["view keys"] = [s[0] for s in review_store.parse("render", review_store.view("render", "h"))["sections"]]
    return out


def step_state():
    print(json.dumps(state()))


def step_carry(map_path, origin, report, write="write"):
    import rename_carry
    status, plan = rename_carry.run(json.load(open(map_path)), origin, write=write == "write", report=report)
    print(json.dumps({"status": status, "carry": [list(c) for c in plan.carry] if plan else None,
                      "refused": [list(r) for r in plan.refused] if plan else None}))


def step_digest():
    """A digest of every review file of the small tree (indexes, sidecars, sampled records)."""
    h = hashlib.sha256()
    for d, _, files in sorted(os.walk("reviews")):
        for n in sorted(files):
            p = os.path.join(d, n)
            h.update(p.encode())
            h.update(open(p, "rb").read())
    print(json.dumps(h.hexdigest()))


# ---------------------------------------------------------------- the test

def main():
    import rename_carry
    work = tempfile.mkdtemp(prefix="rename_carry_test.")
    bad = []

    def expect(cond, what):
        if not cond:
            bad.append(what)

    try:
        sub = rename_carry.substituter({"x.a_2025": "x.a_now"})
        expect(sub("x.a_2025 and x.a_2025_if_y and y.x.a_2025 and x.a_2025. and p[q].a_2025 and x[k].a_2025")
               == "x.a_now and x.a_2025_if_y and y.x.a_2025 and x.a_now. and p[q].a_2025 and x[k].a_now",
               "substitution: whole ids and the collection form only")
        root, before = os.path.join(work, "tree"), os.path.join(work, "before")
        build(root)
        before_state = inside(root, "setup")
        for k in ("transcription t", "transcription h", "render t", "render h", "classm t"):
            expect(before_state.get(k) is None, f"before the rename, {k} is current: {before_state.get(k)}")
        expect(all(before_state["questions"].values()), "before the rename, every question review is current")
        subprocess.run(["cp", "-c", "-R", root, before], check=True)
        write_tree(root, forms(renamed=True))
        renamed = inside(root, "state")
        expect(renamed["transcription t"] and renamed["render h"] and renamed["classm t"],
               "after the rename and before the carry, the reviews are stale")
        # a stale map: refused whole, nothing written
        stale_map = os.path.join(work, "stale.json")
        with open(stale_map, "w") as f:
            json.dump({**MAP, "t.zz_2025": "t.zz_now"}, f)
        digest = inside(root, "digest")
        got = inside(root, "carry", stale_map, before, os.path.join(work, "stale.md"))
        expect(got["status"] == 2 and got["carry"] is None, f"a stale map is refused: {got}")
        expect(inside(root, "digest") == digest, "a stale map writes nothing")
        map_path = os.path.join(work, "map.json")
        with open(map_path, "w") as f:
            json.dump(MAP, f)
        # part B: against a --from tree in which line 1's label differs from what the rename was made from, the
        # render review of line 1 (which judges labels) is not carried; its transcription review is
        other = os.path.join(work, "other")
        subprocess.run(["cp", "-c", "-R", before, other], check=True)
        docs = forms()
        docs["t"]["lines"][1]["label"] = "Line one, edited at --from"
        write_tree(other, docs)
        got = inside(root, "carry", map_path, other, os.path.join(work, "other.md"), "dry-run")
        refused_b = {(k, u): w for k, u, w in got["refused"]}
        expect(refused_b.get(("render", "t 1"), "").startswith("at --from: the line or what it reads changed"),
               f"part B refuses a line whose year-carry parts differ at --from: {refused_b}")
        expect(("transcription", "t 1") in {(k, u) for k, u, _ in got["carry"]}, "part B: the transcription review carries")
        expect(inside(root, "digest") == digest, "a dry run writes nothing")
        # the carry
        got = inside(root, "carry", map_path, before, os.path.join(work, "report.md"))
        carried = {(k, u) for k, u, _ in got["carry"]}
        refused = {(k, u): w for k, u, w in got["refused"]}
        print(f"  carried {len(carried)}: " + "; ".join(f"{k} {u}" for k, u in sorted(carried)))
        print(f"  not carried {len(refused)}: " + "; ".join(f"{k} {u}: {w}" for (k, u), w in sorted(refused.items())))
        for unit in [("transcription", "t 1"), ("transcription", "t 2"), ("transcription", "t 3"),
                     ("transcription", "h h.m_now (was h.m_2025)"), ("render", "t 1"), ("render", "t 3"),
                     ("render", "h k_now (was k_2025)"), ("render", "h m_now (was m_2025)"), ("classm", "t (whole)"),
                     ("questions", "t.a_2025 -> t.a_now"), ("questions", "h.k_2025 -> h.k_now")]:
            expect(unit in carried, f"carried: {unit}")
        expect(("render", "t 2") in refused and "the log was not current" in refused[("render", "t 2")],
               f"a rename with a changed label is not carried: {refused}")
        after = inside(root, "state")
        for k in ("transcription t", "transcription h", "render h", "classm t"):
            expect(after.get(k) is None, f"after the carry, {k} is current: {after.get(k)}")
        expect(after["render t"] and "lines changed or not yet reviewed: 2" in after["render t"],
               f"the line whose proof failed is still stale: {after['render t']}")
        expect(after["store check"] == 0, f"review_store.check accepts the carried indexes: {after['store problems']}")
        expect(after["rulings check"] == 0, "rulings.check accepts the re-keyed sidecar")
        expect(after["render h keys"] == ["k_now", "m_now"] and after["view keys"] == ["k_now", "m_now"],
               f"renamed log keys: {after['render h keys']}, view {after['view keys']}")
        expect(after["render h sidecar"] == ["k_now"], f"the ruling on a renamed key is re-keyed: {after['render h sidecar']}")
        expect(after["questions"] == {"h.k_now": True, "t.a_now": True}, f"question records carried: {after['questions']}")
        expect(after["question rulings"] == ["unruled:t.a_now#1"] and after["question ruling current"] == ["unruled:t.a_now#1"],
               f"question ruling re-keyed with the current subject: {after['question rulings']}")
        expect(after["consumers"] == ["consumer:t.a_now@d:p1", "consumer:h.k_now@d:p2"],
               f"consumers.json keys of renamed inputs are re-keyed: {after['consumers']}")
        report = open(os.path.join(work, "report.md")).read()
        expect("## Not carried" in report and "render t 2" in report, "the report lists what was not carried")
        # a second run finds nothing more to carry, and refuses again only the line whose proof failed
        again = inside(root, "carry", map_path, before, os.path.join(work, "again.md"))
        expect(again["carry"] == [] and [(k, u) for k, u, _ in again["refused"]] == [("render", "t 2")],
               f"a second run carries nothing more: {again}")
        expect(inside(root, "state") == after, "a second run changes nothing")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    for b in bad:
        print("rename-carry self-test: WRONG:", b, file=sys.stderr)
    print(f"rename-carry self-test: {'ok' if not bad else str(len(bad)) + ' problem(s)'}")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--inside":
        sys.path.insert(0, HERE)
        sys.path.insert(0, os.path.join(REPO, "tools"))
        step, args = sys.argv[2], sys.argv[3:]
        del sys.argv[1:]
        {"setup": step_setup, "state": step_state, "carry": step_carry, "digest": step_digest}[step](*args)
        sys.exit(0)
    sys.path.insert(0, HERE)
    sys.exit(main())
