# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-6
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

# A = np.array([1, 1, 1])
# B = np.array([2, 2, 2])
#
# C = np.vstack((A, B))  # vertical stack
# D = np.hstack((A, B))  # horizontal stack
# print(D)
# print(A.shape, C.shape)
# print(A.shape, D.shape)
#
# print(A[np.newaxis, :])  # 矩阵A加一个维度
# print(A[:, np.newaxis])  # 矩阵A加一个纵向维度

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.concatenate((A, B, B, A), axis=0)
print(C)
