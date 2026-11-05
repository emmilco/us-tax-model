# Household credit tables: one for your spouse if married filing joint return

- Table: `ny_hh_spouse_count` (keyed)
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "plus one for you (and one for your spouse if Married filing joint return) is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

Rows: 5; keys: status (Enum(filing_status)); entry: Count

| status | Entry |
| --- | --- |
| single | 0 |
| mfj | 1 |
| mfs | 0 |
| hoh | 0 |
| qss | 0 |
