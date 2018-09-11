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
        
    epsilon : float
        Threshold to c_x and c_y, if whose value is larger than
        epsilon, interlayer distance has no sence.
        
    irreducible_list : list of z-coordinates and elements
        List of reducible z-coordinates and elements
        sorted by these list elements.
        
    reducible_list : list of z-coordinates and elements
        List of reducible z-coordinates and elements
        sorted by these list elements (mainly for debug).
    """
    
    delta = 0.001
    epsilon = 0.00001
    
    def __init__(self, struct, ref_z=0.0000):
        """
        Parameters
        ----------
        Struct : Structure object (from pymatgen)
            Structure object from pymatgen,
            which has informations about atomic coordinates.
        
        ref_z : float
            Z-coordinates of reference layer, which generate
            the change of interlayer distance.
        """
        self.struct = struct
        self.__ref_z = ref_z
        
        self.__check_valid_struct()
        
        self.reducible_list = []
        self.irreducible_list = []
        
        self.__get_irreducible_list()
    
    def __get_irreducible_list(self):
        """
        Getting irreducible list from pymatgen format structural data.

        """
        self.__get_reducible_list()
        self.__shift_ref_z()
        
        pre_site = None
        for site in self.reducible_list:
            if pre_site is None:
                sum = site[0]
                nsites = 1
                pre_site = site
            else:
                if (
                    abs(site[0] - pre_site[0]) < self.delta and
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
        
        # sort by z-coordinates
        self.irreducible_list.sort(key=itemgetter(0))
    
    def show_irreducible_list(self):
        print("z\telement")
        for site in self.irreducible_list:
            print(str(site[0]) + "\t" + str(site[1])
            )
    
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
    
    def __shift_ref_z(self):
        """
        Shifting ref_z to the center of layer.
        """
        for site in self.reducible_list:
            site[0] -= self.__ref_z
            if abs(site[0]) > self.struct.lattice.matrix[2][2] / 2:
                site[0] -= (
                    self.struct.lattice.matrix[2][2] 
                    * (site[0] / abs(site[0]))
                )
    
    def __check_valid_struct(self):
        """
        Checking whether struct is valid.
        
        If the value of x or y of lattice vector c is not 0,
        interlayer distance has no sence to consider in normal situation.
        """
        assert abs(self.struct.lattice.matrix[2][0]) < self.epsilon and \
               abs(self.struct.lattice.matrix[2][1]) < self.epsilon, \
               "ERROR: c_x or c_y is larger than epsilon."
    

if __name__ == "__main__":
    #layer_assert = Interlayer(v2p.vasp2pymatgen("../test/vasp/POSCAR_assert"))
    
    layer_Al4 = Interlayer(v2p.vasp2pymatgen("../test/vasp/POSCAR_Al4"))
    layer_NaCl = Interlayer(v2p.vasp2pymatgen("../test/vasp/POSCAR_NaCl"))
    layer_Si = Interlayer(v2p.vasp2pymatgen("../test/vasp/POSCAR_Si"))
    print(layer_Si.irreducible_list)
    layer_Al4.show_irreducible_list()
    layer_NaCl.show_irreducible_list()
    layer_Si.show_irreducible_list()
