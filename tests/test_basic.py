# -*- coding: utf-8 -*-

from .context import src
from src.Interlayer import Interlayer
from src.Vasp2pymatgen import Vasp2pymatgen as v2p

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True
    
    def test_basic(self):
        layer_Al4 = Interlayer(v2p.vasp2pymatgen("tests/vasp/POSCAR_Al4"))
        layer_NaCl = Interlayer(v2p.vasp2pymatgen("tests/vasp/POSCAR_NaCl"))
        layer_Si = Interlayer(v2p.vasp2pymatgen("tests/vasp/POSCAR_Si"))
        
        layer_Al4.show_irreducible_list()
        layer_NaCl.show_irreducible_list()
        layer_Si.show_irreducible_list()


if __name__ == '__main__':
    unittest.main()