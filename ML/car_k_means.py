# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:30:30 2022

@author: Hayes

K means Clustering
"""

import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt

#importing data

dataset = pd.read_csv('cars_(dataset_for_k_means).csv')

X = dataset[dataset.columns[:-1]]
X = X._convert(numeric = True)
X.head()


# elinate Null values

for i in X.columns:
    X[i] = X[i].fillna(int(X[i].mean()))
for i in X.columns:
    print(X[i].isnull().sum())
    
#start using elbow method to find optimal number of clusters

from sklearn.cluster import KMeans

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init='k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
#plt.plot(range(1, 11), wcss)
#plt.title('Elbow Method')
#plt.xlabel('# clusters')
#plt.ylabel('wcss')
#plt.show()

#Apply k-means to the cars dataset

kmeans = KMeans(n_clusters = 3, init='k-means++', max_iter = 300, n_init = 10, random_state = 0)

y_kmeans = kmeans.fit_predict(X)
X = X.values

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1], s = 100, c = 'red', label = 'Toyota')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1], s = 100, c = 'blue', label = 'Nisan')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1], s = 100, c = 'green', label = 'Honda')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow' , label = 'centroids')

plt.show()