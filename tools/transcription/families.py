"""Model families and the names their review artifacts take.

A family is the first token of a model name (`claude-opus-5-5` -> `claude`, `deepseek-v4-pro`
-> `deepseek`). The Claude family's logs keep their plain names; a second family's review of
the same form sits beside them:

  reviews/<year>/<kind>/<form>.md                      the Claude log and <form>.rulings.json
  reviews/<year>/<kind>/<form>.<family>.md             a second family's log and <form>.<family>.rulings.json
  fixtures/<year>/classm.json / classm.<family>.json   class M fixtures per family; a second family's
                                                       case ids carry the family as a suffix

`families.json` lists the families check_logs.py requires a current log from for every form, those it
checks only when a log is present, and whether each family is active. An inactive family's logs and
fixtures are history: no review tool calls its model, and check_logs.py does not require or fail them.
Reactivating a family is setting its `active` flag to true. A single deliberate run of an inactive
family needs the override (`--inactive-family FAMILY --inactive-family-reason TEXT` on the review tools
and rerun_all.py), and each paid call it makes records the reason in its cost-ledger row.
"""
import json
import os

DEFAULT = "claude"
LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "families.json")
OVERRIDE_ENV = "REVIEW_INACTIVE_FAMILY"            # the inactive family a deliberate run may call
OVERRIDE_REASON_ENV = "REVIEW_INACTIVE_FAMILY_REASON"  # its reason, written into each cost-ledger row


class InactiveFamily(ValueError):
    """A model of an inactive family was called without the override that names it."""


def load(kind=None):
    """Family requirements and selected models, with optional per-kind overrides."""
    data = json.load(open(LIST, encoding="utf-8"))
    models = dict(data.get("models", {}))
    if kind is not None:
        data = data.get("by_kind", {}).get(kind, data)
        models.update(data.get("models", {}))
    active = json.load(open(LIST, encoding="utf-8")).get("active", {})
    return {"required": list(data.get("required", [])), "optional": list(data.get("optional", [])), "models": models,
            "active": {f: bool(on) for f, on in active.items()}}


def is_active(family):
    """Whether the family's reviews run and its logs are checked (families.json `active`; an unlisted family is not)."""
    return load()["active"].get(family, False)


def override():
    """(family, reason) of the inactive-family override this process runs under, else None."""
    family, reason = os.environ.get(OVERRIDE_ENV, "").strip(), os.environ.get(OVERRIDE_REASON_ENV, "").strip()
    return (family, reason) if family and reason else None


def require_active(model):
    """Refuse a model of an inactive family unless the override names that family with a reason."""
    family = family_of(model)
    if is_active(family):
        return None
    granted = override()
    if granted and granted[0] == family:
        return granted
    raise InactiveFamily(f"model family {family!r} ({model}) is inactive in tools/transcription/families.json; "
                         f"run it once with --inactive-family {family} --inactive-family-reason TEXT, "
                         f"or reactivate it by setting its \"active\" flag to true")


def add_override_args(ap):
    ap.add_argument("--inactive-family", metavar="FAMILY", help="allow this run to call an inactive model family (families.json)")
    ap.add_argument("--inactive-family-reason", metavar="TEXT", help="why; recorded in each paid call's cost-ledger row")


def apply_override(ap, a):
    """Set the override from parsed --inactive-family/--inactive-family-reason for this process and its
    children, then refuse a `--model` (a.model) of an inactive family the override does not name."""
    family, reason = getattr(a, "inactive_family", None), (getattr(a, "inactive_family_reason", None) or "").strip()
    if family is not None or reason:
        if not family or not reason:
            ap.error("--inactive-family and --inactive-family-reason go together, and the reason must not be empty")
        if is_active(family):
            ap.error(f"--inactive-family {family}: the family is active; no override is needed")
        os.environ[OVERRIDE_ENV], os.environ[OVERRIDE_REASON_ENV] = family, reason
    if getattr(a, "model", None):
        try:
            require_active(a.model)
        except InactiveFamily as ex:
            ap.error(str(ex))


def selected_model(family, kind=None):
    return load(kind)["models"].get(family)


def require_selected_model(model):
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
