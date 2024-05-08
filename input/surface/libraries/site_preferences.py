name = "Metal Binding Energies"
shortDesc = ""
longDesc = """

generalized coordination numbers first postulated by Calle-Vallejo et al. in 
"Fast Prediction of Adsorption Properties for Platinum Nanocatalysts with Generalized 
Coordination Numbers", 2014 doi: 10.1002/anie.201402958

subsequent use for advanced scaling relations from Gao et al. in "Determining the 
adsorption energies of small molecules with the intrinsic properties of adsorbates 
and substrates", 2020, doi: 10.1038/s41467-020-14969-8

this is a simple decision tree for picking the preferred binding site for a species
"""

# sites: hollow: 
entry(
    index = 0,
    label = "111_fcc_hollow",
    adjacency_list = """
1 X u0 p0
2 X u0 p0
3 X u0 p0
""",
    facet = "111",
    site = "111_fcc_hollow",
    coordination_number = 6.955,
    metal_atoms = 3,
    shortDesc = """111 fcc hollow""",
    longDesc = 
""" 
""",
)

tree(
"""
L1: R*
    L2: R*bidentate
        L3: C*C*
            L4: C-*C-*
            L4: C=*RC=*R
            L4: C-*R2C-*R2
            L4: C-*R2C=*R
            L4: C-*RC=*
        L3: C*N*
            L4: C-*R2N=*
            L4: C-*R2N-*R
            L4: C=*N-*
            L4: C=*RN=*
            L4: C=*RN-*R
        L3: C*O*
            L4: C=*RO-*
            L4: C-*R2O-*
        L3: N*N*
            L4: N-*RN-*R
            L4: N-*RN=*
        L3: N*O*
            L4: N=*O-*
        L3: O*O*
    L2: R*single_chemisorbed
        L3: C*
            L4: Cq*
            L4: C#*R
                L5: C#*CR3
                L5: C#*NR2
                L5: C#*OR
            L4: C=*R2
                L5: C=*RCR3
                L5: C=*RNR2
                L5: C=*ROR
            L4: C=*(=R)
                L5: C=*(=C)
                L5: C=*(=NR)
            L4: C-*R3
                L5: C-*R2CR3
                L5: C-*R2NR2
                L5: C-*R2OR
                L5: C-*RNR
                L5: C-*RO
        L3: N*
            L4: N#*
            L4: N=*R
                L5: N=*CR3
                L5: N=*NR2
                L5: N=*OR
            L4: N-*R2
                L5: N-*RCR3
                L5: N-*RNR2
                L5: N-*ROR
                L5: N-*CR2
                L5: N-*NR
                L5: N-*O
        L3: O*
            L4: O=*
            L4: O-*R
                L5: O-*CR3
                L5: O-*NR2
                L5: O-*OR
    L2: R*vdW
        L3: (CR4)*
            L4: (CR3CR3)*
            L4: (CR3NR2)*
            L4: (CR3OR)*
        L3: (CR3)*
            L4: (CR2NR)*
            L4: (CR2CR)*
            L4: (CR2O)*
        L3: (CR2)*
            L4: (CRN)*
            L4: (CRCR)*
        L3: (NR3)*
            L4: (NR2NR2)*
            L4: (NR2OR)*
        L3: (N=[O,N]R)*
            L4: (NRO)*
            L4: (NRNR)*
        L3: (OR2)*
            L4: (OROR)*
""",
)