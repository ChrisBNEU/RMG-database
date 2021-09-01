#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C8H9"
shortDesc = u"Phenyl radical ethylene addition and H-abstraction"
longDesc = u"""
Combined Quantum Chemical/RRKM-ME Computational Study of the Phenyl + Ethylene, Vinyl + Benzene, and H + Styrene Reactions
I. V. Tokmakov and M. C. Lin
J. Phys. Chem. A 2004, 108, 9697-9714

Calculations were performed at the G2M(RCC5)//B3LYP method. Te-Chun Chu et al. recalculated TST rates in Arkane and used LAS/MBMS experiments to validate this PES in Green group.
"""
autoGenerated=False
entry(
    index = 0,
    label = "C2H4 + C6H5 <=> i1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4600, 'cm^3/(mol*s)'),
        n = 2.623,
        Ea = (1.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.06942, dn = +|- 0.00850785, dEa = +|- 0.0565298 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.06942, dn = +|- 0.00850785, dEa = +|- 0.0565298 kJ/mol
""",
)

entry(
    index = 1,
    label = "i1 <=> i2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.128e-05, 's^-1'),
        n = 5.076,
        Ea = (22.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1108.87, dn = +|- 0.888795, dEa = +|- 5.90553 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1108.87, dn = +|- 0.888795, dEa = +|- 5.90553 kJ/mol
""",
)

entry(
    index = 2,
    label = "i1 <=> i3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.5824, 's^-1'),
        n = 3.511,
        Ea = (21.858, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 30.5782, dn = +|- 0.433589, dEa = +|- 2.88095 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 30.5782, dn = +|- 0.433589, dEa = +|- 2.88095 kJ/mol
""",
)

entry(
    index = 3,
    label = "i1 <=> i4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.549e+08, 's^-1'),
        n = 1.082,
        Ea = (14.314, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.07842, dn = +|- 0.00957029, dEa = +|- 0.0635891 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.07842, dn = +|- 0.00957029, dEa = +|- 0.0635891 kJ/mol
""",
)

entry(
    index = 4,
    label = "i1 <=> i5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.457e+08, 's^-1'),
        n = 1.06,
        Ea = (30.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.01413, dn = +|- 0.00177913, dEa = +|- 0.0118213 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.01413, dn = +|- 0.00177913, dEa = +|- 0.0118213 kJ/mol
""",
)

entry(
    index = 5,
    label = "i1 <=> C6H5C2H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.472e+07, 's^-1'),
        n = 1.813,
        Ea = (33.679, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 2.27608, dn = +|- 0.104262, dEa = +|- 0.692764 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 2.27608, dn = +|- 0.104262, dEa = +|- 0.692764 kJ/mol
""",
)

entry(
    index = 6,
    label = "i2 <=> C6H5C2H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.718e+08, 's^-1'),
        n = 1.438,
        Ea = (44.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 2.35307, dn = +|- 0.108479, dEa = +|- 0.720783 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 2.35307, dn = +|- 0.108479, dEa = +|- 0.720783 kJ/mol
""",
)

entry(
    index = 7,
    label = "C6H5C2H3 + H <=> i6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.287e+06, 'cm^3/(mol*s)'),
        n = 1.915,
        Ea = (6.704, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.65308, dn = +|- 0.0637195, dEa = +|- 0.423379 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.65308, dn = +|- 0.0637195, dEa = +|- 0.423379 kJ/mol
""",
)

entry(
    index = 8,
    label = "C6H5C2H3 + H <=> i7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.932e+07, 'cm^3/(mol*s)'),
        n = 1.726,
        Ea = (3.815, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.29365, dn = +|- 0.0326388, dEa = +|- 0.216866 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.29365, dn = +|- 0.0326388, dEa = +|- 0.216866 kJ/mol
""",
)

entry(
    index = 9,
    label = "C6H5C2H3 + H <=> i8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.393e+07, 'cm^3/(mol*s)'),
        n = 1.812,
        Ea = (5.116, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.41307, dn = +|- 0.0438329, dEa = +|- 0.291244 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.41307, dn = +|- 0.0438329, dEa = +|- 0.291244 kJ/mol
""",
)

entry(
    index = 10,
    label = "C6H5C2H3 + H <=> i9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 1.817,
        Ea = (4.637, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.45824, dn = +|- 0.0478213, dEa = +|- 0.317745 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.45824, dn = +|- 0.0478213, dEa = +|- 0.317745 kJ/mol
""",
)

entry(
    index = 11,
    label = "i2 <=> i3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.308e-17, 's^-1'),
        n = 8.362,
        Ea = (44.593, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 475564, dn = +|- 1.65717, dEa = +|- 11.0109 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 475564, dn = +|- 1.65717, dEa = +|- 11.0109 kJ/mol
""",
)

entry(
    index = 12,
    label = "C2H4 + C6H5 <=> C6H6 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.157, 'cm^3/(mol*s)'),
        n = 4.094,
        Ea = (4.882, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 3.72812, dn = +|- 0.166817, dEa = +|- 1.1084 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 3.72812, dn = +|- 0.166817, dEa = +|- 1.1084 kJ/mol
""",
)

entry(
    index = 13,
    label = "C6H6 + C2H3 <=> i6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (15120, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (7.179, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 12 data points; dA = *|/ 1.03282, dn = +|- 0.00409364, dEa = +|- 0.0271999 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 12 data points; dA = *|/ 1.03282, dn = +|- 0.00409364, dEa = +|- 0.0271999 kJ/mol
""",
)

