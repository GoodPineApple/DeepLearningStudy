# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:02:10 2017

@author: taemi
"""

import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)
# batch 숫자 설정하기
train_size = x_train.shape[0] # 시험데이터의 형상가져오기 : 60000
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size) # 0~60000사이에서 랜덤으로 10개 숫자 뽑기
print(batch_mask)

# batch_mask(0~60000사이의 랜덤수 10개)에 맞는 인덱스만 뽑아서 batch 만들기
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)