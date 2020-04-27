#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/rules"
shortDesc = u""
longDesc = u"""
Taken from training reactions.py
"""
entry(
    index = 1,
    label = "db;doublebond",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (4.66e+06, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.65,
        alpha = 0,
        E0 = (226.564, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
)

