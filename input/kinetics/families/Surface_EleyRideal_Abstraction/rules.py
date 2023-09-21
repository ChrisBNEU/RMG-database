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
    kinetics = StickingCoefficientBEP(A=6.05628e-11, n=1.826, alpha=0.5, E0=(87810.2,'J/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
R17 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948
""",
)

