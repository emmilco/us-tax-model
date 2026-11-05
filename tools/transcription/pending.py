"""Reviews of a jurisdiction not yet run: reviews/<jurisdiction>/<year>/pending.json.

The New York documents entered the project before their first model reviews. Until a review is run,
the check scripts (check_logs.py, check_completeness.py, check_screens.py) in New York mode report its
document as pending instead of failing:

    {"transcription": ["ny_it201", ...], "render": [...], "classm": [...], "completeness": [...], "screens": [...]}

Each list names the documents (for "screens", the screen ids) whose review of that kind is pending. A listed
document that has a review fails the check until it is removed from the list, so the list only shrinks and
each document is held to the strict check from its first review on. Deleting the file (or emptying every list)
makes the checks strict. The federal tree has no such file, so every federal check is strict as before.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402

# In New York mode REVIEW_PENDING_FILE names another list (the tests use it to check both outcomes); federally the
# list is always reviews/<year>/pending.json, which does not exist.
PATH = (os.environ.get("REVIEW_PENDING_FILE") if jurisdiction.NY else None) or str(jurisdiction.ypath("reviews", Y, "pending.json"))
KINDS = ("transcription", "render", "classm", "completeness", "screens")


def load(path=None):
    path = path or PATH
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding="utf-8"))
    bad = sorted(set(data) - set(KINDS) - {"note"})
    if bad:
        raise SystemExit(f"{os.path.relpath(path, ROOT)}: unknown review kind(s) {', '.join(bad)}")
    return {k: set(data.get(k) or []) for k in KINDS}


def listed(kind, path=None):
    """The documents (screens) whose review of `kind` is pending."""
    return load(path).get(kind, set())


def name():
    return os.path.relpath(PATH, ROOT)
