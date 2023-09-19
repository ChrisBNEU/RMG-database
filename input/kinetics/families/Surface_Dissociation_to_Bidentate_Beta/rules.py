#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Combined;VacantSite1;VacantSite2",
    kinetics = SurfaceArrheniusBEP(
        A=(1.3251e+18,'m^4/(mol^2*s)'), 
        n=0.948, 
        alpha=0.5, 
        E0=(101330,'J/mol'), 
        Tmin=(200,'K'), 
        Tmax=(3000,'K')
        ),
    rank = 0,
    shortDesc = u"""Rate rule generated for uncertainty""",
    longDesc = u"""
Rate rule generated for uncertainty
""",
)

