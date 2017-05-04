# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:43:24 2017

@author: taemi
"""

import numpy as np
import matplotlib.pyplot as plt

def relu_function(x):
    return np.maximum(0,x)  # 0이하는 0으로 표시, 그 이상은 입력값을 출력
    
#%%
x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)
plt.plot(x,y)
plt.ylim(-0.1, 5.0)  # y축 범위 지정
plt.show()