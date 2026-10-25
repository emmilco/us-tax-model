"""Model families and the names their review artifacts take.

A family is the first token of a model name (`claude-opus-5-5` -> `claude`, `deepseek-v4-pro`
-> `deepseek`). The Claude family's logs keep their plain names; a second family's review of
the same form sits beside them:

  reviews/<year>/<kind>/<form>.md                      the Claude log and <form>.rulings.json
  reviews/<year>/<kind>/<form>.<family>.md             a second family's log and <form>.<family>.rulings.json
  fixtures/<year>/classm.json / classm.<family>.json   class M fixtures per family; a second family's
                                                       case ids carry the family as a suffix

`families.json` lists the families check_logs.py requires a current log from for every form and
those it checks only when a log is present.
"""
import json
import os

DEFAULT = "claude"
LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "families.json")


def load(kind=None):
    """Family requirements and selected models, with optional per-kind overrides."""
    data = json.load(open(LIST, encoding="utf-8"))
    models = dict(data.get("models", {}))
    if kind is not None:
        data = data.get("by_kind", {}).get(kind, data)
        models.update(data.get("models", {}))
    return {"required": list(data.get("required", [])), "optional": list(data.get("optional", [])), "models": models}


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
