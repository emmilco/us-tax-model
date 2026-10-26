# Internal adapter contracts

These contracts describe project plumbing, not independently transcribed IRS
quantities. They are host-only and earn no H/B/M/engine assertion or source-review
qualification. Their behavior and expected answers never enter blind requests.

`2025/div.json` identifies `div.screen`, a zero-valued adapter after distribution
scope and component checks. A sum of distribution components would violate this
contract even though its type would be valid. Twenty-one engineering cases check
accepted zero/nonzero distribution facts, each refusal regime, component totals,
and genuinely missing answers. Every case checks the adapter and its sixteen
direct worksheet copies. The declared consumer inventory must match the live
copy wiring; a new, removed or rewired copy requires deliberate contract review.
This does not certify the scope or arithmetic of the worksheets consuming it.

Run `python3 tools/transcription/adapter_contracts.py` after compilation. The full
suite also runs it. A fixed interpreter evaluates authored project definitions
in a bounded subprocess (32 cases, 30 seconds, 256-MiB V8 old-space setting).
The source-review type-only checker and the model partial-input checker retain
their separate roles; no candidate is repaired or installed by this check.

Registered internal helpers are omitted from blind transcription targets. When
a document has no source-defined computed targets, `transcribe.py` makes no model
call and produces no empty passing review. Existing dividend replies and their
interface-gap rulings remain historical, unmodified records. Comparison reports
explicitly exclude those adapter rows from source agreement/noise denominators;
an adapter-only document earns no source assertion even if an old log says AGREE.
The read-only audit records the excluded ids without upgrading any receipt.

The registry is deliberately narrow: it currently identifies only `div.screen`.
It does not exempt all helpers, supply adapter formulas to other source requests,
or replace independent review of actual tax quantities. Newly identified opaque
helpers remain interface gaps until their role is resolved explicitly.
