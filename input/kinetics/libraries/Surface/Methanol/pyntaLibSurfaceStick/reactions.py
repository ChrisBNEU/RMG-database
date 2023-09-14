
entry(
    index = 2,
    label = "O[Pt] + X <=> [Pt] + O=[Pt]",
    kinetics = SurfaceArrhenius(
        A = (2.186588e+15, 'm^2/(mol*s)'),
        n = 0.638,
        Ea=(159.22, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R2""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 4,
    label = "O=C=[Pt] + [Pt] <=> O=C[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (1.446484e+19, 'm^2/(mol*s)'),
        n = -0.793,
        Ea=(97.6, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R4""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 7,
    label = "O=C=O + X + X <=> O=C=[Pt] + O=[Pt]",
    kinetics = StickingCoefficient(
        A = 1.726497e-08,
        n = 1.407,
        Ea=(155.47, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R7""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 9,
    label = "O + X + X <=> O[Pt] + [Pt]",
    kinetics = StickingCoefficient(
        A = 1.533035e-08,
        n = 1.399,
        Ea=(99.69, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R9""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 11,
    label = "CO[Pt] + X <=> OC[Pt] + X",
    kinetics = SurfaceArrhenius(
        A = (2.158285e+14, 'm^2/(mol*s)'),
        n = 1.991,
        Ea=(307.6, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R11""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 13,
    label = "O=C=O + [Pt] + X <=> O=CO[Pt] + X",
    kinetics = StickingCoefficient(
        A = 3.081230e-05,
        n = 0.253,
        Ea=(80.39, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R13""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 15,
    label = "OCO[Pt] + X + X <=> [Pt] + [Pt]OCO[Pt]",
    kinetics = SurfaceArrhenius(
        A = (1.325104e+18, 'm^4/(mol^2*s)'),
        n = 0.948,
        Ea=(120.34, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R15""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 17,
    label = "C=O + N=[Pt] + X <=> N#[Pt] + CO[Pt]",
    kinetics = StickingCoefficient(
        A = 6.056276e-11,
        n = 1.826,
        Ea=(95.09, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R17""",
    metal = "Cu",
    facet = "111",
)
