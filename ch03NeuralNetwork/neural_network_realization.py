# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:50:59 2017

@author: taemi
"""
import numpy as np

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))
    
#%%

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]]) # 배열 중간에 <,>가 있어야 컴파일됨
    network['b1'] = np.array([0.1,0.2,0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])
    
    return network
    
#%%

def identity_function(x):
    return x

#%%

def forward(network, x): # 순전파를 forward라고 함 <=> 역전파
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    #y = identity_function(a3)  identity_function은 출력층에대해 아무런 기능이 없음
    y = softmax(a3)  # 출력층에서 softmax 적용 / classification에서 주로 사
    
    return y
    
#%%

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a -c) #오버플로 대책 : 입력신호 중 최댓값을 빼준다.
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
#%%

network = init_network() # 딕셔너리 변수
x = np.array([1.0,0.5])
y = forward(network,x)
print(y)
