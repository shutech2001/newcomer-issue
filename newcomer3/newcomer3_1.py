# $ python3 newcomer3_1.py

from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles('COc1ccc(Cl)cc1Cc1c[nH]c2c1cc(C(=O)Nc1nc(CC(=O)[O-])cs1)cc2')
Draw.MolToFile(mol, 'in.png')