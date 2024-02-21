#!/usr/bin/env python
# encoding: utf-8

name = "Metal Binding Energies"
shortDesc = ""
longDesc = """

generalized coordination numbers first postulated by Calle-Vallejo et al. in 
"Fast Prediction of Adsorption Properties for Platinum Nanocatalysts with Generalized 
Coordination Numbers", 2014 doi: 10.1002/anie.201402958

subsequent use for advanced scaling relations from Gao et al. in "Determining the 
adsorption energies of small molecules with the intrinsic properties of adsorbates 
and substrates", 2020, doi: 10.1038/s41467-020-14969-8
"""

# sites: hollow: 
entry(
    index = 0,
    label = "111_fcc_hollow",
    facet = "111",
    site = "111_fcc_hollow",
    coordination_number = 6.955,
    shortDesc = """111 fcc hollow""",
    longDesc = 
"""
111 surface FCC hollow site. 
""",
)

entry(
    index = 1,
    label = "111_hcp_hollow",
    facet = "111",
    site = "111_hcp_hollow",
    coordination_number = 7.5,
    shortDesc = """111 hcp hollow""",
    longDesc = 
"""
111 surface HCP hollow site.
""",
)

entry(
    index = 2,
    label = "100_hollow",
    facet = "100",
    site = "100_hollow",
    coordination_number = 6.62,
    shortDesc = """100 hollow""",
    longDesc = 
"""
100 surface hollow site.
""",
)

# Sites: bridge
entry(
    index = 3,
    label = "111_bridge",
    facet = "111",
    site = "111_bridge",
    coordination_number =7.33,
    shortDesc = """111 bridge""",
    longDesc = 
"""
111 surface bridge site.
""",
)

entry(
    index = 4,
    label = "100_bridge",
    facet = "100",
    site = "100_bridge",
    coordination_number =6.67,
    shortDesc = """100 bridge""",
    longDesc = 
"""
100 surface bridge site.
""",
)

entry(
    index = 5,
    label = "211_100_edge_bridge",
    facet = "211",
    site = "211_100_edge_bridge",
    coordination_number =5.39,
    shortDesc = """211/100 step edge bridge""",
    longDesc = 
"""
bridge step edge site on 211 surface.
""",
)

###################### left off here
entry(
    index = 6,
    label = "553_111_edge_bridge",
    facet = "553",
    site = "553_111_edge_bridge",
    coordination_number = 5.44,
    shortDesc = """553/111 bridge step edge""",
    longDesc = 
"""
bridge step edge on 553/111 step edge.
""",
)

entry(
    index = 7,
    label = "211_kink_bridge", 
    facet = "211_DEFECT",
    site = "211_kink_bridge",
    coordination_number = 4.39, 
    shortDesc = """211 kink bridge site""",
    longDesc =
"""
bridge kink site on 211 surface.
""",
)

entry(
    index = 8,
    label = "2AD_100T_bridge",
    facet = "211_DEFECT",
    site = "2AD_100T_bridge",
    coordination_number = 3.11, 
    shortDesc = """2AD@100T bridge""",
    longDesc =
"""
bridge site with 2 metal adatoms on 100 surface.
""",
)

entry(
    index = 9,
    label = "2AD_111T_bridge",
    facet = "211_DEFECT",
    site = "2AD_111T_bridge",
    coordination_number = 2.83, 
    shortDesc = """2AD@111T bridge""",
    longDesc =
"""
bridge site with 2 metal adatoms on 111 terrace surface.
""",
)

entry(
    index = 10,
    label = "2AD_100E_bridge",
    facet = "211_DEFECT",
    site = "2AD_100E_bridge",
    coordination_number = 1.44, 
    shortDesc = """2AD@100E bridge""",
    longDesc =
"""
bridge site with 2 metal adatoms on 100 edge surface.
""",
)

# Sites: top
entry(
    index = 11,
    label = "532_111_edge_top", 
    facet = "532",
    site = "532_111_edge_top",
    coordination_number = 9.58, 
    shortDesc = """532/111 top step edge""",
    longDesc =
"""
top step site at bottom of 532/111 step.
""",
)

entry(
    index = 12,
    label = "553_111_edge_top",
    facet = "553",
    site = "553_111_edge_top",
    coordination_number = 9.50,
    shortDesc = """553/111 top step edge""",
    longDesc =
"""
top site at bottom of 553/111 step.
""",
)

entry(
    index = 13,
    label = "211_100_edge_top",
    facet = "211",
    site = "211_100_edge_top",
    coordination_number = 8.75, 
    shortDesc = """211/100 top step edge""",
    longDesc =
"""
top site at bottom of 211/100 step.
""",
)

entry(
    index = 14,
    label = "532_100_edge_top",
    facet = "532",
    site = "532_100_edge_top",
    coordination_number = 8.42,
    shortDesc = """532/100 top step edge""",
    longDesc =
"""
top site at bottom of 532/100 step.
""",
)

entry(
    index = 15,
    label = "111_top",
    facet = "111",
    site = "111_top",
    coordination_number = 7.5,
    shortDesc = """111 top""",
    longDesc =
"""
111 surface on-top site.
""",
)

entry(
    index = 16,
    label = "100_top",
    facet = "100",
    site = "100_top",
    coordination_number = 6.67,
    shortDesc = """100 top""",
    longDesc =
"""
100 surface on-top site.
""",
)

entry(
    index = 17,
    label = "110_top",
    facet = "110",
    site = "110_top",
    coordination_number = 5.83,
    shortDesc = """110 top""",
    longDesc =
"""
110 surface on-top site.
""",
)

entry(
    index = 18,
    label = "211_100_edge_top",
    facet = "211",
    site = "211_100_edge_top",
    coordination_number = 5.58,
    shortDesc = """211/100 top step edge""",
    longDesc =
"""
top site at bottom of 211/100 step.
""",
)

entry(  
    index = 19,
    label = "553_111_edge_top",
    facet = "553",
    site = "553_111_edge_top",
    coordination_number = 5.50,
    shortDesc = """553/111 top step edge""",
    longDesc =
"""
top site at bottom of 553/111 step.
""",
)

entry(
    index = 20,
    label = "532_kink_top", 
    facet = "532_DEFECT",
    site = "532_kink_top",
    coordination_number = 4.75,
    shortDesc = """532 kink top""",
    longDesc =
"""
kink top site on 532 surface.
""",
)

entry(
    index = 21,
    label = "211_kink_top",
    facet = "211_DEFECT",
    site = "211_kink_top",
    coordination_number = 4.67,
    shortDesc = """211 kink top""",
    longDesc =
"""
kink top site on 211 surface.
""",
)

entry(
    index = 22,
    label = "2AD_100T_top",
    facet = "100_DEFECT",
    site = "2AD_100T_top",
    coordination_number = 3.58,
    shortDesc = """2AD@100T top""",
    longDesc =
"""
top site with 2 metal adatoms on 100 surface.
""",
)

entry(
    index = 23,
    label = "1AD_100T_top",
    facet = "100_DEFECT",
    site = "1AD_100T_top",
    coordination_number = 3.00,
    shortDesc = """1AD@100T top""",
    longDesc =
"""
top site with 1 metal adatom on 100 surface.
""",
)

entry(
    index = 24,
    label = "2AD_111T_top",
    facet = "111_DEFECT",
    site = "2AD_111T_top",
    coordination_number = 2.92,
    shortDesc = """2AD@111T top""",
    longDesc =
"""
top site with 2 metal adatoms on 111 surface.
""",
)

entry(
    index = 25,
    label = "1AD_111T_top",
    facet = "111_DEFECT",
    site = "1AD_111T_top",
    coordination_number = 2.50,
    shortDesc = """1AD@111T top""",
    longDesc =
"""
top site with 1 metal adatom on 111 surface.
""",
)

entry(
    index = 26,
    label = "2AD_211_top",
    facet = "211_DEFECT",
    site = "2AD_211_top",
    coordination_number = 1.67,
    shortDesc = """2AD@211 top""",
    longDesc =
"""
top site with 2 metal adatoms on 211 surface.
""",
)




