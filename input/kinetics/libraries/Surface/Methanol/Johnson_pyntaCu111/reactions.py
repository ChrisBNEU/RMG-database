

""""""
name = "Johnson_pyntaCu111"
shortDesc = u""
longDesc = u"""
from Pynta─An Automated Workflow for Calculation of Surface and Gas–Surface Kinetics
by our very own Matt Johnson et al.
https://pubs.acs.org/doi/full/10.1021/acs.jcim.3c00948
"""
entry(
    index = 1,
    label = "O=[Pt] + [Pt] <=> X + O[Pt]",
    kinetics = SurfaceArrhenius(
        A = (2.452e-07, 'm^2/(molecule*s)'),
        n = 0.335,
        Ea=(88.36, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 2,
    label = "X + O=C[Pt] <=> O=C=[Pt] + [Pt]",
    kinetics = SurfaceArrhenius(
        A = (3.557e-06, 'm^2/(molecule*s)'),
        n = -0.381,
        Ea=(18.26, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

# h migration, not sure if we can use as is (maybe in kmc)
# entry(
#     index = 3,
#     label = "[Pt] + X <=> [Pt] + X",
#     kinetics = SurfaceArrhenius(
#         A = (8.66e-07, 'm^2/(molecule*s)'),
#         n = 0.019,
#         Ea=(12.44, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Value from pynta paper""",
#     longDesc = u"""R1""",
#     metal = "Cu",
#     facet = "111",
# )

entry(
    index = 4,
    label = "O=[Pt] + O=C=[Pt] <=> X + X + O=C=O",
    kinetics = SurfaceArrhenius(
        A = (6.289e-08, 'm^2/(molecule*s)'),
        n = 0.027,
        Ea=(42.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

# sticking coefficient rxn
entry(
    index = 5,
    label = "O[Pt] + [Pt] <=> O + X + X",
    kinetics = SurfaceArrhenius(
        A = (0.0001412, 'm^2/(molecule*s)'),
        n = -0.634,
        Ea=(104.21, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 6,
    label = "OC[Pt] + X <=> CO[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (0.0001124, 'm^2/(molecule*s)'),
        n = -0.322,
        Ea=(210.76, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 7,
    label = "O=CO[Pt] + X <=> O=C=O + [Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (1.608e-09, 'm^2/(molecule*s)'),
        n = 0.678,
        Ea=(50.4, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 8,
    label = "[Pt] + [Pt]OCO[Pt] <=> OCO[Pt] + X  + X ",
    kinetics = SurfaceArrhenius(
        A = (1.315e-07, 'm^4/(molecule^2*s)'),
        n = 0.265,
        Ea=(73.73, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 9,
    label = "N#[Pt] + CO[Pt] <=> C=O + N=[Pt] + X ",
    kinetics = SurfaceArrhenius(
        A = (5.218e-14, 'm^2/(molecule*s)'),
        n = 2.674,
        Ea=(53.39, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    metal = "Cu",
    facet = "111",
)
