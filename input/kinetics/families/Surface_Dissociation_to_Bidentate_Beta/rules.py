#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Combined;VacantSite1;VacantSite2",
    kinetics = SurfaceArrheniusBEP(A=(1.3251e+18,'m^4/(mol^2*s)'), n=0.948, alpha=0.5, E0=(101330,'J/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
R15 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948
""",
)

