# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:52:33 2017

@author: taemi
"""

import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#%%
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
        
#%%
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
        
#%%
print("XOR은 AND, NAND, OR를 조합한 다층 퍼셉트론으로 구현할 수 있다.")
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

#%%
print("XOR 0,0/ 1,0/ 0,1/ 1,1")
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
print("다층퍼셉트론을 통해 비선형 영역도 표현할 수 있다.")
print("원하는 값을 얻기위해서 매개변수로 가중치를 사용하는데 아직까진 수동으로 작")