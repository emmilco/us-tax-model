# Lane m4: the Form 5695 mutation cases, written from the table below into fixtures/2025/mutation.json.
# Every case starts from the inputs of mutation.t2.f5695.doors_not_main_home (themselves those of classm.f5695.9:
# a single filer, $9,055 of tax on Form 1040 line 18, no other credits), with every Form 5695 kind answered No,
# every cost $0, every QMID held, lines 17a to 17c and 21a to 21b Yes, and then the changes of the row.
# Amounts are in cents. Predictions are by hand from Form 5695 (2025) and its instructions (cited per case).
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from casegen import load, base_inputs, apply, build, write

MUT = 'fixtures/2025/mutation.json'
data = load(MUT)
BASE_ID = 'mutation.t2.f5695.doors_not_main_home'
base = base_inputs(data, BASE_ID)

KINDS = ['solar', 'solar_water', 'wind', 'geothermal', 'insulation', 'doors', 'windows', 'panel', 'audit', 'heat_pump',
         'hp_water_heater', 'central_ac', 'water_heater', 'furnace', 'biomass']
COSTS = ['line1', 'line2', 'line3', 'line4', 'battery_cost', 'line12', 'line18a', 'line19a', 'line19d_i', 'line19d_ii',
         'line19e', 'line20a_i', 'line20a_ii', 'line20a_iii', 'line20a_iv', 'line20b', 'line22a', 'line22b', 'line23a_i',
         'line23a_ii', 'line23b', 'line24a', 'line24b', 'line25c', 'line26b', 'line29a', 'line29b', 'line29c', 'line29d',
         'line29e', 'line29f']
reset = {f'f5695.{k}': False for k in KINDS}
reset.update({f'f5695.{k}': 0 for k in COSTS})
reset.update({'f5695.any': True, 'f5695.line5a': False, 'f5695.line7a': False, 'f5695.carry': False,
              'f5695.line17a': True, 'f5695.line17b': True, 'f5695.line17c': True, 'f5695.line17e': False,
              'f5695.line21a': True, 'f5695.line21b': True, 'f5695.b_new_home': False, 'f5695.line25a': False,
              'f5695.line26a': False, 'f5695.joint_occupancy': False, 'f5695.separate_homes': False})
reset.update({f'f5695.qmid_{q}': True for q in ['doors', 'windows', 'ac', 'wh', 'furnace', 'enabling', 'hp']})
start = apply(base, reset)

SRC = ("inputs of mutation.t2.f5695.doors_not_main_home (classm.f5695.9: single, $9,055 of tax on Form 1040 line 18, no "
       "other credit), every Form 5695 kind answered No and every cost $0 but as stated")
I = 'i5695 (2025)'
F = 'f5695 (2025)'

rows = []


def row(name, mutants, changes, predict, why, base_over=None):
    inputs = apply(base_over if base_over is not None else start, changes)
    rows.append({'id': f'mutation.m4.f5695.{name}', 'covers': ['f5695', 's3'] if any(k.startswith('s3.') for k in predict) else ['f5695'],
                 'inputs': inputs, 'predict': predict,
                 'note': f"Mutation fixture ({mutants}), {SRC}. Expected values predicted by hand before running the evaluator: {why}"})


# Nothing installed: line 7a (fuel cell) is never asked, so it is unanswered.
row('nothing_installed', 'operand.f5695.f5695.line13.line11_if_any',
    {'f5695.any': False, **{f'f5695.{k}': None for k in KINDS}, **{f'f5695.{k}': None for k in COSTS},
     'f5695.line5a': None, 'f5695.line7a': None},
    {'f5695.line13': 0, 's3.line5a': 0},
    f"nothing was installed and no audit paid for (f5695.any No), so no kind, cost or fuel cell question is asked. Line 13 "
    f"adds lines 6b, 11 and 12 ({F} p. 1); with nothing installed each is $0, so line 13 is $0 and Part I gives no credit "
    f"(Schedule 3 line 5a $0). The fuel cell answer, never asked, does not enter.")
row('fuel_cell_only', 'operand.f5695.f5695.line7a_if_any.line7a.then0; operand.f5695.f5695.kinds_answered.line7a_if_any.all.5.any.0.eq.0',
    {'f5695.line7a': True},
    {'s3.line5a': ('refusal', 'f5695.line7a')},
    f"the only property installed is qualified fuel cell property (line 7a Yes; {F} p. 1, lines 7a to 11). Part I is "
    f"figured, and line 13 includes line 11, the fuel cell credit, which this tool refuses; Schedule 3 line 5a carries "
    f"that refusal (record taken from the evaluator once the gate was confirmed to be f5695.line7a).")
row('wind_only', 'operand.f5695.f5695.kinds_answered.wind_if_any.all.2.any.0.eq.0',
    {'f5695.wind': True, 'f5695.line3': 1000000},
    {'f5695.line13': 300000, 's3.line5a': 300000},
    f"a small wind turbine costing $10,000 is the only property ({F} p. 1, lines 3, 6a, 6b, 13 to 15): line 6b is 30% of "
    f"$10,000, $3,000; line 13 is $3,000; the line 14 limit (tax $9,055 less no other credits) exceeds it, so line 15 and "
    f"Schedule 3 line 5a are $3,000.")
for name, kind, cost, line, amount, cap, mut in [
        ('heat_pump_only', 'heat_pump', 'line29a', '29h', 1000000, 'the $2,000 limit of line 29h', 'heat_pump_if_any.any.0'),
        ('hp_water_heater_only', 'hp_water_heater', 'line29c', '29h', 300000, None, 'hp_water_heater_if_any.any.1'),
        ('biomass_only', 'biomass', 'line29e', '29h', 400000, None, 'biomass_if_any.any.5')]:
    credit = min(amount * 30 // 100, 200000)
    row(name, f'operand.f5695.f5695.sec_b_kinds.{mut}.eq.0',
        {f'f5695.{kind}': True, f'f5695.{cost}': amount},
        {'f5695.line29h': credit, 'f5695.line30': credit, 's3.line5b': credit},
        f"the only property is one item of line {cost[4:]} costing ${amount // 100:,} with its QMID, at a home in the United States "
        f"the filer uses as a residence (lines 21a and 21b Yes; {F} p. 4, Part II, Section B, lines 29a to 29h): 30% of the cost is "
        f"${amount * 30 // 10000:,}" + (f", capped at {cap}," if cap else "") + f" so line 29h is ${credit // 100:,}; "
        f"line 30 adds line 28 ($0) and line 29h; the line 31 limit is $9,055, so line 32 and Schedule 3 line 5b are "
        f"${credit // 100:,}.")
row('panel_only', 'operand.f5695.f5695.sec_b_kinds.panel_if_any.any.6.eq.0',
    {'f5695.panel': True, 'f5695.line25a': True, 'f5695.line25c': 100000},
    {'f5695.line25e': 30000, 'f5695.line30': 30000, 's3.line5b': 30000},
    f"the only property is a panelboard (line 25a Yes) costing $1,000 with its QMID, installed in 2025 to enable a heat pump also installed in 2025 ("
    f"line 25a Yes; {F} p. 3, lines 25a to 25e): 30% is $300, under the $600 limit, so line 25e is $300; lines 27, 28 and 30 are $300 (the $1,200 "
    f"limit of line 28 is not reached) and line 32 and Schedule 3 line 5b are $300.")
row('doors_not_main_home_with_solar', 'operand.f5695.f5695.sec_a_home.no.then1; operand.f5695.f5695.line19c.door1_30',
    {'f5695.line17a': False, 'f5695.doors': True, 'f5695.line19a': 50000, 'f5695.solar': True, 'f5695.line1': 1000000},
    {'f5695.line19c': 15000, 'f5695.line19h': 0, 's3.line5a': 300000},
    f"line 17a is No (the home is not the filer's main home in the United States) and one exterior door cost $500; solar "
    f"panels cost $10,000. Line 19c is the smaller of 30% of line 19a ($150) and $250, so $150 ({F} p. 2, line 19c). "
    f"With line 17a No, Section A is not completed ({F} p. 2, line 17: 'If you checked the “No” box for line 17a, 17b, "
    f"or 17c, you cannot claim the energy efficient home improvement credit. Do not complete Part II, Section A'), so line 19h is $0. Part I: line 6b is "
    f"$3,000, within the line 14 limit, so Schedule 3 line 5a is $3,000.")
row('new_home_insulation_no_doors', 'operand.f5695.f5695.doors_no_qmid.no.then1',
    {'f5695.insulation': True, 'f5695.line18a': 100000, 'f5695.line17e': True},
    {'f5695.line18b': 30000, 'f5695.line19h': 0},
    f"insulation costing $1,000 at the main home, and line 17e is Yes (the improvements are related to the construction "
    f"of the home, which this tool refuses on line 30). No doors were installed, so the doors' QMID is not asked and "
    f"line 19h is $0 ({F} p. 2, lines 19a to 19h); line 18b is 30% of $1,000, $300, under the $1,200 limit.")
row('windows_no_qmid', 'operand.f5695.f5695.windows_no_qmid.windows_qmid_missing.then0; operand.f5695.f5695.sec_b_claimed.no.then1',
    {'f5695.windows': True, 'f5695.line20a_i': 100000, 'f5695.qmid_windows': False, 'f5695.b_new_home': None},
    {'f5695.line20d': ('refusal', 'f5695.windows_no_qmid'), 'f5695.line30': ('refusal', 'f5695.windows_no_qmid')},
    f"windows costing $1,000 for which the filer has no QMID, and no Section B property (so the Section B new-home "
    f"question is not asked). An item without a valid QMID is refused ({I} p. 1, Qualified manufacturer identification numbers: "
    f"'you must include the four-character alphanumeric unique qualified manufacturer identification number (QMID) for each item'), so line 20d and line 30, which adds it through lines 27 and 28, carry the windows' QMID refusal "
    f"(record taken from the evaluator once its gate was confirmed).")
row('doors_no_qmid_no_windows', 'operand.f5695.f5695.windows_no_qmid.no.then1',
    {'f5695.doors': True, 'f5695.line19a': 50000, 'f5695.qmid_doors': False},
    {'f5695.line19h': ('refusal', 'f5695.doors_no_qmid'), 'f5695.line20d': 0},
    f"one exterior door costing $500 without a QMID, and no windows. The door is refused for its missing QMID ({I} p. 1, "
    f"Qualified manufacturer identification numbers), so line 19h carries that refusal; no windows were installed, so line 20d is "
    f"$0 ({F} p. 2, lines 20a to 20d).")
row('water_heater_new_home_audit', 'operand.f5695.f5695.ac_no_qmid.no.then1; operand.f5695.f5695.hp_no_qmid.no.then1',
    {'f5695.water_heater': True, 'f5695.line23a_i': 100000, 'f5695.b_new_home': True, 'f5695.audit': True,
     'f5695.line26a': True, 'f5695.line26b': 20000},
    {'f5695.line22d': 0, 'f5695.line23d': 30000, 'f5695.line26c': 6000, 'f5695.line29h': 0},
    f"a water heater costing $1,000 with its QMID, a home energy audit costing $200 (line 26a Yes), and the Section B "
    f"property is related to the construction of the home (refused on line 30). No central air conditioner and no heat "
    f"pump were installed, so lines 22d and 29h are $0 and their QMIDs are not asked ({F} p. 3, lines 22a to 22d, and p. 4, "
    f"29a to 29h); line 23d is 30% of $1,000, $300, under $600; line 26c is 30% of $200, $60, under $150.")
row('section_b_not_main_home', 'operand.f5695.f5695.line22d.zero.then1; operand.f5695.f5695.line23d.zero.then1; '
    'operand.f5695.f5695.line24d.zero.then1; operand.f5695.f5695.enabling_claimed.no.then1; operand.f5695.f5695.line30.line29h',
    {'f5695.line21a': False, 'f5695.line21b': None, 'f5695.central_ac': True, 'f5695.line22a': 100000,
     'f5695.water_heater': True, 'f5695.line23a_i': 100000, 'f5695.furnace': True, 'f5695.line24a': 100000,
     'f5695.qmid_furnace': False, 'f5695.heat_pump': True, 'f5695.line29a': 100000, 'f5695.line25c': None},
    {'f5695.line22d': 0, 'f5695.line23d': 0, 'f5695.line24d': 0, 'f5695.line25e': 0, 'f5695.line29h': 0, 'f5695.line30': 0},
    f"a central air conditioner, a water heater, a furnace (without a QMID) and a heat pump, $1,000 each, at a home that "
    f"line 21a does not cover (line 21a No: not a home in the United States the filer uses as a residence; so line 21b is not asked; no panelboard, so its "
    f"cost is not asked). Section B is not completed ({F} p. 3, line 21: 'If you checked the “No” box for line 21a or "
    f"21b, you cannot claim the credit for your residential energy property costs. Skip lines 22 through 25 and line 29'), so lines 22d, 23d, 24d, "
    f"25e and 29h are $0, and line 30 (line 28 plus line 29h) is $0.")
row('panel_no_enabling_cost', 'boundary.f5695.f5695.enabling_costs; operand.f5695.f5695.enabling_no_qmid.no.then1',
    {'f5695.panel': True, 'f5695.line25a': True, 'f5695.line25c': 0, 'f5695.qmid_enabling': None},
    {'f5695.line25e': 0},
    f"line 25a is Yes but the panelboard's qualifying cost on line 25c is $0, so no QMID is asked for it and line 25e is "
    f"30% of $0, $0 ({F} p. 3, lines 25a to 25e).")
# One kind left unanswered while another Section B kind is Yes: the Part I flag is unknown.
for i, (kind, other, ocost) in enumerate([('panel', 'water_heater', 'line23a_i'), ('heat_pump', 'water_heater', 'line23a_i'),
                                          ('hp_water_heater', 'water_heater', 'line23a_i'), ('central_ac', 'water_heater', 'line23a_i'),
                                          ('water_heater', 'furnace', 'line24a'), ('furnace', 'water_heater', 'line23a_i'),
                                          ('biomass', 'water_heater', 'line23a_i')]):
    idx = {'panel': 9, 'heat_pump': 11, 'hp_water_heater': 12, 'central_ac': 13, 'water_heater': 14, 'furnace': 15, 'biomass': 16}[kind]
    row(f'{kind}_unanswered', f'operand.f5695.f5695.kinds_answered.{kind}_if_any.all.{idx}.any.0.eq.0',
        {f'f5695.{kind}': None, f'f5695.{other}': True, f'f5695.{ocost}': 100000},
        {'s3.line5a': ('unknown', f'f5695.{kind}')},
        f"a partial return: something was installed, the {other.replace('_', ' ')} ($1,000) was, every other kind is No, "
        f"and whether a {kind.replace('_', ' ')} was installed is not yet answered. Whether Part I is filed waits for "
        f"every kind to be answered (the device f5695.kinds_answered), so Schedule 3 line 5a is unknown on that answer "
        f"(record taken from the evaluator once the input was confirmed).")
# The four statuses other than married filing jointly, a heat pump without a QMID.
STATUS_BASES = {'single': BASE_ID, 'mfs': 'mutation.t2.mfs_sli_line5', 'hoh': 'mutation.t2.hoh_s1a_senior', 'qss': 'mutation.t2.qss_s1a_senior'}
for i, status in [(0, 'single'), (2, 'mfs'), (3, 'hoh'), (4, 'qss')]:
    sb = base_inputs(data, STATUS_BASES[status])
    over = apply(sb, {k: v for k, v in start.items() if k.startswith('f5695.')})
    assert over['f1040.status'] == status
    row(f'hp_no_qmid_{status}', f'operand.f5695.f5695.separate_homes_joint.no.then{i}',
        {'f5695.heat_pump': True, 'f5695.line29a': 100000, 'f5695.qmid_hp': False},
        {'f5695.line30': ('refusal', 'f5695.hp_no_qmid')},
        f"a heat pump costing $1,000 without a QMID, filing status {status} (the other inputs those of "
        f"{STATUS_BASES[status]}, with the Form 5695 answers above). The separate-homes question concerns spouses filing "
        f"jointly and is not asked; line 30 carries the heat pump's QMID refusal through line 29h ({I} p. 1, Qualified "
        f"manufacturer identification numbers; record taken from the evaluator once its gate was confirmed).",
        base_over=over)

write(MUT, build(rows), 'mutation.m4.f5695.')
