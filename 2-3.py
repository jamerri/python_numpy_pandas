# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-3
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
#
# # c = a - b
# # c = 10 * np.sin(a)
# # print(c)
# print(b)
# # print(b < 3)
# print(b == 3)

# a = np.array([[1, 1],
#               [0, 1]])
# b = np.arange(4).reshape((2, 2))
#
# c = a * b  # 每个元素相乘
# c_dot = np.dot(a, b)  # 矩阵相乘
# c_dot_2 = a.dot(b)
#
# print(c)
# print(c_dot)
# print(c_dot_2)

a = np.random.random((2, 4))

print(a)
# print(np.sum(a))
print(np.sum(a, axis=1))  # axis=1是指每一行 axis=0是指每一列
# print(np.min(a))
print(np.min(a, axis=0))
# print(np.max(a))
print(np.max(a, axis=1))