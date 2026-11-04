# Proposed bug entries (package p4-docs)

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1 — The register entry `amb.2025.dc_born_died_half_year` records a reading the encoding no longer uses

- **Caught by:** T-095 premise check, 2026-11-03. Each unlinked register entry was compared with the lines it names.
- **Source:** p503 p. 3, Birth or death of otherwise qualifying person: "a person who was born or died in 2025 is treated as having lived with you for more than half of 2025 if your home was the person's home more than half the time they were alive in 2025".
- **Symptom:** the entry's `chosen` says "The second, as encoded (no question is added); it can only leave out a qualifying person". That second reading is "The dependent tests' answer stands, so such a person may not be counted". But since BUG-0157, `dependent.dc_disabled_qp` reads `dependent.dc_lived_half`. That line counts a person other than a qualifying child who was born or died in 2025, through `dependent.born_died` and `dependent.part_year_home`. This is the first reading, and the line cites p503 p. 3. The register therefore misstates the reading applied (spec 3, requirement 7). No values sheet shows the entry, because no line links it.
- **Fix:** not made, because this package may not change a recorded choice or an owner verdict. Proposed: the owner retires the entry as superseded by BUG-0157 (the source rule is now encoded, so no ambiguity remains), or restates `chosen` as the first reading and links it from `dependent.dc_lived_half`.
- **Fix lines:** `ambiguities/2025.yaml` (`amb.2025.dc_born_died_half_year`); optionally `dependent.dc_lived_half`.
- **Siblings checked:**
  - The 11 other unlinked entries, each against its named lines. This was checked at the level of label, op and `places`, not by evaluating the lines; on that check their `chosen` text matches the encoding: `eic.line1_in_table`, `dependent.eic_ssn`, `scveh.screen`, `scveh.unrecovered`, `mq.q4` and `mq.total`, `scveh.bus_cost` (places 6), `person.sep_s5`, the `sc.f7206_line7`/`_line9` pair with their `_pos` helpers, and `sc.qbi_se`/`qbi_plan`/`qbi_ded`.
  - `dependent.hoh_lived_half` (the head of household twin; BUG-0153), which has no register entry.
- **Regression predictions:** none; no value changes. `stage15.f2441.parent_died_part_year` (BUG-0157's regression) already exercises the first reading.
- **Validation:** source and YAML inspection (`forms/2025/dependent.yaml:388-418`, `:1492-1509`; BUG_INVENTORY BUG-0157).
- **Tags:** register-drift; documentation; owner-decision-needed
