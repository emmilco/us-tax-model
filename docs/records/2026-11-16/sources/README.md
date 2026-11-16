# Fetched IRS sources for BUG-0805 and BUG-0901 (lane fetch-sources, 2026-11-16)

Nothing was written inside the repository. The files here are plain downloads. The archive copies are not made yet.

## What was fetched

All by curl with a generic User-Agent ("Mozilla/5.0"). sha256 is of the PDF bytes. Text is `pdftotext -layout`, the same tool the project uses for `<id>.txt`. The project's reading-order files (`.cols.txt`, `.pages.json`) were not built, because `--derive` writes into the repo.

| File here | URL | Printed edition / date | Pages | Bytes | sha256 |
|---|---|---|---|---|---|
| p936.pdf / .txt | https://www.irs.gov/pub/irs-pdf/p936.pdf | "Publication 936 (2025) Catalog Number 10426G", Oct 28, 2025 | 23 | 1353191 | a4ef802b92ddd40ce2d00331b5012834dd274fd6ce74624586a1ea7dc31c32de |
| i1040sh.pdf / .txt | https://www.irs.gov/pub/irs-pdf/i1040sh.pdf | "Instructions for Schedule H (Form 1040) (2025) Catalog Number 21451X", Dec 1, 2025 | 11 | 254570 | 3e4b07dd0867386395ea6bd162e5c2cbc172cbd350dcee66d1eaf1ea05e67f7a |
| p926-2025.pdf / .txt | https://www.irs.gov/pub/irs-prior/p926--2025.pdf | "Publication 926 (2025) Catalog Number 64286A", Dec 17, 2024 | 18 | 1250568 | 1e25a16919cb96ef49aa6fef40cd3aa99b5009427bf5cc7067c5127c97ddf2b7 |
| p926-2026.pdf / .txt (for reference only) | https://www.irs.gov/pub/irs-pdf/p926.pdf | "Publication 926 (2026) Catalog Number 64286A", Nov 24, 2025 | 18 | 1292919 | db57fe2911bc0baec40339cd898a2594e28d86eb033f13052786d12fee23e5e7 |

Key finding on Pub. 926: the current irs-pdf/p926.pdf is the 2026 edition ("For use in 2026"; wage threshold $3,000). The 2025 edition, which applies to wages paid in 2025 (threshold $2,800, matching the 2025 Schedule H instructions), is only at the irs-prior address above (HTTP 200). `irs-pdf/p926--2025.pdf` and `p936--2024.pdf` return 404. The current p936.pdf and i1040sh.pdf are the 2025 editions. `raw/` holds the response headers and intermediate files; ignore it. I also downloaded irs-prior p926--2024 and p936--2024 into raw/ (not needed).

## How to add them tomorrow (project method; read from tools/fetch_sources.py and sources/2025/manifest.json)

Mechanism, checked in tools/fetch_sources.py: the catalog is `tools/sources/2025.json` (a list of `{id, title, designation, url}`), the fetch only runs with `--fetch`, and the host must be www.irs.gov (no path restriction for `us`). With `--fetch --only <id>` it downloads, runs pdftotext, derives the reading-order pair, and appends a manifest entry with `revision: null` and `revision_status: "Pending inspection of archived document; not cleared for encoding"` (fetch_sources.py around line 385). The revision fields are then filled by hand.

1. Append to `tools/sources/2025.json` (near p501/p502/p526; shape copied from the p501 entry):
```json
{"id": "p936", "title": "Home Mortgage Interest Deduction", "designation": "Publication 936", "url": "https://www.irs.gov/pub/irs-pdf/p936.pdf"},
{"id": "p926", "title": "Household Employer's Tax Guide", "designation": "Publication 926 (2025 edition)", "url": "https://www.irs.gov/pub/irs-prior/p926--2025.pdf"},
{"id": "i1040sh", "title": "Instructions for Schedule H (Form 1040)", "designation": "Instructions for Schedule H (Form 1040)", "url": "https://www.irs.gov/pub/irs-pdf/i1040sh.pdf"}
```
   (Use the irs-prior URL for p926: the current URL now serves the 2026 edition, which would be the wrong tax year.)
2. Run `python3 tools/fetch_sources.py --fetch --only p936 p926 i1040sh` (add `--jurisdiction us` is the default). Then `python3 tools/fetch_sources.py --derive` if the fetch did not already build the reading-order files, and run it with no flag to verify offline.
3. Check the fetched hashes equal the ones above (a changed hash means IRS reposted; re-read the printed date).
4. Set the manifest fields by hand, in the style of the existing entries (p501: `"revision": "2025 returns; PDF created 2026-02-04"`; i1040sd: `"revision": "2025; printed date 2025-12-11"`):
```
p936:    "revision": "2025; printed date 2025-10-28",  "revision_status": "Printed year/revision inspected in extracted text; content review is tracked separately in PREMISES.md",  "revision_locator": "PDF page 1, printed heading and footer"
p926:    "revision": "2025 edition; printed date 2024-12-17 (irs-prior archive copy; current irs-pdf copy is the 2026 edition)", same status, locator "PDF page 1, printed footer 'Publication 926 (2025)'"
i1040sh: "revision": "2025; printed date 2025-12-01", same status, locator "PDF page 1, printed footer"
```
(Inferred, not checked: whether `check_all` requires PREMISES.md rows for new sources; read tools/README.md "sources" section before running.)

## Passages (PDF page = printed page number for p936 and the Schedule H instructions; checked by reading the extracted text)

### Pub. 936 (2025), for BUG-0805 ("substantially improve")
- p. 1, Reminders: "Home equity loan interest. No matter when the indebtedness was incurred, you can no longer deduct the interest from a loan secured by your home to the extent the loan proceeds weren't used to buy, build, or substantially improve your home."
- p. 12, "Cost of home or improvements" and the definition: "The cost of building or substantially improving a qualified home includes the costs to acquire real property and building materials, fees for architects and design plans, and required building permits. **Substantial improvement.** An improvement is substantial if it: • Adds to the value of your home, • Prolongs your home's useful life, or • Adapts your home to new uses. Repairs that maintain your home in good condition, such as repainting your home, aren't substantial improvements. However, if you paint your home as part of a renovation that substantially improves your qualified home, you can include the painting costs in the cost of the improvements." (The last two sentences straddle pp. 12 and 13.)
- p. 3 (flowchart): mortgages after Oct 13, 1987 count only if "used to buy, build, or substantially improve the main home secured by that main home mortgage" or the second home.
- p. 8, points: "If the loan is a home equity, line of credit, or credit card loan and the proceeds from the loan are not used to buy, build, or substantially improve the home, the points are not deductible." Points on a home improvement loan to "substantially improve your main home" are deductible in the year paid (same page, "Deduction Allowed in Year Paid").
- Other mentions of the phrase, not read in full: pp. 2, 4, 7, 9, 10, 11, 15, 16, 22.

### Pub. 926 (2025 edition, Dec 17, 2024), for BUG-0901 (agencies, registries)
- p. 3, "Do You Have a Household Employee?": "You have a household employee if you hired someone to do household work and that worker is your employee. The worker is your employee if you can control not only what work is done, but how it is done. If the worker is your employee, it doesn't matter whether the work is full time or part time or that you hired the worker through an agency or from a list provided by an agency or association. It also doesn't matter whether you pay the worker on an hourly, daily, or weekly basis, or by the job."
- p. 4: "If an agency provides the worker and controls what work is done and how it is done, the worker isn't your employee." Same page: "A self-employed worker usually provides their own tools and offers services to the general public in an independent business. A worker who performs childcare services for you in their home generally isn't your employee." Also the lawn-care example (worker runs a business; neither the worker nor helpers are your employees). Cross-reference: "section 1 of Pub. 15-A".
- The 2026 edition (Nov 24, 2025) has the same sentences on pp. 3 and 4 (checked by search). The 2025 threshold is $2,800 (p. 6); the 2026 edition says $3,000.

### Instructions for Schedule H (2025), p. 2
- "Did you have a household employee? If you hired someone to do household work and you could control what work they did and how they did it, you had a household employee. This is true even if you gave the employee freedom of action. What matters is that you had the right to control the details of how the work was done."
- "If a worker is your employee, it doesn't matter whether the work is full or part time or that you hired the worker through an agency or from a list provided by an agency or association."
- Section 3504 agent: "If you're a home care service recipient receiving home care services through a program administered by a federal, state, or local government agency, and the person who provides your care is your household employee, you can ask the IRS to authorize an agent under section 3504 to report, file, and pay all federal employment taxes, including FUTA taxes, on your behalf. See Form 2678 ... If a government agency or third-party agent reports and pays the employment taxes on wages paid to your household employee on your behalf, you don't need to file Schedule H to report those taxes."
- "**Workers who aren't your employees.** Workers you get from an agency aren't your employees if the agency is responsible for who does the work and how it is done. Self-employed workers are also not your employees. A worker is self-employed if only the worker can control how the work is done."
- Reading (inferred): the test is control over how the work is done, not the hiring channel. An agency or registry placement (a "list provided by an agency or association") still gives a household employee if the taxpayer controls the work; an agency that controls who does the work and how makes the worker the agency's, so no Schedule H wages. No text found that mentions "registry" by name.
