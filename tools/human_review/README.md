# Human reading packets

The reading list of the integrity plan (item 1.1) as data, a packet per item for a person to read the project's lines against the archived IRS pages, and a local server that saves what the reader types into `reviews/<year>/human/<form>.md`.

As of the owner's 2026-10-24 policy revision, packets and ruling samples are optional. See
`docs/2026-10-24_validation_policy.md`. The list remains available; completing it is not a build or
stage-completion requirement. Human evidence still requires the receipt, verdict and author checks.

## Usage

1. `python3 tools/human_review/packet.py --all` writes one HTML per item to the git-ignored `.human-review/` (`--item N` for one; `--list` for the counts). Pages are rendered once with `pdftoppm` into `.human-review/pages/`; `--force` re-renders.
2. `python3 tools/human_review/serve.py` serves `.human-review/` at `http://127.0.0.1:8790/` (`--port` to change).
3. Open an item. The right pane has one card per **printed** line: the IRS label as printed, links to the relevant pages, the reading English (what the encoding computes, in page terms), the refusal gates, a worked example from the fixtures, the YAML under "show expression", and the verdict box. Full citations and their verbatim quotes are under source details. The left pane shows the pages that line's citation names (click a card, or a page link in it); the cited quote, heading or printed line number is highlighted on the image, and the caption under each image says what was located and what was not. Choose MATCH / MISMATCH / UNCLEAR and write the reason in your own words. Type your own name as the reader; the page never fills it in.
4. "Save verdicts" POSTs to the server, which writes or updates `reviews/<year>/human/<form>.md`, one log per form, merged by line id when several items touch one form. A draft is also kept in the browser until saved.
5. Commit your completed logs with yourself as git author. H credit appears after that commit and the next `node engine/dist/main.js evidence` (or `npm run check-all`). H means a human source reading; it supplies no human-calculated expected values and never fills class B. Unsigned or edited logs are shown as pending, with no H credit.

Save requires a verdict and a reason for each submitted line. Blank lines remain browser drafts and do not erase earlier saved entries. MISMATCH and UNCLEAR preserve your concern and earn no H credit; they do not block unrelated validation or report generation. Stale readings also earn no H. Malformed records, duplicate entries, invalid reader identity and incorrect committed authorship still fail record validation. Engineering responses remain separate from your verdicts. Old drafts and saved verdicts are not restored into a changed packet.

`reading_list.json`: for each item its id, title, lines (`<form>.<id>`; a def's bare id after its form, as `se.line2`; `tax_table.band_<at_least>` for one Tax Table cell) and the documents and pages the list was drawn from. Edit it when the plan's list changes. The ids stay as they are; the packet decides what is judged (below).

## Item 2: one short check at a time

The standard-deduction packet has fourteen questions, with just one visible at a time. Each question
shows one computation or input and its own IRS excerpt. References to other amounts are named rather
than recursively expanded. Base amounts, box counts, additions and the final choice are separate
questions. Full source pages remain available under a disclosure.

Your name, a verdict and a brief reason are required. Validation and save feedback appear beside
the navigation; a missing field receives focus. Saving disables duplicate submissions, and a failed
save preserves the current question and notes. After a packet update, old draft notes are restored
but the verdict must be selected again against the updated reading.

Save & next records the completed check; Back revisits it; Skip for now moves on without a verdict.
Save progress stores only completed checks, leaving unfinished writing as a browser draft. Reloading
resumes at the first unfinished question. The reader can stop after any saved check.

Each of these verdicts credits only its own named computation. Reading a base amount does not approve
its use in later calculations; reading the final Form 1040 routing does not approve the upstream rules.
`steps.py` defines presentation boundaries and source excerpts; the reading is generated from the
canonical expression with the other steps' amounts named. No second tax calculator is authored here.

## Other packets: printed lines, helpers folded

A line is printed when its `printed` is none of `(helper)`, `(gate)`, `(computed helper)`, `(screen)`, `(question)`. Only printed lines get a verdict box. A listed helper is folded into the printed line that reads it: its expression is expanded in the reading English, its citation's pages join the line's pages. When no listed printed line reads a listed helper (item 2 lists only helpers), the packet walks up the readers of that helper to the nearest printed line and judges that one, marked as including the intermediate steps selected for review; among several at the same distance it prefers the one whose reading covers the most of the item's lines, then one cited in the item's documents, then the one that drags in the fewest lines outside the item. A listed helper that no chosen printed line reads is shown at the end under "helpers used only by other items", with its reading and no verdict box. `packet.py --list` prints, per item, how many printed lines are judged, how many helpers are folded and how many listed helpers go unread.

The modules: `reading.py` (the canonical JSON read as English, one literal template per atom; printed lines named "line N of <form> (“label”)", inputs by their interview question, parameters by amount and name; a compound helper gets a letter tag whose definition follows), `pages.py` (the citation's segments through `tools/citations.py`; a page segment's pages, a form-line locator's page by the same `line_beside_label` rule; word boxes from `pdftotext -bbox-layout`, rectangles drawn with PIL on a copy of the page image under `.human-review/pages/hl/`), `examples.py` (the fixture case asserting the line with the most nonzero values among what it reads, evaluated with `engine eval --batch`). A span, list or title-only locator is flagged on the card as locating no page, and the document's pages are offered when it has at most four.

## The list: two dozen items, how they were chosen

The list holds 26 optional items. Items 1 to 13 are the original list; items 14 to 26 were added under the former stop-rule decision13. The 2026-10-24 amendment retires that mandatory-reading consequence and any required sequence. The list remains available for voluntary review. Its original selection rule was stakes times churn: dollars and share of returns affected, using archived IRS counts, times commits touching the definition.

Items 14 to 26 originally preferred lines no engine reaches, household predicates outside the Direct File comparison, and coarse citation locators. A missing engine comparison does not itself mean a line now has evidence from only one model family: consult both the per-line evidence report and `reports/2025/second_family.md` for current coverage and gaps.

## What the log records

A header table (date, reader, items, receipt format, lines judged, the verdict counts), the source pages read (document, revision, pages, text sha256, cols sha256, as the render logs record them; the pages are those the printed lines' citations and their folded citations name), then per printed line its printed number and id, the IRS label, the reading English read (flattened to one line, a tagged definition in brackets), its per-line receipt, the citation, the pages, the helpers folded into it, the item, and the reader's verdict and reason verbatim. Every entry is a printed line, so `check_logs.py`'s rule that every line carries a verdict holds; a folded helper is judged with its printed line and named on the entry's `Helpers folded` field.

Each printed record carries a `Review sha256` receipt. `logs.py` hashes the displayed reading,
expanded helpers, referenced input and parameter definitions, their source form files, parameters,
interview wording, source snapshots and reading tools. The browser submits the receipt it displayed;
the server rejects an older packet. Canonical data must match the source definitions before a packet
can be shown or saved. A change in Schedule A therefore stales a Form 1040 reading that expanded it.
The source-page list is selected by the same function as the page images, including the printed form.

`logs.py` supplies the same validation to `check_logs.py` and the engine's evidence report. A MATCH
with a reason earns H only when the exact log contents are committed with the named person as git
author. This is author attribution, not a cryptographic proof of who read the page. For guided questions H credits only that computation; for other packets it credits the
printed line and the helpers expanded in its reading, with links naming the reader and the printed
line that covered each helper. It does not credit other printed lines merely referenced by number.
Second-family transcription/render readings remain in `second_family.md`; they are not yet wired
into the scoreboard.

## Verification

`python3 tools/human_review/test_review.py` runs the complete save/sign/report path and its failure
cases in a temporary repository. Invented test verdicts never enter this repository's human logs.
This regression test currently uses the archived TY2025 standard-deduction packet and runs in
`check-all`. The evidence step runs after the engine differential, so it reads that run's summary.

For a browser smoke test, run a separate headless Chrome with remote debugging on port 9227 and
start the normal review server on 8790, then run `node tools/human_review/test_browser.mjs`. It checks
desktop and phone layouts and source images on the real blank packet, then saves a synthetic
verdict, reloads it, commits it and checks H credit in an isolated temporary repository on an automatically assigned local port.
The test writes desktop and phone screenshots to `/private/tmp/tax-human-review-*.png`.

## Reading on a tablet through lab-server

`serve.py --uds <socket>` listens on a Unix socket instead of 127.0.0.1, which is the dynamic-app shape `~/Documents/GitHub/lab-server/README.md` ("Adding an app") expects. The entry would be:

```toml
[apps.tax-reading]
working_dir   = "/Users/elliotmilco/Documents/GitHub/tax-formalization"
start_command = "python3 tools/human_review/serve.py --uds /Users/elliotmilco/.lab-sockets/tax-reading.sock"
health_path   = "/index.html"
enabled       = true
```

The socket name must match the section name; DNS is a manual CNAME per that README. It is not registered; build the packets first, since the server only serves what `.human-review/` holds.
