# $ python3 newcomer3_8.py fukunishi_data.csv

import warnings
warnings.simplefilter('ignore')

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, Descriptors, Descriptors3D
from rdkit.ML.Descriptors import MoleculeDescriptors
from RDKit_calc import RDKit_calculator

from sklearn import *
from sklearn.linear_model import *
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import lightgbm as lgb

df = pd.read_csv(sys.argv[1])
#set response variable
y = df['LogP app'].values

df_train, df_test, y_train, y_test = train_test_split(df, y, test_size=95, random_state=0)

X_train = df_train['SMILES'].values
X_test = df_test['SMILES'].values
X_train = RDKit_calculator(X_train)
X_test = RDKit_calculator(X_test)
X_train = X_train.compute_2D_desc()
X_test = X_test.compute_2D_desc()

#Standardization of explanatory variables
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

names = [
	'6',
	'7_ecfp4',
	'7_3d',
]
regression = [
	lgb.LGBMRegressor(
	boosting_type='goss',
	num_leaves=63,
	max_depth=949,
	learning_rate=0.02061442427834546,
	n_estimators=382,
	min_child_weight=9.93246483600419e-08,
	min_child_samples=10,
	reg_lambda=9.347509937659662e-08
	),
	svm.SVR(
	kernel='linear',
	gamma='auto',
	tol=0.04452423351599806,
	C=0.0008675341299462108,
	epsilon=0.07707366424031765,
	),
	svm.SVR(
	kernel='rbf',
	gamma='auto',
	tol=1.165972163302293e-07,
	C=6.357352836096048,
	epsilon=0.6999527204922626,
	),
]
for name, reg in zip(names, regression):
	reg.fit(X_train, y_train)
	y_pred = reg.predict(X_test)
	diff = []
	for true, pred in zip(y_test, y_pred):
		diff.append(true - pred)
	diff = np.array(diff)
	data = np.array([df_test['SMILES'].values, df_test['Assay ID'].values, diff]).T
	columns = ['SMILES', 'Assay ID', 'diff']
	newcom_df = pd.DataFrame(data=data, columns=columns)
	newcom_df.to_csv('newcomer3_{}_result.csv'.format(name))
