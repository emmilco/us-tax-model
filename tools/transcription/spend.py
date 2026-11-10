#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""The owner's cost gate for paid review runs, shared by every tool that plans paid calls (rerun_all.py,
completeness_review.py, screen_review.py).

A planned job is a dict with `run` (bool), `usd` (the estimate, or None when the ledger cannot price it), and
`kind` and `form` (named in refusals). A run whose estimate exceeds COST_GATE_USD, or that includes calls the
ledger cannot price, is refused unless --approve-cost DOLLARS is at least the estimate.

The estimate prices a request's prompt characters at the recent cost per prompt character of the same tool and
model family in the cost ledger (.transcription/costs.jsonl).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402

COST_GATE_USD = 3.00     # an estimated run above this needs --approve-cost
PRICE_SAMPLE = 30        # recent ledger calls per (tool, family) that set the price per prompt character
REASON_ENV = "REVIEW_RERUN_REASON"   # transcribe.record_cost writes it into the ledger row


def prices(ledger=None):
    """{(tool, family): estimated USD per prompt character} over the most recent PRICE_SAMPLE priced,
    successful calls of each tool and family in the cost ledger."""
    import costs
    import transcribe
    rows, _ = costs.read(ledger or os.path.join(transcribe.RAW, transcribe.LEDGER_NAME))
    groups = {}
    for r in rows:
        if r.get("outcome") == "ok" and r.get("estimated_cost_usd") is not None and (r.get("prompt_chars") or 0) > 0:
            groups.setdefault((r.get("tool"), families.family_of(r.get("model_requested") or "-")), []).append(r)
    out = {}
    for key, rs in groups.items():
        rs = sorted(rs, key=lambda r: r.get("timestamp", ""))[-PRICE_SAMPLE:]
        out[key] = sum(r["estimated_cost_usd"] for r in rs) / sum(r["prompt_chars"] for r in rs)
    return out


def estimate(chars, tool, model, price):
    """USD for a request of `chars` prompt characters, or None when the ledger has no price for the tool and family."""
    rate = price.get((tool, families.family_of(model)))
    return None if chars and rate is None else chars * (rate or 0)


def gate(planned, approve):
    """None when the run may proceed, else the refusal: an estimate above COST_GATE_USD, or calls the
    ledger cannot price, need --approve-cost of at least the estimate."""
    total = sum(j["usd"] or 0 for j in planned if j["run"])
    unpriced = [j for j in planned if j["run"] and j["usd"] is None]
    if unpriced and approve is None:
        return (f"{len(unpriced)} job(s) have no ledger price for their tool and family "
                f"({', '.join(j['kind'] + ' ' + j['form'] for j in unpriced)}); pass --approve-cost DOLLARS to run them")
    if total > COST_GATE_USD and (approve is None or approve < total):
        return (f"estimated ${total:.2f} exceeds the ${COST_GATE_USD:.2f} gate; pass --approve-cost {total:.2f} "
                "(or more) to run it")
    return None
