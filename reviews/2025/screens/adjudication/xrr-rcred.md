# Screen and false-no adjudication, release rerun (xrr, family rcred)

Ruled by the rcred fork (claude-opus-5-5, judgment). These are the new samples (one per unit, Claude only) of the
family's units whose subject changed in the xint integration. Each finding was checked against `sources/2025/*.txt`,
the form YAML and the interview wording. The earlier xrel rulings of the same units were rechecked against the current
lines. Fragments: `/tmp/xrr/frag/rcred.screens.json` and `/tmp/xrr/frag/rcred.false_no.json` (empty: no false-no item of
the family is unruled); `xrr.py merge` (validate only) prints no REFUSED line. `rulings.json` was not edited.

## Screens

Samples: 3. Findings: 6. Classes: accepted WIDE 5, defect 1 (an existing entry, BUG-0873). No new bug.

| sample | findings (n: class) | disposition |
|---|---|---|
| `f2441.mfs_spouse_deemed#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect; WIDE only. A Yes refuses at f2441.line19, so a spouse at an internet-only or correspondence school, or one whose earnings exceed the deemed amount, is refused, which is safe |
| `s8812.combat_pay#1` | 0: accepted WIDE | no gate defect; WIDE only. Combat pay refuses wherever it can matter (f2441 lines 4, 5, 18 and 19; EIC Step 5 line 4; Schedule 8812 Earned Income Worksheet line 1b), so a filer for whom it changes nothing is refused unnecessarily |
| `gate:f8853c.has_periodic#1` | 0: defect (BUG-0873); 1: accepted WIDE; 2: accepted WIDE | defect (wording) recorded. Line 24's "paid back to you" is still narrower than "received or expect to receive" (BUG-0873, medium, unfixed). Asking line 22 when line 21 controls costs one question. A Method 1 rate change is refused, which is safe |

## False-no

No unruled false-no items in family rcred. All 96 items in the work list were already ruled.

## Items not ruled

None. The work list had no items of kind `due` or `short` for this family.
