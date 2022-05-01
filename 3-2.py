# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     3-2
   Description :
   Author :       Jamerri
   date：          2022/5/2
-------------------------------------------------
   Change Activity:
                   2022/5/2:
-------------------------------------------------
"""

import pandas as pd
import numpy as np

dates = pd.date_range('20220502', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)

# 打印某一列
print(df['A'], df.A)

# 选择一定的行内容
print(df[0: 3], df['20220502': '20220504'])

# select by label: loc
print(df.loc['20220502'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20220502', ['A', 'B']])

# select by position: iloc
print(df.iloc[3])  # 打印第三行
print(df.iloc[3, 1])  # 打印第三行第一位
print(df.iloc[3: 5, 1: 3])  # 打印第三行到第五行第一位到第三位
print(df.iloc[[1, 3, 5], 1: 3])  # 打印第一行第三行第五行第一位到第三位

# 已经弃用ix
# mixed selection: ix
# print(df.ix[:3, ['A', 'C']])

# Boolean indexing
print(df[df.A > 8])