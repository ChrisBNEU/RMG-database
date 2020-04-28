#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen"
shortDesc = u""
longDesc = u"""
Nitrogen surface reactions that are too specific to make families for.
"""

entry(
    index = 2,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 0.011,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NH3 Surface Adsorption vdW""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R2
    metal = 'Ni'
    """
)

entry(
    index = 3,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1.0e-6,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Adsorption Dissociative""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R3
    metal = 'Ni'
    """
)

# todo: this one throws TypeError: 'NoneType' object is not subscriptable
# entry(
#     index = 7,
#     label = "N_X + N_X <=> N2 + X + X",
#     kinetics = SurfaceArrehnius(
#         A = (4.02e14, 'm^2/(mol*s)'),
#         n = 0,
#         Ea=(113.9, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""N2 Adsorption Dissociative""",
#     longDesc = u"""
#     Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
#     Xu, Clayton, Balakotaiah, Harold et al.
#     doi: 10.1016.j.apcatb.2007.08.008
#
#     This is R7
#     metal = 'Pt'
#     """
# )

entry(
    index = 51,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (5e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(107.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NO Adsorption Dissociative""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f

    is supposedly only valid for a Pt/Rh ratio of 75%/25%

    This is R51
    metal = 'Pt'
    """
)
