#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Eley Rideal reaction with a gas phase double, triple, or quadruple bonded species with a species (most likely hydrogen) directly bonded to the surface.

 *2-*3      *5=*4                    *2               *5-*4-*3
  |  +           +         ---->     ||       +        |    
~*1~               ~*6~             ~*1~             ~*6~

This family is almost the same as the Surface_EleyRideal_Addition_Multiple_Bond, 
Except that it includes the migration of the adsorbed species to a new site.

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol^2/s).
"""

template(reactants=["Adsorbate1", "Gas", "VacantSite1"], products=["Adsorbate2", "VacantSite2"], ownReverse=False)

reverse = "Surface_EleyRideal_Deletion_Dual_Site"

reactantNum=3
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*4', -1, '*5'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*5', 1, '*6'],

])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 X  ux px cx {2,[S,D,T]}
2 *2 R  ux px cx {1,[S,D,T]}, {3,S}
3 *3 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Gas",
    group =
"""
multiplicity [1]
1 *4 R!H u0 px cx {2,[D,T,Q]}
2 *5 R!H u0 px cx {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite1",
    group =
"""
1 *6 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate1
L1: Gas
"""
)