# Extraction conservation checks

Offline checks that the archived IRS text is a faithful reading of the archived PDFs (tools/check_extraction.py). Words are compared as lower-case alphanumeric tokens per page, characters where spacing differs. The layout text and the reading-order text come from the same line boxes and must agree exactly; PDFKit reads the text layer independently of poppler and can only show what poppler lacks; the HTML snapshot is the IRS's own second publication of the instructions.

| check | documents | failing |
| --- | --- | --- |
| layout vs reading order | 6 | 0 |
| PDFKit against poppler | 6 | 0 |
| PDF vs HTML snapshot | 1 | 0 |

## Per document

- **ny_it2** layout vs reading order: 2 pages, identical characters
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (1 such occurrences; 2 words poppler reads that PDFKit skips)
- **ny_it201** layout vs reading order: 4 pages, identical characters
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (0 such occurrences; 0 words poppler reads that PDFKit skips)
- **ny_it201att** layout vs reading order: 2 pages, identical characters
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (0 such occurrences; 0 words poppler reads that PDFKit skips)
- **ny_it201i** layout vs reading order: 41 pages, identical characters (4 page(s) differ only in word spacing)
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (26 such occurrences; 64 words poppler reads that PDFKit skips)
    - HTML snapshot `ny_it201i-html`: every word of every page occurs in the HTML text, 6 page(s) excepted
        - p. 25 accepted: ['dollars', 'john', 'maple', 'pl', 'sa', 'smith'] — Sample check illustration (line 83, direct deposit: JOHN SMITH, 999 Maple Street, Someplace, the rotated word 'Sample', Dollars); the HTML publication carries it as an image, so its text is not in the snapshot
        - p. 35 accepted: ['agi'] — Running heading 'Tax computation – New York AGI of more than $107,650 (continued)' on a continuation page of the tax computation worksheets; the HTML publication prints the section once, without the continuation heading
        - p. 36 accepted: ['agi'] — Running heading 'Tax computation – New York AGI of more than $107,650 (continued)' on a continuation page of the tax computation worksheets; the HTML publication prints the section once, without the continuation heading
        - p. 37 accepted: ['agi'] — Running heading 'Tax computation – New York AGI of more than $107,650 (continued)' on a continuation page of the tax computation worksheets; the HTML publication prints the section once, without the continuation heading
        - p. 38 accepted: ['agi'] — Running heading 'Tax computation – New York AGI of more than $107,650 (continued)' on a continuation page of the tax computation worksheets; the HTML publication prints the section once, without the continuation heading
        - p. 39 accepted: ['agi'] — Running heading 'Tax computation – New York AGI of more than $107,650 (continued)' on a continuation page of the tax computation worksheets; the HTML publication prints the section once, without the continuation heading
- **ny_it270i** layout vs reading order: 1 pages, identical characters
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (0 such occurrences; 0 words poppler reads that PDFKit skips)
- **ny_tax_law_601** layout vs reading order: 58 pages, identical characters
    - PDFKit: no page where PDFKit reads words poppler lacks beyond tolerance (0 such occurrences; 0 words poppler reads that PDFKit skips)
