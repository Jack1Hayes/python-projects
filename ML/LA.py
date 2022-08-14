# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:35:09 2022

@author: Hayes

Linear Algebra
"""
import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt

data = pd.read_csv('SocialNetworkAds.csv')
data.head()

X = data.iloc[:, [2,3]].values
y = data.iloc[:, 4].values

#spliting data

from sklearn.model_selection import train_test_split
X_train, X_test, y_test, y_train = train_test_split(X, y, test_size = 0.25, random_state = 0)

# feature caling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# fitting to NAive bayes training set

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm
