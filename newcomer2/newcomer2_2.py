#python3 newcomer2_2.py 1buw.pdb A

import warnings
warnings.simplefilter('ignore')

import sys
import math
import numpy as np
from Bio.PDB import *

pdb_parser = PDBParser()
structure = pdb_parser.get_structure(sys.argv[1][:3], sys.argv[1])

sum_of_coord = np.array([0., 0., 0.])
num_of_atom = 0
sum_of_square = 0

for chain in structure.get_chains():
	if(chain.id == sys.argv[2]):
		mass = [atom.mass for atom in chain.get_atoms()]
		coord = [atom.coord for atom in chain.get_atoms()]
		x_m = [(x*m, y*m, z*m) for (x,y,z), m in zip(coord, mass)]
		xx_m = sum((xm*x+ym*y+zm*z) for (xm,ym,zm), (x,y,z) in zip(x_m, coord))
		total_mass = sum(mass)
		mm = sum((sum(i)/total_mass)**2 for i in zip(*x_m))
		rg = math.sqrt(xx_m/total_mass - mm)
		print('Radius of Gyration (chain '
			+ sys.argv[2] 
			+') : '  
			+ str(rg))