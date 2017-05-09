# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:42:29 2017

@author: taemi
"""

#MSE(Mean Squared Error 평균제곱오차)

import numpy as np

def mean_squared_error(y,t) :
    return 0.5 * np.sum((y-t)**2)  # 정답과 추정값 사이의 차를 제곱하여 모두 더함
    
#%%

#정답은 '2'
t = [0,0,1,0,0,0,0,0,0,0]

# 예1 : '2'일 확률이 가장 높다고 추정함(0.6)
y1 = [0.1,0.05,0.6,0,0.05,0.1,0,0.1,0,0]

# 예2 : '7'일 확률이 가장 높다고 추정함(0.6)
y2 = [0.1,0.05,0,0.05,0.1,0,0.6,0.1,0,0]

print("y1의오차 : "+str(mean_squared_error(np.array(y1),np.array(t))))
print("y2의오차 : "+str(mean_squared_error(np.array(y2),np.array(t))))
print("'2'일 확률이 높다고 추정한 y1의 오차가 '7'일 확률이 높다고 추정한 y2의 오차보다 낮으므로 답은 '2'라고 추정함")
