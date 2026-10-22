"""What each kind of review judges, as a hash: the "subject sha256" every review log
records, so that check_logs.py can tell when a log no longer describes the data.

  transcription  the form's definition, citations left out (tools/citations.py checks them)
  render         the rendered English (rendered/<year>/<form>.md), citations left out
  classm         what the hand-work computes: each line's id, type and expression,
                 without an input's question wording

A change to the review tool's prompt or to the pages a citation names does not
change a subject: those are deliberate and rerun deliberately.
"""
import hashlib
import json
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CITE_TEXT = re.compile(r"\[[a-z0-9-]+\] [^\n]*?\([^()\n]*; sha256 [0-9a-f]+\)")


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _without_cites(o):
    if isinstance(o, dict):
        return {k: _without_cites(v) for k, v in o.items() if k != "cite"}
    if isinstance(o, list):
        return [_without_cites(x) for x in o]
    return o


def of_form(yaml_text):
    return _sha(_without_cites(yaml.safe_load(yaml_text)))


def of_rendered(md_text):
    return hashlib.sha256(CITE_TEXT.sub("[cite]", md_text).encode()).hexdigest()


def of_computation(yaml_text):
    raw = yaml.safe_load(yaml_text)
    doc = raw.get("form") or raw.get("def")
    rows = [{"id": l.get("id"), "type": l.get("type"),
             "expr": {k: v for k, v in (l.get("expr") or {}).items() if k != "source"}} for l in doc.get("lines", [])]
    return _sha(rows)


def path(kind, fid, year):
    if kind == "render":
        return os.path.join(ROOT, "rendered", str(year), fid + ".md")
    return os.path.join(ROOT, "forms", str(year), fid + ".yaml")


def of_text(kind, text):
    return {"transcription": of_form, "render": of_rendered, "classm": of_computation}[kind](text)


def current(kind, fid, year):
    """The subject hash of a form as it is now."""
    return of_text(kind, open(path(kind, fid, year), encoding="utf-8").read())
