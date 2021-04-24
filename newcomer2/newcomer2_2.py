#python3 newcomer2_2.py 1buw.pdb A

import warnings
warnings.simplefilter('ignore')

import sys
import numpy as np
from Bio.PDB import *

pdb_parser = PDBParser()
structure = pdb_parser.get_structure(sys.argv[1][:3], sys.argv[1])

sum_of_coord = np.array([0., 0., 0.])
num_of_atom = 0
sum_of_square = 0

for chain in structure.get_chains():
	if(chain.id == sys.argv[2]):
		for atom in chain.get_atoms():
			sum_of_coord += np.array(atom.coord)
			num_of_atom += 1
		center = sum_of_coord / num_of_atom
		print('center : ' + str(center))
		for atom in chain.get_atoms():
			sum_of_square += np.sum((np.array(atom.coord) - center) ** 2)
		print('Radius of Gyration (chain '
			+ sys.argv[2] 
			+') : '  
			+ str(np.sqrt(sum_of_square / num_of_atom)))