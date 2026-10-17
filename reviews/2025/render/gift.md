# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 8c74ff60e608dd574843b5c449277663a57d6b04a865d92b1e18004e2189e121 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees, 
Status: **MATCH**

Model: The instructions define the amount of the deduction as the deduction 'before applying any income limits that could result in a carryover,' after 'any required reductions.' For a group, the filer must 'consider all items in the group, even if items in the group were donated to more than one donee organization.' The input's label matches this.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: Section A includes publicly traded securities 'even if the claimed value was more than $5,000.' The input flag captures that exception. The other security categories in 2.d are only refused more broadly through section_b, which narrows the program but does not misstate the text.

### special — Does this group need an appraisal or other special treatment (including vehicles, pass-thr
Status: **MATCH**

Model: The instructions treat several categories specially: vehicles, intellectual property, inventory, pass-through entity gifts, conservation and partial interests, and 'a single article of clothing or household item that is not in good used condition or better ... over $500' (which needs Section B). The program refuses all of these, so it narrows the supported cases without miscomputing the ones it handles.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The instructions put in Section B items with a deduction 'of more than $5,000' per item or group, excluding Section A items such as publicly traded securities. Those items 'require a written qualified appraisal.' The other Section A exceptions are either caught by the special refusal or refused conservatively, which narrows the program but is not wrong.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: Within the supported cases (Section A only, no special property), the amount reported is the deduction figured before income limits. The refusals name Section B and special-treatment property as the excluded cases.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The instructions define the amount of the deduction as the deduction 'before applying any income limits that could result in a carryover,' after 'any required reductions.' For a group, the filer must 'consider all items in the group, even if items in the group were donated to more than one donee organization.' The input's label matches this."
  - key: "public_securities"
    status: MATCH
    reason: "Section A includes publicly traded securities 'even if the claimed value was more than $5,000.' The input flag captures that exception. The other security categories in 2.d are only refused more broadly through section_b, which narrows the program but does not misstate the text."
  - key: "special"
    status: MATCH
    reason: "The instructions treat several categories specially: vehicles, intellectual property, inventory, pass-through entity gifts, conservation and partial interests, and 'a single article of clothing or household item that is not in good used condition or better ... over $500' (which needs Section B). The program refuses all of these, so it narrows the supported cases without miscomputing the ones it handles."
  - key: "section_b"
    status: MATCH
    reason: "The instructions put in Section B items with a deduction 'of more than $5,000' per item or group, excluding Section A items such as publicly traded securities. Those items 'require a written qualified appraisal.' The other Section A exceptions are either caught by the special refusal or refused conservatively, which narrows the program but is not wrong."
  - key: "allowed"
    status: MATCH
    reason: "Within the supported cases (Section A only, no special property), the amount reported is the deduction figured before income limits. The refusals name Section B and special-treatment property as the excluded cases."
```
