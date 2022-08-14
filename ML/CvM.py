# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:17:47 2022

@author: Hayes

Support vector Machine
"""

import numpy as np
import pandas as pd
from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

recipes = pd.read_csv(r'C:\Users\Hayes\OneDrive\Documents\Python Scripts\ML\Cupcakes_vs_Muffins.csv')
print(recipes)

#sns.lmplot(x = 'Flour', y = 'Sugar', data = recipes, hue = 'Type',
#            palette = 'Set1', fit_reg=False, scatter_kws = {'s':70});

# format or pre process data

type_label = np.where(recipes['Type'] == 'Muffin', 0, 1)
recipe_features = recipes.columns.values[1:].tolist()
recipe_features
Ingredients = recipes[['Flour', 'Sugar']].values
print(Ingredients)

#fit model

model = svm.SVC(kernel='linear')
model.fit(Ingredients, type_label)

#get the serperating hyperplane

w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30, 60)
yy = a * xx - (model.intercept_[0]/w[1])

# plot parallells

b = model.support_vectors_[0]
yy_down = a*xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a* xx + (b[1] - a * b[0])

sns.lmplot(x = 'Flour', y = 'Sugar', data = recipes, hue = 'Type',
            palette = 'Set1', fit_reg=False, scatter_kws = {'s':70})

plt.plot(xx, yy, linewidth = 2, color = 'black')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

#create muffin or cupcake function

def muffin_or_cupcake(Flour, Sugar):
    if (model.predict([[Flour, Sugar]])) == 0:
        print('Muffin recipe')
    else:
        print('cupcake recipe')
        
muffin_or_cupcake(50, 20)