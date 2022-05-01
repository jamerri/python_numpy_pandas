# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-4
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

A = np.arange(2, 14).reshape((3, 4))

print(np.argmin(A))  # 矩阵A最小值的序号
print(np.argmax(A))  # 矩阵A最大值的序号
print(np.mean(A))  # 矩阵A的平均值
print(A.mean())  # 矩阵A的平均值
print(np.average(A))  # 矩阵A的平均值
print(np.median(A))  # 矩阵A的中位数
print(A)
print(np.cumsum(A))  # 矩阵A各元素依次累加
print(np.diff(A))  # 矩阵A各元素两两相减
print(np.nonzero(A))  # 矩阵A非零元素
print(np.sort(A))  # 矩阵A排序
print(np.transpose(A))  # 矩阵A的转置
print(np.clip(A, 5, 9))  # 矩阵A中所有小于5的数都变为5，所有大于9的数都变为9
print(np.mean(A, axis=0))  # 矩阵A每一列的平均值
print(np.mean(A, axis=1))  # 矩阵A每一行的平均值

