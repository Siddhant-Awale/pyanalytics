# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:58:45 2022

@author: siddh
"""

# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],'Second Score': [30, 45, 56, np.nan],'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
df.isnull()
df
df.fillna(0)
df.dropna()
df.isna().sum().sum() # number of NA in columns and then sum of total NA values
df.isna().sum(axis =1)# number of NA in rows
df['First Score'].isna().sum() # number of NA in a particular column

df
