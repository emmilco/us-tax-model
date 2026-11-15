#!/usr/bin/env python3
"""Lane 2a: write this lane's entries of the question bank (interview/2025/questions.yaml) from the table below.

Run from the worktree root. It replaces the lane's entries in place (the first of them marks the place) and leaves
every other entry untouched. The table is the lane's wording: edit it here and run again."""
import json, re
REFUSES = "A return with this is outside what this tool prepares; a Yes ends the interview here."
Q = []  # (input, order, seq, prompt or None, help or None, value_labels or None)
def q(i, prompt=None, help=None, labels=None, order=120): Q.append([i, order, 0, prompt, help, labels])

q("$dependent",
  "In 2025, did children live with you, or did you (or, on a joint return, your spouse) support anyone else, such as a parent, another relative or a partner? List each one, or leave the list empty.",
  "Any label you will recognize will do, such as “Child 1”; a name is not needed. List a child who was away at school, and a child of yours who lives with the other parent. Do not list your husband or wife.")
q("dependent.relationship", "How is this person related to you?",
  "On a joint return, give the relationship to you: your spouse's child is your stepchild, and your spouse's parent, brother or sister is your in-law. Choose the last answer if your relationship with the person broke local law. A person who was your husband or wife at any time in 2025 cannot be listed.",
  {"child": "My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild",
   "sibling": "My brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of my brother, sister, half brother or half sister (a niece or nephew)",
   "sibling_descendant": "Another descendant of a brother or sister, such as a grandniece or grandnephew, or a stepbrother's or stepsister's child",
   "parent": "My father or mother (not a stepparent or foster parent)",
   "parent_relative": "My grandparent or an earlier ancestor, or a brother or sister of my father or mother (an aunt or uncle)",
   "in_law": "My stepfather or stepmother, or my son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law, even after a death or divorce",
   "household_member": "Someone else who lived with me all of 2025 as a member of my household, such as a partner, a friend, a cousin or a foster parent",
   "other": "Someone else"})
q("dependent.age", "How old was this person at the end of 2025?", "Enter 0 for a baby born in 2025.")
q("dependent.lived_all_year",
  "Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)",
  "Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you. For a child who was missing because of a kidnapping, answer No.")
q("dependent.months",
  "For how many months of 2025 did this person live with you?\n\nCount time away at school, on vacation, on business, in hospital, in military service or in juvenile detention, but not time a kidnapped child was missing.\n\nIf it was more than half the year but fewer than 7 full months, enter 7.\n\nFor a person born, adopted or placed with you in 2025, or who died in 2025: enter 12 if your home was theirs for more than half of their part of the year (for a person who cannot be your qualifying child, for all of it), and 0 otherwise.")
q("dependent.born_died"); q("dependent.placed"); q("dependent.part_year_home")
q("dependent.kidnapped",
  "Is this a child whom the police or other authorities presume was kidnapped by someone outside your family and the child's, and who was missing because of it at some time in 2025?",
  "Answer Yes even if the authorities first presumed the kidnapping after 2025, or the child has since come home.")
q("dependent.citizen_ssn",
  "Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it, such as “Not Valid for Employment”, answer No.)",
  "The number must have been issued before the due date of your 2025 return, extensions included; if it was not, answer No.")
q("dependent.younger", "Is this person younger than you (or, if you file together, younger than either of you)?")
q("dependent.student", "Was this person a full-time student during any part of 5 months of 2025?",
  "Full-time is what the school counts as full-time. The school must have regular teaching staff and students who attend, or be a full-time on-farm training course. A co-op job that is part of the course counts; on-the-job training, correspondence schools and online-only schools do not.")
q("dependent.disabled",
  "At any time in 2025, was this person permanently and totally disabled: unable to do any substantial paid work because of a physical or mental condition that a doctor has found has lasted, or will last, at least a year, or will lead to death?")
q("dependent.own_money",
  "In 2025, did this person have money of their own (pay, benefits in their name, savings, a trust, a loan) or own the home they lived in?",
  "For a child with no income, savings or property of their own, answer No. If you are not sure, answer Yes.")
q("dependent.self_support_view", "Did this person pay for more than half of their own living costs in 2025 out of their own money?",
  "Living costs are housing, food, clothing, schooling, medical care, recreation and transport. A scholarship does not count as the person's own money. If it is close, choose the last answer: the next question gives the rules.",
  {"under_half": "No: clearly less than half", "over_half": "Yes: clearly more than half", "unsure": "It is close, or I am not sure"})
q("dependent.self_support")
q("dependent.ever_married", "Has this person ever been married?", "Count a marriage that has since ended.")
q("dependent.married",
  "Was this person married at the end of 2025, or is this person on a joint tax return for 2025 (for example one filed with a husband or wife who died in 2025)?",
  "A person legally separated under a decree of divorce or separate maintenance is not married. " + REFUSES)
q("dependent.joint_return",
  "Is a joint tax return for 2025 being filed that includes this person, other than one filed only to get back tax that was withheld or paid in advance?")
q("dependent.other_claimant",
  "Besides you (and your spouse, if you file together), did this person live for more than half of 2025 with another relative who could claim them: a parent, grandparent, aunt, uncle, or grown brother or sister?",
  "Answer Yes even if that relative will not claim the person. Any relative the person is the child, grandchild, younger brother or sister, niece or nephew of can count. A Yes may end the interview here: the rules for a child two people can claim are outside what this tool prepares.")
q("dependent.other_nontaxpayer",
  "Is every such relative someone who does not have to file a 2025 tax return, and who either files none or files only to get back tax that was withheld or paid in advance?",
  "A relative who is not a U.S. citizen and has no U.S. income also counts. One who files to claim the earned income credit or any other credit or deduction does not.")
q("dependent.parents_apart",
  "Is this person a child whose parents are divorced, separated, or lived apart for the last 6 months of 2025?",
  "Count parents who never married each other. If you are not sure, answer Yes.")
q("dependent.divorced_rule",
  "Has the parent this child lived with for more of 2025 given the right to claim the child to the other parent, by signing Form 8332 or under a divorce decree or separation agreement?",
  "Answer Yes whichever parent you are. A release that was taken back still counts for 2025 unless the other parent was told in writing in 2024 or earlier. " + REFUSES)
q("dependent.spouse_relative")
q("dependent.qr_all_year",
  "Was this person away from your home in 2025 only for a temporary reason, yours or theirs: illness, school, work, vacation, military service, juvenile detention, or a stay in a nursing home for constant medical care?\n\nAnswer Yes also if the person lived with you until they died in 2025, or from their birth, adoption or placement with you in 2025.")
q("dependent.lawful", "Was your relationship with this person lawful under local law throughout 2025?",
  "Answer No only if the relationship broke local law at some time in 2025.")
q("dependent.gross_income",
  "What was this person's total income in 2025, before any expenses, leaving out income that is not taxed (such as social security that is not taxable)?",
  "Count rent received before expenses, a partner's share of a partnership's gross income, a business's sales less the cost of the goods sold, taxable unemployment pay and taxable scholarships.")
q("dependent.supported_view", "Did you pay for more than half of this person's living costs in 2025?",
  "Living costs are housing (at what it would rent for), food, clothing, schooling, medical care, recreation and transport. What the person paid from their own income or benefits is not paid by you. If it is close, choose the last answer: the next question gives the rules.",
  {"under_half": "No: clearly less than half", "over_half": "Yes: clearly more than half", "unsure": "It is close, or I am not sure"})
q("dependent.supported")
q("dependent.multiple_support",
  "Did two or more people, you among them, together pay more than half of this person's living costs in 2025, with no one of them paying more than half?",
  REFUSES)
q("dependent.citizen",
  "In 2025, was this person a U.S. citizen, a U.S. national, or a resident of the United States for tax purposes (a “resident alien”)?",
  "If you are a U.S. citizen or national and this is your adopted child who lived with you all year as a member of your household, answer Yes.")
q("dependent.canada_mexico", "Was this person a resident of Canada or Mexico in 2025?")
q("dependent.tin",
  "Will this person have a social security number, or an ITIN or ATIN (or an application for one), by the due date of your 2025 return, extensions included?",
  "An ITIN is a tax number for a person who cannot get a social security number; an ATIN is one for a child being adopted. An expired ITIN counts only if renewed, or renewal applied for, by then.")
q("dependent.work_ssn",
  "Does this person have a social security number that is valid for work, issued before the due date of your 2025 return, extensions included?",
  "If the card says “Not Valid for Employment”, answer No. If it says “Valid for Work Only With DHS Authorization”, answer Yes only while that authorization is valid.")
q("dependent.parent_home_paid")
q("dependent.absence_no_return",
  "In counting the time this person lived with you, did you count time away that the person, or you, was not expected to come back from, or during which you did not keep up the home?")
q("dependent.us_half",
  "Did this person live with you in the United States for more than half of 2025? (For a child born, adopted or placed with you in 2025, or who died in 2025: more than half of their part of the year.)",
  "The United States is the 50 states and the District of Columbia; your home counts as there while you are on extended military duty abroad. Time away at school, on vacation or in hospital counts as living with you; time a kidnapped child was missing does not.", order=314)
q("dependent.eic_ssn",
  "Does this person have a social security number that counts for the earned income credit, issued by the due date of your 2025 return, extensions included?",
  "Any social security number counts unless the card says “Not Valid for Employment” and the number was issued only to get a federally funded benefit. A card that says “Valid for Work Only With DHS Authorization” counts only while the authorization is valid.", order=314)

# The order within the first sitting (order 120): the plain facts every dependent is asked, each followed by the
# questions only its rare answer opens; then the tests of a relative who is not a child; then the papers.
# other_claimant, parents_apart, ever_married and own_money are adjacent: the lane's candidates for one tick-list.
SEQ = """$dependent relationship age lived_all_year kidnapped months born_died placed part_year_home younger student disabled
other_claimant parents_apart ever_married own_money other_nontaxpayer divorced_rule married joint_return self_support_view
self_support spouse_relative qr_all_year lawful gross_income multiple_support supported_view supported citizen_ssn citizen
canada_mexico tin work_ssn parent_home_paid absence_no_return""".split()
rank = {("dependent." + n if not n.startswith("$") else n): k for k, n in enumerate(SEQ)}
first = [x for x in Q if x[1] == 120]
assert {x[0] for x in first} == set(rank), {x[0] for x in first} ^ set(rank)
first.sort(key=lambda x: rank[x[0]])
later = [x for x in Q if x[1] != 120]
for group in (first, later):
    for k, x in enumerate(group): x[2] = k + 1
Q = first + later

def entry(i, order, seq, prompt, help, labels):
    out = [f"  - input: {i}", f"    order: {order}", f"    seq: {seq}"]
    if help: out.append("    help: " + json.dumps(help, ensure_ascii=False))
    if prompt: out.append("    prompt: " + json.dumps(prompt, ensure_ascii=False))
    if labels:
        out.append("    value_labels:")
        out += [f"      {k}: " + json.dumps(v, ensure_ascii=False) for k, v in labels.items()]
    return "\n".join(out) + "\n"

path = "interview/2025/questions.yaml"
text = open(path, encoding="utf-8").read()
head, *items = re.split(r"(?m)^(?=  - input: )", text)
mine = {x[0] for x in Q}
block = "".join(entry(*x) for x in Q)
out, placed = [head], False
for it in items:
    name = it.split("\n", 1)[0][len("  - input: "):].strip()
    if name in mine:
        if not placed: out.append(block); placed = True
        continue
    out.append(it)
assert placed
open(path, "w", encoding="utf-8").write("".join(out))
print(len(Q), "entries written")
