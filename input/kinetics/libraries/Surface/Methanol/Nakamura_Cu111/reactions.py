""""""

name = "Nakamura_Cu111"
shortDesc = u""
longDesc = u"""
co2 adsorption via eley-rideal mechanism with adsorbed h
https://doi.org/10.1038/s41557-019-0282-1

Ea from https://doi.org/10.1021/jacs.2c02797
"""

entry(
    index = 1,
    label = "CO2 + HX <=> HCOOX",
    kinetics = StickingCoefficient(
        A = 0.5,
        n = 0,
        Ea=(55.6, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1""",
	metal = "Pt",
)
