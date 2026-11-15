FORM = 'asset'
SCREEN = 'asset.screen'
HELPERS = [
    dict(id='asset.claims_bonus', label='Placed in service in 2025 and a special depreciation allowance is claimed for its class',
         when=('asset.is2025', True), then='asset.bonus_claimed'),
]
# asset.bonus_claimed is written by hand in the form (a test on asset.bonus_choice).
CHILDREN = [
    dict(id='asset.kind_excluded',
         label='Real property (a building or a structural component, other than qualified improvement property) or land; a car, truck or other vehicle; an aircraft; a film, videotape or sound recording',
         q='Is this a building or part of one, land, a vehicle, an aircraft, a film or a recording?'),
    dict(id='asset.software', counts=False,
         label='Computer software',
         q='Is this computer software?'),
    dict(id='asset.software_spread', gate=('asset.software', True), gate_name='software', gate_says='of computer software',
         label='Computer software not placed in service in 2025, or whose business cost is not all deducted in 2025 through section 179 and the special depreciation allowance',
         q='Is any of its business cost left to deduct after 2025: you began using it before 2025, or you are not deducting the whole cost in 2025?'),
    dict(id='asset.industry', counts=False,
         label='The business is a utility, an energy producer, a recycler, a rent-to-own dealer, a motorsports complex, or one with floor plan financing',
         q='Is your business a utility or energy producer, a recycler, a rent-to-own dealer, a motor racing track, or a dealer that finances its stock with a loan secured by it?'),
    dict(id='asset.industry_item', gate=('asset.industry', True), gate_name='industry', gate_says='of a business of one of those kinds',
         label='Qualified reuse and recycling property; qualified rent-to-own property; energy property; a motorsports entertainment complex; a natural gas gathering line; smart electric meter or grid property; electric transmission property; an initial clearing and grading land improvement for utility property; or, with a special depreciation allowance in 2025, property described in section 168(k)(9)(A) or 168(k)(9)(B)',
         q='''Is this item any of these?

- machinery or equipment used exclusively to collect, distribute or recycle reuse and recyclable materials (qualified reuse and recycling property, section 168(m))
- qualified rent-to-own property (section 168(i)(14))
- energy property specified in section 168(e)(3)(B)(vi)
- a motorsports entertainment complex (section 168(i)(15))
- a natural gas gathering line (section 168(i)(17))
- qualified smart electric meter or qualified smart electric grid system property
- electric transmission property specified in section 168(e)(3)(E)(v)
- an initial clearing and grading land improvement for gas utility property or for electric utility transmission and distribution plants
- property you claim a special depreciation allowance for in 2025 that is either of these:
  - property primarily used in a trade or business of furnishing or selling electrical energy, water or sewage disposal services, gas or steam through a local distribution system, or transportation of gas or steam by pipeline, whose rates are established or approved by a State or political subdivision, an agency or instrumentality of the United States, a public service or public utility commission or similar body of a State or political subdivision, or the governing or ratemaking body of an electric cooperative
  - property used in a trade or business that has had floor plan financing indebtedness (a loan used to buy motor vehicles, boats, farm machinery or equipment, or trailers or campers held for sale or lease, and secured by them) whose interest was taken into account under section 163(j)(1)(C) in figuring the business interest expense limit'''),
    dict(id='asset.long_production',
         label='Property with a long production period, or qualified production property',
         q="Was it built or produced for you over a long period (property with a 'long production period'), or is it 'qualified production property'?"),
    dict(id='asset.got_other',
         label='Acquired in a like-kind exchange or an involuntary conversion, with a trade-in, from a related person, or by gift or inheritance',
         q='Did you get it with a trade-in, in an exchange, as a replacement for property that was destroyed, stolen or condemned, from a relative or a business you control, or as a gift or inheritance?'),
    dict(id='asset.before_2017',
         label='Acquired before September 28, 2017',
         q='Did you get it before September 28, 2017?'),
    dict(id='asset.used_before', gate=('asset.claims_bonus', True), gate_name='bonus', gate_says='of property placed in service in 2025 with a special depreciation allowance',
         label='A special depreciation allowance is claimed for it in 2025 and its original use did not begin with you',
         q='Had anyone used it before you got it?'),
    dict(id='asset.ended_2025',
         label='Disposed of, or a portion of it disposed of, or converted to personal use in 2025',
         q='In 2025, did you sell, give away or scrap it or part of it, or start using it personally and no longer in the business?'),
    dict(id='asset.basis_changed',
         label='Basis adjusted for anything other than depreciation (for example a casualty loss), or reduced by a credit or deduction other than the section 179 deduction and the special depreciation allowance, for example: the section 179D deduction for energy efficient commercial building property; the deduction for removal of barriers to the disabled and the elderly; the disabled access credit; the enhanced oil recovery credit; the credit for alternative fuel vehicle refueling property; the credit for employer-provided childcare facilities and services; a basis adjustment for investment credit property or advanced manufacturing investment credit property',
         q='Has its cost for tax purposes been changed by anything except depreciation, such as a casualty loss, or a tax credit or special deduction taken for it?'),
    dict(id='asset.use_changed', gate=('asset.is2025', False), gate_name='earlier', gate_says='of property placed in service before 2025',
         label='Its business use percentage has changed since it was placed in service',
         q='Has the business share of its use changed since you first used it in the business?'),
    dict(id='asset.short_year',
         label='The 2025 tax year, or any tax year since it was placed in service, is shorter than 12 months',
         q='Was 2025, or any year since you began using it in the business, a tax year of less than 12 months for you?'),
    dict(id='asset.method_other',
         label='ADS, the straight line method or the 150% declining balance method elected; a method other than the MACRS percentage tables; a general asset account; amortized',
         q='Did you choose a special way of depreciating it: straight line, 150% declining balance, the alternative system (ADS), a general asset account, amortization, or any method that does not use the IRS percentage tables?'),
    dict(id='asset.ads_required',
         label='Must be depreciated under ADS, for example: imported property covered by an executive order of the President of the United States; property used predominantly in a farming business and placed in service in a tax year in which you made an election under section 263A(d)(3) not to have the uniform capitalization rules apply; qualified improvement property held by an electing real property trade or business; property with a recovery period of 10 years or more held by an electing farming business',
         q='Are you required to use the alternative depreciation system (ADS) for it, for example as imported property covered by a presidential order, or as property of a farming or real estate business that made certain elections?'),
    dict(id='asset.outside_use',
         label='Used predominantly outside the United States, or tax-exempt use or tax-exempt bond financed property',
         q='Is it used mostly outside the United States, leased to a charity, a government or a foreign person, or paid for with tax-exempt bonds?'),
    dict(id='asset.qbu_low', gate=('asset.listed', True), gate_name='listed', gate_says='of listed property',
         label='Listed property whose qualified business use is 50% or less',
         q='''Is its business use 50% or less once you leave out these uses, which are not qualified business use?

- investment use
- leasing it to a 5% owner or related person, or using it as compensation for services of a 5% owner or related person, unless for the lease the value is reported as income to that person
- using it as compensation for services of anyone else unless an amount is included in that person's income for the use and any required income tax was withheld
- use that is nondeductible under section 274'''),
]
