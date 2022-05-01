# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-7
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)

print(np.split(A, 2, axis=1))  # 对矩阵A按照列分为两部分
print(np.split(A, 3, axis=0))  # 对矩阵A按照行分为三部分
print(np.array_split(A, 3, axis=1))  # 不均等分割

print(np.vsplit(A, 3))  # 对矩阵A横向分割
print(np.hsplit(A, 2))  # 对矩阵A纵向分割
