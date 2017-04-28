# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:37:33 2017

@author: taemi
"""

import numpy as np

X = np.array([[51,55],
              [14,19],
              [0,4]])
print(X)

print("X[0] : ")
print(X[0])
print("X[0][1] : ")
print(X[0][1])

print("for row in X")
for row in X:
    print(row)
    
print()
X = X.flatten()
print("X = X.flatten() - 1차원 배열로 변환, 여전히 numpy임")
print(X)

print("X[np.array([0,2,4])] - 인덱스가 0,2,4인 원소얻기")
print(X[np.array([0,2,4])])
print("X[0,2,4]")
print()
print("15이상인 값만 구하기")
print("X>15")
print(X>15)
print("X[X>=15]")
print(X[X>=15])

