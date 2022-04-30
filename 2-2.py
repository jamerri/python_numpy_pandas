# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-2
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

a = np.array([[2, 3, 4],
              [2, 3, 4]])
# print(a)

a = np.zeros((3, 4))
# print(a)

a = np.ones((3, 4), dtype=np.int16)
# print(a)

a = np.empty((3, 4), dtype=np.float32)
# print(a)

a = np.arange(10, 20, 2)
# print(a)

a = np.arange(12).reshape((3, 4))
# print(a)

a = np.linspace(1, 10, 6).reshape((2, 3))
print(a)