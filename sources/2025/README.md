# TY2025 source archive

This is a partial Stage 0 delivery, paused at the first confirmed scope correction.
No source has yet been transcribed into executable tax rules.

`manifest.json` identifies 32 public IRS PDFs, their extracted text, actual UTC
fetch timestamps, requested/resolved addresses, SHA-256 hashes, and the printed
revision inspected in the extracted text. A printed creation/date line is labelled
as such; it is not represented as an independently verified web posting date.
The hashes identify the exact snapshots even when two releases share a printed
date. The 1099 forms and instructions are continuous-use January 2024 revisions.

`PREMISES.md` distinguishes reviewed findings from pending checks and proposes
the specification correction awaiting the owner's decision. Revision inspection
does not mean the document's tax content has been reviewed in full. Review of
IRS correction notices and any additional sources needed for the remaining
premises is still pending. HTML instruction snapshots have not been collected.

Schedule B includes its instructions in `f1040sb.pdf`. Form 4952 includes its
instructions in `f4952.pdf` (pages 3–4). Instructions for Schedules 2 and 3 are
included in `i1040gi.pdf`. The Form 8995-A sources are evidence for the proposed
scope correction, not authorization to implement that form. Form 1116 instructions
are evidence for the simple-path boundary; Form 1116 remains deferred.

The current W-2 URLs initially returned 2026 documents. Those downloads were
excluded from this archive and replaced with IRS prior-year 2025 URLs. The
catalog also corrects the unavailable combined 1099 instruction address to the
separate interest/OID and dividend instruction PDFs.

Verify every PDF and text hash without network access:

```sh
python3 tools/fetch_sources.py
```

Page locators in the findings refer to one-based PDF pages. The extracted text
retains form feeds. For this delivery, the agent inspected text, not page images;
visual checks of tables and complex layouts remain necessary before encoding.

The IRS publications are source material. Locally authored metadata and premise
findings are dedicated under CC0-1.0, consistent with the project specification.
