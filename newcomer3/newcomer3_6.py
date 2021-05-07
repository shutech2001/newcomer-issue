# $ python3 newcomer3_6.py fukunishi_data.csv

import warnings
warnings.simplefilter('ignore')

import sys
import math
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
from sklearn.model_selection import KFold

import lightgbm as lgb
import optuna
# import optuna.integration.lightgbm as olgb

#*================================================*
#Prepare for searching hyper parameter 

def result_reg(reg):
	reg.fit(X_train, y_train)
	y_pred = reg.predict(X_test)
	print('#---------------------------------------#')
	print('RMSE : ' + str(math.sqrt(mean_squared_error(y_test, y_pred))))
	print('Q^2 : ' + str(r2_score(y_test, y_pred)))
	print('#---------------------------------------#')

def objective_Ridge(trial):
	alpha = trial.suggest_loguniform('alpha', 1e-4, 15)
	max_iter = trial.suggest_loguniform('max_iter', 1, 1000)

	reg = Ridge(alpha=alpha,
			    max_iter=max_iter)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()

def objective_BRidge(trial):
	alpha_1 = trial.suggest_loguniform('alpha_1', 1e-8, 1e-4)
	alpha_2 = trial.suggest_loguniform('alpha_2', 1e-8, 1e-4)
	lambda_1 = trial.suggest_loguniform('lambda_1', 1e-8, 1e-4)
	lambda_2 = trial.suggest_loguniform('lambda_2', 1e-8, 1e-4)
	n_iter = trial.suggest_int('n_iter', 1, 500)

	reg = BayesianRidge(alpha_1=alpha_1,
						alpha_2=alpha_2,
						lambda_1=lambda_1,
						lambda_2=lambda_2,
					    n_iter=n_iter)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()

def objective_SVR(trial):
	kernel = trial.suggest_categorical('kernel', ['linear', 'poly', 'rbf', 'sigmoid'])
	gamma = trial.suggest_categorical('gamma', ['scale', 'auto'])
	tol = trial.suggest_loguniform('tol', 1e-5, 1e-1)
	C = trial.suggest_loguniform('C', 1e-4, 10)
	epsilon = trial.suggest_loguniform('epsilon', 1e-4, 1e-1)

	reg = svm.SVR(kernel=kernel,
				  gamma=gamma,
				  tol=tol,
				  C=C,
				  epsilon=epsilon)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()

def objective_KN(trial):
	n_neighbors = trial.suggest_int('n_neighbors', 1, 15)
	weights = trial.suggest_categorical('weights', ['uniform', 'distance'])
	algorithm = trial.suggest_categorical('algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'])
	leaf_size = trial.suggest_int('leaf_size', 10, 50)

	reg = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors,
								   	    weights=weights,
									    algorithm=algorithm,
									    leaf_size=leaf_size,
									    n_jobs=-1)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()

def objective_RFR(trial):
	n_estimators = trial.suggest_int('n_estimators', 50, 200)
	max_depth = trial.suggest_int('max_depth', 100, 500)
	min_samples_split = trial.suggest_int('min_samples_split', 2, 5)
	min_samples_leaf = trial.suggest_int('min_samples_leaf', 1, 10)
	max_features = trial.suggest_categorical('max_features', ['auto', 'sqrt', 'log2'])

	reg = RFR(n_estimators=n_estimators,
			  max_depth=max_depth,
			  min_samples_split=min_samples_split,
			  min_samples_leaf=min_samples_leaf,
			  max_features=max_features,
			  n_jobs=-1,
			  random_state=0)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()


def objective_LGB(trial):
	boosting_type = trial.suggest_categorical('boosting_type', ['gbdt', 'goss'])
	num_leaves = trial.suggest_int('num_leaves', 30, 100)
	max_depth = trial.suggest_int('max_depth', 700, 1000)
	learning_rate = trial.suggest_loguniform('learning_rate', 5e-3, 5e-1)
	n_estimators = trial.suggest_int('n_estimators', 200, 500)
	min_child_weight = trial.suggest_loguniform('min_child_weight', 1e-8, 1e-5)
	min_child_samples = trial.suggest_int('min_child_samples', 8, 30)
	reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-9, 1e-5)

	reg = lgb.LGBMRegressor(boosting_type=boosting_type,
							num_leaves=num_leaves,
							max_depth=max_depth,
							learning_rate=learning_rate,
							n_estimators=n_estimators,
							min_child_weight=min_child_weight,
							min_child_samples=min_child_samples,
							reg_lambda=reg_lambda,
							n_jobs=-1,
							random_state=0)

	kf = KFold(n_splits=4, shuffle=True, random_state=0)
	RMSE = []
	for tr_index, val_index in kf.split(X_train, y_train):
		X_tr, X_val = X_train[tr_index], X_train[val_index]
		y_tr, y_val = y_train[tr_index], y_train[val_index]
		reg.fit(X_tr, y_tr)
		y_pr = reg.predict(X_val)
		RMSE.append(math.sqrt(mean_squared_error(y_val, y_pr)))
	return np.array(RMSE).mean()

# def lgb_cv(X, y):
# 	ds = olgb.Dataset(X, y)
# 	params = {'objective':'regression',
# 			  'metric':'rmse',
# 			  'random_seed':0}
# 	tuner = olgb.LightGBMTunerCV(params, ds, verbose_eval=-1, num_boost_round=1000, folds=KFold(n_splits=4), verbosity=-1)
# 	tuner.run()
# 	print('LightGBM : Best parameters')
# 	print(tuner.best_params)
# 	result_reg(lgb.LGBMRegressor(**tuner.best_params), X, y)

#*================================================*

df = pd.read_csv(sys.argv[1])
smiles = df['SMILES'].values
RDKit_descriptor = RDKit_calculator(smiles)

#set explanatory variables and response variable
X = RDKit_descriptor.compute_2D_desc()
y = df['LogP app'].values

#Standardization of explanatory variables
sc = StandardScaler()
X = sc.fit_transform(X)

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=95, random_state=0)

# study = optuna.create_study()
# study.optimize(objective_Ridge, n_trials=100)
# print('Ridge : Best parameters')
# print(study.best_params)
# result_reg(Ridge(**study.best_params))

# study = optuna.create_study()
# study.optimize(objective_BRidge, n_trials=100)
# print('BayesianRidge : Best parameters')
# print(study.best_params)
# result_reg(BayesianRidge(**study.best_params))

# study = optuna.create_study()
# study.optimize(objective_SVR, n_trials=100)
# print('SVR : Best parameters')
# print(study.best_params)
# result_reg(svm.SVR(**study.best_params))

# study = optuna.create_study()
# study.optimize(objective_KN, n_trials=100)
# print('KNeighborsRegressor : Best parameters')
# print(study.best_params)
# result_reg(neighbors.KNeighborsRegressor(**study.best_params))

# study = optuna.create_study()
# study.optimize(objective_RFR, n_trials=100)
# print('RFR : Best parameters')
# print(study.best_params)
# result_reg(RFR(**study.best_params))

study = optuna.create_study()
study.optimize(objective_LGB, n_trials=100)
print('LGB : Best parameters')
print(study.best_params)
result_reg(lgb.LGBMRegressor(**study.best_params))

# lgb_cv(X, y)
