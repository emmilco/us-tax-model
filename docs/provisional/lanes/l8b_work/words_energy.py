# Lane 8b wording: home energy improvements (order 230; the 2024 carryforward at 239).
SP = 'you (or, on a joint return, your spouse)'
REFUSE = ' A Yes is outside what this tool prepares and ends the interview here.'
AFTER = ', after any rebate or utility subsidy?'
# The rules on what to take off a cost. Part I (labor counts) and Part II (subsidized financing is left out).
H1 = ('Take off a rebate from the seller, maker or installer, a Department of Energy Home Energy Rebate, and a utility subsidy that was not '
      'taxed as income. Do not take off other state incentives or net metering credits. Leave out loan interest, fees and extended warranties.')
H2 = H1 + ' Leave out any part paid with a subsidized energy loan from a government program.'
QMID = ('The maker gives this code for each product, and a product installed in 2025 counts only with one. Without it, go back and leave that '
        'cost out. A No is outside what this tool prepares and ends the interview here.')
CEE = ' It counts only if it meets the highest efficiency tier of the Consortium for Energy Efficiency (CEE) in effect at the start of 2025; the installer or maker can say.'
O = 230
E = {}
def q(i, seq, prompt=None, help=None, order=O):
    E['f5695.' + i] = dict(order=order, seq=seq, **({'prompt': prompt} if prompt else {}), **({'help': help} if help else {}))

q('any', 1, help='It counts for 2025 if the installation was finished in 2025, whenever it was paid for. A furnace, boiler, wood stove, electrical panel or home energy audit counts too. If in doubt, answer Yes.')
# Tick-list A: making or storing energy
q('solar', 2, help='Solar roof tiles and shingles count.')
q('solar_water', 3)
q('wind', 4)
q('geothermal', 5)
q('line5a', 6, 'Did that include a battery that stores at least 3 kilowatt hours of electricity?', 'A smaller battery cannot be claimed; answer No for it.')
q('line7a', 7, 'Did that include a fuel cell at your (or, on a joint return, your spouse\'s) main home?',
  'A fuel cell makes electricity from a fuel such as natural gas or hydrogen.' + REFUSE)
# Tick-list B: keeping heat in, wiring and audits
q('insulation', 8)
q('doors', 9)
q('windows', 10)
q('panel', 11)
q('audit', 12)
# Tick-list C: heating, cooling and hot water
q('heat_pump', 13)
q('hp_water_heater', 14)
q('central_ac', 15)
q('water_heater', 16)
q('furnace', 17)
q('biomass', 18)
# What ends the interview, before any amount is typed
q('business_use', 20, 'Is any of these items used more than 20% of the time for a business, for renting out or to earn other income?',
  'An item used 80% or more for personal purposes counts in full; answer No for it.' + REFUSE)
q('joint_occupancy', 21, 'Did you share a home where this work was done with another occupant who is not your spouse on this return, such as a housemate, a partner or a co-owner living there?',
  'This is about insulation, doors, windows, heating, cooling, hot-water and panel work and audits, at your main home or another home. Answer Yes whether or not the other person paid or claims a credit. Answer No if a neighbor only shared the cost of equipment serving each of your own homes.' + REFUSE)
q('separate_homes', 22, None, 'Each spouse then figures this credit on a separate form.' + REFUSE)
q('construction_later', 23, 'Was any of the solar, wind, geothermal or battery equipment put in a home being built or rebuilt that you did not begin to live in during 2025?',
  'Costs of building or rebuilding a home count in the year you first live in it: equipment put in during 2024 in a new home first lived in in 2025 counts for 2025, and the answer is then No.' + REFUSE)
# Part I amounts
def cost(i, seq, thing, labor='with installation labor', help=''):
    q(i, seq, f'What did {thing} cost, {labor}{AFTER}', ((help + ' ') if help else '') + (H1 if labor.startswith('with') and seq < 30 else H2))
cost('line1', 24, 'the solar panels', help='Leave out roof decking or rafters, and any part that heats a swimming pool or hot tub.')
cost('line2', 25, 'the solar water heater', help='It counts only if at least half its energy comes from the sun and it is certified by the Solar Rating Certification Corporation or a body your state endorses. Leave out any part that heats a swimming pool or hot tub.')
cost('line3', 26, 'the wind turbine')
cost('line4', 27, 'the geothermal heat pump', help='It counts only if it met the Energy Star requirements in effect when it was bought.')
cost('battery_cost', 28, 'the battery')
# Section A: insulation, doors, windows
q('line17a', 30, 'Were the insulation, doors or windows put in the home in the United States that you own and live in most of the time (your main home)?',
  'A home you rent does not count for these. If you had more than one main home in 2025, for example because you moved, answer and give the costs for one of them only.')
q('line17b', 31, 'Were they new when installed, with you as their first user?')
q('line17c', 32, 'Do you expect them to stay in use in that home for at least 5 years?')
q('line17e', 33, 'Was any of them put in as part of building that home new, rather than in an existing home, an addition or a renovation?',
  'Answer Yes even if they went in after you moved into the new home.' + REFUSE)
NL = 'without labor'
cost('line18a', 34, 'the insulation and air sealing materials', NL, 'Count materials made mainly to cut heat loss or gain that meet the energy code (IECC) standard; the installer or maker can say.')
DOOR = 'Count only doors that meet the Energy Star requirements.'
cost('line19a', 35, 'the most expensive exterior door', NL, DOOR)
q('line19d_i', 36, 'What did the second most expensive door cost, on the same basis?', 'Zero if there was one door.')
q('line19d_ii', 37, 'What did the third most expensive door cost?', 'Zero if there were two doors.')
q('line19e', 38, 'What did all the other doors cost together?', 'Zero if there were three doors or fewer.')
q('qmid_doors', 39, 'Do you have the four-character manufacturer identification number (QMID) of each of these doors?', QMID)
WIN = 'Count only windows and skylights with the Energy Star Most Efficient designation, not just the ordinary Energy Star label.'
cost('line20a_i', 40, 'the most expensive window or skylight', NL, WIN)
q('line20a_ii', 41, 'What did the second most expensive window or skylight cost, on the same basis?', 'Zero if there was one.')
q('line20a_iii', 42, 'What did the third most expensive window or skylight cost?', 'Zero if there were two.')
q('line20a_iv', 43, 'What did the fourth most expensive window or skylight cost?', 'Zero if there were three.')
q('line20b', 44, 'What did all the other windows and skylights cost together?', 'Zero if there were four or fewer.')
q('qmid_windows', 45, 'Do you have the four-character manufacturer identification number (QMID) of each of these windows and skylights?', QMID)
# Section B: heating, cooling, hot water, the panel
q('line21a', 50, 'Was the heating, cooling, hot-water or electrical equipment installed at a home in the United States that you live in?',
  'A second home or a home you rent counts.')
q('line21b', 51, 'Was it new, not used by anyone before you?')
q('b_new_home', 52, 'Was any of it installed as part of building a new home, rather than in an existing home, an addition or a renovation?', REFUSE.strip())
W = 'with installation labor'
cost('line29a', 53, 'the heat pump (the most expensive, if more than one)', W, CEE.strip())
q('line29b', 54, 'What did the other heat pumps cost together?', 'Zero if there was one.')
cost('line29c', 55, 'the heat pump water heater (the most expensive, if more than one)', W, CEE.strip())
q('line29d', 56, 'What did the other heat pump water heaters cost together?', 'Zero if there was one.')
cost('line29e', 57, 'the biomass stove or boiler (the most expensive, if more than one)', W, 'It counts only with a thermal efficiency rating of at least 75% (by the higher heating value of the fuel).')
q('line29f', 58, 'What did the other biomass stoves and boilers cost together?', 'Zero if there was one.')
q('qmid_hp', 59, 'Do you have the four-character manufacturer identification number (QMID) of each heat pump, heat pump water heater and biomass stove or boiler?', QMID)
cost('line22a', 60, 'the central air conditioner (the most expensive, if more than one)', W, CEE.strip())
q('line22b', 61, 'What did the other central air conditioners cost together?', 'Zero if there was one.')
q('qmid_ac', 62, 'Do you have the four-character manufacturer identification number (QMID) of each central air conditioner?', QMID)
cost('line23a_i', 63, 'the gas, propane or oil water heater (the most expensive, if more than one)', W, CEE.strip())
q('line23a_ii', 64, 'What did the second most expensive such water heater cost?', 'Zero if there was one.')
q('line23b', 65, 'What did all the other such water heaters cost together?', 'Zero if there were two or fewer.')
q('qmid_wh', 66, 'Do you have the four-character manufacturer identification number (QMID) of each of these water heaters?', QMID)
cost('line24a', 67, 'the furnace or hot water boiler (the most expensive, if more than one)', W,
     CEE.strip() + ' An oil furnace or boiler must also meet the 2021 Energy Star criteria and be rated for fuel blends at least 20% of which is an eligible fuel.')
q('line24b', 68, 'What did the other furnaces and hot water boilers cost together?', 'Zero if there was one.')
q('qmid_furnace', 69, 'Do you have the four-character manufacturer identification number (QMID) of each furnace or hot water boiler?', QMID)
q('line25a', 70, 'Was the panel or wiring work done so that another of the new items could be installed and used, with both put in during 2025?',
  'The other item may be windows or skylights, a central air conditioner, a water heater, a furnace or boiler, a heat pump, a heat pump water heater or a biomass stove or boiler. If one went in in 2024 and the other in 2025, you may treat both as installed in 2025.')
cost('line25c', 71, 'the panel and wiring work', W, 'It counts only if installed to the National Electric Code with a load capacity of at least 200 amps.')
q('qmid_enabling', 72, 'Do you have the four-character manufacturer identification number (QMID) of each item of the panel and wiring work?', QMID)
q('line26a', 73, 'Did the audit inspect your main home in the United States and come with a written report from a certified home energy auditor?',
  'The home may be owned or rented. The report must list the most significant and cost-effective improvements with the energy and cost savings of each, and give the auditor\'s name and tax identification number, a statement that the auditor is certified by a Qualified Certification Program, and that program\'s name. If any of this is missing, answer No.')
q('line26b', 74, 'What did the audit cost' + AFTER, H2)
q('condo', 75, 'Is any of these costs your share of what a condominium association or housing cooperative paid?', 'It changes no amount; a box on the form is checked.')
# The carryforward from 2024, beneath "does your 2024 return include any separate form"
q('carry', 1, help='Line 16 is the part of a solar or other clean energy credit that was more than the 2024 tax; it carries to 2025.', order=239)
q('line12', 2, 'What is the amount on line 16 of your (or, on a joint return, your spouse\'s) 2024 Form 5695? Add the forms if there is more than one.', order=239)
ENTRIES = E
REMOVE = ['f5695.part1_any', 'f5695.part2_any']
_new = ['any', 'solar', 'solar_water', 'wind', 'geothermal', 'insulation', 'doors', 'windows', 'panel', 'audit', 'heat_pump', 'hp_water_heater',
        'central_ac', 'water_heater', 'furnace', 'biomass', 'carry']
INSERT_AFTER = {}
_prev = 'f5695.business_use'
for _k in _new:
    INSERT_AFTER['f5695.' + _k] = _prev; _prev = 'f5695.' + _k
