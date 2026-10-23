# Human reading packets

The reading list of the integrity plan (item 1.1) as data, a packet per item for a person to read the project's lines against the archived IRS pages, and a local server that saves what the reader types into `reviews/<year>/human/<form>.md`.

## Usage

1. `python3 tools/human_review/packet.py --all` writes one HTML per item to the git-ignored `.human-review/` (`--item N` for one; `--list` for the counts). Pages are rendered once with `pdftoppm` into `.human-review/pages/`; `--force` re-renders.
2. `python3 tools/human_review/serve.py` serves `.human-review/` at `http://127.0.0.1:8790/` (`--port` to change).
3. Open an item. The right pane has one card per **printed** line: the IRS label as printed, the citation with its quotes verbatim, the reading English (what the encoding computes, in page terms), the refusal gates, a worked example from the fixtures, the YAML under "show expression", and the verdict box. The left pane shows the pages that line's citation names (click a card, or a page link in it); the cited quote, heading or printed line number is highlighted on the image, and the caption under each image says what was located and what was not. Choose MATCH / MISMATCH / UNCLEAR and write the reason in your own words. Type your own name as the reader; the page never fills it in.
4. "Save verdicts" POSTs to the server, which writes or updates `reviews/<year>/human/<form>.md`, one log per form, merged by line id when several items touch one form. A draft is also kept in the browser until saved.
5. Commit the logs yourself: `check_logs.py` requires the commit author to equal the reader field.

`reading_list.json`: for each item its id, title, lines (`<form>.<id>`; a def's bare id after its form, as `se.line2`; `tax_table.band_<at_least>` for one Tax Table cell) and the documents and pages the list was drawn from. Edit it when the plan's list changes. The ids stay as they are; the packet decides what is judged (below).

## What the packet judges: printed lines, helpers folded

A line is printed when its `printed` is none of `(helper)`, `(gate)`, `(computed helper)`, `(screen)`, `(question)`. Only printed lines get a verdict box. A listed helper is folded into the printed line that reads it: its expression is expanded in the reading English, its citation's pages join the line's pages. When no listed printed line reads a listed helper (item 2 lists only helpers), the packet walks up the readers of that helper to the nearest printed line and judges that one, marked "Not itself on the reading list"; among several at the same distance it prefers the one whose reading covers the most of the item's lines, then one cited in the item's documents, then the one that drags in the fewest lines outside the item. A listed helper that no chosen printed line reads is shown at the end under "helpers used only by other items", with its reading and no verdict box. `packet.py --list` prints, per item, how many printed lines are judged, how many helpers are folded and how many listed helpers go unread.

The modules: `reading.py` (the canonical JSON read as English, one literal template per atom; printed lines named "line N of <form> (“label”)", inputs by their interview question, parameters by amount and name; a compound helper gets a letter tag whose definition follows), `pages.py` (the citation's segments through `tools/citations.py`; a page segment's pages, a form-line locator's page by the same `line_beside_label` rule; word boxes from `pdftotext -bbox-layout`, rectangles drawn with PIL on a copy of the page image under `.human-review/pages/hl/`), `examples.py` (the fixture case asserting the line with the most nonzero values among what it reads, evaluated with `engine eval --batch`). A span, list or title-only locator is flagged on the card as locating no page, and the document's pages are offered when it has at most four.

## What the log records

## The list: two dozen items, how they were chosen

The list holds 26 items (item 13 optional). Items 1 to 13 are the plan's original reading list (item 1.1 of `docs/2026-10-22_integrity_plan.md`); items 14 to 26 double it under the plan's stop rule (the owner's decision 13, after the rule fired on 2026-10-22). Every item was chosen by the same rule, stakes times churn: stakes are the dollars and the share of returns a line touches (IRS Statistics of Income, tax year 2023, archived under `sources/2025/soi-*`), churn is the number of commits touching the form file (`git log --oneline -- forms/2025/<form>.yaml | wc -l`). No line appears in two items.

Items 14 to 26 further prefer, in order: (a) lines no engine reaches, so that until a person reads them their only evidence is from one model family (the E column of `reports/2025/evidence.md`; the mapped lines of `reports/2025/engine_differential.md`); (b) the forms the Direct File comparison (plan item 1.7) could not cover; (c) the lines the citation check lists under "Locators to rewrite" in `reports/2025/citations.md`, whose citations are the weakest. Form 8606 Part I was weighed and set aside (six lines, one commit, no IRS count). The owner reads items 1 to 12 first (decision 13).

## What the log records

A header table (date, reader, items, subject kind and sha256, lines judged, the verdict counts), the source pages read (document, revision, pages, text sha256, cols sha256, as the render logs record them; the pages are those the printed lines' citations and their folded citations name), then per printed line its printed number and id, the IRS label, the reading English read (flattened to one line, a tagged definition in brackets), the citation, the pages, the helpers folded into it, the item, and the reader's verdict and reason verbatim. Every entry is a printed line, so `check_logs.py`'s rule that every line carries a verdict holds; a folded helper is judged with its printed line and named on the entry's `Helpers folded` field.

The subject is the `render` kind of `tools/transcription/subjects.py`: the sha256 of `rendered/<year>/<form>.md` with its citations masked. The reading English is generated from the canonical JSON, which that file renders from the same source, so a human log goes stale exactly when a render log would; the subject exists for every form and table on the list, and `check_logs.py` already knows how to recompute it.

`tools/transcription/check_logs.py` checks every human log present (none is required): subject current, every line with a verdict and a reason, a reader who is not a model (`/claude|gpt|deepseek|model|agent/i`), and, once committed, a last commit author equal to the reader.

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
