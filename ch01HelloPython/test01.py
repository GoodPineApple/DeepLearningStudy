# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def array_left_rotation(a, n, k):
    alist = list(a)
    print (alist)
    b = alist[k:]+alist[:k]
    return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')