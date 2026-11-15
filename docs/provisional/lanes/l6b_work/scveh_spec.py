FORM = 'scveh'
SCREEN = 'scveh.screen'
HELPERS = [
    dict(id='scveh.claims_bonus_2025', label='Placed in service in 2025 and a special depreciation allowance is claimed for it',
         when=('scveh.is2025', True), then='scveh.claims_bonus'),
]
CHILDREN = [
    dict(id='scveh.records', refuses_on=False,
         label='Its business use can be proved with adequate records or with sufficient evidence to support your own statements',
         q='Do you have a mileage log or other records that show how much you drove it for the business?'),
    dict(id='scveh.got_other',
         label='Acquired in a trade-in or from a related person, or in an involuntary conversion or a like-kind exchange',
         q='Did you get this vehicle with a trade-in, in an exchange, as a replacement for one that was destroyed, stolen or condemned, or from a relative or a business you control?'),
    dict(id='scveh.before_2017', gate=('scveh.is2025', True), gate_name='2025', gate_says='of a vehicle placed in service in 2025',
         label='Placed in service in 2025 but acquired before September 28, 2017',
         q='Did you get it before September 28, 2017?'),
    dict(id='scveh.used_before', gate=('scveh.claims_bonus_2025', True), gate_name='bonus', gate_says='of a vehicle placed in service in 2025 with a special depreciation allowance',
         label='A special depreciation allowance is claimed for it in 2025 and its original use did not begin with you',
         q='Had anyone used this vehicle before you got it?'),
    dict(id='scveh.bonus_excluded', gate=('scveh.claims_bonus_2025', True), gate_name='bonus', gate_says='of a vehicle placed in service in 2025 with a special depreciation allowance',
         label='A special depreciation allowance is claimed for it in 2025 and it is property described in section 168(k)(9)(A) or 168(k)(9)(B): property primarily used in a trade or business of furnishing or selling electrical energy, water or sewage disposal services, gas or steam through a local distribution system, or transportation of gas or steam by pipeline, whose rates are established or approved by a State or political subdivision, an agency or instrumentality of the United States, a public service or public utility commission or similar body of a State or political subdivision, or the governing or ratemaking body of an electric cooperative; or property used in a trade or business that has had floor plan financing indebtedness (a loan used to buy motor vehicles, boats, farm machinery or equipment, or trailers or campers held for sale or lease, and secured by them) whose interest was taken into account under section 163(j)(1)(C) in figuring the business interest expense limit',
         q='Is your business a regulated utility (electricity, water, sewage, gas or steam), or one that finances the vehicles or equipment it holds for sale or lease with a loan secured by them?'),
    dict(id='scveh.prior_bonus', gate=('scveh.is2025', False), gate_name='earlier', gate_says='of a vehicle placed in service before 2025',
         label='A special depreciation allowance was claimed for it in an earlier year',
         q="Did you claim a special ('bonus') depreciation allowance for it in an earlier year?"),
    dict(id='scveh.prior_smr', gate=('scveh.is2025', False), gate_name='earlier', gate_says='of a vehicle placed in service before 2025',
         label='The standard mileage rate was used for it in an earlier year',
         q='Did you use the standard mileage rate for it in an earlier year?'),
    dict(id='scveh.prior_low_use', gate=('scveh.is2025', False), gate_name='earlier', gate_says='of a vehicle placed in service before 2025',
         label='Its business use was 50% or less in any earlier year',
         q='In any earlier year, was half or less of its use for business?'),
    dict(id='scveh.converted',
         label='Converted from personal use to business use, or from business use to personal use, during 2025',
         q='During 2025, did this vehicle change between personal and business use: you began using a personal vehicle for the business, or stopped using this one for the business?'),
    dict(id='scveh.disposed',
         label='Disposed of in 2025',
         q='In 2025, did you sell, trade in, give away or scrap this vehicle?'),
    dict(id='scveh.basis_changed',
         label='A substantial improvement made to it in 2025 or an earlier year (such as adding air conditioning or a new engine); its basis reduced by a clean-fuel deduction or a vehicle credit; its basis reduced because of a casualty',
         q='Has its cost for tax purposes been changed by a major improvement (such as a new engine or added air conditioning), a vehicle tax credit or clean-fuel deduction, or a casualty loss?'),
    dict(id='scveh.short_year',
         label='The 2025 tax year, or any tax year since it was placed in service, is shorter than 12 months',
         q='Was 2025, or any year since you began using it in the business, a tax year of less than 12 months for you?'),
    dict(id='scveh.for_hire',
         label='Used in your business of transporting persons or property for hire, or an ambulance or hearse',
         q='Do you use it to carry people or goods for pay, such as a taxi, ride-share or delivery service, or is it an ambulance or hearse?'),
    dict(id='scveh.investment',
         label='Used in 2025 for investment, that is, for the production of income outside your trade or business',
         q='In 2025, did you also use it to earn income outside the business, such as looking after investments?'),
    dict(id='scveh.method_other',
         label='Must be depreciated under ADS (for example, used predominantly outside the United States), or ADS, the straight line method or the 150% declining balance method elected for it',
         q='Do you depreciate it by straight line, 150% declining balance or the alternative system (ADS), by choice or because you must (for example, it is driven mostly outside the United States)?'),
    dict(id='scveh.others_use', counts=False,
         label='Used by someone other than you, or in a use that is nondeductible under section 274',
         q='Does anyone but you use this vehicle (someone you lease or lend it to, a relative, a co-owner, or someone who gets its use as pay), or is any of its use for entertainment?'),
    dict(id='scveh.leasing', gate=('scveh.others_use', True), gate_name='others_use', gate_says='of a vehicle others use',
         label='You are regularly engaged in the business of leasing passenger automobiles; or you are not a corporation and you purchased it and lease it to others, unless you manufactured or produced it, or the lease term (including options to renew) is less than 50% of its class life and for the first 12 months after the transfer to the lessee your business deductions for it (other than rents and reimbursed amounts) are more than 15% of its rental income',
         q='''Are you regularly in the business of leasing cars, or did you buy this vehicle and lease it to others?

Answer No to the second if you manufactured or produced the vehicle, or if the lease term (including options to renew) is less than 50% of its class life and for the first 12 months after the transfer to the lessee your business deductions for it (other than rents and reimbursed amounts) are more than 15% of its rental income.'''),
    dict(id='scveh.exempt_use', gate=('scveh.others_use', True), gate_name='others_use', gate_says='of a vehicle others use',
         label='Used by a tax-exempt organization, unless used in connection with the production of income subject to the tax on unrelated trade or business income; or used by a governmental unit or a foreign person or entity, unless used under a lease with a term of less than 6 months',
         q='''Is it used by a tax-exempt organization, a governmental unit, or a foreign person or entity?

Answer No for a tax-exempt organization that uses it in connection with the production of income subject to the tax on unrelated trade or business income, and for a governmental unit or foreign person or entity that uses it under a lease with a term of less than 6 months.'''),
    dict(id='scveh.qbu_low', gate=('scveh.others_use', True), gate_name='others_use', gate_says='of a vehicle others use',
         label='Its qualified business use is 50% or less once uses that are not qualified business use are left out',
         q='''Is its business use 50% or less once you leave out these uses, which are not qualified business use?

- investment use
- leasing it to a 5% owner or related person, or using it as compensation for services of a 5% owner or related person, unless for the lease the value is reported as income to that person
- using it as compensation for services of anyone else unless an amount is included in that person's income for the use and any required income tax was withheld
- use that is nondeductible under section 274'''),
]
