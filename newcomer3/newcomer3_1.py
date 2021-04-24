# $ python3 newcomer3_1.py

from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles('C1N(C)C(=O)[C]N(C)C(=O)[C](NC(=O)[C]2CCCN2C(=O)[C](NC(=O)[C](Cc2ccccc2)NC1=O)C[C](C)C)Cc1ccc(O)cc1	C[C@@](C)C')
Draw.MolToFile(mol, 'newcommer3_1.png')