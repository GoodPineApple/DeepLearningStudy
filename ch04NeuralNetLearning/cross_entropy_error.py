# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:55:03 2017

@author: taemi
"""

#CEE(Cross Entropy Error 교차엔트로피 오차)

import numpy as np

def cross_entropy_error(y,t) :
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))  # ????????
    
#%%

#정답은 '2'
t = [0,0,1,0,0,0,0,0,0,0]

# 예1 : '2'일 확률이 가장 높다고 추정함(0.6)
y1 = [0.1,0.05,0.6,0,0.05,0.1,0,0.1,0,0]

# 예2 : '7'일 확률이 가장 높다고 추정함(0.6)
y2 = [0.1,0.05,0,0.05,0.1,0,0.6,0.1,0,0]

print("y1의오차 : "+str(cross_entropy_error(np.array(y1),np.array(t))))
print("y2의오차 : "+str(cross_entropy_error(np.array(y2),np.array(t))))
print("'2'일 확률이 높다고 추정한 y1의 오차가 '7'일 확률이 높다고 추정한 y2의 오차보다 낮으므로 답은 '2'라고 추정함")