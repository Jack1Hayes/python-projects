# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:40:03 2022

@author: Hayes

Linear regression
"""

import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

data = pd.read_csv('data_(1)_(dataset_for_logistic).csv')
#data.head()

#sns.jointplot(x = 'radius_mean', y = 'texture_mean',data = data)

#sns.heatmap(data.corr())

#data.isnull().sum()

X = data[['radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst']]
y = data['diagnosis']

#create test data

from sklearn.model_selection import train_test_split

#split data into test and train data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

#create model

from sklearn.linear_model import LogisticRegression

logMogel = LogisticRegression()

logMogel.fit(X_train, y_train)

y_pred = logMogel.predict(X_test)

print(y_pred)

#how good is model

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))