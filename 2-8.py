# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2-8
   Description :
   Author :       Jamerri
   date：          2022/5/1
-------------------------------------------------
   Change Activity:
                   2022/5/1:
-------------------------------------------------
"""

import numpy as np

a = np.arange(4)
print(a)

a[0] = 11

b = a
c = a
d = b
print(b)
print(c)
print(d)

b = a.copy()  # deep copy
a[2] = 33
print(a)
print(b)