# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f9cadca04d9e5e18eb58daed409e9a2ad083e02db1396dc5244b18b5f295a6ab |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 794d904fecdb03bb84fe5c70e45b1b159c22bb13125a24b3e1599ea189c04c1e |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 962700f91d1deda91ef176514fe78170d81855f2dc066437eb99609060c21cff |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, household, s1, sa, scope, scveh |
| named line | s8812 |
| shared page | person, sc |

## Lines

### ltc.amount — The smaller of (a) or (b)
Status: **AGREE**
Reviewed in: pass a6e279fd56be

### 2(b) — The amount for that person's age
Status: **AGREE**

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| ltc.amount | b9f8b3c8c6c16ccd6092cf9322764a44272696af9b92ec7a17d40bacede0d79e |
| 2(b) | be1bc3486c4ac604c2230b183e578bff0751dbaab1c1ee0190d642a68419b0e2 |
| (rest of the document) | d7dc454d6b46478b770b8f3bc4c29597a7902f0a42eba92c01e52c69c90a55c8 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| ltc.amount | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass a6e279fd56be

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines ltc.amount |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a6e279fd56bee0a36a7e4f5e9842b3c29db830cb712dd3f7166751d3b4561140 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 122608d0d9b51a49c67e836c1dcd69f59b7a3e131ace25b4dc3ad07e0efd0f92 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d8094f21afe69370cc498d708f50b148438b27223e7c16763c0f342c19c6cb78 |
| receipt | .transcription/ltc.deepseek.lines-c8be3b200627 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: s1.alimony, s1.alimony_paid, s1.alimony_received, s1.alimony_unsupported, s1.cod_amount, s1.cod_any, s1.cod_unsupported, s1.gambling_pro, s1.gambling_winnings, s1.jury_to_employer, s1.line15, s1.line16, s1.line17, s1.line8_other, s1.line8g, s1.line8h, s1.line8i, s1.line8j, s1.line8r, s1.uc_paid, s1.uc_repaid, s1.uc_unsupported | s1 |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | s8812 |
| shared page | person, sc |

##### Raw second transcription

```yaml
lines:
  - id: ltc.amount
    printed: "(helper)"
    label: "Qualified long-term care insurance amount for this person: the smaller of the premiums paid (line 2(a)) and the age-based limit (line 2(b))"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ltc.payments
        - ltc.limit
```

## Raw second transcription

```yaml
lines:
  - id: ltc.limit
    printed: "2(b)"
    label: "The amount shown below. Use the person's age at the end of the tax year."
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: ltc_limit
      keys:
        - ltc.age
  - id: ltc.amount
    printed: "(helper)"
    label: "For coverage under a qualified long-term care insurance contract, enter for each person covered the smaller of (a) or (b)."
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ltc.payments
        - ltc.limit
```
