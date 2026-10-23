# Human reading packets

The reading list of the integrity plan (item 1.1) as data, a packet per item for a person to read the project's lines against the archived IRS pages, and a local server that saves what the reader types into `reviews/<year>/human/<form>.md`.

## Usage

1. `python3 tools/human_review/packet.py --all` writes one HTML per item to the git-ignored `.human-review/` (`--item N` for one; `--list` for the counts). Pages are rendered once with `pdftoppm` into `.human-review/pages/`; `--force` re-renders.
2. `python3 tools/human_review/serve.py` serves `.human-review/` at `http://127.0.0.1:8790/` (`--port` to change).
3. Open an item, read each line against the page image (every citation has a "show page" link), choose MATCH / MISMATCH / UNCLEAR and write the reason in your own words. Type your own name as the reader; the page never fills it in.
4. "Save verdicts" POSTs to the server, which writes or updates `reviews/<year>/human/<form>.md`, one log per form, merged by line id when several items touch one form. A draft is also kept in the browser until saved.
5. Commit the logs yourself: `check_logs.py` requires the commit author to equal the reader field.

`reading_list.json`: for each item its id, title, lines (`<form>.<id>`; a def's bare id after its form, as `se.line2`; `tax_table.band_<at_least>` for one Tax Table cell) and the documents and pages shown. Edit it when the plan's list changes.

## What the log records

A header table (date, reader, items, subject kind and sha256, lines judged, the verdict counts), the source pages read (document, revision, pages, text sha256, cols sha256, as the render logs record them), then per line its printed number and id, the IRS label, the rendered English read, the citation, the item, and the reader's verdict and reason verbatim.

The subject is the `render` kind of `tools/transcription/subjects.py`: the sha256 of `rendered/<year>/<form>.md` with its citations masked. It is what the packet shows (the rendered English and the expression both come from that file), it exists for every form and table on the list, and `check_logs.py` already knows how to recompute it, so a human log goes stale exactly when a render log would.

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
