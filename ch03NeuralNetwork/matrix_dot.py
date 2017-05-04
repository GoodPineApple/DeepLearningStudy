# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:50:33 2017

@author: taemi
"""

import numpy as np

A = np.array([[1,2],[3,4]])
print("A의 차원")
print(np.ndim(A))
print("A의 모양")
print(np.shape(A))

B = np.array([[5,6,7],[8,9,10]])
print("B의 차원")
print(np.ndim(B))
print("B의 모양")
print(np.shape(B))
print()
print("2x2행렬과 2x3행렬의 내적")
print(np.dot(A,B))  # 2x3행렬로 계산