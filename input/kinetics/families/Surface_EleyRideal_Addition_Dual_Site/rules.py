#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/rules"
shortDesc = ""
longDesc = """
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 1,
    label = "Adsorbate1;Gas;VacantSite1",
    kinetics = StickingCoefficientBEP(A=5e-06, n=0, alpha=0, E0=(68.66,'kJ/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Default""",
    longDesc = 
"""
E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205
""",
)

entry(
    index = 2,
    label = "*H;O=C=O;VacantSite1",
    kinetics = StickingCoefficientBEP(A=3.08123e-05, n=0.253, alpha=0.5, E0=(107800,'J/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
R13 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948
""",
)

