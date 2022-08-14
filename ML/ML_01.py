# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:17:47 2022

@author: Hayes

"""

import numpy as np
import pandas as pd
from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

recipes = pd.read_csv('cupcakes vs muffins')
print(recipes)