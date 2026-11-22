"""Model families, their review tiers, and the names their review artifacts take.

A family is the first token of a model name (`claude-opus-5-5` -> `claude`, `deepseek-v4-pro`
-> `deepseek`). `families.json` puts each family in one of two tiers:

  qualified  a current log from any one of these families satisfies a form's review requirement.
             check_logs.py asks them in the order listed and passes a form on the first log that
             is current and holds no open ruling. Every other log of that form is advisory.
  advisory   a review that corroborates but never satisfies: it is usable beside a qualified
             log and is never the only basis for a form. Its logs are integrity-checked and
             counted, and one that has gone stale where it would otherwise earn credit fails the
             check while its family is callable.

`callable` says whether the tools may call the family's model, and is independent of the tier: a
family that may not be called keeps its logs and its standing (Claude's logs go on satisfying
forms while Claude is not called), and a qualified family that is not callable is simply not asked
again. A deliberate call to a family that is not callable needs the override
(`--uncallable-family FAMILY --uncallable-family-reason TEXT` on the review tools and
rerun_all.py), and each paid call it makes records the reason in its cost-ledger row.

The Claude family's logs keep their plain names; another family's review of the same form sits
beside them:

  reviews/<year>/<kind>/<form>.md                      the Claude log and <form>.rulings.json
  reviews/<year>/<kind>/<form>.<family>.md             another family's log and <form>.<family>.rulings.json
  fixtures/<year>/classm.json / classm.<family>.json   class M fixtures per family; another family's
                                                       case ids carry the family as a suffix

Logs are keyed by family, not by model, so `models` pins at most one model per family: two models of
one family would share a log slot, and a pinned family's evidence is the review that model wrote. Claude
is unpinned as before, so the tools' `--model` default names it. A family in neither tier fails the check
when it holds a log, so a demoted family is moved, never dropped silently.

`by_kind` overrides the tiers and the models for one review kind; `callable` is global, because it
says which transports this machine may call, not what a kind needs.
"""
import json
import os

DEFAULT = "claude"                                 # the family whose logs carry no suffix
LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "families.json")
UNCALLABLE_ENV = "REVIEW_UNCALLABLE_FAMILY"             # the not-callable family a deliberate run may call
UNCALLABLE_REASON_ENV = "REVIEW_UNCALLABLE_FAMILY_REASON"  # its reason, written into each cost-ledger row


class NotCallable(ValueError):
    """A model of a family the tools may not call was called without the override that names it."""


def load(kind=None):
    """The tiers, the pinned models and callability, with the optional per-kind overrides of the
    tiers and the models applied."""
    with open(LIST, encoding="utf-8") as f:
        base = json.load(f)
    data = base.get("by_kind", {}).get(kind, base) if kind is not None else base
    models = dict(base.get("models", {}))
    models.update(data.get("models", {}))
    qualified, advisory = list(data.get("qualified", [])), list(data.get("advisory", []))
    both = sorted(set(qualified) & set(advisory))
    if both:
        raise ValueError(f"{LIST}: {', '.join(both)} is in both qualified and advisory; "
                         f"a family's log either satisfies a form or corroborates one")
    return {"qualified": qualified, "advisory": advisory, "models": models,
            "callable": {f: bool(on) for f, on in base.get("callable", {}).items()}}


def is_callable(family):
    """Whether the tools may call the family's model (families.json `callable`; an unlisted family is not).
    Independent of the tier: a family that is not callable keeps its logs and their standing."""
    return load()["callable"].get(family, False)


def override():
    """(family, reason) of the not-callable-family override this process runs under, else None."""
    family, reason = os.environ.get(UNCALLABLE_ENV, "").strip(), os.environ.get(UNCALLABLE_REASON_ENV, "").strip()
    return (family, reason) if family and reason else None


def require_callable(model):
    """Refuse a model of a family that may not be called unless the override names that family."""
    family = family_of(model)
    if is_callable(family):
        return None
    granted = override()
    if granted and granted[0] == family:
        return granted
    raise NotCallable(f"model family {family!r} ({model}) is not callable in tools/transcription/families.json; "
                      f"run it once with --uncallable-family {family} --uncallable-family-reason TEXT, "
                      f"or allow it by setting its \"callable\" flag to true")


def add_override_args(ap):
    ap.add_argument("--uncallable-family", metavar="FAMILY",
                    help="allow this run to call a model family families.json marks not callable")
    ap.add_argument("--uncallable-family-reason", metavar="TEXT", help="why; recorded in each paid call's cost-ledger row")


def apply_override(ap, a):
    """Set the override from parsed --uncallable-family/--uncallable-family-reason for this process and its
    children, then refuse a `--model` (a.model) of a family the override does not name. A model equal to the
    parser's default is left to the call, so a tool's own default (and a dry run under it) is not refused at
    the arguments."""
    family, reason = getattr(a, "uncallable_family", None), (getattr(a, "uncallable_family_reason", None) or "").strip()
    if family is not None or reason:
        if not family or not reason:
            ap.error("--uncallable-family and --uncallable-family-reason go together, and the reason must not be empty")
        if is_callable(family):
            ap.error(f"--uncallable-family {family}: the family is callable; no override is needed")
        os.environ[UNCALLABLE_ENV], os.environ[UNCALLABLE_REASON_ENV] = family, reason
    if getattr(a, "model", None) and a.model != ap.get_default("model"):
        try:
            require_callable(a.model)
        except NotCallable as ex:
            ap.error(str(ex))


def selected_model(family, kind=None):
    """The model pinned for the family (and kind), or None when families.json pins none."""
    return load(kind)["models"].get(family)


def require_selected_model(model):
    """Refuse a model other than its family's pinned one: a family's log slot holds one model."""
    selected = selected_model(family_of(model))
    if selected and model != selected:
        raise ValueError(f"selected model is {selected!r}, not {model!r}; see families.json")


def family_of(model):
    return model.split("-")[0].lower()


def stem(form, family=DEFAULT):
    """The file stem of a form's log for a family."""
    return form if family == DEFAULT else f"{form}.{family}"


def split_stem(name):
    """(form, family) from a log's file stem; a stem without a dot is the Claude family's."""
    form, dot, family = name.partition(".")
    return (form, family) if dot else (form, DEFAULT)


def fixture_name(family=DEFAULT):
    return "classm.json" if family == DEFAULT else f"classm.{family}.json"


def case_id(job_id, family=DEFAULT):
    """The fixture case id for a class M job; a second family's cases are suffixed so no two
    families' cases share an id."""
    return job_id if family == DEFAULT else f"{job_id}.{family}"
