# $ python3 newcomer3_3.py fukunishi_data.csv

import sys
import numpy as np
import pandas as pd
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

class RDKit_calculator:
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
		desc_vector = tmp_df.values
		print(desc_vector)

	def compute_ECFP4(self):
		ecfp4_data = []
		ecfp4 = [AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048) for mol in self.mols]
		for fp in ecfp4:
			arr = np.zeros((1,))
			DataStructs.ConvertToNumpyArray(fp, arr)
			ecfp4_data.append(arr)
		tmp_df = pd.DataFrame(ecfp4_data)
		ecfp4_vector = tmp_df.values
		print(ecfp4_vector)

df = pd.read_csv(sys.argv[1])
test_smiles = df['SMILES'][:5].values
RDKit_descriptor = RDKit_calculator(test_smiles)
X = RDKit_descriptor.compute_ECFP4()
