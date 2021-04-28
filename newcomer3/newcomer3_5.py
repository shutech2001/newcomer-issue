# $ python3 newcomer3_5.py fukunishi_data.csv

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
smiles = df['SMILES'].values
RDKit_descriptor = RDKit_calculator(smiles)

#set explanatory variables and response variable
X = RDKit_descriptor.compute_2D_desc()
y = df['LogP app'].values

#Standardization of explanatory variables
sc = StandardScaler()
X = sc.fit_transform(X)

#split to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=95, random_state=0)

names = [
	'Linear Regression',
	'Ridge Regression',
	'Bayesian ridge Regression',
	'Support Vector Regression',
	'Nearest Neighbors Regression',
	'Random Forest Regression',
	'LightGBM Regression'
]

regression = [
	LinearRegression(),
	Ridge(alpha=0.1),
	BayesianRidge(),
	svm.SVR(),
	neighbors.KNeighborsRegressor(),
	RFR(n_jobs=-1, random_state=0),
	lgb.LGBMRegressor()
]

for name, reg in zip(names, regression):
	reg.fit(X_train, y_train)
	y_pred = reg.predict(X_test)
	print(name)
	print('#---------------------------------------#')
	print('MSE   : ' + str(mean_squared_error(y_test, y_pred)))
	print('R^2   : ' + str(r2_score(y_test, y_pred)))
	print('#---------------------------------------#')

