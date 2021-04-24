# $ python3 newcomer3_2.py fukunishi_data.csv

import sys
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

class RDKit_2D_descriptors:
	def __init__(self, smiles):
		self.mols = [Chem.MolFromSmiles(i) for i in smiles]
		self.smiles = smiles

	def compute_2D_desc(self):
		desc_2d = []
		calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors.descList])
		header = calc.GetDescriptorNames()
		for i in range(len(self.mols)):
			ds = calc.CalcDescriptors(self.mols[i])
			desc_2d.append(ds)
		tmp_df = pd.DataFrame(desc_2d, columns=header)
		# tmp_df.insert(loc=0, column='smiles', value=self.smiles)
		desc_vector = tmp_df.values
		print(desc_vector)

df = pd.read_csv(sys.argv[1])
test_smiles = df['SMILES'][:5].values
RDKit_descriptor = RDKit_2D_descriptors(test_smiles)
RDKit_descriptor.compute_2D_desc()