# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f7dcabf5d889bf8d8435a6f445c10ae49c38ebd728c9a22637f79dd9ef425fa3 |
| lines judged | 18 |
| match / mismatch / unclear / missing | 18 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **MATCH**

Model: The IRS line says "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099". The helper is that same total, entered as an input.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: The IRS line says "Multiply line 1 by 50% (0.50)", which is the same as 1/2. The refusals exclude the Exception cases the IRS sends to Pub. 590-A or Pub. 915, and the lump-sum election in Pub. 915, which the IRS also points to.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: The IRS line says "Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8". The restatement adds the same seven lines, and the signed Dollars type lets a loss on line 7a reduce the total.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: The IRS line says "Enter the amount, if any, from Form 1040 or 1040-SR, line 2a". The restatement enters f1040 line 2a.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: The IRS line says "Combine lines 2, 3, and 4". The restatement adds those same lines.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25; zero i
Status: **MATCH**

Model: The IRS line is the total of Schedule 1, lines 11 through 20, 23 and 25. The program enters $0 and refuses whenever any Schedule 1 income or adjustment applies, so $0 is right for every case it computes.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **MATCH**

Model: The IRS line says to subtract line 6 from line 5 when line 6 is less, and otherwise to stop and enter -0- on line 6b. Entering -0- when the result is zero or less makes every later line work out to -0-, so line 18 ends up the same.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: The IRS amounts are $32,000 for MFJ and $25,000 for single, HOH, QSS, or MFS who "lived apart from your spouse for all of 2025". For MFS who lived with their spouse, the IRS says "skip lines 8 through 15", and the program puts $0 in those skipped lines and handles the case on line 16.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **MATCH**

Model: The IRS line says to subtract line 8 from line 7 when line 8 is less, and otherwise to enter -0- on line 6b. Entering -0- when the result is zero or less gives the same final result.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: The IRS line says "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart". The restatement matches, and MFS living together is a skipped line.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS line says "Subtract line 10 from line 9. If zero or less, enter -0-". The restatement says the same.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 9 or line 10". The restatement says the same.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: The IRS line says "Enter one-half of line 12". Multiplying by 1/2 is the same thing.

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 2 or line 13". The restatement says the same.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: The IRS line says "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-". The restatement uses the same rate, and 85% of zero is already zero.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: The IRS line says "Add lines 14 and 15", and line 8 says that for MFS who lived with their spouse you "multiply line 7 by 85% (0.85) and enter the result on line 16". The restatement covers both cases.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: The IRS line says "Multiply line 1 by 85% (0.85)". The restatement says the same.

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 16 or line 17". When line 1 is $0, line 17 is $0, so the restatement's "No amount" ($0) is the same result.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says \"Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099\". The helper is that same total, entered as an input."
  - key: "2"
    status: MATCH
    reason: "The IRS line says \"Multiply line 1 by 50% (0.50)\", which is the same as 1/2. The refusals exclude the Exception cases the IRS sends to Pub. 590-A or Pub. 915, and the lump-sum election in Pub. 915, which the IRS also points to."
  - key: "3"
    status: MATCH
    reason: "The IRS line says \"Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8\". The restatement adds the same seven lines, and the signed Dollars type lets a loss on line 7a reduce the total."
  - key: "4"
    status: MATCH
    reason: "The IRS line says \"Enter the amount, if any, from Form 1040 or 1040-SR, line 2a\". The restatement enters f1040 line 2a."
  - key: "5"
    status: MATCH
    reason: "The IRS line says \"Combine lines 2, 3, and 4\". The restatement adds those same lines."
  - key: "6"
    status: MATCH
    reason: "The IRS line is the total of Schedule 1, lines 11 through 20, 23 and 25. The program enters $0 and refuses whenever any Schedule 1 income or adjustment applies, so $0 is right for every case it computes."
  - key: "7"
    status: MATCH
    reason: "The IRS line says to subtract line 6 from line 5 when line 6 is less, and otherwise to stop and enter -0- on line 6b. Entering -0- when the result is zero or less makes every later line work out to -0-, so line 18 ends up the same."
  - key: "8"
    status: MATCH
    reason: "The IRS amounts are $32,000 for MFJ and $25,000 for single, HOH, QSS, or MFS who \"lived apart from your spouse for all of 2025\". For MFS who lived with their spouse, the IRS says \"skip lines 8 through 15\", and the program puts $0 in those skipped lines and handles the case on line 16."
  - key: "9"
    status: MATCH
    reason: "The IRS line says to subtract line 8 from line 7 when line 8 is less, and otherwise to enter -0- on line 6b. Entering -0- when the result is zero or less gives the same final result."
  - key: "10"
    status: MATCH
    reason: "The IRS line says \"Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart\". The restatement matches, and MFS living together is a skipped line."
  - key: "11"
    status: MATCH
    reason: "The IRS line says \"Subtract line 10 from line 9. If zero or less, enter -0-\". The restatement says the same."
  - key: "12"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 9 or line 10\". The restatement says the same."
  - key: "13"
    status: MATCH
    reason: "The IRS line says \"Enter one-half of line 12\". Multiplying by 1/2 is the same thing."
  - key: "14"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 2 or line 13\". The restatement says the same."
  - key: "15"
    status: MATCH
    reason: "The IRS line says \"Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-\". The restatement uses the same rate, and 85% of zero is already zero."
  - key: "16"
    status: MATCH
    reason: "The IRS line says \"Add lines 14 and 15\", and line 8 says that for MFS who lived with their spouse you \"multiply line 7 by 85% (0.85) and enter the result on line 16\". The restatement covers both cases."
  - key: "17"
    status: MATCH
    reason: "The IRS line says \"Multiply line 1 by 85% (0.85)\". The restatement says the same."
  - key: "18"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 16 or line 17\". When line 1 is $0, line 17 is $0, so the restatement's \"No amount\" ($0) is the same result."
```
```
