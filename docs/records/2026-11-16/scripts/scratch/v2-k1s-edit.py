"""Lane v2-k1s: edit the b/ copies (BUG-0882, 0886 and the k1s siblings). Each replacement must match exactly once."""
import json
import sys

B = "/tmp/nightplan/scratch/v2-k1s/b/"


def sub(text, old, new, what):
    n = text.count(old)
    if n != 1:
        sys.exit(f"{what}: matched {n} times")
    return text.replace(old, new)


SP = "(or your spouse, whether or not you file jointly)"
SPAND = "(and your spouse, whether or not you file jointly)"

# ---------------------------------------------------------------- forms/2025/k1s.yaml
p = B + "forms/2025/k1s.yaml"
t = open(p).read()

t = sub(t, """a disposition of stock, at-risk amounts, losses carried from earlier years by basis or at-risk limits and the other material
    participation tests are refused.""", """a disposition of stock, at-risk amounts, losses carried from earlier years by basis or at-risk limits, the other material
    participation tests, a corporation trading investments for its owners, a real estate professional's box 2 when no rental
    of the filer's own is listed (Schedule E Part I asks it then), a rented home a shareholder used personally, interest on
    money borrowed to buy into the corporation, and section 199A information on a K-1 whose box 1 is a passive loss are
    refused.""", "note")

# BUG-0886: spouse wording
t = sub(t, "source: In 2025, did you (or, on a joint return, your spouse) work in this corporation's business?",
        f"source: In 2025, did you {SP} work in this corporation's business?", "work")
t = sub(t, "source: Did you (or, on a joint return, your spouse) work more than 500 hours in it in 2025, counting both of you together?",
        f"""source: Did you {SP} work more than 500 hours in it in 2025, counting both of you
        together?""", "hours500")
t = sub(t, """      source: Did you (or, on a joint return, your spouse) work more than 100 hours in it in 2025, with no one else, employees
        included, working more?""", f"""      source: Did you {SP} work more than 100 hours in it in 2025, with no one else,
        employees included, working more?""", "most_hours")
t = sub(t, """      source: In at least 5 of the years 2015 to 2024 (or any 3 earlier years, if it is a personal service business), did
        you (or, on a joint return, your spouse) materially participate in this business (its income or loss was nonpassive
        on your return)?""", f"""      source: Did you {SP} materially participate in this business in at least 5 of the
        years 2015 to 2024 (any 3 earlier years if it provides personal services)?""", "past_years")
t = sub(t, """      source: Did you do nearly all the work done in it, or work over 100 hours in it and over 500 hours in all such businesses
        together, or meet another test of material participation?""", f"""      source: Did you {SP} do nearly all the work in it, work over 100 hours in it and over
        500 hours in all such businesses, or meet another test of material participation?""", "mp_other")
t = sub(t, """      source: In 2025, did you (or, on a joint return, your spouse) help make management decisions for its rental real estate,
        such as approving tenants, rents or repairs?""", f"""      source: In 2025, did you {SP} help make management decisions for its rental real
        estate, such as approving tenants, rents or repairs?""", "active")
t = sub(t, """      source: Did you (or, on a joint return, your spouse) own at least a tenth of this corporation's stock, by value, all
        through 2025?""", f"""      source: Did you {SPAND} own at least a tenth of this corporation's stock, by value,
        all through 2025?""", "tenth")

# BUG-0882 and siblings: trading, real estate professional, a rented home used personally; debt-financed acquisition
t = sub(t, """          - k1s.has_loss
          - const: false
        then: k1s.no
    cite: *id031
  - id: k1s.ok
""", """          - k1s.has_loss
          - const: false
        then: k1s.no
    cite: *id031
  - id: k1s.trader
    printed: (screen)
    label: The corporation's business is trading investments for its owners (nonpassive)
    type: Bool
    gated_by: k1s.trader_if_b1
    expr:
      op: input
      source: Is this corporation's business trading stocks, commodities or other investments for its owners?
    cite: &id301
      doc: i1120ssk
      locator: p. 5, "Trading personal property for the account of owners of interests in the activity"
  - id: k1s.trader_if_b1
    printed: (gate)
    label: Trading, asked only when box 1 shows an amount (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - k1s.box1_any
          - const: true
        then: k1s.trader
      - guard:
          op: test
          eq:
          - k1s.box1_any
          - const: false
        then: k1s.no
    cite: *id301
  - id: k1s.re_pro
    printed: (screen)
    label: Real estate professional (box 2 may be nonpassive)
    type: Bool
    gated_by: k1s.re_pro_if_b2
    expr:
      op: input
      source: Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all
        your work time?
    cite: &id302
      doc: i1120ssk
      locator: p. 6, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity
        if you were a real estate professional (defined earlier) and you materially participated in the activity"
  - id: k1s.re_pro_if_b2
    printed: (gate)
    label: Real estate professional, asked only when box 2 shows an amount and no rental or royalty of your own is listed
      (false otherwise; Schedule E Part I asks it then, and a Yes there refuses the return)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          all:
          - op: test
            eq:
            - k1s.box2_any
            - const: true
          - op: test
            eq:
            - scope.rental
            - const: false
        then: k1s.re_pro
      - guard:
          op: test
          any:
          - op: test
            eq:
            - k1s.box2_any
            - const: false
          - op: test
            eq:
            - scope.rental
            - const: true
        then: k1s.no
    cite: *id302
  - id: k1s.dwelling
    printed: (screen)
    label: A rented home used personally by a shareholder beyond the greater of 14 days or 10% of the fair-rental days
    type: Bool
    gated_by: k1s.dwelling_if_rent
    expr:
      op: input
      source: In 2025, did you or another shareholder use one of its rental homes personally for over 14 days and over a
        tenth of the days it was rented at a fair price?
    cite: &id303
      doc: i1120ssk
      locator: p. 5, "The rental of a dwelling unit any shareholder used for personal purposes during the year for more than
        the greater of 14 days or 10% of the number of days that the residence was rented at fair rental value"
  - id: k1s.dwelling_if_rent
    printed: (gate)
    label: Personal use of a rented home, asked only when box 2 or box 3 shows an amount (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          any:
          - op: test
            eq:
            - k1s.box2_any
            - const: true
          - op: test
            eq:
            - k1s.box3_any
            - const: true
        then: k1s.dwelling
      - guard:
          op: test
          all:
          - op: test
            eq:
            - k1s.box2_any
            - const: false
          - op: test
            eq:
            - k1s.box3_any
            - const: false
        then: k1s.no
    cite: *id303
  - id: k1s.interest_buy
    printed: (screen)
    label: Interest on money borrowed to buy shares or put capital into the corporation (debt-financed acquisition)
    type: Bool
    expr:
      op: input
      source: Did you pay interest in 2025 on money you borrowed to buy shares of this corporation or to put money into it
        as an owner?
    cite: &id304
      doc: i1040se
      locator: p. 9, S Corporations, "If you used loan proceeds to buy an interest in, or make a contribution to the capital
        of, an S corporation (debt-financed acquisition), report your share of deductible S corporation interest expense on
        either Schedule A or Schedule E"
  - id: k1s.ok
""", "new screen lines")
t = sub(t, """    - when: k1s.not_at_risk_if_loss
      form: Form 6198 (At-Risk Limitations)
      remedy: A loss with amounts not at risk is figured on Form 6198, which this tool does not prepare.
      cite: *id031
""", """    - when: k1s.not_at_risk_if_loss
      form: Form 6198 (At-Risk Limitations)
      remedy: A loss with amounts not at risk is figured on Form 6198, which this tool does not prepare.
      cite: *id031
    - when: k1s.trader_if_b1
      form: A corporation trading investments for its owners (nonpassive trading activity)
      remedy: A corporation that trades investments for its owners is outside this tool.
      cite: *id301
    - when: k1s.re_pro_if_b2
      form: Schedule K-1 (Form 1120-S) box 2 of a real estate professional (Schedule E, line 43)
      remedy: Rental real estate from an S corporation held by a real estate professional is outside this tool.
      cite: *id302
    - when: k1s.dwelling_if_rent
      form: Rental of a home a shareholder used personally (nonpassive; Form 8582 does not apply)
      remedy: An S corporation's rental of a home a shareholder used personally for more than the limit is outside this tool.
      cite: *id303
    - when: k1s.interest_buy
      form: Schedule E, line 28, interest on money borrowed to buy into an S corporation (debt-financed acquisition)
      remedy: Interest on money borrowed to buy into an S corporation is outside this tool.
      cite: *id304
""", "ok refusals")

# k1s.qbi sibling: a passive box 1 loss may be partly held back on Form 8582; only the allowed part is QBI
t = sub(t, """  - id: k1s.qbi
    printed: (helper)
    label: Qualified business income (loss) from this K-1 before the passive activity limitation (box 17, code V)
""", """  - id: k1s.qbi_passive
    printed: (gate)
    label: Section 199A information on a K-1 whose box 1 is a passive loss (only the part Form 8582 allows is QBI)
    type: Bool
    expr:
      op: test
      all:
      - op: test
        gt:
        - k1s.p1_loss
        - const: 0
      - op: test
        any:
        - op: test
          lt:
          - k1s.qbi_stmt_if_any
          - const: 0
        - op: test
          gt:
          - k1s.qbi_stmt_if_any
          - const: 0
    cite: &id305
      doc: i8995
      locator: p. 3, "If a loss or deduction is partially suspended, only the portion of the allowed loss or deduction attributable
        to QBI must be considered when determining QBI from the trade or business in the year the loss or deduction is incurred"
  - id: k1s.qbi
    printed: (helper)
    label: Qualified business income (loss) from this K-1 (box 17, code V), when box 1 is not a passive loss
""", "qbi_passive")
t = sub(t, """      remedy: When a loss is partly carried forward by the basis limitation, only the allowed part of the qualified business
        loss counts this year; working out that part is outside this tool.
      cite: *id036
""", """      remedy: When a loss is partly carried forward by the basis limitation, only the allowed part of the qualified business
        loss counts this year; working out that part is outside this tool.
      cite: *id036
    - when: k1s.qbi_passive
      form: Form 8995 with a passive loss from a Schedule K-1 (Form 1120-S), box 1
      remedy: When a passive loss may be held back on Form 8582, only the allowed part counts toward qualified business income;
        working out that part is outside this tool.
      cite: *id305
""", "qbi refusal")
open(p, "w").write(t)

# ---------------------------------------------------------------- interview/2025/questions.yaml
p = B + "interview/2025/questions.yaml"
t = open(p).read()
t = sub(t, """  - id: k1s_prior
    heading: On an earlier return, was a loss from this corporation held back for any of these reasons?
""", """  - id: k1s_prior
    heading: On an earlier return, was a loss from this corporation held back for any of these reasons?
  - id: k1s_activity
    heading: Is any of these true of you or this corporation?
""", "group")
t = sub(t, """      prepares; a Yes ends the interview here.
  - input: f7203.election
    order: 264
    seq: 180
""", """      prepares; a Yes ends the interview here.
  - input: k1s.trader
    order: 264
    seq: 179
    group: k1s_activity
    tick: Its business is trading stocks or other investments for its owners
    help: A fund that buys and sells stocks for its owners is one; a business that sells goods or services is not. Outside
      what this tool prepares; a Yes ends the interview here.
  - input: k1s.re_pro
    order: 264
    seq: 180
    group: k1s_activity
    tick: Over 750 hours, and most of your work time, in real estate
    help: Outside what this tool prepares; a Yes ends the interview here.
  - input: k1s.dwelling
    order: 264
    seq: 181
    group: k1s_activity
    tick: One of its rental homes had over 14 days of personal use
    help: A day counts if you, another shareholder, a family member of either, or anyone paying less than a fair rent used
      it. Outside what this tool prepares; a Yes ends the interview here.
  - input: k1s.interest_buy
    order: 264
    seq: 182
    group: k1s_activity
    tick: You paid interest on money borrowed to buy into it
    help: A loan used to buy shares, or to put money into the corporation as an owner. Outside what this tool prepares; a
      Yes ends the interview here.
  - input: f7203.election
    order: 264
    seq: 183
""", "k1s bank + f7203.election seq")
for inp, old, new in [("f7203.loans", 181, 184), ("f7203.line1", 182, 185), ("f7203.line2", 183, 186)]:
    t = sub(t, f"  - input: {inp}\n    order: 264\n    seq: {old}\n", f"  - input: {inp}\n    order: 264\n    seq: {new}\n", inp)
open(p, "w").write(t)

# ---------------------------------------------------------------- fixtures/2025/defaults.json
p = B + "fixtures/2025/defaults.json"
t = open(p).read()
CLOSED = "Closed: the circumstance this question asks about does not apply unless the scenario says so."


def insert_before(t, new_input, before_input):
    anchor = '    {\n      "input": "%s",' % before_input
    e = '    {\n      "input": "%s",\n      "value": false,\n      "reason": "%s"\n    },\n' % (new_input, CLOSED)
    return sub(t, anchor, e + anchor, "default " + new_input)


t = insert_before(t, "k1s.dwelling", "k1s.hours500")
t = insert_before(t, "k1s.interest_buy", "k1s.most_hours")
t = insert_before(t, "k1s.re_pro", "k1s.risk_carry")
t = insert_before(t, "k1s.trader", "k1s.v_other")
json.loads(t)
open(p, "w").write(t)
print("k1s edits applied")
