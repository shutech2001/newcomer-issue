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
