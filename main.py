import src
import src.Interlayer
from src.Interlayer import Interlayer
import src.Vasp2pymatgen
from src.Vasp2pymatgen import Vasp2pymatgen as v2p
import test
import test.test as te

if __name__ == "__main__":
    layer_Al4 = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_Al4"))
    layer_NaCl = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_NaCl"))
    layer_Si = Interlayer(v2p.vasp2pymatgen("test/vasp/POSCAR_Si"))

    layer_Al4.show_irreducible_list()
    layer_NaCl.show_irreducible_list()
    layer_Si.show_irreducible_list()
