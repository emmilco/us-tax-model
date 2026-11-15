import re,sys
p='forms/ny/2025/ny_it201.yaml'; s=open(p).read()
def T(x,v): return '{ op: test, eq: ["%s", { const: %s }] }'%(x,v)
def ch(g,a,b): return '{ op: choose, alternatives: [{ guard: %s, then: "%s" }, { guard: %s, then: "%s" }] }'%(T(g,'true'),a,T(g,'false'),b)
cite29=re.search(r"    - id: ny_it201.pension_exclusion_line\n(?:      .*\n)*?      (cite: .*)\n",s).group(1)
s=s.replace("    - id: ny_it201.gate.line29\n","""    - id: ny_it201.pension_exclusion_after_gov
      printed: '(helper)'
      label: 'The pension exclusion may apply, once the government pension questions are answered No (a government pension is refused on line 26)'
      type: Bool
      expr: %s
      %s
    - id: ny_it201.gate.line29
"""%(ch("ny_it201.gov_pension_any","ny_it201.no","ny_it201.pension_exclusion_line"),cite29),1)
m=re.search(r"(    - id: ny_it201.gate.line29\n(?:      (?!expr).*\n)*?)      expr:.*\n(?:        .*\n)*",s)
s=s.replace(m.group(0), m.group(1)+"      expr: %s\n"%ch("ny_it201.has_pension_income","ny_it201.pension_exclusion_after_gov","ny_it201.no"))
open(p,'w').write(s); print("ok")
