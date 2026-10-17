# Source archiving (Stage 0)

Run `python3 tools/fetch_sources.py --fetch` deliberately to retrieve the public
IRS PDFs listed in `tools/sources-2025.json`. Python 3, curl and Poppler's
`pdftotext` must already be installed. No packages are downloaded by the script.
Use `--only ID ...` to retrieve a subset. No return data is accepted or sent.

Run `python3 tools/fetch_sources.py` to verify archived PDF and extracted-text
hashes offline and report missing catalog entries. This is an archive integrity
check, not the later implementation's CLI or a tax correctness check.

The manifest records requested and resolved URLs, actual UTC retrieval time,
SHA-256 hashes, and revision review status. Current IRS URLs can change: a
download is **not** automatically considered a TY2025 source. Inspect its printed
year/revision and record that finding in the manifest before citing it for
encoding. Reusable forms may have an older printed revision. Existing snapshots
are preserved; replacing a revision requires a deliberate catalog/archive change.
Extracted text retains page breaks; PDF page numbers can be located by splitting
on form-feed characters. Layout extraction does not replace visual review where
columns or checkboxes matter.

Source PDFs are IRS publications. Script code is Apache-2.0 as required by the
project specification; the source catalog and archive metadata are CC0-1.0.

## Toolchain inspected

The Stage 0 check found Node v24.11.1, npm 11.6.2, Lean 4.29.1 through elan,
Lake 5.0.0 (the installed Lean build), and pdftotext 26.01.0. Python 3 and curl
are also present. No installation was needed. Elan's remote `stable` query
failed in the sandbox but the installed Lean toolchain ran successfully.
No project toolchain is pinned yet; engine/proof configuration belongs to Stage 1.

## Commit guard

`npm run check-all` runs `tools/check_all.sh`, which runs the whole suite
(`npm run check-all-steps`) and, when it passes, writes the hash of the tested
working tree to `.git/check-all-green`. The run counts as green only if nothing
outside the suite's own outputs (`reports/`, `rendered/`) changed while it ran.

`tools/hooks/pre-commit` refuses any commit whose tree is not exactly the
tested tree: no green run, a tree changed since the run, or a partial stage.
Enable it once per clone:

    git config core.hooksPath tools/hooks

`git commit --no-verify` bypasses it; that is a deliberate act, not a routine.
