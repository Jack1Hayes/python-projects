# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:21:03 2022

@author: Hayes

MLR
"""

import numpy as np
import pandas as pd
from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

#import data

companies = pd.read_csv(r'C:\Users\Hayes\OneDrive\Documents\Data_sets\Machine Learning Full\Linear Regression\1000_Companies.csv')

X = companies.iloc[:, :-1].values
y = companies.iloc[:, 4].values

companies.head()

#sns.heatmap(companies.corr())

#encoding data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])

from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)

#avioding dummy variable
X = X[:, 1:]

#create linear regression model

#create test data

from sklearn.model_selection import train_test_split

#split data into test and train data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred
print(regressor.coef_)
print(regressor.intercept_)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

