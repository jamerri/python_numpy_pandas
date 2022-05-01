# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     3-3
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

df.iloc[2, 2] = 1111
df.loc['20220502', 'B'] = 2222
# df[df.A > 4] = 0
df.B[df.A > 4] = 0
df['F'] = np.nan
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20220502', periods=6))
print(df)