#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration/rules"
shortDesc = u""
longDesc = u"""
Surface species migrating where it binds to the surface
"""
entry(
    index = 1,
    label = "Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A=(1.992037e+15,'s^-1'),
        n=-0.322, 
        alpha=0.5, 
        E0=(182137,'J/mol'), 
        Tmin=(200,'K'), 
        Tmax=(3000,'K')
        ),
    rank = 0,
    shortDesc = """Rate rule generated for uncertainty""",
    longDesc = 
"""
R10 from table 1 in Pynta─An Automated Workflow for Calculation of Surface and Gas-Surface Kinetics Johnson et al. https://doi/full/10.1021/acs.jcim.3c00948
multiply by copper surface site density to get similar rate (2.943e-05)
""",
)
