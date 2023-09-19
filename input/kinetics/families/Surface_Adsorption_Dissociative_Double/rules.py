#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociation_Double/rules"
shortDesc = u""
longDesc = u"""
Dissociative adsorption of a gas-phase species forming two adsorbates, each with a double bond to a surface site
"""

entry(
    index = 1,
    label = "Adsorbate;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.01,
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 2,
    label = "CO2;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A=1.7265e-08, 
        n=1.407, 
        alpha=0.5, 
        E0=(138983,'J/mol'), 
        Tmin=(200,'K'), 
        Tmax=(3000,'K')
        ),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
Rate rule generated for uncertainty
""",
)

