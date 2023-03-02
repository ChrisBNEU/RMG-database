#!/usr/bin/env python
# encoding: utf-8

name = "Bimolec_Hydroperoxide_Decomposition/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["Root"], products=["ROOrad", "ROrad", "H2O"], ownReverse=False)

reverse = "Peroxyl_alkoxy_association"
reversible = True

reactantNum = 2

productNum = 3

autoGenerated = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*4', '1'],
])

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *1 O u0 {2,S} {5,S}
2 *2 O u0 {1,S} {6,S}
3    O u0 {4,S} {7,S}
4 *4 O u0 {3,S} {8,S}
5    R u0 {1,S}
6    H u0 {2,S}
7    R u0 {3,S}
8 *3 H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_5R-inRing",
    group = 
"""
1 *1 O u0 r0 {2,S} {5,S}
2 *2 O u0 r0 {1,S} {6,S}
3    O u0 r0 {4,S} {7,S}
4 *4 O u0 r0 {3,S} {8,S}
5    R u0 r1 {1,S}
6    H u0 r0 {2,S}
7    R u0 {3,S}
8 *3 H u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_N-5R-inRing",
    group = 
"""
1 *1 O u0 {2,S} {5,S}
2 *2 O u0 {1,S} {6,S}
3    O u0 {4,S} {7,S}
4 *4 O u0 {3,S} {8,S}
5    R u0 r0 {1,S}
6    H u0 {2,S}
7    R u0 {3,S}
8 *3 H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_N-5R-inRing_5R->C",
    group = 
"""
1 *1 O u0 {2,S} {5,S}
2 *2 O u0 {1,S} {6,S}
3    O u0 {4,S} {7,S}
4 *4 O u0 {3,S} {8,S}
5    C u0 r0 {1,S}
6    H u0 {2,S}
7    C u0 {3,S}
8 *3 H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R",
    group = 
"""
1  *1 O   u0 {2,S} {5,S}
2  *2 O   u0 {1,S} {6,S}
3     O   u0 {4,S} {7,S}
4  *4 O   u0 {3,S} {8,S}
5     C   u0 r0 {1,S}
6     H   u0 {2,S}
7     C   u0 r0 {3,S} {9,S}
8  *3 H   u0 {4,S}
9     C   u0 r0 {7,S} {10,[S,D,T,B,Q]}
10    R!H ux {9,[S,D,T,B,Q]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_N-5R-inRing_N-5R->C",
    group = 
"""
1 *1 O u0 {2,S} {5,S}
2 *2 O u0 {1,S} {6,S}
3    O u0 {4,S} {7,S}
4 *4 O u0 {3,S} {8,S}
5    H u0 r0 {1,S}
6    H u0 {2,S}
7    R u0 r0 {3,S}
8 *3 H u0 {4,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_5R-inRing
    L2: Root_N-5R-inRing
        L3: Root_N-5R-inRing_5R->C
            L4: Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R
        L3: Root_N-5R-inRing_N-5R->C
"""
)

