layer_Al4 = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_Al4"))
layer_NaCl = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_NaCl"))
layer_Si = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_Si"))

layer_Al4.show_irreducible_list()
layer_NaCl.show_irreducible_list()
layer_Si.show_irreducible_list()
