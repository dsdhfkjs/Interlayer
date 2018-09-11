"""Interlayer.py

Python module to calculate interlayer distance.

In this module, we make the irreducible z-coordinate list
from the pymatgen format structural data.

"""

from operator import itemgetter

import pymatgen as mg
from Vasp2pymatgen import Vasp2pymatgen as v2p


class Interlayer:
    """
    This class calculate interlayer distance.
    
    Attributes
    ----------
    delta : float
        Calculation threshold to z-coordinates difference.
        
    irreducible_list : list of z-coordinates and elements
        List of reducible z-coordinates and elements
        sorted by these list elements.
        
    reducible_list : list of z-coordinates and elements
        List of reducible z-coordinates and elements
        sorted by these list elements (mainly for debug).
    """
    
    delta = 0.001
    
    def __init__(self, struct):
        """
        Parameters
        ----------
        Struct : Structure object (from pymatgen)
            Structure object from pymatgen,
            which has informations about atomic coordinates.
        """
        self.struct = struct
        self.reducible_list = []
        self.irreducible_list = []
        self.__get_irreducible_list()
    
    def __get_irreducible_list(self):
        """
        Getting irreducible list from pymatgen format structural data.

        """
        self.__get_reducible_list()
        
        pre_site = None
        for site in self.reducible_list:
            if pre_site is None:
                sum = site[0]
                nsites = 1
                pre_site = site
            else:
                if (
                    site[0] - pre_site[0] < self.delta and
                    site[1] is pre_site[1]
                ):
                    sum += site[0]
                    nsites += 1
                    pre_site = site
                else:
                    self.irreducible_list.append([sum/nsites, pre_site[1]])
                    sum = site[0]
                    nsites = 1
                    pre_site = site
        self.irreducible_list.append([sum/nsites, pre_site[1]])
    
    def __get_reducible_list(self):
        """
        Getting reducible list from pymatgen format structural data.
        """
        for site in range(len(self.struct)):
            self.reducible_list.append([self.struct.cart_coords[site][2],
                                        self.struct.species[site]])
        
        # sort by z-coordinates
        self.reducible_list.sort(key=itemgetter(0))
        
        # sort by elements
        self.reducible_list.sort(key=itemgetter(1))

if __name__ == "__main__":
    print(Interlayer(v2p.vasp2pymatgen(
        "../test/vasp/POSCAR_Al4"
    )).reducible_list)
    print(Interlayer(v2p.vasp2pymatgen(
        "../test/vasp/POSCAR_NaCl"
    )).reducible_list)
    print(Interlayer(v2p.vasp2pymatgen(
        "../test/vasp/POSCAR_Al4"
    )).irreducible_list)
    print(Interlayer(v2p.vasp2pymatgen(
        "../test/vasp/POSCAR_NaCl"
    )).irreducible_list)

