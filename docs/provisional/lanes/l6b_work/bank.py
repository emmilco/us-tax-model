"""Rewrite lane 6b's entries of the question bank: every entry of $scveh, scveh.*, $asset, asset.*, s179.* is removed
and written again from the lists below, at the places the old ones had ($asset and $scveh; then the rest)."""
import re, json, sys

p = 'interview/2025/questions.yaml'
s = open(p).read()
MINE = re.compile(r'^(\$scveh|\$asset|scveh\..*|asset\..*|s179\..*)$')

# split the bank into entries
head_end = s.index('  questions:\n') + len('  questions:\n')
head, body = s[:head_end], s[head_end:]
entries = re.split(r'(?m)^(?=  - input: )', body)
entries = [e for e in entries if e]

years = ''.join(f"      y{y}: '{y}'\n" for y in range(2025, 2004, -1))
quarters = "      q1: January to March\n      q2: April to June\n      q3: July to September\n      q4: October to December\n"
convs = ("      hy: Half-year\n      mq1: Mid-quarter, first used January to March\n      mq2: Mid-quarter, first used April to June\n"
         "      mq3: Mid-quarter, first used July to September\n      mq4: Mid-quarter, first used October to December\n")
bonus = ("      full: 'Yes: the special depreciation allowance'\n"
         "      forty: The 40% allowance in place of 100% (an election for property acquired after January 19, 2025)\n"
         "      none: 'No: I elect not to take any special allowance'\n")

cl = json.load(open('tables/2025/class_lives.enum.json'))
first = ['c00_12', 'c00_11', 'c00_13']
plain = {'c00_12': 'A computer, printer or similar equipment (00.12 Information Systems)',
         'c00_11': 'Office furniture and fixtures, such as desks, chairs, files and safes (00.11)',
         'c00_13': 'A copier, calculator or similar office machine, not a computer (00.13 Data Handling Equipment)'}
def title(k):
    if k in plain: return plain[k]
    t = cl['descriptions'][k]
    t = re.split(r': Includes|: Assets|:  ', t)[0]
    t = re.sub(r'\s+', ' ', t).strip()
    return t
order_vals = first + [v for v in cl['values'] if v not in first]
labels = {}
for k in order_vals:
    t = title(k)
    while t in labels.values(): t += ' (' + k[1:].replace('_', '.') + ')'
    labels[k] = t
classes = ''.join("      %s: '%s'\n" % (k, labels[k].replace("'", "''")) for k in order_vals)

V = [  # vehicles, order 255
 ('scveh.method', '''    prompt: For this vehicle — How do you want to figure what this vehicle cost the business in 2025?
    value_labels:
      standard: 'By the mile: $0.70 for each business mile (the standard mileage rate)'
      actual: 'By what it actually cost: gas, repairs, insurance and the like, with depreciation or lease payments (actual expenses)'
'''),
 ('scveh.miles_business', '''    prompt: For this vehicle — How many miles did you drive it for this business in 2025? Do not count driving between
      home and your regular workplace.
'''),
 ('scveh.parking', '''    prompt: For this vehicle — How much did you pay for parking and tolls on business trips in 2025? (Zero if none.)
'''),
 ('scveh.smr_always', '''    help: The standard mileage rate is the by-the-mile method. If you used actual expenses for this vehicle in any earlier
      year, answer No.
'''),
 ('scveh.smr_first', ''),
 ('scveh.fleet', ''),
 ('scveh.miles_commuting', '''    prompt: For this vehicle — How many miles did you drive it in 2025 between home and your regular workplace (commuting)?
'''),
 ('scveh.miles_other', '''    prompt: For this vehicle — How many other miles did you drive it in 2025 (personal driving that is not commuting)?
'''),
 ('scveh.operating', '''    prompt: For this vehicle — How much did it cost to run in 2025 (gas, oil, repairs, insurance, license plates and the
      like)? Leave out depreciation, lease or rent payments, interest, parking and tolls.
'''),
 ('scveh.employee_use', '''    prompt: For this vehicle — Do any of your employees use it for themselves, including driving it to and from work?
      (Answer No if they drive it only for your business.)
'''),
 ('scveh.owned', '''    prompt: For this vehicle — Do you own it? (Answer No if you lease it.)
'''),
 ('scveh.lease', '''    prompt: For this vehicle — How much did you pay in lease payments for it in 2025?
'''),
 ('scveh.lease_smr_before', ''),
 ('scveh.placed', '''    prompt: For this vehicle — In what year did you start using it in the business?
    value_labels:
''' + years),
 ('scveh.records', ''),
 ('scveh.got_other', '''    help: Depreciation of a vehicle got in one of these ways is outside what this tool prepares; a Yes ends the
      interview here.
'''),
 ('scveh.before_2017', ''),
 ('scveh.converted', ''),
 ('scveh.disposed', ''),
 ('scveh.basis_changed', ''),
 ('scveh.short_year', '''    help: If you have filed a return for the full calendar year every year, the answer is No.
'''),
 ('scveh.for_hire', ''),
 ('scveh.investment', ''),
 ('scveh.others_use', ''),
 ('scveh.leasing', ''),
 ('scveh.exempt_use', ''),
 ('scveh.qbu_low', ''),
 ('scveh.method_other', '''    help: If you have never chosen a depreciation method for it, the answer is No.
'''),
 ('scveh.prior_bonus', ''),
 ('scveh.prior_smr', ''),
 ('scveh.prior_low_use', ''),
 ('scveh.cost', '''    prompt: For this vehicle — What did it cost, including sales tax, destination charges and dealer preparation? Do not
      subtract depreciation or any section 179 deduction.
    help: Subtract any gas guzzler tax. For a vehicle you used personally before using it for the business, enter the
      smaller of its adjusted basis or its fair market value on the date you began using it for the business.
'''),
 ('scveh.passenger', ''),
 ('scveh.suv', ''),
 ('scveh.s179_elect', '''    prompt: For this vehicle — How much of its cost do you choose to deduct at once in 2025 under the section 179
      election? (Zero if none.)
'''),
 ('scveh.bonus_choice', '''    prompt: For this vehicle — For the vehicles, computers and other 5-year property you began using in 2025, do you take
      the special ("bonus") depreciation allowance?
    value_labels:
''' + bonus),
 ('scveh.after_jan19', ''),
 ('scveh.bonus_same', ''),
 ('scveh.used_before', '''    help: A rebuilt or reconditioned vehicle counts as used, unless the cost of its used parts is not more than 20% of its
      total cost.
'''),
 ('scveh.bonus_excluded', ''),
 ('scveh.quarter', '''    prompt: For this vehicle — In which part of 2025 did you start using it in the business?
    value_labels:
''' + quarters),
 ('scveh.prior_179', ''),
 ('scveh.prior_conv', '''    value_labels:
''' + convs),
 ('scveh.placed_date', ''),
]
A = [  # equipment, order 257
 ('asset.class', '''    prompt: For this property — What kind of property is it? Choose the description that fits the item; if none does,
      choose the one that fits what your business does.
    help: These are the asset classes of IRS Publication 946, Appendix B. A class listed for your kind of business (Table
      B-2) comes before a general one when the item is named there. An addition or improvement takes the class of the
      property it was made to.
    value_labels:
''' + classes),
 ('asset.placed', '''    prompt: For this property — In what year did you start using it in the business?
    help: It counts from the year it was ready and available for use, even if not yet used. Property you first used
      personally counts from the year you began using it in the business. An addition or improvement counts from the
      later of its own year and the year of the property it was made to.
    value_labels:
''' + years),
 ('asset.kind_excluded', '''    help: A car, truck or van is entered with the business's vehicles, not here. An improvement to the inside of a
      business building may be listed, with qualified improvement property as its kind.
'''),
 ('asset.software', ''),
 ('asset.software_spread', ''),
 ('asset.industry', ''),
 ('asset.industry_item', ''),
 ('asset.long_production', ''),
 ('asset.cost', '''    prompt: For this property — What did it cost, including sales tax, delivery and installation?
    help: For property you used personally before using it in the business, enter the smaller of its adjusted basis or its
      fair market value on the date you began using it in the business.
'''),
 ('asset.pct', '''    prompt: For this property — What percentage of its use is for this business, from 1 to 100?
    help: For listed property, measure the use by the time the property is actually used (rather than merely being
      available for use). For listed property you converted from personal use to business use during 2025, figure the
      percentage only for the months you used it in the business, multiply it by the number of those months and divide by
      12.
'''),
 ('asset.listed', '''    prompt: For this property — Is it equipment of a kind used for entertainment or recreation (such as a camera, or sound
      or video recording equipment) that is not used only in your business or at your regular place of business? Also
      answer Yes for a computer you began using before 2018 that is not used only at your regular place of business.
    help: A part of your home is your regular business establishment only if that part meets the requirements for
      deducting expenses for the business use of a home.
'''),
 ('asset.qbu_low', ''),
 ('asset.got_other', '''    help: Property got in one of these ways is outside what this tool prepares; a Yes ends the interview here.
'''),
 ('asset.before_2017', ''),
 ('asset.ended_2025', ''),
 ('asset.basis_changed', '''    help: Credits and deductions that change it include the disabled access credit, the deduction for removing barriers
      to the disabled and the elderly, the energy efficient commercial building deduction, and the credits for employer
      childcare facilities, refueling property and investment credit property.
'''),
 ('asset.use_changed', ''),
 ('asset.short_year', '''    help: If you have filed a return for the full calendar year every year, the answer is No.
'''),
 ('asset.method_other', '''    help: If you have never chosen a depreciation method for it, the answer is No.
'''),
 ('asset.ads_required', ''),
 ('asset.outside_use', ''),
 ('asset.s179', '''    prompt: For this property — How much of its cost do you choose to deduct at once in 2025 under the section 179
      election? (Zero if none; not more than its business cost.)
    help: Only property you bought for use in your business qualifies. Land, land improvements and property held for
      investment do not.
'''),
 ('asset.not179', '''    prompt: For this property — Is it a land improvement (such as a fence, paving or a swimming pool), property held for
      investment, or property you bought and lease to others or that a tax-exempt organization, a government or a
      foreign person uses?
    help: "Answer No for property you lease to others if you manufactured or produced it, or if the lease term (including
      options to renew) is less than 50% of its class life and for the first 12 months your business deductions for it
      (other than rents and reimbursed amounts) are more than 15% of its rental income. Answer No for use by a
      tax-exempt organization in connection with income subject to the tax on unrelated business income, and for use by
      a government or foreign person under a lease of less than 6 months."
'''),
 ('asset.bonus_choice', '''    prompt: For this property — For property of this kind that you began using in 2025, do you take the special ("bonus")
      depreciation allowance?
    value_labels:
''' + bonus),
 ('asset.after_jan19', '''    prompt: For this property — Did you acquire it after January 19, 2025? (Answer No if you signed a binding written
      contract for it before January 20, 2025, even if you received it later.)
'''),
 ('asset.bonus_same', ''),
 ('asset.used_before', '''    help: Rebuilt or reconditioned property counts as used, unless the cost of its used parts is not more than 20% of its
      total cost.
'''),
 ('asset.quarter', '''    prompt: For this property — In which part of 2025 did you start using it in the business?
    value_labels:
''' + quarters),
 ('asset.prior_conv', '''    value_labels:
''' + convs),
 ('asset.prior_179', ''),
 ('asset.prior_bonus', ''),
]
S = [
 ('s179.prior_form', '''    help: This is line 13 of the last Form 4562 (Depreciation and Amortization) you filed, a "section 179 carryover". If
      you have never had a business of your own, the answer is No.
'''),
 ('s179.carryover', ''),
 ('s179.wc_interest', None),  # keeps its help
]

def old_extra(inp):
    for e in entries:
        if e.startswith(f'  - input: {inp}\n'):
            return e
    return None

def render(inp, order, seq, extra):
    if extra is None:  # keep the old entry's fields other than order and seq
        e = old_extra(inp)
        rest = ''.join(l for l in e.splitlines(True)[1:] if not re.match(r'    (order|seq): ', l))
        return f'  - input: {inp}\n    order: {order}\n    seq: {seq}\n' + rest
    return f'  - input: {inp}\n    order: {order}\n    seq: {seq}\n' + extra

roster_asset = '''  - input: $asset
    order: 257
    seq: 1
    prompt: For this business — List each piece of equipment, furniture or machinery (anything lasting other than a vehicle)
      whose cost this business deducts over several years or under the section 179 election, one entry per item; leave
      the list empty if none. Include items first used from 2005 to 2025.
    help: Things whose cost you deduct in full as supplies, or under a de minimis rule, are not listed here.
'''
roster_scveh = '''  - input: $scveh
    order: 255
    seq: 1
    prompt: For this business — List each car, truck or van you drove for this business in 2025 and want to deduct costs
      for, one entry per vehicle; leave the list empty if none.
    help: Driving between your home and your regular place of work is commuting, not driving for the business.
'''
vehicles = ''.join(render(i, 255, n + 2, x) for n, (i, x) in enumerate(V))
equipment = ''.join(render(i, 257, n + 2, x) for n, (i, x) in enumerate(A))
carry = ''.join(render(i, 258, n + 1, x) for n, (i, x) in enumerate(S))

out, placed_rest = [], False
for e in entries:
    inp = re.match(r'  - input: (\S+)\n', e).group(1)
    if inp == '$asset':
        out.append(roster_asset); continue
    if inp == '$scveh':
        out.append(roster_scveh); continue
    if MINE.match(inp):
        if not placed_rest:
            out.append(vehicles + equipment + carry); placed_rest = True
        continue
    out.append(e)
open(p, 'w').write(head + ''.join(out))
print('bank written:', len(V), len(A), len(S))
