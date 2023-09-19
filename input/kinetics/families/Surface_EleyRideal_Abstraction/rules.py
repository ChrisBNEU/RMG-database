#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/rules"
shortDesc = ""
longDesc = """
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 1,
    label = "Adsorbate1;Gas",
    kinetics = StickingCoefficientBEP(A=6.05628e-11, n=1.826, alpha=0.5, E0=(87810.2,'J/mol'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
Rate rule generated for uncertainty
""",
)

