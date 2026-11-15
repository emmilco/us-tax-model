# Lane 8b wording: education (orders 240 to 243) and student loan interest (244).
REFUSE = ' A Yes is outside what this tool prepares and ends the interview here.'
ENTRIES = {
 'f8863.paid': dict(order=240, seq=1,
   prompt='In 2025, was tuition paid for you (or, on a joint return, your spouse) or for a dependent you claim, at a college, university or trade school?',
   help='Count tuition paid by anyone, including with a loan or a scholarship, and a required fee or required course materials even where no tuition was charged. Only education after high school counts.'),
 'f8863.ban': dict(order=242, seq=1,
   prompt='Has the IRS ever denied or reduced an American opportunity credit you claimed, for more than a math error, or barred you from claiming it?',
   help='Answer No if you filed Form 8862 with your 2024 return and the credit was then allowed, or if a bar has run out: it lasts 2 years after a finding of reckless or intentional disregard of the rules, 10 years after a finding of fraud.' + REFUSE),
 'sli.any': dict(order=244, seq=1,
   help='A loan taken out to pay for college or trade school. If you are not sure whether a loan counts, answer Yes: the questions that follow sort it out.'),
 'sli.interest': dict(order=244, seq=2,
   help='A lender may send no form for a small amount of interest; its year-end statement shows what you paid.'),
 'sli.unqualified_any': dict(order=244, seq=3,
   help='School costs are tuition, fees, room and board, books, supplies and the like, for a degree or certificate program. Someone you could have claimed as a dependent but for that person\'s income or joint return, or because you could be claimed yourself, counts as your dependent here.'),
 'sli.unqualified': dict(order=244, seq=4),
 'sli.assisted_any': dict(order=244, seq=5,
   help='The programs are the National Health Service Corps Loan Repayment Program and state programs that repay or forgive loans for work where health services are short.'),
 'sli.assisted': dict(order=244, seq=6),
 'person.edu_born_2007': dict(order=243, seq=1),
 'person.edu_born_2002': dict(order=243, seq=2),
 'person.edu_half_support': dict(order=243, seq=3,
   prompt='For this person (you, or your spouse on a joint return) — In 2025, was your pay from work less than half of your support, meaning what your food, housing, clothing, medical care, education and the like cost?',
   help='Pay from work is wages, salaries, fees and other pay for services, including the part of a scholarship paid for teaching or research. Support counts whoever paid for it; a scholarship is not support if you were a full-time student.'),
 'person.edu_fulltime': dict(order=243, seq=4,
   prompt='For this person (you, or your spouse on a joint return) — Were you a full-time student during some part of at least five months of 2025?',
   help='At a college, university or trade school. A full-time on-farm training course given by such a school or by a state, county or local government agency also counts. The months need not be in a row.'),
 'person.edu_parent': dict(order=243, seq=5),
}
INSERT_AFTER = {'sli.any': 'sli.interest', 'sli.unqualified_any': 'sli.any', 'sli.unqualified': 'sli.unqualified_any',
                'sli.assisted_any': 'sli.unqualified', 'sli.assisted': 'sli.assisted_any'}
O = 241
TWINS = {
 'edu': dict(order=O, seq=1,
   prompt='In 2025, was tuition or a required fee paid for this person as a student at a college, university or trade school?',
   help='The school must be one that can take part in federal student aid; nearly every accredited college, university and trade school is.'),
 'edu_1098t': dict(order=O, seq=2,
   prompt='Did the school send this person a Form 1098-T (Tuition Statement) for 2025?',
   help='Answer Yes also if the school did not have to send one (for example, scholarships paid everything, or the courses gave no academic credit), or if it was asked for after February 2, 2026, the school was given what it needed to prepare it, and the enrollment and the payments can be shown.'),
 'edu_inst': dict(order=O, seq=9,
   prompt='How much was paid to the school in 2025 for this person\'s tuition and required fees? (Form 1098-T box 1 shows what the school received.)',
   help='''Use what was actually paid, by anyone, for terms that began in 2025 or in January to March 2026. Books, supplies and equipment count here only if they had to be bought from the school.

Leave out:
- room and board, insurance, medical costs (student health fees too) and transportation
- amounts paid with a tax-free withdrawal from a 529 plan or a Coverdell account
- amounts deducted elsewhere on this return
- courses in sports, games or hobbies, and courses without credit, unless they are part of the degree program (or, for a student who cannot get the American opportunity credit, they improve job skills)'''),
 'edu_a2025': dict(order=O, seq=11,
   prompt='How much tax-free help with these school costs came in during 2025: scholarships and grants (Form 1098-T box 5), an employer\'s tuition assistance, veterans\' education benefits?',
   help='Count only the tax-free part; a Pell grant is a grant. Leave out loans, gifts, inheritances, savings, wages, emergency financial aid grants, and any scholarship reported as income on a tax return.'),
 'edu_a2026': dict(order=O, seq=12,
   prompt='How much more of that tax-free help has come in during 2026, so far, for the same school terms?'),
 'edu_refunds': dict(order=O, seq=13,
   prompt='How much of the tuition and fees paid in 2025 has the school refunded, in 2025 or so far in 2026?'),
 'edu_over': dict(order=O, seq=14,
   prompt='Was there a school term for which the tax-free help and the refunds came to more than that term\'s tuition, required fees and required course materials?',
   help='With one term in the year, answer by that term alone.' + REFUSE),
 'edu_line23': dict(order=O, seq=3,
   prompt='Has the American opportunity credit already been claimed for this person, by anyone, in four tax years before 2025?',
   help='It is the main tax credit for the first four years of college. For a student who first went to college in 2022 or later, the answer is No.'),
 'edu_line24': dict(order=O, seq=4,
   prompt='For at least one term that began in 2025, was this person\'s enrollment at least half-time, in a program leading to a degree or certificate? (Form 1098-T box 8 is checked if so.)',
   help='A term that began in January to March 2026 also counts if it was paid for in 2025.'),
 'edu_line25': dict(order=O, seq=5,
   prompt='Were this person\'s first four years of college already complete before 2025 began, by the school\'s count of academic credit?',
   help='Credit awarded only for passing proficiency examinations is not counted.'),
 'edu_line26': dict(order=O, seq=6,
   prompt='By the end of 2025, was there a federal or state felony conviction of this person for possessing or distributing a controlled substance (illegal drugs)?'),
 'edu_ein': dict(order=O, seq=7,
   prompt='Is the school\'s employer identification number (EIN) at hand? Form 1098-T shows it, and the school can give it.'),
 'edu_tin_issued': dict(order=O, seq=8,
   prompt='Had this person\'s social security number, ITIN or ATIN actually been issued by the due date of your 2025 return, extensions included?',
   help='Answer No if a number had only been applied for by then, even if it has come or will come later.'),
 'edu_mat': dict(order=O, seq=10,
   prompt='How much was spent in 2025 on books, supplies and equipment needed for this person\'s courses, bought anywhere but from the school?',
   help='Leave out what is left out of tuition: anything paid with a tax-free 529 plan or Coverdell withdrawal or deducted elsewhere on this return.'),
}
DEPENDENT_ONLY = ['edu_tin_issued']
