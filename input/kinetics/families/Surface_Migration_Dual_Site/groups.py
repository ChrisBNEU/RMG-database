#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration_Dual_Site/groups"
shortDesc = u""
longDesc = u"""
Surface species migrating where it binds to the surface. dependent on 2 surface 
sites instead of one like in Surface_Migration.

     *4                                     *4
      |                                      |
 *2--*3   +                             +   *2--*3
  |                    ---->                     |
~*1~          ~*5~               ~*1~          ~*5~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s).

"""

template(reactants=["Adsorbate1", "VacantSite1"], products=["Adsorbate2", "VacantSite2"], ownReverse=True)

reverse = "Surface_Migration_Rearrangement_Reverse"

reactantNum=2
productNum=2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*5', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 X   ux px cx {2,S}
2 *2 R!H ux px cx {1,S} {3,[S,D]}
3 *3 R!H ux px cx {2,[S,D]} {4,S}
4 *4 R   ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *5 Xv u0
""",
    kinetics = None,
)


entry(
    index = 3,
    label="*C",
    group =
"""
1 *1 X   ux px cx {2,S}
2 *2 C   ux px cx {1,S} {3,[S,D]}
3 *3 R!H ux px cx {2,[S,D]} {4,S}
4 *4 R   ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="*CC",
    group =
"""
1 *1 X ux px cx {2,S}
2 *2 C ux px cx {1,S} {3,[S,D]}
3 *3 C ux px cx {2,[S,D]} {4,S}
4 *4 R ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "*CO",
    group =
"""
1 *1 X   ux px cx {2,S}
2 *2 C   ux px cx {1,S} {3,S}
3 *3 O   ux px cx {2,S} {4,S}
4 *4 R   ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "*COH",
    group =
"""
1 *1 X   u0 p0 c0 {2,S}
2 *2 C   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 O   u0 p2 c0 {2,S} {4,S}
4 *4 H   u0 p0 c0 {3,S}
5    H   u0 p0 c0 {2,S}
6    H   u0 p0 c0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: *C
        L3: *CC
        L3: *CO
            L4: *COH
L1: VacantSite1
""" 
)
