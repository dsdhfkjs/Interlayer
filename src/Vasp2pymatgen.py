"""Vasp2pymatgen
Python module to convert vasp format structure file
to Structure object from pymatgen.
"""

import pymatgen as mg


class Vasp2pymatgen:
    """
    This class convert vasp format structure file
    to Structure object from pymatgen.
    """
    
    @staticmethod
    def vasp2pymatgen(vasp):
        """
        Converting vasp format structure file to Structure object.
        
        Parameters
        -------
        vasp : str
            Path to vasp format strcture file, "POSCAR".
        
        Returns
        -------
        (none) : Structure object (from pymatgen)
        """
        return mg.Structure.from_str(open(vasp).read(), fmt="poscar")
