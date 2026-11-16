"""Lane v2-k1p: edit the b/ copies (BUG-0837, 0838, 0841, 0843 on k1p). Each replacement must match exactly once."""
import json
import sys

B = "/tmp/nightplan/scratch/v2-k1p/b/"


def sub(text, old, new, what):
    n = text.count(old)
    if n != 1:
        sys.exit(f"{what}: matched {n} times")
    return text.replace(old, new)


SP = "(or your spouse, whether or not you file jointly)"
SPAND = "(and your spouse, whether or not you file jointly)"

# ---------------------------------------------------------------- forms/2025/k1p.yaml
p = B + "forms/2025/k1p.yaml"
t = open(p).read()

# form note: the new refusals
t = sub(t, """material
    participation by tests 4, 6 or 7, losses above basis or not at risk, and the held-back losses Form 8582 does not take
    here.'""", """material
    participation by tests 4, 6 or 7, losses above basis or not at risk, losses carried from earlier years by the basis or
    at-risk limits, the held-back losses Form 8582 does not take here, unreimbursed partnership expenses, interest on money
    borrowed to buy into the partnership, a fuel tax credit from it claimed in 2024, a real estate professional''s box 2
    when no rental of the filer''s own is listed (Schedule E Part I asks it then), and a rented home a partner used
    personally.'""", "note")

# BUG-0841: unreimbursed partnership expenses and debt-financed acquisition interest (k1p_facts ticks)
t = sub(t, """      locator: p. 2, Sale or Exchange of Partnership Interest, "Generally, a partner who sells or exchanges a partnership
        interest"
  - id: k1p.b19_other
""", """      locator: p. 2, Sale or Exchange of Partnership Interest, "Generally, a partner who sells or exchanges a partnership
        interest"
  - id: k1p.upe
    printed: (helper)
    label: Unreimbursed partnership expenses paid under the partnership agreement
    type: Bool
    expr:
      op: input
      source: Did you pay expenses of the partnership yourself, without being paid back, that the partnership agreement required
        you to pay?
    cite: &id201
      doc: i1040se
      locator: p. 10, Unreimbursed Partnership Expenses, "You can deduct unreimbursed ordinary and necessary partnership expenses
        you paid on behalf of the partnership on Schedule E if you were required to pay these expenses under the partnership
        agreement"
  - id: k1p.interest_buy
    printed: (helper)
    label: Interest on money borrowed to buy the interest or put capital into the partnership (debt-financed acquisition)
    type: Bool
    expr:
      op: input
      source: Did you pay interest in 2025 on money you borrowed to buy your share of this partnership or to put money into
        it?
    cite: &id202
      doc: i1040se
      locator: p. 9, Domestic Partnerships, "If you used loan proceeds to buy an interest in, or make a contribution to the
        capital of, a partnership (debt-financed acquisition), report your share of deductible partnership interest expense
        on either Schedule A or Schedule E"
  - id: k1p.b19_other
""", "upe/interest_buy lines")

# BUG-0838: spouse wording, participation and active participation
t = sub(t, "source: In 2025, did you (or, on a joint return, your spouse) do any work in the partnership's business?",
        f"source: In 2025, did you {SP} do any work in the partnership's business?", "work")
t = sub(t, """      source: Did you (or, on a joint return, your spouse) work in it more than 100 hours in 2025, and at least as many hours
        as anyone else, employees included?""",
        f"""      source: Did you {SP} work in it more than 100 hours in 2025, and at least as many
        hours as anyone else, employees included?""", "most_hours")
t = sub(t, """      source: Did you (and, on a joint return, your spouse) do nearly all of the work in it in 2025, counting the work of
        employees and anyone else?""",
        f"""      source: Did you {SPAND} do nearly all of the work in it in 2025, counting the work
        of employees and anyone else?""", "nearly_all")
t = sub(t, """      source: In at least 5 of the years 2015 to 2024, did you materially participate in this business (its income or loss
        was nonpassive on your return)?""",
        f"""      source: In at least 5 of the years 2015 to 2024, did you {SP} materially participate
        in this business?""", "five_of_ten")
t = sub(t, """      source: Is it a business of services in health, law, engineering, architecture, accounting, actuarial science, performing
        arts or consulting, in which you materially participated in any 3 years before 2025?""",
        f"""      source: Is it a business of services in health, law, engineering, architecture, accounting, actuarial science, performing
        arts or consulting, in which you {SP} materially participated in any 3 years before
        2025?""", "t6")
t = sub(t, """      source: In 2025, did your work in it and in other businesses where you worked more than 100 hours add up to more than
        500 hours?""",
        """      source: In 2025, did your work (with your spouse's, whether or not you file jointly) in it and in other businesses
        where you worked over 100 hours add up to over 500 hours?""", "t4")
t = sub(t, "source: Did you work in it in 2025 on a regular, continuous and substantial basis, for more than 100 hours?",
        f"""source: Did you {SP} work in it in 2025 on a regular, continuous and substantial
        basis, for more than 100 hours?""", "t7")
t = sub(t, """      source: Did you (or, on a joint return, your spouse) help make decisions for its rental real estate in 2025, such as
        approving tenants, rents or repairs?""",
        f"""      source: Did you {SP} help make decisions for its rental real estate in 2025, such as
        approving tenants, rents or repairs?""", "decisions")
t = sub(t, """      source: All through 2025, did you (and, on a joint return, your spouse) own at least a tenth (by value) of all the interests
        in that rental real estate?""",
        f"""      source: All through 2025, did you {SPAND} own at least a tenth (by value) of all the
        interests in that rental real estate?""", "tenth")

# BUG-0837: tests 5 and 6 need no work in 2025; tests 4 and 7 do
t = sub(t, """  - id: k1p.ask_five
    printed: (helper)
    label: Worked 500 hours or less and tests 2 and 3 not met
    type: Bool
    expr:
      op: test
      all:
      - op: test
        eq:
        - k1p.under500
        - const: true
      - op: test""", """  - id: k1p.ask_five
    printed: (helper)
    label: Box 1 shows an amount and tests 1, 2 and 3 are not met (no work in 2025 is needed for tests 5 and 6)
    type: Bool
    expr:
      op: test
      all:
      - op: test
        eq:
        - k1p.has_b1
        - const: true
      - op: test
        eq:
        - k1p.hours500_if_work
        - const: false
      - op: test""", "ask_five")
t = sub(t, "    label: Asked only when tests 1 to 3 are not met (false otherwise)\n",
        "    label: Asked only when box 1 shows an amount and tests 1 to 3 are not met (false otherwise)\n", "five_of_ten_if_asked label")
t = sub(t, "    label: Worked in the business but met none of tests 1, 2, 3 and 5\n",
        "    label: Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met\n", "ask_other label")
t = sub(t, """  - id: k1p.ask_other_gp
    printed: (helper)
    label: A general partner who met none of tests 1, 2, 3 and 5
    type: Bool
    expr:
      op: test
      all:
      - op: test
        eq:
        - k1p.ask_other
        - const: true
""", """  - id: k1p.ask_other_gp
    printed: (helper)
    label: A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5
    type: Bool
    expr:
      op: test
      all:
      - op: test
        eq:
        - k1p.ask_other
        - const: true
      - op: test
        eq:
        - k1p.work_if_b1
        - const: true
""", "ask_other_gp")
t = sub(t, """    label: Asked only of a general partner who met none of tests 1, 2, 3 and 5 (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - k1p.ask_other_gp
          - const: true
        then: k1p.t4""", """    label: Asked only of a general partner who worked in the business and met none of tests 1, 2, 3 and 5 (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - k1p.ask_other_gp
          - const: true
        then: k1p.t4""", "t4_if_gp label")
t = sub(t, """    label: Asked only of a general partner who met none of tests 1, 2, 3 and 5 (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - k1p.ask_other_gp
          - const: true
        then: k1p.t7""", """    label: Asked only of a general partner who worked in the business and met none of tests 1, 2, 3 and 5 (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - k1p.ask_other_gp
          - const: true
        then: k1p.t7""", "t7_if_gp label")

# BUG-0843: real estate professional (box 2) and a rented home used personally (boxes 2 and 3)
t = sub(t, """      locator: p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities
        must include the income or loss from those activities in Part IV"
  - id: k1p.has_activity
""", """      locator: p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities
        must include the income or loss from those activities in Part IV"
  - id: k1p.re_pro
    printed: (helper)
    label: Real estate professional (box 2 may be nonpassive)
    type: Bool
    expr:
      op: input
      source: Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all
        your work time?
    cite: &id203
      doc: i1065sk1
      locator: p. 14, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity
        if you were a real estate professional (defined earlier) and you materially participated in the activity"
    gated_by: k1p.re_pro_if_b2
  - id: k1p.re_pro_if_b2
    printed: (gate)
    label: Asked only when box 2 shows an amount and no rental or royalty of your own is listed (false otherwise; Schedule
      E Part I asks it then, and a Yes there refuses the return)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          all:
          - op: test
            eq:
            - k1p.has_b2
            - const: true
          - op: test
            eq:
            - scope.rental
            - const: false
        then: k1p.re_pro
      - guard:
          op: test
          any:
          - op: test
            eq:
            - k1p.has_b2
            - const: false
          - op: test
            eq:
            - scope.rental
            - const: true
        then: k1p.no
    cite: *id203
  - id: k1p.dwelling
    printed: (helper)
    label: A rented home used personally by a partner beyond the greater of 14 days or 10% of the fair-rental days
    type: Bool
    expr:
      op: input
      source: In 2025, did you or another partner use one of its rental homes personally for over 14 days and over a tenth
        of the days it was rented at a fair price?
    cite: &id204
      doc: i1065sk1
      locator: p. 11, Special rules for certain other activities, "The rental of a dwelling unit any partner used for personal
        purposes during the year for more than the greater of 14 days or 10% of the number of days that the residence was
        rented at fair rental value"
    gated_by: k1p.dwelling_if_rent
  - id: k1p.dwelling_if_rent
    printed: (gate)
    label: Asked only when box 2 or box 3 shows an amount (false otherwise)
    type: Bool
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          any:
          - op: test
            eq:
            - k1p.has_b2
            - const: true
          - op: test
            eq:
            - k1p.has_b3
            - const: true
        then: k1p.dwelling
      - guard:
          op: test
          all:
          - op: test
            eq:
            - k1p.has_b2
            - const: false
          - op: test
            eq:
            - k1p.has_b3
            - const: false
        then: k1p.no
    cite: *id204
  - id: k1p.has_activity
""", "re_pro/dwelling lines")

# BUG-0841: losses carried by the basis or at-risk limits; a 2024 fuel tax credit (k1p_carry ticks)
t = sub(t, """          - k1p.any_loss
          - const: false
        then: k1p.no
    cite: *id036
  - id: k1p.se_loss_not_material
""", """          - k1p.any_loss
          - const: false
        then: k1p.no
    cite: *id036
  - id: k1p.basis_carry
    printed: (helper)
    label: Losses from this partnership not allowed in an earlier year because of the basis limitation
    type: Bool
    expr:
      op: input
      source: Was a loss from this partnership held back on an earlier return because your basis in it was too low?
    cite: &id205
      doc: i1065sk1
      locator: p. 13, "If you have losses, deductions, or credits from a prior year that weren’t deductible or usable because
        of certain limitations, such as the basis limitations or the at-risk limitations, take them into account in determining
        your net income, loss, or credits for this year"
  - id: k1p.risk_carry
    printed: (helper)
    label: A loss from this partnership not allowed in an earlier year because of the at-risk limitation
    type: Bool
    expr:
      op: input
      source: Was a loss from this partnership held back on an earlier return by the at-risk rules (Form 6198)?
    cite: *id205
  - id: k1p.fuel_2024
    printed: (helper)
    label: A credit for federal tax on fuels claimed on the 2024 return from this partnership's information
    type: Bool
    expr:
      op: input
      source: Did your 2024 return claim a credit for federal tax on gasoline or other fuels based on information from this
        partnership?
    cite: &id206
      doc: i1040se
      locator: p. 9, Domestic Partnerships, "If you claimed a credit for federal tax on gasoline or other fuels on your 2024
        Form 1040, 1040-SR, or 1040-NR based on information received from the partnership, enter as income in column (h) or
        column (k), whichever applies, the amount of the credit claimed for 2024"
  - id: k1p.se_loss_not_material
""", "carry lines")

# k1p.screened: refusal entries, in the order they are asked (64-65, 82-83, 97-99)
t = sub(t, """    - when: k1p.r_disposed
      form: Sale or other disposition of a partnership interest (Form 8949, section 751)
      remedy: A sale or other disposition of a partnership interest is outside this tool.
      cite: *id056
""", """    - when: k1p.r_disposed
      form: Sale or other disposition of a partnership interest (Form 8949, section 751)
      remedy: A sale or other disposition of a partnership interest is outside this tool.
      cite: *id056
    - when: k1p.upe
      form: Schedule E, line 28, unreimbursed partnership expenses (and box 14, code A reduced by them)
      remedy: Partnership expenses you paid yourself under the partnership agreement are outside this tool.
      cite: *id201
    - when: k1p.interest_buy
      form: Schedule E, line 28, interest on money borrowed to buy into a partnership (debt-financed acquisition)
      remedy: Interest on money borrowed to buy into a partnership is outside this tool.
      cite: *id202
""", "screened upe")
t = sub(t, """    - when: k1p.t7_if_gp
      form: Material participation by test 7 (facts and circumstances)
      remedy: Material participation by the facts and circumstances test is outside this tool.
      cite: *id030
""", """    - when: k1p.t7_if_gp
      form: Material participation by test 7 (facts and circumstances)
      remedy: Material participation by the facts and circumstances test is outside this tool.
      cite: *id030
    - when: k1p.re_pro_if_b2
      form: Schedule K-1 (Form 1065) box 2 of a real estate professional (Schedule E, line 43)
      remedy: Rental real estate from a partnership held by a real estate professional is outside this tool.
      cite: *id203
    - when: k1p.dwelling_if_rent
      form: Rental of a home a partner used personally (nonpassive; Form 8582 does not apply)
      remedy: A partnership's rental of a home a partner used personally for more than the limit is outside this tool.
      cite: *id204
""", "screened re_pro")
t = sub(t, """    - when: k1p.not_at_risk_if_loss
      form: Form 6198 (at-risk limitations)
      remedy: A partnership loss with an amount not at risk is outside this tool.
      cite: *id036
""", """    - when: k1p.not_at_risk_if_loss
      form: Form 6198 (at-risk limitations)
      remedy: A partnership loss with an amount not at risk is outside this tool.
      cite: *id036
    - when: k1p.basis_carry
      form: Schedule E, line 28, column (i), a loss carried from an earlier year by the basis limitation
      remedy: A partnership loss carried from an earlier year by the basis limitation is outside this tool.
      cite: *id205
    - when: k1p.risk_carry
      form: Form 6198 (at-risk limitations), a loss carried from an earlier year
      remedy: A partnership loss carried from an earlier year by the at-risk limitation is outside this tool.
      cite: *id205
    - when: k1p.fuel_2024
      form: Schedule E, line 28, a 2024 fuel tax credit from the partnership taken into income
      remedy: A fuel tax credit from a partnership claimed on your 2024 return is outside this tool.
      cite: *id206
""", "screened carry")
open(p, "w").write(t)

# ---------------------------------------------------------------- interview/2025/questions.yaml
p = B + "interview/2025/questions.yaml"
t = open(p).read()
t = sub(t, """  - id: k1p_part_other
    heading: Is any of these true of your work in this business?
  - id: k1p_prior
    heading: Which part of the partnership was that loss held back from?
""", """  - id: k1p_part_other
    heading: Counting your spouse's work with yours (whether or not you file jointly), is any of these true of your work in
      this business?
  - id: k1p_rental
    heading: Is either of these true of you or of this partnership's rentals?
  - id: k1p_prior
    heading: Which part of the partnership was that loss held back from?
  - id: k1p_carry
    heading: Does your 2024 return, or an earlier one, show any of these for this partnership?
""", "groups")
t = sub(t, """  - input: k1p.r_disposed
    order: 264
    seq: 63
    group: k1p_facts
    tick: You sold or gave up any of your share in 2025
    help: A Yes ends the interview here.
""", """  - input: k1p.r_disposed
    order: 264
    seq: 63
    group: k1p_facts
    tick: You sold or gave up any of your share in 2025
    help: A Yes ends the interview here.
  - input: k1p.upe
    order: 264
    seq: 64
    group: k1p_facts
    tick: You paid partnership expenses the partnership agreement required you to pay
    help: Only expenses the partnership did not pay you back. A Yes ends the interview here.
  - input: k1p.interest_buy
    order: 264
    seq: 65
    group: k1p_facts
    tick: You paid interest on money borrowed to buy into it
    help: A loan used to buy your share, or to put money into the partnership. A Yes ends the interview here.
""", "upe bank")
t = sub(t, "    help: Count your own hours and, on a joint return, your spouse's hours in it together.\n",
        "    help: Count your own hours and your spouse's hours in it together, whether or not you file jointly.\n", "hours500 help")
t = sub(t, """  - input: k1p.tenth
    order: 264
    seq: 81
    help: The partnership's records or item J show your share. Answer No if it was less than a tenth at any time in 2025.
""", """  - input: k1p.tenth
    order: 264
    seq: 81
    help: The partnership's records or item J show your share. Answer No if it was less than a tenth at any time in 2025.
  - input: k1p.re_pro
    order: 264
    seq: 82
    group: k1p_rental
    tick: Over 750 hours, and most of your work time, in real estate
    help: A Yes ends the interview here.
  - input: k1p.dwelling
    order: 264
    seq: 83
    group: k1p_rental
    tick: One of its rental homes had over 14 days of personal use
    help: A day counts if you, another partner, a family member of either, or anyone paying less than a fair rent used it.
      A Yes ends the interview here.
""", "re_pro bank")
t = sub(t, """      from a bank or other outside lender that you must repay. A Yes ends the interview here.
  # --- end k1p ---
""", """      from a bank or other outside lender that you must repay. A Yes ends the interview here.
  - input: k1p.basis_carry
    order: 264
    seq: 97
    group: k1p_carry
    tick: A loss held back because your basis in it was too low
    help: A Yes ends the interview here.
  - input: k1p.risk_carry
    order: 264
    seq: 98
    group: k1p_carry
    tick: A loss held back by the at-risk rules (Form 6198)
    help: A Yes ends the interview here.
  - input: k1p.fuel_2024
    order: 264
    seq: 99
    group: k1p_carry
    tick: A credit for federal tax on fuels, from its information
    help: A Yes ends the interview here.
  # --- end k1p ---
""", "carry bank")
open(p, "w").write(t)

# ---------------------------------------------------------------- fixtures/2025/defaults.json (sorted inserts, text level)
p = B + "fixtures/2025/defaults.json"
t = open(p).read()
CLOSED = "Closed: the circumstance this question asks about does not apply unless the scenario says so."


def entry(inp):
    return '    {\n      "input": "%s",\n      "value": false,\n      "reason": "%s"\n    },\n' % (inp, CLOSED)


def insert_before(t, new_input, before_input):
    anchor = '    {\n      "input": "%s",' % before_input
    return sub(t, anchor, entry(new_input) + anchor, "default " + new_input)


t = insert_before(t, "k1p.basis_carry", "k1p.basis_short")
t = insert_before(t, "k1p.dwelling", "k1p.five_of_ten")
t = insert_before(t, "k1p.fuel_2024", "k1p.general")
t = insert_before(t, "k1p.interest_buy", "k1p.most_hours")
t = insert_before(t, "k1p.re_pro", "k1p.t4")
t = insert_before(t, "k1p.risk_carry", "k1p.t4")
t = insert_before(t, "k1p.upe", "k1p.work")
json.loads(t)
open(p, "w").write(t)
print("k1p edits applied")
