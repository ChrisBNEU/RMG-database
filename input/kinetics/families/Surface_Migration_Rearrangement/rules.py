#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration_Rearrangement/rules"
shortDesc = u""
longDesc = u"""
Surface species migrating where it binds to the surface
only difference between this and Surface_Migration is the fact that it depends 
on 2 sites instead of 1. 
"""
entry(
    index = 1,
    label = "Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (50, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205 sort of,
    but mostly made up -E"""
)

entry(
    index = 2,
    label = "*COH",
    kinetics = SurfaceArrheniusBEP(
        A = (0.0001124, 'm^2/(molecule*s)'),
        n = -0.322,
        alpha = 0.5,
        E0=(210.76, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
    from Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics
    Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948"""
)
