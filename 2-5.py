# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-5
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

A = np.arange(3, 15).reshape((3, 4))
print(A)
# print(A[2][1])
# print(A[2, 1])  # 打印第二行第一列的数
# print(A[2, :])  # 打印第二行所有数
# print(A[2, 1:3])  # 打印第二行第一个数到第二个数

# 打印每一行
for row in A:
    print(row)

# 打印每一列
for column in A.T:
    print(column)

print(A.flatten())
# 迭代每一个项
for item in A.flat:
    print(item)
