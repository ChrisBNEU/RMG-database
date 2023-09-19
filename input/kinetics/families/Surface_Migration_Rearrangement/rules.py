#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration_Rearrangement/rules"
shortDesc = ""
longDesc = """
Surface species migrating where it binds to the surface
only difference between this and Surface_Migration is the fact that it depends 
on 2 sites instead of 1.
"""
entry(
    index = 1,
    label = "Adsorbate1",
    kinetics = SurfaceArrheniusBEP(A=(6.76873e+19,'m^2/(mol*s)'), n=-0.322, alpha=0.5, E0=(182137,'J/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
Rate rule generated for uncertainty
""",
)

entry(
    index = 2,
    label = "*COH",
    kinetics = SurfaceArrheniusBEP(A=(0.0001124,'m^2/(molecule*s)'), n=-0.322, alpha=0.5, E0=(210.76,'kJ/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Default""",
    longDesc = 
"""
from Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics
    Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948
""",
)

