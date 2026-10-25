# SPDX-License-Identifier: Apache-2.0
"""One local computation per standard-deduction review question.

The reading is still generated from the canonical expression. Names for amounts
checked in other questions stop recursive expansion. A verdict credits ONLY its
own line, never those named amounts or the whole Form 1040 result.
"""
import reading as R

LABELS = {
    "sa.standardbase": "the base deduction for your filing status",
    "sa.extra": "the dollar amount added for each qualifying age or blindness box",
    "person.age65": "the answer to the birth-date question",
    "sa.boxes_age65": "the number of eligible age boxes",
    "sa.boxes_blind": "the number of blindness boxes",
    "sa.extra_age65": "the age addition in dollars",
    "sa.extra_blind": "the blindness addition in dollars",
    "sa.standardraw": "the base deduction plus the age and blindness additions",
    "sa.mfs": "the answer to 'Are you married filing separately?'",
    "sa.mfs_spouse_itemizes": "the answer to 'Are you married filing separately with a spouse who itemizes?'",
    "sa.standard": "the standard deduction",
    "sa.itemizes": "the decision to use itemized deductions",
    "sa.deduction": "the selected deduction",
    "sa.line17": "the total itemized deductions from Schedule A, line 17",
}


def source(doc, page, quote):
    return {"doc": doc, "locator": f'p. {page}, "{quote}"'}


def plan(canon, make_record):
    chart = source("i1040gi", 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind")
    age = source("i1040gi", 33, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)")
    death = source("i1040gi", 33, "If your spouse was born before January 2, 1961, but died in 2025 before reaching age 65")
    birth = source("f1040", 2, "Were born before January 2, 1961")
    itemize = source("i1040gi", 34, "In most cases, your federal income tax will be less if you take the larger of your standard deduction or itemized deductions")
    exception = source("i1040gi", 34, "If you checked the box on line 12b, your standard deduction is zero")
    # Each title asks about just one expression or input. These are presentation
    # boundaries, not independent tax formulas or handwritten expected values.
    definitions = [
        ("sa.standardbase", "Check the base amounts", "Do these amounts match the IRS sidebar? Age and blindness additions are checked separately.",
         [source("f1040", 2, "Standard deduction for")], "around"),
        ("sa.extra", "Check the dollar amount for one box", "The IRS chart prints total deductions, not a separate per-box amount. Subtract the base deduction from the one-box total, or compare successive chart rows. Does that difference match the dollar amount below?", [source("f1040", 2, "Standard deduction for"), chart], "below"),
        ("person.age65", "Check the birth-date question", "Does the question use the same birth-date cutoff as the IRS checkbox?", [birth], "around"),
        ("sa.boxes_age65", "Which age boxes count?", "Check only who is counted here, including the exception for a person who died before reaching 65.",
         [age, death, canon.lines["person.died_before_65"]["cite"]], "around"),
        ("sa.boxes_blind", "Which blindness boxes count?", "Check only whose blindness boxes are counted. The medical definition of blindness is outside this question.", [age], "around"),
        ("sa.extra_age65", "Calculate the age addition in dollars", "Multiply dollars per box by the number of age boxes. This gives a dollar amount; it does not multiply the age count by the blindness count. The dollar amount per box and the count are checked separately.", [chart], "below"),
        ("sa.extra_blind", "Calculate the blindness addition in dollars", "Multiply dollars per box by the number of blindness boxes. This gives a separate dollar amount to add to the age addition. The dollar amount per box and the count are checked separately.", [chart], "below"),
        ("sa.standardraw", "Add the three dollar amounts", "Add the base deduction, age addition and blindness addition. This is equivalent to adding the age and blindness box counts first, multiplying that total by the dollars per box, then adding the base deduction. Compare that result with the IRS chart.", [chart], "below"),
        ("sa.mfs", "Identify a separate return", "Check that this condition means married filing separately.", [source("f1040", 1, "Married filing separately")], "around"),
        ("sa.mfs_spouse_itemizes", "Identify the spouse-itemizes exception", "Check the two conditions for this exception. Its effect on the amount is the next question.", [exception], "around"),
        ("sa.standard", "Apply the spouse-itemizes exception", "Check the zero-or-calculated-amount choice and the listed situations where this computation stops.", [exception, chart], "around"),
        ("sa.itemizes", "When are itemized deductions selected?", "Check these three reasons for selecting itemized deductions. Their total is reviewed elsewhere.",
         [itemize, source("f1040sa", 1, "If you elect to itemize deductions even though they are less than your standard deduction"), exception], "around"),
        ("sa.deduction", "Choose between the two amounts", "Check the selection rule. The itemize decision and the standard-deduction amount have their own questions.", [itemize], "around"),
        ("f1040.line12e", "Put the selected amount on Form 1040", "Check only that the selected deduction goes on line 12e. This verdict does not approve the preceding calculations.",
         [source("f1040", 2, "Standard deduction or itemized deductions (from Schedule A)")], "around"),
    ]
    records = []
    for lid, title, question, sources, window in definitions:
        rd = R.Reading(canon, lid, stop_at={k: v for k, v in LABELS.items() if k != lid})
        rec = make_record(lid, rd, "one computation")
        if canon.lines[lid]["expr"]["op"] == "param":
            value = canon.params["values"][canon.lines[lid]["expr"]["ref"]]["value"]
            groups = {}
            for status in R.STATUS_WORDS:
                if status in value:
                    groups.setdefault(value[status], []).append(R.STATUS_WORDS[status])
            rec["reading"] = R.Node("For your filing status:", [
                R.Node(f"{' or '.join(statuses).capitalize()}: {R.dollars(amount)}.") for amount, statuses in groups.items()])
            if lid == "sa.extra":
                rec["reading"].text = "Dollar amount added for each qualifying box, by filing status:"
            rec["reading_text"] = rec["reading"].flat()
        elif canon.lines[lid]["expr"]["op"] == "input":
            rec["reading"] = R.Node(canon.question(lid))
            rec["reading_text"] = rec["reading"].flat()
        rec.update(guided=True, title=title, question=question, credit_lines=[lid], source_cites=sources,
                   source_window=window, folded_cites=[])
        records.append(rec)
    return records, []
