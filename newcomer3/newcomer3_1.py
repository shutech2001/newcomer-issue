# $ python3 newcomer3_1.py

from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles('c1(C(=O)OC)c(C(=O)OC)cccc')
Draw.MolToFile(mol, 'newcomer3_7_ecfp4_out/21.png')