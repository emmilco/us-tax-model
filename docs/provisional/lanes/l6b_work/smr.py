"""scveh.smr_ok taken apart (the old id stays, derived), and asset.bonus_claimed added. Run once, after the V1 and A1
patches (which add scveh.no and asset.no)."""
p = 'forms/2025/scveh.yaml'
s = open(p).read()
a = s.index('  - id: scveh.smr_ok\n'); b = s.index('  - id: scveh.smr_bad\n')
old = s[a:b]
cite = old[old.index('    cite:\n'):]
new = '''  - id: scveh.smr_always
    printed: (screen)
    label: The standard mileage rate was used for this vehicle in every year it was used for business
    type: Bool
    expr:
      op: input
      source: Have you used the standard mileage rate for this vehicle every year you have used it for the business?
        (Answer Yes if 2025 is the first year.)
''' + cite + '''  - id: scveh.smr_first
    printed: (screen)
    label: The vehicle is owned and the standard mileage rate was used for it in the first year it was used for business
    type: Bool
    gated_by: scveh.smr_first_if_not_always
    expr:
      op: input
      source: Do you own this vehicle, and did you use the standard mileage rate for it in the first year you used it for
        the business? (Answer No if you lease it.)
''' + cite + '''  - id: scveh.smr_first_if_not_always
    printed: (gate)
    label: The vehicle is owned and the standard mileage rate was used for it in its first year, asked only when the rate
      was not used every year (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - scveh.smr_always
          - const: false
        then: scveh.smr_first
      - guard:
          op: test
          eq:
          - scveh.smr_always
          - const: true
        then: scveh.no
''' + cite + '''  - id: scveh.fleet
    printed: (screen)
    label: One of five or more vehicles used in the business at the same time
    type: Bool
    expr:
      op: input
      source: In 2025, did you use five or more vehicles in the business at the same time?
''' + cite + '''  - id: scveh.smr_ok
    printed: (screen)
    label: 'May you use the standard mileage rate for this vehicle? If you own this vehicle: did you use the standard mileage
      rate for it in the first year you used it for business? If you lease it: are you using the standard mileage rate for
      the entire lease period? (No if this is one of five or more vehicles you used in the business at the same time.)'
    type: Bool
    expr:
      op: test
      all:
      - op: test
        eq:
        - scveh.fleet
        - const: false
      - op: test
        any:
        - op: test
          eq:
          - scveh.smr_always
          - const: true
        - op: test
          eq:
          - scveh.smr_first_if_not_always
          - const: true
''' + cite
s = s[:a] + new + s[b:]
open(p, 'w').write(s)

p = 'forms/2025/asset.yaml'
s = open(p).read()
a = s.index('  - id: asset.bonus_same\n')
b = s.index('  - id: asset.bonus_choice\n')
blk = s[b:a]
cite = blk[blk.index('    cite:\n'):]
s = s[:a] + '''  - id: asset.bonus_claimed
    printed: (helper)
    label: A special depreciation allowance is claimed for the class of this property (the full allowance or the 40%
      allowance)
    type: Bool
    expr:
      op: test
      ne:
      - asset.bonus_choice
      - const: none
''' + cite + s[a:]
open(p, 'w').write(s)
print('ok')
