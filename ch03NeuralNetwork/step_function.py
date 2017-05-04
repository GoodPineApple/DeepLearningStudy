# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:01:05 2017

@author: taemi
"""

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x>0, dtype=np.int)  # 비교연산자 계산하여 true/false. dtype을 1/0으로
    
#%%
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)  # y축 범위 지정
plt.show()