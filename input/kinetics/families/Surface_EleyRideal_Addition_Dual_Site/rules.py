#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/rules"
shortDesc = u""
longDesc = u"""
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 1,
    label = "Adsorbate1;Gas",
    kinetics = StickingCoefficientBEP(
        A = 5e-6,
        n = 0,
        alpha = 0,
        E0 = (68.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205"""
)


# Get reverse rate
# converted to sticking coefficient: 
# A = 5.379e-43 m^5/(molecule*s)
# n = 0.753
# Ea = 80.39 kJ/mol

entry(
    index = 2,
    label = "*H;O=C=O",
    kinetics = StickingCoefficientBEP(
        #A = (5.379e-43, 'm^5/(molecule*s)'),
        # n = 0.753,
        # E0=(80.39, 'kJ/mol'),
        A = 5e-6,
        n = 0,
        alpha = 0,
        E0 = (68.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Value from pynta paper""",
    longDesc = u"""R1""",
    rank = 0,
)