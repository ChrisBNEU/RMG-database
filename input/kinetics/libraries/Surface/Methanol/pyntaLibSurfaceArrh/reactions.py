
entry(
    index = 1,
    label = "[Pt] + O=[Pt] <=> O[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (1.476594e+17, 'm^2/(mol*s)'),
        n = 0.335,
        Ea=(88.36, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 3,
    label = "O=C[Pt] + X <=> O=C=[Pt] + [Pt]",
    kinetics = SurfaceArrhenius(
        A = (2.142025e+18, 'm^2/(mol*s)'),
        n = -0.381,
        Ea=(18.26, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R3 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 5,
    label = "[Pt] + X <=> [Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (5.215052e+17, 'm^2/(mol*s)'),
        n = 0.019,
        Ea=(12.44, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R5 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 6,
    label = "O=C=[Pt] + O=[Pt] <=> O=C=O + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.787236e+16, 'm^2/(mol*s)'),
        n = 0.027,
        Ea=(42.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R6 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 8,
    label = "O[Pt] + [Pt] <=> O + X + X",
    kinetics = SurfaceArrhenius(
        A = (8.503064e+19, 'm^2/(mol*s)'),
        n = -0.634,
        Ea=(104.21, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R8 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 10,
    label = "OC[Pt] + X <=> CO[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (6.768728e+19, 'm^2/(mol*s)'),
        n = -0.322,
        Ea=(210.76, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R10 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 12,
    label = "O=CO[Pt] + X <=> O=C=O + [Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (9.683376e+14, 'm^2/(mol*s)'),
        n = 0.678,
        Ea=(50.4, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R12 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 14,
    label = "[Pt] + [Pt]OCO[Pt] <=> OCO[Pt] + X + X",
    kinetics = SurfaceArrhenius(
        A = (7.918930e+16, 'm^2/(mol*s)'),
        n = 0.265,
        Ea=(73.73, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R14 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 16,
    label = "N#[Pt] + CO[Pt] <=> C=O + N=[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (3.142280e+10, 'm^2/(mol*s)'),
        n = 2.674,
        Ea=(53.39, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R16 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948""",
    metal = "Cu",
    facet = "111",
)
