#!/usr/bin/env python
# encoding: utf-8


# for now, focusing on adding in the normal, non=defect sites for 111 surfaces:
# 111 top site
# 111 bridge site
# 111 fcc hollow site
# 111 hcp hollow site

name = "Metal properties"
shortDesc = ""
longDesc = """

subsequent use for advanced scaling relations from Gao et al. in "Determining the 
adsorption energies of small molecules with the intrinsic properties of adsorbates 
and substrates", 2020, doi: 10.1038/s41467-020-14969-8

valence_electrons: number of valence electrons for the metal atom
electronegativity: pauling electronegativity of the metal atom (I assume in eV, 
not sure if it matters since it is a relative scale)
phi: 
"""

entry(
    index = 1,
    label = "Sc",
    metal = "Sc",
    valence_electrons = 3,
    electronegativity = 1.36,
    psi =  6.62,
    beta = 1,
)

entry(
    index = 2,
    label = "Ti",
    metal = "Ti",
    valence_electrons = 4,
    electronegativity = 1.54,
    psi =  10.39,
    beta = 1,
)

entry(
    index = 3,
    label = "V",
    metal = "V",
    valence_electrons = 5,
    electronegativity = 1.63,
    psi =  15.34,
    beta = 1,
)

entry(
    index = 4,
    label = "Cr",
    metal = "Cr",
    valence_electrons = 6,
    electronegativity = 1.66,
    psi =  21.69,
    beta = 1,
)

entry(
    index = 5,
    label = "Mn",
    metal = "Mn",
    valence_electrons = 7,
    electronegativity = 1.55,
    psi =  31.61,
    beta = 1,
)

entry(
    index = 6,
    label = "Fe",
    metal = "Fe",
    valence_electrons = 8,
    electronegativity = 1.83,
    psi =  34.97,
    beta = 1,
)

entry(
    index = 7,
    label = "Co",
    metal = "Co",
    valence_electrons = 9,
    electronegativity = 1.88,
    psi =  43.09,
    beta = 1,
)

entry(
    index = 8,
    label = "Ni",
    metal = "Ni",
    valence_electrons = 10,
    electronegativity = 1.91,
    psi =  52.36,
    beta = 1,
)

entry(
    index = 9,
    label = "Cu",
    metal = "Cu",
    valence_electrons = 11,
    electronegativity = 1.90,
    psi =  63.68,
    beta = 1,
)

entry(
    index = 10,
    label = "Zn",
    metal = "Zn",
    valence_electrons = 12,
    electronegativity = 1.65,
    psi =  87.27,
    beta = 1,
)

entry(
    index = 11,
    label = "Y",
    metal = "Y",
    valence_electrons = 3,
    electronegativity = 1.22,
    psi =  7.38,
    beta = 1,
)

entry(
    index = 12,
    label = "Zr",
    metal = "Zr",
    valence_electrons = 4,
    electronegativity = 1.33,
    psi =  12.03,
    beta = 1,
)

entry(
    index = 13,
    label = "Nb",
    metal = "Nb",
    valence_electrons = 5,
    electronegativity = 1.60,
    psi =  15.63,
    beta = 1,
)

entry(
    index = 14,
    label = "Mo",
    metal = "Mo",
    valence_electrons = 6,
    electronegativity = 1.16,
    psi =  31.03,
    beta = 1,
)

entry(
    index = 15,
    label = "Tc",
    metal = "Tc",
    valence_electrons = 7,
    electronegativity = 1.90,
    psi =  25.79,
    beta = 1,
)

entry(
    index = 16,
    label = "Ru",
    metal = "Ru",
    valence_electrons = 8,
    electronegativity = 2.20,
    psi =  29.09,
    beta = 1,
)

entry(
    index = 17,
    label = "Rh",
    metal = "Rh",
    valence_electrons = 9,
    electronegativity = 2.28,
    psi =  35.53,
    beta = 1,
)

entry(
    index = 18,
    label = "Pd",
    metal = "Pd",
    valence_electrons = 10,
    electronegativity = 2.20,
    psi =  45.45,
    beta = 1,
)

entry(
    index = 19,
    label = "Ag",
    metal = "Ag",
    valence_electrons = 11,
    electronegativity = 1.93,
    psi =  87.10,
    beta = 1,
)

entry(
    index = 20,
    label = "Cd",
    metal = "Cd",  
    valence_electrons = 12,
    electronegativity = 1.69,
    psi =  85.21,
    beta = 1,
)

entry(
    index = 21,
    label = "La",
    metal = "La",
    valence_electrons = 3,
    electronegativity = 1.10,
    psi =  8.18,
    beta = 1,
)

entry(
    index = 22,
    label = "Hf",
    metal = "Hf",
    valence_electrons = 4,
    electronegativity = 1.30,
    psi =  12.31,
    beta = 1,
)

entry(
    index = 23,
    label = "Ta",
    metal = "Ta",
    valence_electrons = 5,
    electronegativity = 1.50,
    psi =  16.67,
    beta = 1,
)

entry(
    index = 24,
    label = "W",
    metal = "W",
    valence_electrons = 6,
    electronegativity = 2.36,
    psi =  15.25,
    beta = 1,
)

entry(
    index = 25,
    label = "Re",
    metal = "Re",
    valence_electrons = 7,
    electronegativity = 1.90,
    psi =  25.79,
    beta = 1,
)

entry(
    index = 26,
    label = "Os",
    metal = "Os",
    valence_electrons = 8,
    electronegativity = 2.20,
    psi =  29.09,
    beta = 1,
)

entry(
    index = 27,
    label = "Ir",
    metal = "Ir",
    valence_electrons = 9,
    electronegativity = 2.20,
    psi =  36.82,
    beta = 1,
)

entry(
    index = 28,
    label = "Pt",
    metal = "Pt",
    valence_electrons = 10,
    electronegativity = 2.28,
    psi =  43.86,
    beta = 1,
)

entry(
    index = 29,
    label = "Au",
    metal = "Au",
    valence_electrons = 11,
    electronegativity = 2.54,
    psi =  75.92,
    beta = 1,
)

entry(
    index = 30,
    label = "Hg",
    metal = "Hg",
    valence_electrons = 12,
    electronegativity = 2.00,
    psi =  72,
    beta = 1,
)