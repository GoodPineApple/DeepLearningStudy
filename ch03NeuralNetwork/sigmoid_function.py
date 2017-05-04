# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:39:28 2017

@author: taemi
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))
    
#%%
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)  # y축 범위 지정
plt.show()