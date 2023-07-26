#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/rules"
shortDesc = ""
longDesc = """
A vdW species splitting, adsorbing to the surface, 
and transferring a functional group to a single bonded surface species.
"""
entry(
    index = 1,
    label = "Donating;Abstracting",
    kinetics = SurfaceArrheniusBEP(A=(1e+13,'m^2/(mol*s)'), n=0, alpha=0.5, E0=(0,'kcal/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Default""",
    longDesc = 
"""
Made up
""",
)

entry(
    index = 2,
    label = "C-OH;*C=R",
    kinetics = SurfaceArrheniusBEP(A=(1e+17,'cm^2/(mol*s)'), n=0, alpha=0.5, E0=(0,'kcal/mol')),
    rank = 1,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
Rate rule generated for uncertainty
""",
)


