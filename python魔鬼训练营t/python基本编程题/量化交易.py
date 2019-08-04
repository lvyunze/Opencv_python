# # *_*coding:utf-8 *_*
# import numpy as np
# import scipy as sp
# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as  plot
import pandas知识py as pd

df1 = pd.read_excel('http://pbpython.com/extras/excel-comp-data.xlsx')
print(df1['city'])
df1['category'] = pd.where(df1['total'] > 200000, 'A', 'B')
print(df1['category'])
