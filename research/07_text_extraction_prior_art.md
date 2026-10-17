# Text extraction: what another PDF-to-text pipeline offers this project

Assessment written 2026-10-17 after reading the extraction and audit
documents of a separate, unpublished PDF-to-text pipeline against the
way this project turns archived IRS PDFs into the text its encoding and its
three model reviews read. Measurements are over the archived `sources/2025/`
texts as of commit `7ad0871`. Tasks T-022 to T-024 came out of it.

## How this project reads its sources

`tools/fetch_sources.py` downloads each IRS PDF, checks the PDF header and
runs `pdftotext -layout` to produce a sibling `.txt`; the manifest records
the hash of both. The review tools (`tools/transcription/`) paste the cited
pages of that text into the prompt. The model never sees an image. The
encoding and the reviews therefore rest on one extraction pass, with no
check on the pass itself.

## What that pipeline does, and why most of it does not transfer

Its sources are scanned or born-digital books. The production path renders
page images, runs a layout detector over them, assigns roles with a bounded
vision-model step, reads text with an OCR engine chosen by a measured
comparison, and enforces a bidirectional conservation net: every word in the
coordinate layer lands in exactly one unit, and every word in a unit is
grounded in coordinate-layer words inside its box. An audit gate of 27
checks and an end-to-end source-to-audio integrity warrant sit downstream.
The layout detector, the OCR engines, the footnote geometry and the audio
alignment answer problems that do not arise with born-digital IRS PDFs,
whose text layer is complete (see below). Their own note records that a
pure born-digital PDF text layer is an untested, strictly easier case for
them.

## What was measured here

| Observation | Value |
| --- | --- |
| Lines on the Stage 8 cited instruction pages (i1040gi pp. 14, 17 to 21, 34, 35) that carry text from both columns | 31% to 56% per page |
| Instruction pages, of 126, where over half the lines do | 52 |
| Distinct words on i1040gi pp. 17 to 19 absent from the HTML snapshot, after hyphen rejoin | 0 (p. 14: only hyphenation fragments such as "circumstan", "ces") |
| Pages of any archived text with fewer than 40 words (a sign of a missing text layer) | none, apart from a near-blank sheet in f4952 and p550 |
| i1040gi pages a naive gutter test calls clean two-column prose (no multi-word block crossing the centre) | 23 of 126; pp. 17 to 21 among them, p. 14 not |
| i1040gi p. 17 under `pdftotext -bbox-layout` | 7 left-column blocks, 21 right-column blocks, none crossing |

`pdftotext -layout` interleaves the booklet's two columns line by line:
left-column prose and right-column flowchart text share each output line.
The model de-interleaves silently and did find BUG-0011 to BUG-0015 on these
pages, but a misattached "AND" or "or" in a flowchart is exactly the error
class the reviews exist to catch, and nothing checks that step. Worksheet
pages (Credit Limit Worksheet A, i1040s8812 p. 4) read well in layout mode
and would be harmed by column splitting; the gutter test marks them as
mixed (13 spanning blocks on that page).

## Constraint

That pipeline is not a dependency of this project and cannot become one.
Anything taken from it is a principle to be rebuilt here from scratch, in
this project's own code, with its own tests; no import, no shared module,
no copied file.

## What transfers

1. **Coordinate-first extraction for two-column prose pages (T-022).** The
   project already uses `pdftotext -bbox-layout` in the Tax Table
   extractor. Emitting per-column reading-order text for pages the gutter
   test calls clean, with a line-break hyphen rejoin, would give the model
   clean prose; layout mode stays for everything else. A per-block ordering
   that keeps spanning blocks in place would extend coverage beyond the 23
   pages and is the larger version. Any change to an archived text changes
   its hash, and every review log pins the hash it read, so this belongs
   with the Stage 6 refetch, when every review is rerun anyway.
2. **A conservation check between independent readings (T-023).** The
   archive already holds a second reading of every instruction booklet, the
   HTML snapshot. A per-page check that every PDF word (hyphens rejoined)
   occurs in the HTML, run offline in `check-all`, costs nothing and catches
   extraction loss on refetch. The forms have no HTML twin; an OCR pass
   would be the independent reading there, at a
   modest one-time cost, and the word profile gives no present reason for
   it.
3. **Decisions as structured data, rendered to prose, never parsed back
   (T-024).** Their pipeline keeps every decision in JSONL and generates
   reports from it. BUG-0016 is the failure that design prevents: rulings
   regex-parsed out of markdown and lost on rerun.

## What was not found

No observed model misreading caused by column interleaving: the risk is
argued from the text, not from a failure in the logs. No text-layer loss
on the pages checked. No reason to adopt an OCR engine, a layout model or a
vision-model step for born-digital sources.
