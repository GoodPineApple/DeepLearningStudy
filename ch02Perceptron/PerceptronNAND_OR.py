# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:26:04 2017

@author: taemi
"""
import numpy as np

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
print("NAND 0,0/ 1,0/ 0,1/ 1,1")
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))
print("OR 0,0/ 1,0/ 0,1/ 1,1")
print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))
print("AND,NAND,OR는 모두 같은 구조의 퍼셉트론, 차이는 가중치 매개변수의 값뿐임.")
print("실제로 위의 코드들은 가중치와 편향값만 다르게 설정했다.")