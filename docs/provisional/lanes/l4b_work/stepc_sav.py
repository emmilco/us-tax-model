import sys; sys.path.insert(0,'/tmp/l4b')
from bank import Bank
F='For this person (you, or your spouse on a joint return) — '
END=' A return with this is outside what this tool prepares; a Yes ends the interview here.'
b=Bank()
b.set('person.sav_student',order=315,seq=1,
  prompt=F+'Were you a full-time student during any part of five calendar months of 2025?',
  help='Technical, trade and mechanical schools count, and so does a full-time on-farm training course given by a school or a government agency. On-the-job training, correspondence schools and schools that teach only over the internet do not.')
b.set('person.sav_claimed',order=315,seq=2,
  help="Answer Yes only if someone actually claims you on their 2025 return, not merely could.")
b.set('person.sav_roth',order=315,seq=3,
  prompt=F+'How much did you put into a Roth IRA for 2025, in 2025 or by the deadline for your 2025 return? Do not count rollovers or conversions.',
  help='A contribution you later moved to a traditional IRA (recharacterized) is a traditional IRA contribution, not a Roth one.')
b.set('person.sav_voluntary',order=315,seq=4,
  prompt=F+'How much of your own after-tax money did you choose to put into a retirement plan at work for 2025? It may be shown in box 14 of your Form W-2.',
  help='Do not count Roth contributions, contributions your employer requires of you, or contributions your employer pays for you. The federal Thrift Savings Plan counts as a plan.')
b.set('person.sav_able',order=315,seq=5,
  prompt=F+'Is an ABLE account held for you, and did you put money into it for 2025, or get money out of it in 2023 or later?',
  help=END.strip())
b.set('person.sav_excess',order=315,seq=6,
  prompt=F+'Did you put more of your pay into retirement plans at work in 2025 than the yearly limit (for a 401(k), $23,500 plus any catch-up amount your plan allows)?',
  help='Box 12 of each Form W-2 shows what you put in. Your plan administrator tells you if you went over the limit.')
b.set('person.sav_prior_joint',order=315,seq=7); b.set('person.sav_prior_other',order=315,seq=8)
b.save()
