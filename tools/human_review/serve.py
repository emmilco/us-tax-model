#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Serve the reading packets of .human-review/ and save the verdicts a reader types in them to
reviews/<year>/human/<form>.md, one log per form, merged by line id across items.

A log entry is a printed line (what the packet judges); the helpers the packet folded into it
are recorded on the entry under "Helpers folded", so every line of the log carries a verdict.

Listens on 127.0.0.1 only (or a Unix socket with --uds, for lab-server). The reader's name is
whatever the page sends; a name that looks like a model is refused, and nothing is defaulted.

    serve.py [--port 8790] [--uds /path/to.sock]

    GET  /                       the index of packets (build them with packet.py first)
    GET  /<item>.html, /pages/…  the packets and page images
    GET  /api/verdicts?item=N    the verdicts already logged for item N's printed lines
    POST /api/verdicts           {item, reader, date, lines:[{ref, verdict, reason}]}
"""
import argparse
import datetime
import json
import os
import re
import socket
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import packet  # noqa: E402

sys.path.insert(0, str(packet.ROOT / "tools" / "transcription"))
import subjects  # noqa: E402

Y = packet.Y
LOGS = packet.ROOT / "reviews" / Y / "human"
MODEL_NAME = re.compile(r"claude|gpt|deepseek|model|agent", re.I)
SUBJECT_KIND = "render"
FIELDS = ("Label", "Reading", "Cite", "Pages", "Helpers folded", "Item")


def log_path(fid):
    return LOGS / f"{fid}.md"


def parse_log(text):
    """A human log's header fields and per-line records, by line id."""
    header = dict(re.findall(r"^\| ([a-z /]+) \| (.*) \|$", text, flags=re.M))
    lines = {}
    for m in re.finditer(r"^### (.*?) — `([^`]+)`\n(.*?)(?=^### |\Z)", text, flags=re.M | re.S):
        body = m.group(3)
        fields = dict(re.findall(r"^([A-Z][a-z]+(?: [a-z]+)?): (.*)$", body, flags=re.M))
        reason = re.search(r"^Reason:\n(.*)\Z", body, flags=re.M | re.S)
        v = re.match(r"\*\*(\w+)\*\*", fields.get("Verdict", ""))
        reason = reason.group(1).strip() if reason else ""
        rec = {"printed": m.group(1), "verdict": v.group(1) if v and v.group(1) in packet.VERDICTS else "",
               "reason": "" if reason == "(empty)" else reason}
        for f in FIELDS:
            rec[f] = fields.get(f, "")
        lines[m.group(2)] = rec
    return header, lines


def source_pages(text):
    """doc -> set of pages, from a human log's source table."""
    out = {}
    for doc, pages in re.findall(r"^\| (\S+) \| [^|]* \| ([^|]*) \| [0-9a-f]{64} \| (?:[0-9a-f]{64}|-) \|$", text, flags=re.M):
        out.setdefault(doc, set()).update(int(x) for x in re.findall(r"\d+", pages))
    return out


def line_pages(rec):
    """doc -> set of pages the packet shows for one printed record (its citation and the folded ones)."""
    import citations as C
    out = {}
    cites = [rec["cite"]] + [packet.canon().lines[h].get("cite", {}) for h in rec.get("folded_cites", [])]
    arch = C.Archive()
    for ct in cites:
        if not ct.get("doc"):
            continue
        for seg_doc, pages, _, _, _ in C.segments(ct["doc"], ct.get("locator", "")):
            if seg_doc in arch.docs:
                out.setdefault(seg_doc, set()).update(pages)
    return out


def saved_for_item(n):
    it = packet.item(n)
    recs, _ = packet.plan_item(it)
    out, reader = [], ""
    for r in recs:
        p = log_path(r["form"])
        if not p.exists():
            continue
        header, lines = parse_log(p.read_text(encoding="utf-8"))
        reader = reader or header.get("reader", "")
        if r["id"] in lines and (lines[r["id"]]["verdict"] or lines[r["id"]]["reason"]):
            out.append({"ref": r["ref"], **{k: lines[r["id"]][k] for k in ("verdict", "reason")}})
    return {"item": n, "reader": reader, "lines": out}


def write_log(fid, title, reader, date, items, records, pages):
    """records: id -> {printed, Label, Reading, Cite, Pages, Helpers folded, Item, verdict, reason};
    pages: doc -> set of pages."""
    docs = packet.manifest()
    counts = {v: sum(1 for r in records.values() if r["verdict"] == v) for v in packet.VERDICTS}
    empty = sum(1 for r in records.values() if not r["verdict"])
    out = [f"# Human reading — {fid}", "",
           f"Printed lines of `{title}` (`rendered/{Y}/{fid}.md`) read against the archived IRS pages by a person, "
           f"through the packets of `tools/human_review/` (integrity plan item 1.1), each with the helper lines the packet "
           f"folded into it. Every verdict and reason is the reader's own text.", "",
           "| field | value |", "| --- | --- |",
           f"| date | {date} |", f"| reader | {reader} |",
           f"| items | {', '.join(str(i) for i in sorted(items))} |",
           f"| subject kind | {SUBJECT_KIND} |",
           f"| subject sha256 | {subjects.current(SUBJECT_KIND, fid, Y)} |",
           f"| lines judged | {len(records)} |",
           f"| match / mismatch / unclear / empty | {counts['MATCH']} / {counts['MISMATCH']} / {counts['UNCLEAR']} / {empty} |", "",
           "## Source pages read", "",
           "| document | revision | pages | text sha256 | cols sha256 |", "| --- | --- | --- | --- | --- |"]
    for doc in sorted(pages):
        d = docs[doc]
        out.append(f"| {doc} | {d.get('revision') or ''} | {', '.join(map(str, sorted(pages[doc])))} | {d['text_sha256']} | {d.get('cols_sha256', '-')} |")
    out += ["", "## Lines", ""]
    for lid, r in records.items():
        out += [f"### {r['printed']} — `{lid}`"] + [f"{f}: {r.get(f, '')}" for f in FIELDS] + [
                f"Verdict: **{r['verdict']}**" if r["verdict"] else "Verdict: (empty)",
                "Reason:", r["reason"] or "(empty)", ""]
    LOGS.mkdir(parents=True, exist_ok=True)
    log_path(fid).write_text("\n".join(out), encoding="utf-8")


def save(body):
    n = int(body["item"])
    reader = (body.get("reader") or "").strip()
    if not reader:
        raise ValueError("the reader field is empty")
    if MODEL_NAME.search(reader):
        raise ValueError(f"the reader field names a model ({reader!r}); a human log is signed by a person")
    date = body.get("date") or datetime.date.today().isoformat()
    it = packet.item(n)
    recs, _ = packet.plan_item(it)
    posted = {l["ref"]: l for l in body.get("lines", [])}
    by_form, pages_of = {}, {}
    for r in recs:
        p = posted.get(r["ref"], {})
        v = (p.get("verdict") or "").strip().upper()
        if v and v not in packet.VERDICTS:
            raise ValueError(f"{r['ref']}: verdict {v!r} is not one of {', '.join(packet.VERDICTS)}")
        pages = line_pages(r)
        for doc, nums in pages.items():
            pages_of.setdefault(r["form"], {}).setdefault(doc, set()).update(nums)
        by_form.setdefault(r["form"], {})[r["id"]] = {
            "printed": r["printed"], "Label": r["label"], "Reading": r["reading_text"].replace("\n", " "),
            "Cite": r["cite_text"], "Pages": "; ".join(f"{d} {', '.join(map(str, sorted(s)))}" for d, s in sorted(pages.items())),
            "Helpers folded": ", ".join(r["helpers"]) or "(none)", "Item": str(n), "verdict": v,
            "reason": (p.get("reason") or "").strip()}
    written = []
    for fid, new in by_form.items():
        records, items, pages = {}, {n}, {}
        p = log_path(fid)
        if p.exists():
            text = p.read_text(encoding="utf-8")
            header, records = parse_log(text)
            if header.get("reader") and header["reader"] != reader:
                raise ValueError(f"{p.name} is signed by {header['reader']!r}; one log has one reader (its commit author)")
            items |= {int(x) for x in re.findall(r"\d+", header.get("items", ""))}
            pages = source_pages(text)
        records.update(new)
        for doc, nums in pages_of.get(fid, {}).items():
            pages.setdefault(doc, set()).update(nums)
        write_log(fid, packet.form_title(fid), reader, date, items, records, pages)
        written.append(str(p.relative_to(packet.ROOT)))
    return written


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(packet.OUT), **k)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.log_date_time_string(), fmt % args))

    def _json(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/api/verdicts":
            q = parse_qs(u.query)
            try:
                return self._json(200, saved_for_item(int(q.get("item", ["0"])[0])))
            except (ValueError, SystemExit) as e:
                return self._json(400, {"error": str(e)})
        if ".." in u.path:
            return self._json(400, {"error": "bad path"})
        return super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path != "/api/verdicts":
            return self._json(404, {"error": "no such endpoint"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("content-length", "0"))) or b"{}")
            written = save(body)
        except (ValueError, KeyError, SystemExit) as e:
            return self._json(400, {"error": str(e)})
        self._json(200, {"written": written})


class UnixServer(ThreadingHTTPServer):
    address_family = socket.AF_UNIX

    def server_bind(self):
        if os.path.exists(self.server_address):
            os.unlink(self.server_address)
        self.socket.bind(self.server_address)

    def get_request(self):
        sock, _ = self.socket.accept()
        return sock, ("unix", 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8790)
    ap.add_argument("--uds", help="listen on this Unix socket instead of 127.0.0.1 (for lab-server)")
    a = ap.parse_args()
    if not packet.OUT.exists():
        sys.exit(f"{packet.OUT} does not exist; run packet.py --all first")
    if a.uds:
        srv = UnixServer(a.uds, Handler)
        print(f"serving {packet.OUT} on {a.uds}; logs to {LOGS}", flush=True)
    else:
        srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
        print(f"serving {packet.OUT} at http://127.0.0.1:{a.port}/ ; logs to {LOGS}", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
